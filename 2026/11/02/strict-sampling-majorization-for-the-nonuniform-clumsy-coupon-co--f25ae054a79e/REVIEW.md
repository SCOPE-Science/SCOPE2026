# Scientific review: nonuniform clumsy coupon collection

## Correctness — PASS

The transition kernel follows from independent rate-weighted Poisson refresh clocks. Strong Markov factorization of the empty-to-full and full-to-full resolvents gives the exact probability-generating function with \(z=(1+s)^{-1}\). Its linear expansion at \(s=0\) gives the mean after finite expectation is justified by a uniform positive-probability success block. The pair-factor decomposition gives a strict pointwise transform inequality under nontrivial balancing, and a positive exact mean gap. The local tangent Hessian is positive. The included exact-rational checker passed 394 assertions comparing a separately constructed absorbing Markov chain and the analytic formulas; these finite checks do not substitute for the general proof.

## Originality — PASS, provisional

Attrill–Garoni (arXiv:2605.14206v1) treats the clumsy process under **uniform** sampling, providing its PGF and expected time. Long (arXiv:2605.14511v1) studies uniform clumsy entry flux; its unequal-probability section concerns **global resets**. The older unequal-probability classical collector is the no-loss boundary and its special-case facts are explicitly credited. Kleiner's 2026 fragile collector has losses only before first discovery; its Schur order is for meeting deadlines, not repeated local losses. Published research comparisons supplied no matching arbitrary-weight strict PGF order. The most material remaining risk is indirectly covering results for random-scan heat-bath chains, and the publisher's 429 response limited full direct access to the fragile article. These limits prevent a claim of definitive historical priority.

## Mathematical value — PASS

Sampling weights are a physically meaningful model parameter, not an arbitrary finite slice. The theorem resolves a natural design question for all finite dimensions with common selected-type loss. It strengthens mean optimization to strict transform order and gives exact integral and quadratic heterogeneity costs. The finite formulas could inform selection-policy comparison and perturbation analysis, without relying on unproved downstream performance claims.

## Limitations and independence

All results assume strictly positive sampling weights, common \(p\in[0,1)\), the all-absent initial state and first all-present hitting. No usual stochastic-order claim, type-specific loss theorem, or independent validation is made. Source comparisons are same-review assessments and do not constitute an external priority certification.

Self-review: passed. Independent audit: not yet performed.
