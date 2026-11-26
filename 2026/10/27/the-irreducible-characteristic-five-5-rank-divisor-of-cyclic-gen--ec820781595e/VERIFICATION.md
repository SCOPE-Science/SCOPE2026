---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The five finite branch points and infinity have tame index 3, so the genus is four. Orders at infinity of x,y,dx are -3,-5,-4, respectively; at a finite branch point dx has order 2 and y has order 1. These checks give the displayed regular basis. Rewriting u=dx/y as (y^-2)^5 f^3 dx and v_i=x^i dx/y^2 as (y^-1)^5 x^i f dx gives the stated off-diagonal Cartier blocks. The semilinear square on u has coefficient H^(1/25); when H=0 the cube kills the basis, and otherwise the span of u and Cartier(u) is the entire stable image of dimension two. Multinomial extraction at x exponents 4,9,14 verifies the eleven terms (the last coefficient is 3a_4). The weight of each alpha_i is 11-5i, and that of beta_i^5 is 5+5i. The leading coefficient in a_0 is 3a_4^6 while the constant term retains a_3^8 at a_4=0; hence the quadratic is primitive. Its discriminant at a_1=a_2=0,a_4=1 is a_3^8(a_3^2+3), which has simple roots and is not a square. A polynomial square in the fraction field of a UFD must already be a square in the ring, so specialization rules out a square and Gauss's lemma gives absolute irreducibility. Both polynomial examples meet the stated squarefree conditions and give H=0 and H=2, respectively, so the squarefree open meets the hypersurface and its complement.

## originality

PASS

Credit is limited to the explicit polynomial criterion and the irreducibility statement in full affine quintic coefficient space. Abstract moduli-level rank-zero irreducibility and codimension were known. A separate later-dated Resultary record demonstrably gives the exact same H and claims, plus additional a-number data; this rules out treating the two statements as distinct mathematics but does not establish coverage preceding the frozen record. No earlier covering statement for the explicit coefficient hypersurface was established in the bounded comparisons.

## value

PASS

An explicit test in coefficients is usable for any smooth member without computing a Jacobian or passing to a moduli space. Proving the polynomial absolutely irreducible ensures the observed rank drop is a single divisor in this marked parameter space, a structural statement that an abstract quotient or a prime-field census does not give by itself. The claim is about this equation and its locus, not the already known abstract genus-four rank stratum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
