# Uniform destruction of the rotation-1/3 caustic in the cos 5theta deformation of the circle

## Context

Consider the explicit analytic family of strictly convex tables Gamma_epsilon in
polar coordinates r(theta) = 1 + epsilon cos(5 theta) for small epsilon, with
rotation number in (0,1/2] where rotation number 1/3 corresponds to period-3
orbits. The first-order Bialy-Mironov obstruction for q = 3 vanishes identically
because 5 is not divisible by 3, so the persistence-versus-destruction decision
turns on higher-order coefficients. Related general theory gives necessary and
sufficient high-order persistence conditions via the Bialy-Mironov generating
function, but does not evaluate this polar n = 5, q = 3 case.

## Definitions

Let gamma(theta; epsilon) = (1 + epsilon cos 5theta)(cos theta, sin theta).
For apex A and symmetric triangles (A, A+t, A-t) define the perimeter
L(A,t;epsilon) = 2|gamma(A) - gamma(A+t)| + |gamma(A+t) - gamma(A-t)|.
Critical points in t give symmetric 3-periodic billiard orbits. At epsilon = 0,
t* = 2pi/3 gives equilateral triangles with L_0''(t*) = -3sqrt(3)/2, nonzero.
By the implicit function theorem each A in {0, pi/5} continues to a unique
symmetric critical point t*(A;epsilon), with reduced action
ell(A;epsilon) = L(A, t*(A;epsilon); epsilon). Put
Delta(epsilon) = ell(pi/5; epsilon) - ell(0; epsilon).

## Result

There is epsilon_0 > 0 such that for all 0 < |epsilon| < epsilon_0 the table
Gamma_epsilon has no smooth convex caustic of rotation number exactly 1/3.
The two symmetric 3-periodic orbits have perimeters differing by
Delta(epsilon) = -855 sqrt(3) epsilon^3 + O(epsilon^4), hence nonzero for
small nonzero epsilon, contradicting the equal-action consequence of a 1/3
invariant circle. First order vanishes and second-order reduced action is
apex-independent (K2 = 111 sqrt(3)/4 at both apices); the barrier first
appears at order epsilon^3 with K3(0) = +855 sqrt(3)/2 and
K3(pi/5) = -855 sqrt(3)/2.

## Proof / evidence

Chord expansion q = q0 + eps q1 + eps^2 q2 + eps^3 q3 with
q1 = Q1/2q0, q2 = Q2/2q0 - Q1^2/8q0^3,
q3 = Q1^3/16q0^5 - Q1 Q2/4q0^3 (no Q3 since r is affine in epsilon).
Exact sympy evaluation at t* = 2pi/3 gives e.g. L1* = 0,
L2* = 3sqrt3/16, L3* = -/+3sqrt3/64, F1* = +/-63/4, F2* = -81/32,
G0* = -3sqrt3/2, G1* = +/-183sqrt3/8 (upper sign at A = 0), H0* = 3/4.
Lyapunov-Schmidt recursion u1 = -F1/G0, u2 = -(G1 u1 + H0 u1^2/2 + F2)/G0
gives u1 = +/-7sqrt3/2, u2 = 447sqrt3/8 (both), and the reduced actions
ell(A;eps) = 3sqrt3 + (111sqrt3/4) eps^2 +/- (855sqrt3/2) eps^3 + O(eps^4).
Newton solutions of dL/dt = 0 from t* confirm true orbits:
Delta/eps^3 = -1370.28, -1451.98, -1473.60, -1479.73 at
eps = .01, .005, .0025, .001 (and identical values for negative eps),
converging to -855sqrt3 approx -1480.90, with shifts converging to
+/-7sqrt3/2. The billiard map of a strictly convex analytic table is an
exact monotone twist map; a 1/3 caustic yields a rotational invariant
circle on which all period-3 orbits are action-minimizing with common
action (Aubry-Mather / Mather barrier), so the two symmetric orbits would
have equal perimeter, contradicted by nonzero Delta.

## Limitations

The twist-map non-persistence lemma is quoted from standard Aubry-Mather
and Mather barrier theory with references, not re-proved. Identification
of the two symmetric continuations as the Birkhoff minimizer/minimax pair
uses Z5 symmetry and the leading cos(15s) reduced potential.
Length-rescaling invariance of the barrier order is argued as a global
A-independent 1 + O(eps^2) factor, not computed term by term.

## Reproducibility

Run output/artifacts/ls_data.py to reproduce all exact coefficients and
the K1/K2/K3 values; run output/artifacts/newton_check.py to reproduce
the true-orbit Delta/eps^3 convergence for both signs of epsilon.
Hand checks of F1* and L2* and high-precision odd-part checks agree.

## References

Koudjinan-Ramirez-Ros, High-order persistence of resonant caustics in
perturbed circular billiards, arXiv:2503.07488 / Ergod. Th. Dynam. Sys.
2026; Kaloshin-Sorrentino, Ann. Math. 2018; Bialy-Mironov, Ann. Math.
2022; Mather 1982/84, Bangert, Meiss-MacKay barrier theory.
