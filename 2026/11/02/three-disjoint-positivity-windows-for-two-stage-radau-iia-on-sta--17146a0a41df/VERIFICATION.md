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

# Reproducibility checks

The embedded `verify.py` requires Python 3 and SymPy and replays exactly from the embedded content. It symbolically verifies the closed matrix-entry identities, mass conservation, the derivative and global minimum of the Radau response, polynomial specializations, and coefficients underpinning both asymptotic expansions. It then checks selected rational full matrix inversions for the star Laplacian, negative hub and leaf witnesses at eleven leaves, and several exact positive-root counts.

The observed replay was `PASS 3951 exact symbolic/rational/root assertions`. These tests establish algebraic consistency on checked expressions and instances. The general root and sign classification relies on the exact analytic proof in `RESULT.md` (not on any finite experiment or timeout). No external or independent audit was carried out.
