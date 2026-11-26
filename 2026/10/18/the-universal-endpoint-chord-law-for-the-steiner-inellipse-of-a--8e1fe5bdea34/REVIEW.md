# Scientific assessment of the corrected chord law

## Correctness

The closed intersection probability differs from the distinct-side conditional formula at scale one. A same-side segment hits the full ellipse exactly when it contains the side midpoint; this contributes half the same-side probability. The full law therefore has a jump of size \(\sum_i p_i^2/2\), in addition to the logarithmic approach to its left limit. The distinct-side formula follows from the reference-triangle incidence polynomial and exact piecewise integration, and its scale-one value can also be obtained by direct rational integration. Since that value exceeds \(1/2\), the shape order is strict even after accounting for same-side segments. The symbolic and numerical checker includes same-side pairs and verifies explicit straddling and nonstraddling cases; the proof supplies the universal quantifiers.

## Originality and value

The classical midpoint tangency and the associated straddling probability are not standalone originality claims. The specific ellipse conditional law and its sharp logarithmic asymptotic concern independent arclength-uniform boundary samples. Kinematic and isotropic-uniform chord models use a different measure. Centroidal inner-triangle interception laws illustrate an analogous atom with a different conditional law. The exact result shows how both Euclidean sampling weights and the affine-natural ellipse affect chord penetration, separating a cusp in the continuous part from the singular mass at the edge. Earlier unindexed equivalent calculations are not ruled out.
