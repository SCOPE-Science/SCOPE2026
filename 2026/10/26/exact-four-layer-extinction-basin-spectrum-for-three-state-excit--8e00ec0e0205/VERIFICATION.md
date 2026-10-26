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

The all-parameter proof appears in `RESULT.md`. It uses Hall's criterion for rainbow transversals, direct iteration of the update rule in its two disjoint combinatorial cases, and elementary inclusion-exclusion. The theorem is not based on finite sampling.

`verify.py` is a complete standard-library-only checker, executable using `python verify.py`. It applies exactly the vertex-level three-state update, rather than assuming the classification or using the closed count formula to generate orbits. For every ordered triple of positive integers satisfying \(1\le a\le b\le c\le4\), \(a+b+c\le10\), it exhaustively evaluates all configurations and compares the directly observed first-extinction-time distribution with the formula. It also verifies the predicted depth-four sharpness and checks that all states not extinguished after four rounds are actually nonzero three-cycles. Recorded output is included in `verification_output.txt` and ends `VERIFY_OK triples=18 total_initial_states=206172`.

The computation does not establish any statement for larger graphs by itself, and no external or independent audit has taken place.
