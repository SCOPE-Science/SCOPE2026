#!/usr/bin/env python3
"""Direct syntax-and-semantics check for the two-variable separating formulas.

Finite test only: arbitrary lengths are proved in RESULT.md.
"""
from itertools import product
from functools import lru_cache


def alternate(v):return 'y' if v=='x' else 'x'
def H(k,z):
    if k==0:return ('true',)
    w=alternate(z)
    return ('ex',w,('and',('lt',w,z),H(k-1,w)))
def Rank(k,z):return ('and',H(k,z),('not',H(k+1,z)))
def Inc(a,b):return ('and',('not',('le',a,b)),('not',('le',b,a)))
def Atom(S,e,z):
    w=alternate(z)
    return ('and',Rank(1,z),
                ('ex',w,('and',Inc(z,w),Rank(S-e,w))),
                ('not',('ex',w,('and',Inc(z,w),H(S-e+1,w)))))
def Psi(S,e,k):
    return ('ex','x',('and',Rank(k,'x'),
                         ('all','y',('imp',Atom(S,e,'y'),('le','y','x')))))
def sep(S,e):return ('ex','x',Atom(S,e,'x'))

def vars_used(f):
    if isinstance(f,str):return {f}
    return set().union(*(vars_used(c) for c in f[1:]))

def eval_fo2(f,domain,env):
    op=f[0]
    if op=='true':return True
    if op=='le':return all(i<=j for i,j in zip(env[f[1]],env[f[2]]))
    if op=='lt':return env[f[1]]!=env[f[2]] and all(i<=j for i,j in zip(env[f[1]],env[f[2]]))
    if op=='and':return all(eval_fo2(g,domain,env) for g in f[1:])
    if op=='not':return not eval_fo2(f[1],domain,env)
    if op=='imp':return not eval_fo2(f[1],domain,env) or eval_fo2(f[2],domain,env)
    var,body=f[1:]
    if op=='ex':return any(eval_fo2(body,domain,env|{var:v}) for v in domain)
    if op=='all':return all(eval_fo2(body,domain,env|{var:v}) for v in domain)
    raise AssertionError(op)

def domain(exps):return list(product(*(range(e+1) for e in exps)))

def main():
    # Both examples have equal cardinality 48 and top rank 8.
    a=(5,1,1,1);b=(3,3,2)
    f=sep(8,5)
    assert vars_used(f)<={'x','y'}
    assert eval_fo2(f,domain(a),{})
    assert not eval_fo2(f,domain(b),{})
    # Same exponent support and same maximum rank, different multiplicity of exponent one.
    c=(2,2,1,1);d=(2,1,1,1,1)
    assert sum(c)==sum(d)==6
    f=Psi(6,1,2)
    assert vars_used(f)<={'x','y'}
    assert eval_fo2(f,domain(c),{})
    assert not eval_fo2(f,domain(d),{})
    print('FO2_FORMULA_MODEL_CHECK_OK')
    print('exponent_presence_pair=(5,1,1,1) vs (3,3,2): PASS')
    print('exponent_multiplicity_pair=(2,2,1,1) vs (2,1,1,1,1): PASS')
    print('syntactic_variable_set={x,y}: PASS')
if __name__=='__main__':main()
