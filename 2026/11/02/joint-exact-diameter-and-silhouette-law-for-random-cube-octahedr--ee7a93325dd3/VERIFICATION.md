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

# Reproduction and boundaries

Run `python3 verify.py` in the directory with `RESULT.md` and the checker. It uses only the standard Python library, with a fixed pseudorandom seed. On the checked package, the output was:

```text
EXACT_SECTOR_NORMALIZATION_AND_SHADOW_PROBABILITY_PASSED
INDEPENDENT_ALL_VERTEX_PAIRS_AND_OCTAHEDRON_HULLS_PASSED 1600
INDEPENDENT_HAAR_SIGNED_SLACK_CDF_CHECKS_PASSED 7
SHARP_LOWER_AND_SIX_VERTEX_ONSET_EXPANSIONS_PASSED
ALL_CHECKS_PASSED
```

The checker enumerates the 26 nonzero possible difference directions between cube vertices for 1600 independent unit normals. It independently builds a Euclidean two-plane frame, computes the planar convex hull of the projected six octahedron vertices, and checks the predicted count. It integrates each analytic density branch and checks the known exact six-vertex probability, then compares seven CDF values with 160000 seeded independent Gaussian directions normalized onto the sphere. Three shrinking-threshold integrations test the lower and six-vertex onset constants. These are finite and numerical checks, not a replacement for the analytic proof of the full distribution or its exact endpoint asymptotics. No independent audit or certification is represented.
