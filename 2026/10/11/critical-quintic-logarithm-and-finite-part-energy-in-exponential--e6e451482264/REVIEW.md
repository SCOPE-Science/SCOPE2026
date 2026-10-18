# Independent mathematical audit

## correctness

PASS

The original ODE gives v''+beta v'=alpha v^p. Every positive trajectory eventually has v'>0; the exact phase relation (Y²)'=2alpha v^p-2beta Y yields Y~c v^q (q=(p+1)/2>2), hence dv/dt~c v^q and finite-time blow-up. Substitution derives d=-beta/(q+1) and e=beta²q/[2c(q+1)²] in Y=c v^q+d v+e v^{2-q}+R. The proof bounds R by O(v^{3-2q}) for 2<q<3, O(v^-3 log v) for q=3, and O(v^-q) for q>3, each integrable at infinity. Renormalized squared energy has derivative -2beta R, proving finite K and stated tail rates. For q=3, coefficient -3beta³/(16c) of log v was independently verified by SymPy, as were d²+2ce=beta²/(q+1) and the first-order Y coefficient. Comparing two positive phase velocities gives (Y2²-Y1²)'=-2beta(Y2²-Y1²)/(Y1+Y2), so the finite K difference is strictly positive by exact integration.

## originality

PASS

Ichida's primary study of this precise exponential-memory power F1 model proves finite blow-up and leading rates but not this explicitly renormalized energy and critical log coefficient. General multi-order blow-up methods of Asai et al. and Hoang give frameworks/leading errors, not the displayed model-specific K comparison. An indexed 2026 earlier memory-blowup invariant concerns a reciprocal-memory F2 nonlinearity, not the same phase equation.

## value

PASS

Dissipative memory destroys the undamped energy conservation; the exact finite-part correction recovers a trajectory invariant of the asymptotics. The p=5 logarithmic resonance separates two regimes and the positive K-order formula distinguishes trajectories at the same memory coordinate. These are motivated dynamic invariants rather than merely another leading blow-up exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
