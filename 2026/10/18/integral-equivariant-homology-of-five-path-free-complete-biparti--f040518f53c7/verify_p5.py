#!/usr/bin/env python3
"""Standalone exact finite checks of path-free complexes; no external packages."""
from itertools import combinations


def all_faces(m,n):
    d=m+n
    # In K_{m,n}, a five-vertex path exists iff one part has >=3
    # selected vertices and the other part has >=2.
    result=[set() for _ in range(d+1)]
    for mask in range(1,1<<d):
        a=(mask&((1<<m)-1)).bit_count()
        b=(mask>>m).bit_count()
        if not ((a>=3 and b>=2) or (a>=2 and b>=3)):
            result[mask.bit_count()-1].add(mask)
    return result


def direct_path_test(mask,m,n):
    vertices=[j for j in range(m+n) if mask>>j&1]
    if len(vertices)<5:return False
    for c in combinations(vertices,5):
        a=sum(j<m for j in c)
        b=5-a
        if (a,b) in ((2,3),(3,2)):
            return True
    return False


def matrix_rank_modp(face_prev,face_next,p):
    index={mask:i for i,mask in enumerate(face_prev)}
    pivots={}
    for mask in sorted(face_next):
        bits=[b for b in range(mask.bit_length()) if mask & (1<<b)]
        v={index[mask^(1<<b)]: ((-1)**k)%p for k,b in enumerate(bits)}
        v={i:a for i,a in v.items() if a%p}
        while v:
            row=min(v)
            if row in pivots:
                piv=pivots[row]
                a=v[row]
                for q,c in piv.items():
                    new=(v.get(q,0)-a*c)%p
                    if new:v[q]=new
                    else:v.pop(q,None)
            else:
                inv=pow(v[row],-1,p)
                pivots[row]={i:(a*inv)%p for i,a in v.items()}
                break
    return len(pivots)


def test_one(m,n):
    F=all_faces(m,n)
    assert all(not direct_path_test(s,m,n) for faces in F for s in faces)
    assert sum(len(a) for a in F)==sum(not direct_path_test(s,m,n) for s in range(1,1<<(m+n)))
    bettis=[]
    for p in (2,3,5,101):
        ranks=[0]+[matrix_rank_modp(F[k-1],F[k],p) for k in range(1,m+n)] + [0]
        b=[len(F[k])-ranks[k]-ranks[k+1] for k in range(m+n)]
        b[0]-=1 # reduced H_0
        bettis.append((p,tuple(b)))
        expected=((m*(m-1)//2)*(n*(n-1)//2) - (m-1)*(n-1))
        assert all((b[k]==expected if k==3 else b[k]==0) for k in range(m+n)),(m,n,p,b,expected)
    print('m,n:',m,n,'f-vector:',[len(x) for x in F if x], 'betti3:',expected,'checks:',[v[0] for v in bettis])

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(4,4),(3,5),(4,5),(5,5)]:
        test_one(m,n)
    print('ALL EXACT FINITE HOMOLOGY CHECKS PASSED')
