---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Use tetrahedron tight-frame identities Σt_i=0, Σt_i²=4/3 to parametrize directions. For x=rho/R>0 with nonzero squared distance factors, constrained log-product extrema have at most two distinct t_i; three possibilities give squared product A=(x-1)²(1+x²+2x/3)³, B=(x+1)²(1+x²-2x/3)³ and C=(1+2x²/3+x⁴)². Exact independent symbolic factorizations A-C=-64x³(x²+x+1)/27, B-C=64x³(x²-x+1)/27, A-B=-128x³(x²+1)/27 establish A<C<B. x=1 zeros and x=0 center handled; continuity fills interval. Sampled random directions over eight positive radii with no violation; analytical proof is the basis.

## originality

PASS

Hajja et al's relation identifies algebraic constraints on tetrahedral vertex distances, not the radial product's min/max; neighboring same-date SCOPE sum profile uses a different function. The exact product extremal inequalities require optimization beyond the known relation. Independent semantic searches returned the identical October 4 finding as first hit (self-match, not external prior evidence); no stronger implication identified among actually inspected competing sources. This is a qualified best-of-knowledge judgment.

## value

PASS

The product of distances to a regular tetrahedron's vertices is a natural multiplicative geometric invariant. Its entire sharp fixed-radius range, directions of extremizers and equality cases are not consequences merely of knowing algebraic relations among squared distances; the full profile provides a benchmark extremal result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
