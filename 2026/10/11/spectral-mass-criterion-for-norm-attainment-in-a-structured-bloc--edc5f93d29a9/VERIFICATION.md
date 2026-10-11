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

The focal source was inspected in full HTML form at the passages defining the norm formula and maximizing set, the singleton necessity lemma, the eigenvalue sufficiency lemma, the main strict-monotonicity theorem, and its examples. A second block-operator paper on absolute norm attainment was inspected as a broader-coverage check.

For correctness, the argument was replayed from the spectral theorem for \(B=|A^*|\): the reduced block operator is the direct integral of the finite matrices \(M_t\), and equality in the norm bound is equivalent to nonzero spectral support on \(\Omega\) together with the fibrewise top singular subspace. The singleton case was checked to reduce to a nonzero atomic spectral projection, hence an eigenvalue.

The explicit multiplication-operator example was checked symbolically. No numerical experiment is used as an infinite-dimensional proof. The result does not cover arbitrary noncommuting block matrices, and an older decomposable-operator formulation remains a literature risk.
