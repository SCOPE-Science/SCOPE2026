# Review of Optimality of equal bisection in the large-negative-\(\gamma\) Poincaré recurrence

## Correctness
PASS. The proof starts from the source definitions of \(\mathcal F(h)\) and \(M(h)\). On the full-step exceedance set, \(\mathcal F(h)\) is exactly the integral of \(|\Delta_hg|^p-|h|^{p+\gamma}\). Retaining this subtracted term changes the source's bisection threshold coefficient from \(2^{-\gamma}\) to \(2^{-\gamma}-1\). For arbitrary finite proportional partitions, weighted convexity gives the exact coefficient \(\sum_i t_i^{\gamma+1}-1\), and strict convexity plus Jensen's inequality proves the unique global minimizer. The argument covers all \(p\in[1,\infty)\) and \(\gamma<-p\) in the claim.

## Originality
PASS. The focal 2026 paper was inspected through its introduction, Section 4, and Section 5.1. It states the weaker Lemma 4.4 coefficient and iterates equal bisection, but does not state either the retained-threshold coefficient or optimality among finite proportional subdivisions. The motivating 2025 Nguyen article was inspected in its nonlocal-inequality section and does not contain this recurrence optimization. Targeted source, alias, parameter, and implication searches did not locate a stronger covering statement. Residual risk remains that the short coefficient argument could occur implicitly in older inequality literature under different terminology.

## Value
PASS. The focal paper explicitly exposes a parameter-dependence gap: its global construction is exponential in \(|\gamma|\), while its lower bound for the least constant is only linear. The result identifies an exact bottleneck inside the paper's large-negative-parameter mechanism and proves that no finite retuning of proportional subdivision lengths can remove the exponential threshold loss. This is a structural method boundary, not merely a cosmetic subtraction of one from a coefficient.

## Closest literature and limitations
The closest source is arXiv:2610.04259v1 itself: Lemma 4.4 gives the bisection recurrence, Theorem 4.1 gives the resulting exponential global bound, and Proposition 5.1 gives the linear lower bound. The 2025 Nguyen article supplies the motivating family and open Poincaré problem but not the Section 4 recurrence. The result does not determine the true global asymptotic dependence on \(\gamma\), and it does not rule out fundamentally different proof mechanisms.

Same-model review: passed. Independent audit: not yet performed.
