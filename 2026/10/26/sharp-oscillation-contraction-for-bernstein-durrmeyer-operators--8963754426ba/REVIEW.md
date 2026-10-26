# Scientific review: sharp Bernstein–Durrmeyer contraction

## Correctness — PASS

The theorem quantifies over every integer \(n\geq1\) and finite positive Borel base measure with positive mass on \((0,1)\). The posterior likelihood ratios are increasing, with endpoint mass signs handled by direct Bernstein factors. This proves the single-crossing formula for posterior total variation. Ordered distribution functions imply that every posterior pair is bounded by the endpoint pair; convexity controls all mixtures, and endpoint inputs attain the row diameter. Direct density comparison gives the explicit threshold and exact integral. Approximating the Hahn-set indicator by continuous functions gives sharpness on \(C([0,1])\). Interior common mass makes the contraction strict. Symmetric kernel density proves detailed balance, while the standard Dobrushin estimate handles iteration. Exact-rational finite test cases pass, but they are not offered as proof of universal quantifiers.

## Originality — PASS, with named literature-access risk

The closest primary source (Diaconis–Khare–Saloff-Coste, arXiv:0808.3852, §4.1.2, inspected full open PDF) identifies the Beta–Binomial chain and gives spectral/chi-square information. Those results do not themselves evaluate the exact one-step Dobrushin coefficient for arbitrary prior measures. Gaubert–Qu's full arXiv text explains a general Dobrushin/oscillation equivalence but contains no specialization to Bernstein–Durrmeyer kernels or endpoint posterior threshold calculation. Berdysheva–Jetter's 2009 study of arbitrary weights and Berdysheva's 2012 arbitrary-measure study have directly relevant operator definitions and theorems on approximation and spectral behavior; only accessible extracted portions were inspected, not the unavailable full manuscripts. Relevant general formulas therefore do not visibly imply the newly evaluated sharp coefficient without the posterior ordering argument. A plausible unindexed identical result or a formula buried in the inaccessible full texts remains possible; novelty is a supported best-knowledge comparison, not an assertion of exhaustive uniqueness.

## Value — PASS

For a positive approximation operator, the exact Hopf-oscillation norm is a natural stability invariant, and for the equivalent Beta–Binomial Gibbs sampler it is the precise uniform one-step total-variation mixing bound. The endpoint-reduction lemma solves this invariant for **all** finite positive interior-mass base measures, including non-smooth and singular priors, not merely a special choice of parameters. The concrete \(1-2^{-n}\) law for the uniform measure distinguishes worst-case one-step contraction from spectral contraction and supplies a sharp independent diagnostic for iteration; arbitrary priors retain the explicit threshold-integral answer.

## Closest literature and limits

1. Diaconis–Khare–Saloff-Coste, arXiv:0808.3852, full text section on the Beta–Binomial \(\theta\)-chain; spectral and chi-square focus.
2. Berdysheva–Jetter, DOI 10.1016/j.jat.2009.11.005; arbitrary-weight polynomial operator and spectral/approximation results; full text not retrieved.
3. Berdysheva, DOI 10.1016/j.jmaa.2012.03.004; uniform convergence under arbitrary measures; full text not retrieved.
4. Gaubert–Qu, arXiv:1307.4649, full general cone/Markov contraction framework.

The sharpness claim concerns a supremum on continuous test functions; the indicator extremizer is merely measurable, and continuous approximants are sufficient. Sharpness of the \(m\)-step coefficient for \(m>1\) is not established. No full literature uniqueness assertion and no independent external audit are made.

Self-review: passed. Independent audit: not yet performed.
