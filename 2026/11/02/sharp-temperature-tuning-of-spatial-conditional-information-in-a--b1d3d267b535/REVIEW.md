# Independent mathematical audit

## correctness

PASS

The stationary v–force cross moment of each nonzero mode is (gamma a/tau)/(gamma+1/tau+k tau); the v-variance balance adds this moment divided by gamma to t. The zero mode has the same velocity limit and does not require a stationary displacement. For t>0 the reciprocal spectrum is 1/t−(a/t²)/(H−B cos q); Fourier inversion gives r^{|j|}/Delta for the latter resolvent. At t=0 the reciprocal is degree one in cos q. For the split into the selected pair and its complement the uniformly positive covariance has a bounded invertible complement block; Gaussian projection on the closed span of the remaining velocities gives the Schur complement, whose inverse is exactly the pair restriction of J. Thus −J_n/J_0 is the conditional correlation, positive and strictly less than one when t>0. In the strictly increasing r coordinate, the factor multiplying r^{n−1} is (r_0−r)(1/r_0−r)/(2(alpha−r)); its log derivative is negative for n=1 and the full log derivative for n≥2 is strictly decreasing from +infinity to −infinity. Increasing n adds 1/r, so the root moves strictly right. The root equation gives n(r_0−r_n)→r_0; H'(r_0)=−sqrt(A²−B²)/r_0 and the smooth factor after division by r_0−r tends to 1. This gives the linear t_n coefficient and the e^(−1)/n peak correlation, and the Gaussian log formula then gives the peak information. Checked the proof independently; the finite-ring and mode checks described in the frozen files were inspected as code and not executed or treated as an all-distance proof.

## originality

PASS

Pass for the exact distance-dependent optimization of two-site conditional information with all other velocity sites conditioned on: existence, uniqueness, strict ordering and coefficient-level peak and temperature asymptotics. The input covariance is published; inversion and the generic loss of a sparse precision pattern under additive white noise are not independent novelty. No inspected earlier statement covers the distinctive optimizer result under the exact Gaussian AR(1)-plus-white-noise equivalence. This judgment is bounded by the cited access and search limits.

## value

PASS

Ordinary nonzero-lag pair covariance is blind to the thermal contribution, yet conditional dependence changes from local to dense and displays a unique intermediate-temperature peak at every nonadjacent distance. The strict optimizer ordering and simultaneous sharp scales for temperature and peak give a natural quantitative classification beyond a routine Fourier inversion. The claim is about the equal-time infinite Gaussian velocity field, not finite-ring optimization, displacement stationarity, or entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
