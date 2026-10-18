---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Source RESULT.md explicitly gives bias-corrected silent-history moment factors c1=(1-beta1)/(1-beta1^tau) and c2=sqrt((1-beta2)/(1-beta2^tau)). Hence mini coordinate update denominator is c2||g||_2/sqrt(d)+epsilon versus c2|g_j|+epsilon for Adam. Cancelling the identical numerator yields the claimed ratio. |g_j|<=||g|| proves <=sqrt(d), achieved in the infinite-impulse-amplitude limit for one nonzero coordinate with fixed epsilon>0. Equal k-support gives sqrt(d/k). Maximizing over blocks produces sqrt(max d_b) and pigeonhole gives the optimal sqrt(ceil(N/B)); balanced partitions attain it. Independent new checks covered d<=14, all k, and small integer partitions. No claim of actual training-loss amplification is proven.

## originality

PASS

The defining Adam-mini rule and observed sparse embedding-row instability predate this claim. The audited statement is a precise universally sharp coordinate-response comparison and optimal fixed-state-count partition frontier. Accessible source material and Resultary results do not contain that exact theorem. Comparisons do not confuse this criterion with Hessian optimality or empirical loss-spike claims.

## value

PASS

The scalar-memory compression in Adam-mini creates a mathematically meaningful, optimizer-specific sparse-coordinate response vulnerability. The sharp sqrt(d/k) support law and sqrt(ceil(N/B)) memory-count frontier quantify the exact unavoidable cost, which a researcher can use when choosing or testing partitions under sparse updates. This is not asserted as a universal training-loss or convergence guarantee; its elementary pigeonhole step is only part of the calculation, not the significance by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
