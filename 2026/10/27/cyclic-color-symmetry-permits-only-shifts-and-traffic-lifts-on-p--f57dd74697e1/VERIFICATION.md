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

# Reproducibility and checks

Run `python3 verify.py` from the same directory. It uses only Python's standard library and exhaustively checks all \(81\) equivariant local rules in two independent representations: the output-edge formula and direct preservation on all proper four-color inputs. It verifies the exact 15 functions, three color translates of each representative, the five induced binary rules, the forbidden output witnesses `1100` and `0011`, and the three full-permutation-equivariant shifts.

The local-rule classification is finite and exhaustive; no extrapolation beyond the 81 possibilities is involved. The induced non-surjectivity results follow from reachability of two-bit predecessor states on arbitrary binary edge strings and the fact that every binary edge string lifts to a proper three-coloring. Finite cyclic rings of sizes 3 through 7 provide supplementary checks only.

The historical-priority comparison is not mathematically certified. Independent mathematical audit has not been performed.
