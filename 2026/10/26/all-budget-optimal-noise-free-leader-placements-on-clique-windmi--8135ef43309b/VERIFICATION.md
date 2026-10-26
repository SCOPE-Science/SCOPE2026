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

Run `python verify.py` with Python 3.10+ and SymPy 1.10+; `requirements.txt` gives the dependency. The script independently assembles the actual unweighted clique-windmill Laplacian and checks traces of principal inverses against the derived occupancy formula using exact rational arithmetic; it also checks strict conditional minima by enumerating entire small occupancy spaces, exhaustive small three-leader sets, all optimizing counts in those examples, analytic symbolic derivatives and the sharp three-leader regime over multiple parameter ranges.

Recorded exact output is in `verification_output.txt`. Its successful reproduction was checked against the packaged `verify.py` before packaging. Finite computations corroborate, but do not establish, the full infinite-family claim, whose proof is in RESULT.md. The 2020 paper identified in RESULT.md is a significant unresolved originality risk, and no independent mathematical audit has been carried out.
