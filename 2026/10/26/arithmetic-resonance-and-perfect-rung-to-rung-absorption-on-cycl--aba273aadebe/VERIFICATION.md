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

The `verify.py` file is a standalone finite checker (NumPy and SymPy needed). Running `python verify.py` prints `PASS 128 analytic/spectral/independent-integer-Krylov checks`.

Actual tests include: direct \(2n\times2n\) adjacency construction; eigenprojector reconstruction of the dimension of the sink's local cyclic subspace and source survival for every \(3\le n\le42\); independent explicit collision lists for the shifted cosine branches; and exact integer Krylov ranks for \(n=3,\ldots,10\).

The all-integer proof of the collision classification uses exact Ramanujan sums and the inequality \(\alpha_u^2\le2\alpha_u\) for nonnegative real cyclotomic conjugates. These analytic steps are checked in the accompanying proof, not assumed based on numerical matrix diagonalization. Floating-point tests do not certify equality of close algebraic eigenvalues in arbitrary dimensions. The independent integer ranks check small instances only.

The supplied source code was executed directly from its packaged path and returned the documented PASS count. No external independent audit has been performed.
