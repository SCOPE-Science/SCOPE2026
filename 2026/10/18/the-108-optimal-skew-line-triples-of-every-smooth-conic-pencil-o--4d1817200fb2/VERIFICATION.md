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

# Reproducible checks

Run `python3 conic_pencil_f4_verify.py` using Python 3 and no extra packages. It prints `VERIFY_OK` and the exhaustive census counts. The program checks exact geometric conic smoothness via the characteristic-two polar radical rather than testing only rational points. It enumerates every projective conic, all distinct pencils, all 21 rational lines and every unordered line triple for each of the 20,160 smooth pencils. It checks that every smooth pencil admits exactly 108 witnessing triples and no pair.

The mathematical projective-frame stabilizer and two-line impossibility arguments are written in RESULT.md. No claim is made concerning all finite fields, nonrational members, or independent audit.
