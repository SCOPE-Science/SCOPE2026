# Scientific review

## Correctness
**PASS.** The exact weighted hard-core packing maximum follows from minimum separation on each half-axis and a strict comparison when the central symbol is zero. Weighted distance to a constant center is affine in the occupied weight, giving the explicit minimax radius. For an arbitrary real-valued ambient center, coordinatewise Cesàro averaging approaches a constant configuration in the weighted metric. Convexity of maximum distance forces arbitrarily late finite windows with a strict discrepancy; the Markov renewal mechanism gives uniformly positive conditional probability to reproduce each prescribed admissible word after a finite all-zero reset. Conditional avoidance decays geometrically, proving the zero-measure statement. At the critical radius a constant center captures the entire support. The included exact rational dynamic-programming verifier passes 504 finite assertions; no infinite statement depends on enumeration.

## Originality
**PASS under accessible evidence, with bibliographic risk.** The motivating Hilbert-cube paper [1] demonstrates Lebesgue-product expansivity and topological genericity; it does not state this singular, dependent Markov-family radius. The published concentration characterization [3] was inspected in full: it assumes independent coordinate laws, uses product factorization, and does not cover Markov dependence or exact constrained support packing. Foundational measure-expansivity sources supply definitions and qualitative consequences, not the exact weighted minmax values. A broader prior-art equivalence or uninspected sections of the motivating paper remain possible; a search is not an exhaustive novelty guarantee.

## Value
**PASS.** Quantitative measure expansivity of a non-expansive infinite-dimensional shift becomes sensitive to dynamical constraints: requiring two rather than one zeros between ones lowers the sharp radius from \(3/2\) to \(9/7\), and the radius tends to \(1\) with spacing. The full-support Markov law is dependent and singular relative to Hilbert-cube product Lebesgue measure. The parameter-independent exact threshold is a natural invariant of this specifically normalized symbolic-support problem, with a proof mechanism different from independent marginal concentration.

## Literature and limitations
[1] G. Lacerda, *Typical expansive measures for infinite-dimensional maps*, arXiv:2610.09482v1, 2026-10-07, https://arxiv.org/abs/2610.09482. Read accessible abstract and Hilbert-cube theorem/proof portion; entire later manuscript unavailable for full comparison.

[2] C. A. Morales, *Measure-expansive systems*, arXiv:2503.16757, https://arxiv.org/abs/2503.16757. Abstract-level comparison only.

[3] *A concentration criterion and Baire dichotomy for product measures on the Hilbert-cube shift*, publicly available research note at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-concentration-criterion-and-baire-dichotomy-for-product-measur--a21666c938a0. Complete RESULT.md proof examined, including independence scope, factorization and limitations.

The theorem does not cover one-sided balls, arbitrary dependent processes or different product-metric weights. Equivalent general packing or symbolic measure-expansivity specializations may have escaped the literature comparison.

Self-review: passed. Independent audit: not yet performed.
