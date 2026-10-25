# Scientific review

## Correctness — PASS

Every edge equates its endpoints' successor sets by transitivity and right-Euclideanness, yielding a canonical partition into successor-row classes with one nonempty reflexive core each. Conversely every such decorated partition defines an admissible frame, with no overcount. Independent fair marking of an ordinary uniform partition, conditioned to meet every block, is exactly the desired uniform distribution. The elementary block-count argument shows its mean number of blocks is sublinear, and the conditioning event costs \(\exp(o(n))\) at every fixed interior mark density. Stirling's binomial approximation and a matching Chernoff upper/single-point lower bound give the two stated sharp logarithmic probabilities. Exhaustive checking through four worlds independently supports the finite reduction; no finite data are used as a proof of asymptotics.

## Originality — PASS (qualified)

OEIS A143396 (2008) already states the exact mark-count triangle and generating function; OEIS A143405 (2008 onward, with a relevant relational note in 2026) already gives the univariate count and structural interpretation; Kotěšovec (2022) gives sharp total-count asymptotics. **None is claimed as novel.** The reviewed contribution is exclusively the entropy-rate theorem for the random reflexive-core proportion, including the sharp bilateral tail rate. Targeted research-record and mathematical-literature searches for this statement and its interpretations found no equal-or-stronger published claim. This does not rule out an older general conditioned-assembly large-deviation theorem; that remains a stated risk. The 2026 Nishimura modal-semantics work addresses semantic representation rather than the marked-fiber law.

## Value — PASS

A natural semantic statistic of finite \(\mathsf{KD45}\) frames is the proportion of reflexive worlds. The result shows that a uniformly sampled admissible frame is typically half reflexive, and quantifies the exact exponential cost of atypical proportions. This is stronger than the pre-existing table of finite counts and addresses probabilistic benchmarks for doxastic-frame modelling. It requires a proof that conditioning every epistemic component to have a reflexive core incurs no exponential penalty; the resulting rate is not inferred merely by extrapolating a table. The result does not claim a central limit theorem or an independent mathematical audit.

## Closest coverage and remaining risks

The closest exact finite table is OEIS A143396, and the closest total asymptotic analysis is Kotěšovec's arXiv:2207.10568. A general theorem for assemblies with sublinear component count might subsume the rate; full historical priority cannot be certified by the searches performed. The probability model is uniform on labelled relations only.

Self-review: passed. Independent audit: not yet performed.
