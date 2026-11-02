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

# Reproducible checks and boundaries

The standalone `verify.py` uses Python 3 and SymPy. Run `python3 verify.py` from the package directory to reproduce exact polynomial discriminant, root parametrization, unit-circle root bounds, critical factorization at \(\mu=15/16\), endpoint residue-amplitude comparison, sixth-coefficient rational identity, signed mass identity and coefficient-generating-function agreement. It also checks representative root orderings at positive step parameters. The script completed with the printed PASS count, but numerical root checks are not a proof of the infinite-index statement.

The proof in `RESULT.md` handles the infinite quantifier via one real and two complex conjugate characteristic roots, comparison of their moduli, strict positivity of the real residue, rational/irrational phase sign arguments and a separate exact endpoint amplitude calculation. The total variation of the causal Green series converges because every characteristic root has modulus less than one. The all-index strict-positivity cutoff, arbitrary starters and nonlinear positivity are not claimed. Independent validation is not performed.
