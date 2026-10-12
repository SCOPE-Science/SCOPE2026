# Scientific review

**Correctness — PASS.** The arithmetic model, its two split transversal \(A_2\) curves, and the full 96-node list follow from the exact equations and proofs in Burek [1, Sections 6–7]. The new step computes local divisor classes for a Galois-stable sum of twelve section graphs. Its exact, repeatable certificate covers all nodes, cross-checks the section equations and opposite/same-ruling criterion for every incident pair, and yields absolute local classes 2 (64 times) and 4 (32 times). The local ordinary-node reflexive algebra and Veronese construction then produce a projective smooth small crepant resolution over \(\mathbf Q\). No inference from partial sampling is used. Limit: the general local conifold class-group lemma is justified mathematically, rather than by software.

**Originality — PASS.** Burek [1] supplies the 96-node and six-section incidence ingredients, but constructs the resolution geometrically over \(\mathbf C\) and does not establish a model over \(\mathbf Q\); its Table 1 does not give signed Galois-norm classes. Coverage of the nodes by six complex section images, even when incidence minimality is known, does not imply that a Galois-invariant Weil divisor survives cancellation of opposite local rulings. The signed local class computations and relative Proj are the new comparison-relevant content. The broader projectivity/gluing framework of Kaplan–Schedler [2] does not calculate this example. Searches for the descent statement, its conifold and divisor-class aliases, and broader coverage found no decisive prior implication. Risk: an arithmetic reformulation elsewhere might already derive the rational resolution.

**Value — PASS.** A complex projective small resolution need not descend through Galois: conjugation can exchange the two local rulings, and simultaneous projectivity can impose an additional global obstruction. An explicit rational divisor that stays non-Cartier at all 96 nodes resolves both obstacles constructively in a geometrically high-rank elliptic Calabi–Yau example. The 64/32 local class distribution is an exact intrinsic feature of the specific rational norm divisor. This is a natural arithmetic-geometric question, not a normalization or finite enumeration without structural motivation.

**Scope.** The theorem concerns this particular \(\mathbf Q\)-defined model and geometric Mordell–Weil rank twelve; it does not compute the arithmetic rank, classify all resolutions, or establish novelty from database silence.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] D. Burek, arXiv:2610.01276v1, Sections 6–7 and Appendices A–B.

[2] D. Kaplan and T. Schedler, arXiv:2311.07539v4, Section 3.3.
