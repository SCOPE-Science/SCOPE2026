# Research review: directed-circle ballot dispersion and competence frontier

## Correctness — PASS

The exact ballot-weight generating function follows from the marked-cycle count: ordered positive compositions of \(n\) into \(k\) guru weights are counted with multiplicity \(n/k\). The all-delegating probability is accounted for separately. The dispersion formula independently counts ordered original-voter pairs with a shared guru and subtracts the full-cycle intersection of the two delegation-only arcs. Both finite formulas were checked by an exhaustive exact-rational enumerator for 24 parameter/size cases.

For the asymptotic law, a union bound limits the longest delegate run to \(O_{\mathbb P}(\log n)\). Truncated length-squared rewards have \(O(\log^5 n/n)\) averaged variance and expectation converging to \((2-q)/q\), establishing the required normalized squared-weight limit. Conditional independent guru signals then satisfy Lindeberg's condition, yielding the Gaussian sign-margin limit, and independent random types give the direct-voting binomial benchmark. Every limit concerns fixed \(0<q<1\) with accuracy deviations on the \(n^{-1/2}\) scale; the theorem makes no equality-frontier finite-size assertion. The proof is analytical, not inferred from computation.

## Originality — PASS, with stated residual risks

The nearest primary studies are Berinsky et al. (2021, arXiv:2107.11868), which analyzes random-target transitive delegations and concentration conditions; Becker et al. (2021, arXiv:2104.01828), which addresses optimization and hardness; Kahng, Mackenzie and Procaccia (2018), which assumes delegation toward more competent neighbors; Colley et al. (2023, arXiv:2301.02462), which computes delegation-aware voting power; and Chatterjee et al. (2025, PODC), which establishes general variance-dependent sufficient conditions for local mechanisms. Relevant portions of these primary full texts were examined. None of the inspected results gives the explicit Bernoulli clockwise-cycle correct-tally law and squared-weight formula together with the sharp \(n^{-1/2}\)-competence truth-tracking frontier. Results about the general principle that concentration can harm majority reliability are acknowledged as prior, not claimed new.

Published mathematics-index searches and semantic research-record queries were also compared with accessible previous claims, including a different bidirectional-cycle delegation enumeration, a single-expert five-voter optimization, a quota-criticality calculation and a bipartite lost-delegation law. Those earlier claims do not imply this one-way stochastic-cycle exact fluctuation and sharp asymptotic frontier. These searches cannot prove universal uniqueness. A relevant 2026 Grossi et al. article on first-moment expected voting weight had only abstract/secondary material accessible; hidden related results in that primary full text or other unindexed literature remain residual risks.

## Mathematical value — PASS

General liquid-democracy truth-tracking theory recognizes the competition between selecting better-informed casters and concentrating many ballots onto a small number of independent signals. For any fixed information advantage, both direct and appropriately nondegenerate delegation settings commonly saturate at perfect accuracy, making raw asymptotic comparison uninformative. The local \(n^{-1/2}\) competence regime isolates a natural statistically nontrivial comparison. The theorem **quantifies** both the exact finite concentration factor and its consequence: an explicit strict boundary between delegation helping and harming truth discovery, with a concrete \(q=1/2\) threshold \(2/\sqrt3-1\). This is a model-specific structural law, not merely a bound on an arbitrary sum.

The model is limited to a fixed oriented cycle, independent direct/delegate indicators, independent binary signals and strict-majority decisions. No implication is drawn for correlated votes, arbitrary graph topologies, strategic delegation, or changing \(q\). The boundary itself gives equal limiting accuracy only, not any finite-size ordering.

Self-review: passed. Independent audit: not yet performed.
