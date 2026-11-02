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

# Reproducibility and evidence limits

The theorem has a complete all-rank mathematical induction in `RESULT.md`, involving the unique fresh central marker and two binary high-bit cases plus their symmetric counterpart. It proves the set classification, disjointness of factors, the generating polynomial, the exact lengthwise counts, and the total; finite computation is not used to infer an infinite proposition.

Run `python3 checker.py` in any directory with Python 3.10 or newer. The checker independently constructs the literal Zimin word; tests every nonempty contiguous factor for borders; builds the explicitly claimed disjoint-bit template set; and compares sets and counts for ranks 1–8. A separate exhaustive loop checks the bit-pair characterization for marker ranks 0–7. All these tests passed at preparation. Expected final line: `ALL CHECKS PASS`.

The computational checks stop at rank eight for factor enumeration and rank seven for the bit-pair test. These are exact finite checks but **not** exhaustive over arbitrary rank. Historical-priority comparisons relied on accessible full-text material and research-record searches; absence of hits cannot prove no equivalent result exists. Independent audit status: not performed.
