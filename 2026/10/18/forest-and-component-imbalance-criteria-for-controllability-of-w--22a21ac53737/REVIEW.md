# Independent mathematical audit

## correctness

PASS

The Kronecker-sum Laplacian has eigenspaces 1⊗1, U_p⊗1, 1⊗U_q, U_p⊗U_q with eigenvalues 0, ap, bq, ap+bq. For terminal inputs, PBH requires restriction injective on each full eigenspace; U_p⊗U_q consists of zero-row/column-sum matrices, and the unselected-supported kernel is exactly the circulation space of the bipartite unselected graph H, which vanishes iff H is a forest (cycle alternation/leaf peeling). Nonresonance: no two entire unselected rows/columns when H is acyclic, so mean-zero single-coordinate vectors cannot hide; constant mode detected. Resonance ap=bq: middle modes Y_ij=f_i+g_j, and selected edges force component parameters t_c satisfying sums r_c t_c=s_c t_c=0, so t<=2 with rank-two imbalance for t=2. Forest maximum edges p+q-1 yields minimum (p-1)(q-1); resonant rank lower bound and explicit double-star/tree complements give special min max(p,q) if min(p,q)=2; matrix-tree theorem yields p^(q-1) q^(p-1) optimum nonresonant placements. Independent exact modular PBH rank compared with graph tests on ALL selections in 2x2,2x3,2x4,3x3,3x4, in both resonance regimes: minima [1,2],[2,3],[3,4],[4,4],[6,6]. Infinite p,q result is from the algebraic proof, not those masks.

## originality

PASS

Prior PBH and product spectral facts are acknowledged; no inspected source derives the complete all-terminal-sets forest plus resonant selected-component rank classification, nor the optimal-placement count. Access/alias risk remains.

## value

PASS

A natural exact actuator-placement classification for all weighted rectangular complete-graph Cartesian products, distinguishing a single eigenvalue-collision hypersurface, with an interpretable cycle-space obstruction, sharp actuator count and labeled optimal placement count; not a routine multiplicity inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
