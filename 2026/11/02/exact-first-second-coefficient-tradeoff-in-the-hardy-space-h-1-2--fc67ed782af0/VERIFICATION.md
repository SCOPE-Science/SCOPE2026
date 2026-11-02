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

The analytical proof is in `RESULT.md`; `CHECK.py` is a reproducible supplementary checker requiring the packages listed in `requirements.txt`. From a directory containing those files, execute `python CHECK.py`. A successful run prints `CHECK_OK 92`.

The checker independently differentiates the rational two-parameter objective symbolically, establishes the identity of its stationary numerators with the claimed quartic, verifies the endpoint polynomial evaluations and exact coefficient constants, and compares finite-weight solutions to constrained numerical optimization with several starts. It also checks the normalization on a 4096-point boundary grid and the absence of polynomial roots in the closed disk for those tested weights. None of these finite tests proves the infinitely quantified inequalities; the analytical steps use the outer-extremal theorem, compactness, Descartes' sign rule and a zero-free homotopy. Strict convexity and equality rigidity are likewise analytical consequences, not software certificates.

Independent audit: not performed. Computational libraries and floating-point tolerances may produce small platform-dependent variations in numerical diagnostics; their scope is supplementary.
