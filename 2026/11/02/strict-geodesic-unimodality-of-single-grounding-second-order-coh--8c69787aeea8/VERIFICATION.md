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

# Verification record

Running `python verify_tree.py` from this package with a Python 3 standard-library runtime completes exact-rational Green-matrix inversions and compares them with the linear-time rerooting identities. On the recorded deterministic seed the executable completed **635 weighted-tree instances**, **3,798 separately computed rational grounded-matrix inversions**, and **78 instances with exactly two adjacent optimal vertices**. Its assertions also inspect all simple paths of those instances for strict directional bracket increase, confirm the total minimizer set, verify that every downhill step heads into a component containing a global optimum, and check an explicit nonconvex objective sequence.

The tested tree sizes are 2 through 10 and include rational resistances and symmetric tie configurations. The analytic proof in `RESULT.md`, not finite enumeration, establishes the theorem for all positive real edge resistances and every finite tree. Near-tie numerical calculations with floating-point inputs may require exact or interval arithmetic. No independent audit has been carried out.
