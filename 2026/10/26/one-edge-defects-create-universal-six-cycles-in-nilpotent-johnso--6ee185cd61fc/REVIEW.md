# Scientific review

## Correctness
PASS. A self-contained exterior-algebra proof establishes that the original adjacency matrix squares to zero and has rank \(r=\binom{n-2}{k-1}\). The four vectors associated to an edge form an independent, invariant four-dimensional space whose explicit action has one fixed point, one three-cycle and two six-cycles. The formula for \(B^2\) proves all states reach that space in at most two updates. Symmetry and a direct-sum rank argument establish the exact transient population. A standalone verifier checked all initial configurations on the three smallest tested graph instances, as well as nine exact-rank instances through \(n=10\). Finite testing is corroboration only.

## Originality
PASS within documented search coverage. Peeters (2002), Section 4.1, already proves relevant binary ranks and polynomial constraints for unperturbed Johnson graphs, so those antecedents are not claimed as new. The extra edge-deletion term defeats the original nilpotence and yields a four-dimensional periodic attractor of order six; no implication of this perturbed classification was found in the inspected sources, related published parity-automaton results, or accessible historical claim records. Ganesan (2014) treats graph automorphisms, not XOR dynamical orbits; Kong–Lv–Wang (2011) treats Johnson incidence graphs. An unindexed or inaccessible equivalent remains a material risk. Novelty is not certified by the absence of a search hit.

## Value
PASS. The main insight is that deletion of a single adjacency creates exact six-periodic oscillations from a globally nilpotent update, uniformly over an infinite two-parameter Johnson family. The sixteen-state attractor, full cycle census, and exact two-step transient populations quantify a natural robustness failure in finite binary network dynamics. This is a qualitative bifurcation, not merely a recomputation of the known binary rank.

## Limits
All quantifiers require even \(n\ge4\) and even \(2\le k\le n-2\), and the graph must have exactly one removed edge. Independent examination and exhaustive coverage of historical literature have not been performed.

Self-review: passed. Independent audit: not yet performed.
