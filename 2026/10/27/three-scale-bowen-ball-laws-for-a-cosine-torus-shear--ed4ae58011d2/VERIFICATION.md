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
# Verification and limits

The analytic proof in `RESULT.md` verifies the only universal implications: exact lifting of the affine fiber difference without changes of integer winding; localization at two simple velocity-level roots for noncritical centers; dominated quadratic scaling at the extrema; Haar reduction to an arcsine-law integral; and a uniform large-argument expansion with integrable remainder. The finite tests in `verify_bowen.py` reproduce the actual output in `verify_bowen_output.txt` when run with standard Python 3 and are not certificates of infinite-time claims.

The limits require a fixed amplitude \(0<a<1/8\), fixed radius \(0<arepsilon<1/8\), the maximum circular-distance metric, and normalized Haar area. The regular-center limit excludes the two critical centers and the root-on-boundary equality locus. Critical-center and averaged limits have separately justified normalization. A complete independent scientific audit has not been performed.
