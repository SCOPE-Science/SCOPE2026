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

Run `python verify_invertible_coordinate_frame.py` in the same directory with Python 3 and NumPy. It enumerates the actual invertible matrices and checks normalizations, entry-by-entry Gram matrices, eigenvalue multiplicities, and the endpoint regime against independent finite-field character evaluations. Six configurations are used: \((q,d)=(2,2),(3,2),(5,2),(2,3),(3,3),(2,4)\). The program terminates with `ALL_CHECKS_PASS` if successful.

The proof's exact rank-two character-sum calculation does not rely on the computation. Strict positivity uses explicit elementary inequalities, and the upper-endpoint transition follows from a polynomial with sign determined by dimension. These derivations cover all prime-power fields, including extension fields not directly enumerated by this prime-field checker. No additional tests, infinite computation, or independent audit are claimed.
