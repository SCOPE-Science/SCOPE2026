# Review

## Correctness

PASS. The sample mean and range are both decomposed over the two adjacent support gaps. Four elementary cut-indicator covariance identities give the displayed quadratic formula exactly. The sign argument then uses only the strict monotonicity of
\[
\phi_n(u)=(1-u)^{n-1}-u^{n-1}.
\]
When one endpoint has mass at least one half, all three quadratic coefficients have one strict sign. When both endpoint masses are below one half, the gap-ratio polynomial has positive constant term, negative leading term, and negative root product, hence exactly one positive zero. Direct exact enumeration reproduces the covariance formula.

## Originality

PASS, with an older order-statistics literature risk. Hwang--Hu's archive-era result treats independence of the sample mean and sample range as a normal characterization. Hu--Lin's complete later paper reproduces that result explicitly and develops more range theory, but does not give a three-point covariance sign phase diagram.

Searches using covariance, uncorrelatedness, sample mean, sample range, three-point distributions, fixed probabilities, and discrete support geometry did not locate the quadratic formula or unique support threshold.

The current deterministic sample-range inequality paper concerns order covariance between two ordered vectors rather than stochastic covariance of two statistics under repeated sampling.

## Value

PASS. The sample mean and range are the two statistics used jointly in classical location--dispersion monitoring, and their independence under normality is a characterization theorem. For discrete or categorical populations, independence is impossible in the normal-characterization sense, but covariance can still vanish. The result gives an exact and interpretable answer to when that happens: endpoint majority forces a robust sign, while otherwise there is exactly one geometric balancing point.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK enumeration_checks=3500 identity_checks=40000 sign_checks=39989 reflection_checks=40000 root_checks=26481`.
