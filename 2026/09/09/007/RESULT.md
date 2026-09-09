# Complete prime-quadruplet gap maximum and Legendre-square occupancy census to 5e6

## Context
Prime quadruplets of pattern (0,2,6,8) are the unique minimal-diameter admissible
4-tuple. The Hardy–Littlewood k-tuple conjecture predicts their mean spacing via
the quadruplet constant H4 ≈ 4.15118; Kourbatov's statistical model predicts
maximal constellation gaps near x as ≈ a·log(x/a) with a = C4·log⁴x,
C4 = 1/H4. Legendre-type conjectures for constellations ask whether every square
interval [n²,(n+1)²] beyond some threshold contains a constellation. Exact
small-scale censuses calibrating the estimator and square-interval reliability
were previously limited to bare position lists and isolated record gaps.

## Definitions
- Quadruplet: primes (p, p+2, p+6, p+8), indexed by least prime p.
- Bound: p ≤ 5,000,000. Consecutive quadruplet gap: q_{i+1} − q_i.
- Kourbatov quantities at x: a = C4·log⁴x, T0 = a·log(x/a) (b=0),
  standardized residual R0 = (G − T0)/a.
- Legendre intervals: [n²,(n+1)²], n = 1..2235 ((n+1)² ≤ 5e6), occupant = interval
  containing ≥1 quadruplet least prime. Binning by floor-sqrt coincides with
  inclusive-interval membership (no square is prime).
- HL expected count in interval n: E_n = (2n+1)·H4/log⁴(mid_n),
  mid_n = (n²+(n+1)²)/2.

## Result
Over least primes p ≤ 5,000,000:
1. There are exactly **546** prime quadruplets, first least-prime 5, last 4997381.
   Their 545 consecutive gaps attain the exact unique maximum **Gq* = 56910** at
   **(q1,q2) = (3741161, 3798071)** (second largest 56580). All eight numbers
   q1+{0,2,6,8}, q2+{0,2,6,8} are prime. The 18 record gaps are
   (6,5,11), (90,11,101), (630,191,821), (660,821,1481), (1170,2081,3251),
   (2190,3461,5651), (3780,5651,9431), (6420,25301,31721), (8940,34841,43781),
   (9030,88811,97841), (13260,122201,135461), (16470,171161,187631),
   (24150,301991,326141), (28800,739391,768191), (29610,1410971,1440581),
   (39990,1468631,1508621), (56580,2990831,3047411), (56910,3741161,3798071).
2. With H4 = 4.151180863656573, C4 = 1/H4, at x = q2 = 3798071:
   a ≈ 12690.52, T0 ≈ 72353.63, **R0 = (Gq*−T0)/a ≈ −1.2169**
   (b=1 → R ≈ −0.217; b=2 → R ≈ +0.783).
3. Exactly **K = 478** of the 2235 Legendre intervals are occupied. The maximal
   run of consecutive empty intervals is **E = 22** at n = 187..208, i.e. no
   quadruplet least prime in **[187², 209²] = [34969, 43681]**, bracketed by
   occupants n=186: [34841] and n=209: [43781]. This empty run is the unique
   maximum (next longest 21).
4. HL comparison: expected total ΣE_n ≈ **538.45** (observed 546); expected
   occupied Σ(1−e^{−E_n}) ≈ **461.40** (observed 478).

## Proof / Evidence
Exhaustive finite computation, not an analytic theorem. Bytearray sieve to 5e6,
linear (0,2,6,8) scan, full consecutive-gap maximum with uniqueness check,
floor-sqrt binning with empty-run scan, closed-form HL sums. Witness endpoints
certified by sieve plus deterministic Miller–Rabin (bases 2,7,61) and independent
trial-division check. `artifacts/verify.py` (stdlib only) re-derives all numbers
and prints VERIFY_OK. An independent reimplementation reproduced count,
uniqueness, record chain, K, E, witness, residuals, and HL sums within stated
tolerances.

## Limitations
- Bound 5e6 is modest; maximal gap undershoots T0 (negative residual); no large
  positive estimator anomaly was found.
- Kourbatov b-parameter is heuristic; primary residual uses b=0 with b=1,2 variants.
- Empty run reported as exact finite extremum; no Gumbel-fit or significance claim.
- Isolated gap value 56910 and witness q1=3741161 are tabulated prior art
  (OEIS A113404/A229907, Kourbatov tables to 1e15); novelty is the combined gap +
  residual + complete square-occupancy census with HL comparison, not the bare list.
- H4 taken as published constant; certification rests on machine arithmetic,
  mitigated by two agreeing implementations.

## Reproducibility
Run `python3 artifacts/verify.py` (stdlib only, seconds). Expected output:
`quads=546 Gmax=56910 witness=(3741161,3798071) a=12690.52 T0=72353.63 R0=-1.2169`,
`K=478 E=22 witness=[34969,43681] HLexp_total=538.45 HLexp_occ=461.40`, `VERIFY_OK`.

## References
- A. Kourbatov, Maximal gaps between prime k-tuples: a statistical approach,
  arXiv:1301.2242 (estimator, HL constants, Legendre-type conjectures).
- A. Kourbatov, Tables of record gaps between prime constellations,
  arXiv:1309.4053 (record gaps to 1e15).
- OEIS A007530 (prime quadruples, bare enumeration); A113404 (record quadruplet
  gaps, incl. 56910); A229907 (initial primes preceding record gaps, incl.
  3741161); A192870 (conjectural maximal empty-square thresholds, n=4: 719377).
- T. Oliveira e Silva, Gaps between consecutive primes to 4e18 (single-prime gaps).
