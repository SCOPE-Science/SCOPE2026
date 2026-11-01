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

Run `python3 verify_weak_path_attractor.py` from the directory containing the extracted accompanying script. The program uses only the standard library, enumerates every map from its binary adjacent increment and allowable initial value, computes every \(f^n\) by direct iteration, compares the eventual clamp and all fixed-interval/original-rank bins to the analytic formula, and independently checks the rank histograms and known total for each integer \(1\le n\le13\). It prints `VERIFY_OK` on success. In the largest instance, it checks 28,672 actual transformations.

The computation is finite and cannot independently prove arbitrary path length, binomial central limit behavior or independence. Those claims rely on the explicit general increment parametrization and the tightness/conditional CLT argument supplied in RESULT.md. The source definitions and earlier *initial-image* counts are externally documented; the *eventual-image* fiber theorem is what is assessed. Literature coverage is not exhaustive; in particular, the full text of the related partial-transformations fixed-point article could not be reviewed.
