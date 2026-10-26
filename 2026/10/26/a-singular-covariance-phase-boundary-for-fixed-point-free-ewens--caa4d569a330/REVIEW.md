# Scientific review

## Correctness

**PASS.** The Ewens conditioning and normalization are explicitly defined. Marking distinct cycles yields the exact covariance determinant, including the boundary \(n=a+b\). The singularity-transfer expansion gives the second-order universal constant by cancellation of the lower-order terms. For \(\theta=1\), the integral remainder proves a geometric bound on shifted tails; that bound strictly dominates the quadratic error of the determinant for \(N\ge2\), while \(N=0,1\) are checked directly. A standalone exact checker executed successfully with 4,883 assertions including complete enumeration for up to eight labels. The infinite-domain conclusions rely on the proofs, not the census.

## Originality

**PASS, with priority risk.** Da Silva, Jamshidpey and Tavaré (2020, arXiv:2006.04840v1, Equation (6)) explicitly publish the factorial moments and hence an exact formula from which the covariance can be formed. That important coverage is acknowledged, and the exact moment identity is not claimed new. Their inspected treatment stops at the asymptotic independent-Poisson conclusion for the small cycles, without the universal \(n^{-2}\) constant or the finite-size alternating and factorial critical covariance law. Tavaré (2021, Section 7.2.2) treats the Ewens derangement process, but not these additional quantitative dependence classifications in the inspected section. The random-Latin-square cycle article of Cavenagh, Greenhill and Wanless (2008) concerns another measure; only its accessible abstract was inspected. An unnoticed earlier exploitation of the full moment formula or a broad conditioning theorem could supersede this contribution.

## Value

**PASS.** The theorem gives a complete phase boundary in a natural family of cycle-count dependence questions, not merely a re-expression of known means: the leading conditional covariance for all distinct fixed cycle lengths has a shared coefficient and changes sign at \(\theta=1\), while at the boundary every finite sample alternates between strict positive and negative dependence and its magnitude drops from a polynomial to a factorial scale. This distinguishes exact independence of distinct short-cycle counts in unconditioned uniform permutations from the exceptionally small but never-zero covariance after excluding fixed points. Quantitative covariance terms are useful in finite-size Poisson approximation and second-order analysis of conditioned assemblies. No parameter-uniform crossover, diagonal classification, or independent validation is claimed.

## Sources and limitations

Primary text inspected: da Silva, Jamshidpey and Tavaré, arXiv:2006.04840 (Introduction, Section 2, Section 4.3, Discussion, Appendix); Tavaré, doi:10.1112/blms.12537 (Section 7.2.2); Cavenagh, Greenhill and Wanless, doi:10.1002/rsa.20216 (abstract only). Classical coefficient transfer is used as an analytical tool. Historical priority is not guaranteed by database searches. The theorem fixes \(\theta,a,b\) in its asymptotics and requires \(a\ne b\).

Self-review: passed. Independent audit: not yet performed.
