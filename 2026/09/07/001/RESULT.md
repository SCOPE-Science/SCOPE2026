# Sharp 1-forbidden bound for 4-sets on 8 points: maximum is 17, unique ball

## Context

Restricted-intersection theorems (Erdos-Ko-Rado, Ahlswede-Khachatrian Complete Intersection Theorem, Frankl forbidden-intersection theorems, Ellis-Keller-Lifshitz stability, Kupavskii-Zakharov spread approximations) determine extremals for `n` large relative to `k`, where the `(l+1)`-star dominates. At small `n` a second construction --- all `k`-sets inside a `(2k-l-1)`-set --- competes. The assigned target for `(n,k,l)=(8,4,1)` asserted max `<=15` with a star-clique tie `C(6,2)=C(6,4)=15` provable by shifting plus double-counting. That target is false. This record gives the corrected sharp bound.

## Definitions

- Ground set `[8]={1,...,8}`; `C([8],4)` has 70 sets.
- `F subset C([8],4)` is **1-free** if `|A cap B| != 1` for all distinct `A,B in F`.
- `M = max |F|` over 1-free `F`.
- Pair-star: all 4-sets containing a fixed pair `{i,j}`, size `C(6,2)=15`.
- K6-clique: all 4-sets contained in a fixed 6-set, size `C(6,4)=15`.
- Ball: for a 4-set `S`, `B(S)={A:|A cap S|>=3}`, size `1+C(4,3)*C(4,1)=17`.

## Result

**Theorem.** Let `F subset C([8],4)` have no two distinct members intersecting in exactly one element. Then `|F| <= 17`. The bound is sharp and equality holds iff `F=B(S)` for some 4-set `S` (up to permutation, unique extremal). In particular the pair-star (15) and K6-clique (15) are valid 1-free families but not optimal. Frankl `(i,j)`-shifts do not preserve 1-freeness.

## Proof / Evidence

**Lower bound (by hand).** `|B(S)|=1+16=17`. If `A,B in B(S)` then `A cap S, B cap S subset S` have size `>=3`, so `|A cap B| >= |(A cap S) cap (B cap S)| >= 3+3-4=2`. Hence `B(S)` is 1-free; `M>=17`. Star/clique 1-freeness: star contains fixed pair (`inter>=2`); clique lies in 6-set (`|A union B|<=6` so `inter>=2`).

**Shifting is invalid (explicit counterexample).** `F={{2,3,4,5},{1,6,7,8}}` is 1-free (`inter=0`), but `S_{1,2}(F)={{1,3,4,5},{1,6,7,8}}` has `inter=1`. Standard shifting preserves monotone `>=t` properties, not forbidden exact values. No reduction to shifted families is available.

**Upper bound (symmetry + exact computation).**
- Lemma 1 (transitivity): it suffices to bound families containing `1234`.
- Lemma 2 (three second sets): `Stab(1234)=S_{1..4} x S_{5..8}` (576 perms) acts transitively on `{B:|B cap 1234|=a}` for each `a`; `a=1` excluded by 1-freeness, `a=4` gives `B=1234`. Representatives: `a=0:5678` (orbit 1), `a=3:1235` (orbit 16), `a=2:1256` (orbit 36).
- Computation: for each rep `r` let `P_r` be sets compatible with both fixed sets (`|P_r|=36/42/40`). Exact branch-and-bound (bitmask sets; prunes: popcount bound, forced inclusion of isolated vertices by exchange argument, greedy clique-cover bound, exhaustive include/exclude on max-degree vertex) certifies no 16 more in any case (31/167/69 nodes; 267 total), i.e. no 1-free family over `{1234,r}` reaches size 18. Redundant direct search on the full 53-set pool compatible with `1234` confirms no 17 more. Hence no 1-free family has size `>=18`: `M<=17`. Combined `M=17`.

**Uniqueness (exact enumeration).** Exhaustive enumeration of all 17-sets containing `1234` finds exactly 17 families --- precisely the balls `B(S)` for the 17 centers `S in B(1234)`, all verified 1-free and distinct. Since `S8` acts transitively on 4-sets and `pi(B(S))=B(pi(S))`, they form a single orbit. Every max family is permuted into one of these, so every extremal is a ball.

**Remark on counting.** Pair/triple convexity alone cannot bound `m`: at `m=18` the constraints `N2+3N3>=156`, `N2+N3<=153` are jointly satisfiable, so structure must come from symmetry plus search.

## Limitations

- Upper bound and uniqueness are computer-assisted (exact integer branch-and-bound, not fully human case analysis). Correctness rests on auditable pruning rules plus independent cross-checks (two search paths, predicted-count match 17=17, independent Max-Clique re-proof with 47/79/383 nodes and independent enumeration with 24809 nodes).
- Literature search was limited to main lines; the 17-ball may appear in an obscure table/thesis. Claimed as corrected sharp bound with proof, not a new general theory.
- Scope strictly `(n,k,l)=(8,4,1)`; no asymptotic claims.

## Reproducibility

Stdlib-only Python, seconds. Master check `artifacts/final_verify.py` asserts: both 15-constructions 1-free; shifting counterexample `0->1`; ball 17 1-free and maximal; no-18 in all three orbit cases; full-pool cross-check; 17 distinct 1-free balls from 17 candidate centers. `artifacts/bnb.py` redoes per-case decisions; `artifacts/enumerate17.py` redoes uniqueness enumeration (exactly 17, one orbit, all balls). Auditor independently re-proved max with a Tomita-style Max-Clique coloring-bound solver and re-enumerated with ordered-combination DFS.

## References

- Ellis-Keller-Lifshitz, Stability for the Complete Intersection Theorem, and the Forbidden Intersection Problem of Erdos and Sos, arXiv:1604.06135 (excludes `n/2-o(n)<k<n/2+t/2`, hence `(8,4,1)`).
- Kupavskii-Zakharov, Spread approximations for forbidden intersections problems, arXiv:2203.13379 (asymptotic, no small-n sharp constant).
- Frankl, Forbidden intersections, Trans. AMS 1987, doi:10.1090/S0002-9947-1987-0871675-6; Frankl-Tokushige survey (large-n star dominance).
- Ahlswede-Khachatrian Complete Intersection Theorem (ball as 2-intersecting family; new here is optimality among 1-free allowing 0).
