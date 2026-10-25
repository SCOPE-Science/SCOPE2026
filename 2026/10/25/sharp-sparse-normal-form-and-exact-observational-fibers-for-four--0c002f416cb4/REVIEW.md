# Review of the four-extrema theorem

## Correctness — PASS

For each row, the existential predicate on the suffix \(U_k\) is exactly the comparison \(h_i\ge k\), while the universal predicate is \(\ell_i\ge k\), including the empty-row sentinels. The original four semantic clauses therefore give the stated prefix maximum, suffix minimum, suffix minimum, and prefix maximum; these threshold arrays reconstruct all four one-step operations. Induction on formulas supplies pointwise equivalence under common upward-closed valuations, and one-variable modal tests recover the four arrays. The local recurrence with four boundary records proves the exact fiber product by independent row-endpoint choices. Deleting interior row edges preserves every record. The constructed two-point-per-row frames force both endpoints in any equivalent relation by the strictly increasing prefix-minimum records, final suffix-minimum record, and suffix-minimum-of-maxima records.

The standalone checker exhaustively enumerated all \(2^{n^2}\) binary relations for each \(1\le n\le4\), checked the four direct semantic quantifier clauses for all suffixes, checked every signature fiber against the independent multiplicative formula, and checked the sharp family through twelve worlds. It terminated with `ALL_CHECKS_OK 337329`. The unrestricted theorem is proved symbolically; finite checks are corroboration, not an infinite-domain certificate.

## Originality — PASS within inspected material

Balbiani and Gencer, *Four intuitionistic modal connectives* (arXiv:2606.07348v1, June 5, 2026), introduce the semantics, but the inspected full text does not give the four-record chain observational quotient, an all-fiber formula, or a sharp two-edge-per-world representative theorem. Related published finite-chain descriptions impose downward/forward confluence or a pair of order-interaction properties and count raw permitted relations rather than equivalence classes of all unrestricted relations under all four modalities. These statements do not imply the present observational classification without the new threshold and reconstruction arguments. Searches for aliases in modal algebra, order-theoretic endpoint descriptions, direct numerical fingerprints, and four-modal equivalence did not identify a stronger covering theorem. Such searches cannot establish absolute priority. A previously documented four-way-confluent finite-chain classification restricts relation ownership by axioms and addresses an independently different counting problem.

## Value — PASS

Four primitive modalities are proposed to distinguish non-equivalent constructive possibilities and necessities. A complete account of precisely what their combined language can observe on finite chains is a natural question. This theorem answers it for every valuation and nesting depth, compresses every representative to two edges per world optimally, proves that no one of the four primitives is redundant, and gives a multiplicative formula for each class size (not merely a few small counts). Exact finite benchmarks \(2,16,279,7171\) quantify the resulting semantic compression. These are structural and classification results, not only a numerical exercise.

## Prior literature and remaining limitations

The closest source is Balbiani--Gencer (2026), Section 3.4. Two related fully inspected finite-chain classifications concern, respectively, \(\mathbf{KI}\) forward/downward confluence and Fischer--Servi-type row/column maxima conditions. They address different restricted classes and raw relation counts. General modal duality papers were retrieved at abstract level only. An equivalent observational-normal-form specialization might appear in older distributive-modal-algebra or multivalued-relation literature under different terms, so priority is provisional. No independent audit has occurred. The theorem does not cover non-chain orders or independent-valuation frame-validity equivalence.

Self-review: passed. Independent audit: not yet performed.
