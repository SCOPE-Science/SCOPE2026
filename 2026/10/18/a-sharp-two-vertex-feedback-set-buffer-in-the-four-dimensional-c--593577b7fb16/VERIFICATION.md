---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For Q4 (16 vertices, 32 edges) a retained forest inequality 32-4|S|+e(S)<=15-|S| rules out |S|<6. Parity-neighbor overlap shows a six-set cannot be mixed, and the only valid pure parity sets omit one antipodal pair, giving eight minima. An independently written 2^16-mask forest test (union-find on Hamming-one edges) enumerated exactly 8,1008,4090 valid sets at sizes 6,7,8, found 80+9072 toggle edges and the 8-star+928-isolate capacity-seven decomposition; capacity eight has one component of all 5106 states. BFS over all 8 minima gave precisely 12 same-parity pairs at distance 4 and 16 opposite-parity pairs at 12. This exhausts every relevant 16-vertex set and never extrapolates to higher-dimensional cubes.

## originality

PASS

Focardi–Luccio–Peleg address feedback-vertex-number bounds in hypercubes and an earlier 1999 report; Bousquet et al study reconfiguration on planar graph classes (subcubic tractability, degree-four PSPACE hardness). The cube Q4 is 4-regular and nonplanar, and the prior theorems do not supply this exact TAR capacity graph or min-set distance spectrum. Focardi full publisher text is not independently read; possible small-cube census overlap is retained.

## value

PASS

Minimum feedback-set reconfiguration with limited temporary buffer is a natural exact graph-algorithm invariant, not simply re-evaluating the optimal set size. The precise two-extra-vertex connectivity threshold and optimal-pair shortest path dichotomy characterize a canonical hypercube small enough for complete verification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
