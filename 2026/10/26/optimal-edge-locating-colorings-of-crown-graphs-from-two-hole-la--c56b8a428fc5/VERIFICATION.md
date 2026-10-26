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

# Reproducibility and verification scope

Run `python3 verify.py` with Python 3 and its standard library. It executes two logically different finite checks: an arithmetic missing-pair test across every \(n\) from 6 to 5000, and a direct graph-shortest-path test of the original edge-locating definition, including properness and color-class nonemptiness, for \(n=6,\ldots,13\). The current execution produced:

`PASS: 4,995 parameter instances and 8 independent graph-distance checks`

The proof for all \(n\ge6\), including untested orders, is in `RESULT.md`. The key inference is the congruence-based enumeration of collisions between unordered missing-color pairs, not empirical extrapolation. The accepted domain excludes \(n=4,5\). No independent audit has been performed.
