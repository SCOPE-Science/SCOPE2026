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

Run `python3 verify.py` from the extracted package. It uses exact integer binomial recurrences and independently reproduces the modular product. The test spans every position for \(r=2,\ldots,12\) and \(s=2,\ldots,\min(r,8)\), totaling 56,780 comparisons. It also checks the entire predicted histogram for each such row and the four-residue modulus-16 law for \(r=4,\ldots,12\). The test output was:

```
VERIFY_OK cases=56780 rows=2..12 precisions=2..8
MOD16_COUNTS: 1=2^(r-1)-2, 9=2^(r-1)-2, 13=2, 7=1; r>=4
```

The proof in `RESULT.md` is symbolic and applies to unbounded \(r\) and \(s\) within the stated domain. The program is not a substitute for this proof or an independent audit. A plausible older source could be inaccessible; originality is therefore subject to the recorded literature limitations.
