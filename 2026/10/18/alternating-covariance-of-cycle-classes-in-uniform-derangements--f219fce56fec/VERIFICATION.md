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

# Mathematical verification

Execute the self-contained `verify.py` using Python 3; it requires only the standard library. The tested program performs direct enumeration of every uniform derangement for sizes 3 through 8 and independently evaluates the relevant two-length first and mixed cycle moments. It also performs 27,234 exact assertions covering alternating determinants, strict signs, alternating-series bounds and explicitly stated small examples, plus three finite floating-point asymptotic consistency checks (27,237 checks total).

These finite verifications do **not** establish the universal sign or asymptotic limit by themselves. Those statements are established by the marked-cycle counting argument, the all-shifts alternating-determinant inequality, and alternating-series estimates in `RESULT.md`.

The only external scientific inputs are the already established derangement counting identities and classical Ewens moment framework. The conditional factorial-moment formula is credited to the primary reference, not presented as independent discovery.
