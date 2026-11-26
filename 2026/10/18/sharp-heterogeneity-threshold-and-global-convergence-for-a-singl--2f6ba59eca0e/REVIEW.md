# Independent mathematical audit

## correctness

PASS

The only boundary equilibrium is zero: a zero component nullifies infection in all other equations, while no component equal to one can be stationary. At positive equilibria multiplication by xᵢ gives the stated scalar parametrization with s=λ times the product of the components. The log-elasticity sum decreases strictly from n/2 to zero; the level function diverges at both ends and has a nondegenerate unique minimum, giving the claimed exact root counts. At an interior equilibrium the Jacobian is diagonally similar to a symmetric positive rank-one perturbation of a negative diagonal; a positive diagonal congruence reduces its inertia test to the elasticity sum crossing one. For the dynamical fold, the left zero eigenvector can be chosen strictly positive from the rank-one kernel and the positive diagonal similarities, so its pairing with F_λ is positive. Differentiating F(X(s),L(s))=0 twice and pairing with that eigenvector at s* gives the quadratic pairing along X′(s*) as minus L″(s*) times this positive pairing. It is nonzero, which verifies the simple saddle-node conditions. At zero the Jacobian is −diag(rᵢ) because n≥3. Direct differentiation gives the exact weighted-gradient identity. Upper faces are left immediately and the logarithmic term traps the orbit in a compact sublevel with strictly positive gradient weights; LaSalle puts the limit set in the finite equilibrium set. The connectedness of the limit set then gives convergence, including at the fold and for initial points on lower faces. Strict concavity of log φ(exp u) gives Jensen and strict Karamata inequalities at each finite s; evaluating at the more heterogeneous vector's attained minimizer preserves strictness. Implicit smoothness of the minimizing s and the envelope identity give the stated sensitivity and sum. Independent numerical replay `python3 /workspace/branches/independent-replay.py 1` reproduced the five folds and checked the stationary identities, derivative values and one strict fixed-mean majorization comparison; the analytic proof establishes the general statements.

## originality

PASS

No inspected statement covers the combined individualized-ratio exact fold, strict log-majorization, and all-trajectory convergence including at the fold. The strongest heterogeneous node-based paper already contains the model as a special case, and the nearest Resultary exact-fold theorem covers the homogeneous single-edge specialization, so neither novelty of the general model nor of the homogeneous fold is credited. The distinction is exact classification, quantitative balancing of individual ratios, and global convergence in the heterogeneous special case.

## value

PASS

A single genuinely higher-order conjunctive interaction is a natural building block rather than an arbitrary parameter slice. The result gives the exact size and direction of the heterogeneity effect through a strict ordering and coordinate sensitivities, and it separates global convergence of individual trajectories from mere local stability, including at the degenerate parameter. These are useful model-level conclusions even without a result for overlapping edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
