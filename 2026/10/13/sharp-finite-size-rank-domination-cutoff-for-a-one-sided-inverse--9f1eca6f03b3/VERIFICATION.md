---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For square matrices, rank(g(X,Y))≤C rank(XY−I) at all m≤N is equivalent to zero evaluation whenever XY=I, since all other denominators have rank at least one and C=N trivially works. Square one-sided inverse implies Y=X^{-1}; embedding X⊕I also reduces all smaller dimensions to N. Modulo (xy−1,yx−1), any g becomes Laurent π(g)(t). Rational canonical form forces its numerator to be divisible by the least common annihilator P_q,N=∏_{irreducible φ≠t, deg φ≤N} φ^{floor(N/deg φ)}; companion matrices force necessity. At unrestricted sizes the degrees diverge and the kernel is (xy−1,yx−1); equality rank(XY−I)=rank(YX−I) plus finite ideal expressions gives a global rank constant. Degree L free words yield Laurent exponents [-L,L], so 2L≥deg P, sharp by lifting t^{-ceil(D/2)}P into x and y monomials. Independently computed P_2,2=(t+1)^2(t²+t+1) modulo two and checked the stated 3×3 inverse-pair counterexample. This proves universal finite prime powers, not merely tested small fields.

## originality

PASS

Yan–Yang study the homogeneous rank Nullstellensatz and mention the nonhomogeneous pair (xy−1,yx−1), including the rank equality needed here. They do not in the accessible abstract/source comparison give a finite-field filtration by universal annihilator polynomials or a sharp least false-positive free-word degree. Shamovich–Volčič study equal rank on all matrices over characteristic zero, not the bounded finite-field inequality. The irreducible-product annihilator is a standard rational-canonical-form consequence; originality is its exact interaction with rank domination and the sharp degree criterion. Similar Resultary finite-field matrix work had different predicates. Residual risk: older finite-field generalized linear group polynomial identity tables might contain the annihilator as a named result.

## value

PASS

The exact finite-size/degree threshold answers a fundamental verification question: when can bounded matrix tests legitimately certify a global free-polynomial rank implication, and what is the first explicit false positive? The complete ideal filtration over every finite field and tight ceiling deg(P)/2 provide useful structural bounds, even though rational canonical form and irreducible enumeration are standard tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
