# Independent mathematical audit

## correctness

PASS

The repaired theorem retains the frozen Finding. In frozen RESULT.md lines 80–82 the relative error O(exp(-at)) is false for a>1: at lambda=a the normalized error is asymptotic to -exp(-t), from the numerator of h. The repair keeps that numerator exactly and factors the denominator as 1-delta, delta=(1+lambda-2 lambda exp(-t))exp(-lambda t)/2. On the whole compact rate interval, delta=O(exp(-at)) and its lambda derivative is O(t exp(-at)) at late times. Thus the relative error is O(exp(-min(a,1)t)), and the log derivative is 1/lambda+1/(1+lambda)-t+O(t exp(-at)), strictly negative uniformly for large t. The three relevant forward equations have no incoming paths from other states; integrating them gives the stated masses. Pair weighting gives W1=2A+D and W2=2B, so the ratio B/W1 gives the covariance comparison under the W1-weighted law. It has lambda derivative t+O(t^2) uniformly at early times. The weighted law remains nondegenerate, so the two-draw covariance identity gives strict signs even for discrete or singular mixtures. Both masses are positive for finite t>0, and continuity yields existence, not uniqueness, of an equality. Complete corrected RESULT.md and VERIFICATION.md are in repairs/5. Bounded independent replay: python3 /workspace/check_frozen_mathematics.py 5 (NumPy/SciPy matrix exponential and Decimal). Three discrete laws give opposite signs at t=0.03 and 12; at lambda=2 the old relative error multiplied by exp(t) tends numerically to -1. The computations do not establish the universal assertions; the repaired analytic proof does. The verification notes distinguish the 126 transient comparisons from other assertions.

## originality

PASS

The supported distinct claim is strict eventual reversal of the early count ordering for this transient pair-weighted observable, uniformly in the sense of eventual sign for each nondegenerate compact positive rate law. Early apparent nonlinear bias from heterogeneity and the broader caution about extrapolation are not new. The correction to the remainder does not alter the finding or the comparisons.

## value

PASS

The three-person group is the smallest with both relevant infectious counts and remaining susceptibility. Strict reversal for all nondegenerate compact positive mixtures is a structural distinction between pooled conditional association and the underlying linear hazard, not just an example or failure of a short-time approximation. It sharpens how a calibration time can affect inference in a precisely defined statistical model. Late at-risk pairs may be very rare; the finding is not a claim about empirical estimability or actual epidemics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
