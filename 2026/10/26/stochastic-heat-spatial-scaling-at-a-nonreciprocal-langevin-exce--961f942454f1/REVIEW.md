# Independent mathematical audit

## correctness

PASS

The drift is triangular with eigenvalue -k_N<0, so the stationary centered Gaussian law is unique. Independently, its covariance solves C(i,j)=(D/k_N)1_{i=j}+[C(i+1,j)+C(i,j+1)]/(2k_N) with entries outside the chain set to zero. Iterating to each diagonal site (ell,ell) counts binomially many pairs of directed paths and yields the stated finite sum. For a pair of fixed offsets, d_N/sqrt(N) tends to |u-v| and the upper index divided by N tends to L=1-s. At r=floor(Nt), t>0, the binomial mass times sqrt(N) tends by Stirling to exp(-|u-v|²/(4t))/sqrt(pi*t); the damping factor tends to exp(-2*zeta*t). To check the small-index argument precisely, regard the rescaled sum as the integral of its step function, extended by zero after the last cell. For t>0, sqrt(N)/sqrt(floor(Nt)+1)<=t^(-1/2); the elementary maximal binomial atom bound and bounded near-critical damping give an integrable dominating function on a fixed bounded interval. Equivalently the discrete small-index error is O(sqrt(epsilon)+N^(-1/2)); this makes the cutoff wording in the proof precise. Covariance convergence gives exactly the finite-dimensional Gaussian convergence. The white-noise isometry and heat-kernel convolution give the coefficient D/sqrt(pi), the Fourier transform is 2D times the integral of exp[-t(omega²+2*zeta)] over [0,L], and the high-frequency tail 2D/omega² gives the increment coefficient 2D. The critical erfc formula follows by integration, and the three fixed-damping regimes follow respectively from the binomial generating function, central binomial asymptotics, and summation near the geometric endpoint. Negative fixed zeta is legitimate at finite L and positive k_N for large N. VERIFY.py was inspected, not executed: finite spot checks are not a proof of convergence. No function-space tightness follows or is claimed.

## originality

PASS

Pass is for the calibrated, jointly spatial and inverse-length-damped Gaussian limit of the stationary finite open chain. The finite covariance and the critical square-root variance growth both predate this record, and the stochastic-heat scaling exponents and limit family are classical in related processes. A later-dated indexed result gives essentially the same detuned kernel at a boundary-centered observation window, not independent evidence of earlier priority. The inspected earlier statements do not give the joint finite-chain stationary limit with mesoscopic separations and this detuning.

## value

PASS

Uniform Hurwitz eigenvalues coexist with much larger stationary bulk noise as chain depth grows. The exact mesoscopic joint law quantifies when two sites decorrelate, how the downstream noise depth sets the effective stochastic-heat time, and how inverse-size detuning changes the correlations rather than only the one-site variance. Those observables are useful in this natural directed model even though the finite covariance and critical variance exponent were known. No general universality, entropy-production theorem or continuous-function convergence is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
