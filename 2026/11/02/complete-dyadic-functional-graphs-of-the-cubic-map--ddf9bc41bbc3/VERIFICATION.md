---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every k>=5 the even restriction of f(x)=x+x^3 mod 2^k is an isometry since f(a)-f(b)=(a-b)(1+a^2+ab+b^2), multiplier=1 mod4 for evens; it therefore permutes the finite even set. For x with ν2(x)=r>=1, f(x)-x=x^3 has valuation 3r. The iterate-difference quotient remains 1 mod4, so doubling iteration gives ν2(f^(2^j)(x)-x)=3r+j, and the least period is 2^max(k-3r,0). Every valuation stratum size 2^(k-r-1) therefore has the claimed quotient count of cycles and zero is fixed. Odd a in one class mod8 satisfies ν2(f(a)-f(b))=ν2(a-b)+2, and odd residues map precisely to even targets ±2 mod32 with four sources per contributing source class and eight total. The resulting indegrees are 0:2^(k-1), 1:7*2^(k-4), 9:2^(k-4), with odd leaves depth exactly one. Independent brute force graphs k=5..11 matched complete cycle and indegree counts.

## originality

PASS

General 2-adic polynomial cycle-lifting in Fan–Liao can be specialized but the inspected statements and quadratic examples do not present the exact map-specific cycle, leaf and indegree census. DesJardins–Zieve treats odd primes, and Resultary cubic-graph hits address a distinct spectral construction. The natural cubic map’s complete finite 2-power graph appears best-of-knowledge new, subject to specialized dynamical systems literature not fully indexed.

## value

PASS

This is an all-level structural classification of a simple nonlinear 2-adic dynamical system, including exact ramified odd fibers and cycle lengths by valuation. It gives the complete graph, not just example orbits, and is a useful baseline for finite-ring dynamical classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
