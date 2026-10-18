---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Every ternary order-five de Bruijn cycle contains 00000, which has symbol-pair discrepancy five and gives an unconditional lower bound. Pinned witness.txt has exactly 243 symbols, 81 per symbol and 243 distinct cyclic five-windows; those exhaust all ternary five-words. Its prefix-height extrema for pairs (0,1),(0,2),(1,2) are respectively (−4,1),(−4,1),(−2,3), width five each. Equality of global symbol frequencies makes every wrapping interval's imbalance the negative of its complementary interval, so all 243² circular factors have pair discrepancy ≤5. The independent exhaustive direct scanner confirms every cyclic interval. The matching lower and upper bounds prove the exact finite optimum; no assumption of an unsearched optimization routine is needed.

## originality

PASS

The precise quantified final claim was compared against primary sources, semantic published-result searches, equivalent mathematical formulations and stronger possible implications. No decisive coverage was found on the actually read material; sources not fully read remain recorded as risks, not represented as full-text negatives.

## value

PASS

The authors' published conjecture and exact-value table singled out the ternary order-five parameter as a natural missing case, with a general n+1 upper bound and trivial n lower bound. A complete 243-symbol certificate closing this one-unit gap resolves a concrete unfilled natural invariant that can serve as a sharp benchmark for future low-discrepancy de Bruijn constructions. No general new theorem is asserted or required for this finite exact answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
