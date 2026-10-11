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

# Verification details

Run `python3 verify.py` using Python 3 with no third-party packages. The exact arithmetic program verifies the \(715\) coefficient identities in the quartic sum-of-squares equation, all \(15\) simple four-cycles of \(K_5\), all \(45\) twofold edge-pair incidences, all \(32\) permitted extremal edge-sign patterns, and the \(L^2\) and \(L^4\) fourth-power data \(10\) and \(640\) for the equal-coefficient witness.

The program is an arithmetic replay of a finite coefficient identity; the proof of nonnegativity follows from visibly squared real polynomials. The invariant Euclidean-position argument is a finite-group averaging proof, not a numerical ellipsoid optimization. No numerical optimizer, statistical significance inference, or unfinished exhaustive search is needed. The conclusion makes no claim for different dimensions, exponents, or complex coefficients.
