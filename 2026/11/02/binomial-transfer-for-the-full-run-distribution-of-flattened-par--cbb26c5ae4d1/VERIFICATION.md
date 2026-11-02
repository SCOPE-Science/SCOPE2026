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

The recurrence is proved for every positive length by an exact bijection between completed transfer states and flattened parking-function words. The transition coefficients are extracted exactly from ordinary stars-and-bars generating series; the parking-prefix test is necessary and sufficient for the sorted preference condition.

Run `python3 verify.py` with Python 3.10 or later. The script checks the direct defining predicate on every word of length one through six, compares the binomial recurrence with a separate literal run-allocation dynamic program through length twelve, and verifies each published run-count row through length eight. It additionally replays the reported rows at lengths nine through twelve, fifteen and twenty. The successful ending marker is `VERIFY_OK`.

These computations do not independently establish the theorem for unbounded length. No independent human or external audit has been performed; no computational output should be construed as independent proof.
