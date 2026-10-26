"""Exact, dependency-free checks for reentrant single-monitor placement on paths.
Run: python verify.py
"""
from fractions import Fraction
from itertools import product
import json

def add(a, b):
    n = max(len(a),len(b))
    return [ (a[i] if i<len(a) else 0) + (b[i] if i<len(b) else 0) for i in range(n) ]

def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return c

def eq(a,b):
    return all(x==0 for x in sub(a,b))

w=[6,5,6,1,5]
f=[[0]*5 for _ in range(5)]
for j in range(5):
    for i in range(5): f[j][abs(i-j)] += w[i]

identities={
    'F2_minus_F0':(sub(f[2],f[0]),mul(mul(mul([0,1],[1,-1]),[1,1]),[1,5])),
    'F2_minus_F3':(sub(f[2],f[3]),mul([1,-1],[5,0,6])),
    'F2_minus_F4':(sub(f[2],f[4]),mul(mul(mul([1,-1],[1,1]),[1,2]),[1,3])),
    'F2_minus_F1':(sub(f[2],f[1]),mul([1,-1],[1,-5,5]))
}
for lhs,rhs in identities.values(): assert eq(lhs,rhs)

# Each vertex-pair gap on P4 is represented as a 4-component vector
# polynomial: components multiply arbitrary seed weights a,b,c,d.
def scalar_vec(v,a): return [[x*t for t in v] for x in a]
def add_vec(a,b):
    n=max(len(a),len(b));out=[]
    for i in range(n): out.append([ (a[i][k] if i<len(a) else 0)+(b[i][k] if i<len(b) else 0) for k in range(4)])
    return out
def mul_vec(a,b):
    n=len(a)+len(b)-1
    out=[[0]*4 for _ in range(n)]
    for i,x in enumerate(a):
        for j,v in enumerate(b):
            for k in range(4):out[i+j][k]+=x[k]*v
    return out
E=[[int(i==k) for k in range(4)] for i in range(4)]
F=[]
for j in range(4):
    poly=[[0]*4 for _ in range(4)]
    for i in range(4):
        for k in range(4): poly[abs(i-j)][k]+=E[i][k]
    F.append(poly)
V=lambda *vv:[list(t) for t in vv]
A,B,C,D=E
zero=[0]*4
M=lambda a,b:[x-y for x,y in zip(a,b)]
P4={
 (0,1):mul_vec(V(M(A,B),list(map(lambda x:-x,C)),list(map(lambda x:-x,D))),[1,-1]),
 (0,2):mul_vec(V(M(A,C),list(map(lambda x:-x,D))),[1,0,-1]),
 (0,3):mul_vec(V(M(A,D),add_vec([M(A,D)],[M(B,C)])[0],M(A,D)),[1,-1]),
 (1,2):mul_vec(V(M(B,C),M(A,D)),[1,-1]),
 (1,3):mul_vec(V(M(B,D),A),[1,0,-1]),
 (2,3):mul_vec(V(M(C,D),B,A),[1,-1]),
}
# P4 actual gaps have exactly the six factorizations listed above.
for (i,j),rhs in P4.items():
    lhs=add_vec(F[i],[[-x for x in c] for c in F[j]])
    n=max(len(lhs),len(rhs))
    for k in range(n):
        assert (lhs[k] if k<len(lhs) else zero)==(rhs[k] if k<len(rhs) else zero),(i,j,k,lhs,rhs)

configs=0
comparisons=0
wtotal=sum(w)
probability_tables={}
for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
    formula=[sum(Fraction(w[i],wtotal)*p**abs(i-j) for i in range(5)) for j in range(5)]
    enumerated=[Fraction(0) for _ in range(5)]
    for edges in product([0,1],repeat=4):
        weight=Fraction(1)
        for open_edge in edges: weight*=p if open_edge else 1-p
        for source in range(5):
            seedweight=Fraction(w[source],wtotal)
            for monitor in range(5):
                if all(edges[e] for e in range(min(source,monitor),max(source,monitor))):
                    enumerated[monitor]+=weight*seedweight
                comparisons+=1
            configs+=1
    assert formula==enumerated
    argmax=max(range(5),key=lambda i:formula[i])
    assert all(formula[argmax]>formula[j] for j in range(5) if j!=argmax)
    assert argmax=={Fraction(1,5):2,Fraction(1,2):1,Fraction(4,5):2}[p]
    probability_tables[str(p)]={'monitor_probabilities':[str(t) for t in formula],'unique_optimizer':argmax}

out={'schema_version':1,'scope':'exact path-sentinel polynomial identities and five-node edge enumeration',
     'symbolic_five_site_gap_identities':len(identities),'symbolic_four_site_pair_identities':len(P4),
     'source_edge_configurations':configs,'monitor_comparisons':comparisons,
     'source_weights':w,'source_weight_sum':wtotal,'probability_tables':probability_tables,
     'limitations':'Symbolic identities and finite example verified. Universal no-reentry inference uses the monotonicity proof in RESULT.md, not finite enumeration.'}
print(json.dumps(out,indent=2,sort_keys=True))
