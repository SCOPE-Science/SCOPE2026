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

Run `python verify.py` with Python 3.8 or newer; there are no external dependencies. The checker enumerates all ordered orthonormal bases in dimensions \(3\) and \(4\) by a backtracking search over odd-weight columns and direct orthogonality tests. The computed counts are \(6\) and \(48\), and all nonzero defining vectors have exactly the predicted attainable graph target sizes. For dimensions \(3\) through \(9\), the checker independently enumerates orbits under swaps and four-coordinate transvections and compares each complete visited set with the proposed orbit description. It prints `VERIFY_OK` on success.

These finite tests verify the implementation and low-dimensional cases, not the full theorem. The unrestricted correctness argument is the explicit orthogonal-group orbit reduction and the characterization of all natural bases in RESULT.md. None of the computations assesses independent audit status.
