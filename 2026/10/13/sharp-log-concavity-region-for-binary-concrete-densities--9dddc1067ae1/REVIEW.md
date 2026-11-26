# Independent mathematical audit

## correctness

PASS

The CDF has endpoint limits 0 and 1 and differentiates to the stated density. With h=x(1−x), u=2x−1, and v=2F−1, differentiating (log f)'=(u−τv)/h gives 2h²(log f)''=(τv−u)²−(τ²−1). This gives strict log-convexity for τ<1 and singles out uniformity for log-concavity at τ=1. For τ>1, midpoint curvature forces |a|≤b, where a=(log α)/2 and b=arcosh τ. Sufficiency is not a midpoint extrapolation: monotonicity in a and reflection reduce it to H_b(s)=τ tanh(τs−b)−tanh s≥−r, r=√(τ²−1). For (tanh s−r)/τ≤−1 this is automatic; on the remaining interval the inverse-tanh comparison has derivative 2τr tanh(s)/[τ²−(tanh(s)−r)²], negative to the left of s=0 and positive to its right, with minimum value b at 0. This includes the bias endpoints. Solving cosh(a)≤τ gives both equivalent thresholds. Independent exact differentiation at (τ,α)=(2,100) gave 68808/10201. Inspected verify_concrete.py without running it; its rational sample signs are not needed for the universal implication. The scope is the original x-scale, scalar two-category density.

## originality

PASS

The distinct supported claim is the sharp global two-parameter log-concavity region on the original x-scale, including necessity and sufficiency. The low-temperature log-convexity and distribution family are prior art. The available competing Concrete assertion is either an unqualified false extension or, if read as referring to the symmetric plot, a restricted case. No inspected statement supplies the full threshold; priority under the older distribution names is not certified.

## value

PASS

This is a necessary-and-sufficient shape decision rule for a standard distribution on its original support. It identifies precisely how strong asymmetry forces the required temperature upward, resolves the symmetric versus biased distinction in an existing shape assertion, and does so globally rather than giving only a counterexample. No gain for multivariate Concrete or for any downstream algorithm is presumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
