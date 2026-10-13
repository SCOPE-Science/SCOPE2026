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

`verify.py` uses exact rational arithmetic and returns `VERIFY_OK` when the packaged witness and algebraic coefficient checks agree with the theorem. It verifies the two eigenmodes of the explicit witness lie strictly inside the unit disk, reconstructs the first three iterates and exact solution, and checks the coefficient identity that yields the third-iterate off-diagonal formula.

The universal threshold is not inferred from finite testing. It follows from the exact identity
\[
(q_3(C))_{ij}=\omega^2\left((3-2\omega)g_{ij}+\omega\sum_{\ell\ne i,j}g_{i\ell}g_{\ell j}\right)
\]
for unit-diagonal SPD Stieltjes \(C\), together with positivity of \(q_3(C)\) on the convergent spectral interval. The verifier only replays the algebraic witness and coefficient bookkeeping.

No claim is made about all later iterates, nonsymmetric matrices, changing weights, or nonzero initial vectors.
