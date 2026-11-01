# Mathematical review

## Correctness

**PASS.** The statement fixes the Laplacian normalization, time/space measures, Hermite normalization, complex coefficient domains, and precise local asymptotics. The lens identity has Jacobian factor one-half. Five exact Gaussian moments yield the entire two-mode norm; its monotone derivative gives the sharp maximum and global fourth-order deficit. Exact additional Gaussian moments and constant temporal Fourier coefficients give the unique three-mode quartic square and the nonzero sextic coefficient. The package checker reproduces these identities symbolically, and separate numerical quadrature confirmed selected small-parameter values. The finite symbolic calculation proves these finite-dimensional identities, not an infinite odd-data theorem.

## Originality

**PASS relative to inspected primary results and indexed mathematical records, with explicit residual risk.** Gonçalves's 2017 general Hermite representation supplies the method but neither states the optimized two-mode polynomial nor the uniquely cancelled fourth-order/positive sixth-order normal form. Gonçalves and Zagier's 2021 parity-specific result is for the different \(L^6\) Strichartz norm; their discussion of the mixed \(L_t^8L_x^4\) operator leaves a parity question open. Suzuki's October 22, 2026 theorem is for even data. Gonçalves–Negro–Oliveira e Silva's September 2026 paper studies Gaussian-centered stability, not this odd family. Targeted mathematical-record searches returned no equivalent coefficients. The general 2017 identity could be taken as implicitly containing them after explicit computation, and incompletely indexed finite-band calculations may exist. No claim of global uniqueness in all literature is made.

## Value

**PASS.** The first two odd Hermite functions are the canonical lowest spectral truncation of a parity-constrained sharp mixed Strichartz problem whose full sharp constant remains unsettled. The exact sharp stability profile is a natural test case for the odd Gaussian-derivative candidate. The additional calculation explains why its quadratic loss vanishes along a dilation tangent, identifies the unique second-order Hermite correction, and quantifies the first unavoidable sixth-order loss in that three-mode model. The calculation is a finite truncation result with a concrete connection to a motivating open spectral question, not a claim of global parity sharpness.

## Closest sources and limitations

Primary full-text comparisons: Suzuki, arXiv:2610.31543v1; Gonçalves–Negro–Oliveira e Silva, arXiv:2609.11644v1; Gonçalves–Zagier, DOI 10.4171/RMI/1322; Gonçalves, arXiv:1702.08510. The general Hermite identity and the finite scope limit originality and interpretation. The local sixth-order result addresses only the explicitly normalized curve and no global three-mode extremizer classification. The review was performed on the presented claim and code, without independent validation.

Self-review: passed. Independent audit: not yet performed.
