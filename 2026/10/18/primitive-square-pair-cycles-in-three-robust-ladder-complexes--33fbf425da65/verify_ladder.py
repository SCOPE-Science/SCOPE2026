"""Finite independent checks for integral square-pair cycles in 3-robust ladder complexes.
No external packages. Usage: python verify_ladder.py
"""
from itertools import combinations
from collections import defaultdict
from math import comb


def sign(q):
    return -1 if sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q))) % 2 else 1


def square_cycle(i,n):
    # Vertices 0,...,n-1 top; n,...,2n-1 bottom.
    x=[i,i+1,n+i+1,n+i]
    E=[]
    for j in range(4):
        a,b=x[j],x[(j+1)%4]
        E.append(((a,b) if a<b else (b,a),1 if a<b else -1))
    return E


def wedge(A,B):
    Z=defaultdict(int)
    for (a,b),s in A:
        for (c,d),t in B:
            q=[a,b,c,d]
            if len(set(q))<4:continue
            Z[tuple(sorted(q))]+=s*t*sign(q)
    return {q:v for q,v in Z.items() if v}


def boundary(Z):
    D=defaultdict(int)
    for q,a in Z.items():
        for k in range(4):
            D[q[:k]+q[k+1:]]+=a*(-1)**k
    return {q:a for q,a in D.items() if a}


def apply_sym(Z,p):
    D=defaultdict(int)
    for q,a in Z.items():
        u=[p[x] for x in q]
        D[tuple(sorted(u))]+=a*sign(u)
    return {q:a for q,a in D.items() if a}


def rank_mod2(columns):
    piv={}
    for c in columns:
        while c:
            k=c.bit_length()-1
            if k in piv:c^=piv[k]
            else:
                piv[k]=c
                break
    return len(piv)


def verify(n):
    N=2*n
    # All graph edges are horizontal and vertical rungs.
    edges=set()
    for i in range(n-1):
        edges.add((i,i+1));edges.add((n+i,n+i+1))
    for i in range(n):edges.add((i,n+i))
    e=lambda i,j:tuple(sorted((i,j))) in edges
    def is_3face(a):return any(e(i,j) for i,j in combinations(a,2))
    def is_4face(a):
        a,b,c,d=a
        return ((e(a,b) and e(c,d)) or (e(a,c) and e(b,d)) or (e(a,d) and e(b,c)))
    faces3=[f for f in combinations(range(N),3) if is_3face(f)]
    faces4=[f for f in combinations(range(N),4) if is_4face(f)]
    idx={x:i for i,x in enumerate(faces3)}
    columns=[]
    for q in faces4:
        bits=0
        for k in range(4):bits ^= 1 << idx[q[:k]+q[k+1:]]
        columns.append(bits)
    nullity=len(faces4)-rank_mod2(columns)
    assert nullity==comb(n-1,2),(n,nullity)
    C=[square_cycle(i,n) for i in range(n-1)]
    pairs=list(combinations(range(n-1),2))
    Z={p:wedge(C[p[0]],C[p[1]]) for p in pairs}
    assert len(Z)==comb(n-1,2)
    row=[n+i if i<n else i-n for i in range(N)]
    col=[n-1-i if i<n else (3*n-1-i) for i in range(N)]
    tested=0
    for (i,j),z in Z.items():
        assert z and not boundary(z)
        assert all(q in faces4 for q in z)
        # A signed identity submatrix with row indexed by each square pair.
        pivot=tuple(sorted((i,i+1,n+j,n+j+1)))
        assert abs(z.get(pivot,0))==1
        assert all(z1.get(pivot,0)==0 for p,z1 in Z.items() if p!=(i,j))
        assert apply_sym(z,row)==z
        target=tuple(sorted((n-2-i,n-2-j)))
        assert apply_sym(z,col)==Z[target]
        tested+=1
    # Expected number of invariant pairs under column reversal.
    s=n-1;t=s//2
    fixed=sum(tuple(sorted((s-1-i,s-1-j)))==(i,j) for i,j in pairs)
    assert fixed==t
    return n,len(faces3),len(faces4),nullity,tested,fixed


def main():
    print('n  triangles tetrahedra H3_mod2_rank integral_pair_cycles fixed_pairs_col_reflection')
    total=0
    for n in range(3,12):
        result=verify(n)
        total+=result[4]
        print(*result)
    print('PASS; verified',total,'explicit nonzero boundary-zero cycles, primitive pivots and two symmetries')

if __name__=='__main__':main()
