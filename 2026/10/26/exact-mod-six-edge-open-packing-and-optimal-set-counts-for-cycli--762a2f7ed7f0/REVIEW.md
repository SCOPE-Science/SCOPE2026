# Scientific assessment: edge open packing of cyclic prisms

## Correctness — PASS

The graph-theoretic definition is tested directly against every pair of edges in seven through fourteen column prisms. The resulting allowed mask alphabet and one/two-step conflict predicates yield an exact cyclic 17-state transfer for every prism order at least seven. A four-state integer potential makes every transition deficiency zero or one, with total deficiency equal to the number of columns minus the number of selected edges. The executable verifier constructs the exact integer matrices, proves the identity \(B_0^8=B_0^2\) by equality of all entries, identifies the sole zero-deficiency six-cycle, and calculates the stated traces. Those finite identities establish the two infinite formulas by periodicity and trace counting; direct subset enumeration is additional corroboration, not the infinite proof. Main risk: hand transcription of local predicates, mitigated by the independent original-graph test.

## Originality — PASS (best-knowledge, not independently certified)

The 2022 originating paper treats paths, cycles, wheels, complete multipartite graphs, and the Petersen graph, not a full cyclic-prism extremal count. The 2024 bounds paper supplies the general \(\lvert E\rvert/\delta\) upper bound and characterizes its equality case; the later Cartesian-product paper supplies lower bounds but not the complete residue-specific optimal-subset multiplicities. A direct implication comparison therefore separates this statement from the closest known theorems. Searches also used the aliases injective edge coloring, independent edge-conflict sets and disjoint induced stars. The nearest identified mathematical-record hits concern other graph invariants on the same prisms; their statements do not imply the edge-packing enumerator. Residual risk is a nonindexed or differently named prior theorem or a hidden implication from a broader classification.

## Value — PASS

This is an all-order sharp classification for a natural family of cubic Cartesian products. It decides precisely when the universal cubic packing capacity is attained and when exactly one edge must be sacrificed; beyond that scalar question it counts **every** extremal edge subset, with an unexpected six-periodic oscillation between constant and linearly growing multiplicities. Both the upper-bound equality issue and edge-product questions are explicit themes of the primary 2024 literature. The result is not a renamed version of the general cubic bound, because that bound does not enumerate non-equality cases or optimal configurations.

## Limits and priority risk

No assertion is made for cyclic prisms of orders three through six or for arbitrary graph products. Existing general inequalities and foundational definitions are cited as prior work, not claimed. The 2022 source, two accessible 2024 full texts, relevant terminology variants and research-index summaries were checked. A complete priority audit across all older injective edge coloring or induced-star classifications is unavailable.

Self-review: passed. Independent audit: not yet performed.
