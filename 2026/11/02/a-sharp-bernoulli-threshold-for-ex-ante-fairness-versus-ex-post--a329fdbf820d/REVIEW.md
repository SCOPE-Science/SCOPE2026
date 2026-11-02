# Scientific review

## Correctness — PASS

The exact domain is two agents with additive values, with one independent fair-binary \(\{0,2r\}\)-valued good and \(r\) independent fair-binary \(\{0,2\}\)-valued goods for each agent, all allocated before values are observed. Ex-ante EF is equivalent to allocating no ordinary goods alongside the large one. The distributional identity \(Q_t=t+(r\varepsilon_0+\sum_j\varepsilon_j)/2\) determines each agent's probability of not envying; their independence yields the binomial-tail product. Its consecutive difference has one crossing; a strictly positive first difference for every \(r\ge3\) and explicit small cases establish the exact boundary. Chernoff concentration gives the asymptotic maximizing count. The independent exact-arithmetic script checks 65 direct valuation enumerations and 200 optimizers, and is not substituted for the proof. Quantifier and tie conventions are stated in RESULT.md.

## Originality — PASS, subject to literature risk

Aloisio and colleagues (AAMAS 2024) study preallocated goods whose valuations resolve later, but their objective is expected *magnitude* of maximum envy, not the probability of no envy. Halpern–Psomas–Zhang (arXiv:2602.12359, February 12, 2026) study stochastic valuations with valuation-responsive strategic mechanisms and high-probability asymptotic outcomes, not the exact probability spectrum of precommitted heterogeneous Bernoulli goods. Babaioff–Grofman (arXiv:2601.16579) and Chen–Long (arXiv:2609.23577) place randomness in the allocation mechanism rather than unobserved good utilities. The closely relevant Igarashi–Oh lottery-good manuscript (arXiv:2610.34906, October 26, 2026), including its convolution-power and non-atomic symmetry results and its general symmetric bounds, was inspected. Its stated hypotheses do not entail this atomic, heteroscedastic example, and the exact all-multiplicity classification was not found. Search and research-record comparisons did not identify an equivalent statement or dominating theorem. This is best-knowledge priority assessment, not proof of global uniqueness; unindexed precise results are a residual risk.

## Value — PASS

The mathematical question is whether balancing expected utility *before* uncertain utilities resolve also maximizes the chance that both agents will be envy-free *after* resolution. With a distinguished lottery good and a variable number of independent light lottery goods, the result determines a sharp transition at three light goods, the exact optimal allocation at every size, and its asymptotic half-split. It pinpoints the role of discrete atoms and item-scale heterogeneity in a natural two-agent benchmark. The contribution is a structural infinite family, not an arbitrary isolated example.

## Limits and closest literature

The claim requires fixed, valuation-blind deterministic allocation, fair independent binary indicators, and the exact \(2r\)-versus-\(2\) scale relationship. It makes no claim about arbitrary distributions, strategic truthfulness, or randomization over allocation rules. The direct exact counts end at \(r=10\), and the enumerated optimizer checks end at \(r=200\); the analytic proof covers all \(r\ge1\). Relevant references and the scientific comparison appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
