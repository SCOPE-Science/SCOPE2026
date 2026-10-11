# Independent mathematical audit

## correctness

PASS

For SM3-I, an off-target poisoning support hits every cover set containing target \(i\) iff every corresponding accumulator receives the increment \(M^2\); after the target-only gradient, each such accumulator is exactly \(M^2+\delta^2\). For SM3-II, the first-round local statistics are \(M^2\) on the activated support and zero elsewhere, so the same hitting condition makes every target-cover accumulator exactly \(M^2\); the second round again gives \(M^2+\delta^2\). If any target-cover set is missed, its accumulator stays zero, proving sharpness of the transversal number. A fresh independent matrix replay reproduced target statistic 53 for \(M=7,\delta=2\). The row-column and codimension-one tensor covers have transversal number two under the stated nondegeneracy conditions.

## originality

PASS

The defining SM3 paper introduces arbitrary covers, proves that SM3 statistics upper-bound coordinatewise accumulated squares, recommends row-column and codimension-one tensor covers, and explicitly says worst-case behavior can be worse than AdaGrad while arguing informally that compatible activation patterns should perform well. It does not formulate a hitting/transversal invariant, the exact minimum off-target poisoning support, the universal value two for the standard matrix/tensor covers, or the exact attenuation factor. Current published-finding search found no same-result theorem.

## value

PASS

The result isolates an exact combinatorial cost of compressing per-coordinate adaptive history and gives sharp two-spike witnesses for the standard covers used by the algorithm. It quantitatively explains when an untouched coordinate can have its first update arbitrarily suppressed, which is a motivated optimizer-structure question rather than an arbitrary adversarial sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
