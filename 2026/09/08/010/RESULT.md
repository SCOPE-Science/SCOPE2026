# Sharp domination ceiling floor((n+2)/4) for striped maximal outerplanar graphs

## Context

Maximal outerplanar graphs (triangulations of a convex n-gon) satisfy the
classical Chvatal / Matheson-Tarjan ceiling gamma <= floor(n/3). The
(n,n2)-parametrized refinement gamma <= (n+n2)/4 (n2 = number of degree-2
vertices) is due to Campos-Wakabayashi (2013) and independently Tokunaga
(2013). For the striped subclass (n2 = 2) this gives gamma <= (n+2)/4, but
prior literature states neither per-n sharpness inside the striped class nor
exact maxima, distributions, or extremal geometry. The only prior "striped"
study found (Zhuang 2021) treats double domination, not standard domination.

## Definitions

- Maximal outerplanar graph: convex n-gon plus n-3 non-crossing diagonals
  (n cycle edges, n-2 triangles).
- Striped (snake / linear 2-tree / dual-path): dual tree is a path,
  equivalently exactly two degree-2 vertices (ears).
- gamma(G): standard domination number.
- M(n) = max gamma(G) over striped maximal outerplanar G on n vertices.
- Fixed-ear peel words: with ear T1=(0,1,2) fixed, striped triangulations
  biject with prepend/append words of length n-4; exactly 2^(n-4) labelled
  instances (64 at n=10, 256 at n=12, 16384 at n=18, 65536 at n=20).
  Unlabelled representatives obtained by quotienting under the dihedral
  action via canonical adjacency signatures.

## Result

Let G be striped maximal outerplanar on n vertices, 6 <= n <= 30. Then
gamma(G) <= floor((n+2)/4). The bound is best possible for every such n.
In particular, on the assigned window 10 <= n <= 30:

  M(n) = floor((n+2)/4) exactly.

It beats floor(n/3) by floor(n/3)-floor((n+2)/4) in {0,1,2} (2 for n >= 21
mostly; 10 vs 8 at n=30, ~n/12 asymptotically) and beats the per-graph
Caro-Wei bound on every extremal (e.g. ~6.62 < 8 at n=30).

Exact census (unlabelled reps; gamma distribution; M(n)):

  n=10: 20 reps {1:1,2:16,3:3} M=3
  n=11: 36 reps {1:1,2:21,3:14} M=3
  n=12: 72 reps {1:1,2:28,3:43} M=3
  n=13: 136 reps {1:1,2:33,3:102} M=3
  n=14: 272 reps {1:1,2:40,3:221,4:10} M=4
  n=15: 528 reps {1:1,2:45,3:408,4:74} M=4
  n=16: 1056 reps {1:1,2:52,3:671,4:332} M=4
  n=17: 2080 reps {1:1,2:57,3:1002,4:1020} M=4
  n=18: 4160 reps {1:1,2:64,3:1409,4:2650,5:36} M=5
  n=19: 8256 reps {1:1,2:69,3:1884,4:5910,5:392} M=5
  n=20: 16512 reps {1:1,2:76,3:2435,4:11728,5:2272} M=5

Labelled extremal counts n=10..18:
40, 264, 912, 2496, 224, 2160, 10240, 34272, 1152.
Unlabelled extremal counts n=10..18: 3, 14, 43, 102, 10, 74, 332, 1020, 36.

Sharpness family: the alternating zigzag LRLR... does NOT attain the bound
(gamma 3,4,5,6 at N=14,18,22,26 vs targets 4,5,6,7). The attaining family is
the 3+1-periodic comb L R LLL (RLLL)* RL... (truncated to word length N-3),
certified instance-by-instance for every 10 <= N <= 30. Its degree sequences
are comb-like (hubs of degree 6-7 separated by degree-3 runs), never the flat
zigzag profile.

## Proof / evidence

Upper bound: cited as the n2=2 case of the refereed Campos-Wakabayashi
theorem (doi:10.1016/j.dam.2012.08.023); no originality claimed for the
inequality. Sharpness: (i) complete dihedral-quotiented peel-word enumeration
to n=20 with exact domination numbers (bitmask branch-and-bound branching on
the closed neighbourhood of the first uncovered vertex, greedy upper-bound
pruning, cross-validated by brute-force subset search for every
representative at n<=12), proving M(n)=floor((n+2)/4) for 10<=n<=20
independently of any citation; (ii) explicit periodic comb witnesses for
every 10<=n<=30, each certified by the exact solver (adjacency lists
shipped). For 21<=n<=30 the maximum is pinned between the proved ceiling and
the certified attaining family, hence exact without full
2^(n-4)-scale enumeration. End-block induction data (16/16 four-prefixes and
30/32 five-prefixes co-dominated, with 4-block fallback for LLLLR/RRRRL and
verified residue arithmetic) is published as verified data toward a
citation-free induction; the standard attachment-forcing step is honestly
flagged as not machine-closed, so the ceiling rests on the citation.

## Limitations

(i) The inequality is credited to Campos-Wakabayashi/Tokunaga, not proved
from scratch. (ii) Full distributions enumerated to n=20; for 21<=n<=30 only
the maximum is pinned (ceiling + attaining witness). (iii) Full extremal
classification up to dihedral isomorphism holds to n=20; beyond that one
certified family per n is shipped. (iv) No double-domination or partial
domination claims. (v) Pilot guesses (512 words at n=12, 256 extremals at
n=18, zigzag attains) were falsified and replaced by the verified integers.

## Reproducibility

Stdlib-only Python: snakes.py (peel-word generator, canonical quotient),
domsolve.py (exact B&B + brute force), extremals_10_30.json (21 certified
diagonal lists), table10_18.json (census rows). Recompute: enumerate
2^(n-4) fixed-ear words, quotient by canonical_key, solve gamma per
representative, compare to (n+2)//4. Full census to n=18 reruns in seconds,
to n=20 in minutes; n<=12 B&B-vs-brute agreement asserted in code.
Extremal check: build closed-neighbourhood bitmasks from each diagonal list
plus cycle edges and run gamma_exact.

## References

- C. N. Campos, Y. Wakabayashi, On dominating sets of maximal outerplanar
  graphs, Discrete Appl. Math. 161(3):330-335 (2013).
  doi:10.1016/j.dam.2012.08.023
- S. Tokunaga, Dominating sets of maximal outerplanar graphs,
  Discrete Appl. Math. 161:3097-3099 (2013).
  doi:10.1016/j.dam.2013.06.025
- W. Zhuang, Double domination in maximal outerplanar graphs,
  arXiv:2107.02796 (2021) — striped case for double domination only.
- J. D. Alvarado, S. Dantas, D. Rautenbach, Dominating sets inducing large
  components in maximal outerplanar graphs, arXiv:1511.08713 (2015).
- P. Borg, P. Kaemawichanurat, Partial domination of maximal outerplanar
  graphs, arXiv:1903.12292 (2019); Extensions of the Art Gallery Theorem,
  arXiv:2002.06014 (2020).
