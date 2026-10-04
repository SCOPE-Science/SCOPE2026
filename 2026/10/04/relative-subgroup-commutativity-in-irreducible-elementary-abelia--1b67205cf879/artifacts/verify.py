from itertools import product, combinations
from fractions import Fraction

def eye(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def mat_mul(A, B, p):
    n = len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) % p for j in range(n)) for i in range(n))

def mat_pow(A, e, p):
    R = eye(len(A))
    while e:
        if e & 1:
            R = mat_mul(R, A, p)
        A = mat_mul(A, A, p)
        e >>= 1
    return R

def mat_vec(A, v, p):
    return tuple(sum(A[i][j]*v[j] for j in range(len(v))) % p for i in range(len(v)))

def vadd(v, w, p):
    return tuple((a+b) % p for a,b in zip(v,w))

def span(gens, p, r):
    if not gens:
        return frozenset({(0,)*r})
    out = set()
    for coeffs in product(range(p), repeat=len(gens)):
        v = [0]*r
        for c,g in zip(coeffs, gens):
            for i in range(r):
                v[i] = (v[i] + c*g[i]) % p
        out.add(tuple(v))
    return frozenset(out)

def all_subspaces(p, r):
    V = list(product(range(p), repeat=r))
    nonzero = [v for v in V if any(v)]
    spaces = {span([],p,r)}
    for k in range(1,r+1):
        for gens in combinations(nonzero,k):
            spaces.add(span(gens,p,r))
    return sorted(spaces, key=lambda S:(len(S),sorted(S)))

def check_case(p, r, q, A):
    acts = [mat_pow(A,j,p) for j in range(q)]
    assert acts[0] == eye(r) and acts[-1] != acts[0]
    assert mat_pow(A,q,p) == eye(r)
    Vectors = list(product(range(p), repeat=r))
    z = (0,)*r

    def mul(g,h):
        v,i = g
        w,j = h
        return (vadd(v, mat_vec(acts[i],w,p), p), (i+j)%q)

    def cyclic(g):
        e=(z,0); H={e}; x=e
        while True:
            x=mul(x,g)
            if x==e: break
            H.add(x)
        return frozenset(H)

    spaces = all_subspaces(p,r)
    invariant = [U for U in spaces if frozenset(mat_vec(A,v,p) for v in U)==U]
    assert len(invariant)==2

    space_groups = [frozenset((v,0) for v in U) for U in spaces]
    complements = [cyclic((v,1)) for v in Vectors]
    assert all(len(C)==q for C in complements)
    assert len(set(complements)) == p**r
    complements = list(dict.fromkeys(complements))
    G = frozenset((v,j) for v in Vectors for j in range(q))
    subgroups = space_groups + complements + [G]
    assert len(subgroups) == len(spaces)+p**r+1
    assert len(set(subgroups)) == len(subgroups)

    for H in subgroups:
        e=(z,0)
        assert e in H
        for x in H:
            for y in H:
                assert mul(x,y) in H

    def setprod(H,K):
        return frozenset(mul(h,k) for h in H for k in K)

    perm = {}
    for H in subgroups:
        for K in subgroups:
            perm[(H,K)] = (setprod(H,K)==setprod(K,H))

    s=len(spaces); P=p**r; L=s+P+1
    def s_count(d): return len(all_subspaces(p,d))

    for H in subgroups:
        LH=[K for K in subgroups if K.issubset(H)]
        num=sum(1 for K in LH for J in subgroups if perm[(K,J)])
        got=Fraction(num,len(LH)*L)
        if H==G:
            want=Fraction(s*s+2*s+7*P+1,L*L)
        elif all(j==0 for _,j in H):
            size=len(H); d=0; zsize=size
            while zsize>1:
                assert zsize%p==0
                zsize//=p; d+=1
            if d==0:
                want=Fraction(1,1)
            elif d==r:
                want=Fraction(s*(s+1)+2*P,s*L)
            else:
                sd=s_count(d)
                want=Fraction(sd*(s+1)+P,sd*L)
        else:
            assert len(H)==q
            want=Fraction(L+4,2*L)
        assert got==want,(p,r,q,len(H),got,want)

    counts=sorted(sum(perm[(H,K)] for K in subgroups) for H in subgroups)
    expected=sorted([L,L,L]+[s+1]*(s-2)+[4]*P)
    assert counts==expected

A_223=((0,1),(1,1))
A_237=((0,0,1),(1,0,1),(0,1,0))
A_523=((0,4),(1,4))

for case in [(2,2,3,A_223),(2,3,7,A_237),(5,2,3,A_523)]:
    check_case(*case)

print("VERIFY_OK")
