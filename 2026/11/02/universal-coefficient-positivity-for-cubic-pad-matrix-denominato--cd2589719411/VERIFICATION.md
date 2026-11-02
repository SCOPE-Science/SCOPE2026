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

# Reproducible verification

The analytic proof in `RESULT.md` establishes positivity for all integers \(k,n\ge0\). The independent-of-proof finite checks below test its critical algebra without treating enumeration as a proof of the infinite claim.

Run from the extracted package directory:

```
python3 verify.py
```

Requires Python 3.10+ and SymPy. Verified output:

```
VERIFY_OK 15914 exact checks, with symbolic cubic and residue identities
```

The script checks (i) the normalized Padé cubic and its depressed form, (ii) the exact factored residue inequality and the sign polynomial, (iii) 15,884 exact-rational coefficient and recurrence tests for 44 parameter values over 181 indices (including zeros and equality cases), and (iv) strictly positive rational inverses for a symmetric irreducible nonnegative test matrix. The number of checks counts assertions in the script, not sampled proof cases or independent external certification.

The source theorem requires only elementary cubic algebra, partial fractions and the Perron eigenvector theorem. No floating-point root finding enters its proof. The supplementary finite tests do not establish general convergence of full Padé numerators, high-degree results, or rounding stability.
