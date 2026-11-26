# Independent mathematical audit

## correctness

PASS

This assessment is of the repaired claim at repairs/4/RESULT.md. The original endemic reduction is correct: for a>0 multiplication by 1−ax gives a nonzero quadratic or lower-degree polynomial, and for a=0 the equation is nonzero affine or constant. The rational roots and strict cubic Routh signs verify the two sinks and the saddle with one unstable direction, but the original local eigenvalue argument did not establish which basins the unstable branches enter. The repaired proof checks that additional assertion: in deviations y=I−E and z=R−E the norm r²=y²+βbE z² cancels the fast linear cross term. Direct bounds on 0≤x≤13/50 give r′≤−3r/10+5|x′|/4 inside r≤|G|/16 and |x′|≤3|G|/800. The wall derivative is at most −177|G|/12800, and x′ has the sign of G and magnitude at least h|G|/2. Thus the two tube regions trap and converge to different endemic sinks. Compactness at an interior slice, with passage times diverging as the starting points tend to the saddle, yields a backward orbit to that saddle in each tube; the unstable manifold has only those two branches. Hyperbolic exit and openness of the two sink basins give the local two-sided separation. Finite segments entering sink neighborhoods persist under small parameter changes. The unchanged script certifies equilibrium algebra and stability coefficients, not the new orbit conclusion; the certificate for that conclusion is analytic.

## originality

PASS

Pass applies only to the repaired, explicitly certified basin-separation and saddle-to-sink connection claim. The original headline count and rational existence of the local endemic pattern are not distinct: Resultary 862b1c9a80d4 proves the same at-most-two endemic-root statement for a>0 and gives the same two endemic sinks and interior endemic saddle; the a=0 root count is immediate and the extra disease-free sink does not change the endemic pattern. The original proof also did not establish its suggestion of actual basin separation. The repair removes the count and the existence of two local sinks as originality claims and proves the destinations of both unstable branches for the original witness, which neither the stronger local-attractor result nor the motivating model and simulations establish in the inspected passages.

## value

PASS

For this three-dimensional coupled flow, coexistence of two sinks and an intervening saddle in the adherence coordinate is not a basin theorem. The explicit certificate identifies both unstable branch destinations and two open sets of initial conditions with monotone but different adherence outcomes, at a specified finite behavioral speed. It gives dynamical meaning to the saddle and a robust separation statement that the local equilibrium count alone could not support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
