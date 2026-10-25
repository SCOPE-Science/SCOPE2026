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

`python3 artifacts/verify.py 11` runs without third-party dependencies and checks exactly all cliques, all 20n free-face collapse pairs, all slab forbidden-pair ten-cycles and intersections for each integer n from 7 to 11. The output is included as `artifacts/verification-output.txt`. The verifier does not enumerate infinitely many lengths; the all-n result uses the local classification and gluing proof in RESULT.md.

Independent scientific audit has not been performed.
