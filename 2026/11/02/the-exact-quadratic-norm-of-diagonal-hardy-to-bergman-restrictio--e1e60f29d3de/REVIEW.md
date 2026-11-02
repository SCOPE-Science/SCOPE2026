# Scientific review: exact quadratic diagonal restriction norm

## Correctness — PASS

The two-space norms reduce exactly to normalized point evaluation on analytic quadratics: \(\|DF\|_{A^1}=|P(1)|/2\) and \(\|F\|_{H^1}=\int_{\mathbb T}|P|dm\). Phase normalization, coefficient conjugation and reversal preserve point evaluation and norm, and convex averaging reduces all complex triples to real palindromic triples. The resulting one-variable integral is convex on the full real line; its derivative has a unique zero determined by \(\tau=\cos\tau\). The exact integral at the minimum equals \(2\tau/\pi\), giving the claimed norm without numerical premises. The standard-library checker passes the scalar/circular evaluations, but is supplementary only.

## Originality — PASS under available comparative evidence

Brevig et al. (arXiv:2610.16227v1, sections 1 and 4) prove contractivity for \(p\ge2\), and show the \(p=1\) linear test ratio \(\pi/3\), not the exact homogeneous quadratic restricted norm. Arestov (1980, pp. 539–542 inspected) studies general inequalities and a sharp geometric-mean endpoint rather than this degree-one trigonometric \(L^1\)-evaluation constant. Doktorski (2020, sections 1, 3, 4) treats order-type Nikolskii inequalities, not the exact scalar root. No matching claim was found in the recorded semantically overlapping database queries. These comparisons do not prove absolute uniqueness: equivalent classical trigonometric norm calculations remain a residual risk.

## Value — PASS

The smallest homogeneous diagonal section not captured by the known linear benchmark is a natural finite-dimensional test of the unresolved \(p<2\) diagonal restriction norm. Its complete, all-complex-coefficient sharp constant supplies a new explicit quantitative lower bound on that full norm, and the optimizer exhibits a genuinely mixed quadratic profile. The precise threshold is mathematically motivated by this finite-section extremal problem, not an arbitrary coefficient slice.

## Scope and residual risk

The full \(H^1\)-to-\(A^1\) operator norm remains unknown. Classical trigonometric polynomial degree-one evaluation results not located by the present searches could implicitly subsume the formula. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
