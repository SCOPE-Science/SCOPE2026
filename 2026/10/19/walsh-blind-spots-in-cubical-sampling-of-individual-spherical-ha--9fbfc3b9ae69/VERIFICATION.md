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

# Verification summary
The proof identifies the image using explicit harmonic witnesses and trace exclusions for arbitrary dimensions at least six. A standalone exact checker is included as `check_hypercube_harmonic.py`. Run it with `python check_hypercube_harmonic.py` and SymPy installed.

The checker expands \(C_\ell^{(d-2)/2}(t)\) exactly and diagonalizes its cube-vertex kernel in the Walsh basis by the integral Krawtchouk sums. For each dimension 6 through 10 it examines all degrees zero through dimension plus two, and all Walsh weights. It verifies exact zero/nonzero patterns, positivity of each nonzero eigenvalue, rank equality, and the identity \(P_6(1/\sqrt3)=2/9\). Total: **505 rational eigenvalue tests**.

The finite tests do not establish the theorem in arbitrary dimensions, or establish priority in historical literature. The full proof is in `RESULT.md`. No independent audit or third-party certification has been performed.
