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

Run `python verify.py` using a standard Python 3 interpreter. No nonstandard packages, network access, or external data files are required. The expected final output is `CHECK_OK`.

The program reconstructs the three sign-region lower polynomials directly from the root-magnitude formula. On boxes containing the zero-, one-, and three-high-radius regions, it expands each polynomial into the degree-four Bernstein basis using exact rational coefficients. Their exact smallest coefficients are respectively \(247/81\), \(344/729\), and \(2\), all strictly positive.

For the two-high-radius region, it expands the discriminant complement \(D=AC-B^2\) after \(u=1-a\), \(v=1-b\). The entire rectangle \([0,7/20]^2\) is covered by degree-eight tensor Bernstein coefficients. All eighty-one coefficients are nonnegative, and precisely the \((0,0)\) coefficient is zero. This proves \(D\ge0\) on a continuum, with equality only at \(u=v=0\), because the Bernstein basis is a partition of unity and all other coefficients are positive.

Independently, the program confirms that \((1+z)^2(1-z/4)\) has coefficient sequence \((1,7/4,1/2,-1/4)\), Hardy norm square \(35/8\), and first-coefficient ratio square \(7/10\). The angle inequality and classification of equality phases are elementary algebra given in `RESULT.md`; the code's finite exact polynomial certificates supplement that derivation rather than sampling possible roots. No independent audit or arbitrary-precision numerical inference is asserted.
