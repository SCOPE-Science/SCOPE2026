# Independent mathematical audit

## correctness

PASS

PASS. For U,V joint centered normal with variance q and correlation r, cos-cos and sin-sin covariance identities yield C=(1-z)^2/2+z(cosh(qr)-1), S=(1-z^2)/2+z sinh(qr), z=e^-q. Reflection kills cross cosine-sine covariance, so maximum over arbitrary phi of Var[(cos(U+phi)+cos(V+phi))/2] is max(C,S)/2. On [-1,0], C strictly decreasing and S strictly increasing in r, with C(-1)>S(-1), C(0)<S(0); their unique intersection e^(-qr)=2-z yields r*=-log(2-z)/q strictly in (-1,0). On (0,1] S exceeds the zero-correlation maximum, proving global uniqueness. Substitution gives (1-z)^2/(2(2-z)), and endpoint comparisons/limits follow from elementary inequalities and Taylor series. Independently expanded characteristic functions and re-expressed hyperbolic terms in exponentials for symbolic equality checks; finite quadrature claims in the package are corroborative only.

## originality

PASS

Best-knowledge originality of exact unique interior Gaussian minimax over all unknown phases; general antithetic methods and sign-switch rules do not compute this scalar phase balancing.

## value

PASS

PASS. A phase-unknown heat Fourier observable has a natural two-dimensional cosine/sine covariance geometry, making worst-phase variance a motivated robust design criterion. A strictly interior unique correlation with exact minimax risk and a sharp contrast with antithetic/independent sampling is an actionable benchmark for coupled Brownian estimators, even though the Fourier multiplier itself is analytically known and generation cost not optimized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
