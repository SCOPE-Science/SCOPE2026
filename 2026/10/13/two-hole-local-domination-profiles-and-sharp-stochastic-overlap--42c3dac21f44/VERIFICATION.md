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

Run `python3 verify.py` using Python 3 standard library; compare the textual stdout with `verification_output.txt`. The script independently constructs closed-neighborhood bitmasks for every graph of orders 4 through 7 possessing the prescribed degree-defect-two root. It directly enumerates all vertex subsets containing the root and verifies domination at every vertex, without reusing the two-neighborhood characterization. It compares the resulting cardinality histograms against the stated closed form.

The program also checks every feasible connected parameter profile through order 9 using exact integer coefficients and rational means, including adjacent-overlap stochastic tail comparisons and the upper bound with its equality condition. It prints counts for 33,864 graphs, 2,131,008 candidate subsets, 360 parameter profiles and 140 nontrivial adjacent-overlap comparisons. Its finite coverage is exhaustive in the stated finite domain only. The proof in `RESULT.md` supplies the infinite quantifiers, stochastic coupling, feasibility construction and equality argument.

The checker requires no external packages, network, or unpublished data. The included output is an actual run, not a substitute for independent external validation.
