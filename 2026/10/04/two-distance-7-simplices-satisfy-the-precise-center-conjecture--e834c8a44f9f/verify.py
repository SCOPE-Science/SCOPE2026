#!/usr/bin/env python3
from itertools import combinations, permutations

N=8
PAIRS=[(i,j) for i in range(N) for j in range(i+1,N)]
PID={e:k for k,e in enumerate(PAIRS)}
ALL_PERMS=list(permutations(range(N)))

def mask_from_edges(edges):
    m=0
    for i,j in edges:
        if i>j: i,j=j,i
        m |= 1 << PID[(i,j)]
    return m

def edges_from_mask(mask):
    return [e for k,e in enumerate(PAIRS) if (mask>>k)&1]

def permute_mask(mask,p):
    out=0
    for k,(i,j) in enumerate(PAIRS):
        if (mask>>k)&1:
            a,b=p[i],p[j]
            if a>b:a,b=b,a
            out |= 1 << PID[(a,b)]
    return out

def orbit(mask):
    return {permute_mask(mask,p) for p in ALL_PERMS}

def generate_regular_masks(d):
    rem=[d]*N
    nbr=[set() for _ in range(N)]
    out=[]
    def rec():
        v=next((i for i,r in enumerate(rem) if r),None)
        if v is None:
            out.append(mask_from_edges((i,j) for i in range(N) for j in nbr[i] if i<j))
            return
        need=rem[v]
        eligible=[u for u in range(v+1,N) if rem[u]>0 and u not in nbr[v]]
        if len(eligible)<need:
            return
        for C in combinations(eligible,need):
            rem[v]=0
            for u in C:
                rem[u]-=1; nbr[v].add(u); nbr[u].add(v)
            if min(rem)>=0:
                rec()
            for u in C:
                rem[u]+=1; nbr[v].remove(u); nbr[u].remove(v)
            rem[v]=need
    rec()
    return out

def is_vertex_transitive(mask):
    # exact: search all automorphisms and record the image of vertex 0
    images=set()
    for p in ALL_PERMS:
        if permute_mask(mask,p)==mask:
            images.add(p[0])
    return len(images)==N

def cycle_union(parts):
    edges=[]; off=0
    for m in parts:
        for i in range(m):
            edges.append((off+i,off+(i+1)%m))
        off += m
    return mask_from_edges(edges)

CUBIC_EDGES=[
[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,7),(4,7),(5,6),(6,7)],
]
CUBIC=[mask_from_edges(E) for E in CUBIC_EDGES]
DEG2=[cycle_union([8]),cycle_union([3,5]),cycle_union([4,4])]

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if s is None:return 0
            A[k],A[s]=A[s],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
        prev=pivot
    return sign*A[n-1][n-1]

def facet_det(mask,deleted,t):
    verts=[v for v in range(N) if v!=deleted]
    M=[[0]*8 for _ in range(8)]
    for i in range(1,8): M[0][i]=M[i][0]=1
    for i,a in enumerate(verts,1):
        for j,b in enumerate(verts,1):
            if i==j: val=0
            else:
                x,y=(a,b) if a<b else (b,a)
                val=t if ((mask>>PID[(x,y)])&1) else 1
            M[i][j]=val
    return bareiss_det(M)

def check_poly_identity(mask,vertex,formula):
    # Cayley-Menger determinant degree is <=6 for a 6-simplex facet,
    # so equality at 7 distinct t-values proves the polynomial identity.
    for t in range(7):
        got=facet_det(mask,vertex,t)
        exp=formula(t)
        assert got==exp,(vertex,t,got,exp)

def main():
    # complete finite classification of degree-2 color graphs
    two=set(generate_regular_masks(2))
    O2=[orbit(m) for m in DEG2]
    assert all(O2[i].isdisjoint(O2[j]) for i in range(3) for j in range(i))
    assert set().union(*O2)==two
    assert len(two)==3507
    assert [len(o) for o in O2]==[2520,672,315]
    assert [is_vertex_transitive(m) for m in DEG2]==[True,False,True]

    # complete finite classification of cubic color graphs
    cub=set(generate_regular_masks(3))
    O3=[orbit(m) for m in CUBIC]
    assert all(O3[i].isdisjoint(O3[j]) for i in range(6) for j in range(i))
    assert set().union(*O3)==cub
    assert len(cub)==19355
    assert [len(o) for o in O3]==[35,2520,10080,3360,840,2520]
    assert [is_vertex_transitive(m) for m in CUBIC]==[True,False,False,False,True,True]

    # Nontransitive degree-2 type C3 union C5.
    g=DEG2[1]
    fA=lambda t: t*(9*t-16)*(t*t-3*t+1)**2
    fB=lambda t: -t*t*(t*t-3*t+1)*(7*t*t-5*t-9)
    for v in (0,1,2): check_poly_identity(g,v,fA)
    for v in (3,4,5,6,7): check_poly_identity(g,v,fB)
    for t in range(7):
        assert fA(t)-fB(t)==16*t*(t-1)**3*(t*t-3*t+1)

    # Nontransitive cubic type 1.
    g=CUBIC[1]
    fA=lambda t: -t**3*(t-2)*(23*t*t-50*t+20)
    fB=lambda t: -t**3*(7*t**3-48*t*t+72*t-24)
    for v in (0,1,6,7): check_poly_identity(g,v,fA)
    for v in (2,3,4,5): check_poly_identity(g,v,fB)
    for t in range(7): assert fA(t)-fB(t)==-16*t**3*(t-1)**3

    # Nontransitive cubic type 2. One pair of facet classes already forces t=1.
    g=CUBIC[2]
    fA=lambda t: t*(t-2)*(t**4-34*t**3+88*t*t-60*t+12)
    fB=lambda t: t*(t*t-4*t+2)*(t**3-16*t*t+26*t-4)
    fC=lambda t: -t*(3*t*t-6*t+2)*(5*t**3-10*t*t-6*t+4)
    for v in (0,1,6,7): check_poly_identity(g,v,fA)
    for v in (2,5): check_poly_identity(g,v,fB)
    for v in (3,4): check_poly_identity(g,v,fC)
    for t in range(7): assert fA(t)-fB(t)==-16*t*(t-1)**4

    # Nontransitive cubic type 3. The extra common root makes every facet degenerate.
    g=CUBIC[3]
    fA=lambda t: -(t*t-3*t+1)*(4*t**3+7*t*t-37*t+19)
    fB=lambda t: -(t*t-3*t+1)*(20*t**3-41*t*t+11*t+3)
    fC=lambda t: (t*t-3*t+1)**2*(16*t*t-36*t+13)
    for v in (0,1,2): check_poly_identity(g,v,fA)
    for v in (3,4,5): check_poly_identity(g,v,fB)
    for v in (6,7): check_poly_identity(g,v,fC)
    for t in range(7): assert fA(t)-fB(t)==16*(t-1)**3*(t*t-3*t+1)

    print('VERIFY_OK')
    print('degree2_labeled=3507 classes=3 orbit_sizes=2520,672,315')
    print('degree3_labeled=19355 classes=6 orbit_sizes=35,2520,10080,3360,840,2520')
    print('nontransitive_classes=4')
    print('determinant_identities=verified_exactly_by_degree_bound_and_7_integer evaluations')

if __name__=='__main__': main()
