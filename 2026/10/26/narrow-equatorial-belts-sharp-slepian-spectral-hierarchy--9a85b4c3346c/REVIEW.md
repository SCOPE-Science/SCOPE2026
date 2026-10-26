# Self-review

## Correctness — PASS

The reduction of a fixed absolute azimuthal sector to a polynomial weighted Gram matrix is exact under spherical area measure. The exterior-power Cauchy–Binet argument reconstructs every spectral exponent and coefficient, and the jet quotient is precisely the endpoint Christoffel kernel for the shifted Jacobi weight. All normalizations, the special case \(L=0\), the unique maximum exponent, and the global condition-number constant were checked. The supplied standard-library program passed 832 exact-rational finite consistency assertions. The finite tests are corroboration, not a proof of universal quantifiers.

## Originality — PASS, qualified

The closest full text is Simons–Dahlen, arXiv:math/0603271: it treats the same equatorial belt and complementary double cap, but its actual statements concern commuting matrices, finite-band numerical eigenvalues and geodetic inverse estimation, not the full fixed-band thin-belt asymptotic with exact Jacobi endpoint coefficients. Simons–Dahlen–Wieczorek, arXiv:math/0408424, develops general Slepian concentration and polar caps, with a high-bandwidth/shrinking-cap regime different from this fixed-bandwidth belt. Bates–Khalid–Kennedy, arXiv:1608.05479, addresses numerical algorithms for arbitrary regions. The 2021 Roddy–McEwen wavelet paper, arXiv:2106.02023, has a verified public date and motivates regional decomposition, but only its abstract and partial introductory excerpt were accessible: this leaves a genuine priority uncertainty. Relevant published hemisphere spectral results involve nonshrinking half-spheres and do not imply the new scale constants.

## Value — PASS

For satellite/sky data observed in a progressively narrower belt, the result quantifies the complete hierarchy of information loss in every azimuthal order, not just a trace or a largest eigenvalue. In particular the exact least-mode constant and \(\varepsilon^{-2L}\) condition-number law are directly pertinent to stable reconstruction and regularization. Its full arbitrary-fixed-\(L\) classification and factorial endpoint constants are substantial beyond evaluating a small finite matrix.

## Limits and risk

There is no uniform-in-\(L\) claim, no finite-width exact diagonalization, and no independent audit. Older spherical Slepian material is rich, so concealed historical priority remains possible, especially in the inaccessible full 2021 source. All assumptions and claim boundaries appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
