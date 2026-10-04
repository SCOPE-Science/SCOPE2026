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

# Verification

The analytic proof establishes the claim. `verify.py` checks representative instances without external packages:

- the state \\((I\\otimes R_y(\\theta))|\\Phi^+\\rangle\\) has maximally mixed one-qubit reductions and numerically matches \\(F_Q=2(1+\\cos\\theta)\\);
- an even-qubit tensor product of singlets has \\(E_{{\\mathrm D}}=N\\) and \\(F_Q[J_z]=0\\);
- the corresponding GHZ state has \\(E_{{\\mathrm D}}=N\\) and \\(F_Q[J_z]=N^2\\).

These finite checks are consistency tests only. The continuous interval and all-even-\\(N\\) conclusions are proved symbolically in `RESULT.md`.

Scientific source comparison includes arXiv:2609.11720v1, DOI 10.1088/1751-8113/47/42/424006, DOI 10.1103/PhysRevLett.100.100503, and targeted semantic searches. The remaining access limitation is recorded in `RESULT.md`, `REVIEW.md`, and `AUDIT.json`.
