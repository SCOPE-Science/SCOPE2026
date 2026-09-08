# Substitution-skeleton census for length-4 principal classes, n = 8..11

## Context

Substitution decomposition (Albert–Atkinson program, continued by Vatter; surveyed by Brignall)
reduces every pattern class to its simple-permutation skeleton: classes with finitely many
simple permutations are algebraically tractable, while simple-rich classes drive non-D-finite
complexity. No per-class simple / sum / skew / inflation census across the single length-4
principal classes existed (databases hold only bare avoidance totals and global simple totals).
This record supplies that exact skeleton data for the closed natural unit of all symmetry
classes × consecutive lengths 8–11.

## Definitions

- A permutation is a list `p[1..n]` of `{1..n}`. A pattern occurrence of `pi` (length 4) is
  indices `i1<i2<i3<i4` whose four values have the same relative order as `pi`.
  `Av_n(pi)` = permutations of length `n` with no occurrence of `pi`.
- An *interval* (block) is a contiguous index segment whose values form a contiguous integer
  set. A permutation (`n ≥ 4`) is *simple* if its only intervals are singletons and the whole
  permutation. It is *sum-decomposable* if some proper prefix has values `{1..k}`;
  *skew-decomposable* if some proper prefix has values `{n-k+1..n}`. These two categories are
  disjoint (verified exhaustively: no overlap in S8). Otherwise the substitution decomposition
  theorem gives a unique finest interval partition into ≥ 2 blocks whose quotient is a simple
  permutation of length ≥ 4; this case is called *inflation* and the quotient length (minimum
  block count over all interval partitions) is recorded.
- The 7 dihedral representatives `1234, 1243, 1324, 1342, 1432, 2143, 2413` cover all 24
  length-4 patterns under reverse / complement / inverse; each symmetry maps intervals to
  intervals and hence preserves substitution type (orbit sizes 2,4,2,8,4,2,2 verified).

## Result

Exact type partition simple / sum / skew / inflation (totals in parentheses).
Full quotient-length histograms are in `artifacts/results_<pi>.json`.

| pi   | n=8 (total)                 | n=9 (total)                    | n=10 (total)                      | n=11 (total)                         |
|------|-----------------------------|--------------------------------|-----------------------------------|--------------------------------------|
| 1234 | 1437/1222/6376/6732 (15767) | 8155/4074/36922/45208 (94359)  | 47197/13789/222817/302787 (586590) | 278611/47371/1391739/2045569 (3763290) |
| 1243 | 706/3189/6376/5496 (15767)  | 3682/17196/36922/36559 (94359) | 19872/99220/222817/244681 (586590) | 110216/603385/1391739/1657950 (3763290) |
| 1324 | 603/1430/6378/7382 (15793)  | 3020/5070/36975/49711 (94776)  | 15714/18122/223681/334433 (591950) | 84388/65246/1402997/2271481 (3824112) |
| 1342 | 323/3873/6333/4956 (15485)  | 1443/21031/36333/32438 (91245) | 6676/120258/216206/212522 (555662) | 31654/716403/1325202/1401831 (3475090) |
| 1432 | 674/3895/6376/4822 (15767)  | 3423/21336/36922/32678 (94359) | 18011/123701/222817/222061 (586590) | 97564/751128/1391739/1522859 (3763290) |
| 2143 | 478/5009/6376/3904 (15767)  | 2450/28773/36922/26214 (94359) | 13074/172951/222817/177748 (586590) | 71846/1078821/1391739/1220884 (3763290) |
| 2413 | 72/6333/6333/2747 (15485)   | 280/36333/36333/18299 (91245)  | 1150/216206/216206/122100 (555662) | 4830/1325202/1325202/819856 (3475090) |

Selected quotient-length profiles at n=11 (lengths 4..10):

- 1234: 65528 / 58706 / 134610 / 233476 / 408192 / 577819 / 567238.
- 1324: 124032 / 149762 / 304582 / 428588 / 516840 / 466307 / 281370.
- 2413: 281512 / 91390 / 157824 / 116802 / 93888 / 55440 / 23000.

Exact sum = skew symmetry holds in Av(2413) at all n (internal certificate).

**Extremal ranking (simple-rich vs simple-poor).** Simple counts rank identically at every
n = 8, 9, 10, 11:

> 1234 (max) > 1243 > 1432 > 1324 > 2143 > 1342 > 2413 (min).

At n=11: 278611 vs 110216 vs 97564 vs 84388 vs 71846 vs 31654 vs 4830.
Max/min margin 278611 − 4830 = 273781 (ratio ≈ 57.7×); max/runner-up margin
278611 − 110216 = 168395. Simple density at n=11 ranges from 7.40% (1234) to 0.14% (2413).

**Explicit witnesses (n=11, interval-free, avoidance re-verified):**

- `2 6 11 1 10 5 9 4 8 3 7` in Av_11(1234), simple.
- `7 1 3 8 4 9 5 10 6 11 2` in Av_11(2413), simple.
- `2 4 6 8 10 1 11 9 7 5 3` in Av_11(1324), simple.
- One simple witness per (pi, n) stored in `artifacts/witnesses_<pi>.txt` (28 total).

## Proof / evidence

Computational exhaustion with two agreeing implementations (not a closed form):

- Script A (`artifacts/enum.c`, C, `-O2`): depth-first backtracking placing values left to
  right, abandoning a prefix as soon as the newest value completes a pi-occurrence; O(n²)
  interval scan classifies each leaf; minimum-block mask search records inflation quotient
  length with quotient-simplicity assertion (`anomalies = 0` in all 28 cells).
- Script B (`artifacts/crosscheck.py`, Python): independent `brute` (itertools),
  `backtrack`, and `samples` re-verification modes.
- Full dual agreement: all 7 classes at n=8 by brute force; 2413 and 1324 at n=9 by
  backtracking (plus independent audit brute force for all 7 at n=8, backtrack AGREE for
  2413/1324 at n=9); all n=10,11 quota samples plus all 28 witnesses re-verified
  (`SAMPLES-OK` × 14, 55 checks each).
- Consistency identities: type counts sum to totals in all 28 cells; qhist sums to inflation
  counts in all 28 cells; 2413 sum = skew exactly; Wilf-class total equalities hold;
  Av(1324) totals match OEIS A061552 (15793/94776/591950/3824112).
- Auditor rebuilt Script A from source and re-ran full n=8..11 closures for 2413 and 1324
  with byte-identical counts, and independently brute-forced all 7 classes at n=8 to exact
  agreement including qhist.

## Limitations

- Counts are computational (exhaustive backtracking with pruning), not closed forms.
- Full dual enumeration covers n=8 (brute) and n=9 (backtrack); n=10,11 full tables rest on
  Script A plus quota-sample/witness re-verification and consistency identities.
- Claims are confined to the 7 × (n=8..11) window; no asymptotics, growth rates, or
  Wilf-classification beyond the observed total equalities are claimed.

## Reproducibility

Build with `gcc -O2 -o enum artifacts/enum.c`; run `./enum <PATTERN> artifacts/` for each
of the 7 patterns (~10–17 s for the largest cell Av_11(1324), single core, parallel-safe);
then `python3 artifacts/crosscheck.py {brute|backtrack|samples} <PAT> <n>`.
Committed `results_<pi>.json` files carry the type counts, qhist, anomalies, and cpu times.

## References

- R. Brignall, A Survey of Simple Permutations, arXiv:0801.0963.
- M. H. Albert and M. D. Atkinson, Simple permutations and pattern restricted permutations,
  Discrete Math. 300 (2005), 1–15 (via OEIS A111111 links).
- E. Bagno et al., Blockwise simple permutations, arXiv:2303.13115 (different object).
- A. L. L. Gao, S. Kitaev, P. B. Zhang, On pattern avoiding indecomposable permutations,
  arXiv:1605.05490 (sum-indecomposable axis only).
- OEIS A061552 (1324-avoiding totals); OEIS A111111 (global simple-permutation totals).
