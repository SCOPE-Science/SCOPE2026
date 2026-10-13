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
The attached `verify.py` directly constructs infinity graphs \(F_{p,q}\), implements ordinary color refinement from the uniform coloring, evaluates the exact stabilization formula, and constructs the explicit automorphism-orbit partition.

For every
\[
3\le p,q\le50,
\]
it verifies both the depth formula and equality of the stable partition with the orbit partition.

The checker returns:

`VERIFY_OK depth_checks=2304 orbit_checks=2304 p,q=3..50`

These finite checks are corroborative only. The all-parameter result rests on the proof in `RESULT.md`.
