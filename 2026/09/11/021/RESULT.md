# Joint inversion / minus-one census of diagonally symmetric ASMs of order 7

## Context
Diagonally symmetric alternating sign matrices (DSASMs) are the last major ASM
symmetry class without a product formula. Behrend-Fischer-Koutschan (BFK,
arXiv:2309.08446) gave the first exact enumeration: a Pfaffian for |DSASM(n)|
plus Pfaffians for refined generating functions in statistics R (nonzero
strictly-upper entries), S (nonzero diagonal entries), T (first-row 1 column),
and a Section 10 generalized Xbar(p,r,s+,s-,t) with strictly-upper inversion
statistic P and split diagonal statistics. BFK publishes totals
(|DSASM(7)| = 2630) but no evaluated order-7 joint distribution in
generalized inversion number I and minus-one count M = N_-1.

## Definitions
- DSASM(n): n x n alternating sign matrices A with A^T = A.
- I(A) = sum_{i<i', j'<=j} A_{ij} A_{i'j'} (Robbins-Rumsey generalized
  inversion number).
- M(A) = number of -1 entries. R(A) = nonzero strictly-upper count,
  S(A) = nonzero diagonal count, P(A) = strictly-upper inversion sum.
- For DSASMs: M = R + (S-n)/2, I = 2P + (n-S)/2 (BFK Secs. 2/10); S = n mod 2.
- J_7(i,r) = #{A in DSASM(7): I(A)=i, M(A)=r}.
- P_7 = BFK numDSASM Pfaffian value at n = 7.

## Result
Exhaustive monotone-triangle enumeration (218348 ASMs of order 7 filtered to
2630 DSASMs) gives J_7 with 116 nonzero cells summing to 2630. Independent
exact evaluation of the BFK generalized Xprs Pfaffian at n = 7 (6x6 Pfaffian
of exact trivariate polynomials, 132 terms, all coefficients >= 0,
S-support {1,3,5,7}) projects via I = 2P+(7-S)/2, M = R+(S-7)/2 to the
identical J_7. Both totals equal P_7 = 2630, itself evaluated by two exact
routes (matching-sum Pfaffian vs Bareiss-determinant square root); BFK totals
for n <= 10 are reproduced exactly: 1,2,5,16,67,368,2630,24376,293770,4610624.

Joint table J_7 (rows I, columns M = 0..9):
- 0: [1,0,0,0,0,0,0,0,0,0]
- 1: [6,5,4,3,2,1,0,0,0,0]
- 2: [10,12,9,4,0,0,0,0,0,0]
- 3: [9,11,13,14,14,8,5,2,1,0]
- 4: [16,27,36,28,20,9,4,0,0,0]
- 5: [13,17,27,30,30,15,10,0,0,0]
- 6: [19,40,76,81,80,50,36,14,4,1]
- 7: [17,23,45,40,40,8,5,2,0,0]
- 8: [19,46,110,115,123,59,21,6,0,0]
- 9: [19,24,54,30,33,14,0,0,0,0]
- 10: [17,44,102,83,74,38,18,4,1,0]
- 11: [19,22,56,26,16,5,2,0,0,0]
- 12: [13,26,51,41,30,9,3,0,0,0]
- 13: [17,19,40,18,8,0,0,0,0,0]
- 14: [7,12,19,12,6,0,0,0,0,0]
- 15: [13,13,22,12,6,1,0,0,0,0]
- 16: [3,3,3,0,0,0,0,0,0,0]
- 17: [8,5,5,1,0,0,0,0,0,0]
- 18: [1,0,0,0,0,0,0,0,0,0]
- 19: [4,1,0,0,0,0,0,0,0,0]
- 21: [1,0,0,0,0,0,0,0,0,0] (I = 20 absent: 0.)

Marginals: M: {0:232,1:350,2:672,3:538,4:482,5:217,6:104,7:28,8:6,9:1};
I: {0:1,1:21,2:35,3:77,4:140,5:142,6:401,7:180,8:499,9:174,10:381,11:146,
12:173,13:102,14:56,15:67,16:9,17:19,18:1,19:5,21:1}.
Extremal witnesses (in witnesses.json): min-I (0,0) identity; max-I (21,0)
anti-identity; max-M (6,9) dense symmetric ASM with 9 minus-ones; plus
(8,6),(18,0),(19,0).

Accompanied by a proved and machine-checked antisymmetrizer-to-Pfaffian
reduction lemma (classical Stembridge-type 2-family step): for ordered sinks
with path weights w, K(i,j) = sum_{a<b}(w(xi,a)w(xj,b)-w(xi,b)w(xj,a));
Pf(K) equals the signed non-intersecting family sum, intersecting families
cancelling via the fixed-point-free tail-swap involution at the first common
vertex. Claimed as DSASM instantiation plus machine check, not invention of
Stembridge's theorem.

## Proof / evidence
- Route A (enumeration): monotone triangles bottom-up; generator validated
  (ASM totals 1,2,7,42,429,7436; DSASM totals to n = 6); every n = 7 object
  passes row/column sum checks; per-object (I,M) via direct matrix sums AND
  via structural (P,R,S) relations, asserted equal on all 2630.
- Route B (Pfaffian): exact trivariate series to degree 6 via recurrence
  D*S = 1, D = 1-ru-rv+(r^2-p)uv; G = (v-u)/(1-uv) convolution; i = 1
  prefactor s(1+u), sign verified against the X_3 closed form; 6x6 Pfaffian
  over 15 matchings in exact integer arithmetic; projects cell-for-cell to J_7.
- Cross-checks: totals n <= 10 dual-route; S-parity; nonnegativity of Xprs
  coefficients; extremal witnesses re-verified axiomatically (ASM + symmetric
  + stats).
- Auditor independently re-ran: live 218348 -> 2630 enumeration matching the
  committed table; direct-vs-structural agreement on all 2630; dual-route
  totals to n = 10; Xprs/PRS projection equality as (P,R,S) multisets;
  all 6 witnesses.

## Limitations
- The Xprs formula itself (proofs omitted in BFK Sec. 10) is evaluated
  exactly as stated; the Pfaffian route is an independent evaluation plus
  agreement certificate, not a new proof of BFK's six-vertex/Yang-Baxter proof.
- The reduction lemma is the classical Stembridge argument instantiated;
  originality is the DSASM instantiation plus machine check, stated as such.
- Literature search: fused SerpBase/Crossref retrieval (OpenAlex 0 hits,
  status ok) plus direct BFK/OEIS/FindStat fetches found no J_7/C_7 table.

## Reproducibility
Stdlib-only Python artifacts: dsasm_enum2.py (generator + stats),
pfaffian.py (Bareiss + matching Pfaffian + BFK totals), xprs7_full.py
(Xprs evaluation), lemma_check.py, J7_enum.json, PRS7_enum.json,
Xprs7_full.json, witnesses.json, verify.py.

## References
- R. E. Behrend, I. Fischer, C. Koutschan, Diagonally symmetric alternating
  sign matrices, arXiv:2309.08446.
- OEIS A005163 (DSASM totals); OEIS A005156 (VSASM/OSASM totals).
- FindStat: Alternating sign matrices collection.
- R. E. Behrend, Multiply-refined enumeration of ASMs, Adv. Math. 2013.
- R. E. Behrend, I. Fischer, M. Konvalinka, DASASMs of odd order.
- N. Kumari, Off-diagonally symmetric ASMs, arXiv:2503.18685.
