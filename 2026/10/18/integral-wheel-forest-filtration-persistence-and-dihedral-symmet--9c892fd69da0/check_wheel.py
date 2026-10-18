#!/usr/bin/env python3
"""Exact finite checks for wheel induced-forest filtration and dihedral characters.

Standard-library only; executes exhaustive face enumeration and GF(2) ranks.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def independent_sets(m):
    result={0:[()]}
    for d in range(1,m//2+1):
        result[d]=[s for s in combinations(range(m),d)
                   if all((x-y)%m not in (1,m-1) for x,y in combinations(s,2))]
    return result


def indep_count(m,d):
    return m*comb(m-d,d)//(m-d) if 1<=d<=m//2 else 0


def r_beta(m):
    q,v=divmod(m,3)
    return (q if v==2 else q-1), (2 if v==0 else 1)


def predicted(m,d):
    r,beta=r_beta(m)
    chi=-1+sum((-1)**(j-1)*indep_count(m,j) for j in range(1,d+1))
    return (-1)**(d-1)*(chi-((-1)**r*beta if d>r+1 else 0))


def forest_faces(m,d):
    n=m+1
    edges=[(i,(i+1)%m) for i in range(m)]+[(i,m) for i in range(m)]
    ranks=defaultdict(list)
    for mask in range(1,1<<n):
        s=[v for v in range(n) if mask&(1<<v)]
        parent=list(range(n)); deg=[0]*n
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        okay=True
        for u,v in edges:
            if not (mask&(1<<u) and mask&(1<<v)):
                continue
            deg[u]+=1; deg[v]+=1
            if deg[u]>d or deg[v]>d:
                okay=False;break
            ru,rv=find(u),find(v)
            if ru==rv:
                okay=False;break
            parent[ru]=rv
        if okay:
            ranks[len(s)-1].append(tuple(s))
    return ranks


def bitrank(vectors):
    piv={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k not in piv:
                piv[k]=v;break
            v^=piv[k]
    return len(piv)


def mod2_bettis(faces):
    dimensions=sorted(faces)
    ranks={}
    for k in dimensions:
        if k==0:
            continue
        rows={face:i for i,face in enumerate(faces[k-1])}
        vectors=[]
        for face in faces[k]:
            v=0
            for j in range(len(face)):
                v^=1<<rows[face[:j]+face[j+1:]]
            vectors.append(v)
        ranks[k]=bitrank(vectors)
    out={}
    for k in dimensions:
        b=len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0:b-=1
        if b:out[k]=b
    return out


def dhedral_char(m,vertexmap):
    V=set(range(m))
    E={(u,v) for u in range(m) for v in range(u+1,m)
       if (v-u)%m not in (1,m-1)}
    trace0=sum(vertexmap(v)==v for v in V)
    trace1=0
    for u,v in E:
        a,b=vertexmap(u),vertexmap(v)
        if {a,b}=={u,v}:
            trace1+=1 if (a,b)==(u,v) else -1
    return trace1-trace0+1


def expected_reflection(m,a):
    if m%2:
        return -(m-3)//2
    return 1-m//2 if a%2==0 else 3-m//2


def run():
    summary=[]
    for m in range(8,13):
        a=m//2; r,beta=r_beta(m)
        for d in range(2,a+1):
            fs=forest_faces(m,d)
            actual=mod2_bettis(fs)
            predicted_b={m-2:1}
            if d==r+1:
                predicted_b[d]=predicted_b.get(d,0)+predicted(m,d)
            elif d<r+1:
                predicted_b[d]=predicted_b.get(d,0)+predicted(m,d)
            else:
                predicted_b[r+1]=predicted_b.get(r+1,0)+beta
                predicted_b[d]=predicted_b.get(d,0)+predicted(m,d)
            predicted_b={k:v for k,v in predicted_b.items() if v}
            assert actual==predicted_b, ('homology',m,d,actual,predicted_b)
            assert len(fs[m-2])==m and all(len(x)==m-1 for x in fs[m-2])
            summary.append((m,d,actual,sum(map(len,fs.values()))))
        b=predicted(m,2)
        assert dhedral_char(m,lambda v:v)==b
        for k in range(1,m):
            expected=1-m//2 if m%2==0 and k==m//2 else 1
            assert dhedral_char(m,lambda v,k=k:(v+k)%m)==expected, ('rotation',m,k)
        for a0 in range(m):
            actual=dhedral_char(m,lambda v,a0=a0:(a0-v)%m)
            assert actual==expected_reflection(m,a0),('reflection',m,a0,actual)
    for line in summary:
        print('m=%2d d=%d GF2_reduced_homology=%s nonempty_faces=%d'%line)
    print('PASS: full wheel face/chain checks, all predicted ranks, and every dihedral element for 8<=m<=12')

if __name__=='__main__':run()
