# Simple-module census of the parafermion VOA K(G2,2): 48 simples, conformal weights, top-space dimensions, and dim A = 149

## Context

Let g = G2 with simple roots (a1, a2), Cartan matrix [[2,-1],[-3,2]], invariant form (a1,a1) = 2, (a2,a2) = 2/3, (a1,a2) = -1, highest root th = 2a1 + 3a2, dual Coxeter number h^v = 4, rho = 3a1 + 5a2. At level k = 2 the affine VOA L_2(G2,0) has central charge c_aff = 2*14/(2+4) = 14/3. The rank-two Heisenberg parafermion coset C = K(G2,2) = Com(M_h(2), L_2(G2,0)) has central charge c = 14/3 - 2 = 8/3.

Level-2 integrable weights are P^2_+ = {0, w1, w2, 2w2} with w1 = (2,3), w2 = (1,2), 2w2 = (2,4) in simple-root coordinates, of affine conformal weights Delta = 0, 2/3, 1/3, 7/9. G2 has trivial center so P = Q. The long-root lattice Q_L = Z a1 + Z 3a2 has index 3 in Q, and Q/2Q_L ~= Z2 x Z6 has order 12. No Dynkin mark equals 1, so there is no simple-current identification. By Dong-Ren rationality and sector parametrization plus Ai-Dong-Jiang-Lin counting, K(G2,2) is rational with exactly |P^2_+| * |Q/2Q_L| / |P/Q| = 4 * 12 = 48 inequivalent simple modules M^{L,l}, L in P^2_+, l mod 2Q_L. Prior literature supplies these labels and counting machinery but no G2 level-2 numerical table.

## Definitions

Write classes mod 2Q_L = 2Z a1 + 6Z a2 as (i,j) = (a1 mod 2, a2 mod 6). For an affine module L_2(G2,L) let A_n(w) be the multiplicity of weight w at grade n. The Q_L-correct string functions are A_n(w) = c_[w](n - |w|^2/4) with [w] in Q/2Q_L. For each sector define F(n,w) = 36n - 9|w|^2 (equivalently 36 times the coset grade shift). The coset conformal weight is h(M^{L,l}) = Delta_L + Fmin/36 where Fmin is the minimum of F over (n,w) with w in class l and A_n(w) > 0, and the top-space dimension t is the multiplicity A at the minimizer (summed if several minimizers share Fmin).

## Result

K(G2,2) has exactly 48 simple modules with the following conformal weights h and top-space dimensions t:

- L = 0 (Delta 0): (0,0): h=0, t=1; (0,1),(0,5),(1,1),(1,2),(1,4),(1,5): h=5/6, t=1; (0,2),(0,4): h=4/3, t=3; (0,3),(1,0),(1,3): h=1/2, t=1.
- L = w1 (Delta 2/3): (0,0): h=2/3, t=2; (0,1),(0,5),(1,1),(1,2),(1,4),(1,5): h=1/2, t=1; (0,2),(0,4): h=1, t=3; (0,3),(1,0),(1,3): h=1/6, t=1.
- L = w2 (Delta 1/3): (0,0): h=1/3, t=1; (0,1),(0,5),(1,1),(1,2),(1,4),(1,5): h=1/6, t=1; (0,2),(0,4): h=2/3, t=3; (0,3),(1,0),(1,3): h=5/6, t=3.
- L = 2w2 (Delta 7/9): (0,0): h=7/9, t=3; (0,1),(0,5),(1,1),(1,2),(1,4),(1,5): h=11/18, t=2; (0,2),(0,4): h=1/9, t=1; (0,3),(1,0),(1,3): h=5/18, t=1.

By rationality the Zhu algebra A(C) is semisimple with blocks Mat_t, so dim A(C) = sum t^2 = 28 + 31 + 52 + 38 = 149. Quantum dimensions qdim(M^{L,.}) = qdim_{L_2(G2)} L(L) are 1, 1.8793852416, 2.8793852416, 2.5320888862 with global dimension 230.8130686012, consistent with 12 sectors per L. The vacuum character begins 1, 0, 6, 13, 38, 80, 182 (grades 0..6): C_2 is 6-dimensional (conformal vector plus five weight-2 primaries) and dim C_3 = 13. Consequently the open classically-free question (whether gr A(C) -> R_C is an isomorphism) is reduced to the exact numerical identity dim R_C = 149.

## Proof / evidence

Affine weight multiplicities of all four L_2(G2,L) to grade 9 were computed by Freudenthal-Kac recursion in exact rational arithmetic with level k = 2 (not k+h^v) in the affine cross terms. B-truncation audit: box B = 14 vs B = 20 agree on all grades 0..9; vacuum grade totals 1, 14, 119, 497, 1890, 5999, 17521, 46852, 118398, 283003 (grade 1 = 14 = dim G2; grade 2 = 119 = dim Sym^2(14)+14). String functions were extracted with Q_L-correct theta blocks over the 12 classes with zero consistency conflicts. In every one of the 48 sectors all F-minimizers carry one common multiplicity (verified uniform), giving t, and h follows from Delta_L + Fmin/36. The (0,0) string series (1,2,11,35,...) reconvolved with eta^2 reproduces the vacuum character 1,0,6,13,38,80,182 independently. Scripts and data (sectors.py, stringql.py, kac2.py, sectors.json, stringQL.json) reproduce the table.

## Limitations

The full target (explicit generator-relation ideals of A(C) and R_C and the classically-free verdict) is not closed: cross-root OPE data and a Groebner reduction for dim R_C remain open. The vacuum character is claimed exact only through grade 6. Top dimensions use the standard coset lowest-weight identification plus the computationally verified uniformity property.

## Reproducibility

Run output/artifacts/kac2.py and output/artifacts/stringql.py for the vacuum recursion and string extraction, and output/artifacts/sectors.py for all four affine modules and sector minima; compare against output/artifacts/sectors.json and output/artifacts/stringQL.json and the table above.

## References

- C. Dong, C. H. Lam, Q. Wang, H. Yamada, The structure of parafermion VOAs.
- C. Dong, Z. Ren, Representations of parafermion VOAs K(g,k).
- H. Ai, C. Dong, X. Jiang, W. Lin, classification, counting, quantum dimensions and fusion rules of K(g,k)-modules.
- T. Arakawa, C. H. Lam, H. Yamada, Zhu's algebra, C2-algebra and C2-cofiniteness of parafermion VOAs (sl2 presentations); arXiv:1207.3909.
- T. Arakawa, C. H. Lam, H. Yamada, Parafermion VOAs and W-algebras.
