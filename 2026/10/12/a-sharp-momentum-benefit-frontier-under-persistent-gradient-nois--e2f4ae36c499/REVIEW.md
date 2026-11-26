# Independent mathematical audit

## correctness

PASS

For z=a x the heavy-ball polynomial is λ²−(1−t+β)λ+β. The Schur conditions 1−β>0, t>0 and 2(1+β)−t>0 all hold, as does r<1. The augmented system is therefore stable, the initialization contributes no limiting mean square, and the stationary comparison requires only the innovation variance. I independently eliminated ξ to obtain an AR(3) for z with coefficients (h+r, −β−rh, rβ), h=1−t+β, and innovation variance t²σ². Solving its lag-one through lag-three Yule–Walker equations symbolically and substituting into the lag-zero equation reproduces the proposed variance difference, including the factor −2βtσ² multiplying Q and the positive denominator (plus the x=z/a scaling). Replay: /workspace/independent_checks.py, momentum; the example differences are −1/30 and 446/7095. Q is convex in β, strictly negative at β=1, and has constant coefficient C=rt²+(1−r)t−(1+r). If C≤0 the chord places Q strictly below zero inside (0,1). If C>0 there is exactly one crossing there, the smaller quadratic root for r>0 and t−1 at r=0. The derivative of C in t is positive; C(1,r)=−r and C(sqrt(2),r)=(sqrt(2)−1)(1−r), while ∂C/∂r=t²−t−1<0 along the root. This gives the claimed boundary equality behavior, strict monotone threshold and limiting endpoints, without a Gaussian assumption or optimization over t.

## originality

PASS

The admitted overlap is exact white-noise covariance and its fixed-step comparison, plus a distinct indexed curvature-matched t=1 comparison. The supported distinct claim is the all-t, positive-AR(1) sign and threshold classification. The strongest colored covariance framework provides a way to calculate variance, not a previously derived inequality or an explicit closed comparison on this domain.

## value

PASS

At fixed step and objective curvature, changing only temporal persistence can reverse whether momentum helps. The exact classification turns that phenomenon into a design criterion: below the persistence-dependent threshold no positive momentum helps at all, while above it a single crossover determines the allowable interval. The criterion and its strict boundaries add scientific information beyond either a general covariance formula or the single reversal example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
