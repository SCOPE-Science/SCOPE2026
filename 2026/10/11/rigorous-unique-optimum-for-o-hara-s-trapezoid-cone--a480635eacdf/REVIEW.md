# Independent mathematical audit

## correctness

PASS

Directly reconstructed edge-to-apex face areas: A(x,y,h)=6+sqrt(h²+x²)+2sqrt(h²+(2-x)²)+[sqrt(5h²+(x+2-2y)²)+sqrt(5h²+(x+2+2y)²)]/2 and V=2h. The paired lateral terms are even and strictly convex in y, forcing y=0. On that plane F=A³/(4h²), equivalent to Phi=A h^(-2/3). Phi is coercive as h tends to 0 or infinity or |x| diverges. For any c>0, G_c=A-c h^(2/3) is convex and strictly convex in h; A is strictly convex in x at fixed h>0. Two global minimizers would force a negative midpoint G_c, impossible. At any stationary Phi=c, G_c=0 and grad G_c=0, so convexity makes it a global minimizer; hence the two explicit A_x=0, 3hA_h=2A equations have exactly one solution. Recomputed this root and F to 20+ significant digits by an independent high-precision numerical procedure. The root solve corroborates only numeric values: global existence/uniqueness is analytic.

## originality

PASS

The motivating primary source publishes the canonical trapezoid and its numerical minimizer/fixed-height horizontal centers, but does not prove global uniqueness or an exact stationary-system characterization for the nontriangular case. Checked Resultary under exact numerical and geometry aliases; related optimized cones concern other bases/functionals. This is a bounded, best-of-knowledge refinement of a previously numerical test case, not a new general polygon theorem.

## value

PASS

A natural, explicitly published counterexample to naive extension of the triangle incenter method previously had only sampled numerical optima. Determining its unique global isoperimetric apex and exact stationary characterization is a mathematically motivated resolution of that specific nontriangular benchmark, not just reprinting numerical data. The strict-convexity argument gives a reusable certification mechanism for similar convex-norm surface functionals while expressly making no broad polygonal claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
