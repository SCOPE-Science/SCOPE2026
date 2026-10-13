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

Run `python3 checker.py` with Python 3; no third-party packages are required. The executable independently visits every function \([n]\to[n]\) for each \(n\in\{1,2,3,4,5,6,7\}\), filters by adjacent Lipschitz inequalities and composition idempotency, and compares image-rank totals with a separate adjacency-walk recurrence. All ranks matched during preparation. The expected response is `VERIFY_OK`.

The direct count at \(n=7\) is \((7,192,131,46,14,4,1)\) across ranks \(1\) to \(7\), totaling \(395\); the separate five-interval rank-three census is \((29,24,25,24,29)\). The values \(a_6=12\) and \(a_7=29\) in published Conjecture 14 give \(130\), proving a finite disagreement. The attached code verifies these identities but is not a proof of the all-\(n\) formula; the proof is the universal interval-and-two-walk bijection in `RESULT.md`.

No independent audit or external certification has been performed.
