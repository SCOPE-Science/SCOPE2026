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

The supplied `checker.py` uses independent greedy scattered-subsequence embeddings of every \(0^a1 0^b1 0^c\) target. It tests the constructive source on 1,680 pairs \((m,N)\) with \(2\le m\le21\), \(0\le N\le80\); enumerates every source word with \(2\le m\le5\), \(0\le N\le7\) across 144 zero-budget combinations; exhaustively enumerates unrestricted source lengths through \(N=7\); and checks the integer minimum formula through \(N=500\). The full script executed successfully using `python3 checker.py`.

The unbounded conclusions depend on the interval-packing lower bound and the explicit floor-gap embedding in `RESULT.md`. No finite test replaces those arguments. The external scientific assessment and independent audit have not been performed.
