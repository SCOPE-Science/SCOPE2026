#!/usr/bin/env python3
"""Exact finite corroboration for intrinsic ellipsoids of one-factor polytopes.

Uses only Python standard library. Finite tests do not prove general theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def matchings(v):
    if not v:
        yield ()
        return
    a=v[0]
    for j in range(1,len(v)):
        b=v[j]
        for rest in matchings(v[1:j]+v[j+1:]):
            yield ((a,b),)+rest

def check(N):
    assert N%2==0 and N>=6
    E=list(combinations(range(N),2)); m=len(E)
    d=m-N
    u=F(1,N-1)
    r2=F(1,(N-1)*(N-3))
    R2=F(N*(N-2),2*(N-1))
    assert d==N*(N-3)//2
    def proj(e,f):
        overlap=len(set(e)&set(f))
        return F(int(e==f))-F(overlap, N-2)+F(2,(N-1)*(N-2))
    P=[[proj(e,f) for f in E] for e in E]
    assert all(sum(P[i][j] for j in range(m))==0 for i in range(m))
    assert all(sum(P[i][j] for j,e in enumerate(E) if vertex in e)==0 for i in range(m) for vertex in range(N))
    assert all(sum(P[i][k]*P[k][j] for k in range(m))==P[i][j] for i in range(m) for j in range(m))
    for e_idx,e in enumerate(E):
        diag=P[e_idx][e_idx]
        assert diag==F(N-3,N-1)
        # Tangent point q_e in the affine hull; every other coordinate > 0.
        q=[u-P[f_idx][e_idx]/(N-3) for f_idx in range(m)]
        assert q[e_idx]==0 and all(x>0 for j,x in enumerate(q) if j!=e_idx)
        assert all(sum(q[j] for j,f in enumerate(E) if vertex in f)==1 for vertex in range(N))
        assert sum((x-u)**2 for x in q)==r2
        assert all(q[j]==(0 if f==e else F(1,N-2) if len(set(f)&set(e))==1 else F(N-4,(N-2)*(N-3))) for j,f in enumerate(E))
    checked_cut=0
    for s in range(3,N-2,2):
        for S in combinations(range(N),s):
            T=set(S)
            c=[F((x in T)!=(y in T)) for x,y in E]
            t=s*(N-s)
            slack=F(t,N-1)-1
            proj_norm2=sum(c[i]*P[i][j]*c[j] for i in range(m) for j in range(m))
            assert proj_norm2==F(2*t*(t-N+1),(N-2)*(N-1))
            assert slack*slack/proj_norm2==F((N-2)*(t-N+1),2*t*(N-1))
            assert slack*slack/proj_norm2>r2
            checked_cut+=1
    all_m=list(matchings(tuple(range(N))))
    count=1
    for j in range(N-1,0,-2):count*=j
    assert len(all_m)==count
    # Exact expectation from exhaustive perfect matchings.
    counts=[0]*m
    second=[[0]*m for _ in range(m)]
    lookup={e:i for i,e in enumerate(E)}
    for mt in all_m:
        inds=[lookup[e] for e in mt]
        for i in inds:counts[i]+=1
        for i in inds:
            for j in inds:second[i][j]+=1
        assert sum((F(int(e in mt))-u)**2 for e in E)==R2
    assert all(F(count,len(all_m))==u for count in counts)
    f=R2/d
    assert all(F(second[i][j],len(all_m))-u*u==f*P[i][j] for i in range(m) for j in range(m))
    # Fractional 1-factor supported on two triangles and remaining disjoint edges:
    # this point violates an integral odd-cut constraint but satisfies Bx=1.
    fractional={e:F(0) for e in E}
    for cyc in ((0,1,2),(3,4,5)):
        for i in range(3):
            fractional[tuple(sorted((cyc[i],cyc[(i+1)%3])))]=F(1,2)
    for a in range(6,N,2):fractional[(a,a+1)]=F(1)
    assert all(sum(fractional[e] for e in E if v in e)==1 for v in range(N))
    assert all(0<=z<=1 for z in fractional.values())
    assert sum(fractional[e] for e in E if (e[0]<3)!=(e[1]<3))==0
    assert sum((fractional[e]-u)**2 for e in E)<R2
    # Entire fractional relaxation lies in outer ball: x_e^2<=x_e,
    # since 0<=x_e<=1 and the common degree equations fix their sum.
    assert sum(fractional.values())==F(N,2)
    print('N=',N,'edges=',m,'dimension=',d,'matchings=',len(all_m),'odd_sets=',checked_cut,
          'John_r2=',r2,'Lowner_R2=',R2,'certificate_OK')

if __name__=='__main__':
    for N in (6,8,10):check(N)
    print('ALL_EXACT_TESTS_OK')
