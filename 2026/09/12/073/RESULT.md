# H^2 of ordered configuration spaces of the once-punctured torus: exact weight-3 character polynomial and sharp onset

## Context

Let T* = T^2 minus one point (equivalently a smooth affine elliptic curve over C, also written T^circ, E^x, Sigma_{1,1}) and F_n(T*) the ordered configuration space of n distinct points with S_n permuting labels. Work over Q and put V_n = H^2(F_n(T*); Q). Write X_k(sigma) for the number of k-cycles of sigma in S_n; X_k has weight k. Church-Ellenberg-Farb and Miller-Wilson representation stability predicts that characters of such FI-modules are eventually given by character polynomials; Wawrykow and Pagaria established the Betti growth b_2(F_n(T*)) = 2C(n,3)+5C(n,2), and Cheong-Huang computed unordered Betti/Hodge generating functions. None of these gives the ordered S_n character. The admitted target asked for the minimal stable-range integer N_2 and explicit weight-3 polynomial P_2, in particular whether N_2 = 6.

## Definitions

Totaro (Cohen-Taylor) E_2 page: E_2 = H*((T*)^n)[G_ij]/(Arnold, sliding) with G_ij = G_ji of bidegree (0,1), Arnold relations G_ij G_jk + G_jk G_ki + G_ki G_ij = 0, sliding relations (x_i - x_j)G_ij = 0 for x in H^1, differential d(G_ij) = Delta_ij := a_i b_j - b_i a_j in H^2((T*)^n), d|_{H*} = 0. H*(T*;Q) = Lambda(a,b) with H^2(T*) = 0, so H*((T*)^n) = Lambda(a_1,b_1,...,a_n,b_n)/<a_i b_i>. Total degree 2 has bidegrees (2,0), (1,1), (0,2). E_3 = H(E_2, d); over Q, S_n-representations are semisimple so H^2 splits as the direct sum of the E_infinity pieces.

## Result

Theorem. Let

P_2 = (1/3) X_1^3 + 2 X_1 X_2 + 2 X_3 + (3/2) X_1^2 - X_2 - (11/6) X_1 + 0.

Then: (1) P_2(n,0,...) = n^3/3 + 3n^2/2 - 11n/6 = 2C(n,3) + 5C(n,2) for every n. (2) For every n >= 0 and every sigma in S_n, chi_{V_n}(sigma) = P_2(X_1(sigma), X_2(sigma), ...); in particular the identity holds for all n >= N* with sharp onset N* = 0 (vacuous at n = 0, 1, non-vacuous for n >= 2; values 5, 17, 38, 70, 115, 175 at n = 2..7). (3) The proposed minimal stable range N_2 = 6 is FALSE as a character-polynomial onset: P_2 never fails, so no N* admits a weight-3-polynomial failure at N*-1. The value 6 is consistent only with uniform representation-stability (multiplicity stability), a different invariant that onsets later. (4) In FI language the E_2 algebra is generated in FI-degree <= 2, presented in degree <= 3 (Arnold on triples, sliding in degree 2), with page-2 differential determined in degree 2; the triple direct-sum decomposition propagates this to all n.

## Proof / evidence

Bidegree (2,0): Delta_ij are linearly independent (each uses basis monomials a_i b_j, a_j b_i occurring in no other Delta), so d^{0,1} is injective of rank C(n,2); dim E_3^{2,0} = dim H^2((T*)^n) - C(n,2) = 3C(n,2) since dim H^2 = C(2n,2)-n = 2n(n-1). Character: tr H^2 = 4C(X_1,2) - 2X_2 (both-fixed pairs contribute +1 in each of four families; transposed pairs contribute -1,-1,0), tr E_2^{0,1} = C(X_1,2)+X_2 (fixed edges), difference E^{2,0} = (3/2)(X_1^2-X_1) - 3X_2.

H^3((T*)^n) is a triple direct sum: degree-3 exterior monomials at 2 points all contain some a_i b_i = 0, so survivors have one generator at each of three distinct points, 8 per triple, dim 8C(n,3). Character H^3 = 8C(X_1,3) - 4X_1X_2 + 2X_3 (local traces +8 identity, -4 transposition, +2 3-cycle; transposition sign verified by direct computation).

Bidegree (1,1): F^{1,1} = H^1 tensor span{G_ij}, f(h tensor G_ij) = h cup Delta_ij; E_2^{1,1} = F^{1,1}/R with 2C(n,2) sliding relations in ker f, independent per edge. Rank lemma: rank(f) = 4C(n,3) for every n, because h supported on {i,j} cups Delta_ij to a vanishing 2-point degree-3 monomial, so the map splits over triples with independent codomains, and each local rank is 4 by exact rational computation at n = 3 (local_rank3.py). Hence dim E_3^{1,1} = 2nC(n,2) - 4C(n,3) - 2C(n,2) = 2C(n,3)+2C(n,2). Character: tr(R) = 2C(X_1,2)-2X_2; tr(F^{1,1}) = 2X_1(C(X_1,2)+X_2); local cokernel per triple is 4-dimensional with traces (4,-4,4) over Q (local_rank3.py), so tr(coker f) = 4C(X_1,3)-4X_1X_2+4X_3; combining gives E^{1,1} = (1/3)X_1^3+2X_1X_2+2X_3+2X_2-(1/3)X_1. Sum E^{2,0}+E^{1,1} = P_2 with constant term 0.

Vanishing E_3^{0,2} = 0: ker(d^{0,2}: E_2^{0,2} -> E_2^{2,1}) = 0 for every n (Lemma 8). Edge-projection: coefficients on edges disjoint from the projection edge vanish (no sliding relator of g is supported on a disjoint edge e); hence every class involves only sharing pairs. Triple restriction then reduces to the n = 3 base case, where exact rational computation (l2_base.py) gives injectivity (rank difference 2 = dim E_2^{0,2}(K_3)); restriction preserves NBC expansions so all sharing-pair coefficients vanish. Computed ker(d02) = 0 for 2 <= n <= 8 (dim E_2^{0,2} = 322 injects at n = 8).

Degeneration and descent: on pages r >= 3 every differential into or out of total degree 2 has source or target with p < 0 or q < 0 except d_3: E_3^{0,2} -> E_3^{3,0} with source 0; thus E_3^{tot 2} = E_infinity^{tot 2} (Totaro degeneration for smooth complex varieties). Over Q semisimplicity gives V_n = E_3^{2,0} + E_3^{1,1} as S_n-modules with character P_2 for every n >= 0. All matrices are integral; the three local facts were verified over Q and all character values additionally mod primes 1000003 and 1000033.

Machine verification: dims through n = 9 match 2C(n,3)+5C(n,2); full S_n character tables for 2 <= n <= 7 (43 conjugacy classes across those n; 56 class-slots in the report's counting) all agree with P_2; class-function constancy, nonneg-integral S_4 multiplicities (4,0,7,3,2), S_5-to-S_4 restriction, and n = 2 Gysin hand-check (3+2 = 5) all pass.

## Limitations

General-n E_3^{0,2} vanishing invokes standard Arnold-algebra NBC-basis facts (broken circuits, restriction preserving NBC expansions). Totaro E_3 = E_infinity degeneration for the smooth quasi-projective punctured torus is cited as the known theorem. Machine evidence combines exact QQ arithmetic for local lemmas with finite-field linear algebra at n <= 9 and two-prime agreement. S_n multiplicity stability (uniform representation stability) onsets later than the character-polynomial onset 0; the two notions must not be conflated.

## Reproducibility

Run in output/artifacts: python3 explore_dims.py (dims and ranks), python3 local_rank3.py and python3 l2_base.py (exact QQ local lemmas; need sympy), python3 compute_d02.py and python3 dims89.py (vanishing and n = 8, 9 dims), python3 twoprime.py and char_table.py with characters.py (character tables and two-prime agreement over Fp with p = 1000003, 1000033).

## References

Totaro, Configuration spaces of algebraic varieties, Topology 1996. Church-Ellenberg-Farb, FI-modules over Noetherian rings, Geom. Topol. 2015. Miller-Wilson, Higher-order representation stability and ordered configuration spaces of manifolds, Geom. Topol. 2019. Pagaria, cohomology of configuration spaces of the torus. Wawrykow arXiv:2008.11766 (secondary stability, once-punctured torus). Cheong-Huang arXiv:2009.07976 / Trans. AMS 2022 (unordered punctured-elliptic-curve Betti/Hodge functions). Huang arXiv:2011.07153 (punctured-variety splitting). Huang-Ramos arXiv:2507.09746 (punctured-surface Hilbert series).
