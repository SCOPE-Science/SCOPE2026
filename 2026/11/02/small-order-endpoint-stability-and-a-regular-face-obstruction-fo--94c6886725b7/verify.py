#!/usr/bin/env python3
"""Exact certificates for entrywise stability of doubly-stochastic projection.
Uses only Python standard library; all quantities are rational.
"""
from fractions import Fraction as Q
from itertools import permutations
from collections import Counter

def perm_masks(n):
    return [sum(1 << (i*n+p[i]) for i in range(n)) for p in permutations(range(n))]

def total_supports(n):
    matchings=perm_masks(n)
    for mask in range(1,1 << (n*n)):
        union=0
        for p in matchings:
            if mask&p==p: union|=p
        if union==mask: yield mask

def orbit_reps(n, supports):
    ps=list(permutations(range(n)))
    maps=[tuple(r[i]*n+c[j] for i in range(n) for j in range(n))
          for r in ps for c in ps]
    remain=set(supports)
    reps=[]
    while remain:
        chosen=min(remain)
        orbit=set()
        for mp in maps:
            x=chosen; y=0
            while x:
                z=x&-x; y|=1<<mp[z.bit_length()-1]; x-=z
            orbit.add(y)
        assert orbit <= set(supports)
        assert orbit <= remain
        reps.append((chosen,len(orbit)))
        remain.difference_update(orbit)
    return reps

def inv(M):
    r=len(M)
    a=[[Q(x) for x in row]+[Q(i==j) for j in range(r)] for i,row in enumerate(M)]
    for j in range(r):
        k=next(i for i in range(j,r) if a[i][j])
        a[k],a[j]=a[j],a[k]
        p=a[j][j]
        a[j]=[v/p for v in a[j]]
        for i in range(r):
            if i!=j and a[i][j]:
                k=a[i][j]
                a[i]=[v-k*w for v,w in zip(a[i],a[j])]
    return [row[r:] for row in a]

def projector_rows(n, E, requested=None):
    """Rows of orthogonal cycle-space projector via exact reduced Gram inverse."""
    E=list(E); m=len(E)
    parent=list(range(2*n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for i,j in E: parent[find(i)]=find(n+j)
    comps={}
    for u in range(2*n): comps.setdefault(find(u),[]).append(u)
    deleted={max(v) for v in comps.values()}
    keep=[u for u in range(2*n) if u not in deleted]
    B=[[Q(u==i or u==n+j) for i,j in E] for u in keep]
    r=len(keep)
    gram=[[sum(B[i][k]*B[j][k] for k in range(m)) for j in range(r)] for i in range(r)]
    G=inv(gram)
    # T=G B (the inverse normal-equation response).
    T=[[sum(G[i][k]*B[k][j] for k in range(r)) for j in range(m)] for i in range(r)]
    targets=range(m) if requested is None else requested
    ans={}
    for k in targets:
        row=[]
        for j in range(m):
            val=Q(k==j)-sum(B[i][k]*T[i][j] for i in range(r))
            row.append(val)
        ans[k]=row
    return ans

def norm_and_details(n,E):
    rows=projector_rows(n,E)
    rownorms=[sum(map(abs,rows[i])) for i in rows]
    return max(rownorms),rownorms

def certify_small(n,expected_count,expected_orbits,expected_max):
    supports=set(total_supports(n))
    assert len(supports)==expected_count, (n,len(supports))
    reps=orbit_reps(n,supports)
    assert len(reps)==expected_orbits, (n,len(reps))
    assert sum(sz for _,sz in reps)==len(supports)
    values=Counter()
    maxval=Q(0);fullmask=(1 << n*n)-1
    for mask,orbit in reps:
        edges=[(i,j) for i in range(n) for j in range(n) if mask>>(i*n+j)&1]
        val,_=norm_and_details(n,edges)
        values[str(val)]+=1
        maxval=max(maxval,val)
        if mask!=fullmask: assert val < expected_max,(n,mask,val)
    assert maxval==expected_max,(n,maxval)
    assert norm_and_details(n,[(i,j) for i in range(n) for j in range(n)])[0]==maxval
    print('n=%d: supports=%d, row-column relabeling orbits=%d, max=%s, orbit norms=%s'
          %(n,len(supports),len(reps),maxval,dict(sorted(values.items()))))

def certify_regular_face():
    n=12
    shifts=[0,2,3,6,8,9]
    E=[(i,(i+s)%n) for i in range(n) for s in shifts]
    # Every allowed edge lies in a shift permutation, so support is a Birkhoff face.
    assert len(E)==72
    assert len(set(E))==len(E)
    assert [sum(1 for i,j in E if i==u) for u in range(n)]==[6]*n
    assert [sum(1 for i,j in E if j==u) for u in range(n)]==[6]*n
    e=E.index((0,2))
    row=projector_rows(n,E,[e])[e]
    assert sum(row)==0  # row of a cycle-space projector kills constants
    # A symmetric idempotent projector satisfies ||row||_2^2 = P_ee.
    assert sum(x*x for x in row)==row[e]
    counts=Counter(row)
    expected={Q(-1,72):16,Q(1,36):16,Q(5,288):16,
              Q(-37,288):8,Q(11,288):8,Q(-5,144):4,
              Q(-23,144):2,Q(97,144):1,Q(1,144):1}
    assert counts==expected,(counts,expected)
    value=sum(abs(x) for x in row)
    affine=4*Q(n-1,n)**2
    assert value==Q(41,12)
    assert affine==Q(121,36)
    assert value-affine==Q(1,18)
    print('n=12: E={(i,i+s mod12):s in %s}; target=(0,2); norm=%s > affine=%s by %s'
          %(shifts,value,affine,value-affine))
    print('n=12: exact entry multiplicities:',sorted((str(x),v) for x,v in counts.items()))
    # The sign of this exact row on E is a norm-one perturbation attaining the row norm.
    H=[(1 if x>0 else -1 if x<0 else 0) for x in row]
    assert max(map(abs,H))==1 and sum(a*b for a,b in zip(row,H))==value
    # The face barycenter Y_{i,j}=1/6 on E has strictly positive entries.
    assert min(Q(1,6) for _ in E)>0
    # Strict normal multipliers at every forbidden entry ensure affine activity locally.
    print('n=12: exact sign-witness dual pairing=%s'%sum(a*b for a,b in zip(row,H)))

if __name__=='__main__':
    certify_small(2,3,2,Q(1))
    certify_small(3,49,6,Q(16,9))
    certify_small(4,7443,42,Q(9,4))
    certify_regular_face()
