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

# Reproducibility and limits

Run `python3 artifacts/verify.py` using Python 3 standard library only. The program constructs \(U_n(P,-1)\) by integer recurrence, evaluates direct Möbius transforms of prime parts, and checks them against the theorem for every even parameter \(2\le P\le18\), every prime \(p\le53\), and every \(1\le n\le120\). It also checks the valuation formula for each odd prime, exact nonnegative support and the claimed least repair's sufficiency at the tested indices.

The expected replay output is in `artifacts/verification_output.txt`. Exhaustive finite comparisons cannot establish the infinite theorem and do not independently verify bibliographic originality. Proof of the global theorem is in RESULT.md. No independent external audit has been performed.
