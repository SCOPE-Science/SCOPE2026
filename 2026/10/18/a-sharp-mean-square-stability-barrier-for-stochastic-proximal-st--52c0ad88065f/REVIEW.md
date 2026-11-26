# Independent mathematical audit

## correctness

PASS

Algorithm 1 samples before recomputing g_k, including at k=0. Substituting the sampled curvature gives the stated g_k and solving the shifted quadratic prox gives x_{k+1}=x_k-t g_k/(1+ta). The deterministic z0=(1,1,0) is compatible with the equal-position initialization (no assumption that the subsequently computed g0 is zero). My independent polynomial-feature lift gives det(I-C)=-tF(t)/(16(2t+1)^3), F's rational root bracket, the exact Lyapunov identity and positive leading minors at t=1/2, and both positive Gram determinants from enumerated two-step paths. Descartes' sign count and continuity of the cone Perron eigenvalue imply that its level-one crossing can occur only at the unique positive F root; the contraction at 1/2 and determinant -13/125 at t=2 force it to cross there. Below it, all augmented second moments decay. At and above it, the positive-definite two-step covariance from the specified start pairs positively with a nonzero positive-semidefinite adjoint Perron eigenmatrix; the positive-definite two-step primal observability Gramian turns that into an eventually uniform positive lower bound for E[x_k²] at equality and a geometric lower bound above. The independent charpoly at t=2 factors as (2z-1)(5z²-3z+2)/10 for the mean, so all signed means decay there. This is not a claim of pointwise monotone squared error, almost-sure stability, or instability for every initial. The unbounded-in-x sample gradient variance is x², outside the source convergence theorem.

## originality

PASS

The closest exact catalogue theorem already subsumes the signed-mean half, but not the full exact second-moment classification or the compatible-init primal lower bound. The source's sufficient theorem is for a different noise/stepsize regime. Direct iterate inertia in the other stochastic proximal algorithms does not give this same-sample estimator recursion. No inspected source covers the surviving second-moment claim.

## value

PASS

A minimal heterogeneous but convex common-minimizer instance tests whether momentum variance reduction preserves the stability usually associated with exact prox. The complete stepsize cutoff and compatible-start primal witness provide a precise benchmark beyond the source's bounded-gradient-variance setting and show why a stable signed mean is not enough.

The dated certificate retains the supplied scientific assessment, sources and limitations.
