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

Run `python checker.py` in Python 3 with the files unpacked into one directory. No third-party dependencies are used. The script enumerates all choices of a second linear order for sizes two through seven, computes the exact aligned/reversed successor-overlap distribution, and checks all mixed factorial moments up to total order two against independent compatible-edge counting. It also checks reversal symmetry and exact polynomial coefficient distinctness for the fifty spectral expressions. In a separate finite stress test it computes exact recursive two-variable unary rank-two types for 54 synthetically sampled models whose defect neighborhoods pass a local-isolation test, verifying matching type sets within each of the nine overlap states. The expected output is `TWO_SUCCESSOR_FINITE_CHECKS_OK factorial_moments= 33 spectrum_polynomials= 50 clean_profiles= 54 state_groups= 9`.

These checks cover finite combinatorial identities and arithmetic, not the infinite multivariate moment theorem, local-isolation limit, or logical normal-form argument. Those are justified in the accompanying proof. There was no independent audit or external formal certification. The full theorem uses ordinary first-order quantifiers only, with two variable names and quantifier rank at most three.
