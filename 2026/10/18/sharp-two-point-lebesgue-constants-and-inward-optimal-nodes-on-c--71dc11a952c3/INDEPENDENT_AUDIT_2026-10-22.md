# Independent mathematical audit

## correctness

PASS

For each 0<theta<pi, the input space is complex C(K_theta) and the projection range is span_C{1,z}; optimization is only over two distinct sampling nodes, not all projections. For fixed u<v the two Lagrange functions yield the exact operator norm max_t (|e^{it}-e^{iu}|+|e^{it}-e^{iv}|)/|e^{iv}-e^{iu}|, since arbitrary unit node phases extend continuously to C(K_theta). Set m=(u+v)/2, d=(v-u)/4. Piecewise chord identities give the midpoint bound sec(d) and the farther exterior test bound sin(theta/2)/sin(d). For symmetric nodes the two bounds equal the exact maximum; one strictly increases with d and one decreases, so the unique optimum solves tan(d)=sin(theta/2). Any asymmetric midpoint admits a farther test point with strictly larger sin-quotient, proving the uniqueness assertion. Endpoint norm sec(theta/2), open-arc limits, and small-angle expansion follow. Independently computed direct complex chord values on six arcs and all midpoint/endpoint bounds; all passed. The finite test is corroborative; the exact chord envelope and monotonicity prove continuum quantifiers.

## originality

PASS

The exact all-angle arc family is in the operator-space literature, but the two-node interpolation projector norm and unique inward optimizer are different invariants. The interval Lebesgue minimax, full-circle Chebyshev/Riesz polarization, and high-degree open-arc asymptotics do not entail this closed-form two-sample arc minimax. The proof is elementary but the arc-dependent sharp node placement is a new, nonmechanical parameter optimization among arbitrary node pairs.

## value

PASS

Sharp conditioning for arbitrary continuous complex measurements on a circular subarc is a natural sampling invariant. The unique inward optimal configuration and strict contrast with diverging endpoint conditioning as theta approaches pi diagnose a genuine numerical-stability boundary, not a normalization or textbook inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
