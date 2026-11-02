# Scientific review: exact binomial-quantile allocation in a biased two-bin depletion race

## Correctness — PASS
The proof identifies a bounded first-emptying stopping time and extends the same independent bin-choice sequence to a fixed total of \(n\) draws. Conditional post-stopping binomial counts give the precise weighted positive-part expectation. Its forward difference is a binomial CDF minus \(1-p\), divided by \(p(1-p)\); strictly positive binomial atoms ensure a unique quantile crossing, with a precisely identified possible adjacent tie. For fixed \(p\), Berry–Esseen and uniform integrability justify the optimal-allocation and minimum-remainder asymptotics. The independent rational recurrence checker passes 7,074 assertions. No inference from finitely many tests to an infinite statement is used.

## Originality — PASS, subject to historical limitations
The most directly related full article is Correa et al., arXiv:2602.12523v2: its equal-probability theorem and its isolated unequal-probability example do not imply the present all-\(n\), all-\(p\) quantile characterization. Zhou, Wang and Zhang (2026, DOI 10.1287/opre.2025.2228) present a related symmetric terminal-inventory model. Their abstract and bibliographic material were examined, but the full text could not be inspected; possible undiscovered coverage is explicitly a residual priority risk. Standard newsvendor quantile optimality is not claimed to be new. The exact identification of the stochastic stopping objective with a binomial asymmetric loss is the essential new bridge. Targeted bibliographic and mathematical-claim searches found no directly covering result; a negative search by itself is not treated as proof of novelty.

## Mathematical value — PASS
Correa et al. demonstrate that proportional allocation need not optimize the unequal-selection problem, but provide no general two-bin optimizer. The present result gives a complete finite characterization for arbitrary bias, resolves ties, and quantifies the asymptotic direction, size, and residual cost of the bias correction. These provide usable structural and quantitative answers for the model's natural first nonsymmetric case, rather than a routine reparameterization or a single-instance numerical improvement.

## Closest literature and limits
Primary: Correa et al., *About a ball removal process on bins* (2026), https://arxiv.org/html/2602.12523v2, particularly Section 3. Related: Zhou et al., *Optimal Inventory Allocation for Indifferent Goods Under Dynamic Substitution* (2026), https://doi.org/10.1287/opre.2025.2228, public abstract only. The result does not treat three or more bins, state-dependent probabilities, or biases tending to zero or one with the total. Independent historical-priority assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
