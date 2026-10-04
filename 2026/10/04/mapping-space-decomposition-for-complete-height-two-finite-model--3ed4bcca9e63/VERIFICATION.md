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

The symbolic proof classifies every monotone map between the two complete height-two posets before any computation is used. The only isolated maps are the level-preserving maps whose two level restrictions are both nonconstant. All remaining maps are connected to constants. On that component the explicit map \(\rho\) to the target is order preserving, fixes constants, and yields a relative simplicial contiguity between the identity and inclusion after retraction.

`verify.py` exhaustively enumerates five small source-target choices. It checks the closed total-map and isolated-map formulas, computes all comparability components, verifies that there is exactly one non-singleton component, checks that \(\rho\) is defined and order preserving there, and for every comparable pair verifies the pairwise comparability needed for the contiguity union. The stored `verification_output.txt` ends with `VERIFY_OK`.

The finite enumeration is not an exhaustive proof for all parameters. No claim is made that the finite map poset itself beat-point retracts to the target; the proved deformation retraction is on order-complex realizations.
