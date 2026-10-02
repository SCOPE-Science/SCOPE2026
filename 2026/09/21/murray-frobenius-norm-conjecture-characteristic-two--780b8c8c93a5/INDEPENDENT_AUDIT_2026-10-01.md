---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

Over every field of characteristic two, \(k[t]/(t^{2d})\) with its standard Frobenius form and the twist by \(1+t\) satisfies Murray's central norm condition but gives nonhomothetic forms; the case \(d=1\) is a dimension-two, dimension-minimal counterexample to Conjecture 16.

## Correctness — PASS

The coefficient-of-\(t^{2d-1}\) form on \(k[t]/(t^{2d})\) has reverse-identity Gram matrix and is Frobenius; commutativity makes its Nakayama automorphism the identity, so the norm of \(u=1+t\) is the central unit \(u\). In characteristic two every square has only even powers, so the standard form is alternating, whereas the twist has \(B_u(t^{d-1},t^{d-1})=1\). Alternation is preserved by homothety, so the forms are not homothetic. Dimension one cannot furnish a counterexample because every nondegenerate bilinear form on a one-dimensional algebra is homothetic.

**Checked sources.** assigned RESULT.md at tree 58ffb14105552a3169bde98f9f9ea7a2d144391f; Murray, Bilinear Forms on Frobenius Algebras, full arXiv text

**Residual risks.** No correctness defect was found.

## Originality — PASS

Murray's full primary text states Theorem 15's necessary central-norm condition and then Conjecture 16 as its unrestricted converse. Targeted searches for the conjecture, characteristic-two failures, dual numbers, and truncated-polynomial examples found no published correction or equivalent counterexample.

### Equivalent formulations

The alternating/nonalternating obstruction is an equivalent homothety-invariant formulation of failure of the conjectured implication.

### Broader coverage

The current family fills a genuine boundary left open by the stated conjecture.

### Exact database or table

No finite database/table is relevant; the witness is a symbolic family valid over every characteristic-two field.

### Claim versus prior implication

This is a direct counterexample to the original universal statement, not a special case of a known failure.

**Checked sources.** https://arxiv.org/abs/1401.6486; https://doi.org/10.1016/j.jalgebra.2005.07.031; Resultary semantic search

**Residual risks.** The construction is elementary enough that a differently phrased antecedent in bilinear-form literature remains possible.

## Value — PASS

The result gives a dimension-minimal counterexample to a published 2005 conjecture, extends it uniformly to every positive even dimension, and identifies alternation in characteristic two as the missing invariant. This is a motivated boundary/counterexample, not a routine recomputation.

**Checked sources.** Murray Theorem 15 and Conjecture 16; current symbolic family

**Residual risks.** It does not propose a complete corrected converse.

## Limitations

- The theorem refutes the converse only in characteristic two.
- It does not settle corrected converses in other characteristics or the general nonsymmetric case.
- Originality remains best-of-knowledge because the elementary example may have an unindexed antecedent.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
