# Scientific review

## Correctness — PASS

The proof establishes a frontier invariant in exact synchronous rounds, with \(h\) back-neighbours for every vertex at distance \(h\). It separately proves profile recovery at distance one in round two, then at distance \(h\ge2\) in round \(h+1\) by summing the profiles of its back-neighbours. Automorphisms guarantee that a profile never splits; the final layer has a unique profile. For sharpness, the frontier invariant postpones all distinctions *within* distance \(k-1\) until round \(k\), while mixed factor sizes create two different orbits in that layer. Every quantifier includes all \(q_i\ge2\) and the \(k=1\) boundary. The exact full-graph and weighted-quotient tests both pass. Finite tests do not establish the infinite family by themselves.

## Originality — PASS, qualified

The root-orbit profile formula is not new: Lu (arXiv:2609.06747, Proposition 7.1) covers it in greater generality. The specific contribution is the *exact stopping round of ordinary counting colour refinement* for every dimension and all mixed alphabet sizes, including cases where Lu's punctured linear module has smaller dimension than the orbit module. Arvind et al. (arXiv:1502.01255) provide general refinement theory but no mixed Hamming-product depth theorem. Structural Hamming-graph work by Klavžar (doi:10.1002/jgt.20084) supplies background only. Prior statements on two-factor rook graphs and uniform Hamming products cover special cases, not the new arbitrarily many-factor mixed assertion. Targeted searches did not find an equivalent or stronger direct result; possible overlooked sources remain a residual risk.

## Mathematical value — PASS

This resolves a concrete finite-model-theoretic refinement question uniformly over an unbounded class of high-order Cartesian-product graphs. The exact alphabet-size-independent depth contrasts with the total number of vertices \(\prod_iq_i\) and exposes a sharp one-round jump caused by the presence of two distinct alphabet sizes. It also establishes that combinatorial refinement can recover orbit cells in mixed Hamming products where the already-studied punctured linear adjacency–degree module cannot span all orbit indicators. The scope is natural and the information does not follow just from knowing the orbit counts.

## Limits and closest coverage

The claim concerns one individualized root, exact neighbor-multiset colour refinement, and undirected complete-graph factors; it does not cover arbitrary individualized sets. Lu's full orbit-profile theorem is credited, not reclaimed. Closest earlier local results concern rook graphs and uniform-alphabet Hamming products. The 2005 source was inspected through publisher metadata and abstract rather than full text; an unlocated specialist theorem is possible. No independent external audit was performed.

Self-review: passed. Independent audit: not yet performed.
