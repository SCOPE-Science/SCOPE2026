# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The formulas follow by exhaustive symbolic classification, not by the finite verifier. In the standard model, once one bipartition class is rooted at zero, the opposite class has signs plus or minus one: using both signs forces all vertices on the rooted side to zero, while a constant sign gives independent zero/two choices, yielding the stated total and exactly two range-one functions. In the lazy model, classifying the exact image of the opposite side among the subsets of minus one, zero and one yields the stated total; diameter two and inclusion-exclusion over the two width-one image intervals gives the complete range distribution. Strict discrete convexity of the resulting fixed-order count proves the star/balanced extremizers. A fresh enumeration of representative small bicliques independently matched the formulas.

Originality: PASS. PASS to the best of current knowledge. The complete first twelve pages of Zhu's 2026 primary preprint were inspected through authorized full-text access. They define both models, state the global path-maximal theorems, and treat K_{2,3} as a running example; pages 4-5 explicitly enumerate ten standard functions and derive expected range 9/5, but no general K_{a,b} count or fixed-order biclique extremizer theorem appears in the inspected result/proof sections. Published-record semantic search returned the audited record as the only exact complete-bipartite range law. The classical 2000 and 2003 papers were not both available for complete inspection, so an older special-case enumeration remains an explicit risk.

Scientific value: PASS. PASS. This is a natural complete classification for a canonical graph family in the exact models used by the current path-extremality theory. It upgrades an isolated K_{2,3} running example to closed range distributions for all bicliques and identifies the unique fixed-order extremal shapes, including a nontrivial lazy asymptotic split between stars and balanced bicliques. The proof is elementary but the result is a motivated reusable exact family, not an arbitrary small-instance exercise.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
