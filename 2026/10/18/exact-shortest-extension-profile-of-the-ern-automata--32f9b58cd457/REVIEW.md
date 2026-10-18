# Scientific review: exact shortest-extension profile of the Černý automata

## Correctness

**PASS.** The proof uses the explicit transition normalization \(a:i\mapsto i+1\) cyclically and \(b:0\mapsto1\), then applies a telescoping identity for transition in-degree. The short-suffix lemma constrains every contribution to a cyclic indicator difference indexed by at most the suffix length. This supplies both the strict lower bound and the unique word attaining it. The prefix-count argument proves the cardinality-refined and unconditional histograms, the exact exceptional length-\(n\) subsets, and the mean. Independently coded finite preimage BFS checks all \(3\le n\le11\), while literal word enumeration verifies uniqueness for \(3\le n\le9\). The checker output is supplied. The proof, not the finite search, covers arbitrary \(n\).

## Originality

**PASS within examined evidence.** Miccinesi, arXiv:2609.21603v1, Introduction and Section 8.1, provides general sufficient certificates and the fact that some Černý subsets cannot extend before length \(n\), but neither identifies all such subsets nor gives minimum lengths and unique shortest words for all subsets. Berlinkov–Ferens–Szykuła, arXiv:1704.08233v4, treats extension-complexity questions and an example on a four-state Černý automaton, not the infinite exact profile. Closest published research records address initial *image-rank* compression or *complete avoidance*; neither fixes the first-strict-growth reverse-preimage times. Alternative formulations via complement shrinking, subset-level reverse distances, and complete-avoidance thresholds were compared by statement and implication. Searches do not establish historical priority. An unindexed pre-existing Černý calculation is the main residual risk.

## Value

**PASS.** Uniform bounds on individual extension words enter the extension method for synchronizing automata. The classical extremal Černý family is a natural benchmark, and the originating certificate paper explicitly uses it as an obstruction to the threshold \(n-1\). The exact theorem characterizes every obstruction and every optimal word, quantifies the distribution by subset size, and distinguishes an average cost tending to \(3\) from a worst cost of \(n\). Neither the published nonuniform certificate nor known reset thresholds answer this precise distribution question. This is a natural complete classification rather than a selected finite parameter or a renaming of the known reset-word bound.

## Limits and closest comparison

The scope is exactly the fixed-labeled automata \(C_n\) for \(n\ge3\), with strict *preimage cardinality* extension. The statement does not settle all-subset extendibility in general automata or provide a better reset bound. Unindexed historical literature remains a possible source of an equivalent profile; independent scientific audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
