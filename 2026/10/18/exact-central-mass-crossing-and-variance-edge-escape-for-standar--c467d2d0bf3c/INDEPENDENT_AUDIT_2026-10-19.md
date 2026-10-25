# Independent mathematical audit

## correctness

PASS

With X_nu=sqrt((nu-2)/nu)T_nu, the exact density f_nu has log-ratio L_nu(z)=constant+z/2-(nu+1)/2 log(1+z/(nu-2)); L_nu'(z)=(z-3)/(2(nu-2+z)). Thus one strict density-ratio trough occurs at z=3. Writing X_nu=sqrt(V)G with V=(nu-2)/Q, Q chi-square nu and E V=1, strict Jensen for V^-1/2 shows f_nu(0)>phi(0); total density normalization forces the trough negative; polynomial Student tails force L_nu(z)->infty. Hence exactly two positive density crossings a_nu<sqrt3<b_nu, signs +,-,+. D_nu'(r)=2(f_nu(r)-phi(r)), D_nu(0)=D_nu(infty)=0 and tail sign yield a unique D zero R_nu in (a_nu,b_nu), positive before and negative after. For epsilon=nu-2->0, distribution X_nu->0 in probability, so R_nu->infinity. Exact density integration gives survival Student A_nu epsilon^(nu/2)r^-nu(1+O(epsilon/r^2)), A_nu->1/4; equating with Mills normal survival implies R²=nu H+2(nu-1)log R+2log[1/(A_nu sqrt(2pi))]+o(1), H=log(1/epsilon). Self-consistent R²~2H yields 2H+log(2H)+log(8/pi)+o(1). Large-nu correction 1/(sqrt3 nu) follows algebraically from prior Ouimet density expansion and is not presented as new. Independent survival-function root solving, carefully avoiding catastrophic 1-CDF subtraction, located roots at nu=2.001 (4.1860), 2.01 (3.5527), 3.5 (2.00843), 50 (1.74393), 300 (1.733984), consistent with both endpoints. Finite checks supplement sign and tail proofs.

## originality

PASS

Best-of-knowledge PASS for uniform all-real-nu unique central-mass sign crossover and sharp variance-boundary escape constant, not for the known Student density or Ouimet large-degree expansion. Inspected Ouimet 2022 complete 9-page local density/survival approximation source and identified its large-nu scope; it does not address nu downarrow 2 or prove the global all-degrees unique central mass zero. Resultary searches found related one-sigma Student/F statistics and Gaussian approximations, none of which yields the particular crossing law; an unindexed general mixture comparison theorem remains plausible for uniqueness, but not known to entail boundary asymptotic.

## value

PASS

The Student family passes through a finite-variance boundary where the variance-one law concentrates in probability but retains rare huge tails. A unique switch from excess central probability to deficit, together with an exact log-log escape and additive constant, quantifies a nontrivial competing concentration/tail regime; it is relevant to Gaussian-vs-heavy-tail approximation beyond a routine fixed-radius expansion. It does not assert monotonic R_nu or stronger stochastic order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
