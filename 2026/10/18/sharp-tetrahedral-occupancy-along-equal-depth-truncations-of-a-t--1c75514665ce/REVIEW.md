# Scientific assessment: sharp tetrahedral occupancy under equal-depth truncation

## Correctness — PASS

An unrestricted contained tetrahedron may be pushed vertex by vertex to an extremal quadruple without reducing its absolute determinant. The twelve directed-edge vertices therefore yield an exact and exhaustive \(\binom{12}{4}=495\)-case finite optimization. The standalone integer-polynomial checker enumerates those cases and reproduces all ten determinant classes, their counts, and the unique dominant polynomial. A concrete tetrahedron attains the dominant value. The body-volume factor \(1-4t^3\), polynomial gap factorizations and derivative sign give the universal ratio and unique minimizer on the complete interval. A rational root bracket and decimal values are diagnostic, not infinite proofs.

## Originality — PASS with priority risk

The closest full-text comparisons are Jiao–Torquato, arXiv:1107.2300, a packing-density study of the equal-edge truncated tetrahedron, and Di Summa–Eisenbrand–Faenza–Moldenhauer, arXiv:1406.3512, a general maximum-volume-simplex algorithm and hardness study. Neither inspected paper states or entails the sharp one-parameter \(\frac{(1-t)(1-3t+3t^2)}{1-4t^3}\) occupancy law or its unique quartic minimum. Beck, arXiv:2412.07952, studies expected random simplex volume; only its abstract was available, so whole-document noncoverage is not inferred from it. An older equivalent result under affine truncation or determinant terminology may exist and cannot be excluded by search alone.

## Value — PASS

The first nontrivial regular truncation family interpolates continuously from a tetrahedron through the Archimedean truncated tetrahedron to the octahedron. Determining its optimal simplex approximation fraction for every depth is a natural geometric invariant. The surprising strict interior minimum shows the octahedral endpoint is *not* the least efficiently approximated shape, a structural fact not implied by the familiar endpoint volumes. An exact all-parameter formula, sharp witness, symbolic census and global minimizer supply a useful reproducible benchmark rather than an arbitrary isolated calculation.

## Limits

The theorem treats common affine truncation depths in dimension three only. The 24-element statement concerns vertex-supported maximizers and does not classify all continuously moving equality configurations. Full-text access limitations and undiscovered older equivalences remain risks.

Self-review: passed. Independent audit: not yet performed.
