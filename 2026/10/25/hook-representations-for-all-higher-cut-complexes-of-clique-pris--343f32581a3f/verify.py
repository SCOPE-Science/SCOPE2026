#!/usr/bin/env python3
"""Exact finite signed Lefschetz check of prism k-cut homology characters."""
import itertools
from math import comb

def parts(n):
    if n==0: yield ()
    else:
        for a in range(1,n+1):
            for rest in parts(n-a):
                if not rest or a<=rest[0]:yield (a,)+rest

def perm_of_cycles(cycles):
    p=[]; pos=0
    for z in cycles:
        p.extend(list(range(pos+1,pos+z))+[pos]); pos+=z
    return tuple(p)

def poly_product(polys,deg):
    v=[1]+[0]*deg
    for p in polys:
        w=[0]*(deg+1)
        for i,a in enumerate(v):
            for j,b in enumerate(p):
                if i+j<=deg:w[i+j]+=a*b
        v=w
    return v

def predicted(n,k,cyc,swap):
    pol=[]
    for l in cyc:
        v=[1]+[0]*(l-1)+[-(-1)**l]  # 1-(-t)^l
        pol.append(v)
    coeff=poly_product(pol,k-1)
    # divide by 1+t: q_j=coeff_j-q_{j-1}
    q=0
    for j in range(k):q=coeff[j]-q
    return q*((-1)**((n+1)*swap))

def count_disconnected_selection_complement(mask,n,k):
    # X=vertex complement of mask
    X=((1<<(2*n))-1)^mask
    plus=(X&((1<<n)-1)); minus=(X>>n)&((1<<n)-1)
    support=(plus|minus)
    if support.bit_count()<k:return False
    if (plus==0 or minus==0):return False
    # if supp >= k, and both signs in X, can select k positions and two different signs?
    # if they are both in same column and the others have no choice, still k>=2 works.
    return True

def inv_parity(a):
    s=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            s^=(a[i]>a[j])
    return -1 if s else 1

def direct(n,k,perm,swap):
    act=tuple((perm[i%n]+(n if (i>=n)^bool(swap) else 0)) for i in range(2*n))
    FULL=(1<<(2*n))-1
    tot=-1 # empty simplex: (-1)^(-1)=-1
    faces=0
    for mask in range(1,1<<(2*n)):
        if not count_disconnected_selection_complement(mask,n,k):continue
        faces+=1
        inds=[i for i in range(2*n) if mask>>i&1]
        images=[act[i] for i in inds]
        if sum(1<<v for v in images)!=mask:
            continue
        orientation=inv_parity(images)
        tot+=(-1)**(len(inds)-1)*orientation
    d=2*n-k-2
    return (-1)**d*tot,faces

def run():
    cases=0
    for n in range(2,7):
        for k in range(2,n+1):
            for cyc in parts(n):
                perm=perm_of_cycles(cyc)
                for swap in (0,1):
                    a,faces=direct(n,k,perm,swap)
                    b=predicted(n,k,cyc,swap)
                    assert a==b,(n,k,cyc,swap,a,b,faces)
                    cases+=1
    print('PRISM_CUT_EQUIVARIANT_LEFSCHETZ_VERIFIED',cases)
if __name__=='__main__':run()

def gf2_betti(n,k):
    faces=[[] for _ in range(2*n)]
    for m in range(1,1<<(2*n)):
        if count_disconnected_selection_complement(m,n,k):
            faces[m.bit_count()-1].append(m)
    ranks=[]
    for dim in range(len(faces)):
        if not faces[dim]: ranks.append(0);continue
        if dim==0: # reduced differential to empty face
            ranks.append(1);continue
        row={v:i for i,v in enumerate(faces[dim-1])}
        piv={}
        for m in faces[dim]:
            vec=0
            for i in range(2*n):
                if m&(1<<i):vec ^= 1<<row[m^(1<<i)]
            while vec:
                j=vec.bit_length()-1
                if j in piv:vec^=piv[j]
                else:piv[j]=vec;break
        ranks.append(len(piv))
    beta=[len(faces[i])-ranks[i]-(ranks[i+1] if i+1<len(ranks) else 0) for i in range(len(faces))]
    actual={i:b for i,b in enumerate(beta) if b}
    expected={2*n-k-2:comb(n-1,k-1)}
    assert actual==expected,(n,k,actual,expected)
    return sum(len(f) for f in faces), actual

if __name__=='__main__':
    for n,k in ((4,4),(5,4),(5,5),(6,4),(6,5),(6,6)):
        ct,actual=gf2_betti(n,k)
        print('INTEGRAL_GRADE_MOD2_CHECK',n,k,ct,actual)

def disconnected_k_masks_from_graph(n,k):
    """Build disconnected induced k-sets using only graph adjacency and DFS."""
    edges=[0]*(2*n)
    for v in range(2*n):
        for w in range(2*n):
            if v==w:continue
            if (v//n)==(w//n) or v%n==w%n:
                edges[v]|=1<<w
    disconnected=[]
    for tup in itertools.combinations(range(2*n),k):
        mask=sum(1<<i for i in tup)
        visited=0; frontier=1<<tup[0]
        while frontier:
            visited|=frontier
            around=0
            while frontier:
                b=frontier&-frontier;frontier^=b
                around|=edges[b.bit_length()-1]
            frontier=(around&mask)&~visited
        if visited!=mask:disconnected.append(mask)
    return disconnected

def graph_membership_check():
    tests=0
    for n in range(2,7):
        for k in range(2,n+1):
            disconnected=disconnected_k_masks_from_graph(n,k)
            for mask in range(1<<(2*n)):
                predicted=count_disconnected_selection_complement(mask,n,k)
                direct_graph=any(mask&w==0 for w in disconnected)
                assert predicted==direct_graph,(n,k,mask,predicted,direct_graph)
                tests+=1
    print('PRISM_CUT_GRAPH_FACE_EQUIVALENCE_VERIFIED',tests)

if __name__=='__main__':
    graph_membership_check()
