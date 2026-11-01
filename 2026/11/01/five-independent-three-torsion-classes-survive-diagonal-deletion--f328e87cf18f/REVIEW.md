# Scientific review

## Correctness — PASS
The exact chain complex is defined without hidden inputs. A full enumeration yields \((1,30,315,1420,2715,1854,265)\) faces for the diagonal-deleted complex and \((1,36,450,2400,5400,4320,720)\) for the complete complex. Witness-preserving integer elimination gives 1552 unit pivots and a residual matrix equal to three times a rank-five integer matrix with unit Smith factors. Sixteen exactly reconstructed relations \(\partial_4w_j=3z_j\) yield source order-three cycles; modular reductions show the span is five-dimensional in both source and target third homology. The resulting full three-torsion inclusion is injective. The supplied executable rederives all relevant matrices, exact relations, and ranks, and its recorded output ends with `VERIFY_OK`. Residual risk is an implementation error common to the certificate and proof; the finite check is not an independent audit.

## Originality — PASS, with remaining literature risk
Shareshian and Wachs (arXiv:math/0409054v1), in their inspected Sections 1 and 8, already list the two torsion groups. Their Lemma 8.2 and Theorem 8.3 establish nonvanishing by exhibiting a class that does not die after inclusion, but do not assert that all five independent source torsion classes remain independent in the complete board. The new statement concerns the rank-five map, not the two ranks. Jonsson (arXiv:1203.5644) concerns rectangular chessboard homology and does not supply this specific induced map in inspected material. Searches also used the crown-graph, derangement-rook, missing-diagonal, and matching-complex formulations, and compared potentially stronger coverage. No identified published-finding corpus entry or inspected full-text theorem covers this map. Equivalent unindexed work remains possible; absence from search results does not prove absolute novelty.

## Value — PASS
The canonical inclusion changes a historically studied restricted rook-placement complex into the classical chessboard complex. Although both integral homology groups and a nonzero map were known, neither determines which of the five independent order-three classes survive; an inclusion could have positive kernel while retaining a nonzero image. Determining the full injection supplies a functorial torsion-persistence fact at a natural, independently motivated first nontrivial diagonal-deletion case. It is a finite exact statement with structural significance, not a routine recomputation of Betti numbers or a new name for the pre-existing group calculation.

## Scope and residual risk
Only the six-by-six board and integral third homology are addressed. The proof is computer-assisted exact algebra, with no assertion of a uniform theory. A potentially covering result in unindexed literature, or errors in the finite chain construction, remain possible. The review is not independently validated.

Self-review: passed. Independent audit: not yet performed.
