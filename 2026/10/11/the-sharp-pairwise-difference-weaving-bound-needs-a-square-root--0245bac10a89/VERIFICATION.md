---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the 2021 primary Theorem 4, the step ||a+b||^2<=||a||^2+||b||^2 is false; a cross term is omitted. On any measurable partition, Hilbert direct-integral Minkowski gives E_i(sigma_j;f)^(1/2) <=D_ij(sigma_j;f)^(1/2)+E_j(sigma_j;f)^(1/2) <=(1+sqrt(M))E_j(sigma_j;f)^(1/2), hence each cross-energy <=(1+sqrt M)^2 selected energy. Summing individual K-g-frame lower bounds gives exact lower universal constant A/[1+(m-1)(1+sqrt M)^2], and upper sum B. For each m>=2, M>0, one-point scalar Lambda_1=I, Lambda_i=(1+sqrt M)I for i>=2 and K=I satisfies all pairwise hypotheses (difference squared=M against min{1,c^2}=1) with A=1+(m-1)c^2; assigning point to family 1 gives exact energy 1, equal to corrected lower bound, while published bound A/[1+(m-1)(M+1)]>1. Independently checked m=2,3,5, M=.01,.4,9. This is an exact analytic all-m/all-M counterexample and sharp replacement, not a finite extrapolation.

## originality

PASS

Statement-level comparisons against direct primary mathematical texts found no implication of this full exact claim in the inspected sources; separate specific comparisons below, with documented residual priority risks rather than a negative-search novelty proof.

## value

PASS

Repairs a published quantitative weaving criterion for continuous K-g-frames. The incorrect guaranteed lower stability constant is violated for every m>=2, M>0; the corrected bound is sharp across the whole parameter range and directly changes usable frame reconstruction/stability guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
