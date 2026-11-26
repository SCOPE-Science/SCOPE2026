# Independent mathematical audit

## correctness

PASS

With q=1−a the tracking formula first becomes nonnegative at n0=ceil(1/q), including the case of equality, and any bounded difference from the negative-time frozen branch eliminates the homogeneous term proportional to a^n. The continuation satisfies v[n+1]=b v[n]+n, b=1+δ, and is strictly increasing. Direct summation gives v[n]=(b^n−1−nδ)/δ²+c(b)b^n for δ>0 with c bounded at b=1; the neutral sum is n(n−1)/2. At h=√ε and δ/h→κ the convolution is uniformly a Riemann sum on compact rescaled time intervals; for δ=κh exactly, the kernel and grid errors are O(h). The derivative of Hκ at the threshold is strictly positive, so discrete bracketing gives the claimed limit and O(1) iteration error. Hκ increases strictly in κ for positive t and depends continuously on κ including at zero. For R=Lδ²/ε→∞, integers with n log b=log R±η+O(log b) have nδ=O(log R), and x[n]/L→exp(±η); rounding is negligible precisely because δ→0. This proves the additive-log limit without replacing log(1+δ) by δ.

## originality

PASS

The closest prior swept nonsmooth example is continuous time with fixed unstable rate; the closest discrete nonsmooth theorem is frozen-parameter divergence. Neither supplies the jointly scaled discrete passage law. The positive finding supported here is the finite-κ crossover with its iteration error and the near-neutral additive-log law, not logarithmic fold delay itself.

## value

PASS

This gives a quantitative benchmark at a motivated loss-of-hyperbolicity boundary of a swept border collision. It separates the neutral square-root time scale from the exponential-growth regime, locates the crossover, and retains the exact discrete multiplier in the additive-log law where a continuous-rate replacement can lose precision. It is a useful exact model result, not a universal tipping claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
