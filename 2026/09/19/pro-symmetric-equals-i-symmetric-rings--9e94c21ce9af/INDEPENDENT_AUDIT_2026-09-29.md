# Independent audit — 2026-09-30

## Disposition: PASSED

Record: `2026/09/19/pro-symmetric-equals-i-symmetric-rings--9e94c21ce9af`

### Correctness
PASS. The equivalence survives independent reconstruction. Han–Lee–Lee already prove that I-symmetry implies ordinary symmetry, equality of transposed idempotent triple products, and an abelian unit group. For the converse used here, if p=abc is idempotent in a symmetric ring, reversibility makes idempotents central and the symmetry identities force q=acb into pRp. The corner pRp is reversible and hence directly finite; ABC=p then makes A,B,C units in the corner. Because p is central, U(pRp) embeds by x↦x+(1-p) into U(R); an abelian U(R) therefore gives ACB=ABC=p. The pro-symmetric equivalence follows from the same unit commutator substitution together with the source result that pro-symmetry implies symmetry.

### Originality
PASS, qualified to the inspected evidence. The strongest prior-art risk was resolved rather than left implicit: after open-access attempts failed to supply the complete Han–Lee–Lee article, the authorized institutional copy was obtained and all 12 pages were inspected. That paper proves I-symmetric ⇒ symmetric and U(R) abelian, the equality formulation, the abelian-semiperfect collapse, and the free-algebra example, but it does not state the unrestricted converse symmetric + abelian unit group ⇒ I-symmetric and predates the 2026 pro-symmetric notion. The current Chen–Wang–Zou preprint introduces pro-symmetry and states only that every pro-symmetric ring is symmetric. No earlier statement of the unrestricted criterion or involution-independence was located.

### Scientific value
PASS. The theorem gives a clean intrinsic classification of a newly introduced projection condition, removes dependence on the involution, and turns several examples and special cases into immediate structural consequences. The contribution is a concise classification theorem rather than a merely computational observation.

### Independent findings
- Full-text inspection of Han–Lee–Lee confirms Lemma 1.3(2)-(4): I-symmetric rings are symmetric, have equality under the relevant transposition, and have abelian unit groups.
- Han–Lee–Lee Theorem 3.3 is only the abelian-semiperfect equivalence and does not supply the unrestricted converse used in the SCOPE theorem.
- The corner argument proving symmetric + abelian U(R) ⇒ I-symmetric is algebraically sound.
- The current pro-symmetric preprint's public statement stops at pro-symmetric ⇒ symmetric, so the identification with I-symmetry remains a genuine strengthening on the inspected evidence.

### Independent checks
- Reconstructed the central-idempotent and corner reductions without relying on the filed review.
- Checked direct finiteness of the reversible corner and the central-corner unit embedding.
- Used the substitution a=v^{-1}u^{-1}, b=u, c=v to rederive abelianity of U(R).
- Obtained and read the complete Han–Lee–Lee paper through authorized institutional access after open-access full text was unavailable.

### Literature evidence
- https://doi.org/10.1080/00927872.2022.2102177 — Han–Lee–Lee, Symmetry on zero and idempotents; complete 12-page article inspected via authorized institutional access.
- https://arxiv.org/abs/2609.20084 — Chen–Wang–Zou current pro-symmetric preprint; public v1 statement introduces pro-symmetry and proves pro-symmetric rings are symmetric.
- https://doi.org/10.1080/00927872.2018.1513011 — Alghazzawi–Leroy symmetric-subset background.

### Limitations
- Priority remains qualified against obscure terminology outside the targeted I-symmetric/pro-symmetric literature, although the closest pre-2026 source was fully inspected.
- The free-algebra I-symmetric example itself is already in Han–Lee–Lee; novelty is not assigned to that example apart from its reinterpretation through the new classification.
