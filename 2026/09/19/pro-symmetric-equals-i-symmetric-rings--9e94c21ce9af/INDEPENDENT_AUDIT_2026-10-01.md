# Independent mathematical audit — 2026-10-01

## Final claim assessed

Pro-symmetric rings coincide with I-symmetric rings

## Correctness — PASS

PASS. The unit-group necessity follows by applying I-symmetry to a triple product equal to one: the transposed product is an invertible idempotent and hence one. For the converse, symmetry makes the idempotent \(p=abc\) central and forces \(q=acb\) into the corner \(pRp\). Reversibility makes this corner directly finite; from \(ABC=p\) the corner factors are units. Centrality embeds the corner unit group into \(U(R)\), so abelianness forces \(ACB=ABC=p\). Thus I-symmetry is exactly symmetry plus an abelian unit group. For a ring with involution, I-symmetry immediately implies pro-symmetry, while pro-symmetry supplies symmetry from Chen--Wang--Zou and supplies abelian units by the same triple-equals-one argument, giving the converse. The clean-ring, division-ring, and free-algebra examples follow correctly.

## Originality — PASS

PASS. Two highly relevant primary sources were read in full. Han--Lee--Lee prove that I-symmetric rings are symmetric and have abelian unit group, and prove the converse only under extra hypotheses such as abelian semiperfectness; their full 12-page paper does not state the unrestricted criterion. Chen--Wang--Zou introduce pro-symmetric rings, prove they are symmetric, and characterize the projection triple condition, but their full 11-page preprint neither cites I-symmetry nor identifies pro-symmetry with it. The audited theorem supplies the missing unrestricted converse and then links the two literatures. Resultary search found no earlier published record with this identification.

### equivalent_formulations

Searches: I-symmetric ring symmetric abelian unit group unrestricted; pro-symmetric I-symmetric rings

Evidence: Han--Lee--Lee Lemma 1.3 gives both necessary conditions but no unrestricted converse; Chen--Wang--Zou develop the projection condition separately.

Reasoning: The exact unrestricted equivalence and class identification are not alternate wording of a theorem found in either full text.

### broader_coverage

Searches: Han Lee Lee Symmetry on zero and idempotents full text; Chen Wang Zou pro-symmetric full text

Evidence: The strongest matching Han theorem adds abelian semiperfect hypotheses; Chen's theorems characterize pro-symmetry internally.

Reasoning: Neither prior theorem dominates the unrestricted class equivalence.

### exact_database_or_table

Searches: Resultary semantic search pro-symmetric equals I-symmetric

Evidence: No data table is relevant; the exact theorem search returned the audited record.

Reasoning: This is a structural equivalence theorem.

### claim_vs_prior_implication

Searches: Han Lemma 1.3 I-symmetric units Abelian; Chen Definition 4.5 pro-symmetric

Evidence: The two primary papers supply opposite-side ingredients but not the corner argument establishing the missing converse.

Reasoning: Combining the printed prior results alone does not mechanically yield I-symmetry from symmetry plus abelian units; the corner/direct-finiteness proof supplies that step.

## Scientific value — PASS

PASS. Identifying a newly introduced involution-dependent-looking class with a pre-existing involution-free ring class is a natural classification result. It removes the involution from the property entirely and yields sharp consequences for clean rings and division rings; this is structurally more than a renamed definition.

## Source inspections

- **Symmetry on zero and idempotents** — https://doi.org/10.1080/00927872.2022.2102177. Material read: Complete 12-page primary article, including Lemma 1.3, Remark 3.1 and Theorem 3.3. Assessment: CLOSEST_PRIOR_FULL_TEXT_NOT_COVERING_UNRESTRICTED_CONVERSE. Evidence: It proves I-symmetric implies symmetric and \(U(R)\) abelian, but the converse appears only in special settings such as abelian semiperfect rings.
- **Transposed Triple Products and Pro-Symmetric Rings in star-Rings** — https://arxiv.org/abs/2609.20084. Material read: Complete 11-page primary preprint, especially Proposition 3.13 and Section 4. Assessment: PRIMARY_PRO_SYMMETRIC_SOURCE_NOT_LINKED_TO_I_SYMMETRY. Evidence: It defines pro-symmetry and proves its internal triple-product characterizations but does not mention the I-symmetric class.

## Limitations and residual risks

The theorem classifies the two symmetry notions but does not classify all symmetric rings with nonabelian unit group or provide a structure theorem beyond the stated consequences.

- A still older source using different terminology could contain the unrestricted corner criterion, although targeted searches did not locate one.

## Disposition

**passed**
