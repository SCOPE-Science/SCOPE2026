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

# Reproducibility
Run `python3 verify.py` in a directory containing that file. The deterministic diagnostic completes with `VERIFY_OK 9862`. It checks regular even cyclic polygons with four through 120 vertices, irregular centrally symmetric cyclic examples, an exhaustive angular-pair optimizer versus a linear successor scan, and sampled convex-combination perimeter bounds. The random generator uses a fixed seed.

# Analytic limits
No finite experiment proves the universal theorem. The proof is independently written in `RESULT.md`: center reduction, separate convexity, equality rigidity, circumdisk center constraint, vertex-pair angle formula, and two-pointer scan. The critical sharpness witnesses are the vertex rectangles themselves. The originality search is not an independent priority certification, and an old equivalent could remain undiscovered.
