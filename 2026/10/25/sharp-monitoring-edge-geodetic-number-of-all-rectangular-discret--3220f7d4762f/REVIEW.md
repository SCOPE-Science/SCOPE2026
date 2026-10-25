# Scientific review: rectangular torus edge monitoring

## Correctness — PASS
The claim is quantified for integers \(5\le m\le n\) and uses ordinary Cartesian products of unweighted cycles. A proof of the cycle-gap criterion and the exact factor-section monitoring criterion gives the lower bound \(3n\). A uniform balanced-floor construction certifies this bound except at the two parameter pairs \((5,6)\) and \((7,8)\), where explicit matrices do. The key estimate for cyclic row gaps is \(\lceil((\lceil m/3\rceil-1)n)/m\rceil+1\le\lfloor(n-1)/2\rfloor\) outside those exceptions. Its base cases and two-step induction are supplied in RESULT.md. The standalone verifier tests the original edge-deletion metric rather than only the reduced gap certificate. The universal result is established by proof, not numerical extrapolation.

## Originality — PASS, with residual risk
Haslegrave (arXiv:2210.08955), Theorem 4, proves the **square** discrete-torus equality only. His Theorem 1 gives product bounds that do not determine the values for unequal dimensions. The new result closes those bounds for every unequal rectangle, with a nontrivial balanced placement and two exceptional templates. Relevant cycle/grid sections of Dev et al. (2025) do not state this general equality. Search-based comparisons did not identify a dominating general result. The full article by Xu et al. (2024) could not be inspected; its accessible abstract names different graph products. Unindexed equivalent priority is not ruled out.

## Value — PASS
For every pair of cycle lengths at least five, the result now gives an exact optimal number of edge-failure observation vertices on a rectangular periodic grid. Unlike the prior square case, it handles arbitrary aspect ratio and shows that the lower Cartesian-product bound is always sharp here. The explicit placements can be checked in linear time in the graph size and expose two tight small-dimensional obstructions to a natural floor-sampling construction.

## Limitations and literature
This does not classify all optimal observation sets, analyze graph products with short cycles, or settle strong-product monitoring. Same mathematical model proof inspection and finite computations are not independent validation. Closest literature: J. Haslegrave, arXiv:2210.08955 (especially Theorems 1 and 4); S. R. Dev et al., DOI 10.1016/j.dam.2025.08.041; X. Xu et al., DOI 10.1080/17445760.2024.2301929 (abstract only).

Self-review: passed. Independent audit: not yet performed.
