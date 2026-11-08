# Independent mathematical audit

## correctness

PASS

With dX=(sigma^2/2)Xdt+sigma XdW between rate-r resets to x0, log(X/x0) is driftless Brownian. For ages a and lag t conditional Gaussian signs have correlation h(a,t)=(2/pi)atan(sqrt(a/t)), strictly increasing in a. Equilibrium initial backward age E~Exp(r), fresh age at s is min(E,s), and future resets are independent. This coupling yields strict stationarity-versus-fresh lag-covariance ordering throughout every positive integration triangle, therefore V_eq(T)>V_fresh(T). Stationary sign correlation is erfc(sqrt(rt)); two-time integration gives the supplied erfc closed form. Fresh Poisson-excursion Dirichlet lengths and arcsine variance 1/8 give (z-1+e^-z)/(4z^2). Independent mpmath quadrature at z=0.1,1,5,30 agrees with each form and limits, including z^2 gap ->1/16 and small-time ratio 2. Bound strictly <1/4 via nondegenerate threshold fractions. Proof applies all positive r,sigma,T.

## originality

PASS

Qualified PASS only for the strict entire-window variance ordering between equilibrium-reset-age and fresh-reset preparation, the initial factor-two limit and sharp 1/(16z^2) excess. Fresh-reset arcsine occupation formulas and generic two-time resetting densities are acknowledged prior.

## value

PASS

A sharp natural preparation effect for time-averaged binary observables: strict variance ordering persists at every horizon and a quantitative 1/z^2 residual remains after the common 1/z leading variance. Finite variance of the indicator persists even where moments of the multiplicative level diverge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
