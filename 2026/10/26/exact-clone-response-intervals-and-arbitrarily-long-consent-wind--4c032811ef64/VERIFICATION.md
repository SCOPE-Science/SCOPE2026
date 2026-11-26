---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Adjacent copies increase the candidate count by t and the unanimous-better count for a coalition S by t times the indicator that d originally belonged to that set. The disapprovers of c and its support s do not change. The weak nonblocking inequality is s(m-b_S)-|S|m + t[s(1-chi_S)-|S|] >= 0. Strict majority makes the coefficient positive when chi_S=0 and negative when chi_S=1, giving the stated integer endpoints, including equality, no-disapprover, and empty-interval cases. In the five-voter construction, the approval sets are top segments and the only possible coalitions are the two dissenters individually and together. Their unanimous-better counts are h+2+t, 2h+2, and 3; nonblocking reduces to t<=3h-2, t>=1, and t>=7-3h. The last constraint is redundant for h>=2. Thus the two switches and the interval length follow for all h, not by extrapolating the reported tests.

## originality

PASS

The affine interval is a direct specialization of the published AWVC definition, and qualitative clone sensitivity of the ordinary veto core is known. The supported distinction is the exact two-switch, arbitrarily long finite acceptance window for an unchanged majority-approved alternative with a fixed five-voter electorate, together with the endpoint characterization in which it sits. The inspected sources neither state that construction nor prove a stronger statement that yields it.

## value

PASS

This is a precise robustness obstruction for a defined consent correspondence, not just a generic failure of clone independence. With approvals of the target, every old comparison, and the five-person electorate fixed, cloning restores consent and then destroys it, with an arbitrarily long intervening interval. The sharp endpoints and the three-coalition construction explain how two competing forms of blocking produce the switches. The initial number of alternatives grows with h; the claim is not about typical elections or downstream winner selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
