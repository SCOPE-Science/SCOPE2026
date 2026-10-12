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
The proof establishes the unrestricted theorem. Run `python3 verify.py` with Python 3; no external packages are required. The included `verification_output.txt` is the output from an actual execution of the embedded script. For each modulus 1 through 1000 the test enumerates the complete 2m-index period, checks every fiber and its support, and recomputes the exact second-moment formula; for moduli 1 through 299 it verifies moment orders 1 through 6. The prime-power alternating sums are separately checked for eight odd primes and exponents 1 through 7. The verifier is finite and cannot establish that the formulas hold for arbitrarily large moduli; that is supplied by the CRT and valuation proof. No independent verification has been performed.
