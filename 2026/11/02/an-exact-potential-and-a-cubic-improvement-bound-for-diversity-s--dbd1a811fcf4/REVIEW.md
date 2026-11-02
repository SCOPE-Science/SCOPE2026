# Scientific review of the complete-bipartite diversity-seeking jump theorem

## Correctness — PASS

The claim concerns \(K_{a,b}\), both parts of size at least two, exactly one vacancy, and fraction-of-*occupied-unlike-neighbors* utility. For an agent of type \(t\) moving from the full class \(B\) to the vacant class \(A\), the payoff increment is exactly \(A_t/(a-1)-(B_t-1)/(b-1)\). The normalized within-type pair-count potential changes by the same amount. For a move within one bipartition class, both increments are zero. The symmetric move gives the other cross-class case, so all feasible unilateral deviations are covered. Counting pairs yields \(0\le\Phi\le(a+b-2)/2\); potential differences lie on the lattice with mesh \(1/\operatorname{lcm}(a-1,b-1)\). This proves exact potential, finite termination, pure Nash existence, and the stated cubic move bound. The finite verification reproduced all **658,040** stated rational transition identities; the symbolic proof, rather than enumeration, supports the universal quantifiers. No assumption on which agents are immobile affects this identity.

## Originality — PASS with residual literature risk

The closest full-text source is Narayanan–Sabbagh–Voudouris, *Diversity-Seeking Jump Games in Networks* (arXiv:2305.17757; 2025 journal DOI:10.1007/s10458-025-09714-8). Its Theorem 5.1 covers one-vacancy **regular** graphs, including \(K_{a,a}\), and its Theorem 4.8 covers one-vacancy **spiders**, including stars. Neither hypothesis covers the claimed nonregular cyclic graphs \(K_{a,b}\) with \(a,b\ge2\) and \(a\ne b\). Its concluding discussion explicitly suggests further bipartite topologies. The present potential is **exact** and yields a quantitative polynomial improvement-length bound. The later variety-seeking jump and diversity-seeking swap papers have different payoff and move definitions. The broad entropy-potential theorem for type-composition games (arXiv:2606.14428) concerns composition among *same-action* participants, whereas these payoffs depend on the *opposite* vertex class and on the unique vacancy. No covering implication or identical certificate was located in the inspected material. A genuinely equivalent but unindexed result, or an unrecognized reduction to a broader potential-game theorem, remains possible.

## Mathematical value — PASS

A foundational paper distinguishes one-vacancy regular graphs and one-vacancy spider graphs from general cases with improving-response cycles and expressly raises bipartite topologies as a further direction. Every \(K_{a,b}\) with \(a,b\ge2\), \(a\ne b\) is cyclic and nonregular, so the result identifies a new natural infinite family where all strict better-response trajectories converge under arbitrary scheduling, even with immobile agents and arbitrarily many agent types. The exact potential additionally supplies the explicit \(O((a+b)^3)\) move bound rather than merely a finite-state termination claim. This is a structural potential-game result, not a small parameter recomputation. It does not settle general bipartite graphs or multiple vacancies.

## Limits of review

No independent audit or validation has been conducted. Published-source comparisons were targeted to available complete text and accurately identified differing utilities; absence from indexed searches is not proof of publication priority. Computational checks cover only the listed finite networks and are supplementary to the proof. Any wider generalization requires separate mathematical verification.

Self-review: passed. Independent audit: not yet performed.
