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

Run `python3 artifacts/verify.py` using standard Python 3. The script reproduces both sequences, computes the gcd from five exact translated quartic windows, and compares it to the multiplicative-order product for each positive odd \(k<1200\) coprime to five, yielding 960 independent comparisons. Exact five-window sufficiency follows from the order-five integral recurrence proved in `RESULT.md`; it is not an assumption based on experiment. All computations use unbounded Python integers, finite-field-pair arithmetic, and exact GCDs. The code is supplementary; correctness for all odd lengths in scope rests on the written proof. No independent audit is claimed.
