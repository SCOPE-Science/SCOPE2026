# Review

## Correctness
**PASS.** The unit-edge coordinate model gives the exact height
\[
h=\frac{\sqrt{4\cos^2 a-1}}{2\cos a}.
\]
At one upper vertex, direct facet cross products give one base normal and three side normals with two scalar parameters \(\gamma,\zeta\). The identity
\[
\zeta H=\gamma\sin a
\]
reduces the X-ray condition for the line of azimuth \(\phi\) to the single circular inequality
\[
\operatorname{dist}_{S^1}(\phi,\theta)<\frac{\pi}{2}-a.
\]
The lower-ring condition is the same after subtracting \(\pi\) from its azimuth. Three azimuths separated by \(2\pi/3\) cover the circle whenever \(n>3\), and the endpoint case \(n=3\) misses no transformed vertex azimuth. Gauss-image inclusion passes vertex coverage to every face. The universal lower bound then gives equality. The packaged checker independently verifies all analytic identities and every vertex certificate for \(3\le n\le200\).

## Originality
**PASS, with an unindexed-classical-observation residual risk.** The closest primary X-ray paper was inspected in full. It proves the dimension-minimal value for almost smooth bodies and gives the Gauss-image characterization used here, but contains no “antiprism” occurrence. The uniform antiprism family is not almost smooth, so the source theorem does not imply the result. Candidate-specific searches under regular/uniform antiprism, X-ray number, illumination, Gauss images, and three-direction formulations found no covering statement. The known regular-octahedron case is treated as the \(n=3\) component of the family rather than as new.

## Value
**PASS.** Uniform antiprisms are one of the two canonical infinite families of convex uniform polyhedra. Determining their X-ray number for all \(n\) is therefore a natural family-level classification. The result is structurally stronger than a list of low-\(n\) computations: the same three azimuths work in every case, only their common slope changes, and the proof explains this through an exact normal-cone arc criterion. The family also lies entirely outside the standard almost-smooth sufficient class.

Same-model review: passed. Independent audit: not yet performed.
