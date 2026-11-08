# Independent mathematical audit

## correctness

PASS

PASS. The source's hub-to-leaf softmax flux is exactly 42/289 at the patterned positive rational profile (21/17,14/17,14/17;187/153,127/153,127/153), canceling -84/289 hub and 42/289 leaf logistic drift. The chemical equations vanish exactly. An independently reconstructed six-dimensional Jacobian, decomposed into mean chemical -1, leaf-symmetric 3x3 and leaf-antisymmetric 2x2 blocks, has strictly Hurwitz characteristic polynomials: all cubic Routh-Hurwitz coefficients and a1*a2-a3 are positive at the rigorous upper bound chi<28/25, as are the antisymmetric determinant and negative trace. The homogeneous Jacobian modes kappa=0,1/3,1 also have negative trace and positive determinant there. Independent SymPy differentiation of the original six-dimensional ODE and numerical eigenvalues confirmed every eigenvalue is left of the imaginary axis; finite numerical eigenvalues are corroboration, not the proof. Hyperbolic persistence and open positive basins follow locally from standard stability and implicit-function arguments. The result does not classify basins or all equilibria. Source paths RESULT.md and check.py were read from their assigned frozen Git tree.

## originality

PASS

The exact sparse-graph two-attractor coexistence and strict below-threshold modal stability are not implied by the explicitly inspected original graphon/2-patch results or closest published-finding matches. Best-of-knowledge originality PASS with literature risk.

## value

PASS

PASS. Bistability on the smallest noncomplete connected simple graph shows that strict linear damping of every homogeneous Laplacian mode does not rule out a second hyperbolic spatial pattern with an open positive attraction basin. An exact rational witness in the original softmax chemotaxis model fills a mathematically meaningful nonlinear gap beyond the two-patch and graphon local threshold calculations. It is not merely code reproducibility; the stable coexistence phenomenon is the independently useful claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
