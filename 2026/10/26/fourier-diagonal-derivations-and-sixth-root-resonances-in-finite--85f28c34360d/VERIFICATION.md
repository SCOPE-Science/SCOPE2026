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
# Reproducibility and limitations

Execute `python3 verify.py` in the directory containing the standalone verifier. The script uses only the Python standard library and returns `VERIFY_OK cases= 15` after comparing the full \(p^2\)-variable Leibniz equation rank (for \(p=3,5,7\)) with the Fourier-diagonal rank; for selected \(p=11,13\), it compares the Fourier-diagonal rank with exact discrete logarithm congruences. The rank computation is performed modulo the auxiliary prime \(1009\), not over \(\mathbb C\). Therefore these checks are finite corroboration, not universal derivation proofs, independence tests, or exhaustive arbitrary-prime certification. The general result is justified by the explicit Fourier multiplication and the zero-product Leibniz argument in `RESULT.md`, independently of this program. The characteristic restriction and the uninspected related 2026 full texts are documented there.
