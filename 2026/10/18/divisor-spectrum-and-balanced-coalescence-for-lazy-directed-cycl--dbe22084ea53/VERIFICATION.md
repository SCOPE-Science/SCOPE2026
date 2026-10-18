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

# Verification and scope

The infinite-family claim is supported by the four-step analytical proof in `RESULT.md`: stopped-separation martingale, recurrence/period exclusion, quotient synchronization, and full-support construction for every divisor. The proof is valid for every integer \(n\ge2\) and every \(0<p<1\).

`checker.py` uses exhaustive exact integer composition of the two complementary mask maps for every binary word on cycles of sizes \(2\) through \(8\). It compares the minimum rank over their full finite transformation semigroups with the common-period subgroup order. It also checks periodic full-support examples on small cycles. It returned `PASS: 519 exact finite checks, n <= 8` when run from the assembled candidate directory. Neither finite runs nor missing counterexamples prove the general assertion.

Relevant original literature checked: Grimmett and Holmes' complete accessible 2026 research article; searches for the 2019 arXiv/2021 chapter identified a PDF source but the complete content was inaccessible; the abstract and the newer article's precise attribution were used, without inferring whole-document noncoverage from the abstract. Residual risks include earlier semigroup theory identifying the same special-case period criterion and stronger published results in different vocabulary.

No external independent audit has been performed.
