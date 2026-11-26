# Independent mathematical audit

## correctness

PASS

Nonexplosive linear birth–death–immigration and the independent continuous renewal clock give a proper regenerative stationary law since ET=b/alpha; integrating the interval survival gives exactly the stated age tail, not the inter-reset tail. Substitution of Theta'=lambda+(lambda-mu)Theta and k=u/lambda verifies the forward PGF equation and its zero-state initial condition. Gamma mixing of the Poisson rate then gives the same PGF. Below criticality the ratio to the limiting negative-binomial mass has a factor [(1-x)/(1-qx)]^n with x=exp(-(mu-lambda)A) and bounded prefactor (1-qx)^(-k). Ages below (1-epsilon)log(n)/(mu-lambda) give an exponentially small ratio; above (1+epsilon)log(n)/(mu-lambda) it tends uniformly to one. The intermediate relative probability goes to zero on first letting n grow and then epsilon decrease, proving the local-mass equivalent with its constant. At criticality the product tail can also be checked directly: x^alpha E[(1+x/(b lambda G))^(-alpha)] converges by domination by (b lambda G)^alpha, whose expectation is the claimed Gamma ratio. Above criticality restrict G to [n^(-epsilon),n^epsilon], neglect its polynomially small complement, and use log(1+gn/(lambda G))/g as the age cutoff, where g=lambda-mu. Conditional Poisson Chernoff bounds at (1±eta)n transfer the two mixing-rate tails by regular and slow variation, respectively. Layer-cake summation gives the stated moment conditions including equality at criticality. These are analytic checks for fixed positive parameter tuples, not uniform through the critical point. The frozen checker was inspected, not executed; its reported finite residual and quadrature checks do not prove these asymptotics or constitute formal verification or expert attestation.

## originality

PASS

The age-mixture construction, BDI transition kernel and generic product-tail tools are established. The supported distinct result is the explicit tail comparison for this independent renewal-Lomax reset law, principally the subcritical local negative-binomial mass times the logarithmic age factor and its contrast with the critical and supercritical survival-tail equivalents. The critical formula is a standard product-tail specialization and is not independent novelty in isolation.

## value

PASS

The reset-free dynamical threshold provides a natural parameter split. The theorem explains why finite mean reset intervals guarantee a proper law but need not guarantee any positive occupation moment, and identifies a sharp measurable subcritical correction to the reset-free equilibrium. The common age mechanism produces three different tail classes with explicit constants, without asserting a result for interacting sites or general reset laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
