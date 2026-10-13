# Scientific review

## Correctness — PASS

For each field size \(q\in\{2,3,4,5,7,8,9,11\}\), affine normalization gives precisely \((q-2)!\) distinct fixed-coordinate codes. Every relevant pairwise edit distance reduces to the LCS of an evaluation permutation and one of its \(q(q-1)-1\) nonidentity affine transforms. The bit-parallel dynamic-programming verifier and the structurally independent LIS verifier agree on all enumerated cases, including all \(362880\) normalized evaluation orders over \(\mathbb F_{11}\). Small-field ordinary-DP checks and the complete \(155\)-transform ordinary-DP check of the stated \(\mathbb F_{13}\) witness resolve the critical finite boundaries. No generalization beyond the stated finite domains is inferred.

## Originality — PASS, with residual risk

The closest primary article, Beelen et al., arXiv:2501.11371, already classifies the orders with no correction ability; its Lemma 3 therefore covers the \(\tau=0\) column. Its Proposition 1 and Table 1 do not give the full higher-radius distributions, and its concluding computational observation for fields from \(13\) does not supply an explicit ordering. The 2024 two-dimensional Reed–Solomon construction (arXiv:2311.02771) concerns near-optimal error counts with cubic-sized extension fields, not full-length small-field enumerations. Published searches for the precise field-eleven multiplicities and equivalent LCS/LIS formulas did not uncover an exact prior table. A later 2026 journal version was available at abstract level only; its inaccessible full body and an unindexed finite table remain genuine overlap risks, rather than grounds to assert proven novelty.

## Mathematical value — PASS

The question of which evaluation orderings yield good synchronization correction was explicitly highlighted as open by the originating paper. The exact correction-radius spectrum at every field size through \(11\) quantifies the distribution of performance over *all distinct codes* rather than just establishing existence of one good ordering. A separate length-\(13\) witness establishes the first field where insdel correction exceeds the classical Hamming substitution radius. This is a complete and motivated finite classification with a sharp field-size consequence. No claims are made for higher dimensions, all \(\mathbb F_{13}\) orders, or larger fields.

Self-review: passed. Independent audit: not yet performed.
