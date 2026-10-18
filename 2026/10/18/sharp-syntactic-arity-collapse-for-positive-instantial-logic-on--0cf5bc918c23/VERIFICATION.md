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

# Reproducibility and logical limits

Run `python3 check_pinl_width.py` with Python 3 and no third-party packages. This tests the source witness and co-witness truth conditions directly, separately from the partition construction. It enumerates upsets for eight finite orders, verifies the partition identities for multiple input arities, compares both persistent sharpness frames through every lower arity, and verifies each separating valuation at the width.

Successful output ended:

```
PINL_WIDTH_VERIFY_OK comparisons=1204834 lower_checks=76857
```

The eight orders are the singleton, a four-element chain, four-element fork and diamond, two disjoint two-element chains, three- and four-element antichains, and a six-element crown. Some larger case arguments are fixed-seed samples; the script does **not** exhaust all models or all formulas. The theorem for every finite-width poset, including infinite carriers, follows from Lemmas 1–3, the structural induction, and the explicit arbitrary-poset distinguishing pair in `RESULT.md`. These mathematical arguments, rather than computation or lack of counterexamples, establish correctness.

Two external results matter for novelty comparison: the published finite Boolean-BAIO neighbourhood-reconstruction theorem has a distinct outcome and hypotheses, and the 2026 PINL manuscript defines the ordered two-sided semantics but not a uniform finite-width term translation. The older classical-INL fragment paper was available in abstract only; independent expert assessment of mathematical priority remains outstanding.
