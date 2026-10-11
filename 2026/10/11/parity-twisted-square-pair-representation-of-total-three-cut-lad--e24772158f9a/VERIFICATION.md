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

With Python 3 installed, run `python3 artifacts/verify.py` from this package's root. The script uses only the Python standard library.

The verifier builds graph adjacencies from the two-row ladder definition; checks the signed invariant-complement formula for all four involutions at every \(3\le n\le40\); constructs the full oriented simplicial chain trace independently at every \(3\le n\le7\); and computes complete reduced mod-two simplicial boundary ranks for \(3\le n\le6\). A successful execution ends in `VERIFY_OK`.

These are finite consistency checks, not a proof of the all-parameter result. The all-parameter reasoning and the exact use of the previously published homotopy concentration are in `RESULT.md`. An independent audit has not been performed.
