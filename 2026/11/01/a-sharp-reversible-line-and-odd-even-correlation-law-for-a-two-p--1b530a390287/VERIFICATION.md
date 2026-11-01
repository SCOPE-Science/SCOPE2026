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

Run `python verify_noisy_pca.py` with Python 3 and NumPy. The script constructs the product transition kernel from the neighborhood table (not from the Ising formula), enumerates all states for \(N=3,\ldots,8\), checks the nonreversible three-configuration cycle ratio for multiple \(p,r\), and compares the explicit invariant law to full-state transition/detailed-balance and correlation calculations. It further checks that the whole even and odd sublattice configuration distributions factorize on even cycles and computes the exact magnetization susceptibility. The executed file printed `PASS: 1269 finite checks`.

The all-\(N\) proof is the Kolmogorov cycle calculation, the reversible heat-bath identity, and the two-eigenvalue transfer-matrix calculation stated in `RESULT.md`. No finite enumeration establishes arbitrary-\(N\) validity or historical novelty. Independent scientific audit has not been performed.
