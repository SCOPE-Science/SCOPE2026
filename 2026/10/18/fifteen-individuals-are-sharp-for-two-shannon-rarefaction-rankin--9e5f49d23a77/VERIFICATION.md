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

# Reproducible checks

`verify_entropy_cross.py` needs Python 3's standard library only. Run `python3 verify_entropy_cross.py` beside this file. It generates all positive-integer abundance partitions for \(2\le N\le15\), groups equal-richness pairs, and determines sign comparisons via **integer** log-coefficient vectors with **certified rational** logarithm enclosures. The latter use 400 atanh-series terms and an explicit positive remainder bound before enclosing each logarithm on a denominator of \(10^{36}\); no floating-point tolerance governs theorem acceptance.

The expected output includes `census (15, 175, 1708, {0: 1684, 1: 23, 2: 1})`, exactly one candidate with profiles \((1,1,4,4,5)\) and \((2,2,2,2,7)\), `DIRECT_SUBSET_CROSSCHECK PASS`, and `CERTIFIED_COMPLETE_CLASSIFICATION PASS`. Every lower census has zero two-reversal comparisons. The script independently averages Shannon diversity across labelled subsets for selected sample sizes in the two witnesses; these floating-point evaluations corroborate but do not establish the strict sign pattern. No general-census-size claim is made. Independent audit has not been performed.
