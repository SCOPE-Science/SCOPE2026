# Independent mathematical audit

## correctness

PASS

At the specified equilibrium the two-coordinate linear drift has trace -p-r kappa and determinant r Delta; the diagonal infinitesimal covariance is positive definite. Its unique stationary Gaussian covariance (s,t,u) obeys ps-qt=x_* B, r alpha s+qu=(p+r kappa)t, and u=w_*+alpha t/kappa. Solving gives the two positive-denominator expressions in RESULT.md. In particular (alpha/kappa)s-t=alpha x_*(B-q)/(kappa(p+kappa r)), so (u-t^2/s)/w_* gives the stated ratio and sign. For rho=q/B, eta=alpha q/(kappa p), z=kappa r/p, and h=1-eta(1-rho), the nonconstant factor is (z+rho)/((z+1)(z+h)). Its derivative numerator is (1-rho)(h-rho)-(z+rho)^2. This is negative for rho>1, but with a negative prefactor V increases; at rho=1 V is constant. For rho<1 the numerator strictly decreases at z>0 and changes sign exactly when (1-rho)sqrt(1-eta)>rho. Substitution yields the boxed peak; equality gives a zero derivative only at the excluded boundary. This includes q=0, eta=0. The result assumes the rest of the drift and diffusion parameters are held fixed, and classifies only this conditional Gaussian variance. For the illustration, Descartes and the signs at 0,1,2 isolate two positive roots; exact rational endpoint signs and Delta>0 identify the large stable root. An independently written bounded check (python3 /workspace/review_evidence/bounded_checks.py) solves the three covariance equations numerically by elimination and reproduces r*=1.12283727349205655 and V*=2.01464895217714154, along with the three benchmark ratios. The frozen verifier and its recorded output were inspected, not rerun.

## originality

PASS

The model, linear-noise matrices, Lyapunov description, Gaussian conditioning method and benchmark examples are prior. The supported distinction is the explicit all-rate Schur complement and exact global regime classification for this covariance structure, not any of those prerequisites or the three inherited example rates.

## value

PASS

Beyond a routine covariance solve, the finding resolves the motivated finite-rate question: an intermediate maximum can coexist with convergence to the same reference level, and the exact gain/damping boundary distinguishes it from monotone cases. The benchmark alone does not determine that distinction. The contribution is to a specified Gaussian approximation, not finite-population stationarity, rare-event optimization or a biological design claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
