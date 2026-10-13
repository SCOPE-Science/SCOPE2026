# Review

## Correctness
PASS. The direct support calculation gives a two-qubit block for every bipartition, an exact negative determinant for each nontrivial gate at every positive success probability, and a separate proof excluding convex mixtures of states PPT across cut-dependent partitions. The endpoint and nonspanning-edge cases are explicit. The attached checker corroborates the determinant and the local basis reduction for finite test sizes; the all-size conclusion comes from the proof rather than enumeration.

## Originality
PASS for the **full PPT-mixture rigidity classification and the exact cut determinant**, not for the already-known qualitative claim of NPT on every cut. Salem--Silva--Andrade define the model and use low-qubit PPT-mixture numerical tests; they do not prove this all-size boundary. Chen--Đoković's rank-two Lemma 12 already implies NPT for product-plus-entangled mixtures, and this is acknowledged as prior. Their rank-two results do not by themselves settle the convex hull of operators PPT on different cuts. Comparison with the cited primary results revealed no implication-equivalent single-hyperedge theorem.

## Value
PASS. The theorem gives an all-parameter closed decision rule for a natural idealized primitive underlying the source's multi-edge entanglement study, replacing numerical PPT-mixture decisions for this case. The exact determinant provides a parameter-sensitive certificate of entanglement on every split. It identifies precisely which edges can create genuine multipartite entanglement at arbitrarily low nonzero success probability.

## Closest literature and limitations
The closest physical model is arXiv:2506.20075v1 and its predecessor arXiv:2310.20418v2; the closest general rank-two domination is Lemma 12 of arXiv:1301.2372v1. The original PPT-mixture method is due to Jungnitsch--Moroder--Gühne. A residual risk is unindexed specialized low-rank PPT-mixture theory. The theorem does not analyze realistic gate noise, multiple random hyperedges, or finite experimental detection thresholds.

Self-review: passed. Independent audit: not yet performed.
