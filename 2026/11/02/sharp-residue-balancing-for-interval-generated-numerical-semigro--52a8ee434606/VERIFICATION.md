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

The all-parameter proof is in RESULT.md. A standalone Python 3 checker is included as `verify.py`; running `python3 verify.py` reports the number of independently enumerated semigroups, divisor-modulus residue histograms, and sharp examples. Its algorithm builds the semigroup membership set by recurrence from its generators and compares it with the distinct-gap interval formula and the closed histogram. It additionally tests the equidistribution criterion, the coprime discrepancy bound, the nonunit exact spread, and examples showing sharpness.

Observed finite test result: `PASS: 2844 semigroups, 7921 divisor-modulus profiles, 26 sharp examples`.

These finite checks are diagnostics. The proof uses exact interval decompositions, modular counting, and a cyclic-block stabilizer argument for *all* integer parameters in the stated domain. Source and novelty comparisons remain subject to bibliographic limits; independent scientific assessment was not performed.
