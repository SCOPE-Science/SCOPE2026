# Review of exact random-majority absorption on complete bipartite networks

## Correctness — PASS

For every finite, loopless \(K_{a,b}\), synchronous independent fair ties give independent binomial updates on its two vertex classes. At two-step intervals each strict majority sign is preserved, while a tie persists with probability \(q_aq_b\le1/4\). This proves almost-sure entry into one of exactly three closed classes, and proves the independent terminal-sign product formula, without extrapolating from finite experiments. Conditioning on the first update gives three explicit probability-generating-function recurrences and, by differentiation, the stated rational expectations \(X_{a,b}\), \(Y_{a,b}\), and \(Z_{a,b}\). The monotone upper envelope for \(Z\), central-binomial monotonicity, and nine exact-rational boundary comparisons establish the uniform bound \(79/27\) and its unique equality case \(K_{2,6}\) with both parts tied. A standalone verifier checks exact Bellman identities for all blue-count states on \(144\) part-size pairs; those finite computations corroborate the proof rather than establishing the universal quantifier.

## Originality — PASS, subject to residual priority risk

The originating paper on independently fair-tied random majority (Zehmakan, arXiv:2302.06760v1, 2023-02-14; revised journal publication 2024) includes cycle-graph results. Its \(C_4=K_{2,2}\) random-initialization terminal probabilities are **already covered** and are credited. Examination of its model definitions, cycle results and appendices did not identify a general complete-biclique first-entry-time law or the sharp universal bound. The related majority-dynamics works of Mossel–Neeman–Tamuz (arXiv:1207.0893) and Benjamini–Chan–O'Donnell–Tamuz–Tan (arXiv:1405.2486) use fundamentally different deterministic tie rules; their period-two results do not imply these stochastic finite-time formulas. Comparisons with published mathematical literature and closely related models found no covering statement; models with asynchronous clocks, clique edges, and multipartite parts are not equivalent by an automatic parameter substitution. Specialist work not indexed or read could still contain an equivalent result. No absolute-priority claim is made.

## Value — PASS

For a core opinion-diffusion model, the result gives all-size exact outcome probabilities and exact first-entry distributions on a natural dense bipartite family. The sharp uniform \(79/27\) expected-time law is mathematically informative: a network can be arbitrarily large while its expected entrance time remains uniformly bounded, and the worst case is neither the smallest nor a growing graph. The theorem also separates unanimous agreement from perpetual alternating disagreement and quantifies their likelihood from independently biased initial opinions. This is a structural classification and sharp global extremum, not a routine special case or an empirical census.

## Closest literature and limitations

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (2023-02-14), https://arxiv.org/html/2302.06760v1. The \(C_4\) Bernoulli terminal-probability instance is previously known.
- A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems (2024), https://doi.org/10.1007/s10458-024-09651-y. General and cycle-specific analysis, not the all-biclique sharp hitting-time constant found here.
- E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks* (2012), https://arxiv.org/abs/1207.0893. Different tie convention and objectives.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs* (2014), https://arxiv.org/html/1405.2486v1. Deterministic tie behavior.

The result does not cover incomplete bipartite graphs, biased or dependent tie coins, asynchronous clocks, or more than two opinions. The general existence of uninspected publications creates a remaining priority uncertainty. There is no independent audit or external certification.

Self-review: passed. Independent audit: not yet performed.
