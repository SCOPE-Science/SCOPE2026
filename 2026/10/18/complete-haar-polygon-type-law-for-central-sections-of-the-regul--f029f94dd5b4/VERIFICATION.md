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
# Reproducibility and verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. The script checks the following on the actual embedded source: it generates all \(24\) vertices from signed coordinate permutations; obtains the \(36\) edges using exact squared distances; verifies their common dot product; compares the analytic section-side formula with exact sign-crossing counts for \(9,983\) generic integer directions; triangulates the fundamental normal sector into \(6\) spherical triangles and confirms both its total area and the three probabilities; and samples \(200,000\) Gaussian normals with a fixed random seed to check independently counted edge crossings. It ends with `VERIFY_OK vertices=24 edges=36 rational_tests=9983 spherical_chambers=6 monte_carlo=200000`.

The proof of the continuum theorem uses the face-incidence classification, the exact spherical solid-angle identity and the analytic edge-crossing expectation. No simulation is promoted to an infinite proof; probability values computed by floating-point functions are only consistency checks against symbolic formulas. This is a self-reviewed result. An independent mathematical audit has not been performed.
