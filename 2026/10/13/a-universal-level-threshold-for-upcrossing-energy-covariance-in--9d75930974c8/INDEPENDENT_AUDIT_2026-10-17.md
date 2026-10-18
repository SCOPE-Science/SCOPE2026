# Independent mathematical audit

## correctness

PASS

For n>=2, sigma>0 and -1<rho<1, standardize Y=X/sigma. Integrating the two bivariate Gaussian second-Hermite moments on {Y_i<=a<Y_{i+1}} gives L+R=phi(a){a(1+rho^2)(2Phi(h)-1)-2rho*sqrt(1-rho^2)*phi(h)}, h=a(1-rho)/sqrt(1-rho^2). The Gaussian Markov property propagates conditional centered squared moments by rho^(2 lag). Summing both directions across edges yields exactly sigma^2 phi(a)/(1-rho^2)*sum_{r=1}^{n-1}(1-rho^(2r)) times the bracket; the prefactor is positive. J(z)=(2Phi(z)-1)/(2phi(z)) increases strictly for z>0; a(1+rho^2)J(h)=rho*sqrt(1-rho^2) has one positive root for rho>0. J(h)>=h proves a_*^2<=rho(1+rho)/(1+rho^2) and the stated rho endpoint limits. At rho=0 the sign vanishes only a=0, and rho<0 the bracket is positive. Independent SciPy integration of the two truncated moments for six (a,rho) settings agreed with the closed pair expression to <1e-10; roots .1748628628 (rho=.03), .5273696943 (.25), .8737458924 (.7), .9827045844 (.95) obey the bound. The experiments corroborate but do not prove the continuous parameter theorem.

## originality

PASS

Best-of-knowledge distinct exact finite-discrete AR(1) upcrossing-count versus uncentered quadratic-energy covariance profile and sharp sign transition for arbitrary standardized level. Kratz gives Gaussian level crossing moments and Wiener-chaos framework, Sinn–Keller studies count/count zero crossings, and Di Bernardino–León–Tchumatchenko studies continuous-time cross-signal crossing correlations. The zero-level crossing/energy observation is explicitly prior; the nonzero threshold and sample-length independent sign map are the assessed addition. General Hermite projections might imply the calculation indirectly, and Sinn–Keller full text remained inaccessible via authorized routes.

## value

PASS

Counts of high-level upward transitions and accumulated squared magnitude are natural paired descriptors of correlated Gaussian discrete time series. The exact sign map gives the unique universal normalized crossover a_*(rho) independent of sample length and marginal scale, a substantive complete structural classification beyond one parameter case or a simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
