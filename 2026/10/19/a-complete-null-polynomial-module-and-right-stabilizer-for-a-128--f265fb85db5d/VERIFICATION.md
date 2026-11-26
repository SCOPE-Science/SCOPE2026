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

The seven displayed relations evaluate to zero by the pair multiplication law and the identities for t(r), t(r)^2, t(r)^3. Their distinct leading-coefficient directions give a free basis for their span and reduce arbitrary degrees to the stated thirty normal monomials. The specified 30 by 30 minor was reconstructed using explicit binary matrices and has exact F2-rank 30. There is also a short independent check: write any normal form as F(t)+xH(t), using the monic basis t^j, x t^j for central polynomials. Comparing evaluation at r and r+1 separates F from H since t(r+1)=t(r). For either separated part, r=0 kills its constant coefficient; r=(0,I) kills the triangular part of its t coefficient; r=(E12,0) kills the remaining t coefficient, which is supported in the first column of the upper-right block; r=(E12,E21) has t(r)^2=(0,I), so kills the remaining t^2 coefficient, supported in the triangular block. The two coupled relations have entry gcd t^2 and determinant t^6, giving factors t^2,t^4; the other five relations are diagonal. The resulting exponents sum to 15 and deg(t)=2, giving 2^30 functions. The first six generators stay null after any constant right multiplier. The seventh, g, has product class (a+d)U11 t^3 for a multiplier with diagonal entries a,d; U11 t^3 represents the nonzero normal form U12 t^2. This gives 64 stabilizing constants. Degree at most five uses only the four low-degree generators, which are stable under constants and hence, by centrality, under arbitrary polynomials. g U11 supplies the failure in degree six.

## originality

PASS

The ring, failure of the right-ideal property and degree-six witness are already in Havlovec and receive no novelty credit. The complete module, invariant factors and exact function count, constant right-stabilizer, and exclusion of all smaller failure degrees are supported distinct additions on the evidence inspected.

## value

PASS

This is the motivated counterexample ring from a finite-ring null-polynomial problem. Its full evaluation kernel gives an exact basis and function count in all polynomial degrees; the stabilizer identifies precisely which constants preserve it, and the least degree distinguishes the known witness from all lower-degree possibilities. These strengthen understanding of the counterexample rather than merely replaying it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
