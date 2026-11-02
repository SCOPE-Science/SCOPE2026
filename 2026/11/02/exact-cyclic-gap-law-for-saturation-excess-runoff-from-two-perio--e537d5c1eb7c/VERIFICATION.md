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

# Reproduction and limits

Run `python3 verify_bucket.py` with standard Python 3. The script constructs exact rational values of the attracting two-pulse periodic state and verifies the original two-state clipped fixed-point equations, the three-phase runoff law, the max-of-three formula, and its monotonic ordering.

Actual run: `PASS: 42600 exact periodic-state and runoff cases; ordering, boundaries and example verified`.

Parameters tested were the six retentions \(\{1/5,1/3,1/2,2/3,3/4,9/10\}\), every period length \(3\leq N\leq17\), all admissible smaller integer gaps, and rainfall ratios \(p=j/40\) for \(1\leq j\leq100\). Further exact tests cover the equal-gap coincidence and the example \(N=6\), \(r=1/2\), \(p=3/4\).

The code is a non-exhaustive finite cross-check; arbitrary real parameters and all periods are covered by the proof in `RESULT.md`, not by enumeration. No external audit or independent validation has been performed. Historical priority remains provisional due to incomplete access to some relevant older primary texts and potential general finite-buffer results.
