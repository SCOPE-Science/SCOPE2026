# Scientific review: marked acute-triangle limit for collapsing rectangles

## Correctness — PASS

The claim fixes a nondegenerate interior-uniform sample for each positive rectangle height and orders the vertices by horizontal coordinate. The exact three dot-product inequalities are reconstructed in RESULT.md. The transformation from horizontal gaps to a signed logarithmic exponent and their product has Jacobian \(h^2\log(1/h)\), and the two limiting product-gap intervals are calculated separately. Dominated convergence proves interior marked convergence, while the integral \(6h^2(1+2\delta\log(1/h))\) controls all omitted logarithmic endpoint scales. Exact fourth-degree polynomial integration gives mass one and the claimed marginal independence. The probabilistic limit is analytic, not an extrapolation from finite tests; the standalone verifier independently checks rational constants and finite-height formulas.

## Originality — PASS, with specified source-access risk

Langford (1969) already derives the scalar probability of obtuse triangles from uniform **interior** points of rectangles of every positive aspect ratio. Thus the current result does **not** claim to invent that probability or its scalar asymptotic. Its actual claim is a four-variable conditional weak limit after resolving the two different horizontal gaps into logarithmic scales; a scalar function of aspect ratio cannot determine this joint spatial law. Khan (2017/2019, full arXiv manuscript inspected) supplies extremal properties and smallness bounds for long-thin convex domains, not a marked localization theorem. Beck (2025/2026, publicly readable introduction, distribution formulas and full-text sections inspected) treats the scalar obtusity probability for a three-dimensional cube, not conditional gap scales for collapsing planar rectangles. Claim-level Indexed literature and accessible prior-record searches included conditional distributions, signed/logarithmic horizontal gaps, Langford-equivalent formulations, and two-sided scaling; no published covering marked limit was identified. A previous arclength-**boundary** rectangle triangle theorem concerns a different sampling space and is not logically equivalent.

The 1969 Langford full paper and its 1970 expanded account were not available for full-text comparison. Their scalar claims are known and fully credited; whether they also contain an unindexed marked joint statement remains a historical-priority risk. The unavailable full text is not represented as having been inspected.

## Mathematical value — PASS

The theorem explains the unusual logarithmic probability scale through two continuously varying rare-event gap mechanisms, identifies a uniform logarithmic location law, and proves an independent, nonuniform degree-four vertical-location law. These are structural and experimentally testable features of the geometry of conditioned acute triangles. They provide information unavailable from the known unmarked probability alone. The statement does not simply rename a scalar special case or append routine finite digits. The result is limited to one collapsing rectangular family and does not imply a universal theorem for arbitrary convex bodies.

## Remaining limitations

No explicit finite-height error estimate is established. The conditional limit is for interior points, not points sampled from the boundary. Existing unmarked formulas and related thin-body estimates are not claimed as new. The earlier Langford source was not readable in full; priority may require further specialist literature review. No external independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
