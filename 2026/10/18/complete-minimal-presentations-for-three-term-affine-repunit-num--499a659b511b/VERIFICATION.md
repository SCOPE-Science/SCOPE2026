---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For A=a, B=ba+d and C=b^2a+(b+1)d, gcd(A,B)=1 from gcd(a,d)=1; direct expansion gives (b+1)B=bA+C and qC+rB=(b^2q+br+d)A when a=q(b+1)+r. In low range a<=b+1, reduce C to sB+K0A and eliminate Z, leaving Y^a-X^B. For high divisible case take Y^(b+1)-X^bZ and Z^q-X^(b^2q+d); for high nondivisible case add Y^r Z^q-X^M and Z^(q+1)-X^Mprime Y^(b+1-r). Forward reductions strictly lower lexicographic measure (T=y+(b+1)z, then y), terminate at exactly the a unique pairs 0<=T<a; equal weighted degrees force dT≡dTprime mod a and then T equal. Hence any toric relation reduces to zero. Deleted-relation monomial-fiber arguments ensure indispensability, and distinct relation degrees give Betti elements. Independently recomputed homogeneous relations and normal form uniqueness in eight nontrivial triples through weight100, including all three parameter regimes. Finite checks supplement the all-parameter normal form proof.

## originality

PASS

Best-of-knowledge assessment from exact implication comparisons of same mathematical objects; known special cases and general mechanisms are credited; actual full primary texts read when accessible and residual priority risk recorded. The retained exact result is not proved covered by the identified sources.

## value

PASS

The same affine-repunit three-generator numerical semigroup already has studied Frobenius/genus/Apéry invariants; explicit minimal toric presentations and first Betti degrees are natural complementary factorization invariants. Uniform formulas locate a sharp arithmetic boundary at divisibility of a by b+1 between three-generator complete intersections and three-relation noncomplete intersections. Applicable for arbitrary coprime positive a,d and b>=2, not simply recomputation of a tiny table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
