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

# Reproducibility and evidentiary limits

Run `python3 artifacts/verify.py` from the directory containing the embedded files. SymPy is needed; the script uses integer polynomial arithmetic reduced modulo \(2\). The included `artifacts/verify_output.txt` records an actual execution of the embedded script.

The verifier reconstructs the determinant and its six derivatives, checks the cubic is in the derivative ideal, computes that every product of the three off-principal Veronese minors vanishes modulo the quadrics, checks the affine square-zero generator identity, and independently compares Hilbert functions for degrees \(0\) through \(14\). It prints `ALL_CHECKS_PASSED` if these checks all succeed.

The global non-splitting proof, finite-duality identification of the canonical ideal, and extension-class classification are mathematical arguments in RESULT.md, not properties certified by a finite run or an external formal proof. Historical originality remains provisional. Independent scientific review has not been performed.
