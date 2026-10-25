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

# Reproduction of finite checks

Run `python3 verify_affine_double.py` with Python 3. The script uses only the standard library, constructs group products and powers directly, computes ordinary group characters, and evaluates the published finite-group Drinfeld-double indicator sum without relying on the new closed expressions in its sum evaluator.

The scalar-affine checks cover finite fields of orders \(3,4,5,7,8,9\), including nonprime field arithmetic, and every allowed cyclic complement subgroup listed by the script. For each case, the script loops over all relevant identity, nonzero-kernel, and complement-class character labels and indicator indices up to at least \(15\). The separate abelian-kernel checks cover \(C_9\rtimes C_2\), \(C_{25}\rtimes C_4\), and selected labels of \(C_9^2\rtimes C_2\), including torsion structures that are not elementary abelian. Successful execution ends with `VERIFY_OK_AFFINE_DOUBLE_INDICATORS` and `VERIFY_OK_ALL_FINITE_ABELIAN_KERNELS`.

The finite computations do not test all finite abelian groups or all positive indices, and they are not an infinite proof. The proof of the theorem is the symbolic endomorphism calculation in `RESULT.md`; the code provides independent arithmetic checks of selected finite instances. No independent scientific audit has been performed.
