# Scientific review

## Correctness — PASS
The Markov transition matrix has trace \(u+vz\) and determinant \(-hz\), producing the exact finite-horizon recurrence. Positive initial and recurrence coefficients together with the sign-at-root argument yield \(n\) distinct negative zeros, in agreement with the published real-rootedness result. On the discriminant-negative interval \((t_-,t_+)\), the recurrence gives an exact cosine phase with strictly increasing angle \(\theta\), yielding \(n\)-scaled root counts in every interior interval. The phase increases by precisely \(\pi\); no asymptotic root mass can escape the band, and differentiation supplies the normalized explicit density. Exact-rational and numerical checks are supplementary only.

## Originality — PASS on inspected evidence
Dekking and Kong (arXiv:1102.3613, Proposition 4.2) **already prove real zeros** for the same negative-correlation parameter regime. This existing result and the corresponding Poisson-binomial representation are treated exclusively as prior work. Tang and Tang (arXiv:1908.10024, Theorem 4.1) prove/review the real-root equivalence; Xia and Zhang (arXiv:1001.2144) analyze approximation and stationary moments. In the materially inspected sections of these accessible primary texts, none specifies the weak empirical distribution, support, and density of the individual Bernoulli factors as horizon grows. Targeted title, alias, spectral-root, and parameter searches found no directly dominating formula. Residual risk: a classical theorem for zeros of second-order recurrences could imply this result as a special case even without mentioning Markov chains; full historical priority is not established.

## Value — PASS
For a dependent count distribution that is known to admit an independent-Bernoulli representation, the shape of those independent Bernoulli parameters is a natural unresolved quantitative descriptor. Determining its full limiting law, explicit support edges, and density is more informative than the known fact of representation or a moment bound; it supplies an exact large-horizon factor-parameter profile useful for distributional approximation and simulation. It is not a mere recomputation of a single small parameter case.

## Limitations
Fixed interior transitions and strict \(a+b>1\). No parameter-uniform results, finite-sample band containment, independent external certification, or full assertion of historical priority.

Self-review: passed. Independent audit: not yet performed.
