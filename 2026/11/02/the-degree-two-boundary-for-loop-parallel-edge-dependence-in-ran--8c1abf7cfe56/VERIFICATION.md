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

# Verification of the finite-size configuration covariance theorem

The self-contained `verify.py` requires only Python 3 standard-library modules. Invoke `python verify.py`. Its execution checks 63 nondecreasing degree profiles by independently enumerating every perfect matching of distinguishable half-edges, 4,023 degree profiles against the rational sign/decomposition identity, and 344 regular-degree formulas. The exact run returned: `OK: 63 independently enumerated degree profiles; 4023 finite sign/decomposition profiles; 344 regular-degree identities`.

The mathematical proof separately establishes: (1) the loop-conditioning mixed moment; (2) an exact algebraic decomposition of the covariance numerator; (3) nonnegativity of each three-vertex term by AM–GM; (4) compensation for every negative two-degree pair; and (5) an explicit parity argument for degree-one vertices. This finite test program is a check of low-order cases and arithmetic, not an exhaustive proof for arbitrary size. No independent scientific audit has been performed.
