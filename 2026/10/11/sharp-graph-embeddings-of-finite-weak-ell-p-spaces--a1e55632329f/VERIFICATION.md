---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The exact proof was replayed from the definitions.

For the source unit ball, \(\|x\|_{p,\infty}\le1\) is equivalent to \(x_j^*\le j^{-1/p}\). The finite rearrangement inequality gives
\[
|L_a(x)|\le\sum_{j=1}^m a_j^*j^{-1/p},
\]
and choosing coordinate phases to align with the coefficients and moduli \(j^{-1/p}\) gives equality.

Sufficiency was checked by adjoining a coordinate of modulus at most \((m+1)^{-1/p}\): every target order statistic stays below its defining threshold. Necessity was checked on the equality vector: if the added coordinate exceeded that threshold, all \(m+1\) target coordinates would exceed it and the target quasi-norm would be greater than one.

The disjointness criterion was checked directly: two nonzero coefficients produce disjoint basis vectors whose images share the last coordinate; with at most one nonzero coefficient, disjoint vectors cannot both have a nonzero last coordinate.

The focal PDF was inspected at the definition of weak \(\ell_p\) and Remark 1.1. Its coefficient is exactly the \(m=2\) equal-coefficient equality case. No computational experiment is used to justify the infinite family. Random finite tests across several exponents and dimensions were supplementary stress checks only.

No claim is made about arbitrary non-surjective isometries, higher-codimension graph maps, or noncommutative weak-\(L_p\) spaces.
