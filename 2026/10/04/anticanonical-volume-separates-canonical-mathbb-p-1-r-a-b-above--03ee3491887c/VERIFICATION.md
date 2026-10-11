---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The Reid--Tai calculation gives the exact canonical triangle \(0\le d=b-a\le r\), \(1\le a\le r+d\), hence \(ab\le6r^2\). Equal volumes with reduced weight-sum ratio \(S_1/S_2=u/v\) imply \(u^{r+1}\mid P_1\) and \(v^{r+1}\mid P_2\); unequal sums therefore force \(2^{r+1}\le6r^2\), impossible for \(r\ge8\). Equal sums then force equal products and hence the same ordered pair. I independently enumerated the exact canonical domain for \(2\le r\le7\): precisely the two stated \(r=2\) collision classes occur and none occur for \(3\le r\le7\).

## originality

PASS

The exact canonical triangle and the sharp anticanonical-volume maxima are already published SCOPE findings and were treated as prior art. Neither those records nor the inspected Kasprzyk primary criterion gives an all-dimensional equal-volume classification. The submitted divisibility argument is a separate implication: after reducing the ratio of weight sums to coprime integers, unequal sums force a power at least \(2^{r+1}\) to divide a product at most \(6r^2\), excluding collisions for \(r\ge8\); only \(3\le r\le7\) then require finite exhaustion.

## value

PASS

Anticanonical volume is a central Fano invariant. An exact rigidity theorem saying that it recovers both heavy weights on an entire natural canonical family, together with the complete low-dimensional exception set, is a motivated structural classification rather than a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
