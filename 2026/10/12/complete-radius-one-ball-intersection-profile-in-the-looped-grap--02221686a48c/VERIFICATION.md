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
# Reproducibility and limits

Run `python3 verify.py` from the same directory as these documents; it requires only Python 3 standard-library modules. The program independently enumerates finite-field additive graph words, star-space unions, shifted-ball membership and all predicted cases. Expected final output: `VERIFY_OK 36504`.

It exhausts all supported-edge patterns for five small graph/field configurations, including all length-five binary patterns, and checks deterministic larger examples. For \(q=4\), coordinatewise addition is XOR on the two-bit representation of the field's additive group; field multiplication is not used. Every possible nonzero label assignment is isometric to the unit-valued representative by independent coordinate scaling. The uniform conclusion for all prime powers and graph orders follows from the proof in RESULT.md, not from finite enumeration.

No independent scientific audit has been performed. Source comparison remains subject to unindexed-work risk.
