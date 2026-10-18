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

# Verification and reproducibility

Run `python verify_weighted_iso.py` with Python 3; it requires only the standard library. The reference implementation of weighted pooled-adjacent-violators regression and independently evaluated interval block norms check representative nonuniform weights for dimensions 2 through 8 and ordinary \(\ell_p\) input/output norms with \(p\in\{1,3/2,2,3,4,11,\infty\}\). For each sample it verifies all-pairs upper bounds on independently drawn data and constructs small-perturbation witnesses realizing the claimed maximizing local block norm. The script also enumerates endpoint weight profiles, verifies the exact \(\ell_1\) contrast envelope, and compares the asymptotic envelope with its one-parameter optimizer for fixed exponents and contrast ratios.

Expected output: `WEIGHTED_ISOTONIC_VERIFY_OK 5252`. This result was obtained with the embedded script. A finite collection of floating-point assertions does not certify the continuum over weights, all exponents, all data vectors, or infinite-dimensional limits. The proof in `RESULT.md` supplies those mathematical arguments: finite polyhedral block realization, dual norm equality, extreme-point maximization, and one-variable calculus. No independent audit or external formal certificate is claimed.
