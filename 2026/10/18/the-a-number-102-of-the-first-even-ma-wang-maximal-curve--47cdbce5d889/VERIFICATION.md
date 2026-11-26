---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the normalization over the algebraic closure, A=u^3-u and B=1+A^2 have simple disjoint roots, since A'=-1 and B' is nonzero at B=0. A simple root of A gives a totally ramified place and geometric connectedness; the orders 1,13,-81 are all coprime to 82. The ten tame totally ramified places give 2g-2=-164+10·81. At the finite branch places the differential valuations allow B^floor(13j/82) du/z^j with no further factors; at infinity v(u,z,du,B)=(-82,-81,-83,-492), giving precisely 0≤s≤j-2-6 floor(13j/82) for the monomial u^s. The forms are independent by the Kummer characters and the sum of their dimensions is 324, so they are a full basis. The inverse Frobenius on the characters is j↦55j mod 82. With 3j'-j=82t, z^(-j)=z^(-3j') c^t A^t B^(13t), and u is a separating parameter. Cartier takes the coefficients of exponent 3l+2 with cube roots. The c factor is a common nonzero block scalar; division of the raw output by the common B power preserves rank. The distinct target characters give a direct sum of images. An independently written, executed exact row-reduction replay counted dimension 324 and total rank 222, hence kernel dimension and geometric a-number 102.

## originality

PASS

The curve, its genus and maximality are already Ma–Wang's. The supported distinct result is the exact geometric Cartier rank/a-number of this member. The closest indexed result treats the same curve, and indeed the whole even family, but determines a Weierstrass semigroup rather than Cartier action. The closest general Cartier theorem supplies a nontrivial interval, not this exact rank. This assessment is limited to the checked statements and searches.

## value

PASS

This is the smallest member in the genuinely new even-index parameter range, not an arbitrary small instance. Its geometric a-number supplies exact information about the p-torsion beyond genus, zeta data and p-rank. A researcher comparing the torsion of maximal curves or determining the Ekedahl–Oort type of this member could use the exact value 102 as an input or as a benchmark for proposed formulas within the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
