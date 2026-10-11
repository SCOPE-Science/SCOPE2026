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

Run `python3 verify.py` from the extracted file directory. It requires only the Python standard library. It verifies exact normalized facet support values and squared norms for every pair of omitted matching vertices for each integer parameter from 2 through 14; it reconstructs normalized facet normals from independent rational linear systems through parameter 7; it checks contact multiplicities and exact contact-span ranks through parameter 14. Run `python3 verify.py --hull` for an additional NumPy/SciPy check: it reconstructs convex-hull facets in intrinsic coordinates for parameters 2 through 6 and compares support-plane distances. Both commands passed on the supplied source code.

The tested ranges are finite corroboration only; the complete universal proof is in `RESULT.md`. The source code produces no external certification, no independent mathematical audit, and no claims about untested parameter values except through the written proof. Neither source-search incompleteness nor unreviewed terminology equivalences are resolved by numerical computation.
