# Independent mathematical audit

## correctness

PASS

From stationary generator E[Xsigma]=a/(omega0^2+2 beta q+q^2) and E[X^2]=a^2(2 beta+q)/(2 beta omega0^2 M), the covariance satisfies C_second+2beta C_first+omega0^2 C=a^2 e^{-qt}/M and C_first(0)=0. Exact underdamped solution has K=a^2/(MH)>0, exponential e^-qt plus e^-beta t(A cos(Omega t)+B sin(Omega t)), with nonzero A,B. At q=beta, oscillation amplitude R=sqrt(1+3 beta^2/omega0^2)/2<1; for q<beta the positive exponential-covariance convolution identity yields C_q(t)>0. Critically/overdamped Green function is positive, giving positive twofold convolution. For underdamped q>beta nonzero sinusoid dominates faster exponential: infinitely many negative and positive intervals. Envelope time L_q=log(1/R_q)/(q-beta) brackets first negative lag within 2pi/Omega and proves the stated limit. Independently verified normalized stationary covariance IVP and critical R symbolically; inspected checker.py shows RK4 finite checks but it cannot prove universality. Exact witness beta=.5,omega=1,q=1 at t=2pi/sqrt3 is negative.

## originality

PASS

Best-of-knowledge novel exact all-lag covariance sign dichotomy and first negative-lag divergence, not new linear filter or stationary moments; directly matching Dutta et al model and its main/appendix results compared, distinct comparator of white-noise inertial OU also checked. Hidden earlier stationary colored-noise pole classification remains priority risk.

## value

PASS

Autocorrelation sign is a natural observable in inertial active particles: underdamping alone fails to force negative lags, while crossing telegraph decay rate q=beta changes global sign; delay divergence gives quantitative finite-recording detection scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
