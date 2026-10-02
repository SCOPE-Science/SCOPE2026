# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The unit-group necessity follows by applying I-symmetry to a triple product equal to one: the transposed product is an invertible idempotent and hence one. For the converse, symmetry makes the idempotent \(p=abc\) central and forces \(q=acb\) into the corner \(pRp\). Reversibility makes this corner directly finite; from \(ABC=p\) the corner factors are units. Centrality embeds the corner unit group into \(U(R)\), so abelianness forces \(ACB=ABC=p\). Thus I-symmetry is exactly symmetry plus an abelian unit group. For a ring with involution, I-symmetry immediately implies pro-symmetry, while pro-symmetry supplies symmetry from Chen--Wang--Zou and supplies abelian units by the same triple-equals-one argument, giving the converse. The clean-ring, division-ring, and free-algebra examples follow correctly.

Originality: PASS. Two highly relevant primary sources were read in full. Han--Lee--Lee prove that I-symmetric rings are symmetric and have abelian unit group, and prove the converse only under extra hypotheses such as abelian semiperfectness; their full 12-page paper does not state the unrestricted criterion. Chen--Wang--Zou introduce pro-symmetric rings, prove they are symmetric, and characterize the projection triple condition, but their full 11-page preprint neither cites I-symmetry nor identifies pro-symmetry with it. The audited theorem supplies the missing unrestricted converse and then links the two literatures. Resultary search found no earlier published record with this identification.

Scientific value: PASS. Identifying a newly introduced involution-dependent-looking class with a pre-existing involution-free ring class is a natural classification result. It removes the involution from the property entirely and yields sharp consequences for clean rings and division rings; this is structurally more than a renamed definition.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
