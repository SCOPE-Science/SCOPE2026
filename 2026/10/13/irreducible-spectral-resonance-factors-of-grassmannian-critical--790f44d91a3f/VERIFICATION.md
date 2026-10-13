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

The exact stand-alone program `verify.py` uses only the Python 3 standard library. Execute `python3 verify.py` in the directory containing this file to check the discriminant factor formula in integers for \(n=4,5,6,7\), every \(1\le k<n\), and two spectral specializations per case, together with the small cubic and a distinct-eigenvalue/double-critical-value example. Expected output: `VERIFY_OK`.

The universal theorem does not depend on finite enumeration. Its proof uses exact orbit-transitivity in the symmetric polynomial ring and an exhaustive-by-bijection partition of all pairs of \(k\)-subsets. No computation of the full matrix-entry factorization is claimed. The term 'irreducible' always refers to the coefficient ring \(\mathbb C[e_1,\ldots,e_n]\). The real equal-distance witness does not imply a tied global optimum.
