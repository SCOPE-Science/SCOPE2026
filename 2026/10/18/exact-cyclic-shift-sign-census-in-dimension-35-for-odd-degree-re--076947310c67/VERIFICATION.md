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

# Reproduction of the exact cyclic-shift sign census

Use `python3 verification/spectral_census.py` from the package root. Python 3's standard library is sufficient. The script checks all possible seven-positive and thirteen-positive subsets of the half-shift indices, with exhaustive rather than sampled combinations. It bounds \(\pi\) by the alternating arctangent expansion of Machin's identity and bounds all required real cosines by rational Taylor remainder inequalities. Each spectral comparison is then an integer interval test; it never uses floating-point tolerances.

Expected results: \(\binom{17}{7}=19448\) tested, \(19\) accepted; \(\binom{17}{13}=2380\) tested, \(0\) accepted; three disjoint multiplier orbits of sizes \(12,3,4\), whose union is precisely the surviving set. The program explicitly raises on any ambiguous spectral interval. For all surviving profiles all nonconstant Fourier eigenvalues have certified strictly positive lower bounds, so the Gram rank is \(34\).

The field-degree reduction and the real Fourier-factor converse are algebraic arguments given in `RESULT.md`; the script certifies their finite spectral predicate rather than proving them by numerics. The code does not check any non-shift Weyl–Heisenberg condition or constrain the algebraic degree of an explicit recovered vector. Independent audit has not been performed.
