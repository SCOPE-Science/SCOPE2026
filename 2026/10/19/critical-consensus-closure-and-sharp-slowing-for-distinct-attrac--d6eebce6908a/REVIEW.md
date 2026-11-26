# Independent mathematical audit

## correctness

PASS

On the fixed-mean hyperplane the attractive Laplacian is positive definite, so the Rayleigh maximum defines a finite positive threshold. Symmetric edge pairing gives the exact squared-norm dissipation: a negative semidefinite quadratic plus the negative sum of R_ij times [alpha*Delta^2-Delta*tanh(alpha*Delta)]. Each bracket is strictly positive for a nonzero difference. If the derivative vanishes at or below threshold, y is in the kernel of the signed Laplacian and every repulsive difference vanishes, so L_R*y=0 implies L_A*y=0 and y=0. This proves global asymptotic stability by bounded sublevels and LaSalle; above threshold the linearization has a positive mean-zero eigenvalue. For a simple critical kernel the stable complement is strictly contracting at the linear level. Its center graph has zero quadratic term because the vector field has no quadratic term. Projection of the cubic tanh term gives -kappa*a^3, with kappa=alpha_*^3/(3N) times the fourth-power repulsive edge energy. The energy cannot vanish on a unit null vector by the same two-kernel argument. On the center graph (a^-2)'=2*kappa+O(a^2), giving the signed vector limit, and local exponential tracking transfers it to all orbits except the zero center leaf. Global convergence brings every orbit into the local foliation. The flow is a global diffeomorphism at finite times; integer inverse-time images of the codimension-one strong-stable manifold give the invariant null exceptional set on each fixed-mean hyperplane. Independently, on the three-node path the mean-zero vectors (1,0,-1) and (1,-2,1) have threshold signed eigenvalues 0 and 3 at alpha_*=1/2. The unit critical vector gives kappa=1/18. Direct subtraction gives p'=-p and q'=-(q-tanh q)/3 exactly. For q(0)!=0, U=q^-2 grows to infinity with U'=2/9-4/(45U)+O(U^-2). First U/t tends to 2/9, then U=2t/9+O(log t), making the remainder after subtracting 2/9-2/(5t) integrable. Hence the finite logarithmic constant depends only on q(0). The frozen checker was read, not run; no finite trajectory is used as a proof of either asymptotic.

## originality

PASS

The model, signed-Laplacian frontier, strict-coercivity and instability cases, identical-network equality, and path threshold are credited to Boyce et al. Their exact Hessian supplies ingredients for the boundary closure, so that local extension should not be treated as a separate strong novelty claim. The supported distinct content is the critical dynamical theorem across distinct weighted topologies: the explicit positive edge-energy coefficient, signed sharp limit with a global exceptional-set characterization, and its next-order path specialization.

## value

PASS

At this natural threshold the signed spectrum alone cannot distinguish very slow attraction from instability. The explicit repulsive edge energy predicts the decay amplitude across different networks with a single critical mode, while the exceptional-set result identifies exactly which solutions instead relax exponentially. The path formula gives a concrete benchmark for the subleading correction and shows why a pure inverse-square time law misses a divergent logarithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
