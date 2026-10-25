# Scientific review of the two-hypersimplex cutoff

## Correctness — PASS

The key real-polytope membership equivalence follows by choosing the summand coordinates independently from intervals whose total lower and upper sums bracket the required rank sum; it remains valid at all boundary points. Integer translation gives a bijection from lattice points to signed-coordinate patterns, each counted precisely once by the bounded-composition formula. The \(n\) integer dilation counts determine the degree-\(n-1\) Ehrhart polynomial exactly by forward differences, so the \(252\)-class classification is genuinely exhaustive within the stated finite parameter range. The standalone Python code uses exact integers and rational fractions and generates a complete full-coefficient CSV; a separately implemented coordinate dynamic program checks \(503\) lattice counts. The negative coefficient for the already published \(\Delta_{3,14}+\Delta_{7,14}\) also agrees exactly with Li and St. Dizier [1]. The finite certificate does not establish properties outside ambient dimensions \(2\) through \(14\); none is claimed.

## Originality — PASS, subject to historical-priority uncertainty

Li and St. Dizier [1, Sections 3--4] exhibit one nonpositive two-hypersimplex sum in ambient dimension \(14\), the \((3,7)\) canonical representative here, and compute its negative quadratic coefficient. Their method is the closest conceptual predecessor. Their stated results do not establish minimal ambient dimension or enumerate all rank pairs at the first failure. The new result proves positivity of every two-hypersimplex sum through ambient dimension \(13\) and identifies **all five** negative-coefficient parameter classes at ambient dimension \(14\). Ferroni [2] proves positivity of individual hypersimplices, which does not control sums. Jochemko and Ravichandran [3, Theorem 4.5] prove that all integral generalized permutahedra have nonnegative linear Ehrhart coefficient, not that the higher coefficients of two-hypersimplex sums remain positive. Published-result semantic searches and historical-title comparison did not reveal this sharp dimension cutoff or full first-failure classification; absence of a result in a search is not a proof of originality. Historical priority has not been independently audited.

## Value — PASS

Recent work disproved Ehrhart positivity for a member of a canonical two-summand family. Asking for the **first** dimension in which the failure is possible and whether the initially published pair is exceptional or typical is a natural structural question. A sharp dimension cutoff and complete first-failure classification distinguish five rank configurations out of forty-nine and show that all failure occurs in the quadratic term, with no zeros. This is more informative than another arbitrary counterexample, gives a finite sharp boundary, and is reusable as a benchmark for proposed positivity constraints. A paper-sized general theorem in unbounded dimension is not claimed.

## Closest sources and limits

1. Yupeng Li and Avery St. Dizier, *Schubitopes are not Ehrhart positive*, arXiv:2608.00377, Sections 3--4; the previously published example and combinatorial counting approach.
2. Luis Ferroni, *Hypersimplices are Ehrhart Positive*, arXiv:1911.10146; positivity for each isolated hypersimplex.
3. Katharina Jochemko and Mohan Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, *Mathematika* 68 (2022), DOI:10.1112/mtk.12122, Section 4.1; linear-coefficient nonnegativity for generalized permutahedra.

The claim is restricted to ordinary coefficients for a finite, exact parameter domain; all computations and boundaries are explicitly reproducible. Equivalence under other terminology or unindexed earlier tables remains a historical-priority risk. A separate independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
