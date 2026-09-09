# Maximal spherical growth rate among RACGs on connected graphs with n<=7

## Context and motivation

Spherical growth series of Coxeter groups connect nerve combinatorics,
rationality/reciprocity theorems, hyperbolicity criteria, and conjectures on
growth gaps and the Perron/Salem/Pisot arithmetic of growth rates
(Terragni uniform gap; Kolpakov-Talambutsa Perron theorem; Okun-Scott
rationality). Small-graph tables are the standard laboratory in which such
conjectures are tested. No prior work tabulates exact rational series over all
unlabelled connected defining graphs through 7 vertices or identifies the
maximal-growth extremal in that slice.

## Definitions

- Let `G` run over representatives of all unlabelled connected simple graphs on
  `2 <= n <= 7` vertices: counts `1, 2, 6, 21, 112, 853`, total `995`
  (OEIS A001349).
- For each `G`, let `W(G)` be the right-angled Coxeter group with standard
  generators `S` (`s^2 = 1`; `st = ts` iff `s, t` adjacent in `G`).
- Spherical growth series: `W_G(t) = sum_{w in W} t^{|w|_S} = sum_{k>=0} a_k t^k`.
- Exponential growth rate: `omega(G) = limsup a_k^{1/k} = 1/R`, where `R` is the
  radius of convergence (reciprocal of the smallest-modulus pole).
- Nerve `N`: clique complex of `G`; `c_k` = number of `k`-cliques of `G`
  (`c_0 = 1`), `w` = clique number; `f_N(x) = sum c_k x^k`.

## Result (headline)

1. **Exact series.** For every one of the 995 graphs,
   `W_G(t) = P(t)/Q(t)` with `P(t) = (1+t)^w` and
   `Q(t) = sum_{k=0}^{w} c_k (-t)^k (1+t)^{w-k}` (exact integers, `Q(0) = 1`).
   The table in `artifacts/table.json` lists `(c, w, Q)`, a Sturm-isolated
   smallest positive pole interval, and the rate for all 995 types.
2. **Maximal-growth extremal.** The maximal rate over the whole 995-type slice
   is **exactly 5**, attained on **exactly the eleven 7-vertex trees** and no
   other graph. Each extremal tree has `Q(t) = 1 - 5t` exactly, hence
   `W(t) = (1+t)^2/(1-5t) = 1 + 7t + 36t^2 + 180t^3 + 900t^4 + ...`
   (`a_0 = 1`, `a_1 = 7`, `a_k = 36 * 5^{k-2}` for `k >= 2`).
3. **Gap.** The runner-up rate is `2 + 2*sqrt(2) = 2(1+sqrt(2)) ~= 4.8284`
   (denominator `Q = [1,-4,-4,0]`, smallest root `(sqrt(2)-1)/2`),
   so the gap is `5 - (2+2*sqrt(2)) = 3 - 2*sqrt(2) ~= 0.1715728753`.
4. **Cross-check.** Taylor coefficients of `P/Q` agree with Cayley sphere sizes
   from the faithful integral Tits representation (BFS to radius 5 for all 995
   graphs; extremal trees additionally to radius 8).

## Proof / evidence

- **Formula.** Steinberg formula for RACGs in Chiswell-Okun-Scott form:
  `W_G(t) = 1/f_N(-t/(1+t))` (Okun-Scott arXiv:1812.07755; Chiswell;
  multivariate extension Pilakkat-Rajendran 2026). Since `G` is the 1-skeleton
  of `N`, the `c_k` are exactly the clique counts; clearing denominators with
  `w = dim N + 1` gives the stated `P/Q`. Recomputed `Q` from `(c, w)` for all
  995 rows: 0 mismatches.
- **Enumeration.** Exhaustive labelled scan with canonical-hash dedup for
  `n <= 6` (`1,2,6,21,112`); Prufer trees plus orderly single-edge augmentation
  for `n = 7` (`853`); total `995`, matching OEIS A001349. Audit confirmed:
  `n <= 6` canonical brute-force distinctness; `n = 7` within-invariant-bucket
  brute-force isomorphism check over 861 pairs finds 0 duplicates; the 11
  trees are pairwise non-isomorphic; all 995 graphs connected.
- **Tree lemma (analytic).** A tree on `n >= 3` vertices has
  `c_0 = 1, c_1 = n, c_2 = n-1, w = 2`, so
  `Q(t) = (1+t)^2 - n t(1+t) + (n-1)t^2 = 1 - (n-2)t`.
  Hence every 7-vertex tree has `Q(t) = 1 - 5t` exactly and rate exactly 5.
- **Maximality (Sturm-certified).** Exact-Fraction Sturm root counts in
  `(0, 1/5]` are 0 for all 971 non-tree graphs (independently recounted;
  `Q(1/5) > 0` everywhere non-tree, `Q(1/5) = 0` nowhere). Since series
  coefficients are nonnegative growth counts, Pringsheim's theorem makes the
  radius of convergence the smallest positive pole; absence of `Q`-roots in
  `(0, 1/5]` implies no pole of modulus `<= 1/5`, so every non-tree rate is
  `< 5`. Finite groups are exactly the 6 complete graphs (`Q = 1`, no pole).
  The only graphs with rate `>= 5 - 1e-9` are the eleven 7-trees.
- **Replay.** `python3 artifacts/verify.py` prints `VERIFY_OK` (recomputes
  cliques, `Q`, Sturm max-certificate, Tits BFS radius 5 for all 995; re-ran
  clean in audit).

## Limitations

- Spherical (word) growth only; geodesic-growth rates are not compared.
- No claim about Perron/Salem/Pisot arithmetic type of individual rates.
- Enumeration completeness rests on the Prufer+augmentation orderly-generation
  argument plus the OEIS count match and canonical-hash dedup, not a formally
  verified prover (mitigated by the exact count match and pairwise
  isomorphism checks above).
- The reused theorems (Chiswell/Okun-Scott formula, Brink-Howlett rationality,
  Terragni gap/monotonicity) are prior art; novelty is the exhaustive
  evaluated 995-type table plus the proved rate-5 extremal.

## Reproducibility

- `artifacts/graphs.json`: canonical edge lists for all 995 graphs + counts.
- `artifacts/table.json`: per-graph `(c, w, Q, root interval, rate, tree flag)`.
- `artifacts/maxcert.json`: max-certificate summary (971/971 Sturm zeros,
  argmax 11, runner-up, gap).
- `artifacts/verify.py`: independent stdlib-only replay; prints `VERIFY_OK`.
- Run: `python3 artifacts/verify.py` (stdlib only; minutes).

## References

- T. Terragni, On the growth of a Coxeter group, arXiv:1312.3437.
- B. Okun, R. Scott, Growth series of CAT(0) cubical complexes,
  arXiv:1812.07755.
- A. Kolpakov, A. Talambutsa, Spherical and geodesic growth rates of
  right-angled Coxeter and Artin groups are Perron numbers,
  arXiv:1809.09591.
- Pilakkat-Rajendran, Multivariate growth series of graph products of groups,
  arXiv:2607.23668 (2026).
- OEIS A001349: number of connected unlabelled graphs. https://oeis.org/A001349
