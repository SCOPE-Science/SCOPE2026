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

Run `python3 verify_85.py` with Python 3 and no third-party packages. The program reconstructs the carry graphs for both multipliers, checks reachable state sets, transitions, finite vector-polynomial identities, first coefficients, and independently enumerates digit restrictions through depth 11. The decisive finite-state check is applied to every state, not only the initial carry. Applying matrix powers propagates it to all lengths.

Expected final success line: `VERIFY_OK M13_states=3 M85_states=18 M85_edges=24`.

No finite brute-force test alone establishes the infinite result. The proof also uses rational-series factorization and the established theorem identifying path-set dimension with logarithmic graph growth. No independent audit or external certification has been performed.
