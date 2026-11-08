# Independent mathematical audit

## correctness

PASS

For m>=2, 0<b<1, a>0, 2ma²=c²<1+b=v, decompose the matrix into eigenvalue 1−b (m antisymmetric paired modes), v (m−1 pair-symmetric difference modes), and 2x2 hub block [[1,c],[c,v]], establishing SPD. Existence of a scaling D with κ(DAD)<=K is equivalent to a diagonal S satisfying S<=A<=KS, a convex feasibility set. Averaging under pair-swaps and pair-permutations proves the existence of an orbit-constant optimum; Perron positivity of the top generalized eigenvector and PSD sandwich force each optimal diagonal to be orbit-constant, giving uniqueness modulo common scale. For D(t)=diag(sqrt(t),1,..), λ±(t)=(t+v±sqrt((t−v)^2+4c²t))/2, and κ=λ+/min(λ−,1−b). The λ+/λ− part uniquely minimizes at t=v; if c²<=4b²/v then λ− crosses 1−b at t_c=2b(1−b)/(2b−c²)<=v, giving t*=t_c; otherwise t*=v. Substitute to obtain both exact κ branches and Jacobi iff ma²=b². Independently minimized representative m=3,b=0.4,c²=0.12, yielding t≈0.705882353 and κ≈2.509803922; source verify.py tests 126 cases, but proof is all real parameters.

## originality

PASS

Best-of-knowledge PASS for an exact phase diagram and uniqueness among ALL positive diagonal congruences in the matched-leaf hub/triangular graph, not for abstract diagonal scaling algorithms, Loewner feasibility, or known property-A optimality. Van der Sluis 1969 exact Jacobi optimality for Young property A is inapplicable here because the hub with each paired leaf triangle is not bipartite. Braatz–Morari generic condition-number minimization does not present the explicit t*(b,c²) transition. Relevant Shapiro 1985 and Kolotilina 2002 full papers were unavailable, therefore possible broad characterization reducing to this explicit case remains a documented priority risk.

## value

PASS

Diagonal conditioning is a canonical preconditioning problem and matched pairs with one hub are natural sparse correlation matrices. A sharp switch between an eigenvalue-crossing optimizer and the balanced hub mode, plus an exceptional precise Jacobi-optimality curve and uniqueness unrestricted by symmetry, are meaningful and reusable exact results rather than arbitrary small-dimensional tabulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
