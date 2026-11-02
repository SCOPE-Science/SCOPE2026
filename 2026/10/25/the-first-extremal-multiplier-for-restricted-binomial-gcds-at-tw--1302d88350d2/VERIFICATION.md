---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For 2≤q≤(p−1)/2, mq=(2q−1)p+(p−q)<p², each md has larger units digit, so one borrow. At q0=(p+1)/2, mq0=p²+(p−1)/2 forces two borrows for every d<q0; no third possible. For q=q0+j, 1≤j≤(p−1)/2, units borrow for every d, while d=q0 yields exactly one carry in the complementary addition (next digit 2j≤p−1). At q=p+1, d=q0 has no borrow by Lucas. All cases include p=3 boundaries. Independent valuation via Legendre factorial sums was compared against the exact formula for all 2274 odd-prime/multiplier cells with p≤149; universal claim rests on Kummer case proof. General Fairfax-Ball ceiling r_p(2p−1)=2 supplies maximality globally.

## originality

PASS

No located exact or dominating covering result after primary-paper and Resultary comparisons; all four named comparison checks and residual priority risks are separately documented.

## value

PASS

The least attaining multiplier is an explicit natural invariant defined in the motivating global restricted-GCD paper. This infinite p-dependent family exhibits a nonmonotone rise/peak/drop, and the exact initial spectrum is not implied by the generic ceiling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
