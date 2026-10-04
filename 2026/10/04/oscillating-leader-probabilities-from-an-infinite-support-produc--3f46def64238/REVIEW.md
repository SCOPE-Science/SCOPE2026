# Same-model review

## Correctness
PASS. The proof uses an explicit tail recursion. At the peak subsequence, the probability of no observation above the target level tends to \(e^{-1}\), the target atom produces far more than \(\sqrt n\) tied maxima, and two independent maximizing-index sets intersect with asymptotic conditional probability one. At the trough subsequence, the target level is the maximum with probability tending to one but its common-index probability is bounded by a term tending to zero. These are analytic bounds for the full subsequences, not finite extrapolations.

## Originality
PASS. The closest source, DOI 10.3390/math10101623, proves \(a_n\to0\) for certain regular discrete marginals and poses the arbitrary infinite-support product question; the inspected text contains no oscillating example. The same-author follow-up addresses dependent quasi-unidimensional vectors, and arXiv:2112.15534 concerns Pareto maximality rather than a global leader. Targeted semantic searches for equivalent common-maximizer and maximum-tie formulations found no covering statement. A prior structural maximum-tie criterion does not contain the present law or its peak/trough analysis.

## Value
PASS. The example shows that the source's regularity-based convergence theorem cannot be extended to all infinite-support product laws. The positive limsup and zero liminf expose an oscillatory obstruction that any proof of the weaker no-leader conjecture must accommodate.

## Closest literature and limitations
The finding is closest to Răducan et al. (2022), especially their Conjecture 2 and Proposition 4. It does not solve Conjecture 2 because the constructed law has zero liminf; it instead proves that the stronger convergence claim fails. The exact positive limsup is not determined.

Same-model review: passed. Independent audit: not yet performed.
