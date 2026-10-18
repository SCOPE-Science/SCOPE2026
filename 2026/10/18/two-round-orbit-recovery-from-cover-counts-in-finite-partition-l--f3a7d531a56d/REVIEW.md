# Scientific review

## Correctness — PASS

For a set partition \(P\) with \(k\) blocks of sizes \(s_i\), first-round incoming/outgoing degrees give \(F(P)=\sum_i(2^{s_i-1}-1)\) and \(inom{k}{2}\). For an upper cover merging sizes \(a,b\), the first-round degree change obeys \(2(F(Q)-F(P))-1=(2^a-1)(2^b-1)\). The displayed two-adic lemma proves unique recovery of the unordered pair. The multiset of merged pairs recovers each block-size multiplicity by dividing its pair-incidence count by \(k-1\) when \(k\ge2\); the unique one-block partition is separate. Relabelling proves the resulting classes are exactly automorphism orbits. The two distinct size-\(14\) types \((1,1,3,3,3,3)\) and \((2,2,2,2,2,4)\) share first-round degree pair \((15,12)\), and adjoining singletons propagates the obstruction to all larger sizes. The finite integer-partition enumeration proves the small-size cutoff. Direct full-graph tests cover \(n\le8\), weighted type-level tests cover \(n\le36\), and a finite product check covers \(4005\) unordered exponent pairs. None of these finite checks is used to establish the general case.

## Originality — PASS (provisional publication-priority assessment)

The closest published partition-lattice sources, Ehrenborg–Readdy (arXiv:1009.3976) and Ehrenborg–Hedmark (arXiv:1606.01443), study block-size types, partition-poset covers, and topological or representation-theoretic invariants rather than one-dimensional colour-refinement rounds. Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255) provides the general graph-theoretic notion of a refinable orbit partition but not the concrete directed-Hasse two-round calculation. Relevant published research-record searches and comparisons with accessible earlier claim texts revealed no statement from which this sharp result follows. The bound for the full strict-order predicate, considered separately in the literature of finite relational structures, should not be transferred to the cover predicate without proof; these are different signatures. Exact novelty and publication priority remain subject to independent checking, particularly for specialist treatments of coherent configurations of partition lattices.

## Value — PASS

This gives a uniform, exactly sharp finite-model-theoretic orbit-recovery bound for an unbounded family with Bell-number-sized vertex sets. The two-adic injectivity of merged-block degree changes explains why just a second local-neighbourhood census reconstructs the entire global block-size profile. The phase transition in the minimal number of refinement rounds at size \(14\) is explicit and motivated by the first collision between the degree signatures. This is not merely the classical formula for the number or size of partition-type orbits, nor an unsupported extrapolation from small cases.

## Limits and closest literature

The cover relation is directed. There is no assertion for the undirected Hasse graph, arbitrary posets, or global identification among arbitrary digraphs. The second-round bound and the non-isomorphic first-round examples are mathematically proved; the statement that smaller ground sets need only one round rests on exhaustive, reproducible finite integer-partition enumeration. Originality remains provisional because all relevant specialist literature may not have been indexed or accessible.

Self-review: passed. Independent audit: not yet performed.
