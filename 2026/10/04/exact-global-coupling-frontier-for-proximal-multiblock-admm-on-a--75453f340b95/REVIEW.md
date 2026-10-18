# Independent mathematical audit

## correctness

PASS

Reconstructed the source five-state Gauss–Seidel proximal ADMM map for x1=x0, x2=x1, costs (+a,-a,+a)/2 times x^2, with equal rho and eta. The exact characteristic polynomial splits into Q(r)=[1+(1+chi)p]r^2-(2+chi p)r+1 (always Schur for chi,p>0), and P(r)=(1+3p-dp^2)r^3+[(chi^2-2)p^2-3p-3]r^2+3r-1. Schur reduction of the cubic produces dp<3-sqrt(chi) and ep^2-6p-8<0; other Jury inequalities follow in the stated feasible domain. Independently formed the five-variable matrix and exact rational characteristic polynomials for chi,p=(4,1/10),(4,1/5),(1/2,10),(8,1/100), matching Q*P and eigenvalues. At (4,1/10) cubic factors (6r-5)(5r^2-9r+5)/25, unit-modulus complex roots; for (4,1/5) blocks remain strongly convex but full map unstable. The finite rational cases supplement the algebraic all-parameter proof.

## originality

PASS

Li–Yuan primary work supplies the nonlinear-chain proximal multiblock algorithm and a conservative sequential sufficient parameter procedure, not the exact equal-penalty/equal-proximal scalar spectral frontier. Other direct three-block ADMM results have different block curvature or update architecture (third variable updated twice, fewer proximal terms). The explicit two Schur inequalities, chi=4 convexity/stability separation and chi>=9 obstruction have not been identified as prior corollaries. Residual risk: prior multi-block quadratic spectral analysis under a different method alias.

## value

PASS

The result isolates a real coupling issue in a natural minimal three-block nonconvex model: individual proximal subproblems can be well posed and strongly convex while the globally coupled ADMM map diverges. Exact parameter frontiers and a no-stabilization region inform algorithm design and clarify sufficiency-vs-necessity of existing convergence criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
