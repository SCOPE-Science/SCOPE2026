# Explicit Ramanujan (hence near-Ramanujan) 3-lift of K7 on 21 vertices

## Context

Let G0 = K7, 6-regular on 7 vertices, spectrum 6^1, (-1)^6. Consider the uniform
random 3-lift ensemble defined by independent uniform S3 voltages on the 21
edges of K7. Marcus-Spielman-Srivastava covers 2-lifts; Hall-Puder-Sawin gives
a one-sided r-covering upper bound; Bordenave(-Collins) are large-n limits.
None gives a two-sided fixed-cell (K7, degree 3, 21-vertex) certificate. The
admitted target was: some 3-lift G of K7 has all new eigenvalues satisfying
|lambda| <= 2*sqrt(5)+0.5 (~4.9721), with an edge-expansion witness.

## Definitions

- V(K7) = {0,...,6}, edges E = {a<b}, |E| = 21.
- S3 in one-line notation on {0,1,2}, lex index 0..5:
  0=(0,1,2), 1=(0,2,1), 2=(1,0,2), 3=(1,2,0), 4=(2,0,1), 5=(2,1,0).
- A voltage assignment sigma: E -> S3 (orientation a->b) defines the 3-lift
  with vertex set V x {0,1,2} and edges (a,i) ~ (b, sigma_e(i)) plus the
  symmetric return. Each inter-fiber block is a permutation matrix; the lift
  is 6-regular on 21 vertices with 63 edges.
- Fiber-constant vectors span a 7-dimensional A_G-invariant subspace on which
  A_G acts as A_{K7}; hence old eigenvalues 6^1, (-1)^6 and 14 new ones.
- Kesten-McKay(6) tree moments (closed root-walks on the 6-regular tree):
  (0, 6, 0, 66, 0, 876) for k = 1..6.
- Witness voltages (lex S3 indices, edge order (0,1),(0,2),...,(5,6)):

  [5,3,4,4,4,0,2,1,0,0,2,5,4,2,4,4,0,1,3,0,2]

  Full 21x21 adjacency matrix: output/artifacts/witness_adj.csv.

## Result

**Theorem.** With G0 = K7 and the uniform S3 3-lift ensemble above:

1. Exact expected traces: E Tr(A_G^k) = (0, 126, 210, 2226, 7770, 59136) for
   k = 1..6. The new-eigenvalue part E Tr_new = E Tr - Tr_{K7} equals
   (0, 84, 0, 924, 0, 12474), i.e. per-new-eigenvalue (0, 6, 0, 66, 0, 891),
   matching Kesten-McKay(6) tree moments (0, 6, 0, 66, 0, 876) exactly through
   order 5 with excess only 15 at order 6. Expected-characteristic-polynomial
   leading coefficients from these power sums: c1..c6 =
   (0, -63, -70, 1428, 2856, -14021).
2. Existence at 4.82 from expectation alone: E Tr_new(A_G^6) = 12474 <= 4.82^6
   (integer cert 482^6 = 12539558025308224 >= 12474 x 10^12), so some 3-lift
   has max|lambda_new| <= 4.82 < 2*sqrt(5)+0.5.
3. Explicit witness, Ramanujan: the 3-lift G* defined above has exact
   Tr(A^6) = 54636, Tr_new = 7974 < 8000 = (2*sqrt(5))^6, hence every new
   eigenvalue satisfies |lambda_new| < 2*sqrt(5) (~4.4721), a fortiori within
   the target 2*sqrt(5)+0.5.
4. Expansion: lambda_2(G*) <= max|lambda_new| < 4.5 (integer cert
   45^6 = 8303765625 >= 7974 x 10^6), so by Cheeger
   h(G*) >= (6 - 4.5)/2 >= 0.75 >= (6 - 4.9721)/2 (~0.514).

## Proof / evidence

- Expected traces: for a base closed walk gamma of length k, E of its
  lift-count equals E[Fix(W)] where W is the product of independent uniform
  edge-voltages along gamma. Grouping closed walks (42, 210, 1302, 7770,
  46662 for k = 2..6) by edge-block pattern (2, 6, 24, 120, 440 patterns) and
  evaluating each E[Fix] exactly over 6^m assignments gives the table.
  Replay: `python3 output/artifacts/verify_moments.py` -> VERIFY_OK
  (stdlib-only, ~1 min). Base traces use Tr(A_{K7}^k) = 6^k + 6(-1)^k.
- Existence: for even power 6, max|lambda_new|^6 <= Tr_new(A^6) (sum of 14
  nonneg sixth powers); taking expectations gives some lift with
  max|lambda_new|^6 <= 12474 <= 4.82^6 <= 4.972^6 (integer certs above).
  Lower bound sqrt(5) > 2.236 (2236^2 = 4999696 < 5 x 10^6) pins
  2*sqrt(5)+0.5 >= 4.972.
- Witness: verify.py checks symmetry, 6-regularity, permutation-block
  covering, then exact bigint traces Tr(A^k) = (0,126,204,2074,7750,54636);
  with old_6 = 6^6+6 = 46662, Tr_new = 7974 < 8000 gives the Ramanujan bound.
  Replay: `python3 output/artifacts/verify.py` -> VERIFY_OK (seconds,
  stdlib-only). Newton identities rechecked for c1..c6.
- No general 3-lift interlacing theorem is assumed; the expectation bound is
  a pigeonhole corollary and the member is exhibited explicitly.

## Limitations

- Proof covers items 1-4 above with exact-integer certificates.
- Illustration only (not part of proof): floating spectra (witness
  max|new| ~ 3.61), a 2000-lift random survey, exact h = 16/9 (a retired
  exhaustive 2^21-subset script); only the Cheeger lower bound h >= 0.75 is
  claimed.
- Not claimed: full degree-21 expected characteristic polynomial (only
  leading coefficients c1..c6), a general 3-lift interlacing theorem, or
  optimality of G* / of the order-6 excess 15.

## Reproducibility

- `python3 output/artifacts/verify.py` -> construction + bigint traces +
  Ramanujan/target integer certs + Newton c1..c6 -> VERIFY_OK.
- `python3 output/artifacts/verify_moments.py` -> exact expected-trace
  enumeration -> VERIFY_OK.
- `output/artifacts/witness_adj.csv` (21x21 0/1, symmetric, row sums 6),
  `output/artifacts/moment_table.csv`.

## References

- Marcus, Spielman, Srivastava, Interlacing Families I: Bipartite Ramanujan
  Graphs of All Degrees. https://arxiv.org/abs/1304.4132
- Hall, Puder, Sawin, Ramanujan Coverings of Graphs.
  https://arxiv.org/abs/1506.02335
- Bordenave, Collins, Eigenvalues of random lifts and polynomials of random
  permutation matrices. https://arxiv.org/abs/1801.00876
