# Scientific review

## Correctness: PASS

The claim covers the uniform independent-parent recursive tree, \(n\ge2\) for the covariance and \(n\ge3\) for normalized leaf fluctuations. The path-length centered martingale has square-summable increments from logarithmic depth second moments and therefore converges almost surely and in \(L^2\); its positive variance is inherited from the nonconstant third-step term. The closed leaf-depth mean \(\mathbb EA_n=nH_n/2-n/4\) produces the exact covariance decrement \(-1/4\) by total covariance, and the base case is zero. The Eulerian leaf-count recurrence gives a sum of bounded 1-dependent descent indicators and hence a Gaussian CLT. A finite-label split makes the late-label leaf count independent of each fixed initial history; an \(L^1\) approximation proves the stated mixing limit against every fixed bounded full-history observable. The supplementary checker passed 2,530 exact rational assertions. The infinite proof does not rely on enumeration.

## Originality: PASS, qualified

Full accessible source text for Gałązka–Wdowicka (arXiv:2610.00614), Bryc–Minda–Sethuraman (arXiv:0809.4741), and Lundblad–Wagner (DOI 10.4230/LIPIcs.AofA.2026.2) was compared by implication. The first treats total-path-length fluctuations, the second the marginal leaf process, and the third leaf depth versus all-vertex depth using a multivariate generating function; none states the normal/non-Gaussian mixing assertion. Published records 2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f and 2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba were read beyond their titles: one covers root degree with leaves and the other root attachments with total depth, neither the leaf-count/total-depth pair. Accessible own historical claims were screened for overlapping objects and limiting assertions. The 1999 Dobrow–Fill article's abstract was accessible but its full text was not; it remains a priority risk. The explicit covariance is algebraically obtainable from general multivariate enumerators, so its numeric value is not claimed to have priority independently of the accompanying mixing limit. Search nonmatches are not proofs of uniqueness.

## Mathematical value: PASS

Leaf abundance and total pointer-tracing cost are simultaneously natural diagnostics of a growing recursive tree, but their intrinsic fluctuations live on different scales. The exact negative covariance quantifies their finite-size dependence. Mixing relative to the entire input history gives a much stronger separation than zero limiting correlation: every fixed event determined by the complete growth process is asymptotically uninformative about the standardized leaf count. The result connects an active total-depth martingale research direction to classical Eulerian leaf fluctuations and exhibits how non-Gaussian global shape randomness can coexist with asymptotically fresh Gaussian local-count randomness. This is not a mere restatement of either marginal CLT or martingale convergence. It does not extend to arbitrary weighted attachment, and quantitative mixing rates remain open.

## Risks and scope

The full text of Dobrow–Fill (1999) was not available; a historically unindexed joint functional limit theorem or a stronger general theorem might imply this claim. The 2026 multivariate tree enumerator encodes finite mixed moments implicitly and may subsume the exact covariance component. No claim is made for weighted trees, finite-size independence, or Gaussianity of the path-length limit.

Self-review: passed. Independent audit: not yet performed.
