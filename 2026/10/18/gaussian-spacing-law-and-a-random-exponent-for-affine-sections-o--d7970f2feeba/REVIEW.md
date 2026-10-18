# Mathematical review

## Correctness

**PASS.** The choice of motion-invariant affine hyperplane corresponds to Haar orientation and Lebesgue offset, conditioned on intersection. A rank-\(k\) cut intersects exactly \(k(m-k)\) simplex edges. Normalizing centered Gaussian samples yields the exact expected-spacing formula, including the range bias: the probability is a ratio of expectations, not an unweighted expectation of a ratio. Gaussian extreme-value bounds make that bias asymptotically negligible in total variation, after which binomial tail counts rigorously yield the random polynomial exponent. The analytical proof establishes the infinite-dimensional assertion. Independent finite simulation of Haar orientation and uniform offsets supports the integral calculation.

## Originality

**PASS relative to inspected evidence.** The closest identifiable earlier section-combinatorics article studies attainable counts, gaps and maxima, not their invariant-measure law. The closest previously published regular-simplex fluctuation result is for hyperplanes forced through the centroid and explicitly not randomly translated planes. The complete full text of De Loera–Lopez-Campos–Torres (arXiv:2412.12419) and the published-finding corpus centroidal section paper were read; their statements do not imply the Gaussian-gap probabilities or the random noncentral exponent. Dirksen's inspected section-volume article and Baryshnikov's inspected regular-simplex projection article address distinct observables. Residual risk: obscure earlier integral-geometric formulas or Gaussian-spacing results may imply the law. A historical-priority guarantee is not asserted.

## Mathematical value

**PASS.** The distinction between central and genuinely affine random slices of a high-dimensional regular simplex is geometrically natural and changes the scale of section complexity. The exact finite law gives every attainable vertex-count probability, and the nondegenerate exponent limit identifies a universal distribution inaccessible from maximum-count or central-section results alone. Both the Crofton size bias and the simultaneous Gaussian extreme/tail-count analysis are essential, rather than a variable renaming or a table lookup.

## Scope and uncertainty

The theorem is about regular simplices, oriented motion-invariant affine hyperplanes conditioned on hitting, exact finite-dimensional rank probabilities, and a logarithmic weak limit. The verification script tests only finite ranks. Directly relevant 1992 projection literature was not fully inspected and remains a priority risk, although it is about projections. No independent mathematical review has occurred.

Self-review: passed. Independent audit: not yet performed.
