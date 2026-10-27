#!/usr/bin/env python3
"""Exact-arithmetic checks of two-edge Kirchhoff-index damages on clique bouquets."""
import itertools
import sympy as sp

m, t = sp.symbols('m t', integer=True, positive=True)
b = m + 1
c = (t - 1)*m

def one_edge(kind):
    q = 2*b + c*(m + 3 if kind == 'S' else 2)
    return sp.factor(q/(b*(b-2)))

def same_blade(kind_a, kind_b, incidence):
    z = int(bool(incidence))
    gram = sp.Matrix([[2,z],[z,2]])
    wdiag = lambda k: 2*b + c*(m+3 if k=='S' else 2)
    # Orient signs so an incident pair has Gram off-diagonal +1.
    star_inner = {'SS':m+2,'SR':1,'RR':1}[kind_a+kind_b] if incidence else 0
    h12 = (b*z + c*star_inner)
    hw = sp.Matrix([[wdiag(kind_a),h12],[h12,wdiag(kind_b)]])
    return sp.factor(sp.trace((sp.eye(2)-gram/b).inv()*hw)/b**2)

expected = {
 'SS_hub':same_blade('S','S',True),
 'SR_incident':same_blade('S','R',True),
 'SR_disjoint':same_blade('S','R',False),
 'RR_incident':same_blade('R','R',True),
 'RR_disjoint':same_blade('R','R',False),
 'SS_cross':2*one_edge('S'),
 'SR_cross':one_edge('S')+one_edge('R'),
 'RR_cross':2*one_edge('R')
}
assert sp.factor(expected['SR_disjoint']-expected['SR_cross'])==0
assert sp.factor(expected['RR_disjoint']-expected['RR_cross'])==0

# Symbolic identities provide an independently replayable sign certificate.
identities = [
 ('SS_hub','SR_incident',(m+1)*(t-1)/(m-2)),
 ('SS_hub','SS_cross',2*(m+1)*(m*(t-1)+1)/(m*(m-2)*(m-1))),
 ('SR_incident','SS_cross',-(m+1)*(m*(m-3)*(t-1)-2)/(m*(m-2)*(m-1))),
 ('SR_incident','SR_disjoint',(3*m*t-m+2)/(m*(m-2)*(m-1))),
 ('SS_cross','SR_disjoint',m*(t-1)/(m-1)),
 ('SR_disjoint','RR_incident',(m*(m*m-2*m-2)*(t-1)-2*m-2)/(m*(m-2)*(m-1))),
 ('RR_incident','RR_cross',2*(m*t+1)/(m*(m-2)*(m-1))),
 ('SR_disjoint','RR_cross',m*(t-1)/(m-1)),
]
for u,v,difference in identities:
    assert sp.cancel(expected[u]-expected[v]-difference)==0,(u,v)

# Analytic sign certificate for the only t-dependent lower ordering:
# at m=3 the numerator equals 3*t-11; at m>=4 its m=4 minimum is 14
# and it increases in each variable m,t (prove derivative in m positive for m>=4, t>=2).
num = m*(m*m-2*m-2)*(t-1)-2*m-2
assert sp.simplify(num.subs(m,3) -(3*t-11))==0
assert sp.simplify(num.subs({m:4,t:2})-14)==0
assert sp.expand(sp.diff(num,m) - ((3*m*m-4*m-2)*(t-1)-2)) == 0
assert sp.expand(sp.diff(num,t) - m*(m*m-2*m-2)) == 0


def edges(mv,tv):
    out=[]
    for j in range(tv):
        leaves=[1+j*mv+i for i in range(mv)]
        out.extend((0,v) for v in leaves)
        out.extend(itertools.combinations(leaves,2))
    return [tuple(sorted(e)) for e in out]

def key(e,f,mv):
    def typ(z):return 'S' if 0 in z else 'R'
    def blade(z):return (next(v for v in z if v !=0)-1)//mv
    a,b=typ(e),typ(f)
    kinds=''.join(sorted([a,b],reverse=True)) # 'S' precedes 'R'
    if blade(e)!=blade(f):return kinds+'_cross'
    if kinds=='SS':return 'SS_hub'
    if kinds=='SR':return 'SR_incident' if len(set(e)&set(f)) else 'SR_disjoint'
    return 'RR_incident' if len(set(e)&set(f)) else 'RR_disjoint'

def grounded_inverse(mv,tv,deleted):
    n=1+mv*tv
    L=sp.zeros(n)
    for x,y in edges(mv,tv):
        if (x,y) in deleted: continue
        L[x,x]+=1;L[y,y]+=1;L[x,y]-=1;L[y,x]-=1
    return L[1:,1:].inv()

def kirchhoff(G):
    dim=G.rows
    return (dim+1)*sum(G[i,i] for i in range(dim))-sum(G)

checks=0
for mv,tv in [(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
    ee=edges(mv,tv)
    base=kirchhoff(grounded_inverse(mv,tv,set()))
    picked={}
    for e,f in itertools.combinations(ee,2):
        k=key(e,f,mv)
        if k not in picked:picked[k]=(e,f)
    for k,(e,f) in picked.items():
        got=sp.factor(kirchhoff(grounded_inverse(mv,tv,{e,f}))-base)
        want=sp.factor(expected[k].subs({m:mv,t:tv}))
        assert got==want,(mv,tv,k,got,want)
        checks+=1
    # Check single edge increments independently.
    for k in ['S','R']:
        e=next(e for e in ee if ('S' if 0 in e else 'R')==k)
        got=sp.factor(kirchhoff(grounded_inverse(mv,tv,{e}))-base)
        assert got==sp.factor(one_edge(k).subs({m:mv,t:tv})),(mv,tv,k)
        checks+=1
    ordered=sorted(((sp.factor(v.subs({m:mv,t:tv})),k) for k,v in expected.items() if k in picked),reverse=True)
    assert ordered[0][1]=='SS_hub',(mv,tv,ordered)
    assert ordered[1][1]==('SR_incident' if mv==3 else 'SS_cross'),(mv,tv,ordered)
    print('m,t',mv,tv,'motifs',len(picked),'worst',ordered[0][1], 'runner_up',ordered[1][1])
print('VERIFY_OK',checks,'independent exact grounded inverse comparisons, symbolic sign factorizations')
