---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The cosine samples are strictly ordered on the half-grid, so the quadratic with roots at the adjacent samples \(3n\) and \(3n+1\) is nonnegative everywhere. Two positive weights at those nodes eliminate the second-harmonic coefficient and produce an exact dual upper certificate. The signs \(\cos(2r\theta)<0<\cos(2s\theta)\) give positivity of the weights, and elementary trigonometric identities yield the closed form. The inspected verifier checks these identities for \(1\le n\le100\), but the proof is analytic for all \(n\ge2\).

## originality

PASS

Ivanov explicitly names \(q=2(p+1)n+1\) as a priority family and predicts the zero pattern; for \(p=3\) this is exactly the audited \(q=8n+1\) line. The source's solved adjacent family covers the consistency case \(q=9\), not the new \(n\ge2\) sequence. Two stronger all-grid degree-two SCOPE/Resultary results now imply this theorem, but public repository chronology places their first located publication 11 minutes 26 seconds after the assigned record's import. They are therefore later superseding coverage, not prior-art evidence against originality of this record.

## value

PASS

At the time of the assigned record's public import this solved an infinite subfamily explicitly highlighted by the primary source and supplied both extremizer and optimality certificate. Later same-day work now generalizes it to every cyclic grid, but that supersession does not erase the mathematical value of the earlier sharp family result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
