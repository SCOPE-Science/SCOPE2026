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

Run `python3 verify.py` from this artifact directory, using standard Python 3 with no third-party dependencies. The script reconstructs all minimum circular-prism total dominating sets for orders 3 through 26 through exact cyclic local-constraint dynamic programming. It independently enumerates ordinary vertex subsets up to the optimum for orders 3 through 10, checks the even-cycle Cartesian factorization, and rebuilds one-token exchange neighborhoods and one-excess labels in the cases covered by the theorem. Successful execution reports `ALL_VERIFY_OK`.

Checks observed: n=6 gives 9 minima, all isolated; n=7 gives 14 minima and degree 2; n=8 gives 64 minima with two cycle factors; n=9 gives 3 isolated minima; n=10 gives 625 minima and each 8 exchange neighbors; n=13 gives 26 minima with degree 2; n=16 gives 3136 minima and each 8 exchange neighbors; n=25 gives 50 minima and degree 2. These finite checks support but do not substitute for the proof for arbitrary orders. The 5 mod 6 family is not covered by the theorem. No independent audit was conducted.
