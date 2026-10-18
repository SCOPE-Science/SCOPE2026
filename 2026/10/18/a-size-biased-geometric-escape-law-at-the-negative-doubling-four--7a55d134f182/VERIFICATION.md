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

Run `python verify_escape.py` with Python 3 (standard library only). The executable starts from the actual piecewise-affine inverse branches and performs rational interval intersections and merges, independently of the four-cell symbolic count. It checks the survivor formula through time 23 (24 stages), the transfer-matrix count at the same 24 stages, the small-hole law at three rational parameters across 16 stages (48 identities), 23 first-hole probability differences and the exact four-cycle orbit.

The original saved standalone checker returned:

```
PASS: 24 exact direct-preimage survival counts, 24 Markov counts, 48 small-hole checks, 23 hitting-law checks, period-four boundary orbit.
```

**What is proved without computation.** All time indices \(n\ge0\) are established by the exact inverse-cylinder proof and elementary matrix induction. The conditional switching-time distribution follows from a complete combinatorial classification of all paths, and the moments follow from convergent geometric sums.

**What remains unverified externally.** The mathematical work received self-review only. No independent audit, outside-priority certificate, or general result for other holes has been performed.
