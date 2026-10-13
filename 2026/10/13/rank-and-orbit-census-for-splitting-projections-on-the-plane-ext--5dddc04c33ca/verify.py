"""Finite-field checks for idempotent weight-minus-one Rota--Baxter projections on the four-dimensional exterior algebra."""
from itertools import combinations, product
from math import comb


def rref_space_bases(q,n=4):
    for k in range(n+1):
        for pivots in combinations(range(n), k):
            frees=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
            for values in product(range(q), repeat=len(frees)):
                rows=[[int(j==p) for j in range(n)] for p in pivots]
                for (i,j),v in zip(frees,values): rows[i][j]=v
                yield (k,tuple(tuple(row) for row in rows))


def rank(A,q):
    A=[list(r) for r in A]
    if not A: return 0
    n=len(A[0]); pivot=0
    for j in range(n):
        for i in range(pivot,len(A)):
            if A[i][j]%q:break
        else:continue
        A[pivot],A[i]=A[i],A[pivot]
        inv=pow(A[pivot][j],-1,q)
        A[pivot]=[x*inv%q for x in A[pivot]]
        for i in range(len(A)):
            if i!=pivot:
                m=A[i][j]
                if m:A[i]=[(x-m*y)%q for x,y in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==len(A):break
    return pivot


def mul(a,b,q):
    A,B,C,D=a; E,F,G,H=b
    return ((A*E)%q,(A*F+B*E)%q,(A*G+C*E)%q,(A*H+D*E+B*G-C*F)%q)


def closed(B,q):
    r=len(B)
    return all(rank(B+(mul(x,y,q),),q)==r for x in B for y in B)


def basis_projector(B,C,q):
    from itertools import product
    full=B+C
    if rank(full,q)<4: raise AssertionError('noncomplementary')
    # P(x)=b where x=b+c. For each standard basis column, solve linear equations.
    out=[]
    for j in range(4):
        M=[[full[col][row]%q for col in range(4)]+[int(row==j)] for row in range(4)]
        for pivot in range(4):
            k=next(i for i in range(pivot,4) if M[i][pivot])
            M[k],M[pivot]=M[pivot],M[k]
            inv=pow(M[pivot][pivot],-1,q)
            M[pivot]=[(v*inv)%q for v in M[pivot]]
            for i in range(4):
                if i==pivot:continue
                a=M[i][pivot]
                if a:M[i]=[(v-a*w)%q for v,w in zip(M[i],M[pivot])]
        cs=[M[i][4] for i in range(4)]
        out.append(tuple(sum(cs[i]*B[i][k] for i in range(len(B)))%q for k in range(4)))
    return tuple(out)


def test_rb(P,q):
    def apply(v):return tuple(sum(v[i]*P[i][j] for i in range(4))%q for j in range(4))
    zero=(0,0,0,0)
    for i in range(4):
        for j in range(4):
            a,b=P[i],P[j]
            z=tuple(int(k==i) for k in range(4))
            w=tuple(int(k==j) for k in range(4))
            t1=mul(a,b,q)
            ma=mul(a,w,q);mb=mul(z,b,q);mc=mul(z,w,q)
            t2=apply(tuple((ma[k]+mb[k]-mc[k])%q for k in range(4)))
            if t1!=t2:return False
    for i in range(4):
        if apply(P[i])!=P[i]:return False
    return True


def classify(q):
    assert q in (2,3,5,7,11)
    sub=[(k,B) for k,B in rref_space_bases(q) if closed(B,q)]
    bydim={i:sum(k==i for k,B in sub) for i in range(5)}
    counts={i:0 for i in range(5)}
    reps={}
    for r,B in sub:
        for s,C in sub:
            if r+s!=4 or rank(B+C,q)!=4:continue
            P=basis_projector(B,C,q)
            assert test_rb(P,q),(q,r,B,C)
            counts[r]+=1
            reps.setdefault(r,P)
    L=q*q*(q+1)
    expected={0:1,1:1+L,2:2*L,3:1+L,4:1}
    assert counts==expected,(q,counts,expected)
    # Distinct RREF subspaces uniquely describe all linear subspaces; hence
    # the enumeration is exhaustive over all subalgebra complements.
    expected_sub={0:1,1:q*q+q+2,2:q*q+2*q+2,3:q+2,4:1}
    assert bydim==expected_sub,(q,bydim,expected_sub)
    print('PASS',q,'subalgebras',bydim,'Rota-Baxter ranks',counts,'total',sum(counts.values()))


def normalized_space(rows,q):
    A=[list(row) for row in rows]
    piv=0
    for j in range(4):
        good=next((i for i in range(piv,len(A)) if A[i][j]%q),None)
        if good is None:continue
        A[piv],A[good]=A[good],A[piv]
        inv=pow(A[piv][j],-1,q)
        A[piv]=[v*inv%q for v in A[piv]]
        for i in range(len(A)):
            if i!=piv:
                c=A[i][j]
                if c:A[i]=[(v-c*w)%q for v,w in zip(A[i],A[piv])]
        piv+=1
        if piv==len(A):break
    return tuple(tuple(row) for row in A[:piv])


def test_automorphism_orbits(q):
    z=(0,0,0,1); x=(0,1,0,0); y=(0,0,1,0)
    images=set()
    for a,b,c,d,u,v in product(range(q), repeat=6):
        det=(a*d-b*c)%q
        if not det:continue
        ix=(0,a,b,u);iy=(0,c,d,v);iz=(0,0,0,det)
        T=normalized_space((ix,iz),q)
        L=normalized_space((iy,),q)
        images.add((T,L))
    assert len(images)==q*q*(q+1),(q,len(images))
    # The orbit is exactly the incidence family; every image is a complement.
    assert all(rank(T+L,q)==3 for T,L in images)
    print('PASS',q,'aut-incidence orbit',len(images))

for q in (2,3,5):
    classify(q)
    test_automorphism_orbits(q)
