# Scientific review: Gaussian fixed-time mixing hierarchy near half swaps

## Correctness

PASS. The exact exchange transition is the difference of two independent hypergeometric draws, with conditional expectation \(n/2+\lambda(x-n/2)\) and conditional variance \(2k(n-k)x(n-x)/[n^2(n-1)]\). Their moment recursions prove that after one step the state is near the centre on the scale \(n\), uniformly over initial states. A uniform lattice local central limit theorem, proved by Stirling's expansion in the result, then gives the centred Gaussian law on each later step. The residual random shift of the Gaussian centre is \(O_{L^1}(|\lambda|\sqrt n)=o(\sqrt n)\). The exact overlap formula for two normal densities yields the full worst-state total-variation profile. The finite checker was run against the actual standalone code; its 5,325 assertions passed. These computations are auxiliary and do not replace the analytical limit argument.

## Originality

PASS, subject to historical-priority uncertainty. The comparison concerns implications, not just labels: Theorem 5 in Nestoridi–White (arXiv:1606.01437v2, Section 4.1) supplies vanishing spectral total-variation bounds for at least three half-urn steps, not two, and only treats exchange sizes extremely close to half (at most logarithmically far in its extension). Griffin et al. (arXiv:2308.08676v1, Assumption 4.1 and Theorem 4.2) prove bounded mixing with a two-step lower bound under a first-eigenvalue restriction, without an exact fixed-time profile. Alameda et al. (arXiv:2203.08647v1, Theorem 1.2) assume the exchange fraction tends to a number strictly below one half. The new result proves an entire family of critical windows, including the previously unresolved two-step endpoint. Known spectral descriptions could in principle be used to derive this formula, and non-indexed or later work might cover it; independent priority certification has not been undertaken.

## Value

PASS. The source literature leaves the nearly-half-exchange regime at bounded mixing time and a half-swap three-step guarantee. Identifying a sharp, uniform fixed-time Gaussian total-variation profile resolves the two-step boundary and reveals a hierarchy of distinct, natural critical scales \(n^{1-1/(2t)}\) for every fixed \(t\ge2\). This is stronger than a mixing order estimate and expresses quantitative sensitivity to the exchange rate at finite times, useful for Bernoulli–Laplace interchange and card-shuffle models.

## Limits and source comparisons

The result requires equal urn sizes and colour totals, fixed step count, and an exchange fraction tending to one half. The proof does not address growing step counts or the exact mixing-time tie case when the limiting profile equals the requested tolerance. The primary 2016, 2022 and 2023 analyses were checked in their actual source texts in the statements, hypotheses and nearby proofs relevant to the claim; the remaining historical-priority risk is not a correctness defect.

Self-review: passed. Independent audit: not yet performed.
