#!/usr/bin/env python3
import itertools, math

def all_matchings(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    def rec(pos, used, chosen):
        if pos==len(edges):
            out.append(tuple(chosen))
            return
        u,v=edges[pos]
        rec(pos+1, used, chosen)
        if u not in used and v not in used:
            used.add(u); used.add(v); chosen.append(pos)
            rec(pos+1, used, chosen)
            chosen.pop(); used.remove(u); used.remove(v)
    rec(0,set(),[])
    return edges,out

def inradius(n):
    if n==2:
        return 0.5,"upper"
    odd=1.0/(n+math.sqrt(2*n/(n-1))) if n%2 else None
    deg=1.0/(n-1+math.sqrt(n-1)) if n>=4 else None
    if n in (3,5,7):
        return odd,"odd"
    return deg,("tie" if n==4 else "degree")

def check(n):
    edges,matchings=all_matchings(n)
    N=len(edges)
    r,phase=inradius(n)

    # Coordinate-facet distance.
    assert abs(r-r)<1e-14

    if n>=4:
        ddeg=(1-(n-1)*r)/math.sqrt(n-1)
    else:
        ddeg=float("inf")

    odd_dist=[]
    for s in range(3,n+1,2):
        d=(((s-1)/2)-s*(s-1)/2*r)/math.sqrt(s*(s-1)/2)
        odd_dist.append((s,d))
    minodd=min((d for _,d in odd_dist),default=float("inf"))

    mind=min(r,ddeg,minodd)
    assert abs(mind-r)<1e-10,(n,r,ddeg,odd_dist)
    if phase=="odd":
        assert abs(minodd-r)<1e-10 and (n<4 or ddeg>r-1e-10)
    elif phase=="degree":
        assert abs(ddeg-r)<1e-10 and minodd>r+1e-10
    elif phase=="tie":
        assert abs(ddeg-r)<1e-10 and abs(minodd-r)<1e-10
    elif phase=="upper":
        assert n==2

    # Circumcenter and all vertex distances.
    if n==2:
        q=0.5; R=0.5
    else:
        k=n//2
        q=k/N
        R=math.sqrt(k-k*k/N)
    dvals=[]
    maxk=0
    for M in matchings:
        j=len(M)
        d2=j*(1-q)**2+(N-j)*q*q
        dvals.append((j,math.sqrt(d2)))
        maxk=max(maxk,j)
    mx=max(d for _,d in dvals)
    assert abs(mx-R)<1e-10,(n,mx,R)
    if n>=3:
        assert all((abs(d-R)<1e-10)==(j==maxk) for j,d in dvals)
    return len(matchings),phase

total=0
phases={}
for n in range(2,9):
    cnt,ph=check(n)
    total+=cnt
    phases[n]=ph
print("VERIFY_OK matching-polytope-radii n=2..8 matchings=%d phases=%s" % (total,phases))
