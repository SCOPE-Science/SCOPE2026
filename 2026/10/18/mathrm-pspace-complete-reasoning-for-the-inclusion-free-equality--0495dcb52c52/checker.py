#!/usr/bin/env python3
"""Finite comparison of ordinary weak team semantics with a symbolic equality–constancy evaluator."""
from itertools import product
from random import Random
import argparse


def concrete(node, q, columns, team):
    op=node[0]
    if op=='eq':
        i,j=columns.index(node[1]),columns.index(node[2])
        return all(row[i]==row[j] for row in team)
    if op=='not':
        return len(team)==0 or not concrete(node[1],q,columns,team)
    if op=='and':return concrete(node[1],q,columns,team) and concrete(node[2],q,columns,team)
    if op=='or':return concrete(node[1],q,columns,team) or concrete(node[2],q,columns,team)
    if op in ('exists','forall'):
        trials=[concrete(node[2],q,columns+(node[1],),tuple(row+(a,) for row in team)) for a in range(q)]
        return any(trials) if op=='exists' else all(trials)
    raise ValueError(op)

def signature(cols, team):
    signatures=[tuple(row[j] for row in team) for j in range(len(cols))]
    uniques=[];labels=[]; const=[]
    for s in signatures:
        if s not in uniques:
            uniques.append(s)
            const.append(len(set(s))<=1)
        labels.append(uniques.index(s))
    return tuple(labels),tuple(const)

def symbolic(node,q,cols,labels,const):
    op=node[0]
    if op=='eq':return labels[cols.index(node[1])]==labels[cols.index(node[2])]
    if op=='not':return not symbolic(node[1],q,cols,labels,const)
    if op=='and':return symbolic(node[1],q,cols,labels,const) and symbolic(node[2],q,cols,labels,const)
    if op=='or':return symbolic(node[1],q,cols,labels,const) or symbolic(node[2],q,cols,labels,const)
    if op in ('exists','forall'):
        options=[j for j,c in enumerate(const) if c]
        if len(options)<q:options.append(len(const))
        res=[]
        for choice in options:
            fresh=choice==len(const)
            nconst=const+(True,) if fresh else const
            nlabels=labels+(choice,)
            res.append(symbolic(node[2],q,cols+(node[1],),nlabels,nconst))
        return any(res) if op=='exists' else all(res)
    raise ValueError(op)

def randformula(rng, depth,scope,nextvar):
    if depth==0 or rng.randrange(5)==0:
        u=rng.choice(scope);v=rng.choice(scope)
        return ('eq',u,v),nextvar
    op=rng.choice(('not','and','or','exists','forall'))
    if op=='not':
        inner,n=randformula(rng,depth-1,scope,nextvar)
        return ('not',inner),n
    if op in ('and','or'):
        l,n=randformula(rng,depth-1,scope,nextvar)
        r,n=randformula(rng,depth-1,scope,n)
        return (op,l,r),n
    name='z'+str(nextvar)
    child,n=randformula(rng,depth-1,scope+(name,),nextvar+1)
    return (op,name,child),n

def run():
    rng=Random(960915216)
    cases=0; formulas=0
    for q in (1,2,3):
        for k in (1,2):
            cols=tuple('x'+str(i) for i in range(k))
            assignments=list(product(range(q), repeat=k))
            teams=[tuple(assignments[j] for j in range(len(assignments)) if mask>>j&1) for mask in range(1,1<<len(assignments))]
            fs=[randformula(rng,4,cols,0)[0] for _ in range(35)]
            formulas+=len(fs)
            for f in fs:
                for team in teams:
                    labels,const=signature(cols,team)
                    a=concrete(f,q,cols,team)
                    b=symbolic(f,q,cols,labels,const)
                    cases+=1
                    assert a==b,(q,k,f,team,labels,const,a,b)
    # QBF reduction smoke test: forall u exists v (u==v) is true; exists u forall v (u==v) is false over q=2.
    q=2
    true=('forall','u',('exists','v',('eq','u','v')))
    false=('exists','u',('forall','v',('eq','u','v')))
    assert concrete(true,q,(),((),))
    assert not concrete(false,q,(),((),))
    # Size cutoff: syntactic q>>variables cannot affect any formula with few bound variables.
    for k in (1,2,3):
        cols=tuple('x'+str(i) for i in range(k))
        for z in range(70):
            f,_=randformula(rng,5,cols,0)
            signature0=tuple(range(k))
            mark=tuple(bool(z>>i&1) for i in range(k))
            v0=symbolic(f,k+7,cols,signature0,mark)
            v1=symbolic(f,k+12,cols,signature0,mark)
            assert v0==v1,(f,k,mark,v0,v1)
    print('VERIFY_OK finite_team_symbolic_comparisons', cases, 'formulas', formulas)

if __name__=='__main__':run()

# Separate translation test of the quantitative-Boolean-formula lower bound.
def translate_qbf(prefix,body):
    def tf(node):
        if node[0]=='lit':
            return ('eq',node[1],'a') if node[2] else ('eq',node[1],'b')
        if node[0]=='not':return ('not',tf(node[1]))
        if node[0] in ('and','or'):return (node[0],tf(node[1]),tf(node[2]))
        raise ValueError(node)
    f=tf(body)
    for quant,var in reversed(prefix): f=(quant,var,f)
    return f

def qbf_truth(prefix,body):
    def val(node,env):
        if node[0]=='lit':return env[node[1]]==node[2]
        if node[0]=='not':return not val(node[1],env)
        if node[0]=='and':return val(node[1],env) and val(node[2],env)
        if node[0]=='or':return val(node[1],env) or val(node[2],env)
        raise ValueError(node)
    def prefix_rec(pos,env):
        if pos==len(prefix):return val(body,env)
        op,var=prefix[pos]
        results=[]
        for a in (False,True):
            env[var]=a
            results.append(prefix_rec(pos+1,env))
        env.pop(var)
        return any(results) if op=='exists' else all(results)
    return prefix_rec(0,{})

def rnd_qbf_body(rng,scope,depth):
    if depth==0 or rng.randrange(4)==0:return ('lit',rng.choice(scope),bool(rng.randrange(2)))
    op=rng.choice(('and','or','not'))
    if op=='not':return ('not',rnd_qbf_body(rng,scope,depth-1))
    return (op,rnd_qbf_body(rng,scope,depth-1),rnd_qbf_body(rng,scope,depth-1))

def test_qbf_reduction():
    rng=Random(352006)
    two=('exists','j',('exists','k',('and',('not',('eq','j','k')),('forall','t',('or',('eq','t','j'),('eq','t','k'))))))
    for _ in range(400):
        n=rng.randrange(1,5)
        variables=tuple('u'+str(i) for i in range(n))
        prefix=tuple((rng.choice(('exists','forall')),var) for var in variables)
        body=rnd_qbf_body(rng,variables,3)
        truth=qbf_truth(prefix,body)
        enc=translate_qbf(prefix,body)
        dist=('exists','a',('exists','b',('and',('not',('eq','a','b')),enc)))
        sat=('and',two,dist)
        valid=('or',('not',two),sat)
        assert concrete(sat,2,(),((),))==truth
        for q in (1,2,3):
            assert concrete(valid,q,(),((),))==(truth or q!=2)
    print('VERIFY_OK qbf_translation_cases',400)

if __name__=='__main__':test_qbf_reduction()
