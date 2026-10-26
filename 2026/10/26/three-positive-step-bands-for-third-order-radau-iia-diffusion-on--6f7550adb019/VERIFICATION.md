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

# Verification record

`verify.py` performs exact-rational comparisons of the four spectral-projector entry formulas with the matrix identity \((6I+4hL_m+h^2L_m^2)T_m(h)=6I-2hL_m\) on 176 size/step combinations. It also checks conservation, symmetry, entry-sign polynomial identities, the strict off-diagonal signs for positive steps, exact \(m=11\) hub endpoints and negative polynomial witnesses for every sampled \(m\ge11\). `verification_output.txt` contains the output of the actual run.

The general theorem is proved by symbolic spectral projectors, elementary sign certificates, and Descartes' rule; no finite sample establishes the root counts universally. Reported decimal roots are numerical illustrations, not exact definitions or external certificates. The full claims concern unweighted stars, completed two-stage Radau IIA steps, and nonnegative initial data, not intermediate stages or global integration error.
