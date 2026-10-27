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

# Verification notes

The analytic score-gap inequality is valid for every nonnegative integer electorate size in the model, and the score lattice proves the at-most-three-candidate result for all electorates. Independently, the included `verify_opt_fvr.py` checks the complete four-candidate configuration space for \(n=1,2,3\) voters: \(256\), \(4096\), and \(65536\) ordered tuples, respectively. It employs exact rational arithmetic, confirms the strict-winner predicate at both endpoints, and finds zero profitable deviations. The script also evaluates both exact four-voter witness score vectors and asserts strict unique winners. Run `python3 verify_opt_fvr.py`; the output must equal `verify_output.txt` byte-for-byte.

The finite computations are proof only for four candidates with at most three voters, not for larger electorates. A tie-sensitive version of the result would be false as stated and is not asserted. No independent audit or external validation is claimed.
