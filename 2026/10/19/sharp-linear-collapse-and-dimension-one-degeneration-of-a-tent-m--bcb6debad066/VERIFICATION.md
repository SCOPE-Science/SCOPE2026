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

## Reproducibility

Run `python verify.py` with Python 3 and SymPy installed. The checker uses exact fractions and symbolic linear solves, and should print `VERIFY_OK 246`.

It reconstructs all tent period-\(m\) points in dyadic cylinders for six rational values of the memory parameter, solves the cyclic affine equations exactly, checks that the solved points obey the genuine tent branches, and checks the explicit period-two orbit and an unstable-cone inequality over all sign itineraries of length seven. It does not claim exhaustive verification for infinitely many parameters or itineraries. The universal estimates in `RESULT.md` are analytic arguments.

## Limits

No independent audit or external mathematical certification has been carried out. Model-specific historical priority remains provisional despite inspecting the principal full-text reference and searching known comparable results.
