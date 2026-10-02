---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For differential Ore extensions \(A_h=k[x][t;h(x)\partial_x]\) with nonconstant \(h\), the criterion 'a derivation is locally nilpotent iff its isotropy contains automorphisms of arbitrarily large degree' holds over every characteristic-zero field, while it fails in every positive characteristic already for the locally finite derivation \(E(x)=x,E(t)=0\) on \(A_x\).

## Correctness — PASS

In characteristic zero, the proof uses the known arbitrary-field automorphism description of \(A_h\) and the arbitrary-characteristic-zero classification of locally nilpotent derivations. Affine normalization is valid because the degree is invertible. Reconstructing the source degree comparison shows that unbounded triangular degree first forces \(D(x)\in k[x]\), then forces \(D(x)=0\); the relation and the characteristic-zero centralizer give \(D(t)\in k[x]\), hence local nilpotence. Conversely all such \(D_g\) commute with arbitrary triangular translations. In characteristic \(p>0\), \(E(x)=x,E(t)=0\) respects \([t,x]=x\), is locally finite but never locally nilpotent on \(x\), and commutes with \(t\mapsto t+r(x)\) exactly when \(xr'(x)=0\), which includes all \(r\in k[x^p]\) and yields unbounded degree.

**Checked sources.** assigned RESULT.md at the frozen tree; Baltazar--Lopes--Morales, arXiv:2609.19470; Benkart--Lopes--Ondrus arbitrary-field \(A_h\) structure/derivation papers; Kaygorodov--Lopes--Mashurov 2021

**Residual risks.** The characteristic-zero degree proof is source-specific and depends on nonconstant \(h\); no claim is made for the Weyl or quantum cases.

## Originality — PASS

The motivating theorem is explicitly stated over algebraically closed characteristic-zero fields. Earlier \(A_h\) automorphism/derivation papers work over arbitrary fields, and the additive-group paper works over arbitrary characteristic-zero fields, but searches found no statement combining those inputs into the exact isotropy criterion over all characteristic-zero fields or giving the sharp positive-characteristic Euler/Frobenius counterexample.

### Equivalent formulations

The audited statement is equivalent to removing algebraic closedness from the differential \(A_h\) branch and identifying characteristic as the exact boundary; no prior statement-level match was located.

### Broader coverage

The ingredients are broad, but the audited boundary theorem requires checking that the recent isotropy proof descends and constructing a counterexample in every positive characteristic.

### Exact database or table

A table check is inapplicable; coverage is theorem-level.

### Claim versus prior implication

The final sharp if-and-only-if field boundary is not a formal special case of any checked theorem.

**Source inspections.**
- A Characterization of Local Nilpotence for Derivations of Ore Extensions: Primary abstract and public theorem summary. Assessment: States the \(A_h\) criterion under algebraically closed characteristic zero, not arbitrary fields.
- Actions of the additive group Ga on certain noncommutative deformations of the plane: Open full-text/abstract material stating the field hypothesis and \(A_h\) results. Assessment: Provides arbitrary-characteristic-zero structural input, not the isotropy theorem.
- A Parametric Family of Subalgebras of the Weyl Algebra III. Derivations: Primary abstract and accessible theorem excerpts. Assessment: Works over arbitrary fields and supplies ingredients; does not state the audited isotropy boundary.

**Checked sources.** https://arxiv.org/abs/2609.19470; https://doi.org/10.2478/cm-2021-0024; https://arxiv.org/abs/1406.1508; https://arxiv.org/abs/1210.4631; published-results semantic search

**Residual risks.** The complete 2026 isotropy preprint body was not available through the primary arXiv page during this review. A later revision may remove algebraic closedness independently.

## Value — PASS

The theorem isolates the exact field-characteristic boundary of a new isotropy criterion and shows that positive characteristic fails by a transparent Frobenius mechanism even for a locally finite derivation. This is a motivated structural boundary, not merely a cosmetic hypothesis deletion.

**Checked sources.** Baltazar--Lopes--Morales 2026; arbitrary-field \(A_h\) structure literature; positive-characteristic Ore-extension literature

**Residual risks.** The result does not address iterative higher derivations or classify all positive-characteristic isotropy groups.

## Limitations

- The theorem concerns only the differential Ore-extension family \(A_h\), not all algebras treated in the motivating paper.
- The positive-characteristic result is a counterexample to the ordinary-derivation criterion and does not classify isotropy groups or iterative higher derivations.
- The motivating preprint is very recent, so later revisions remain a priority risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
