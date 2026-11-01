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

# Verification of the quartic-egg zero-free threshold

Execute `python3 verify.py` using a standard Python 3 interpreter. The checker uses only `fractions.Fraction`, `math.comb`, and elementary exact polynomial arithmetic. On successful completion it prints `EXACT_CERTIFICATE_OK`.

It independently builds the eleven-minus-one finite numerator degrees from the rational generating-function coefficients, transforms them through the unit-disk/right-half-plane Cayley map, and constructs the complete Routh arrays with exact rational pivot divisions. It asserts the predicted first-column sign strings for every complex dimension two through eleven, rejects zero pivots, and verifies that the transformed polynomials have no imaginary-axis roots by exact Euclidean gcds. It also proves squarefreeness of the dimension-eleven numerator by polynomial gcd, checks all its coefficients alternate strictly, and cross-checks the two-dimensional numerator against the independently available explicit formula.

The root-count inference uses the classical Routh–Hurwitz sign variation theorem; the checker implements the certificate arithmetic, not a generic proof of that theorem. The reduction from the reproducing kernel to the scalar polynomial uses the cited Fefferman–Szegő formula. Approximate complex roots are given for orientation only and do not certify existence or uniqueness. Dimensions beyond eleven and exponents other than two were neither claimed nor verified.
