# Independent mathematical audit

## correctness

PASS

Reconstructed the transform in interface-centered coordinates. For k=sqrt(s/D), boundedness on the right gives u'(b+)=-k u(b+), and continuity of flux and the backward jump law give u'(b-)=-k u(b+) and u(b-)=(1+Dk/kappa)u(b+). Propagating the left solution back to 0 gives 1=u(b+)[(1+Dk/kappa)cosh(kb)+sinh(kb)]. Propagating right to L and simplifying gives exactly the stated Laplace transform. Under global resets, each independent trial has success probability phi(r)>0 and mean duration (1-phi(r))/r, yielding the normalized F after renewal. For convexity, write the transparent term as integral_0^1 e^(u z)/z du; the second derivative of each e^(a z)/z is e^(a z)[(a z-1)^2+1]/z^3, positive for all real a. This also applies to the two resistance terms. Both endpoint limits are infinity, so the stationary root is unique and interior. Differentiation gives F_B=-2 eta exp((1-2B)z) and F_zB=(1-2B)F_B; implicit differentiation and the positive curvature give the exact signed slope, while the envelope derivative gives strict decrease of the minimized mean. The monotone rate conversion preserves the unique maximum exactly at B=1/2. The proof requires finite positive permeability and resets from both sides as claimed. The recorded finite sweep was not rerun and is not used to establish the universal quantifier.

## originality

PASS

The unreset transform and Poisson renewal identity are prior ingredients. The distinct supported claim is the geometry of the globally reset MFPT optimizer: unique interior rate for each position, increasing then decreasing with its unique position maximum at the midpoint, notwithstanding a strictly decreasing optimized mean. The closest inspected first-passage optimization screens out target-side resets and therefore uses a different renewal problem; the closest inspected global reset catalogue results use stationary observables on a ring.

## value

PASS

The exact midpoint is an invariant of a physically motivated optimization with a tunable geometric obstruction. The optimal rate's nonmonotonicity, despite strictly decreasing mean times at fixed and optimized rates, gives a concrete distinction a researcher comparing screenable and externally imposed resets can use. This is a structural prediction beyond merely computing a known transform or locating a numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
