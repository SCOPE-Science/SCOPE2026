# Independent mathematical audit

## correctness

PASS

The exact warm start yields s=alpha0*b and y=alpha0*A*b, hence alpha_long=alpha0 and alpha_short=(b^T A b)/(b^T A^2 b). For any interval alpha1, x2=alpha0*alpha1*(theta I-A)b with theta=1/alpha0+1/alpha1>=2mu. Stieltjes structure and L<=2mu make theta I-A entrywise nonnegative. For diag(1,kappa), b=(1,eps), theta_short is maximal and (theta_short-kappa)*(1+t)*(1+kappa*t)=kappa^2*t^2+(kappa+1)*t+2-kappa, negative for t=eps^2 sufficiently small when kappa>2. One dimension terminates; 2D is sharp. Independent exact rational fractions match both BB endpoints and midpoint negativity.

## originality

PASS

The known BB interval sharp objective-monotonicity frontier at kappa2 covers objective gaps, not coordinatewise orthant invariance. The separate published CG, steepest-descent and good-Broyden kappa2 findings use different algorithms. The Stieltjes matrix certificate and simultaneous all-selector 2D obstruction add a non-implied sign statement.

## value

PASS

A BB step is routinely used without projection, and whether the raw iterates remain feasible in the nonnegative orthant is an independent natural invariant from objective descent. The exact all-selector condition-number safety limit and uniformly failing minimal 2D witness settle a meaningful one-step numerical boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
