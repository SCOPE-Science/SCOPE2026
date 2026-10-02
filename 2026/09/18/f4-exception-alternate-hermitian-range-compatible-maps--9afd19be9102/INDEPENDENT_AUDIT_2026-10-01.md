# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-9afd19be9102`

## Correctness — PASS

In characteristic two with the nonidentity involution on \(\mathbb F_4\), the Hermitian scalar subgroup and the alternate-Hermitian scalar subgroup both equal the fixed field \(\mathbb F_2\), and the off-diagonal sign distinction disappears; hence the two \(2\)-by-\(2\) matrix spaces coincide. The source paper's exceptional Hermitian map therefore is an alternate-Hermitian range-compatible nonlocal map, contradicting the unconditional locality statement in the cited first version. The Hermitian classification then transfers verbatim: local maps contribute a two-dimensional \(\mathbb F_4\) family and scalar multiples of the nonlocal map contribute a complementary one-dimensional family. An independently reconstructed exhaustive finite-field enumeration reproduces exactly 64 range-compatible maps, 16 local maps, and 48 nonlocal maps.

### Correctness sources

- de Seguins Pazzis, arXiv:2609.20363v1
- artifacts/verify_f4_exception.py
- independent finite-field enumeration

### Correctness risks

- The audit concerns the cited first version; a later source revision could independently incorporate the correction.
- The exceptional Hermitian map itself is prior work and is not treated as new.

## Originality — PASS

The exceptional Hermitian map and its classification are prior results of the source paper. The originality-bearing claim is the overlooked identification of the alternate-Hermitian space with the Hermitian space in the \(\mathbb F_4\), characteristic-two, dimension-two case, together with the resulting correction and exact count. No public correction or equivalent theorem was located in the checked current sources.

### equivalent_formulations

Searches:
- arXiv:2609.20363 first-version theorem statements
- searches for F4 alternate-Hermitian exception and Phi_0 correction

Evidence:
- The source advertises separate Hermitian and alternate-Hermitian classifications; the exceptional map is stated on the Hermitian side.
- No inspected public source states the corrected alternate-Hermitian exception.

Reasoning:
The two matrix spaces are literally equal in the exceptional characteristic-two case, so the source's own Hermitian theorem transfers.

### broader_coverage

Searches:
- de Seguins Pazzis 2016 range-compatible symmetric/alternating matrices
- the source paper's general alternate-Hermitian locality theorem

Evidence:
- The older paper supplies related range-compatible techniques but not this Hermitian/alternate-Hermitian F4 conflict.

Reasoning:
The prior broader classification framework does not remove the internal exceptional case.

### exact_database_or_table

Searches:
- finite-field exhaustive classification for the exact 16-matrix domain

Evidence:
- The independent enumeration yields 64 total, 16 local and 48 nonlocal maps; no separate published table was located.

Reasoning:
The count corroborates the theorem transfer, but the correction is not merely a table lookup.

### claim_vs_prior_implication

Searches:
- implication from source Theorem 1.6 after identifying the spaces

Evidence:
- Once the spaces are equal, Theorem 1.6 directly implies the nonlocal alternate-Hermitian examples and full exceptional classification.

Reasoning:
This implication is the correction itself; it is not prior coverage by a distinct published source.

### source_inspections
- **Range-compatible homomorphisms on Hermitian matrices** — https://arxiv.org/abs/2609.20363. Trigger: Source containing both the exceptional Hermitian theorem and the conflicting alternate-Hermitian statement. Material read: Accessible abstract/metadata and theorem information cross-checked against the assigned exact quotation; current public revision/correction searches were also checked. Method: Primary-source statement comparison plus exact finite verification. Assessment: The source provides the ingredients but the first version's alternate-Hermitian theorem omits the transferred exception. Evidence: The exceptional Hermitian map exists in exactly the matrix space that becomes alternate-Hermitian in this characteristic-two case.
- **Assigned exact finite verifier** — artifacts/verify_f4_exception.py. Trigger: Exact count and classification of the exceptional finite case. Material read: Complete source file. Method: Line-by-line inspection and independent reimplementation of the finite-field enumeration. Assessment: The count and classified family reproduce exactly. Evidence: 64 range-compatible maps are found, of which 16 are local and 48 nonlocal.

### checked_sources

- https://arxiv.org/abs/2609.20363
- https://arxiv.org/abs/1506.07203
- assigned RESULT.md and artifacts/verify_f4_exception.py

### residual_risks

- The source is a very recent first version and may be revised independently.
- Full current source text was not available through every route checked, so an unindexed correction remains a residual risk.

## Scientific value — PASS

Correcting an advertised complete classification in its unique finite exceptional case is mathematically useful, and the result gives the full replacement statement and exact exceptional-space size rather than only a counterexample.

### Value sources

- arXiv:2609.20363v1
- exact finite classification

### Value risks

- The value is a correction to a narrow exceptional case, not a new general theory.

## Limitations

- The exceptional Hermitian map and its nonlocality are prior work.
- The correction is tied to the cited first-version theorem statement.
- A later unindexed source revision could independently incorporate the same correction.

## Disposition

**PASSED**
