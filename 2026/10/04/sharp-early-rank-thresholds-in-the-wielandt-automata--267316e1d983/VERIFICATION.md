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

The theorem is proved symbolically in `RESULT.md`. The executable replay is deliberately finite corroboration.

`verify.py` constructs the two transition maps directly, runs breadth-first search in the power automaton from the full state set for every integer state size from 3 through 14, and checks all of the following:

- exact minimum distances to every target deficiency in the claimed range;
- uniqueness of the minimum-length target word in that range;
- equality of the unique word with the alternating witness specified in the theorem;
- the strict inequality at the first deficiency beyond the claimed linear range whenever such a deficiency exists.

The replay does not establish the infinite theorem by enumeration. Its purpose is to detect transition-convention, parity, or boundary mistakes in the proof and package.
