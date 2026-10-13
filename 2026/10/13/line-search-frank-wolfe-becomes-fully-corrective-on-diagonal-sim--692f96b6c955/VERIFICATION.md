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
# Checks
The proof was reconstructed symbolically from the face KKT equations and the exact one-dimensional line-search objective. The critical identity checked is
\[
(1-\gamma)x^S+\gamma e_j=x^{S\cup\{j\}}
\]
for
\[
\gamma=\frac{a_j^{-1}}{Z_S+a_j^{-1}}.
\]
This establishes the general result analytically for every dimension, every positive diagonal, every nonempty proper face, and every unseen vertex selected by the standard vertex oracle.

The exact-rational checker `artifacts/verify_fw_diagonal_simplex.py` additionally reconstructs the four-coordinate example with diagonal \((1,2,3,6)\), verifies its line-search parameters and global minimizer, and checks the one-step identity for dimensions \(2\) through \(5\), all diagonal entries in \(\{1,2,3,4\}\), every nonempty proper support, and every unseen vertex choice. Its deterministic output is stored in `artifacts/verification_output.txt` and is `VERIFY_OK`.

# Limits
The finite checker is corroborating evidence, not an exhaustive proof over arbitrary dimension or arbitrary positive real diagonal entries. The theorem relies on the analytic derivation above. The checks do not cover dense Hessians, arbitrary non-face-minimizer starts, inexact line searches, nonvertex tied oracle outputs, or floating-point termination.
