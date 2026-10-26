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

# Reproducibility and verification

The accompanying standalone `verify.py` uses Python's standard-library integer arithmetic and `fractions.Fraction`. Execute `python verify.py` from a directory containing the file.

It checks exact unique base-four representations of all \(4096\) integers through \(4^6-1\), validates \(A(n)B(n)\ge n+1\) on these finite domains, constructs rational Cantor-cylinder covers for depths \(1\) through \(8\), and verifies that both required geometric gap families occur with their asserted constant CDF products at every depth. It calculates rational lower CDF values and rational tail bounds (at most \(2^{-L}\)).

Expected exact verification status:

`VERIFY_OK unique_representation=4096_at_depth6 exact_macro_gaps=all_depths_1_to_8`

At depth \(8\), the code prints exact rational enclosures: \(t=11/10\): \([134349/720896,102871/540672]\); at \(t=5/4\): \([85037/163840,514057/983040]\); at \(t=7/5\): \([406125/458752,19121/21504]\). The omitted probability comes from the finite cylinder cover and is bounded by its Lebesgue length.

These checks verify concrete integer identities and finite rational certificates; they are not an exhaustive check of all integers, not a computer proof of convergence, and not an independent review. The analytic proof of the \(W_1\) estimate, density, and infinite gap families is supplied in `RESULT.md`.
