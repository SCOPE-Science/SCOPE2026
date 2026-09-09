# Complete order-polytope Ehrhart census for all unlabeled posets with n <= 6

## Context

For a finite poset $P$ on $n$ elements, Stanley's order polytope
$O(P) \\subset [0,1]^n$ is $\\{x : 0 \\le x \\le 1,\\ x_a \\le x_b$ whenever
$a \\le_P b\\}$. Its normalized volume satisfies $V(P) = e(P)$ where $e(P)$
is the number of linear extensions, and its Ehrhart polynomial
$i(O(P),m) = |m\\,O(P) \\cap \\mathbb{Z}^n|$ counts weakly order-preserving
maps $P \\to [m+1]$. Its $h^*$-vector encodes the Ehrhart series numerator.
General theorems (Stanley 1986), enumerations of unlabeled posets
(OEIS A000112; Brinkmann-McKay; FindStat to $n=7$), linear-extension tables
(FindStat St000100), and family-specific Ehrhart formulas (zig-zag, crown,
snake, skew, graded) plus positivity theorems (dimension $\\le 13$ positive;
non-positivity from dimension $\\ge 21$) were known. No exhaustive
per-type Ehrhart-polynomial table over all $318$ six-element types existed.

## Definitions

- $\\mathcal{P}_n$: set of unlabeled (non-isomorphic) poset types on $n$ elements.
- $O(P)$: order polytope of $P$.
- $i(O(P),m)$: Ehrhart polynomial; $L$-values $i(m)$, $0 \\le m \\le n$.
- $e(P)$: number of linear extensions of $P$.
- $V(P)$: normalized volume $n! \\cdot [m^n]i(O(P),m)$.
- $h^*$: $h^*$-vector from $L(j)=\\sum_{i\\le j} h_i\\binom{j+n-i}{n}$.
- Record index: type ordering in `posets.json` / `ehrhart.json` (index 0 = antichain at each $n$).

## Result (machine-verified census)

Fix $n \\le 6$. Regenerated from scratch,
$|\\mathcal{P}_n| = 1,1,2,5,16,63,318$ for $n=0,\\dots,6$ (406 types total).

1. **Ehrhart table.** For every one of the 406 types, `ehrhart.json` stores
   the exact Ehrhart polynomial (ascending rational coefficients), the values
   $i(m)$, $0 \\le m \\le n$, the $h^*$-vector, and $e(P)$.
2. **Dual volume agreement.** For every type,
   $V(P) = n!\\cdot[m^n]i(O(P),m) = e(P)$,
   where the middle term uses ideal-lattice DP and the right term uses
   independent minimal-element backtracking (the count of top simplices of
   the Stanley triangulation, via cited Stanley theory). All 406 equalities hold.
3. **Maximal-volume witnesses.** Exhaustive comparison gives
   $\\max_{P\\in\\mathcal{P}_n} V(P) = 1,1,2,6,24,120,720$ for $n=0,\\dots,6$,
   each attained uniquely by the $n$-element antichain (record index 0;
   at $n=6$ maximum 720, runner-up 360, minimum 1 at the chain).
4. **Reciprocity.** Every type satisfies Ehrhart-Macdonald reciprocity
   $i(O(P),-m)=(-1)^n\\bar\\Omega_P(m)$ for $1 \\le m \\le n+1$
   ($\\bar\\Omega_P$ = strict order-preserving maps, independently computed).
   All 406 checks pass; all $h^*$-vectors are nonnegative integers summing to $e(P)$.

Examples ($n=6$): antichain (idx 0): $e=720$, $i(m)=(m+1)^6$ with values
$1,64,729,4096,15625,46656,117649$, $h^*=(1,57,302,302,57,1,0)$;
chain (idx 317): $e=1$, $i(m)=\\binom{m+6}{6}$ with values
$1,7,28,84,210,462,924$, $h^*=(1,0,0,0,0,0,0)$.

## Proof / evidence

Exact machine computation in stdlib-only Python with independent replay:

- `gen.py`: enumerates naturally labeled posets (upper-triangular transitive
  masks; every iso class meets this set via a linear extension), quotients by
  the minimum full-relation bitmask over $S_n$; asserts A000112 counts.
- `ehr.py`: per type computes $e(P)$ two ways (ideal-lattice DP and
  minimal-element backtracking), Ehrhart values by memoized ideal-fiber
  recursion $L(Q,m)=\\sum_{I \\lhd Q} L(Q\\setminus I,m-1)$, exact Fraction
  interpolation, $h^*$ by forward substitution, strict maps by antichain-fiber
  recursion, exhaustive per-$n$ maxima; asserts volume agreement and reciprocity.
- `verify.py`: independently replays from committed tables — counts (V1),
  poset axioms (V2), pairwise non-isomorphism by independent $S_n$ signature
  (V3), coefficient/value consistency, $L(1)=\\#$ideals, lead$\
  \\cdot n! = e$, $h^*$ agreement (V4), backtracking $e$ replay (V5),
  reciprocity (V6), maximality replay (V7) — printing `ALL VERIFY_OK`.
- Auditor reran `verify.py`: `ALL VERIFY_OK`; additionally brute-forced all
  weak maps (random types $n=2$..$6$) and all strict maps ($n=3$..$5$),
  permutation-scan linear extensions ($n=4,5$), and the antichain/chain closed
  forms — all matched. At $n=6$ there are 121 distinct Ehrhart $L$-value
  vectors vs 62 distinct $e$ values, so the table strictly refines volumes.

## Limitations

- Scope is $n \\le 6$ only; no general volume inequality or family closed forms claimed.
- Volume values alone follow from FindStat $e(P)$ via Stanley's theorem; the new
  artifact is the full per-type Ehrhart census with dual agreement, reciprocity,
  and certified extremal witnesses.
- Completeness relies on the standard lemma that each iso class has a naturally
  labeled representative; the geometric triangulation identification relies on
  cited Stanley theory as background, not recomputed geometry.
- Correctness is machine-certified exact computation plus independent replay,
  not a hand proof.

## Reproducibility

```
cd output/artifacts
python3 gen.py      # -> posets.json (406 types; asserts A000112 counts)
python3 ehr.py      # -> ehrhart.json (asserts volume agreement + reciprocity)
python3 verify.py   # -> verify.log, ALL VERIFY_OK
```

Stdlib only (plus numpy in `gen.py`); verified with Python 3.12.3.

## References

- R. P. Stanley, Two poset polytopes, Discrete Comput. Geom. 1986. https://doi.org/10.1007/BF02712865
- OEIS A000112. https://oeis.org/A000112
- FindStat, Posets collection. https://www.findstat.org/CollectionsDatabase/Posets/
- FindStat St000100, Number of linear extensions. https://www.findstat.org/StatisticsDatabase/St000100/
- G. Brinkmann and B. D. McKay, Posets on up to 16 points, Order 2002. https://doi.org/10.1023/A:1016543307592
- T. Chappell, T. Friedl, R. Sanyal, Two double poset polytopes, arXiv:1606.04938. https://arxiv.org/abs/1606.04938
- F. Liu, G. Xin, Z. Zhang, Order polytopes of dimension <= 13 are Ehrhart positive, arXiv:2412.07164. https://arxiv.org/abs/2412.07164
