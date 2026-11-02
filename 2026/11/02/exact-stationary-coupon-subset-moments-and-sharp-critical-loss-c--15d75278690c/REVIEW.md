# Scientific review

## Correctness — PASS

The specified post-loss transition is irreducible, aperiodic and permutation-invariant. For every fixed subset of size \(k\), stationary post-draw inclusion and independent survival give a scalar recurrence, solved by an exact positive product. Boolean-lattice inversion recovers the full count distribution. Smoothness of the continuous extension of the logarithmic summand justifies the uniform local Euler–Maclaurin/Taylor remainder at fixed \(c\), including the boundary and the \(p=c/n\) logarithmic correction. A monotone stationary coupling bounds every post-loss hit probability from empty by the full-state invariant mass. A separate label-discrepancy coupling gives uniform mixing error at most \(n(1-p)^t\); polynomial block lengths then show that the reciprocal stationary mass and mean first hit have the same exponential rate. The sign of the strict gap follows from monotonicity of the exponential secant slope. The finite-state verifier reproduced 688 assertions, but infinite claims are not inferred from enumeration.

## Originality — PASS, qualified

Cruciani–Dudeja (arXiv:2602.20705v1, Sections 2 and 4) specify this chain and provide one-coordinate marginals, metastability, an exact expected-time computation procedure, and broad bounds; they do not provide the displayed all-subset invariant product or sharp rate \(I(c)\). Long (arXiv:2605.14511v1, Section 5) gives the same-chain high-tail and hitting laws for **fixed** loss \(p\); the assumptions are incompatible with \(p=c/n\), and the stated asymptotic constant is not uniform in that regime. Attrill–Garoni (arXiv:2605.14206v1) study selected-label refresh, not independent global deletion. Independent published-record and targeted alternate-formulation searches found no directly dominating theorem. Historical novelty is an evidence-based assessment, not an assertion that all relevant past works were accessible: general immigration–thinning stationary formulas may be related, and a comprehensive independent priority audit remains open.

## Mathematical value — PASS

The first motivating paper identifies an exponentially long metastable completion regime under \(p=c/n\) but does not identify its exponent. An exact finite-subset stationary product, a sharp positive prefactor and a corresponding mean first-hit exponent resolve this natural quantitative gap. The strict inequality \(I(c)>\log(1+c)\) shows that an otherwise tempting independent-marginal model is exponentially incorrect, even though its one-point marginal is exact. This changes the principal critical-regime prediction and explains the dependence of rare simultaneous retention events.

## Scope and independent limitations

No exact hitting-time prefactor or exponential limiting distribution is claimed. The asymptotics assume fixed positive \(c\); the exact product allows arbitrary finite \(n\) and \(0<p<1\). Readable inspected sources support the quoted comparisons; older unindexed or generic thinning-queue theory could affect priority and has not received independent adjudication.

Self-review: passed. Independent audit: not yet performed.
