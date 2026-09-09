# Minimal Redei-type blocking sets in PG(2,13) at sizes 21, 23, 24 with direction spectra and a size-22 narrowing lemma

## Context

Small minimal blocking sets in prime-order projective planes are classical objects
(Redei; Blokhuis bound 3(p+1)/2; Ball and the direction/lacunary-polynomial program).
They determine direction sets of functions over finite fields and, via the
cutting-blocking-set correspondence, supply geometric extremals for minimal linear
codes. For p = 13 the Blokhuis bound is 3(13+1)/2 = 21, and the head window
K = {21, 22, 23, 24} is the natural boundary interval above it.

## Definitions

Work in PG(2,13): 183 points, 183 lines, 14 points per line. Coordinates are
homogeneous triples over F_13 up to nonzero scalar; lines are triples (a,b,c)
with incidence ax+by+cz = 0. Let l_inf be z = 0.

- A *blocking set* (w.r.t. lines) meets every line; it is *nontrivial* if it
  contains no line, and *minimal* if every point is essential, i.e. lies on a
  *tangent* line meeting the set in exactly that point.
- A set is *of Redei type* (graph sense used here) if for some line l,
  B = U union D with U = {(x, f(x), 1) : x in F_13} the graph of
  f : F_13 -> F_13 and D = {(1, m, 0) : m in D(f)} the determined slopes
  m = (f(x)-f(y))/(x-y), x != y. Then |B| = 13 + N with N = |D(f)|,
  and |B cap l_inf| = N = |B| - 13 with l_inf explicit.
- The *direction (slope) spectrum* is the set D(f) of determined slopes.
- The *line spectrum* is the table (i : number of lines meeting B in exactly
  i points).
- The *Redei divisibility* check is: for every slope y not in D(f),
  {f(x) - x*y : x in F_13} = F_13 (all 13 values, i.e. the Redei factor
  splits completely).

## Result

### Theorem 1 (verified witnesses, sizes 21, 23, 24)

The following are minimal blocking sets of Redei type in PG(2,13):

| name | f(x) | N = |D| | D(f) | |B| | line spectrum |
|------|------|-----|------|-----|----------------|
| W21 | x^7 | 8 | {1,3,4,5,8,9,10,12} | 21 | 1:126, 2:18, 3:36, 8:3 |
| W23 | x^9+x^5 | 10 | {0,1,2,3,4,5,9,10,11,12} | 23 | 1:96, 2:52, 3:32, 6:1, 10:2 |
| W24 | x^7+2x^3 | 11 | {0,1,2,3,4,6,7,9,10,11,12} | 24 | 1:91, 2:59, 3:16, 4:14, 6:2, 11:1 |

Each satisfies: exact direction set as listed; |B cap l_inf| = N = |B| - 13;
blocking (every one of the 183 lines meets B); minimality (every point essential:
21/21, 23/23, 24/24, with explicit tangents in the DRAFT section 4, each
rechecked to meet B exactly once); line spectrum as listed; and Redei
divisibility for every slope outside D(f). W21 attains the Blokhuis bound 21
and is therefore a smallest nontrivial blocking set. Concretely
[f(0),...,f(12)]: W21 = [0,1,11,3,4,8,7,6,5,9,10,2,12];
W23 = [0,2,11,10,9,10,7,6,3,4,3,2,11];
W24 = [0,3,1,5,2,11,10,3,2,11,8,12,10].

### Theorem 2 (size-22 narrowing lemma, computed exclusion)

A graph-type Redei blocking set of size 22 needs a function with exactly N = 9
directions. Exhaustively over F_13, N = 9 never occurs among: (A0) all monomials
a*x^e (N-values {1,8,12,13}); (A) all binomials a*x^e+b*x^j
(N-values {1,8,10,11,12,13}); (B) all monic trinomials x^e+a*x^j+b*x^k
(N-values {8,10,11,12,13}); (C) all degree <= 6 polynomials via normalized
representatives x^d+c_{d-1}x^{d-1}+...+c_2 x^2 (N-values {1,11,12,13}).
Hence any 9-direction function over F_13, if one exists, has at least 4 nonzero
terms and degree at least 7.

## Proof / evidence

Finite exact certificates replayed from the polynomials alone by stdlib-only
scripts in seconds:

- `artifacts/verify.py` rebuilds PG(2,13) from scratch (183 points, 183 lines,
  exact incidence), forms B = U union D from each polynomial, and checks
  distinctness, D-set equality, Redei-line count, blocking over all 183 lines,
  per-point tangent existence, line-spectrum equality, and Redei divisibility.
  Result: PASS for W21/W23/W24. Audit independently re-ran it (PASS) and
  separately verified all 68 listed tangents and all f-vectors.
- `artifacts/polylog.py` exhaustively computes direction counts N over families
  A0/A/B/C with positive controls (W21 -> 8, W23 -> 10, W24 -> 11).
  Result: PASS, N = 9 count 0 in every family (~6 s on re-run).
- Normalization lemmas: f -> a*f sends slopes s -> a*s; f -> a*f+m*x+c sends
  slopes s -> a*s+m; both are bijections of F_13, hence preserve N. So monic
  representatives cover all trinomials (up to slope permutation) and normalized
  x^d+...+c_2 x^2 representatives cover all degree <= 6 polynomials (up to
  affine slope shift). The complement of (at most 3 terms OR degree <= 6) is
  (at least 4 terms AND degree >= 7). Certificates are proof by exhaustive exact
  finite-field arithmetic, not consequences of quoted general theorems.

## Limitations

- Full {21,22,23,24} classification NOT closed: size-22 existence/nonexistence
  (graph-type Redei with >= 4 terms and degree >= 7, or non-Redei) remains open.
- No PGL(3,13)-uniqueness or exhaustiveness claim within sizes 21, 23, 24; one
  certified representative per size only.
- Redei type here means the graph form B = U union D above. A cardinality-only
  Redei definition (|B cap l| = |B| - 13 for some line, where the vertical
  direction point in B could allow a non-graph affine part) is broader; the
  Theorem 2 exclusion is proved for graph-type functions.
- Certificates are computational over F_13 (exact, replayable), not derived
  from general theorems; the Blokhuis bound is context for W21 extremality only.

## Reproducibility

- `python3 artifacts/verify.py` rebuilds PG(2,13) and replays W21/W23/W24 (seconds).
- `python3 artifacts/polylog.py` replays the N = 9 exclusion families A0-C (seconds).
- Both scripts are stdlib-only and print PASS/FAIL per check with exit status.

## References

- Blocking sets from a union of plane curves. https://arxiv.org/abs/2510.15332
  (general constructions; no PG(2,13) 21-24 spectrum).
- Minimal multiple blocking sets. https://arxiv.org/abs/1703.07843
  (t-fold bounds/structure; not the 1-fold window).
- Full Characterization of Minimal Linear Codes as Cutting Blocking Sets.
  https://arxiv.org/abs/1911.09867 (downstream correspondence).
- Double blocking sets of size 3q-1 in PG(2,q). https://arxiv.org/abs/1805.01267
  (2-fold near 3q; touches q=13 only there).
- Small 3-fold blocking sets in PG(2,p^n). https://arxiv.org/abs/2512.24689
  (different multiplicity).
- On the minimum blocking semioval in PG(2,11). https://arxiv.org/abs/2305.04907
  (different order/property).
