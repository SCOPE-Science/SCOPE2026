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

# Reproducibility

Run `python3 verify_profiles.py` with Python 3 and its standard library. The expected terminal marker is `VERIFY_OK 65534`.

The verifier directly enumerates every binary word of lengths 1 through 15, counts left-minimal mixed windows by examining each candidate interval, computes run-based counts separately, and groups words by full profile. Its assertions compare the number of profiles with cumulative partition numbers; compare entire multisets of fiber sizes with the factorial formula; check the exact maximum number of nonzero differences; and check total word counts.

This finite testing does not prove statements about lengths above 15. The all-length proof is the run-decomposition/partition-bijection argument in `RESULT.md`. No external independent audit or formal verification was performed.
