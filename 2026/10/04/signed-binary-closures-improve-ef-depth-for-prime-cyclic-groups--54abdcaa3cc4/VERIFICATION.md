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

The proof was checked at three levels.

1. **Symbolic closure check.** The doubling relations force the selected images to be the expected powers of two times the first image. The auxiliary relations force the selected partial sums. In either closure choice, the final atomic relation is exactly equivalent to \(py=0\).
2. **Binary-weight check.** For \(a=2^tc\) with \(c\) odd, the identity \(s_2(a)+s_2(2^n-a)=n-t+1\) was rederived directly from bitwise complementation of \(c-1\). This yields the stated \(\lceil n/2\rceil\) bound.
3. **Finite replay.** `verify.py` checks every odd prime below 20000 and the exact examples \(7,17,31,127\). It verifies tuple length, nonzero/distinct representatives, the appropriate closing congruence, and the popcount inequality.

The finite replay is corroborative only. It does not replace the all-prime argument, and no independent audit has been performed.
