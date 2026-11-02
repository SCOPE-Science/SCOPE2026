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

The packaged `verify.py` independently enumerates actual one-line permutations with no more than one descent rather than generating permutations from the two-block reduction in the proof. For every support on up to six labels it compares the actual set of trace patterns to the oriented-star criterion, and independently evaluates the polynomial recurrence. It also checks all four-vertex oriented simple graphs and every support on their arcs.

Recorded output is embedded as `verification_output.txt`. Re-run `python verify.py` using Python 3 and the standard library. Checks are finite corroboration; the general necessity and sufficiency rest on the unrestricted graph argument in `RESULT.md`. The literature comparison is not an exhaustive global priority guarantee. No independent scientific audit was carried out.
