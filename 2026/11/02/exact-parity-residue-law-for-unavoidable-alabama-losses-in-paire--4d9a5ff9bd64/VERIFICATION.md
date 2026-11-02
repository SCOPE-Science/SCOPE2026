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

# Verification and limits

Run `python3 verify.py` with the Python 3 standard library. The verifier independently enumerates legal Hamilton allocations through exact integer quotients, remainders, and every eligible residual-seat subset. It verifies the parity-residue equivalence against the universal two-allocations quantifier over a finite collection of 39,330 parameter-house comparisons. It also compares the exact counting formula with an independent residue-period summation for 1,933 primitive parameter pairs and checks the claimed least-population and first-house witness.

The stated infinite theorem follows from the analytical case distinction and modular counting proof in `RESULT.md`, not from finite enumeration. Exact numerical values, including the \((1,1,4,4)\) transition, are independently reproducible using only the provided files. No external audit or formal proof certification is claimed.
