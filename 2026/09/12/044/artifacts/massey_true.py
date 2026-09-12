"""Massey vanishing on TRUE K (MNF = {01},{23},{45678}).
Classes: a=[01] (H^3), b=[23] (H^3), c=[45678] (H^9); products: ab=[0123] (H^6), ac=[0145678] (H^12), bc=[2345678] (H^12), abc=[top] (H^15).
Triple Massey <a,a,b>? a^2=0 (odd degree) but need ab=0: ab != 0. <a,b,a>? ab!=0. Only defined if pairwise products zero: pairs among {a,b}: ab!=0. Pairs with c: ac,bc != 0 (dim reasons: nonzero classes). So NO triple Massey with all pair-products zero exists among positive-degree classes except those involving... any triple (x,y,z) with |x|,|y|,|z|>0: check degrees: H^3,H^6,H^9,H^12: products of positive classes land in H^>=6... x*y=0 iff degree sum > 15 or complementary... e.g. H^6 * H^9 = H^15? = top (nonzero if dual). H^3*H^12 = top nonzero. H^6*H^6 = H^12? = (ab)*(ab) = a^2 b^2 = 0 (a^2=0 since |a| odd: graded commutativity a^2 = -a^2 -> 2a^2=0 -> 0 over Q). So (ab,ab): product zero! Triple <ab, ab, x>? need (ab)*x=0 too: <ab,ab,a>: (ab)*a = 0 (a^2=0) ✓ and a*(ab)=0 ✓. So <u,u,a> with u=ab (H^6), a (H^3): defined? u*u = 0 ✓, u*a = 0 ✓. Massey <u,u,a>: cocycle degree 6+6+3-1 = 14: H^14 = 0! -> trivially zero. Similarly all defined triples land in zero groups or are zero. General fact: H* = exterior on 2 gens (deg3) tensor polynomial-ish on deg9 (truncated: c^2=0 since H^18=0): H* = Lambda(a,b) tensor Lambda(c). Triple Masseys in a FORMAL (product-of-spheres) cohomology: the space is formal so all vanish; directly: any defined triple has value in H^{|x|+|y|+|z|-1}: enumerate possibilities.
We verify computationally: enumerate all triples of COHOMOLOGY BASIS elements with pairwise products zero, compute Massey cocycle, check boundary. Also verify formality via minimal model: H* is a complete intersection / product of spheres -> formal.
"""
from fractions import Fraction
from itertools import combinations, product as iproduct

N = 9
MNF = [{0,1},{2,3},{4,5,6,7,8}]
def is_face(S):
    St = set(S)
    return not any(set(G).issubset(St) for G in MNF)

# Koszul cognomi: reuse routines (copy minimal set)
def basis_trideg(neg_i, J):
    J = set(J); out = []
    r = -neg_i
    if r < 0: return []
    for L in combinations(sorted(J), r):
        rest = tuple(sorted(J - set(L)))
        if is_face(rest):
            out.append((frozenset(L), rest))
    return out

def sign_u(L, x):
    return (-1) ** sum(1 for y in sorted(L) if y < x)

def diff(m):
    L, B = set(m[0]), tuple(m[1])
    terms = {}
    for x in sorted(L):
        L2 = frozenset(y for y in L if y != x)
        B2 = tuple(sorted(tuple(B) + (x,)))
        if is_face(B2):
            terms[(L2, B2)] = terms.get((L2, B2), Fraction(0)) + Fraction(sign_u(L, x))
    return terms

def mul(m1, m2):
    L1, B1 = set(m1[0]), list(m1[1]); L2, B2 = set(m2[0]), list(m2[1])
    if L1 & L2: return {}
    s = 1
    for x in sorted(L2):
        for y in sorted(L1):
            if y > x: s *= -1
    from collections import Counter
    e = Counter(); e.update(B1); e.update(B2)
    if not is_face(set(e.keys())): return {}
    return {(frozenset(L1 | L2), tuple(sorted(e.elements()))): Fraction(s)}

def mulvec(v, w):
    out = {}
    for m1, c1 in v.items():
        for m2, c2 in w.items():
            for k, s in mul(m1, m2).items():
                out[k] = out.get(k, Fraction(0)) + c1*c2*s
    return {k: x for k, x in out.items() if x != 0}

def homology_basis(neg_i, J):
    C = basis_trideg(neg_i, J); Cout = basis_trideg(neg_i+1, J); Cin = basis_trideg(neg_i-1, J)
    S_out = set(Cout)
    Mo = {}
    for m in C:
        for k, v in diff(m).items():
            if k in S_out: Mo[(k, m)] = Mo.get((k, m), Fraction(0)) + v
    R = list(Cout); Cc = list(C)
    ri = {r: i for i, r in enumerate(R)}; ci = {c: j for j, c in enumerate(Cc)}
    A = [[Fraction(0)]*len(Cc) for _ in R]
    for (r, c), v in Mo.items(): A[ri[r]][ci[c]] = v
    piv_of_col = {}; row = 0
    for c in range(len(Cc)):
        piv = next((i for i in range(row, len(R)) if A[i][c] != 0), None)
        if piv is None: continue
        A[row], A[piv] = A[piv], A[row]
        iv = A[row][c]
        for j in range(c, len(Cc)): A[row][j] /= iv
        for i in range(len(R)):
            if i != row and A[i][c] != 0:
                f = A[i][c]
                for j in range(c, len(Cc)): A[i][j] -= f*A[row][j]
        piv_of_col[c] = row; row += 1
    free = [c for c in range(len(Cc)) if c not in piv_of_col]
    cycles = []
    for f in free:
        v = {Cc[f]: Fraction(1)}
        for c, r in piv_of_col.items():
            if A[r][f] != 0: v[Cc[c]] = v.get(Cc[c], Fraction(0)) - A[r][f]
        cycles.append({k: x for k, x in v.items() if x != 0})
    S = set(C)
    bounds = []
    for m in Cin:
        t = {k: v for k, v in diff(m).items() if k in S}
        if t: bounds.append(t)
    return C, cycles, bounds

def is_boundary(vec, C, bounds):
    if not vec: return True
    keys = list(dict.fromkeys(list(vec.keys()) + [k for b in bounds for k in b.keys()]))
    R = list(keys); nB = len(bounds)
    A = [[bounds[j].get(R[i], Fraction(0)) for j in range(nB)] for i in range(len(R))]
    rhs = [vec.get(R[i], Fraction(0)) for i in range(len(R))]
    M = [A[i][:] + [rhs[i]] for i in range(len(R))]
    row = 0; where = [-1]*nB
    for c in range(nB):
        piv = next((i for i in range(row, len(R)) if M[i][c] != 0), None)
        if piv is None: continue
        M[row], M[piv] = M[piv], M[row]
        iv = M[row][c]
        for j in range(c, nB+1): M[row][j] /= iv
        for i in range(len(R)):
            if i != row and M[i][c] != 0:
                f = M[i][c]
                for j in range(c, nB+1): M[i][j] -= f*M[row][j]
        where[c] = row; row += 1
    for i in range(len(R)):
        if all(M[i][j] == 0 for j in range(nB)) and M[i][nB] != 0: return False
    return True

def cohom_basis(J, ni):
    C, cyc, bnd = homology_basis(ni, tuple(J))
    if not C or not cyc: return C, [], bnd
    def rrank(vecs):
        ci = {c: j for j, c in enumerate(C)}
        Mm = [[Fraction(0)]*len(C) for _ in vecs]
        for i, b in enumerate(vecs):
            for k, v in b.items():
                if k in ci: Mm[i][ci[k]] = v
        A = [row[:] for row in Mm]; r = 0
        for c in range(len(C)):
            piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
            if piv is None: continue
            A[r], A[piv] = A[piv], A[r]
            iv = A[r][c]
            for j in range(c, len(C)): A[r][j] /= iv
            for i in range(len(A)):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    for j in range(c, len(C)): A[i][j] -= f*A[r][j]
            r += 1
        return r
    basis = []
    for v in cyc:
        if rrank(list(bnd)+basis+[v]) > rrank(list(bnd)+basis): basis.append(v)
    return C, basis, bnd

def solve_prim(a, b, Cpb, Cin):
    ab = mulvec(a, b)
    R = list(Cpb); ri = {r: i for i, r in enumerate(R)}
    cols = list(Cin)
    A = [[Fraction(0)]*len(cols) for _ in R]
    for j, m in enumerate(cols):
        for k, v in diff(m).items():
            if k in ri: A[ri[k]][j] += v
    rhs = [ab.get(r, Fraction(0)) for r in R]
    M = [A[i][:] + [rhs[i]] for i in range(len(R))]
    nrows, ncols = len(R), len(cols)
    where = [-1]*ncols; row = 0
    for c in range(ncols):
        piv = next((i for i in range(row, nrows) if M[i][c] != 0), None)
        if piv is None: continue
        M[row], M[piv] = M[piv], M[row]
        iv = M[row][c]
        for j in range(c, ncols+1): M[row][j] /= iv
        for i in range(nrows):
            if i != row and M[i][c] != 0:
                f = M[i][c]
                for j in range(c, ncols+1): M[i][j] -= f*M[row][j]
        where[c] = row; row += 1
    for i in range(nrows):
        if all(M[i][j] == 0 for j in range(ncols)) and M[i][ncols] != 0: return None
    t = [Fraction(0)]*ncols
    for c in range(ncols):
        if where[c] != -1: t[c] = M[where[c]][ncols]
    return {m: t[j] for j, m in enumerate(cols) if t[j] != 0}

# Cohomology basis: only 8 classes. Get them.
supps = [((0,1),-1),((2,3),-1),((4,5,6,7,8),-1),((0,1,2,3),-2),((0,1,4,5,6,7,8),-2),
         ((2,3,4,5,6,7,8),-2),((0,1,2,3,4,5,6,7,8),-3)]
basis = {}
for J, ni in supps:
    C, b, bnd = cohom_basis(J, ni)
    basis[(J,ni)] = (C, b, bnd)
    print(J, ni, "dim:", len(b), "rep:", {str(k): str(v) for k,v in (b[0].items() if b else {})})
print("total:", sum(len(v[1]) for v in basis.values()))

# All triples of basis classes, pairwise products zero -> defining system -> essential?
keys = list(basis.keys())
n = 0; ndef = 0
for ka in keys:
    for kb in keys:
        for kc in keys:
            (Ja,na),(Jb,nb),(Jc,nc) = ka,kb,kc
            if na==0 or nb==0 or nc==0: continue  # positive-degree only (skip unit)
            for av in basis[ka][1]:
                for bv in basis[kb][1]:
                    Jab=tuple(sorted(set(Ja)|set(Jb)))
                    Ca,_,ba = homology_basis(na+nb,Jab)
                    if not is_boundary(mulvec(av,bv),Ca,ba): continue
                    for cv in basis[kc][1]:
                        Jbc=tuple(sorted(set(Jb)|set(Jc)))
                        Cb,_,bb = homology_basis(nb+nc,Jbc)
                        if not is_boundary(mulvec(bv,cv),Cb,bb): continue
                        n += 1
                        x = solve_prim(av,bv,Ca,basis_trideg(na+nb-1,Jab))
                        y = solve_prim(bv,cv,Cb,basis_trideg(nb+nc-1,Jbc))
                        if x is None or y is None: print("PRIM FAIL",ka,kb,kc); continue
                        ndef += 1
                        dega = 2*len(Ja)+na
                        m = {}
                        for k,v in mulvec(x,cv).items(): m[k]=m.get(k,Fraction(0))+((-1)**dega)*v
                        for k,v in mulvec(av,y).items(): m[k]=m.get(k,Fraction(0))+v
                        Jabc=tuple(sorted(set(Ja)|set(Jb)|set(Jc)))
                        Cun,_,bun = homology_basis(na+nb+nc+1,Jabc)
                        ess = not is_boundary(m,Cun,bun)
                        print("triple",ka,kb,kc,"cocycle:",{str(k):str(v) for k,v in m.items()},"ESSENTIAL:",ess)
print("defined triples:",n,"with prims:",ndef)
