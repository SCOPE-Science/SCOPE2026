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

# Verification and reproducibility

Run `python artifacts/verify.py` using Python 3 with SymPy. The checker rebuilds cyclic sixth moments as squares of cubic convolution coefficients, groups seven coefficients by residue class, and confirms the exact symbolic one-variable polynomials and five derivative factorizations. It isolates a unique positive root of the exceptional quintic, checks two simplified radical constants, and compares direct discrete Fourier moments with their cyclic-convolution representation.

The replay output from the packaged checker was:

`VERIFY_OK exact_residue_polynomials=13 exact_derivatives=5 root_isolation=PASS random_complex_cases=3080 subgroup_cases=7 reflection_cases=750 all_checks=PASS`

The numerical cases check cyclic orders \(3\) through \(16\) and subgroup lifts on groups of size \(4r\). Numeric tolerances are used only for sample comparisons, not for the proof or the exact symbolic checks. The unrestricted quantifiers, exact maximizers and equality classification require the proof in `RESULT.md`; the checker is not an independent proof of those assertions.
