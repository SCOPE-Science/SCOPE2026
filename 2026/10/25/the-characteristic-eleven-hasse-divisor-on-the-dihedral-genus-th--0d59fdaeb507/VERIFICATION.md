---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Independent symbolic expansion in F_11[a,z] of (z^2+a z+1)^5 produced [z²]=[z^8]=u=5-a² and [z^5]=v=a^5-2a³-3a=a(a²-3)(a²+1), and therefore H=[(0,0,u),(0,v,0),(u,0,0)]. Verified gcd(u,v)=1 and squarefreeness of the individual factors; det H=-u²v has degree nine. For a²!=4 squarefreeness of degree-eight polynomial gives genus three. Anti-diagonal u/u and diagonal v are stable under p-power semilinear iteration: p-rank equals nonzero coordinate count. u,v never simultaneously zero (at a²=5 v=a!=0). Cartier rank=rank(H), a-number=3-rank(H). All seven parameters are smooth and multiplicity lengths exactly 2+2+5=9. F_11 point checks alone would not cover algebraic closure; factorization does.

## originality

PASS

The same dihedral family and w=a² coordinate are classical from Gutierrez–Shaska, and general hyperelliptic Hasse–Witt coefficient and rank machinery is prior work. The inspected primary normal-form paper does not enumerate the seven special characteristic-eleven parameters, their exact ranks or the two doubled Hasse intersections. This is an exact family-specific complete stratification, not a novel formula for Hasse–Witt matrices. Similar treatments under modular coordinates remain plausible.

## value

PASS

The genus-three dihedral pencil is a naturally moduli-motivated one-dimensional automorphism locus. The scheme-theoretic nonordinary divisor has two tangible tangencies, exactly two p-rank-1 members and no rank-0 members, a complete stratification over the algebraic closure. A future researcher studying characteristic-11 Hasse intersections or dihedral curve families needs these exact multiplicities, rather than only generic p-rank or an algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
