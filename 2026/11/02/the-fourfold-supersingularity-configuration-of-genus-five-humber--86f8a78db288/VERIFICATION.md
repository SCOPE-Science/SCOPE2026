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

# Verification and limitations

Run `python3 verify_humbert23.py` with a Python 3 interpreter and no third-party packages. The attached `verification_output.txt` is the output of an actual successful run from the packaged source, ending in `VERIFY_OK`.

The program constructs \(\mathbb F_{23^2}=\mathbb F_{23}[t]/(t^2-5)\), verifies the exact degree-eleven Hasse factorization with nine linear factors and one irreducible quadratic, and exhaustively enumerates all \(110\) ordered pairs of distinct geometric supersingular roots. It separately checks the \(72\) ordered pairs of rational roots, all \(420\) smooth marked pairs over \(\mathbb F_{23}\), and all \(277202\) smooth marked pairs over \(\mathbb F_{23^2}\). It checks pairwise tangent independence at every higher-multiplicity point and the \(60\)-point relabeling orbit.

The statements over every extension and over the algebraic closure additionally use the printed proof of reduction to supersingular root pairs, the algebraic group-character quotient decomposition, and symmetric double counting; no higher extensions are exhaustively enumerated. The checker is not an external or independent scientific audit.
