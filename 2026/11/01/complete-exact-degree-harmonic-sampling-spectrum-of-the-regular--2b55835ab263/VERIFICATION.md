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

# Reproducibility and scope of checks

Execute `python3 verify_spectrum.py`. It constructs the twelve antipodal directions from signed two-sparse integer vectors, verifies the matrix identities for orthogonality and signed incidence, checks the Chebyshev reduction and predicted spectral levels through degree \(47\), and confirms the affine twelve-step recurrence at all tested degrees. This exact finite replay passed.

The proof does not infer its all-degree conclusions from testing. For odd degrees at least five and even degrees at least twelve, the explicit eigenvalue formulas have strictly positive uniform lower bounds as displayed in RESULT.md. The general addition theorem and symmetry decomposition establish the matrix identities for every degree.

No independent audit or external mathematical certification has been performed.
