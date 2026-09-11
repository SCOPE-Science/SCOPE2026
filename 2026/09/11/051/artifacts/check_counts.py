"""Exhaustive multiplicity-m=2 degree-count feasibility scan for lane-831 window.

Window: base RS [n=64,k=16]/F257, folded s=4 -> N=16 bundles, rate 1/4.
Radius rho=0.52 -> folded agreements t_f >= N*(1-rho)=7.68 -> t_f=8 (errors<=8).
Unfolded agreements t_u >= 64*0.48=30.72 -> t_u=31.
Multiplicity m=2. Standard GS unique-decoder implication needs l<m and t*(m-l) > D.

Scans:
 A) bivariate Q(X,Y), (1,k-1)-weighted deg<=D, Y-deg<=l, on unfolded n=64
    coeffs = sum_{j=0..l} max(0, D-j*(k-1)+1); conds = n*m(m+1)/2 = 192.
 B) bivariate Q(X,Y) on N=16 bundle points: conds = 48, t=8.
 C) (s+1)-variate GR-type Q(X,Y1..Ys), X-deg<=D, total Y-deg<=l (MOST GENEROUS:
    ignores the (k-1)*l degree penalty of the true GR weighted bound, so failure
    here implies failure under the true stricter count):
    coeffs = (D+1)*C(l+s,s); conds = N*C(m+v-1,v), v=s+1=5 -> 6 per point -> 96.
    decoding generous: D < t*(m-l), t=8.
 D) Johnson baseline check: N=16, max pairwise bundle-agreement 3, min agreement 8
    -> second-moment bound on L (analytic + numeric verify).
"""
import math

K = 16
KM1 = K - 1
M = 2
N_FOLD = 16
N_UNF = 64
S = 4
T_F = 8
T_U = 31

def bivar_coeffs(D, l):
    tot = 0
    for j in range(l + 1):
        rem = D - j * KM1 + 1
        if rem > 0:
            tot += rem
    return tot

def scan_bivar(npts, conds, t, Dmax, lmax, tag):
    feas = []
    for l in range(lmax + 1):
        for D in range(Dmax + 1):
            c = bivar_coeffs(D, l)
            exist = c > conds
            if l < M:
                dec = (t * (M - l) > D)
            else:
                dec = False
            if exist and dec:
                feas.append((D, l, c))
    print(f"== {tag}: conds={conds}, t={t}, D<={Dmax}, l<={lmax} -> feasible pairs: {feas if feas else 'NONE'}")
    return feas

def scan_multivar(Dmax, lmax):
    v = S + 1
    per = math.comb(M + v - 1, v)  # C(6,5)=6
    conds = N_FOLD * per
    feas = []
    for l in range(lmax + 1):
        for D in range(Dmax + 1):
            c = (D + 1) * math.comb(l + S, S)
            exist = c > conds
            dec = (l < M) and (T_F * (M - l) > D)
            if exist and dec:
                feas.append((D, l, c))
    print(f"== multivar GR-type (generous): conds={conds} ({N_FOLD}x{per}), t={T_F} -> feasible: {feas if feas else 'NONE'}")
    return feas

def johnson_check():
    N, Amax, Amin = 16, 3, 8
    # f(S)=S^2/N - S increasing for S>=N/2; S>=Amin*L; pairwise cap Amax.
    # Bound: f(Amin*L) <= Amax*L*(L-1) -> 4L^2-8L <= 3L(L-1) -> L<=5.
    ok = True
    for L in range(1, 40):
        S = Amin * L
        lhs = S * S / N - S
        rhs = Amax * L * (L - 1)
        holds = lhs <= rhs  # necessary condition for L codewords to coexist
        if L <= 5:
            assert holds, L
        if L >= 6 and holds:
            print(f"   L={L}: counting does NOT exclude (lhs={lhs}, rhs={rhs})")
            ok = False
    # check the threshold: L=6 -> lhs=4*36-48=96, rhs=3*6*5=90 -> 96<=90 false -> excluded
    L = 6
    S = Amin * L
    print(f"== Johnson: L=6 gives {S**2/N - S} <= {Amax*L*(L-1)} ? {(S**2/N - S) <= Amax*L*(L-1)} (False => L>=6 impossible, so L<=5)")
    # folded distance sanity: floor((k-1)/s)=floor(15/4)=3 full bundles max
    print(f"== folded distance: max pairwise bundle-agreement = floor(15/4) = {15//4}; distance >= {N_FOLD - 15//4} bundles")
    # folded q-ary Johnson radius for ref: 1-sqrt(1-13/16)=1-sqrt(3/16)
    import math as m
    print(f"== folded Johnson radius approx 1-sqrt(1-13/16) = {1 - m.sqrt(1 - 13/16):.4f} (>0.52)")

if __name__ == "__main__":
    print("lane-831 m=2 feasibility scan")
    a = scan_bivar(N_UNF, N_UNF * M * (M + 1) // 2, T_U, 600, 6, "A) bivar unfolded [64,16]")
    b = scan_bivar(N_FOLD, N_FOLD * M * (M + 1) // 2, T_F, 600, 6, "B) bivar folded-bundle N=16")
    c = scan_multivar(600, 8)
    johnson_check()
    print("RESULT:", "BLOCKED (no feasible (D,l) in any scan)" if (not a and not b and not c) else "FEASIBLE PAIR EXISTS")
