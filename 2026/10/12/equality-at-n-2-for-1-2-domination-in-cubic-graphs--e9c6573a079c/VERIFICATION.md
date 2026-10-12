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

The universal claim is proved analytically in `RESULT.md`. No finite computation is used to infer an infinite statement.

`verify.py` independently checks the definitions on every labeled simple cubic graph on four and six vertices. For each graph it brute-forces all vertex subsets to compute the minimum \((1,2)\)-domination number, brute-forces all nontrivial bipartitions to test for a perfect matching cut, and verifies that every half-order minimum set itself induces such a cut.

The finite enumeration is only a stress test of the definitions and equality mechanism. It does not check larger orders and is not a substitute for the proof.
