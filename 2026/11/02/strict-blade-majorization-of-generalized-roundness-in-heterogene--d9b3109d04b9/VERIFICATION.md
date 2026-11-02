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

# Verification record

The scientific argument uses a direct powered-distance quadratic identity, two sharp Cauchy--Schwarz inequalities, strict scalar monotonicity, and integer majorization via elementary pairwise transfers. The equality condition is explicit; the dimension count follows from the rank of the centered squared-distance Gram matrix.

Run `python3 verify.py` in a directory containing the provided `verify.py`; only the Python 3 standard library is required. The executable check was run successfully against the included script before packaging, with output reporting 131 nonisomorphic bouquet configurations, 655 independent Jacobi eigenvalue calculations, 131 majorization-envelope comparisons, and 131 critical null-vector evaluations. These are finite floating-point checks; the proof in RESULT.md establishes the all-parameter theorem. No independent audit, external mathematical certification, or exhaustive infinite check was performed.

The literature risk is concentrated in the unavailable full manuscript behind the 2011 conference statement on windmill generalized roundness and in a 1990 generic truncated-graph embedding paper. These sources were not misrepresented as materially read in full.
