"""Reproduce exact Taylor certificates and representative diffusion matrices."""
from fractions import Fraction
from math import comb
import numpy as np

def a(r,k):
    if k==0: return Fraction(1)
    return Fraction(comb(r+k-1,k)-r**(k-1),(r-1)*r**(k-1))

def edges_witness():
    # 0=u,1=a,2=b,3=v,4=c, 5..8=X, 9..12=Y.
    E=[(0,1),(1,2),(2,3)]
    E += [(0,x) for x in range(5,9)]
    E += [(x,4) for x in range(5,9)]
    E += [(4,y) for y in range(9,13)]
    E += [(y,3) for y in range(9,13)]
    return 13,E

def lap(n,edges):
    L=np.zeros((n,n),dtype=np.int64)
    for u,v in edges:
        L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    return L

def distances(n,edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    out=[]
    for x in range(n):
        d=[999]*n;d[x]=0;q=[x]
        for u in q:
            for v in adj[u]:
                if d[v]==999:d[v]=d[u]+1;q.append(v)
        out.append(d)
    return out

def transition(L,r,h):
    n=len(L);w,U=np.linalg.eigh(L.astype(float))
    z=h*w
    f=(r/(1+z/r)**r-1/(1+z))/(r-1)
    return (U*f)@U.T

assert a(2,1)==1 and a(2,2)==Fraction(1,2)
for r in range(2,19):
    assert a(r,0)==1 and a(r,1)==1 and a(r,2)==Fraction(1,2)
    assert a(r,3)==Fraction(r-2,6*r)
    assert a(r,4)==Fraction(r*r-17*r-6,24*r*r)
for r in range(3,18):
    assert a(r,3)>0 and a(r,4)<0
assert a(2,3)==0 and a(2,4)==-Fraction(3,8)
assert a(18,4)>0 and a(18,5)<0
N,E=edges_witness();D=distances(N,E);L=lap(N,E)
assert max(max(row) for row in D)==3 and D[0][3]==3
L3=np.linalg.matrix_power(L,3);L4=np.linalg.matrix_power(L,4)
assert L3[0,3]==-1 and L4[0,3]==2
assert a(2,4)*int(L4[0,3])==-Fraction(3,4)
# numerical checks avoid underflow/cancellation by evaluating at moderate small h
for r in [2,3,17,18]:
    T=transition(L,r,0.005)
    assert np.max(np.abs(T.sum(axis=1)-1))<1e-10
    if r==2: assert T[0,3]<0
    else: assert T[0,3]>0
for N,r,expected in [(5,3,-1),(5,17,-1),(5,18,1),(6,18,-1)]:
    P=lap(N,[(i,i+1) for i in range(N-1)])
    assert distances(N,[(i,i+1) for i in range(N-1)])[0][-1]==N-1
    assert a(r,N-1)*((-1)**(N-1))*int(np.linalg.matrix_power(P,N-1)[0,-1])>0 if expected==1 else a(r,N-1)*((-1)**(N-1))*int(np.linalg.matrix_power(P,N-1)[0,-1])<0
    if r != 17:
        T=transition(P,r,0.08)
        assert expected*T[0,-1]>0,(N,r,T[0,-1])
# positive diameter-three path under r=2: cubic vanishes, quartic is positive
P=lap(4,[(0,1),(1,2),(2,3)])
assert int(np.linalg.matrix_power(P,4)[0,3])<0
assert a(2,4)*int(np.linalg.matrix_power(P,4)[0,3])>0
assert transition(P,2,0.05).min()>-1e-12
print('VERIFY_OK coefficient_identities=17 threshold_signs=17 witness_vertices=13 witness_diameter=3 witness_L4_uv=2 positive_to_negative_refinement=18 numeric_cases=8')
