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

# Mathematical verification notes

The analytical proof is in `RESULT.md`. The key checks are: (i) the exact coefficient beta integral; (ii) the square-summable gamma-ratio error and the square-integrable first derivatives of the homogeneous kernel; (iii) the unitary logarithmic convolution model and Fourier-transform beta identity; (iv) the scalar Wiener--Hopf Fredholm symbol/index theorem with a declared Fourier sign convention; (v) the separate proof that zero is not Fredholm using weakly-null basis vectors; (vi) strict phase and modulus monotonicity from the gamma recurrence and Euler product, yielding every nonzero integer-parameter double point and transversality.

`CHECK.py` requires only the Python standard library and completed **6,909 assertions**, testing the coefficient gamma-ratio identities, normalization, conjugation, monotonic modulus and phase for positive integers, predicted real intersections, finite gamma-asymptotic comparisons and finite approximations to weakly-null columns. Reproduce with `python3 CHECK.py` in a directory containing the extracted source.

**Proved:** the Fredholm essential spectrum and index formula for all real \(b>0\); the nonzero transverse-double-point count and explicit locations for all integers \(m\ge1\). **Not proved:** complete spectrum, absence of isolated eigenvalues, general noninteger intersection classification, or statements for Hardy exponents other than two. Finite checks do not replace the operator-theoretic or global monotonicity proofs. Independent audit is not performed.
