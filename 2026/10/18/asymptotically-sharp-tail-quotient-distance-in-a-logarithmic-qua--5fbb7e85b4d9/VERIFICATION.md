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

The domain and quantifiers are fixed in `RESULT.md`: both scalar fields, every fixed \(\theta>0\), all finite supports \(A\) of size \(m\), and any vectors in the complete coordinate tails. The pivotal formula is verified algebraically at scale \(t=1\), with absolutely convergent sums. Bounds are \(|D|\le b\log m\) and \(|S\log(|S|/m)|\le2m\log(2/\delta)\); the stated \(\delta_m\) satisfies the strict threshold for large \(m\). No finite enumeration is used to prove the infinite limit.

Reproduce optional finite diagnostics by running `python3 check_tail.py` from the package root. The script has no third-party dependencies and checks exact positive-block/balanced-block norm identities and scale-one lower inequalities for pseudorandom finite vectors. The reviewed execution passed 2015 assertions. That diagnostic suite is not exhaustive and supplies no independent audit.

Originality was checked against the motivating 2026 arXiv full text, the complete published suppression-conditionality RESULT.md, the related 2025 arXiv article, and targeted mathematical-record searches. There is residual unindexed-priority risk; no claim is made that retrieval establishes uniqueness.
