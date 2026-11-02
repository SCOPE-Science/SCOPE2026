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
# Verification and limits

Execute `python3 verify_switch.py` with a standard Python 3 interpreter. This is a standalone, dependency-free finite checker distributed alongside the proof.

The checker enumerates every binary schedule of lengths 1 through 11 and independently every candidate binary itinerary of length one greater. It compares direct survival with exact 2-by-2 transfer counts; evaluates the finite upper bound by clearing rational denominators with integer arithmetic; checks the lower bound with exact integer powers; verifies exact alternating counts; checks four matrix products; and tests three longer sparse-defect schedules of lengths 100, 250 and 500. The local execution passed.

The proof of the universal assertions in RESULT.md consists of explicit matrix identities, monotone nonnegative products, the arithmetic-geometric mean inequality and a limiting estimate. Checking finitely many schedules does not establish the assertions for all schedules or all times. No independent validation or external certification has occurred.
