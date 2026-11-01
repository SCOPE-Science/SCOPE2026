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

The standalone `verify_wheel.py` is Python 3 standard-library code with no third-party dependencies. It uses exact rational arithmetic, computes weighted vertex-to-vertex shortest paths, represents continuous point-to-point shortest distances as lower envelopes of endpoint-route affine functions, and exhausts the critical intersections and boundary candidates in each pair of edge-coordinate domains. Every test configuration is therefore a finite exact check of an independently constructed continuous metric network, not a sample of positions.

The execution passed 80 parameter configurations with rim orders from \(3\) through \(11\), including transition-length inputs, and checked the proposed sharp normalized ratios and attaining spoke lengths. The script can be rerun using `python3 verify_wheel.py` from its own directory.

The proof of the infinite theorem is the geometric argument in `RESULT.md`: reduction to three edge-type pairs, exact witnesses for both rim cases, then direct monotonicity of normalized branches. Finite checks do not certify untested infinitely many orders or irrational spoke lengths. Historical originality is subject to incomplete access to Chen and Garfinkel (1982).
