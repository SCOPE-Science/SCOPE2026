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

The analytical proof is in `RESULT.md`. A standalone Python script `ballot_first_arrival_check.py` is bundled with this result; run `python ballot_first_arrival_check.py` using Python's standard library only.

The script makes three exhaustive four-orientation checks of the interval endpoint pairings and 324 exact rational comparisons between a direct enumeration of all 24 independent exponential race orders and a separately evaluated candidate rational formula. It also evaluates 25 rational points of the sharp attainable-family parameter and the equal-rate calibration. Recorded outcome: **PASS: 352 exact rational checks (including 324 exponential races).** The independent finite arithmetic route checks polynomial normalization, sign conventions and the event coding; it cannot prove the infinite collection of arbitrary continuous distributions. The proof handles that generality using interval conditioning and an \(L^2\) projection bound.

No independent audit or external certification has been performed. This result does not rely on other local files, network downloads or proprietary computational software.
