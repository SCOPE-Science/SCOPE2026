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

Execute `python3 verify.py` with Python 3. It should print `VERIFY_OK` after the complete finite-field enumeration. It checks the three irreducible modulus polynomials, the nonsquare \(-1\) in \(\mathbb F_7\) and its square roots in the degree-two and degree-four extensions, the rational-point counts for \(a=0\) over four successive extension degrees, those for \(a^2=-1\) over extensions of degree two and four, and the four positions and rank alternatives of the Cartier–Manin matrix.

For the two curves over \(\mathbb F_{2401}\), the reported census `(10, 1391, 1000, 2794)` records branch zeros, nonzero-square values, nonsquare values and rational points, including both points at infinity. The argument that this count gives supersingularity uses the Hasse–Weil upper-bound equality case; the claim about geometric isomorphism classes additionally invokes the published automorphism-family classification. Neither assertion is inferred from incomplete finite-field experiments. This is a self-review, not independent validation.
