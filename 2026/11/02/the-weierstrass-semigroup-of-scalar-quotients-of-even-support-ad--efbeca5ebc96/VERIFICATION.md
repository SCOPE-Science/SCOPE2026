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

# Reproduction and boundaries

Run `python3 verify_semigroup.py` with Python 3 and no third-party packages. The script uses exact integer arithmetic to check the stated invariant monomial pole orders, Apéry representatives, generated semigroup through and beyond its conductor, genus, conductor, pseudo-Frobenius numbers and irredundant generators for the 14 cases documented in its output. Successful execution ends with `VERIFY_OK`.

The actual mathematical proof uses the affine invariant ring of the tame scalar quotient and uniqueness of the monomial pole orders. No finite computation is treated as a proof for all prime powers, exponent lengths, or coefficient choices. The input is the family with odd characteristic, even exponents in the additive polynomial, and nonzero first and last coefficients. No formal proof-assistant certificate or independent mathematical review is asserted.
