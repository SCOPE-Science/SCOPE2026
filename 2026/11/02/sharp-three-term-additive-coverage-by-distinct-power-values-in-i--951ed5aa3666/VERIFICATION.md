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

## Reproducibility

Run `python3 verify.py` with Python 3 standard library. The checker independently enumerates distinct \(d\)-th-power values, all three-element subsets, and their additive target sets in 16 finite instances. It includes \(\mathbb Z/p^m\mathbb Z\) for several primes and lengths, \(\operatorname{GR}(4,16)\), fields of sizes four and eight, and length-two rings with residue field of size nine. Expected missing-target sets are hard-coded as separate exact assertions; the successful output is `VERIFY_OK`.

## Proof scope and limitations

The manuscript proves the complete infinite classification by residue lifting and an explicit binary nonunit argument. Exhaustive finite tests supplement but do not prove the universal quantifiers. The original journal full texts from 2019 and 2023 were not obtained; the accessible comparison includes their detailed descriptions in Gu Appendix A. Independent validation remains unperformed.
