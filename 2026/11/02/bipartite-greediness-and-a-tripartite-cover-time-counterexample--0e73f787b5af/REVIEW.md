# Self-review

## Correctness — PASS

The claim specifies independent uniform two-neighbor offers with replacement, vertex coverage, full-history control, and the start part. Deterministic alternation, count-wise probability domination, and a monotone coupling establish stochastic greedy optimality on every complete bipartite graph. For the tripartite claim, the exact occupancy reduction follows from automorphism symmetry, and finite-state proper stochastic-shortest-path Bellman equations have unique solutions. The embedded checker solves these equations in exact rational arithmetic, checks every greedy Bellman comparison (608 ordered offered pairs), and verifies the rational expected-time improvement. The independent-in-method float policy search proposes actions only; exact comparisons certify them.

## Originality — PASS, with residual historical risk

The closest primary source is Georgakopoulos–Haslegrave–Sauerwald–Sylvester, arXiv:1911.05170 (first publicly posted 2019-11-12), whose accessible full HTML sections 1, 2, 7, and 8 were inspected. It develops the model, generic cover-time MDP machinery, and hardness, but no explicit result establishing universal complete-bipartite greedy optimality paired with a complete-tripartite exact counterexample was identified. The 2006 Avin–Krishnamachari publication studies a distinct visit-count preference empirically; its abstract and bibliographic description were available, not all of its full text. Searches for aliases, stronger general statements, and graph-specific examples found no decisive covering statement. Absence from searches is not proof of historical priority.

## Value — PASS

This is a substantive boundary for a natural coverage heuristic: every complete bipartite graph admits an optimal first-visit-greedy policy, while allowing a third part can make the immediately new vertex the strictly worse choice. The effect is structural rather than a numerical optimization of an arbitrary parameter, and the exact small instance provides an independently reproducible benchmark for cover-time control on multipartite graphs. The absolute gain is small; broader classification remains open.

## Scope and limitations

No claim of optimality of the non-greedy witness, of minimum counterexample order, or of performance for arbitrary tripartite sizes. The primary classification is probabilistic controlled Markov chains (MSC2020 60J10); the graph supplies the transition structure. The result was not independently audited.

Self-review: passed. Independent audit: not yet performed.
