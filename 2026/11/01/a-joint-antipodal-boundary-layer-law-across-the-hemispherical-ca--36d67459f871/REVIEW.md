# Scientific review

## Correctness — PASS

For each fixed integer \(q\ge3\) and real \(\lambda>-1/2\), exact signed-latitude constraints reduce near-antipodal cap pairs to an equatorial band. The normal-coordinate Jacobian has the stated leading factor \(\varepsilon^{q+1}\); the squared-distance expansion yields \(\|b\|^2+c^2<1\), while the cap conditions give the independent interval \(-\lambda\le a\le\lambda-c\). The region is compact after fixing \(\lambda\), its boundary has measure zero, and dominated convergence proves both the scalar coefficient and the full conditional joint law. The strict-event exclusion for \(\lambda\le-1/2\), exact three-dimensional polynomial and onset integral are independently checked. The accompanying standard-library verifier passed 117 deterministic checks. Numerical checks alone do not prove the limiting theorem; the proof is analytic.

## Originality — PASS, with residual historical risk

Cabré et al. (2007), Appendix B1 (doi:10.1111/j.1365-2966.2007.12280.x), give scalar angular pair-containment calculations for the ordinary \(\mathbb S^2\) cap, which is outside the claimed range \(q\ge3\). Moseeva, Tarasov and Zaporozhets (2020), Theorem 2.1 and Corollary 2.2 (arXiv:2007.07297v1), supply all-dimensional fixed subhemispherical cap *distance densities*. Those results cover the scalar marginal and, by complements, may be leveraged to calculate scalar large-cap probabilities, so that part is not separately claimed new. A scalar law does not specify the conditional joint tangent-bundle coordinates \((u,a,b,c)\) of pairs at the hemisphere transition, which is the claim's central new object. Inspected primary texts and targeted searches did not reveal that joint law. The self-review priority assessment cannot exclude uninspected sources, particularly work on boundary-layer geometry or local coarea limits.

## Mathematical value — PASS

The cap family supplies a canonical geometric-probability transition where antipodal pairs become barely possible. The joint conditional law resolves where those rare pairs lie, their signed normal offsets, their tangent displacements, and a two-boundary support transition at \(\lambda=\pm1/2\). These quantities are not determined by the known one-dimensional separation distribution and are useful for conditioning and simulation of rare spherical configurations. The exact \(\mathbb S^3\) profile and all-dimensional onset law give concrete benchmarks. This is restricted to fixed dimension and the one-parameter hemisphere scaling; an independent priority audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
