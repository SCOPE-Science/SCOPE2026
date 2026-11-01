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

The executable `artifacts/verify.py` independently reconstructs all \(2^{15}\) labeled graph edge sets and the full domination-threshold simplicial complex. It validates the two neighborhood versions of the face predicate, downward closure, all simplicial boundary-square identities, and exact integer elimination through dimension six. Every nonzero reduction pivot is an integer unit, and boundary ranks are `14,91,364,821,711,180`.

It computes the eleven class traces by actual signed action on the integral image basis of \(\partial_5\), repeats the trace calculation with the columns processed backwards, and evaluates character multiplicities using an independent rim-hook recursion. The chain-level output is in `artifacts/verification_output.txt`; a successful independent replay is `python3 artifacts/verify.py` with marker `D63_S6_INTEGRAL_CHAIN_CHARACTER_VERIFIED`.

These tests are exact finite computations, not a proof for an infinite graph family or of contractibility of a quotient. The rational representation assertion additionally uses standard finite-group character theory; the quotient step uses the rational coinvariant/invariant correspondence after barycentric subdivision. No independent audit has been performed.
