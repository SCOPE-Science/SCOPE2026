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

# Reproducible checks

Run `python3 verify.py` with Python 3. The program uses only the standard library and generates all verification data; it does not require source downloads or network access. The accompanying `verification_output.txt` is the output obtained from running the included version of the script.

The verifier constructs incidence forests using disjoint-set union independently of the arithmetic criterion, compares three independently organized finite counting methods, checks the exact totient decomposition and tests successive sparse extensions. The analytic estimate \(O(N^2)\) and the totient harmonic asymptotic follow from the written proof, not from extrapolation of finite data.

The checks do not constitute an independent audit, nor do they demonstrate that no equivalent result exists in uninspected literature.
