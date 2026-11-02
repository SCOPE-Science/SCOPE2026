# Independent mathematical audit

## correctness

PASS

Let U=sin^2 theta under probability density proportional to sqrt(1-t sin^2 theta), t=1-b^2/a^2. The centered boundary covariance eigenvalues are a^2 A(t) and b^2(1-A(t)), A=E_t[U]. The two independent sampling moments recover its trace and determinant exactly: D=2 tr Sigma, H=3 det Sigma/2. Their ordered eigenvalues therefore solve z^2-(D/2)z+2H/3=0. The nonstandard global step is A'(t)=-1/2 Cov_t(U,U/(1-tU)); the covariance bound gives -A(1-A)/(2(1-t))<A'<0, from which h=(1-t)(1-A)/A is strictly decreasing and s<h<sqrt(s). Hence the ordered eigenvalue ratio uniquely recovers t and then both semiaxes, with the t=0 circle endpoint treated directly. Expanding A at t=0 by the arcsine-beta variance yields eta=32H/(3D^2), t=(8/3)sqrt(1-eta)+O(1-eta); the exponent 1/2 cannot be improved for this scalar. I independently implemented scipy quadrature and reconstructed all 24 test configurations plus three near-circle inverse-expansion cases; finite tests are only a cross-check. No statement about translation, orientation, arbitrary ovals, or Lipschitz inversion at the circle is proved.

## originality

PASS

The elementary covariance trace/determinant identities and forward elliptical-wire inertia integrals are known, notably Tatum section 2.20 and Lord (2014). The specific incremental claim is an all-axis-ratios strictly invertible inertia shape map, the nontrivial sharp ratio sandwich, and square-root loss of inverse conditioning at a circular ellipse. I read Tatum's actual equations and numerical discussion, which do not give those global inequalities. Lord is highly relevant, but complete pages were inaccessible, so priority remains explicitly uncertain; the authenticated institutional request stopped at VPN disconnected. No searched exact or stronger covering theorem was found. PASS is best-of-knowledge, not a uniqueness certificate.

## value

PASS

This is a natural inverse geometric-probability question because Euclidean arclength on a nonspherical ellipse is not the affine push-forward of uniform circle arclength. The result gives exact global identification from two rotation-invariant random-sample statistics and quantitatively locates the circle as an inverse-stability singularity. The global sandwich is mathematical content beyond evaluating an elementary integral; the result is narrowly scoped to Euclidean elliptical boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
