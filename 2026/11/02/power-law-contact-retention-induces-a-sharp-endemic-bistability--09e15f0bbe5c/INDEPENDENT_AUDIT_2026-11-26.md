# Independent mathematical audit

## correctness

PASS

Inward boundary signs give invariance, and positive y stays positive by the multiplicative prevalence equation. The disease-free eigenvalues are tau/(1+omega)-1 and -xi(1+omega). The endemic relation is tau=T(s)=1/s+omega s^(q-1), 0<s<1. Its derivative has numerator omega(q-1)s^q-1, so for all q from 1 through q_c it is strictly decreasing in the open interval, including the critical endpoint case. Above q_c there is a single minimum with T''=q/s_f^3>0 and the stated tau_f below T(1). This verifies the counts including equality at both thresholds. The Jacobian has negative trace and determinant -xi y s T'(s), verifying sink and saddle types. At the fold there is a simple zero eigenvalue; eliminating the contact equation, whose contact derivative is nonzero, gives a scalar equilibrium equation with nonzero parameter and quadratic derivatives. This supplies the saddle-node nondegeneracy. At tau=tau_0 and q<=q_c the cooperative flow traps all solutions between the monotone corner solutions; their limits are equilibria, and the disease-free point is the only one. The critical rates also follow directly without assuming instant contact adjustment or invoking center-manifold tracking: write g(y)=1/[1+omega(1-y)^q], w=z-g(y), a(y)=tau_0/T(1-y)-1, and B(y)=tau_0(1-y). Then y'/y=a+Bw and w'=-[xi/g+g' y B]w-g' y a. For k=1 below q_c and k=2 at q_c, Taylor expansion gives a=-c y^k+O(y^(k+1)), with c=[1-omega(q-1)]/(1+omega) or c=1/(2omega), respectively. Along a positive solution w/y^k solves a scalar linear equation with damping xi/g+g' y B+k y'/y tending to xi(1+omega)>0 and forcing -g'a/y^(k-1) tending to zero. Thus w/y^k tends to zero; y'/y^(k+1) tends to -c and y^(-k)/t tends to kc. This yields both amplitudes at every fixed xi>0, not just in a time-scale limit. The uploaded verifier was inspected but not executed. Its special-case symbolic and trajectory examples are not the universal proof.

## originality

PASS

The aNIMFA model, general disease-free threshold, scalar endemic relation, and examples of adaptive bistability are prior. The supported distinction is the sharp classification of this constant-creation power-law family together with the critical extinction exponent switch and its exact coefficient. A generic inverse-time critical law outside the decreasing-response/cancellation regime is not the degenerate law claimed here.

## value

PASS

The useful contribution is the sharp change of decay exponent at a precise cancellation point, together with the associated equilibrium classification for the stated family. Showing the inverse-square-root law on every positive initial trajectory at criticality, with a leading amplitude independent of the positive link relaxation speed, distinguishes the full planar dynamics from a formal nullcline approximation. This is a deterministic mean-field result, not a finite-network or empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
