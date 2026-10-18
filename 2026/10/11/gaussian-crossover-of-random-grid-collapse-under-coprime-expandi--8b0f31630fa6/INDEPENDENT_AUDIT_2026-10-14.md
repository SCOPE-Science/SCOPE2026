# Independent mathematical audit

## correctness

PASS

For a given word with k maps ×a and t−k maps ×b, the multiplier is a^k b^(t−k); the image of Z/(ab)^n is the uniform cyclic subgroup of cardinality (ab)^n/gcd((ab)^n,a^k b^(t−k))=a^((n−k)_+)b^((n−t+k)_+). Its centered CDF sawtooth has mean-subtracted variance 1/(12M²), so D=1/(M√12) exactly, including t=0 and M=1. Collapse means k≥n and t−k≥n, giving the exact finite-time binomial sum. For t=floor(2n+s√n), p_n=1/2+β/√n, triangular-array CLT gives (K_t−n)/√n⇒s/2+2β+Z/√2 and the complementary count gives s/2−2β−Z/√2. The continuous-mapping theorem on positive parts proves the claimed log profile. Indicator continuity away from Gaussian boundary proves the Bernoulli weak limit for s≥0; for s<0 collapse is impossible. Monotonicity of collapse yields τ limit |4β+√2Z|. At fixed p≠1/2 the minority selections arrive by a sum of n geometric waits, with mean n/q and variance n(1−q)/q²; at that time the other count exceeds n with probability tending to 1. None of the finite enumerations supplies the n→∞ step.

## originality

PASS

Guihéneuf–Monge’s centered Cramér metric and generic finite-time discretization theory are directly acknowledged. Their asymptotic regime fixes iteration time while the grid mesh shrinks and treats generic smooth expanding maps and rounding; the present exact arithmetic resonant family instead needs t≈2n, arithmetic grid (ab)^n, and a random switching bias of order n^(-1/2). Standard binomial and negative-binomial CLTs cover count fluctuations but do not state their coupling to the exact image-subgroup discrepancy or the two-regime crossover as a theorem. The Resultary top hit is this audited record itself and is not an independent source of prior coverage.

## value

PASS

The exact centered Cramér observable for a deterministic exponentially fine grid under a shared random composition gives an analytically sharp crossover between two different hitting-time universality regimes, with the universal folded-normal collapse and slope-dependent logarithmic profile separated. The resonant integer map grid explicitly lies outside the standard generic-rounding approach and supplies a natural tractable benchmark; the result is not claimed to create the underlying binomial CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
