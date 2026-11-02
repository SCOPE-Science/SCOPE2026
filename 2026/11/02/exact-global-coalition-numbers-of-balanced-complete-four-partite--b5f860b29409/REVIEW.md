# Self-review

**Correctness — PASS.** For the graph \(K_{q,q,q,q}\), global domination is equivalent to meeting every part. A partition's class supports are proper nonempty subsets of four indices, with partners precisely when supports cover all four. The upper proof separates the five possible counts of indices used by singleton-supported classes. In the one-index case, one compulsory complementary triple and any non-singleton block incident with that index give \(2z+2\le3q\); in the two-index case the complementary pair classes require a two-index partner. These constraints lead to the three claimed upper bounds. Published constructions attain each relevant bound, including the separate complete-graph boundary \(q=1\). Direct enumeration of all \(4{,}213{,}597\) original-graph partitions at \(q=3\) and exact support optimization through \(q=25\) provide computational corroboration. No finite computation is used to infer the infinite theorem.

**Originality — PASS, provisional priority.** The accessible full text of the 2026 manuscript [1] was inspected at Proposition 6, Theorem 7, Corollary 18 and Conjecture 54. Proposition 6 supplies a lower bound, and Theorem 7 proves the equality for *three* parts; the explicitly open Conjecture 54 covers all part counts. The four equal-part upper bound proved here is not implied by these statements. Equivalently, the theorem determines the coalition number of a union of four equal cliques. Searches using both formulations and exact formulas identified no covering result. Indexed-search incompleteness and differently phrased earlier work remain risks.

**Mathematical value — PASS.** The result proves a genuine infinite first case beyond the already solved three-part theorem of an explicit recent conjecture. The natural balanced four-part family has three distinct optimization regimes, and the proof isolates a reusable role of singleton-support types and mandatory complementary triples. It is neither a mere substitution into the published lower bound nor a single small-instance computation.

The closest source is [1]. The construction proving the lower bound is inherited; only the new sharp upper bound is assessed as original. The result does not settle unbalanced four-part graphs or more parts, and independent mathematical assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.

## Reference

[1] M. Anholcer, N. Besharati, D. A. Mojdeh, M. R. Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386v4 (2026-10-25), https://arxiv.org/html/2509.15386v4.
