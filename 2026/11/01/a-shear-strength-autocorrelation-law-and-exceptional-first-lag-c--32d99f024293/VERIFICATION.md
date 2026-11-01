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

Exact arithmetic checks: `python3 check.py` verifies one-lag rational polygonal integrations for integer strengths \(k=1,\ldots,14\), including a zero at \(k=1\), and the two-lag \(k=1\) matrix. Twelve nonzero clipped-cell contributions fall into three four-cell groups, whose sum equals \(-121/81000\).

The all-integer theorem follows from the separately printed Fourier proof (not numerical interpolation). The exact rational checker does not certify literature priority or classify every lag. A plausible older correlation paper could not be inspected in full. No independent external audit has been performed.
