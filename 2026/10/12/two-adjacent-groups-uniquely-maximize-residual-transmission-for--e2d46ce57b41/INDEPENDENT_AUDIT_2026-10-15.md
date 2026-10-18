# Independent mathematical audit

## correctness

PASS

Write eta_i=1-epsilon u_i, u_i>=0, sum_i u_i=1. The simple 2 eigenvalue of adjacency K makes its perturbed Perron root F(epsilon,u) uniformly C^2 in u for small epsilon across the compact simplex. With J=11^T/5 and reduced resolvent R=(2I-K+J)^-1-J, exact second coefficient Q(u)=(2/5)u^T R K u=(4/25)(E(u)-N(u)), where E=sum cycle-edge products and N=sum two-step nonedge products. An exact Motzkin-Straus-type support shifting proves E<=1/4, and Q=1/25 only at the five balanced adjacent-edge vectors v=(e_i+e_{i+1})/2, because equality also requires N=0. Uniform C^2 convergence of (F-2+2epsilon/5)/epsilon^2 to Q forces every global maximizer near these isolated points. At any v, Q inactive-coordinate partial derivatives are strictly smaller than active ones; the strict inequality persists and forces the optimizer onto the corresponding edge face. Strict negative second derivative -8/25 on that face persists, and reflection symmetry forces the unique exact edge optimum to equal split. Independently reconstructed the 5x5 Q matrix with adjacent coefficients 2/25 and nonadjacent -2/25, characteristic polynomial factors for single and adjacent allocation, and sample Perron roots. Universal small-epsilon proof uses compactness and analytic eigenvalue perturbation, not sampled epsilon values.

## originality

PASS

Delmas, Dronnier and Zitt (2023) introduce exactly the cycle next-generation model and anti-Pareto vaccination; their Section 2.4 gives an extinction-cost theorem and N=12 numerical Pareto/anti-Pareto heuristics, not the exact N=5 small-budget maximizer. Their 2022 cordon sanitaire theorem excludes disconnecting strategies as worst, but all candidate eta_i here stay strictly positive and connected. The separate convexity/concavity sufficient cases do not apply to the mixed-sign spectrum of C5. Thus the explicit N=5 adjacent equal-split phase is not implied by these strong prior results.

## value

PASS

A motivated sharp local optimization theorem for the smallest unresolved odd epidemic circle determines ALL worst vaccine allocations, not merely an example or simulated approximate strategy. The exact adjacent equal split reverses an intuitive one-group-first heuristic at N=5 and supplies a controlled spectral perturbation benchmark within the stated idealized model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
