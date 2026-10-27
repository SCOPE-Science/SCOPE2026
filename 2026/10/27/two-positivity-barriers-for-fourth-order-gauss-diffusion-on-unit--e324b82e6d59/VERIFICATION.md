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

# Verification record

The exact symbolic checker is `artifacts/verify_gauss_path.py`. Run `python3 artifacts/verify_gauss_path.py` from the package root with SymPy installed.

The checker reconstructs the path Laplacians and the [2/2] Padé matrices from their definitions, checks every independent four-node symbolic entry factorization, and verifies that the defining quartic has one positive root in a narrow exact-rational isolation interval. It checks both- and three-node entries, the first relevant Taylor coefficients, and the entire eight-by-eight rational matrix at step four against an explicit integer certificate with minimum numerator 596772 and denominator 61423369. It also verifies finite instances of the path pseudoinverse identity.

These exact finite checks passed. The symbolic script does not replace the proof for unbounded path order: the small-step statement uses a uniquely contributing walk of length seven and a negative Taylor coefficient; the large-step statement uses the path effective-resistance formula and a spectral asymptotic. The analysis concerns the completed matrix, not internal stages. No external independent validation has been performed.
