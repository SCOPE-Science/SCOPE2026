# Independent mathematical audit

## correctness

PASS

Conditional on X_n=x, the p-th moment reduces to a one-dimensional Gaussian integral with quadratic coefficient δ=1−phq(x), q=σ²x²/(1+x)³: it is finite iff δ>0. The maximum q(2)=4σ²/27 gives uniform subcritical all-iterate finiteness. The first-step log-multiplier is a strictly convex Gaussian quadratic with lower support below 2 for every x0, and yields a strictly positive density near x=2. Above critical phσ²=27/4, an open set of X1 values has infinite conditional p-moment. At criticality δ(x)=(x−2)²/12+O((x−2)³) and the finite-case conditional moment grows as exp(c/(x−2)²), nonintegrably against that density. Jensen propagates infinite moments for all n≥2. The underlying Lipschitz diffusion has finite finite-time moments. Independent symbolic identities and Gaussian quadratures passed 36 tests.

## originality

PASS

Independent statement/implication comparison including direct mathematical object parameters and available primary material: The one-step conditional moment Gaussian-MGF formula is classical and appears in the method paper Bréhier–Cohen arXiv:2608.25689 Proposition 9; novelty is the all-initial-state two-step critical reachability and nonintegrability, not the integrator or the one-step identity. A Gaussian integrability identity immediately gives the statewise first-step threshold but cannot alone establish universal blowup by step two at equality: this requires the exact support of first-step distributions, a quadratic vanishing deficit, and an unconditional singular integral. Distinguishes the sharp example from cited sufficient bound; inaccessible full paper may contain stronger implications.

## value

PASS

Exhibits a sharp and surprising finite-step numerical moment failure in a strictly positive high-order scheme despite globally Lipschitz coefficients and all exact SDE moments. Exact boundary and universal two-step reachability make the statement substantially stronger than a sufficient small-step estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
