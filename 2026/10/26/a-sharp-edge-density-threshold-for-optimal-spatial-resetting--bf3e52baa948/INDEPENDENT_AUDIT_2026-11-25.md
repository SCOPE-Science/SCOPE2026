# Independent mathematical audit

## correctness

PASS

With k=sqrt(r/D), renewal gives mean excursion duration (1-I_d)/r and success probability I_d=e^{-dk}G_p(k); the MFPT is their quotient. G_p(k) is the lower incomplete-gamma transform and is asymptotic to Gamma(p+1)/(Bk)^p. In (I_d^{-1}-1)/(Dk²), the subtraction introduces only relative factor 1-I_d tending to 1 uniformly for d>=0 as k grows. Small k diverges at least as T_0, and for d>0 large k diverges, proving compact attainment. If 0<p<2, let a=2-p. The trial k=a/d gives an O(d^a) minimum, excluding all bounded k by positivity of T_0 and its small-k divergence. For all minimizing sequences the rescaled objective is asymptotic to B^p/(D Gamma(p+1)) times e^v/v^a with v=dk. This diverges at both endpoints, so v remains in a compact interval and comparison with the trial forces v to the unique minimizer a. This gives both constants. For p>2 T_0 diverges at large k. For p=2 the exact transform gives T_0=B²/(2D)-1/(Dk²)+o(k^{-2}), i.e. below the tail limit at a finite k. Evaluating at that fixed k and using T_d>=T_0 excludes the entire large-k tail for small d. Continuity on the resulting common compact interval and comparison with every fixed k show every accumulation point optimizes T_0. The last successful excursion has the tilted offset density proportional to u^{p-1}e^{-ku}; k times that offset is a Gamma(p,1) truncated at Bk, converging in total variation. Dividing by dk tending to a gives the asserted Gamma(p, rate a) law for offset/d.

## originality

PASS

Credit the prior general distributed-reset MFPT transform and exponential successful-launch tilt, and the closely related exact uniform p=1 formula and stationarity equation. The supported distinct contribution is the all-global-minimizer edge-gap asymptotic over the subcritical power-law family, the finite-rate retention including p=2, and the launch-law limit coupled to that optimizing gap scale, not the renewal or tilting formulas themselves.

## value

PASS

A natural change in near-target launch density separates regimes with diverging and retained optimal reset rates. The critical exponent cannot be resolved just by the leading tail power because the critical limiting MFPT is finite; the endpoint proof identifies the strict finite-rate advantage for the exact law. Control of every global optimum, asymptotic constants, and the successful-launch law on the physical gap scale are useful beyond merely plotting minima or finding a candidate stationary rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
