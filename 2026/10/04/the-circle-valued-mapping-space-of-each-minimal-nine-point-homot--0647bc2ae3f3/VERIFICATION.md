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

`verify.py` and `beat_sequence.json` are complete standalone verification artifacts for the finite calculation in RESULT.md.

The verifier performs the following checks from explicit source data:

1. reconstructs the nine-point source order from its twelve covers and computes transitive closure;
2. reconstructs the four-point circle target order;
3. enumerates every one of the \(4^9\) functions and retains exactly the order-preserving maps;
4. independently enumerates the same maps by recursive order pruning and requires list equality;
5. replays all \(168\) beat deletions against the current active mapping poset, not against a stale global order;
6. checks that the final four maps are exactly the constants and that their inherited order is the target circle;
7. independently enumerates maps from the opposite source and checks the order-reversing target involution correspondence.

A successful replay prints:

`VERIFY_OK maps=172 deletions=168 up=68 down=100 core=4 constants dual_maps=172`

The finite enumeration proves only the stated finite mapping-space theorem. It is not evidence for a broader theorem about arbitrary weakly contractible finite spaces or arbitrary targets. General topological steps used after the finite calculation are the standard beat-point strong-deformation-retract theorem and the standard finite mapping-space homotopy criterion cited in RESULT.md.
