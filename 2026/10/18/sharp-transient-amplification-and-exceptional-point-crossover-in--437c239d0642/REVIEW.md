# Independent mathematical audit

## correctness

PASS

For the stated dimensionless matrix, direct multiplication gives A²=−k²I, tr A=0 and ||A||_F²=2+2h². The undamped exponential therefore has determinant one and squared Frobenius norm 2+4h²(sin(kτ)/k)², including its linear-in-τ Jordan form at k=0. These fix both singular values and the displayed arsinh norm. When r≥h, arsinh and |sin| bounds give log gain ≤(h−r)τ and the maximum one. For r<h, on the first half-wave the log derivative equals −r+h cos(kτ)/sqrt(1+(h/k)² sin²(kτ)). The derivative of the second term has sign −sin(kτ) there (its positive denominator and factors do not vanish), so there is exactly one critical point, in the first quarter-wave. Every later half-wave repeats the same undamped norm with a strict damping penalty. Solving for the tangent at the critical point and inserting the corresponding sine yields the stated t* and G. At k=0 the derivative is −r+1/sqrt(1+τ²), supplying the Jordan limits directly; the h=0 case is just decay. With r=sk one has v²=1−(1+s²)k² and k²+r²=k²(1+s²), giving both limits and the stated scaling. Differentiating log Ψ cancels the rational terms and leaves −arctan(1/s); the endpoint limits are 2 and 2/e with the specified rescaling.

## originality

PASS

The gain onset is precisely the known numerical-abscissa threshold for this model, and neither the exceptional point nor the two-dimensional trace/determinant method is new. The supported distinct contribution is the quantitative all-time profile/unique peak and the joint approach with fixed r/k and their exact limiting functions. The strongest inspected statements did not supply this optimization and crossover together or a general result that directly subsumes them. Makris's relevant full paper and the model supplement could not be compared; neither access issue was used as evidence of novelty.

## value

PASS

An onset threshold says whether there is amplification but not how large it gets nor how long that takes. The exact optimum answers both and distinguishes two physical scales near the defective line. In particular the crossover quantifies gain of order 1/k for r/k fixed, recovers saturation at 2 for the rescaled weakly damped gain, and gives the distinct damped Jordan coefficient 2/e at the other endpoint. The peak and moving-parameter limit are useful even though elementary matrix identities supply the norm calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
