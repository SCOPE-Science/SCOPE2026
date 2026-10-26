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

Execute `python3 verify.py` with a standard Python 3 installation. The script enumerates all two-hole configurations in balanced complete tripartite hosts for \(m\in\{4,5,6\}\), checks mutual visibility from its geodesic criterion, and constructs every legal token-sliding adjacency directly. It then checks the degree sequence, connectedness, edge and triangle counts, and the exact matrix identity \(T(T^2-m^2I)(T-2mI)=0\). Since the adjacency matrix is real symmetric, its eigenvalues must be among \(\{-m,0,m,2m\}\); connectedness, the zero trace, and the quadratic trace determine the asserted multiplicities. For \(m\in\{4,5\}\), exact modular Gaussian elimination computes two independent Laplacian cofactors and compares them with the product formula for spanning trees. Expected terminal line: `VERIFY_OK`.

Checks actually completed: every listed test, with `VERIFY_OK`; counts are \(48,75,108\) vertices and \(64,125,216\) triangles for \(m=4,5,6\). The checked spanning-tree congruences use primes \(1000000007\) and \(1000000009\). Modular congruences are finite cross-checks and do not on their own certify the exact formula for all parameters. The all-parameter proof is the orthogonal decomposition and Kirchhoff's theorem in `RESULT.md`.
