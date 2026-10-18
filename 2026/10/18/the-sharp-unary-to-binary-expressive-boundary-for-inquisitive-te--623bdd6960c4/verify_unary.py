"""Finite differential checks for unary-team inquisitive logic.
Run: python3 verify_unary.py . No external dependencies.
"""
from itertools import product, combinations
from random import Random

rng=Random(260308646)

def subsets(xs):
    t=list(xs)
    for bits in product((False, True),repeat=len(t)):
        yield frozenset(x for x,b in zip(t,bits) if b)

def atom_ok(expr,assign,Ps):
    kind,a,b=expr
    if kind=='eq':return assign[a]==assign[b]
    if kind=='p':return assign[a] in Ps
    raise ValueError(kind)

def direct(f,X,D,Ps):
    op=f[0]
    if op=='atom':return all(atom_ok(f[1],dict(g),Ps) for g in X)
    if op=='bot':return not X
    if op=='and':return direct(f[1],X,D,Ps) and direct(f[2],X,D,Ps)
    if op=='or':return direct(f[1],X,D,Ps) or direct(f[2],X,D,Ps)
    if op=='imp':return all(not direct(f[1],Y,D,Ps) or direct(f[2],Y,D,Ps) for Y in subsets(X))
    if op in ('all','some'):
        tests=[direct(f[2],frozenset(tuple(sorted(dict(g,**{f[1]:d}).items())) for g in X),D,Ps) for d in D]
        return all(tests) if op=='all' else any(tests)
    raise ValueError(op)

def mso(f,R,c,D,Ps):
    op=f[0]
    if op=='atom':return all(atom_ok(f[1],dict(c, x=z),Ps) for z in R)
    if op=='bot':return not R
    if op=='and':return mso(f[1],R,c,D,Ps) and mso(f[2],R,c,D,Ps)
    if op=='or':return mso(f[1],R,c,D,Ps) or mso(f[2],R,c,D,Ps)
    if op=='imp':return all(not mso(f[1],S,c,D,Ps) or mso(f[2],S,c,D,Ps) for S in subsets(R))
    if op in ('all','some'):
        tests=[mso(f[2],R,dict(c,**{f[1]:d}),D,Ps) for d in D]
        return all(tests) if op=='all' else any(tests)
    raise ValueError(op)

# To ensure no variable capture, choose fresh names along branches.
def formula(depth, used=()):
    vars_=('x',)+used
    if depth<=0:return rng.choice([('bot',),('atom',('p',rng.choice(vars_),None)),('atom',('eq',rng.choice(vars_),rng.choice(vars_)))])
    op=rng.choice(['atom','and','or','imp','all','some'])
    if op=='atom':return formula(0,used)
    if op in ('and','or','imp'):return (op,formula(depth-1,used),formula(depth-1,used))
    y='y'+str(len(used))
    return (op,y,formula(depth-1, used+(y,)))

cases=0
for n in (1,2,3):
    D=tuple(range(n))
    for p in subsets(D):
        for R in subsets(D):
            X=frozenset((('x',z),) for z in R)
            for i in range(160):
                f=formula(3)
                a=direct(f,X,D,p)
                b=mso(f,R,{},D,p)
                if a!=b:raise AssertionError((f,R,p,a,b))
                cases+=1
# Direct witness equivalence for the negative-R FO atom and quantifiers.
for n in (1,2,3,4):
    D=tuple(range(n))
    for R in subsets(D):
        X=frozenset((('x',z),) for z in R)
        negR=('imp',('atom',('eq','x','y0')),('bot',))
        f=('some','y0',negR)
        # On nonempty teams this is the FO sentence 'exists y (not R(y))'.
        if R and direct(f,X,D,set())!=(len(R)<n):raise AssertionError((R,D))
        # On empty teams it must still hold, matching the FO sentence.
        if not R and not direct(f,X,D,set()):raise AssertionError('empty team')
print('UNARY_TEAM_VERIFY_OK',cases,'direct/MSO comparisons; negative-team test passed')
