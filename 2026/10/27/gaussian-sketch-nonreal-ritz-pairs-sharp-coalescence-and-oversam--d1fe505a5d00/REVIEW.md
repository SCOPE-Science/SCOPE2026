# Independent mathematical audit

## correctness

PASS

The Schur complement is positive under the stated bound. Almost surely the two sketched basis columns have full rank. With p=(SQ)^dagger Se3, the reduced matrix is diag(a,a+delta)+p(g,g); its discriminant divided by 2g^2 is t^2-2tX+Y^2 after the orthogonal rotation. At delta=0 the discriminant is a square. The normal-Wishart mixture gives the density (s-1)/(2 pi) times (1+X^2+Y^2)^(-(s+1)/2); both integrals are proper also at s=2. For small t, rescaling Y by sqrt(t) gives width 2 sqrt(2X) in the limit and an integrable bound in X for every s>=2, recovering C_s by the beta integral. At large t the rescaling (X,Y)=t(u,v) fixes 2u>1+v^2, which avoids the origin; the integrable radial tail yields K_s. Solving the radial quadratic gives the stated two inverse radii, and beta integrals give the s=2,3 constants. No fixed-gap s-to-infinity claim is needed. The submitted check.py was inspected, not executed. Independent replay: python /workspace/reproductions/reproduce.py; radial-survival quadrature reproduced P_s(1) for s=2,3,5 and both scaled endpoints (within 0.0007 relative at the selected gaps). These finite checks are not asymptotic proofs.

## originality

PASS

Pass for the exact Gaussian discriminant law and sharp fixed-row-count gap limits as a package; neither qualitative nonreal Ritz values for SPD input nor the Gaussian least-squares Student law is novel. Inspected later index records overlap genuine parts of the finding, but do not establish prior coverage of the package.

## value

PASS

The family isolates the loss of real Ritz values in a standard randomized extraction without confounding the gap with sketch conditioning. The complete gap response gives a benchmark at minimal as well as oversampled row counts, distinguishing a square-root onset from a sketch-size-dependent separated-gap tail. This does not establish robustness or convergence of a full eigensolver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
