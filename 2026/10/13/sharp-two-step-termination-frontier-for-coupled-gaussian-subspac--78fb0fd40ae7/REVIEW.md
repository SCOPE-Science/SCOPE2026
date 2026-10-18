# Independent mathematical audit

## correctness

PASS

For H SPD 2x2, the exact rank-one Newton step becomes y->(I-uu^T)y under y=H^(1/2)x, u proportional to H^(1/2)s. Outside the null event of an initial direction exactly parallel to y0, the first projection leaves a nonzero vector orthogonal to u1; the second annihilates it iff u2 perpendicular to u1. Anisotropic Gaussian angular density is sqrt(kappa)/(2*pi*(cos^2 theta+kappa sin^2 theta)); its maximal overlap with a 90-degree shift integrates to 4/pi*atan(1/sqrt(kappa)). The explicit maximal angular coupling and conditional Gaussian radial density a(theta)r exp(-a(theta)r^2/2) recover exactly N(0,I2) marginals and attain the bound. Joint-Gaussian conditional noise gives zero probability unless deterministic orthogonal C solves HC skew-symmetric, which forces H scalar in 2D. Independent blocks give geometric pair count E[T]=2/q. Numerical midpoint quadrature independently checked angular normalization and overlap for kappa=1,2,5,9,25.

## originality

PASS

PASS best-of-knowledge for the anisotropic sharp Gaussian-marginal two-step success law plus joint-Gaussian rigidity. Classical maximal couplings, isotropic orthogonal random features, and the original RSN method are prior ingredients explicitly excluded from originality.

## value

PASS

A natural random linear-algebra question is how much temporal dependence can improve finite termination while preserving ordinary Gaussian one-step sketches. The exact attainable probability and strong separation from jointly Gaussian dependence are nontrivial algorithmic/probabilistic structural facts, even with Hessian-aware coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
