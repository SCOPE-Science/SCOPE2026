# Independent mathematical audit

## correctness

PASS

For every nonempty proper row subset of F_10, published ACM/Achanta results require uniform distribution modulo divisors and preserve full spark under affine units/translations and complement. Independently enumerating uniformly distributed subsets of sizes 1,...,5 found counts 10,20,60,30,20 and the exact affine representatives {0};{0,1};{0,1,2},{0,1,3};{0,1,2,3},{0,1,3,4};{0,1,2,3,4}. Consecutive reps are Vandermonde full spark. For {0,1,3} every 3-column determinant is Vandermonde times x1+x2+x3: three tenth roots cannot sum to zero because primitive cube-root ratios are not tenth roots. The 4-row exceptional representative has a singular minor on columns {0,1,2,6}; independently reduced that determinant to zero modulo Phi_10(z). Ten affine images are bad in size 4, and complements give ten bad in size 6. Full finite domain covered without floating-point zero tests; remaining adjacent sizes 1,2,3,5 and complements full spark.

## originality

PASS

Alexeev--Cahill--Mixon Theorem 9 supplies uniformity necessity, invariances and the exact N=10 exceptional singular minor, but not the complete classification of EVERY uniform row set at N=10. Achanta et al give coprime/single-missing-row criteria and revisit the same counterexample, yet do not enumerate or classify all affine row orbits at N=10. The finite exhaustive orbit theorem is an additional natural exact classification, although much of its ingredients are published; no dominating exact table was located.

## value

PASS

DFT order 10 is the canonical first composite order where the uniform-distribution condition is insufficient. Classifying all full-spark row selections and exactly two exceptional affine/complement orbits is a complete, useful finite frame-design invariant rather than an unmotivated isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
