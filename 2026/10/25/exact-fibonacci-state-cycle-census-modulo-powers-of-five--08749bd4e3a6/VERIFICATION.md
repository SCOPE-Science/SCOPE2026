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

# Reproducibility and mathematical boundaries

Execute `python3 verify.py` from the same directory as the provided file. No packages beyond the Python standard library are required. The verifier independently enumerates every orbit for moduli 5, 25, 125 and 625, checks all state counts (406900 total), checks fourteen fixed-point counts directly, and compares nine lifted matrices with their predicted prime-five Smith valuations. Expected terminal line: `VERIFY_OK: 406900 enumerated states; 14 fixed-point checks; 9 lift checks`.

The infinite-range proof is in `RESULT.md`, based on the integral matrix lifting recurrence, an explicit determinant and Smith normal form over the five-adic integers. Computer experiments are corroboration, not certification of all exponents. Independently assessed mathematical validation has not been performed.
