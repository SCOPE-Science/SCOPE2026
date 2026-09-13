# Connectedness of the Heisenberg-quotient truncated point scheme V_3(Q) with singular intersection certificate

## Context

Let k be algebraically closed of characteristic neither 2 nor 3, with primitive cube root of unity w (w^2+w+1=0). Let S = S_[0:0:1] = k<x,y,z>/(x^2,y^2,z^2), the degenerate 3-dimensional Sklyanin algebra at [0:0:1]. De Laet (arXiv:1510.04024) constructs a diagonal family of Heisenberg order-27 quotients T_t = S/(v_1,v_2) with cubic relations v_1, v_2 as in Section 5.1; for t != 0, infinity these have Hilbert series 1/(1-u)^3, the same character series as k[x,y,z], and a degree-3 central element (Theorems 5.5, 5.7). De Laet classifies infinite point modules of T_t (Theorem 5.6: parametrized by 6 lines with shift automorphism) but does not compute any finite truncated point scheme V_d(Q). Walton (arXiv:0812.0609) computes V_d only for Sdeg itself. The finite-level scheme V_3(Q), its components, incidence, and singularities were unknown.

## Definitions

Fix t = 1, so Q = T_1 with A = B = 1: v_1 = (zxy + w xyz + w^2 yzx) + (yxz + w zyx + w^2 xzy), v_2 = (zxy + w^2 xyz + w yzx) + (yxz + w^2 zyx + w xzy). Fix d = 3: truncated point modules of length 4, i.e. triples of points of P^2. Write X_i, Y_i, Z_i (i = 0,1,2) for coordinates on the three P^2 factors. Let V = V(XYZ) in P^2 with lines L_0 = V(X), L_1 = V(Y), L_2 = V(Z) and nodes q_0 = [1:0:0], q_1 = [0:1:0], q_2 = [0:0:1].

## Result

For Q = T_1 as above, the reduced truncated point scheme (V_3(Q))_red in (P^2_k)^3 is connected. Precisely, (V_3(Q))_red is the union of six smooth rational curves E_0, E_1, E_2, D_0, D_1, D_2 with pairwise incidence exactly K_{3,3} minus a perfect matching (a 6-cycle E_0-D_1-E_2-D_0-E_1-D_2-E_0). The closed point P = ([0:1:0],[1:0:0],[0:1:0]) lies on exactly the two distinct components E_0 and D_1, where the affine-chart Jacobian has exact rank 4 (4x4 identity minor, det +/-1), so the Zariski tangent space has dimension 2 exceeding the local dimension 1: P is a singular intersection point of two components. This completes admitted alternative (A).

## Proof / evidence

V_3(Q) is cut out by 6 multilinearized quadrics X_j X_{j+1} = Y_j Y_{j+1} = Z_j Z_{j+1} = 0 (j = 0,1) and 2 cubics f_1, f_2 (multilinearizations of v_1, v_2). The pair locus W in P^2 x P^2 has 6 components A_i = {q_i} x L_i, B_i = L_i x {q_i}. Intersecting pair conditions for (0,1) and (1,2) gives 6 components C_i = L_i x {q_i} x L_i and D_i = {q_i} x L_i x {q_i}. On C_0 both cubics restrict to Z_0 Y_2 + Y_0 Z_2 (smooth (1,1) curve E_0); on C_1 to w resp. w^2 times X_0 Z_2 + Z_0 X_2 (curve E_1); on C_2 to w^2 resp. w times X_0 Y_2 + Y_0 X_2 (curve E_2). Each D_j lies wholly in V_3 by a per-monomial zero-factor check. Incidence: E_i meets D_j iff i != j at (q_j, q_i, q_j); E_i's and D_j's are pairwise disjoint; E_i cap D_i is empty since q_i is not on L_i. Hence the dual graph is connected. In chart Y_0 = X_1 = Y_2 = 1 at P (the origin), the linear parts are d(X_0X_1) = a_0, d(Y_0Y_1) = b_1, d(X_1X_2) = a_2, d(F_1) = d(F_2) = c_0 + c_2, with Z-quadrics vanishing to second order: the 4x4 identity minor in columns (a_0,b_1,c_0,a_2) gives rank exactly 4, tangent dimension 6-4 = 2, with distinct branch tangents for E_0 and D_1. Every step is rechecked exactly over Z[w]/(w^2+w+1) by output/artifacts/verify_v3.py.

## Limitations

Proved only for the fixed quotient Q = T_1 (t = 1) of S_[0:0:1]; other diagonal parameters t, Zhang-twisted S_[1:0:0] quotients, SL_2(3)-orbit translates, and higher levels d > 3 are not treated. Requires characteristic not 2 or 3 and a primitive cube root of unity.

## Reproducibility

Run `python3 output/artifacts/verify_v3.py`; it performs exact Eisenstein-integer checks A-F (restrictions, containment, membership, full incidence, Jacobian) and writes verify_results.txt ending in ALL EXACT CHECKS PASSED.

## References

- K. De Laet, Quotients of degenerate Sklyanin algebras, arXiv:1510.04024 (J. Algebra 2017).
- C. Walton, Degenerate Sklyanin algebras and Generalized Twisted Homogeneous Coordinate rings, arXiv:0812.0609 (J. Algebra 2009); corrigendum arXiv:1112.5211.
- S. P. Smith, Degenerate 3-dimensional Sklyanin algebras are monomial algebras, J. Algebra 2012.
