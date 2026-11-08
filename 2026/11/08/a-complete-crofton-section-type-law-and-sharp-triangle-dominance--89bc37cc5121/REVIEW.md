# Scientific review: Crofton sections of right rectangular pyramids

## Correctness — PASS
The random affine plane is sampled with motion-invariant measure before hit-conditioning, ensuring the directional width bias is included. Integrating edge crossings gives the first moment; the polyhedral mean-width identity gives the denominator. Exact offset inequalities produce the pentagonal-section integral, and the other two probabilities follow from an exact two-equation moment system. The derivative identity \(D'(h)=h\phi/L\) yields a strictly increasing expectation and the sharp global bounds. A separate edge-intersection Monte Carlo implementation agrees with the formulas at five different shapes; finite tests do not replace the symbolic proof.

## Originality — PASS, with historical risk
Kim–Yaskin–Zvavitch (2015) treat distributions of section areas, not section vertex counts. The published exact rectangular-pyramid five-vertex result is for planar **shadows** and cannot imply the stationary **affine-section** probabilities, which also have three-sided outcomes. Accessible existing section-type claims concern other bodies or central rather than translated sections. Ohser–Mücklich's 1995 stereology paper was inspectable only by abstract, so its full technical contents remain an explicit residual risk; originality is not independently certified.

## Value — PASS
The complete law across the right rectangular-pyramid family and its shape-free structural consequences resolve a natural geometric-probability statistic beyond a special-case numerical example. Strict triangle dominance, a sharp expectation interval and strict height monotonicity give testable boundaries for future stereological studies.

## Limits and closest literature
The formulas require a rectangular base, centered apex and isotropic stationary planes, and provide an exact quadrature rather than an elementary primitive. The proof is self-contained modulo the classical polyhedral mean-width identity. Compare arXiv:1512.07289v1, Ohser–Mücklich (1995) DOI:10.2307/1427832, and the published rectangular-pyramid shadow result; prior work is not claimed absent beyond inspected sources.

Self-review: passed. Independent audit: not yet performed.
