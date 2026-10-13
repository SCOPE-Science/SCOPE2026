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

The standalone script `verify_spider_color_refinement.py` constructs \(S_d(a,c)\), performs ordinary vertex color refinement from the uniform coloring, and checks the claimed closed form.

It verified the stabilization depth for
\[
3\le d\le8,\qquad 1\le a\le20,\qquad a\le c\le50,
\]
which is \(4860\) parameter triples.

It separately compared every computed intermediate partition with the claimed descriptor partition for
\[
3\le d\le7,\qquad 1\le a\le10,\qquad a\le c\le25,
\]
giving \(10650\) round-level comparisons.

Observed output:

`VERIFY_OK depth_cases=4860 profile_checks=10650 d_depth=3..8 a_depth=1..20 c_depth=a..50 d_profile=3..7 a_profile=1..10 c_profile=a..25`

These are finite checks. The theorem for all \(d\ge3\) and \(1\le a\le c\) is established by the proof in `RESULT.md`.
