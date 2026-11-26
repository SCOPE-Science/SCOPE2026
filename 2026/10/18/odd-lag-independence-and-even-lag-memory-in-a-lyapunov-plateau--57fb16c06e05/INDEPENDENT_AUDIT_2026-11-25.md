# Independent mathematical audit

## correctness

PASS

The prior Appendix A densities are for the specified acip, not an arbitrary invariant probability. An independent stationarity check is to split density intervals at 0, send each constant-density interval through the appropriate affine branch, and divide its height by the absolute slope. For 3<beta<4 the resulting signed jumps, scaled by 18 and listed at the frozen breakpoints, are (1,1,2,2,−4,−2); the extra candidate jump at 4−beta is −1+2+2−3=0. For 4<beta<9/2 the jumps scaled by 54 are (2,1,2,1,2,4,2,−8,−2,−4); the extra jump at 3beta−12 is −5+6+6−7=0. These are precisely the input jumps, so the density is invariant; the same check allows collapsed intervals at beta=3,4. Direct integration gives mass 1 and positive mass 2/3 in both chambers and at these endpoints. The event J0=J1=1 is 0<X<beta/2, with masses (beta+4)/18 and (beta+20)/54, yielding the stated slopes on subtracting 4/9. The plateau Lyapunov value is prior; the stationary average of log |T'| reproduces it. At 4 the four cell images are B, C, C∪D, A∪B; conditional uniformity survives each cell transition, establishing the Markov property rather than just a one-step matrix. With cell weights (1,2,4,2)/9 and u=3v=(−2,−2,1,1), Pu=(−2,1,1,−2), P²u=−u/2, and the weighted product of u and Pu is (4−4+4−4)/9=0. The norm of v squared is 2/9; parity iteration gives all lags. For Bernoulli pairs zero covariance is pairwise independence, and the only possible initial point for three zeros is −4, which has zero measure. Replay: the branch pushforward jump check and RESULT.md lines 54–127 with Appendix A. CHECKER.py and VERIFICATION.md were inspected, not executed; finite-lag comparisons do not establish the infinite-lag claim. The retrieved primary PDF labels the matching density passages (A.11)–(A.15), rather than the frozen numbering.

## originality

PASS

The same map, piecewise densities, positive branch mass and Lyapunov plateau are prior. The same lower-parameter lag-one expression is also obtained directly from the prior density for 2<beta<3. The supported distinct result is the sign transition across 4 together with its complete all-lag parity law. The cited primary statements and bounded catalog searches do not cover that combined claim.

## value

PASS

The branch threshold is intrinsic to this plateau example. The calculation exposes sign-changing memory hidden by a fixed Lyapunov exponent and constant marginal. The distinguished parameter is selected by the lag-one sign law, not an arbitrary sample, and the exact all-lag result separates infinitely many independent odd-separated pairs from persistent even-lag dependence and failure of joint independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
