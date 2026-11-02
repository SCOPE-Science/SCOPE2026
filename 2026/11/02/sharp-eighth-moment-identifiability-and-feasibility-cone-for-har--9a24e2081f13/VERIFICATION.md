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

# Reproduction and limits

Execute `python3 VERIFY.py` from the package root. Python 3 standard library is sufficient. The program independently solves the stationary joint-generator recurrence (without using the beta-density integral) and compares exact rational moments to the closed beta-mixture formula. It evaluates 144 rational configurations with six successive even moments per configuration (orders 2 through 12), checks the sixth identity and parameter reconstruction, and demonstrates one exact pair of indistinguishable lower-moment parameter triples. Its printed success report was observed in this scientific review.

The checker tests only finitely many points; a proof for all positive real parameters is in RESULT.md. No empirical finite-sample statistical guarantees are claimed. No independent audit has been performed.
