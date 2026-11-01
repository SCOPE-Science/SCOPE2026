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

# Reproducibility and scope

The analytic proof is in `RESULT.md`. The standalone Python 3 script `verify.py` has no third-party dependencies: run `python3 verify.py`. It checks 2,320 fixed-seed diagnostic conditions: central finite differences against the exact individual-vertex derivative, trigonometric-grid quantitative lower bounds, admissible perimeter improvements relative to the proposed bound, and exceptional quadrilateral stations. The expected output is `VERIFY_OK 2320`.

The finite tests do not prove the continuum theorem or certify historical originality. Crucial analytic inputs are the exact factorization of the vertex derivative, the uniform sine-grid extremal bound, the nonparallel chord determinant, and Taylor's theorem with an explicit lower bound on chord length. The theorem is restricted to Euclidean planar ellipses \(a>b>0\) and \(n\ge3\). The sole exceptional case is classified for stationarity, not global optimality.

Independent audit has not been performed.
