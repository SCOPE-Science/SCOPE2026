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
# Reproducibility and verification

The proof covers all integers \(m\ge2\). The single included checker, `symplectic_frame_check.py`, requires Python 3 with SymPy and NumPy. From the directory containing the code run `python symplectic_frame_check.py` and require the terminal marker `VERIFY_OK`.

The code independently generates the \(720\) matrices in \(\operatorname{Sp}(4,2)\) using symplectic transvections, checks all \(289\) entries of the constant-plus-coordinate Gram matrix, and verifies its eigenvalues numerically. It directly counts linearly independent symplectic column pairs for dimensions \(4\), \(6\), and \(8\), checks explicit tensor eigenspaces in dimensions \(4\) and \(6\), and symbolically verifies the two decisive determinant factorizations. Integer sign checks over dimensions \(4,6,\ldots,128\) are supplemental tests.

The finite checks do not prove an unrestricted statement. The unrestricted conclusion uses the character-sum identity, symplectic orbit transitivity, tensor decomposition, and exact sign analysis in `RESULT.md`. No external audit or external validation has been performed.
