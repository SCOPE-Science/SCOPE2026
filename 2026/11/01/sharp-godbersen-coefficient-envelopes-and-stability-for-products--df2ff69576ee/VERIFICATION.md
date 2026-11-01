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

# Scientific verification

The exact planar mixed-area polynomial, Cartesian-product volume factorization, coefficientwise positivity, Maclaurin inequality, convex chord estimate, endpoint equality conditions, continuity argument and standard lattice local central limit theorem were checked directly in the proof. The parity-dependent strict Maclaurin step uses the \(e_2\) term for even interior degrees and \(e_3\) for odd interior degrees; neither can be omitted.

Run `python3 verify_mixed_products.py` in this directory with Python 3 and only the standard library. The program has been run successfully and prints `VERIFY_OK 10957`. It independently computes exact rational planar polygon difference/Minkowski areas, all three envelopes and affine stability on a six-factor parameter grid, and exact central multinomial coefficients. The rational finite enumeration does not establish results for uncountably many convex bodies; the stated general theorem is proven analytically. The asymptotic additionally relies on the standard aperiodic lattice local central limit theorem and Stirling's formula, with variance \(1/3\).

No independent external validation has been performed. Potential historical priority overlap remains an acknowledged limitation.
