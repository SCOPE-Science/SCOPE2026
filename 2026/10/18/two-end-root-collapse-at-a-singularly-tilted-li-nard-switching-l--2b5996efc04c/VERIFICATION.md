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

# Analytical verification and limits

The model is explicitly given in `RESULT.md`; no external data or source files are required for the proof. The first-order radial average is the integral over one unperturbed revolution divided by \(2\pi\). The derivative of the switched semicircle primitive yields \(4\sin^{2j+1}\phi/(2j+1)\), while the smooth term is the beta integral \(\binom{2j}{j}/[2\cdot4^j(j+1)]\). The local inner and outer branch limiting equations are affine and binomial, respectively, each with a simple positive root when its sign hypotheses hold; a subsequence argument rules out all other roots. Positive finite limiting radii require the stated simplicity of roots of \(F\).

The included executable `verify.py` uses only Python 3's standard library. Execute `python3 verify.py` from the extracted package directory. Its 204 diagnostic assertions compare numerical angular quadratures against the polynomial formula and test root-bracket and scaling predictions. Finite diagnostics do not prove any universal assertion; the analytical proof does. The positive-root theorem does not rule out high-order cycles or give a perturbation bound uniform in the angle.
