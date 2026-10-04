# Review

## Correctness

PASS. Reversal sends the maximum to \(S-m\) without changing the terminal value. Global sign change sends the maximum to \(-m\) and the terminal value to \(-S\). For odd \(g\), these two distributional identities imply
\[
\mathbb E[M g(S)]
=
\mathbb E[(S-m)g(S)]
\]
and
\[
\mathbb E[M g(S)]
=
\mathbb E[m g(S)].
\]
Eliminating the minimum gives the factor \(1/2\) exactly. No independence or exchangeability enters this argument.

The iid variance specialization is immediate. The correlation limit uses only the standard functional central limit theorem, the Brownian maximum law, and moment uniform integrability under the stated \(2+\delta\) assumption.

## Originality

PASS, with a deliberately narrow novelty claim. Classical Spitzer theory already determines the iid joint maximum/endpoint law, so the iid covariance formula is treated as prior-covered context rather than as the originality claim.

Heinrich's full public text was inspected because it explicitly targets a weaker dependence setting. Its posted correction says that the proposed cyclic-exchangeability proof actually requires independence. The present proof works for a different and strictly weaker symmetry specification: only reversal invariance plus global sign symmetry are used, and the checker supplies examples that are not exchangeable.

Anis--Gharib concerns marginal moments of maxima under exchangeability. Blanchet--Glynn concerns maximum and ladder-height asymptotics for iid random walks. Neither inspected statement gives the odd-transform identity under the two-involution hypothesis.

## Value

PASS. Maximum and endpoint are the two most basic finite-horizon summaries of a random walk path, and their joint law is central in fluctuation theory, barrier problems, and lookback-type functionals.

The result identifies a surprisingly rigid mixed moment that survives far outside the iid setting. The odd-transform family and the exact zero covariance of range with every odd endpoint transform show that the phenomenon is a path-symmetry law, not an accident of Gaussian or simple-walk calculations.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK orbit_identity_checks=36 nonexchangeable_checks=3 iid_cov_checks=38 asymptotic_checks=12`.
