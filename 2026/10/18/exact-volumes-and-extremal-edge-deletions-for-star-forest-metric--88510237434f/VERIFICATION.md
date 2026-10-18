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

# Verification details

The companion `verify_starforest.py` enumerates all integer anchored potentials satisfying the integer edge-difference constraints of each tested graph. There are no sampled or randomized points. For an \((N-1)\)-dimensional lattice polytope, its Ehrhart polynomial has degree \(N-1\); the last forward difference of the enumerated counts at dilations zero through \(N-1\), divided by \((N-1)!\), is the exact anchored volume. Every tested graph has diameter two and the edge-difference system is totally unimodular, yielding lattice vertices.

Eleven cases were checked exactly: \((N;m_i)=(3;1),(4;1,1),(6;4),(4;2),(5;3),(5;1,1),(6;2,2),(6;1,2),(7;2,2),(7;1,1,2),(7;3,2)\). In that order, the exact volumes are \(4,16/3,10,6,8,6,8,37/5,43/5,127/15,93/10\), matching the closed formula throughout. The checker raises an assertion failure on disagreement and prints `PASS: 11 exact independent volume checks` on complete success.

Run `python verify_starforest.py` using Python 3 with no third-party dependencies. Full rational data are deterministic; the proof of infinitely many cases remains the mathematical derivation in `RESULT.md`, not these eleven experiments.

Independent audit status: not performed.
