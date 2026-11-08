# Independent mathematical audit

## correctness

PASS

For whole-line Brownian motion generator D∂xx with transparent inactive point gate, symmetric gamma, Poisson position resets r to x0>0 leaving gate state unchanged, conditioned on incoming side at active absorption: first-zero Laplace modes a=sqrt(r/D), b=sqrt((r+2gamma)/D); no-reset inactive-origin ODE yields (b-a)/(b+a). Keeping the two gate states in renewal matrix R=r(rI-Q)^(-1) gives F_A=(1-z)(1-exp(-bx0))/4, F_I=F_A+exp(-bx0)/(2(1+z)); their stationary mean is P_-=[1-z+z²exp(-bx0)/(1+z)]/4, z=a/b. Algebraic derivatives give decrease with r and x0 and increase with gamma, with 0<P<1/4; as r,gamma->0 at r/gamma->c, P->1/[4(1+sqrt(c/(c+2)))]. Independently solved the six-condition left/right backward boundary-value system (not just copied renewal), matching exact expression to ~5e-16 at four separated parameter tuples. Principal qualifier: the closest published study states a simulation trend for initial-side capture vs gamma opposite to this analytic result; its discrete-time crossing procedure and pathwise definition must be reconciled. Independent continuum BVP and derivation support the mathematical claim, not unqualified numerical agreement with that publication.

## originality

PASS

Same-model Żbik–Dybiec–Capała–Palmowski–Sokolov paper develops total first-passage transforms and simulates incoming-side fractions in Section III.3 Figure5, but supplies no analytical closed form, exact conditional probabilities or joint weak-rate crossover. However its simulation description claims increasing gamma makes initial-side probability grow, in conflict with present opposite-side formula; this is retained as a substantive comparison risk rather than called confirming evidence. Other cited gating models use reflecting inactive targets or gate-redraw resets, where opposite-side mark is absent. Best-of-knowledge original analytic split result with unresolved prior-model discrepancy, not a claim of established numerical concordance.

## value

PASS

The opposite-side mark is a natural observable explicitly simulated in the earlier same-model paper but not supplied by its unmarked passage transforms. Exact sensitivity, conditional-state split, and noncommuting weak-rate/rapid-switching limits reveal different behavior of marked and unmarked observables and dependence on whether gate is reset. This precise fact can be used in transport experiments and model comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
