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

The independent `verify.py` script uses only the Python standard library and runs without data files. It exhaustively enumerates each orientation of every labeled isolate-free simple graph on 2, 3, and 4 vertices, and verifies all corresponding one-edge-subdivision covariance changes. It also tests named families and regular cases; the one-subdivision of the complete graph on five vertices is exhaustively enumerated over \(2^{20}=1,048,576\) independent edge orientations. The stored verifier passed 574 assertion groups.

All computations are with exact integer counts and `fractions.Fraction` rational arithmetic. They support but do not substitute for the unrestricted indicator proof, the exact algebraic sign analysis, and the regular-graph simplification. The enumeration does not verify arbitrary graph sizes, non-fair orientation laws or historical novelty. Independent external audit has not been performed.
