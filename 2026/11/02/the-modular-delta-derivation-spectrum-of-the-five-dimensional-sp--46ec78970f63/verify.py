#!/usr/bin/env python3
"""Exact delta-derivation pencil verification for sl_2(k) semidirect k^2.
Requires SymPy. The symbolic elimination uses only +1/-1 pivots,
so its correctness is characteristic-independent, including small primes.
"""
from itertools import combinations
import sympy as sp

z=sp.symbols('z')
b={}
def bracket(i,j,k,c):
    b[i,j,k]=c
    b[j,i,k]=-c
# h,e,f,u,v indices 0..4.
for args in [(0,1,1,2),(0,2,2,-2),(1,2,0,1),
             (0,3,3,1),(0,4,4,-1),(1,4,3,1),(2,3,4,1)]:
    bracket(*args)

def pencil(x):
    rows=[]
    for i,j in combinations(range(5),2):
        for k in range(5):
            row=[sp.Integer(0) for _ in range(25)]
            for t in range(5):
                row[5*k+t]+=b.get((i,j,t),0)
                row[5*t+i]-=x*b.get((t,j,k),0)
                row[5*t+j]-=x*b.get((i,t,k),0)
            rows.append(row)
    return sp.Matrix(rows)

def symbolically_reduce():
    A=[[sp.expand(pencil(z)[i,j]) for j in range(25)] for i in range(50)]
    remaining=list(range(25)); rowids=list(range(50)); pivots=[]
    while A and A[0]:
        nr=len(A); nc=len(A[0]);
        rcounts=[sum(x!=0 for x in row) for row in A]
        ccounts=[sum(A[i][j]!=0 for i in range(nr)) for j in range(nc)]
        choices=[(rcounts[i]*ccounts[j],i,j) for i in range(nr)
                 for j in range(nc) if A[i][j] in (1,-1)]
        if not choices: break
        _,i,j=min(choices)
        v=A[i][j]
        assert v in (1,-1)
        pivots.append((rowids[i],remaining[j],int(v)))
        pivotrow=A[i]
        new=[]; new_ids=[]
        for k in range(nr):
            if k==i: continue
            c=A[k][j]/v
            row=[sp.expand(A[k][l]-c*pivotrow[l]) for l in range(nc) if l!=j]
            if any(x!=0 for x in row):
                new.append(row);new_ids.append(rowids[k])
        A=new; rowids=new_ids; remaining.pop(j)
    return pivots,remaining,A

pivots,columns,A=symbolically_reduce()
assert len(pivots)==14
assert columns==[1,2,6,7,11,12,16,17,21,22,24]
assert len(A)==19 and all(len(row)==11 for row in A)

# The displayed reduced system in RESULT.md. Ordered exactly as in the
# deterministic row-pivot reduction above; entries are polynomial in z.
zero=sp.Integer(0)
def vec(items):
    row=[zero for _ in range(11)]
    for j,v in items.items(): row[j]=sp.expand(v)
    return row
E=[
 vec({0:-2*(z-1)*(z+1)}),
 vec({2:-2*(z*z+z-1),5:-2*z*z}),
 vec({4:2*(z+1)}),
 vec({6:-(z-1)*(z+2)}),
 vec({8:z+2}),
 vec({1:2*(z-1)*(z+1)}),
 vec({3:-2*(z+1)}),
 vec({2:2*z*z,5:2*(z*z+z-1)}),
 vec({7:-z-2}),
 vec({9:(z-1)*(z+2)}),
 vec({2:-z*(2*z-1),5:-z*z,10:-z*(z-1)}),
 vec({0:z*(z-1)}),
 vec({1:z*(z-1)}),
 vec({2:z*z,5:z*z,10:z-1}),
 vec({0:z*(z-1)}),
 vec({4:-z}),
 vec({2:-z*z,5:-z,10:-(z-1)*(z+1)}),
 vec({3:-z}),
 vec({1:-z*(z-1)}),
]
assert A==E, 'symbolic reduced matrix differs from independently typed certificate'

# Verify the equation matrix has rank 25 minus the theorem's dimension over
# a wide range of primes and every delta value in the prime field.
def rank_mod_p(x,p):
    M=pencil(sp.Integer(x))
    a=[[int(M[i,j])%p for j in range(25)] for i in range(50)]
    rank=0
    for j in range(25):
        row=next((i for i in range(rank,50) if a[i][j]),None)
        if row is None:continue
        a[row],a[rank]=a[rank],a[row]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[(w*inv)%p for w in a[rank]]
        for i in range(rank+1,50):
            if a[i][j]:
                c=a[i][j]
                a[i]=[(v-c*w)%p for v,w in zip(a[i],a[rank])]
        rank+=1
    return rank

def predicted_dimension(x,p):
    d=lambda a: int(x==a%p)
    return 2*d(1)+2*int(((x-1)*(x+2))%p==0)+2*d(-2)+(2 if x==1 else (1 if (2*x)%p==1 else 0))

for p in (3,5,7,11,13,17):
    actual=[]
    for x in range(p):
        dim=25-rank_mod_p(x,p)
        assert dim==predicted_dimension(x,p),(p,x,dim)
        if dim:actual.append((x,dim))
    print('prime',p,'nonzero_deltas',actual)

# Over Q the exceptional set is {-2,1/2,1}. Exact nullities.
for x,dim in ((sp.Integer(-2),4),(sp.Rational(1,2),1),(sp.Integer(1),6),(sp.Integer(0),0),(sp.Integer(-1),0)):
    assert 25-pencil(x).rank()==dim
print('symbolic_unit_pivots',len(pivots),'residual',len(A),'x',len(columns))
print('VERIFY_OK')
