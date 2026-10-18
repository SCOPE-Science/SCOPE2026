#!/usr/bin/env python3
"""Independent finite checks for translation Lefschetz characters of group-Latin-square clique complexes.

Requires only the Python 3 standard library. No external file or package dependencies.
"""
from collections import Counter
from itertools import combinations, product


def group(moduli):
    elements=list(product(*(range(x) for x in moduli)))
    zero=tuple(0 for _ in moduli)
    def add(a,b):
        return tuple((x+y)%m for (x,y,m) in zip(a,b,moduli))
    return elements,zero,add


def complex_data(moduli):
    A,z,add=group(moduli)
    V=list(product(A,A))
    n=len(A)
    adj=[]
    for x,y in V:
        adj.append(tuple(j for j,(r,s) in enumerate(V)
            if (x,y)!=(r,s) and (x==r or y==s or add(x,y)==add(r,s))))
    adj_masks=[sum(1<<j for j in nbr) for nbr in adj]
    faces_by_dim=[[] for _ in range(n)]
    def rec(face,candidates):
        while candidates:
            bit=candidates & -candidates
            candidates-=bit
            v=bit.bit_length()-1
            newface=face+(v,)
            faces_by_dim[len(newface)-1].append(newface)
            rec(newface,candidates & adj_masks[v])
    rec((),(1<<len(V))-1)
    return A,z,add,V,faces_by_dim


def trace_for_translation(V,faces_by_dim,add,a,b):
    ids={v:i for i,v in enumerate(V)}
    perm=[ids[(add(x,a),add(y,b))] for x,y in V]
    trace=-1  # augmented empty-face contribution
    for dim,faces in enumerate(faces_by_dim):
        sign=(-1)**dim
        for f in faces:
            images=[perm[v] for v in f]
            if set(images)!=set(f):
                continue
            inversions=sum(x>y for i,x in enumerate(images) for y in images[i+1:])
            trace+=sign*(-1 if inversions%2 else 1)
    return trace


def gf2_rank(columns):
    pivots={}
    for c in columns:
        while c:
            i=c.bit_length()-1
            if i in pivots:
                c^=pivots[i]
            else:
                pivots[i]=c
                break
    return len(pivots)


def gf2_homology(faces_by_dim):
    ranks=[0]*len(faces_by_dim)
    for k in range(1,len(faces_by_dim)):
        prev={f:i for i,f in enumerate(faces_by_dim[k-1])}
        columns=[]
        for f in faces_by_dim[k]:
            x=0
            for sub in combinations(f,len(f)-1):
                x^=1<<prev[sub]
            columns.append(x)
        ranks[k]=gf2_rank(columns)
    fnums=[len(faces) for faces in faces_by_dim]
    betti=[fnums[k]-ranks[k]-(ranks[k+1] if k+1<len(ranks) else 0) for k in range(len(ranks))]
    betti[0]-=1
    return betti,ranks


def subgroup_generated(generators, zero, add_pair):
    H={zero}; frontier=[zero]
    while frontier:
        x=frontier.pop()
        for g in generators:
            y=add_pair(x,g)
            if y not in H:
                H.add(y);frontier.append(y)
    return frozenset(H)


def subgroup_checks(A,z,add,traces,n,tau):
    zero=(z,z)
    def add_pair(u,v):return add(u[0],v[0]),add(u[1],v[1])
    all_elems=list(product(A,A))
    checked=set()
    def check(H):
        if H in checked:return
        checked.add(H)
        assert zero in H
        subcounts=[]
        for condition in (lambda a,b:a==z,
                          lambda a,b:b==z,
                          lambda a,b:add(a,b)==z):
            HS=[(a,b) for a,b in H if condition(a,b)]
            h=len(HS)
            e=sum(add(a,a)==z and add(b,b)==z for a,b in HS)
            subcounts.append((h,e))
        N=(n-1)**3-(tau-1)*n*n//4
        N+=n*sum(h-1 for h,e in subcounts)
        N-=n*n//4*sum(e-1 for h,e in subcounts)
        N-=len(H)-1
        assert N%len(H)==0,(H,N)
        prediction=N//len(H)
        actual=sum(traces[t] for t in H)//len(H)
        assert sum(traces[t] for t in H)==actual*len(H)
        assert actual==prediction and prediction>=0,(H,actual,prediction)
    check(frozenset(all_elems))
    check(frozenset([zero]))
    for g in all_elems:
        check(subgroup_generated([g],zero,add_pair))
    for i,g in enumerate(all_elems):
        for h in all_elems[i:]:
            check(subgroup_generated([g,h],zero,add_pair))
    return len(checked)


def run(moduli,homology=False):
    A,z,add,V,faces=complex_data(moduli)
    n=len(A)
    tau=sum(add(a,a)==z for a in A)
    B=(n-1)**3-(tau-1)*n*n//4
    observed=Counter()
    assert len(faces[0])==n*n
    traces={}
    for a,b in product(A,A):
        got=trace_for_translation(V,faces,add,a,b)
        if (a,b)==(z,z):
            expect=B
            key='identity'
        else:
            d=1
            x,y=a,b
            while (x,y)!=(z,z):
                d+=1
                x,y=add(x,a),add(y,b)
            line=(a==z or b==z or add(a,b)==z)
            expect=n-1-(n*n//4 if d==2 else 0) if line else -1
            key=('line' if line else 'nonline',d)
        if got!=expect:
            raise AssertionError((moduli,a,b,key,got,expect))
        traces[(a,b)]=got
        observed[(str(key),got)]+=1
    group_subgroups_checked=subgroup_checks(A,z,add,traces,n,tau)
    invariants=sum(traces.values())//(n*n)
    assert sum(traces.values())==n*n*(n-tau)
    assert invariants==n-tau
    fnums=tuple(len(level) for level in faces)
    assert sum((-1)**k*sz for k,sz in enumerate(fnums))-1==B
    if homology:
        betti,ranks=gf2_homology(faces)
        assert betti==[B if k==2 else 0 for k in range(len(faces))]
        print('GF2 homology',moduli,'boundary_ranks',ranks,'reduced_betti',betti)
    print('PASS group=',moduli,'n=',n,'2torsion=',tau,'f_vector=',fnums,
          'characters=',sorted(observed.items()),'quotient_beta2=',invariants,'subgroups_checked=',group_subgroups_checked)


def main():
    for mods in [(5,),(6,),(7,),(8,),(2,4),(2,2,2),(3,3)]:
        run(mods,homology=(mods in [(5,),(6,)]))
    print('PASS: All independent signed face-trace, Euler, homology and orbit-rank checks.')
if __name__=='__main__':
    main()
