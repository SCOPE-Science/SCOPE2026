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
Run `python3 verify.py` with Python 3. SymPy, if installed, additionally activates direct characteristic-polynomial computations. The attached output was obtained by actually running the exact embedded code in an environment with SymPy.

The checks cover: (i) binary matrix ranks of all powers through the dimension for every size from 3 to 80 under both the modified and ordinary rules; (ii) full orbit-following on all 4,088 labelled configurations for sizes 3 to 11, measuring first repeat directly; and (iii) symbolic characteristic polynomials for sizes 3 to 17. These agree with the formulas derived in `RESULT.md`.

They are not an exhaustive check of infinitely many sizes and do not establish novelty. The all-size proof is mathematical. No independent audit has been performed.
