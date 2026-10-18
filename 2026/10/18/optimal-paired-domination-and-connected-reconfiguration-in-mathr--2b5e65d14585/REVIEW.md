# Scientific review

**Correctness: PASS.** The transversal lemma equates total domination in the two-subset Kneser graph with absence of a two-element ground-edge cover. Four-edge supports containing a triangle are ruled out by the cover obstruction or failure of an induced perfect matching; the triangle-free case is bipartite and König's theorem forces three disjoint edges. This is sufficient, and three disjoint edges together with a fourth produce all three explicitly counted edge shapes. The reconfiguration proof gives explicit one-swap bridges for matching replacements and flips, and these transformations connect every three-edge matching. Two independent implementations confirm finite instances, without being treated as proofs for arbitrary order.

**Originality: PASS, with priority risk.** Accessible primary treatments of Kneser domination [1,2] provide ordinary and total domination results, but no statement asserting this complete minimum paired-dominating-set census, its three support shapes, induced pairing multiplicities, or connected token-jumping reconfiguration graph. The known classification of minimal total dominating sets, which includes disjoint triples, is close foundational material but does not itself supply these new optimum and mobility claims. Record and literature searches found no direct covering result; equivalent unindexed work remains a risk.

**Value: PASS.** A paired dominating set imposes a matching constraint absent from ordinary and total domination. This theorem simultaneously classifies all optimal feasible placements, supplies exact counts with three distinct overlap types, measures the multiplicity of compatible pairings, and proves that all optima can be reached from each other by one-location changes without sacrificing feasibility. Such a structural solution-space theorem is not determined by a scalar domination number.

**Limitations.** The family begins at \(n=6\); it does not characterize the Petersen-graph boundary. The counts distinguish labeled sets but not chosen pairing edges. Priority checking cannot establish absolute absence of unindexed results, and external validation remains open.

Self-review: passed. Independent audit: not yet performed.

**Primary literature.** [1] Cornet–Torres, arXiv:2308.15603 (2023), sections on minimum Kneser domination. [2] Brešar–Cornet–Dravec–Henning, arXiv:2312.15464 (2023), Theorems 4–5 on domination and total domination. Full citations appear in `RESULT.md`.
