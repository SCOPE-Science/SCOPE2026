# Exact extremal family at diversity 4 for 2-intersecting permutations

## Context
For fixed t, the largest t-intersecting families of S_n are t-cosets of size
(n-t)!. First-level stability (Ellis 2011) says a non-contained t-intersecting
family has size at most (1-1/e+o(1))(n-t)!, extremized by a family D with
diversity t (2 outside permutations for t=2). The admitted target asked for the
sharp maximum at 2-diversity gamma_2 >= 3. The large-n upper bound remains open;
this record is the proved extremal-construction half: an explicit infinite
family at diversity exactly 4 with a closed-form size, the concrete sharpness
candidate.

## Definitions
Work in S_n. F is 2-intersecting if any two members agree in at least 2
positions. A 2-coset fixes two values: {sigma : sigma(i1)=j1, sigma(i2)=j2}.
Delta_2(F) is the maximum of |F cap C| over 2-cosets C; gamma_2(F)=|F|-Delta_2.
An (n-3)-coset fixes n-3 values. For p not in C0, D(p)={s in C0 : agr(s,p)<2}
is its deletion set. Double-translate isomorphism is sigma -> alpha sigma beta.

## Result
For n >= 7, let C0 be a 2-coset of S_n and M an (n-3)-coset sharing exactly one
defining equation with C0. Put P_full = M \ C0 (4 permutations, pairwise
agreeing in n-3 positions) and F = (C0 union M) minus union_{p in P_full} D(p),
equivalently F = R union P_full with R = {s in C0 : agr(s,p) >= 2 for all
p in P_full}. Then F is 2-intersecting with diversity gamma_2(F) = 4 and exact
size |F| = (n-2)! + 4 - U(n), where U(n) = 4S1 - (4Pnt + 2Ptr) + 4T - Q is an
exact closed rook-theoretic deletion count with terms
avoid(n,rF) = sum_{i,j} (-1)^{i+j} C(n-4,i) rF[j] (m-i-j)! (m = n-2) and rook
vectors (1,1), (1,2,0), (1,2,1), (1,3,1), (1,4,2). Verified values:
U = 14, 64, 362, 2428, 18806 and |F| = 14, 60, 362, 2616, 21518 for
n = 6, ..., 10, with U(n)/(n-2)! -> 1/e so |F| = (1-1/e+o(1))(n-2)!.

## Proof / evidence
C0-internal pairs share the two coset equations; P_full-internal pairs share
the n-3 coset equations (>= 3 for n >= 6); cross pairs satisfy agr >= 2 by the
definition of R; the two kept M cap C0 members were verified to agree >= 2
with every p in P_full. Exhaustive check of all pairs for n <= 9 via
output/artifacts/verify_construction.py confirms 2-intersection. The forbidden
board for each deletion set splits as a disjoint union of a shared (n-4)
diagonal and a 2x2 free board, so rook numbers factor and inclusion-exclusion
over the 4-pattern board is exact; brute union sizes match the formula at
n = 6, 7, 8 (14, 64, 362), and pair/triple/quad intersections match the stated
coefficients (e.g. n=8: singles 309, pairs 256/265, triples 212, quad 168).
Delta_2 is attained at C0: any other 2-coset shares at most one equation with
C0, hence holds at most (n-3)! + 4 members of F, and
|R| - ((n-3)! + 4) = 0, 28, 234, 1888, ... for n = 6, 7, 8, 9, ..., positive for
n >= 7 (n = 6 by direct scan, Delta_2 = 10). Thus gamma_2 = 4. The 1/e limit
follows from the rook expansion. Small-n optimality: n = 6 exhaustive
concentrated-class search attains 14 = formula; n = 8 canonical-pair scan and
n = 9 structured/random probes find nothing beating this construction.

## Limitations
The all-large-n upper bound (no gamma_2 >= 3 family exceeds |F|) and the
equality classification remain conjectural, not claimed. DRAFT's phrase
"s(i) = i for 2 <= i <= n-4" is an off-by-one typo for 2 <= i <= n-3 (|M| = 6
requires n-4 fixed tail equations plus s(0) = 0); the abstract (n-3)-coset
statement and the verified script use the correct indexing.

## Reproducibility
Run `python3 output/artifacts/verify_construction.py` (n <= 8 brute-force in
seconds; n = 9 about a minute; n = 10 formula only). It checks brute-vs-formula
U(n), |F|, and the defining construction. Independent Delta_2 scans over all
2-cosets at n = 6, 7, 8 confirm Delta_2 = |R|.

## References
- D. Ellis, Stability for t-intersecting families of permutations, JCTA 2011
  (arXiv:0807.3115). First-level stability; extremal D has diversity 2.
- J. Wang and J. Xiao, A note on the maximum diversity of intersecting families
  in the symmetric group, EJC 2025/26 (arXiv:2501.06731). t = 1 diversity.
- K. Meagher and A. S. Razafimahatratra, 2-intersecting permutations,
  arXiv:2005.00139. t = 2 EKR program.
- G. Chase, N. Dafni, Y. Filmus, N. Lindzey, Uniqueness for 2-intersecting
  families of permutations and perfect matchings, arXiv:2210.00245.
  Maximum-family uniqueness.
