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

# Reproducibility and boundaries

Execute \(\texttt{python verify.py}\) with NumPy available. The reported run returned `VERIFY_OK 7214 finite-dimensional identities; analytic ratio moment checks`.

The script covers dimensions \((d,r,\ell)=(3,1,1),(3,1,2),(3,1,3),(5,2,2),(5,2,3),(5,2,4),(5,2,5),(7,2,4)\), with 180 seeded random matrix instances in each case. It computes the coefficient-pseudoinverse solution and independently constructs an orthonormal basis for the same random subspace before solving for the physical-minimum solution. It checks residual feasibility, minimum-norm ordering, full-span collapse and a deterministic two-dimensional witness. For the chi-squared ratio, it tests the exact Gamma moment expression and its second-moment simplification.

The computations are **not** proof of a distribution identity, exact tail limit or infinite moment. Those are proved in `RESULT.md` using orthogonal invariance, the Gaussian Schur complement and Gamma integrations. Results assume exact arithmetic; floating-point calculations are only numerical sanity checks. The literature comparison is not an independent audit.
