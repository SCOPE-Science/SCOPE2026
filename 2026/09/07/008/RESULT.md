# Certified census of the binary 5x5 rank-3 stratum: 713 classes with nonnegative rank 3, 6 with nonnegative rank 4, none with 5

## Context
Nonnegative rank equals extension complexity of a slack matrix and lower-bounds randomized communication complexity. Concrete 5x5 examples are dominated by irrational polygon slacks (e.g. regular pentagon, rank 3 and nonnegative rank 5 with golden-ratio entries) with no certified bounded-integer tables. A small-entry integer census shows where the rank vs nonnegative-rank gap first appears over integers and grounds future extension-complexity constructions.

## Definitions
For $M \\ge 0$ entrywise, $\\mathrm{rank}(M)$ is ordinary rank over $\\mathbb{Q}$ and $\\mathrm{rank}_+(M)=\\min\\{r: M=WH,\\, W\\in\\mathbb{R}_+^{5\\times r}, H\\in\\mathbb{R}_+^{r\\times 5}\\}$. Monomial equivalence is $M\\mapsto PMQ$ with permutation matrices $P,Q$, plus transpose; it preserves rank and nonnegative rank. A fooling set of size $k$ is pairs $(i_1,j_1),\\dots,(i_k,j_k)$ with $M_{i_t,j_t}>0$ and $M_{i_t,j_s}M_{i_s,j_t}=0$ for all $t\\ne s$. Lemma: a fooling set of size $k$ implies $\\mathrm{rank}_+(M)\\ge k$ (two fooling positions cannot share the same nonnegative rank-1 component with both products positive). A covering of the ones by $k$ all-ones submatrices likewise needs $k\\le \\mathrm{rank}_+$ for binary $M$.

## Result (theorem)
Up to row/column permutations and transpose there are exactly 719 binary $5\\times 5$ matrices of rank 3. Of these 713 have $\\mathrm{rank}_+=3$ and 6 have $\\mathrm{rank}_+=4$. Hence no $\\{0,1\\}^{5\\times 5}$ matrix has $\\mathrm{rank}=3$ and $\\mathrm{rank}_+=5$.

Counts are of canonical classes; in column-multiset terms the 719 classes cover 63,015 multisets (orbit sizes 10-180, mean 87.6). The full table with one representative per class, exact factors, and fooling data is `artifacts/census.csv`.

## Proof / evidence
- Enumeration: a $5\\times 5$ binary matrix up to column permutations is a multiset of 5 column values in 0..31; there are $\\binom{36}{5}=376{,}992$. All are enumerated, rank by batched SVD with exactness cross-check, giving 63,015 rank-3 multisets with histogram {0:1,1:155,2:5550,3:63015,4:203985,5:104286}. Canonical invariant: for $M$ let $V$ be its 5 column values, $W$ its 5 row values; for each of 120 row-permutations compute sorted-tuple base-32 code on $V$ and on $W$; take the minimum over all 240. This is $\\min(\\mathrm{canon}(M),\\mathrm{canon}(M^T))$, hence a complete orbit invariant. Distinct minima: 719. Audit re-enumerates all 376,992 from scratch and reproduces the 719-code set. SVD safety: min 4th singular value among rank-4 is 0.262 and max noise among rank-3 is 6.2e-16 vs tolerance ~5.5e-15.
- Ranks: each of the 719 representatives has rank 3 proved twice — fraction-free Bareiss elimination (integer only) and `sympy.Matrix.rank()`.
- Upper bounds (exact subset certificates): if $r$ columns of $M$ conically generate all 5 columns over $\\mathbb{Q}_+$ then $\\mathrm{rank}_+(M)\\le r$ with $W$ those columns. Cone membership $Wh=m$, $h\\ge 0$ is decided exactly over Fractions. NMF(4) with $W=4$ columns of $M$ succeeds for all 719 (hence $\\mathrm{rank}_+\\le 4$ everywhere). NMF(3) with $W=3$ columns succeeds for 651; NMF(3) with $H=3$ rows succeeds for the remaining 62. Thus all 713 have exact rational NMF(3); all 6 gap classes have exact rational NMF(4). All equalities $M=WH\\ge 0$ verified in Fractions.
- Lower bounds and classification: the 713 with exact NMF(3) have $\\mathrm{rank}_+=3$ ($\\mathrm{rank}\\le\\mathrm{rank}_+\\le 3$). The 6 remaining have explicit fooling sets of size 4 (stored in `fooling_witnesses.json`, verified entry-by-entry), so $\\mathrm{rank}_+\\ge 4$; with NMF(4) they equal 4. Rectangle-covering numbers agree (4 on exactly these six, 3 on 679, 2 on 34). Floating ANLS was used only for discovery (residuals $\\le 5$e-12 vs $\\ge 0.76$).
- Explicit gap-4 witnesses (Beasley-Laffey extensions): cleanest with no zero row/column (orbit 664, duplicate rows 3==4):
  `M664 = [[1,1,0,0,1],[1,0,1,0,1],[0,1,0,1,1],[0,0,1,1,1],[0,0,1,1,1]]`
  Exact NMF(4): $W$ = first four columns, $H=[I_4\\mid(1,0,0,1)^T]$. Fooling set rows/cols {0,1,2,3} pairs (0,0),(1,2),(2,1),(3,3). Hence $\\mathrm{rank}_+\\ge 4$; with factor $=4$; ordinary rank 3 by Bareiss. All six gaps are degenerate lifts of the 4-cycle (each has a zero and/or duplicate row/column); no primitive binary gap exists.
- Ternary search (negative heuristic, not a theorem): {0,1,2} matrices with fooling-5 pattern searched (800k uniform draws all rank >=4; 30x4000 annealed hill-climbing on 4th singular value best 0.154, never near 0). No witness found. This excludes only sampled fooling-5 witnesses, not all geometric witnesses.

## Limitations
(i) Target {0,1,2} rank-3 vs rank-5 witness not found; ternary nonexistence not claimed (fooling-only heuristic, no nested-polygon/SDP prover). (ii) Census is up to monomial+transpose with column-multiset intermediate — orbit sizes are multiset counts (sum 63,015), not raw $2^{25}$ counts. (iii) Rectangle-covering code is exact but exponential in general (fine for 5x5). (iv) No originality claimed for the 4-cycle pattern itself, only for the complete certified 5x5 binary table.

## Reproducibility
`artifacts/audit.py` (numpy+sympy only, ~1.8s): checks counts (719, sizes sum 63015, 713/6 split), Bareiss+SymPy rank, Fractions $M=WH\\ge 0$ for all 719, fooling witnesses for six, full 376,992 re-enumeration with canon-set equality, 500 SVD/Bareiss spot-checks. Run: `python3 output/artifacts/audit.py`.

## References
- Beasley and Laffey, Real and complex ranks with respect to nonnegative matrices, Linear Algebra Appl. 2009. https://doi.org/10.1016/j.laa.2009.03.050 — isolated 4x4 rank-3/rank-4; no 5x5 census.
- Gillis and Glineur, On the geometric interpretation of the nonnegative rank, Linear Algebra Appl. 2012. https://doi.org/10.1016/j.laa.2012.06.038 — rank-3 nested-polygon theory only.
- Fiorini, Massar, Pokutta, Tiwary, de Wolf, Exponential lower bounds for polytopes / Linear vs semidefinite extended formulations, JACM 2015. https://doi.org/10.1145/2684068 — irrational pentagon 5x5 rank-3/rank-5 slack.
- Cohen and Rothblum, Nonnegative ranks, decompositions and factorizations, Linear Algebra Appl. 1993. https://doi.org/10.1016/0024-3795(93)90560-M — foundational existential bounds.
