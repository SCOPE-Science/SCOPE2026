# Low-degree exterior-square twisted (co)homology of configuration spaces of CP^2#CP^2

## Context
Let M = CP^2 # CP^2, the closed simply connected 4-manifold with b_2 = 2 and
intersection form diag(1,1). Let F_k(M) be the ordered configuration space of k
distinct points, B_k(M) = F_k(M)/S_k the unordered configuration space, and
W_k = Lambda^2(Q^k/Q) the exterior square of the reduced permutation
representation over Q (dim (k-1)(k-2)/2, W_2 = 0). This is a degree-2 polynomial
(FI) coefficient system on B_k(M) via the covering F_k -> B_k. Twisted
homological stability for simply connected closed 4-manifolds with degree-2
coefficients has almost no exact low-degree tables; general theorems (Palmer,
FI-theory) give qualitative ranges but no concrete integers for this manifold
and system. The admitted target asked for a slope-2 range k >= 2i+3 plus a
single-pair sharpness witness; that full target is blocked, and the present
record is the verified low-degree truncation that constrains any future proof.

## Definitions
- Cohomology ring: H^*(M;Q) = Q[a,b,pt]/(a^2-pt, b^2-pt, ab, a pt, b pt, pt^2),
  |a|=|b|=2, |pt|=4.
- Kriz / Idrissi-Lambrechts-Stanley small model of F_k(M): H^*(M^k) with
  degree-3 generators G_ij (i<j) and differential
  d(G_ij) = Delta_ij = pt_i + pt_j + a_i a_j + b_i b_j.
- Over Q, H_i(B_k;W_k) is dual to the S_k-invariant part of
  H^i(F_k;Q) tensor W_k, i.e. H_0(S_k; H_i(F_k) tensor W_k).
- Graded pieces used: H^2(M^k) (a_i,b_i); G = span(G_ij); H^4(M^k):
  pt_i (P), a_i a_j / b_i b_j (A/B), a_i b_j ordered i/=j (C);
  C5 = H^2 tensor G (domain of D in degree 5);
  A6 = degree-6 part of H^*(M^k): pt_i a_j, pt_i b_j (PA/PB) plus triple
  products (T). The Lambda^2(G)/Arnold summand of H^6 is excluded throughout.

## Result (emergent finding)
Over Q, with the notation above:
1. Vanishing: H_0(B_k;W_k) = 0 for k = 2 (W_2 = 0) and all k >= 3
   (coinvariants of W_k vanish); H_1 = 0 for all k (F_k simply connected);
   H_2 = 0 for all k (<H_2(M^k),W> = 0); H_3 = 0 for all k (every G tensor W
   orbit sum is the zero vector; <G,W> = 0).
2. H_4: dim H_4(B_2;W_2) = 0; dim = 1 for every k >= 3, spanned by the C-type
   a_i b_j orbit-sum family. The G tensor W contribution vanishes so im(D)=0.
3. H_5: quotiented (Kriz-relation) H^5-twisted = 0 for 3 <= k <= 7.
   Unquotiented (H^2 tensor G) tensor W invariants have rank 4 (k >= 4; rank 2
   at k = 3); the Kriz-relation subspace has full rank 6,36,120,300,630 at
   k = 3,4,5,6,7 with D(R) = 0; dim(I cap R) = 2 and rank(D|_I) = 2, giving
   (4-2)-2 = 0 (and (2-0)-2 = 0 at k = 3).
4. H_6 A6-piece: inv(A6 tensor W) has rank 2 (k = 3), 4 (k = 4..7) with image
   rank 0 (k = 3), 2 (k >= 4), contributing dimension 2,2,2,2 for k = 3..6
   (Arnold summand excluded; H_6 total not claimed).
5. Boundary probe (H_4 only): at the target sharpness boundary k = 2i+2 for
   i = 4 (k = 10 -> 11), both H_4-twisted sides are 1-dimensional with zero
   differentials (exact Gram rank 1 at k = 10,11). Quotiented H_5 vanishing is
   proved only for 3 <= k <= 7; at k = 10,11 only the unquotiented H_5
   character count 4 is known, so no H_5 boundary equality is claimed.

## Proof / evidence
Transfer + character theory: exact conjugacy-class sums give
chi_W from fix counts, chi_G = C(f,2)+m2, chi_H2 = 2f,
chi_H4 = f + 2G + f(f-1); inner products give <W,1> = 0 (k >= 3),
<H2,W> = <G,W> = 0 and <H4,W> = 1, extended from n <= 12 to all n >= 4 by
stable joint falling moments E[(f)_a (m2)_b] = 2^-b. Exact orbit-sum linear
algebra over Q in the quotient model V_k = Q^k/(1) (Gram ranks via sympy):
G x W rank 0 (k = 5..12 plus reruns), A4 x W rank 1 (k = 3..6,10,11) with only
C-type self-dots nonzero, C5 x W rank 4 with relation intersection and image
ranks above and D(R) = 0 verified, A6 x W ranks above. Scripts reproduce every
quoted integer; k = 4 H_5 quotient rerun gives invC5 = 4, rankR = 36,
dimcap = 2, rankD = 2, dimH5 = 0. Vectors verified S_k-invariant under the
correct quotient action (all transpositions including the distinguished-index
swap).

## Limitations
Lambda^2(G)/Arnold summand of H^6 and all higher cohomology uncomputed; no
total H_i claim for i >= 6 and no uniform k >= 2i+3 range for all i.
Geometric puncture-stabilisation is analyzed only via S_k-inclusion scaling
plus dimension counts; identification of the geometric map with computed
scalars is not proved. Character tables computed explicitly to n = 12 plus
closed stable formulas; orbit-sum Grams cover the k values listed per script.

## Reproducibility
Scripts in output/artifacts/: stab_q4.py, char_dims.py, char_dims2.py,
char_all.py, h5_char.py, identify_maps.py, check_smallk.py,
boundary_k10_k11.py, h5_explore.py, h5_quotient.py, h5_quot_run7.py,
h5_smallk.py, stab_maps.py, h6_check.py, h6_dims_full.py, support_bound.py,
stab_scalar.py, verify_d2.py, g2_arnold.py, dim_table.py, final_checks.py.
Cheap checks: final_checks.py (character table, W_2 = 0);
boundary_k10_k11.py (H^4 at k = 10,11 in seconds); h5_quotient.py at k = 4
(seconds; k = 7 takes minutes). explore_h4.py uses a superseded wrong V-model
and is retained only as a negative control.

## References
- M. Palmer, Twisted homological stability for configuration spaces (2018).
- N. Idrissi, The Lambrechts-Stanley model of configuration spaces (2019).
- M. Kriz, On the rational homotopy type of configuration spaces.
- M. Maguire et al., Computing cohomology of configuration spaces (2016).
- S. Kallel, Configuration spaces of points: a user's guide (2024).
