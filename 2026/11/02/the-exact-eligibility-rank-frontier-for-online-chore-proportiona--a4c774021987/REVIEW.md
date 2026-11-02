# Scientific review

## Correctness — PASS

For any chore assigned to agent \(i\), its cost is at most \(r\) times its fractional proportional-share contribution. Summation proves the stronger universal \(L_i\le rP_i\). The adaptive \(r\)-champion construction preserves, by induction, exactly \(\ell\) received and \(\ell\) eligible unit chores for each level-\(\ell\) champion. After \(h\) levels the last champion has \(L=h\), \(b=1\), \(P=h/r\); hence every factor below \(r\) is violated at sufficiently large finite height. Component joining proves incidence-graph acyclicity. The arithmetic, algorithm quantifiers and empty-bundle case are explicit. The exact-rational verifier exercises broad finite instances but is not substituted for the all-size proof.

## Originality — PASS (self-review)

The closest first-public source, Biburger–Megow–Shahkarami, arXiv:2610.08064 (2026-10-06), gives an unrestricted \(\Theta(\sqrt m)\) factor and an adversary involving large eligibility sets. That asymptotic result does not determine the exact fixed-\(r\) frontier or the rank-\(r\) Berge-tree lower bound. The upper inequality is simple and is compatible with the paper's handling of low-cardinality jobs; sharpness is the substantive added step. Sun–Wang–Li, arXiv:2602.18098, concerns offline relevance-constrained fairness. Bansal et al., arXiv:2604.04159, concern stochastic graph orientation and a global maximum-load benchmark. Searches for direct equivalents and stronger covering claims found none among retrieved material. Unindexed exact bounded-rank fairness results or an implicit classical orientation reduction remain genuine priority risks.

## Mathematical value — PASS

The eligibility-set cardinality is an intrinsic structural parameter for skill-restricted allocation. The theorem replaces an agent-count-dependent asymptotic estimate with an exact all-rank minimax law and locates a strong boundary: even unit chores on a simple connected hyperforest can force the full rank loss. At rank two this is already a tree, contrasting with the offline existence of \(\mathrm{Prop1}\) and giving a natural benchmark for stronger restrictions such as known eligibility types. It is not a routine numerical recomputation or an arbitrary parameter slice.

## Boundaries

The claim concerns deterministic irrevocable online chore assignments, arbitrary finite agent sets, and adaptive eligibility sets of size at most \(r\). It does not cover expected randomized guarantees against oblivious arrivals, heterogeneous costs, or fixed-population optimal factors. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
