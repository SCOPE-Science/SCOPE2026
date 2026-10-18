# Independent mathematical audit

## correctness

PASS

Direct differentiation of W=z−g x²/(2a) gives dW/dt=−bW+κx² because the mixed gxy cancels the x′ term. Exact independent SymPy polynomial expansion checked the identity. A bounded complete trajectory makes W bounded; variation of constants from t−T to t and b>0 eliminates e^(−bT)W(t−T), yielding the nonnegative backward convolution. Equality at any t implies x vanishes on its entire past, then the first equation forces y=0; the third reduces to z′=−bz and backward boundedness forces z=0. Autonomous uniqueness makes the trajectory identically zero. Every compact invariant point belongs to a bounded complete orbit, proving the set statement. No unsupported assertion of existence of chaotic or other non-equilibrium recurrence.

## originality

PASS

The closest direct parent Lorenz-like theorem in Li–Ou 2011 analyzes the opposite sign bg>2a(f+g), κ<0, and its newer 2021 extension studies bifurcations and global heteroclinics, not the κ>0 backward memory/paraboloid exclusion. The 2018 boundary heteroclinic analysis has κ=0. Related Lorenz-84 exponential memory is for a different equation; it does not imply this exact parabolic transform for the Li–Zhao–Geng system. The elementary stable-filter technique is not claimed as new.

## value

PASS

Exact pointwise parabolic confinement on every bounded complete non-equilibrium trajectory is more informative than a stationary moment balance, and is uniform in the arbitrary y-equation coefficients c,d. It gives a structurally motivated admissibility check for compact attractors on the κ>0 side of a natural parameter boundary; it does not purport to prove attractor existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
