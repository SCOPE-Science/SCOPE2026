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

The included `CHECK.py` is a standalone Python 3 script using NumPy, SciPy, and SymPy. Execute `python CHECK.py` from the directory containing the file. The code checks exact symbolic identities between the raw Fourier numerator, its degree-six polynomial, and the Bernstein basis coefficients. It compares twenty-five independently evaluated Bessel integrals with the closed Fourier formula, checks the zero-frequency endpoint and positive nonzero-frequency behavior numerically, and gives an explicit 36-site finite Gram-matrix negative eigenvalue outside the admissible range.

Actual execution reported all symbolic checks PASS; 25 numerical integral comparisons PASS (maximum absolute discrepancy \(5.33\times10^{-15}\)); origin and sampled sign comparisons PASS; and a finite-grid negative eigenvalue approximately \(-0.012938854494\) at \(a=1\), \(\omega=0.8\). The exact admissibility claim is established analytically in `RESULT.md`, not by numerical sampling. Independent mathematical audit and validation are not performed.
