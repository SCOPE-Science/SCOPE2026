---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The PASS is for repairs/5/RESULT.md. The frozen Finding's unrestricted wording about the largest ordinary length of quartics was not established: the cited Theorem 1.3 applies to Blanc–Furter length two and its introduction explicitly distinguishes the separate de Jonquières stratum. The repaired claim limits maximality to length two. Equation (3) is precisely the homogeneous triple at issue; invertible projective left composition preserves the degree and lengths. Write psi=B A with A=(x+y^2,y), B=L A L and L the swap. In the diagonal case strict degree dominance inductively gives coordinate degrees 2*4^(n-1),4^n. In the antidiagonal case A G A^(-1)=A D A L=(ay+(a+b^2)x^2,bx). For nonzero quadratic coefficient its iterates have degrees 2^n by strict dominance, and conjugation changes those degrees by at most a factor four in either direction. On the exceptional curve the conjugate is linear and the degrees are bounded. Its square is the affine scalar -b^3, not generally the identity on the projective extension [tX:tY:Z]. Odd powers exchange axes, so the exact finite order is twice the order of that scalar, and a complex cube root realizes each case. The supplied checker was inspected, not executed; the algebra above holds for all nonzero complex parameters and does not rely on finite sampling.

## originality

PASS

The repaired finding claims neither the known length nor a new abstract conjugacy class. It determines exactly how dynamical degree varies under affine monomial postcomposition of the particular length-seven representative, and establishes a torsion realization within that presentation. Inspected relevant statements establish the known ingredients but not this comparison within the same ordinary-length and projective-equivalence stratum.

## value

PASS

This is a complete parameter classification for the natural subgroup preserving or swapping the coordinate directions, not a few chosen examples. In a single two-sided projective class it exhibits three growth regimes at unchanged degree and relative maximal ordinary length. The exceptional curve separates bounded and exponential growth and realizes every even order while staying in the same class. The useful fact is this lack of control by the fixed presentation invariants, not the textbook Hénon/linear distinction in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
