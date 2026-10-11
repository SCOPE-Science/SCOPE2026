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

# Reproducible checks
Run `python3 verify_grotzsch.py` and `python3 check_homology.py` from the directory containing the two scripts. No third-party dependencies or precomputed data files are needed.

The first script checks the graph construction, all matching faces, complete oriented face-poset acyclicity, signed integral cancellation, and the \(5\times5\) determinant \(-1\). The second independently enumerates graph edges and simplices and calculates boundary ranks modulo two, three and five. Exact expected face numbers are \((20,135,365,360,87)\), and boundary ranks are \((19,116,249,87)\) in each of the three characteristics. The integral homotopy conclusion relies on the signed Morse differential, not the finite-field tests alone.

Checks establish this one fully specified finite complex; no infinite-family assertion or independent review is supplied.
