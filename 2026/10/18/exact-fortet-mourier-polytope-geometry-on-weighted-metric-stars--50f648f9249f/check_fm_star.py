#!/usr/bin/env python3
"""Exact-rational checks for finite weighted-star Fortet-Mourier geometry.

No third-party dependencies. Exhaustive active-set enumeration in small cases
and independent dual-function evaluations with signed atomic masses.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random


def bounds(radii):
    m = len(radii)
    # row a*x <= b, x=(center,leaves ...)
    C = []
    for j in range(m+1):
        for sign in (1,-1):
            a = [Q(0)]*(m+1)
            a[j] = Q(sign)
            C.append((tuple(a),Q(1)))
    for i,r in enumerate(radii,1):
        for sign in (1,-1):
            a=[Q(0)]*(m+1)
            a[0]=Q(-sign);a[i]=Q(sign)
            C.append((tuple(a),r))
    return C


def solve(A,b):
    n=len(b)
    M=[list(A[j])+[b[j]] for j in range(n)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if M[i][col]),None)
        if pivot is None:return None
        M[pivot],M[col]=M[col],M[pivot]
        d=M[col][col]
        for j in range(col,n+1):M[col][j]/=d
        for k in range(n):
            if k==col:continue
            e=M[k][col]
            if e:
                for j in range(col,n+1):M[k][j]-=e*M[col][j]
    return tuple(M[i][-1] for i in range(n))


def feasible(x,C):
    return all(sum(a*y for a,y in zip(row,x))<=b for row,b in C)


def explicit_vertices(radii):
    m=len(radii)
    anchors={Q(-1),Q(1)}
    for r in radii:
        if r<Q(2):
            anchors.update((Q(1)-r,r-Q(1)))
    vertices=set()
    for t in anchors:
        L=[max(Q(-1),t-r) for r in radii]
        U=[min(Q(1),t+r) for r in radii]
        for bit in product((0,1),repeat=m):
            xi=tuple(U[i] if bit[i] else L[i] for i in range(m))
            if t in (Q(-1),Q(1)):
                vertices.add((t,)+xi)
            elif any((t==Q(1)-r and xi[i]==Q(1)) or
                     (t==r-Q(1) and xi[i]==Q(-1))
                     for i,r in enumerate(radii)):
                vertices.add((t,)+xi)
    return vertices


def enumerate_vertices(radii):
    C=bounds(radii); n=len(radii)+1
    out=set()
    for inds in combinations(range(len(C)),n):
        sol=solve([C[j][0] for j in inds],[C[j][1] for j in inds])
        if sol is not None and feasible(sol,C):out.add(sol)
    return out


def dual_breakpoint(radii,coeff):
    ts={Q(-1),Q(1)}
    for r in radii:
        if r<Q(2): ts.update((Q(1)-r,r-Q(1)))
    def obj(t):
        return coeff[0]*t+sum(coeff[i+1]*(min(Q(1),t+r) if coeff[i+1]>=0 else max(Q(-1),t-r)) for i,r in enumerate(radii))
    return max(obj(t) for t in ts)


def dual_by_vertices(vertices,coeff):
    return max(sum(a*x for a,x in zip(coeff,v)) for v in vertices)


def dual_sweep(radii,coeff):
    events={}
    for r,c in zip(radii,coeff[1:]):
        if r>=2:continue
        if c>=0:
            t=Q(1)-r
            events[t]=events.get(t,Q(0))+c
        else:
            t=r-Q(1)
            events[t]=events.get(t,Q(0))-c
    initial=coeff[0]*Q(-1)+sum(c*(min(Q(1),-Q(1)+r) if c>=0 else -Q(1)) for c,r in zip(coeff[1:],radii))
    slope=coeff[0]+sum(max(Q(0),c) for c,r in zip(coeff[1:],radii) if r<2)
    best=initial;t0=Q(-1);f=initial
    for t,down in sorted(events.items()):
        if -1<t<1:
            f+=slope*(t-t0)
            best=max(best,f)
            slope-=down
            t0=t
    f+=slope*(Q(1)-t0)
    return max(best,f)



def facet_witness(radii,kind,index=None,sgn=1):
    """A point where only the nominated nonredundant inequality is active."""
    m=len(radii)
    if kind=='center':
        t=Q(sgn)
        return (t,)+tuple(t-Q(sgn)*min(r,Q(1))/2 for r in radii)
    if kind=='cube':
        r=radii[index]
        t=Q(sgn)*(Q(1)-r/2) if r<2 else Q(0)
        x=[t]*m;x[index]=Q(sgn)
        return (t,)+tuple(x)
    if kind=='edge':
        r=radii[index]
        assert r<2
        t=-Q(sgn)*r/2
        x=[t]*m;x[index]=Q(sgn)*r/2
        return (t,)+tuple(x)
    raise ValueError(kind)

def check_facets(radii):
    C=bounds(radii);m=len(radii);checks=0
    for i in range(m+1):
        for sgn in (1,-1):
            x=facet_witness(radii,'center' if i==0 else 'cube',None if i==0 else i-1,sgn)
            target=2*i+(0 if sgn==1 else 1)
            active=[j for j,(a,b) in enumerate(C) if sum(y*z for y,z in zip(a,x))==b]
            assert active==[target],('cube',radii,i,sgn,active,target)
            checks+=1
    for i,r in enumerate(radii):
        if r>=2:continue
        for sgn in (1,-1):
            x=facet_witness(radii,'edge',i,sgn)
            target=2*(m+1)+2*i+(0 if sgn==1 else 1)
            active=[j for j,(a,b) in enumerate(C) if sum(y*z for y,z in zip(a,x))==b]
            assert active==[target],('edge',radii,i,sgn,active,target)
            checks+=1
    return checks

def count_formula(radii):
    m=len(radii); anchors={}
    for i,r in enumerate(radii):
        if r>=2:continue
        anchors.setdefault(Q(1)-r,[]).append((i,1))
        anchors.setdefault(r-Q(1),[]).append((i,-1))
    total=Q(2)**(m+1)
    for t,events in anchors.items():
        if t in (-1,1):continue
        pins={}
        for i,sgn in events:pins.setdefault(i,set()).add(sgn)
        if any(len(s)==2 for s in pins.values()):total+=2**m
        else:total+=(2**m-2**(m-len(pins)))
    return total


def main():
    rng=Random(20261013)
    groups=[
        ('generic2',(Q(1,3),Q(3,4))),
        ('collision2',(Q(1,2),Q(3,2))),
        ('equal2',(Q(1,2),Q(1,2))),
        ('unit2',(Q(1),Q(1))),
        ('inactive2',(Q(2),Q(3))),
        ('mixed2',(Q(4,5),Q(3))),
        ('generic3',(Q(1,3),Q(3,4),Q(6,5))),
        ('collision3',(Q(1,2),Q(3,2),Q(1))),
        ('inactive3',(Q(2),Q(3,2),Q(5,2))),
        ('equal3',(Q(1,2),Q(1,2),Q(1,2))),
    ]
    tally=0
    for name,rad in groups:
        E=enumerate_vertices(rad)
        X=explicit_vertices(rad)
        assert E==X,(name,len(E),len(X),E-X,X-E)
        assert len(X)==count_formula(rad),name
        tally+=2+check_facets(rad)
        for v in X:
            assert feasible(v,bounds(rad)),name
            tally+=1
        for _ in range(50):
            a=tuple(Q(rng.randint(-4,4)) for _ in range(len(rad)+1))
            d1=dual_breakpoint(rad,a)
            d2=dual_by_vertices(E,a)
            d3=dual_sweep(rad,a)
            assert d1==d2==d3,(name,a,d1,d2,d3)
            tally+=1
        print(name,'vertices',len(X),'tests pass')
    for rad in ((Q(1,3),Q(2,5),Q(3,4),Q(7,6)),
                (Q(1,3),Q(5,3),Q(1),Q(1,2)),
                (Q(3),Q(2),Q(1,2),Q(1,2))):
        E=enumerate_vertices(rad)
        X=explicit_vertices(rad)
        assert E==X and len(X)==count_formula(rad)
        tally+=2+check_facets(rad)
        print('four-leaf case',rad,'vertices',len(X),'passed')
    for m in range(1,10):
        radii=tuple(Q(1,10*(m+1))*(i+1) for i in range(m))
        assert len(explicit_vertices(radii)) == (m+2)*2**m
        tally+=1
    print('PASSED',tally,'exact-rational assertions')

if __name__=='__main__':main()
