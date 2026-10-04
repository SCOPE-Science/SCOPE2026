# Same-model review

## Correctness
PASS. The generator tested against arbitrary functions of \(z\) gives
\[
\mathbb E[dxy-mz\mid z]=0.
\]
The exact polynomial identities
\[
L(z^2)=2dxyz-2mz^2
\]
and
\[
L(x^2)=2xy-2ax^2+2bxyz
\]
then give
\[
\mathbb E\!\left[\left(z+\frac1{2b}\right)^2\right]
=
\frac1{4b^2}+\frac{ad}{bm}\mathbb E[x^2].
\]
The equality case is rigid: a complete compact trajectory with \(x\equiv0\) has \(\dot z=-mz\), hence \(z\equiv0\), and then \(y\equiv0\). Strictness immediately excludes confinement to \(-1/b\le z\le0\). The packaged exact checker reproduces the combined polynomial certificate.

Risk: the equality proof uses the standard invariance of the support of an invariant probability measure for a continuous flow.

## Originality
PASS. The original inspected abstract emphasizes multi-scroll generation, phase portraits, Poincaré maps, bifurcation diagrams, and Lyapunov exponents. The later same-object analytical abstract concerns control, synchronization, and hyperchaotification. Targeted searches under Dadras and Dadras–Momeni aliases found no same-object invariant-measure, conditional-moment, completed-square, or slab-obstruction theorem. Closest semantic records concern different polynomial vector fields and do not imply this statement.

Risk: the complete 2009 and 2015 articles were not accessible in this inspection, so they remain explicit residual bibliographic risks. Search also cannot exclude differently phrased or unindexed earlier results.

## Value
PASS. The result gives a universal recurrence constraint for every compact invariant statistical state of a published multi-scroll flow, rather than a property of one numerically sampled attractor. The slab is mathematically intrinsic because its endpoints are the roots of the quadratic height term in the exact balance, and equality is completely classified. The conclusion is therefore a structural global obstruction rather than a routine numerical or normalization check.

Same-model review: passed. Independent audit: not yet performed.
