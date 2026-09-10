# No 9-direction minimal graph in the AGL-normalized monic degree-7 family over F_13 (PG(2,13) Blokhuis-exponent obstruction)

## Context
Small and non-small minimal blocking sets in Desarguesian projective planes
PG(2,q) are studied via the Redei function-graph construction and the
direction problem. For q = 13, the Blokhuis bound is 3(p+1)/2 = 21, so size
22 = 13 + 9 (nine directions) is the first integer above the bound -- the
natural classification boundary. Small minimal Redei-type sets (fewer than
(q+3)/2 = 8 directions) were classified by Ball, Blokhuis, Brouwer, Storme,
Szonyi and Ball; the N = 9 case is non-small (projective-triangle regime)
and lies outside that classification (Csajbok 2016, Secs. 1, 3). The nearest
size-22 prior (Kadoo 2010) excludes only the "8-secant without 9-secant"
subcase. Degree 7 = (13+1)/2 is the Blokhuis-Redei exponent whose monomial
x^7 attains the bound (8 directions, size 21), making the full normalized
degree-7 family the theorem-mandated principal algebraic route to a size-22
graph-type Redei set.

## Definitions
- Fixed model: PG(2,13) = AG(2,13) plus the line at infinity l_inf:
  183 points, 183 lines (169 affine y = mx + b, 13 verticals x = c, plus
  l_inf). Points at infinity: one per slope m in F_13 plus the vertical
  point (14 total).
- For f : F_13 -> F_13, B(f) = {(x, f(x))} + D(f) with
  D(f) = {(f(x) - f(y)) / (x - y) : x != y} on l_inf.
  |B(f)| = 13 + |D(f)|, so a 22-point Redei set <=> |D(f)| = 9.
- Normalized family: monic degree-7 polynomials with f(0) = 0 and zero x^6
  coefficient: C = [0, a1, a2, a3, a4, a5, 0, 1], 13^5 = 371,293
  representatives (a1 free).

## Result
No AGL-normalized monic degree-7 polynomial f over F_13 with f(0) = 0 and
zero x^6 coefficient has a graph yielding exactly 9 directions with minimal
blocking property in PG(2,13): every such graph either determines a
direction count different from 9 or its 22-point Redei set is non-blocking
or reducible.

Exact census over all 371,293 representatives:

total 371293 hist {8: 13, 11: 117, 12: 1196, 13: 369967} n9 0

Zero representatives determine exactly 9 directions, so there is no
22-point candidate to test and the minimal-blocking half is vacuous.

## Proof / evidence
1. AGL-normalization reduction (replayed, NORMALIZATION_INVARIANCE_OK,
   20 random-polynomial trials): monic scaling f -> a*f scales D by the unit
   a (N invariant); vertical shift f -> f + k leaves D invariant; x-shift
   x -> x - a6/7 (7 invertible mod 13) leaves pair slopes, hence D,
   invariant; linear shift f -> f + m*x translates D (N invariant). Every
   degree-7 polynomial therefore has a normalized representative with the
   same N, so enumerating C = [0, a1..a5, 0, 1] is complete.
2. Exhaustive enumeration by independent pure-Python set-of-slopes
   implementation (replay_fallback_slice.py via direc.py):
   FALLBACK_SLICE_REPLAY_OK with the histogram above, n9 = 0.
3. Auditor independent vectorized re-census (batched Vandermonde evaluation
   + sort-based distinct-slope counts, no shared code with direc.py):
   AUDIT_RECENSUS_OK, byte-identical histogram, n9 = 0.
4. Blocking/minimality protocol machine-verified (verify_target.py,
   VERIFY_OK): blocking is automatic for every Redei graph (slope in D:
   blocked at infinity; slope outside D: f(x) - m*x bijective, exactly one
   affine hit; verticals meet the graph once; l_inf meets D);
   affine-point minimality is automatic (vertical line through a graph point
   meets B(f) exactly once); minimality <=> every m in D admits a missed
   value of f(x) - m*x (tangent at the infinity point m); brute-force replay
   over all 183 lines on x^7. Cross-checks: analytic degree<=2 rows; full
   pure-Python recheck of degrees 3-7 with matching histograms, none N = 9;
   x^7 anchor N = 8 with directions {1,3,4,5,8,9,10,12}.
This is proof (analytic reduction + exhaustive certificate), not
experimental sampling; random samples are supporting only.

## Limitations
Degree-7 AGL-normalized family only (Blokhuis exponent (p+1)/2). General
PG(2,13) size-22 existence across all degrees stays open in this
submission. The headline does not claim full size-22 nonexistence.

## Reproducibility
- output/artifacts/direc.py -- direction primitives (set-of-slopes).
- output/artifacts/replay_fallback_slice.py -- exact-criterion enumeration
  (13^5 reps); run: python3 output/artifacts/replay_fallback_slice.py
  -> FALLBACK_SLICE_REPLAY_OK.
- output/artifacts/normalization_invariance.py -- reduction proof replay;
  run: python3 output/artifacts/normalization_invariance.py
  -> NORMALIZATION_INVARIANCE_OK.
- output/artifacts/verify_target.py -- blocking/minimality + cross-check
  logic; run: python3 output/artifacts/verify_target.py -> VERIFY_OK.
- output/artifacts/audit_independent_recensus_deg7.py -- auditor
  independent vectorized re-census (no shared code); run:
  python3 output/artifacts/audit_independent_recensus_deg7.py
  -> AUDIT_RECENSUS_OK with hist {8:13, 11:117, 12:1196, 13:369967}, n9 0.
Standard library plus numpy only.

## References
- S. Ball, The number of directions determined by a function over a finite
  field, JCTA 2003. DOI 10.1016/j.jcta.2003.09.006.
- B. Csajbok, On bisecants of Redei type blocking sets and applications,
  arXiv:1504.06748v2. https://arxiv.org/html/1504.06748v2
- F. H. Kadoo, The Minimal Blocking Set Of Size 22 In PG(2,13) (2010).
  https://www.researchgate.net/publication/339216840_The_Minimal_Blocking_Set_Of_Size_22_In_PG_2_13
- J. Danielsson, Minimal blocking sets of size 2p-2 and 2p-3 in PG(2,p)
  (2008). DOI 10.1007/s00022-007-1888-9.
- A. Botteldoorn, K. Coolsaet, V. Fack, Classification of minimal blocking
  sets in PG(2,9) (2024). DOI 10.1007/s00022-023-00702-5.
- T. Szonyi, A. Gacs, Zs. Weiner, On the spectrum of minimal blocking sets
  in PG(2,q) (2003). DOI 10.1007/s00022-003-1702-2.
