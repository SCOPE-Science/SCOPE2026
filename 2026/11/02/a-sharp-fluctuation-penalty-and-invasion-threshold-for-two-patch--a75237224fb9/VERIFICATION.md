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

# Mathematical verification

The defining matrices have positive reproduction multipliers, symmetric dispersal fractions between zero and one half, and a two-step periodic schedule. The analytic proof derives the exact characteristic polynomial and a sign-changing threshold using no asymptotic or finite-grid approximation.

To check calculations, extract `check.py` into the same directory and run `python3 check.py`. It uses only Python's standard library, performs exact Fraction arithmetic for matrix products, polynomial evaluations, and the rational source–sink witness, and checks illustrative numerical eigenvalue monotonicity on a bounded grid.

The executable tests cannot establish the infinitely quantified theorem; the symbolic identities and sign inequalities in `RESULT.md` are the proof. No independent audit or external validation is asserted. The full text of Watson et al. (2012) was inaccessible, so the comparison to that paper remains limited to material explicitly described in the accompanying literature discussion.
