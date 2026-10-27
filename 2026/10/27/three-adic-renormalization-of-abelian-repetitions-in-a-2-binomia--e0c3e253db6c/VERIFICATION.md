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

Execute `python3 check_threeadic.py` from the extracted package directory. The checker independently implements the substitution and its digit recursion, enumerates exact window compositions at powers of three, and checks the adjacent-equality coding identity. Expected success lines include `PASS: digit recursion verified on 59049 symbols`, `PASS: block sum, adjacent pair, and forbidden triple verified on 42000 windows`, and `PASS: exact local coding identity for 770 triple-index tests`.

These are bounded regression checks. The unbounded quantifiers in the finding are justified by the ternary-residue argument and not by numerical extrapolation. The experiment does not classify other block lengths. Independent mathematical audit is not performed.
