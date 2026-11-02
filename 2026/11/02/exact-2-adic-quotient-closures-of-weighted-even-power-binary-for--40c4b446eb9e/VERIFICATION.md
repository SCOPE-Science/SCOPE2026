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

# Verification of the exact local closure

The mathematical argument uses the standard surjectivity \( (\mathbb Z_2^\times)^n=1+2^{\nu_2(n)+2}\mathbb Z_2\) for even \(n\), followed by an exhaustive three-case valuation decomposition of the two-variable form. This proves the infinite closure and the three valuation residue classes without extrapolating from finite data.

`python3 verify.py` prints `VERIFIER_OK modular_value_set_tests= 456 nonisotropic_val_shell_tests= 2176`. It tests the image of \(x^n+c y^n\) modulo \(2^6\), \(2^7\), and \(2^8\) for eleven even exponents and sixteen odd coefficients wherever the nonsplit hypothesis holds; a further 2,176 checks verify the elementary valuation-shell restriction. Computations are finite sanity checks, not complete verification over all parameters or a substitute for the proof.

This package has not been independently audited. The earlier density criterion, unweighted reductions, and identified bibliographic risks are recorded in the result and review.
