# Independent mathematical audit

## correctness

PASS

Split on whether a Poisson reset occurs during lag t; independence after a reset gives exact C(t)=exp(-r*t)Cov(g(A),g(A+t)) for stationary A~Exp(r). Since g(a)=T0∫w_q(s)e^-sa ds (Gamma density), Cov(e^-sA,e^-uA)=[r*s*u]/[(r+s+u)(r+s)(r+u)]>0. Tonelli yields strictly positive AC exponential density W(r+s), all moments finite; differentiation gives strict complete monotonicity. As s->0 W(r+s)~[T0*tau^q*mprime(r)/Gamma(q)]s^q, where mprime(r)=T0∫w_q(u)u/(r+u)^2 du>0. Watson/Laplace asymptotics give C~q*T0*tau^q*mprime(r)e^-rt t^(-q-1), with one-order remainder; tilt of the positive density yields LambdaPrime=-Var_t(lambda)<0 and Lambda-r=(q+1)/t+O(t^-2). The q=2 mean derivative yields the stated exponential-integral coefficient, positive from the integral. Independently evaluated exponential-age covariance by adaptive quadrature at r=.7,tau=1.2,q=2: normalized exact/asymptotic ratios at t=5,10,25,60 are 0.2684,0.4673,0.7098,0.8595, consistent with approach to one and not treated as proof; the analytic Laplace argument establishes all t and every q.

## originality

PASS

The 2025 primary source Bodrova-Chechkin-Dubey establishes Poisson reset cooling, one-time PDF and moments but no fixed-rate two-time correlation spectral density or edge coefficient. Crucially, an earlier 2026-10-26 public same scalar age-process result explicitly DOES already prove the renewal covariance identity, positivity, integrated variance and weak-reset transitions; those ingredients are not novel. The audited work adds the positive completely monotone full relaxation-rate density, sharp fixed-r t^(-q-1) prefactor, monotone effective rate and identification. These do not follow as explicitly stated conclusions from the earlier integrated-variance formulas without a new spectral/Laplace derivation. Qualified best-of-knowledge PASS with overlap clearly recorded.

## value

PASS

The explicit relaxation spectrum, strict complete monotonicity, sharp polynomial correction to the universal exponential reset decay and recovery of cooling exponent from log-slope are motivated temporal-memory observables beyond previously known one-time distributions and weak-reset integrated variances. Exact positive density and q=2 cubic prefactor are meaningful self-contained analytic facts, not a mere reparameterization of an existing table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
