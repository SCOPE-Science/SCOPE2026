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

# Reproducibility

Run `python verify.py` with Python 3. The script directly enumerates matrices over \(\mathbb F_p\) for \(p\in\{5,7,11,13,19\}\), calculates matrix powers and traces, and partitions eligible matrices by trace and determinant. All expected class sizes and exact-order-six counts are checked with assertions; the script prints `PERIODIC_DERIVATIONS_OK` only if the assertions succeed.

The proof independently establishes the normal form \(D(A,v)\), removal of \(v\) by automorphism, sixth-root restrictions through the resultant, Frobenius stability of eigenvalue pairs, and orbit sizes from centralizers. The tests neither enumerate arbitrary extension fields nor prove the infinite family; they serve as a finite cross-check. No independent audit was performed.
