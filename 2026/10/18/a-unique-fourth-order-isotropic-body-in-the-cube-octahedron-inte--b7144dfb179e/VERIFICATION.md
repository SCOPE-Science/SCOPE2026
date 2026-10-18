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

# Reproduction of exact checks

Run `python3 verify.py` from the directory containing this file, with Python 3.9 or later. No third-party packages are required. The script independently reconstructs the monomial moment polynomials from the inclusion–exclusion simplex-integral identity. It checks the degree-seven moment-defect polynomial, endpoint signs, unique positive root of the transformed first-interval polynomial, uniform negativity on the second interval, and nonzero sixth-order anisotropy by a rigorous ten-coefficient sign certificate.

The tested execution produced:

```
SIXTH_DEFECT_BERNSTEIN_ALL_NEGATIVE 10
C_STAR_APPROX 1.6990676583226154987602112148832804
ENDPOINT_DEFECTS 2/105 -2/7 -16/15
FIRST_INTERVAL_SIGN_PATTERN ++++++--
SECOND_INTERVAL_SIGN_PATTERN --------
VERIFY_OK exact_moment_polynomials root_uniqueness fourth_isotropy sixth_anisotropy
```

The rational-algebra proof applies to **all positive real parameters**. The last printed decimal is an approximation of an exactly isolated root; numerical root-finding is not evidence for the uniqueness theorem. Separately, two-dimensional numerical quadrature of the exact section integral for the fourth-moment monomials at \(c=1.2\), \(c=c_*\), \(c=1.9\), and \(c=2.5\) agreed with the symbolic formulas to less than \(2\times10^{-8}\) in each comparison. Numerical quadrature is corroborative only. No independent mathematical audit has been performed.
