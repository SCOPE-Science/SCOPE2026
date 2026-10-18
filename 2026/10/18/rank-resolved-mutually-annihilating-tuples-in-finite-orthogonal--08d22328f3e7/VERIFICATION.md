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

The standalone `checker.py` uses only the Python standard library. Running `python3 checker.py` performs direct prime-field matrix enumeration for \((n,q,k)=(3,3,2),(4,3,1),(4,3,2),(4,5,2),(5,3,1),(5,3,2)\), enforcing all ordered zero products and checking actual joint-image ranks against the closed formula. All six tests passed. It also checks the explicit split six-dimensional, rank-three joint-image witness over \(\mathbf F_3\), the split/non-split rank profiles in dimension six, and positivity/integrality across additional parameters. Its terminal success marker is `CHECKER_OK`.

The mathematical proof is independent of the enumerated cases: it uses isotropic joint images, the alternating-form correspondence, subspace-lattice Möbius inversion, and orthogonal flag counting. The checker only enumerates prime fields and small matrices; it does **not** establish the theorem for arbitrary prime powers or all dimensions. No independent mathematical audit has been performed.
