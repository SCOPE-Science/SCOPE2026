# Minimum real rank of diagonal-ones binary matrices with no all-ones 2x2 submatrix: exact minima for n<=5 and a sharp ceil(3n/4) tiling bound

## Context

Rank rigidity of combinatorial matrices connects combinatorics, complexity (minrank, rigidity, biclique cover), and coding theory. Forbidding the all-ones 2x2 (J2), the bipartite C4 condition, is natural, but its effect on real rank under diagonal-ones normalization has no prior exact small-dimension formula. Maxima are trivial (identity gives n) while minima are nontrivial only because diagonal ones exclude the zero matrix; ratios are already non-monotone (3/3, 3/4, 4/5). Small n is exactly verifiable by integer rank computation, and any sharp bound gives a crisp auditable unit with a clear extremal construction (4-cycle tiling).

## Definitions

Let `[n]={0,...,n-1}`. Let `F_n` be the set of `n x n` `(0,1)`-matrices `M` with `M_ii=1` for all `i` and no `i<k, j<l` with `M_ij=M_il=M_kj=M_kl=1` (no all-ones 2x2 submatrix, rows/columns not necessarily consecutive). Write `F_i subset [n]` for support of row `i` (`i in F_i`), `w_i=|F_i|`, `c_j=|{i:j in F_i}|`, `W=sum w_i=sum c_j`. J2-free is `|F_i cap F_k|<=1` for `i!=k`. Transposition preserves `F_n` and rank. Simultaneous permutation `M -> P M P^T` preserves `F_n`, rank, and row-weight multiset. All ranks/determinants are over `Q` (hence over `R`) by exact Bareiss fraction-free elimination (no floating point).

Define `r(n)=min_{M in F_n} rank_R(M)`.

Lemma 1 (column disjointness). Fix column `j`. The sets `F_i\\{j}` over `i` containing `j` are pairwise disjoint. Hence `sum_{i ni j}(w_i-1)<=n-1`. Transposing gives `sum_{j in F_i}(c_j-1)<=n-1` for each `i`. Summing gives `sum_i w_i(w_i-1)<=n(n-1)` and `sum_j c_j(c_j-1)<=n(n-1)`. In particular each row pair shares at most one column, each column pair occurs in at most one row, and `P:={intersecting row pairs}=sum_j C(c_j,2)`.

Lemma 2 (weight-1 peeling). If `M in F_n` has a row equal to `e_i`, after simultaneously permuting `i` last, `M=[C *; 0 1]` with `C in F_{n-1}` and `rank(M)>=rank(C)+1>=r(n-1)+1`. Similarly if some column has weight 1 (by transpose). Proof: row `e_n` vanishes on first `n-1` columns; independent rows of `C` plus `e_n` stay independent by restriction.

Lemma 3 (weight-2 peeling). If `M in F_n` has a row of weight 2, after simultaneous permutation assume row 0 `={0,1}`. Then row 1 does not contain 0 (else rows 0,1 share `{0,1}`), row 0 vanishes outside `{0,1}`, and `E0:=M` with rows `{0,1}` and columns `{0,1}` deleted is in `F_{n-2}`. Moreover `rank(M)>=rank(E0)+1>=r(n-2)+1`. Transpose holds for weight-2 columns. Proof: `E0` inherits diagonal ones/J2; independent rows of `E0` plus row 0 stay independent since row 0 is zero on `E0` columns.

## Result

Theorem A (exact small-n). Over `Q` (hence `R`): `r(2)=2, r(3)=3, r(4)=3, r(5)=4`. Survivor/minimizer counts: `|F_2|=3` (all rank 2); `|F_3|=21` (all rank 3); `|F_4|=311` (6 rank 3, 305 rank 4); `|F_5|=8995` (390 rank 4, 8605 rank 5). Up to simultaneous permutation minimizers form 1 orbit (size 6) for `n=4` and 5 orbits (sizes 120,120,60,60,30) for `n=5`. Every `n=4` survivor has a nonsingular `3x3` minor; every `n=5` survivor has a nonsingular `4x4` minor (explicit integer determinants).

Theorem B (general upper bound). For all `n`, `r(n)<=ceil(3n/4)`. Construction: tile `floor(n/4)` disjoint 4-sets; on each `{a,b,c,d}` put ones at `(a,a),(a,b),(b,b),(b,c),(c,c),(c,d),(d,d),(d,a)` and zeros elsewhere in those rows/columns; identity on remainder (`<4` indices). E.g. block `[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]`, masks `(3,6,12,9)` locally.

Theorem C (weight<=2 optimality). If `M in F_n` has max row weight `<=2`, then `rank(M)>=ceil(3n/4)` for all `n`. Hence the tiling is optimal among weight<=2 matrices.

Theorem D (general lower bound to n<=8). `r(n)>=ceil(n/2)` for `n<=8`.

Conjecture E. `r(n)=ceil(3n/4)` for all `n`.

## Proof / Evidence

Theorem A lower bounds by hand (no computer needed for inequalities). `r(2)=2`: 2 off-diagonal bits; J2-free excludes only all-ones; remaining three matrices `[[1,0],[0,1]],[[1,1],[0,1]],[[1,0],[1,1]]` all have determinant 1. `r(3)=3`: if some row has weight 1, `det(M)=det` of `2x2` principal minor deleting that row/column (expand along `e_i`); minor is diagonal-ones J2-free `2x2` hence not all-ones hence det 1. Else all `w_i>=2`; `sum w_i(w_i-1)<=6` forces `(2,2,2)` (any 3 gives `2+2+6=10>6`). Each row `{i,f(i)}`, `f(i)!=i`; 2-cycle `f(i)=k,f(k)=i` gives shared `{i,k}` forbidden, so `f` is fixed-point-free with no 2-cycles on 3 points, hence a 3-cycle (two possibilities), e.g. `[[1,1,0],[0,1,1],[1,0,1]]` det 2. So all 21 survivors nonsingular. `r(4)>=3`: weight-1 gives `1+r(3)=4>=3`; weight-2 gives `1+r(2)=3`; all `>=3` gives `4*6=24>12` impossible. `r(5)>=4`: weight-1 gives `1+r(4)=4`; weight-2 gives `1+r(3)=4`; all `>=3` gives `5*6=30>20` impossible. Upper bounds by Theorem B (4-cycle for `n=4`; 4-cycle plus isolated 1 for `n=5`).

Computer certificate (independent cross-check + classification). Exhaustive bitmask over `2^{n(n-1)}` completions (4;64;4096;1048576) with popcount J2 test and Bareiss rank gives counts above in ~3s stdlib-only (`enumerate.py`). Canonical forms under all `n!` simultaneous permutations give orbit numbers (`classify.py`). `export` verifies a nonsingular `3x3` (`n=4`) resp. `4x4` (`n=5`) minor for every survivor by Bareiss determinants. Weight data: `n=3` splits `(1,2,2)x9,(1,1,2)x6,(1,1,3)x3,(2,2,2)x2,(1,1,1)x1` dets `1(x19),2(x2)`; `n=4` minimizer orbit e.g. permuted 4-cycle weights `(2,2,2,2)`; `n=5` minimizer orbits include `(1,2,2,2,3),(2,2,2,2,2),(1,2,2,3,3),(2,2,3,2,2),(1,2,2,2,2)` showing isolated rows can occur in optima.

Theorem B proof. Within a block pairwise intersections are 1 (adjacent in directed 4-cycle) or 0 (opposite); across blocks supports disjoint (block-diagonal) so 0; hence J2-free. Each 4-block has `r_a+r_c-r_b-r_d=0` (null vector `(1,-1,1,-1)`) so rank<=3, and top-left `3x3` `[[1,1,0],[0,1,1],[0,0,1]]` det 1 so exactly 3. Identity remainder contributes its size. Total `3*floor(n/4)+(n mod 4)=ceil(3n/4)` (check residues 0..3). Verified by exact rank for `n<=12` in `search.py`.

Theorem C proof by induction. Weight<=2 J2-free means each row `e_i` or `{i,f(i)}`; J2-free iff no 2-cycles `f(i)=k,f(k)=i` (weight-1 rows never cause J2; two weight-2 rows share 2 iff equal 2-sets iff 2-cycle). If some `f(i)=i` (weight 1), Lemma 2 gives `1+ceil(3(n-1)/4)>=ceil(3n/4)` (residues checked) with `C` still weight<=2. Else all weights 2. If some vertex has indegree 0, its column has sole one at its row, so column `e_1` after permuting leaf first and `rank=1+rank(C)` with `C` still weight<=2 (no one points to leaf), induction as above. Else min indegree>=1 with sum `n` forces indegree exactly 1 everywhere: disjoint directed cycles covering all vertices, lengths `!=1,!=2` so `>=3`. `M` is block-diagonal over cycles. `L`-cycle block `I+P` has `det=2` if `L` odd (`det(I+P)=1-(-1)^L` via `lambda^L-1` at `-1`, eigenvalues `1+omega`) hence full rank `L`, and rank `L-1` if `L` even (alternating null vector; delete one row/column leaves triangular det 1). For even `L>=4`, `L-1>=3L/4` equality only at 4; for odd `L`, `L>=3L/4`. Summing gives `>=3n/4`, integer rounding gives ceil. Base `n=1` holds. Exhaustive functional enumeration (`weight2.py`) gives min 5 (`n=6`, 28821 valid) and min 6 (`n=7`, 505876 valid), exhaustive min 6 at `n=8`, matching `ceil(3n/4)`.

Theorem D proof. Frobenius: for `G=M M^T` (diag `w_i`, off-diag `0/1` with `P` ones above diagonal), `rank(M)=rank(G)>=(tr G)^2/||G||_F^2=W^2/(sum w_i^2+2P)` by Cauchy on eigenvalues. Induction base `n<=5` by Theorem A. For `n>=6`, weight-1 gives `1+ceil((n-1)/2)>=ceil(n/2)`; weight-2 gives `1+ceil((n-2)/2)>=ceil(n/2)`; transpose covers light columns. Else all rows and columns `>=3` (else transpose peeling). Then `n>=7` else `6n>n(n-1)`, so `n=6` already covered. For `n<=8` use `Sr-W<=n(n-1)`, `Sc-W<=n(n-1)` so `Sr+Sc<=2W+2n(n-1)`; need `Sr+Sc<=2W^2/n+W` i.e. `W+2n(n-1)<=2W^2/n` i.e. `2W^2-Wn-2n^2(n-1)>=0`, increasing in `W`, minimal at `W=3n` giving `n^2(17-2n)>=0` true for `n<=8`. Hence `W^2/(Sr+2P)>=n/2` (using `2P=Sc-W`), integer rounding gives ceil. Beyond `n<=8` light cases still reduce with ratio `>=1/2` but all`>=3` with `n>=9` left open.

Conjecture support (not proof): exact `n<=5` match; Theorem C shows no weight<=2 counterexample; exhaustive weight<=2 at `n=6,7` attains 5,6; sampled at `n=8` attains 6; random/greedy dense matrices have rank near `n`; single-bit-flip local search from tiling cannot improve at `n=6..12`. Weight-3 beating construction would refute; none found.

## Limitations

- General `ceil(n/2)` proved only to `n<=8`; `n>=9` all`>=3` family open (coarse KST+Frobenius gives `n^2(17-2n)>=0` failing at `n>=9`; joint variance bound not closed).
- General `ceil(3n/4)` proved only for weight<=2; full version is Conjecture E.
- `n=5` counts/orbits rely on computer enumeration grouped to 107 survivor orbits with explicit minors; human induction gives `>=4`, computer gives counts/orbits.
- Originality comparison limited to Boolean-rank/isolation, graph minrank, small-real-rank sources; no exhaustive literature priority claimed.
- Deposited `minors_n5.csv` in inputs had rep/minor mismatch (minor for different orbit member); corrected per-rep minors provided here; verify corrected file, not old literal pairing.

## Reproducibility

Stdlib-only Python 3.12. `enumerate.py` (exhaustive `n<=5`, ~3s for `n=5` 1048576 cases), `classify.py` (orbits under `n!` simultaneous perms, minor search), `search.py` (tiling verification `n<=12` + heuristic random `tries=3000` + local `iters=2000` seed 0), `weight2.py` (functional enumeration `n^n` full to `n=8`, sampled beyond). Bareiss elimination throughout; J2 test by pairwise `popcount<=1`. Commands: `python3 enumerate.py`; `python3 classify.py` (n=4,5); `python3 search.py`; `python3 weight2.py` (long for n=8: 16M functions). All ranks cross-checked vs `Fraction` exact arithmetic.

## References (comparison only, not used)

- R. A. Kovacs, On Minimally Non-Firm Binary Matrices, arXiv:2206.04089 (2022). Same J2 config for Boolean rank vs isolation number and firmness; different rank/objective. https://arxiv.org/abs/2206.04089
- I. Haviv, On Minrank and Forbidden Subgraphs, arXiv:1806.00638 (2018). Minrank over fits maximized over H-free complements; different rank notion/direction. https://arxiv.org/abs/1806.00638
- M. Parnas, A. Shraibman, A Study of the Binary and Boolean Rank of Matrices with Small Constant Real Rank, arXiv:2507.05824 (2025). Fixes real rank d<=4, bounds binary/Boolean above; orthogonal direction. https://arxiv.org/abs/2507.05824
