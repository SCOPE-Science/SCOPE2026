# Independent mathematical audit

## correctness

PASS

P is the normalized adjacency of complete balanced bipartite K_{m,m} with eigenprojectors J,H,R and eigenvalues +1,-1,0^(N-2), so the stationary Lyapunov series converges for all a in (0,1) and produces the displayed common diagonal variance sigma^2/N[1/(1-a²)+1/(1-a²(2d-1)²)+(N-2)/(1-a²(1-d)²)]. The function f(x)=1/(1-a²x²) has f"(x)=2a²(1+3a²x²)/(1-a²x²)^3>0, so the nonconstant variance is strictly convex in dispersal d; endpoint derivative signs yield one minimizer. Substitution gives N=4 optimum 2/3 exactly, and for even N>4 derivative signs give 2/3<d*<N/(N+2). The implicit ratio has positive derivatives in d and a for x=2d-1>y=1-d, forcing d* strictly decreasing in a. Expanding the root with delta=1-d=O_a(N^-1) gives the stated size asymptotic. 84 fresh direct real-space Kronecker-Lyapunov calculations verified equal diagonals and dispersal-invariant mean variance.

## originality

PASS

Known Moran-effect and AR(1) metapopulation literature contains general covariance/synchrony methods. Abbott 2011 full accessible article uses all-to-all uniform migration, not K_{m,m} with spectral values 1,-1,0; Ripa 2000 considers general linearized spatial synchronization but its full article was unavailable and its abstract alone cannot rule out an implicit specialization. In Resultary and adjacent published SCOPE results no identical local-variance optimizer was found. The exact bipartite unique optimum, four-patch exception, monotone response dependence and large-N correction were not identified in the inspected primary statements; originality is qualified.

## value

PASS

A sharp exact migration policy for a symmetric but nontrivial network topology, with an exceptional N=4 rate and sensitive AR(1) dependence, directly addresses a natural variance-mitigation design problem in coupled stochastic populations; its large-N law is structurally informative, despite relying on standard spectral Lyapunov techniques.

The dated certificate retains the supplied scientific assessment, sources and limitations.
