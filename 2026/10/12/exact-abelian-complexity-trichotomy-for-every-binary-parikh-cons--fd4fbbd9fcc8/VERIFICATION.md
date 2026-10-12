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

Run `python3 verify.py` from a directory containing that file. Only the Python standard library is required. The exact observed output is:

`VERIFY_OK morphisms=9 nonconstant=6 pair_base_and_step=54 boundary=66 prefix_checks=9216 direct_class_checks=576`

The checker enumerates all nine admissible substitutions, verifies the finite ordered-pair base for all six nonconstant morphisms and lags \(3\) to \(8\), verifies the eighteen symbolic maps closing the induction, computes exact factor-weight boundary extrema, checks each length \(1\) through \(8\), and tests all three classification formulas for \(1\le n\le1024\). It uses real prefixes of \(\sigma^8(0)\) for the finite instances and constructs the weight sequence directly.

The all-length result additionally requires the induction and sliding-window argument in RESULT.md. Enumerating finite windows alone does not certify an infinite statement. No independent audit has been performed.
