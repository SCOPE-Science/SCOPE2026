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

The analytic proof reduces the partial transpose to two positive scalar blocks and \(n-1\) independent \(2\times2\) Hermitian blocks. For each block, positive trace and the exact determinant
\[
\frac14\left(p_{k-1}p_{k+1}-p_k^2\right)
\]
determine its inertia completely.

The bundled `verify_inertia.py` uses only Python standard-library exact rational arithmetic. It reconstructs the matrix entries of the partial transpose for representative rational families and confirms the claimed direct-sum block pattern. It then checks exact determinant signs for normalized binomial weights through several dimensions and exact determinant equalities for normalized geometric weights.

The finite checker does not prove the universal quantifier over \(n\). The all-dimensional conclusion rests on the displayed symbolic block decomposition, determinant sign test, and the elementary binomial-ratio identity.

No independent audit has been performed.
