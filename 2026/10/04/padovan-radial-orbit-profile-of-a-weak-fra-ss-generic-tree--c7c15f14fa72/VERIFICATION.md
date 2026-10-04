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

`verify.py` enumerates all completed macro-edge words with weights 2 and 3 up to total graph distance 30, appends the four possible terminal states, and counts path codes by distance. It checks the first fifteen radial orbit counts, the recurrence \(q_n=q_{n-2}+q_{n-3}\), the rational generating-function coefficients, the shift to a standard Padovan sequence, and numerical convergence toward the real root of \(x^3=x+1\). `verification_output.txt` ends with `VERIFY_OK`.

The replay checks the enumeration only. The fact that these codes are precisely automorphism orbits is established in `RESULT.md`.
