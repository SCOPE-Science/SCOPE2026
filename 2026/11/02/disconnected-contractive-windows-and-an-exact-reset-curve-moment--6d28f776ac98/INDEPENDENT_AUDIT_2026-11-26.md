# Independent mathematical audit

## correctness

PASS

Subtracting the current Gaussian term gives Y'=AY+s(A+1)χ with s²=h/2 and fresh iid pairs independent of the past. A coupled difference is multiplied by successive A's. A zero multiplier contracts in finite time almost surely. Otherwise the log growth is half the log of |P_q(t)| for P_q=1−2t+(1−q²)t². Positive growth excludes decay. At zero growth the two log magnitudes are either both zero, giving constant magnitude, or opposite nonzero values, giving a recurrent symmetric random walk that returns to product magnitude one infinitely often; thus the endpoints really are excluded under the stated decay definition. Solving −1<P_q<1 gives the two windows, with t>2 throughout the second. In the strict windows the causal affine series converges (exponential multiplier decay against subexponential innovations), and coupling to it gives unique stationary law. The positive additive innovation variance forces E[A²]<1 for finite second moment; conversely the affine series converges in L² there and yields the stated h(2−t)/(1−E[A²]) and bias. At t_ms, |P_q|<1 and t_ms is left of the parabola vertex, so it lies strictly before t_−. The larger reset zero t=1/(1−q) is to the right of the vertex and hence in the second window. The run of k successive −R multipliers since the last zero has probability 2^−(k+1); from initial Y variance s², iterating v↦R²v+(R−1)²s² and adding fresh s² gives h(R^(2k+1)+1)/(R+1). The absolute-moment summands are comparable to (R^p/2)^k, including divergence at equality and cutoff 1/3 at R=8. The phrase infinite variance is understood as failure of finite second moment, not a claim that the mean always exists. No conclusion about existence of stationary laws outside the windows is needed. The independent script (python3 /workspace/review_checks.py, reset) directly propagated the coefficients of the reused noises in Z and matched 63 exact rational conditional variances at three q values. The frozen verifier was inspected, not run; such finite checks are not evidence of infinite-horizon divergence.

## originality

PASS

The distinct contribution is the specific disjoint almost-sure stability windows with the L² frontier and the exact Gaussian mixture along the higher-step reset curve for recycled-noise SGLM. Neither SGLM itself, the general affine contraction mechanism, nor the general possibility of a heavy-tailed stochastic iteration is new. Bounded primary and indexed comparisons did not establish equivalent coverage of the joint exact finding. No historical priority is certified.

## value

PASS

The two scalar windows and exact cutoff distinguish synchronous contraction from variance stability and trustworthy sampling, even when every sampled quadratic is strictly convex. The later stable window is entirely outside full-gradient linear stability and has no finite second moment; its closed reset distribution is a concrete analytical benchmark, not a generic large-step recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
