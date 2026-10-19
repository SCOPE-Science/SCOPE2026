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

# Mathematical verification

The supplied `verify.py` performs exact symbolic determinant comparisons for the four positive-field regimes (five rational representatives), independent direct Hamiltonian recolouring tests for lengths three through eight at all five representatives, and the critical-polynomial remainder check. Its successful observed output was `PASS 5 exact characteristic polynomials; 30 exhaustive finite-length count comparisons; polynomial identity verified`.

Finite checks do not establish all-size correctness; the proof uses the local minimization criterion, closed-walk transfer bijection, nonzero-domain/zero-run renewal decomposition, and Perron asymptotics. The review is same-model only; no independent audit was performed.
