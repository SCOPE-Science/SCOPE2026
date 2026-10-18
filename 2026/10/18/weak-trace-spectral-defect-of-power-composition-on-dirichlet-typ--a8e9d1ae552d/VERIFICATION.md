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

# Reproducibility and limits

Run `python3 check.py` from the directory of this document. Python 3's standard library is the only requirement. The script has 4,882 passing assertions in the recorded run and checks exact coefficient/adjoint-diagonal identities, exact finite shell traces, nonintegral-parameter asymptotic samples, and finite sorted singular-value sequences. No external dependency, random seed, cloud service, or unpublished data is required.

The infinite-dimensional assertions are verified analytically in `RESULT.md`: the monomial action is exact, the first-order weight expansion has an explicit second-order remainder, the count of residue classes is elementary, and the finite trace identity telescopes. The numerical checks do not establish universal limits or exclude equivalent prior publications. The unweighted Bergman reference was not available in full text, while its declared point-spectrum scope was treated as known coverage. No independent audit or validation has been performed.
