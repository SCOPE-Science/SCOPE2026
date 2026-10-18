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

The accompanying standard-library-only `verify.py` computes the continuous linear finite-element mass matrix on a metric star from the elementary integrals of nodal hats, obtains its matrix inverse through exact rational Gauss–Jordan elimination, and integrates absolute reproducing-kernel rows using the exact affine zero-crossing formula. It does not substitute the symbolic inverse formula during the independent inversion.

Run `python3 verify.py` in the directory containing the script. A successful execution prints `PASS 1982 exact rational star systems; matrix inverse, integrated absolute kernel and sharp norm`.

The deterministic test set includes 180 random positive rational length vectors for every arm count from two to twelve (1,980 samples) and two targeted symmetric/threshold cases. For each sample, it verifies the full inverse matrix, all nodal absolute-integral norms, the shortest-arm maximizing norm, and strict dominance over the center. The random seed is fixed in the script, so the output is reproducible.

The mathematical proof is independent of randomized testing. It proves, for arbitrary positive real lengths and every integer arm count at least three, the inverse block formula, operator norm, extremal locations, sharp range and nonattainment. No verification program here can establish novelty or independence of external review. The numerical/sample tests do not claim exhaustive coverage of continuous parameters.
