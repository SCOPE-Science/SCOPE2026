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

# Reproducing the exact certificate

Extract `certificate.py` and `certificate_output.txt` from this finding's embedded file list without changing their bytes. Execute `python3 certificate.py` using Python 3 with only its standard library. The program ends by printing `CERTIFICATE_OK` and all seven earlier exact check values. Compare its stdout with `certificate_output.txt`.

The proof in `RESULT.md` establishes that every squarefree three-prime candidate below the exhibited witness appears in the bounded prime-factor enumeration. `certificate.py` deterministically sieves primes, fully factors \(F(p)\) and \(F(u)\), checks all possible closing primes, and independently checks the three witness primes and the reciprocal-gcd sum. It uses integer arithmetic throughout.

The actual verified output is saved in `certificate_output.txt`. The script was executed directly from the packaged content and produced the exact expected output. Its check asserts the global product minimum only because the paper proof justifies the finite search boundary. No assertion concerns larger products or an unrestricted minimum over integers of every prime-support size.

Self-review covers the stated computation and its use in the proof. No independent audit has been carried out.
