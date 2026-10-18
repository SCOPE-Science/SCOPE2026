# Independent mathematical audit

## correctness

PASS

The source equation (20) defines Phi_Q^w(u)=-(2(1-u)^2)^{-1} integral_u^1 w(Q(p))(1-p)^2 q(p) dp. The source Theorem 7 states X<=disp Y and w1 decreasing, w1<=w2 imply Phi_X>=Phi_Y. With Q_X=p,Q_Y=p+2 and both quantile densities=1, all interquantile ranges coincide and the weights are equal, nonnegative, integrable and strictly decreasing. But Phi_Y=e^{-2}Phi_X while Phi_X<0 (the defining positive integrand gives the strict sign), hence Phi_X<Phi_Y for EVERY u in (0,1). Independent exact antiderivative e^{-u}(u^2+1)-2/e checks the integral. Source proof incorrectly invokes X>=st Y from dispersive order without endpoint/location condition; in example X<st Y. This is symbolic, not sample-based.

## originality

PASS

Theorem 7 is the actual recent printed target. The paper itself notes weighted extropy is not translation invariant, and standard dispersive-order references establish interquantile equivalence under shifts. Nonetheless, no inspected earlier article states this specific failure of the printed 2026 theorem, which combines those facts incorrectly. The result is a new concrete published-theorem counterexample, not a claim to invent translation sensitivity or dispersive order.

## value

PASS

An exact analytic counterexample invalidates a recently printed stochastic-order theorem under its own hypotheses for every residual quantile u. It identifies a substantive missing location condition and prevents unsound reliability comparisons; the value is theorem correction, not an arbitrary inexpensive negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
