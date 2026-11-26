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

Grouping by the number of occupied hubs gives Z=(1+q^2 z)^m+2q^m z(1+z)^m+z^2(q^2+z)^m; spin complement gives reciprocity and the constant term is 1. A separate exact enumeration of all 96 spin subsets for the two graphs confirmed both coefficient vectors, reciprocal reductions and five sign identities. For m=3, Z=(z+1)z^2 F3(z+1/z) and the monic quadratic F3 has signs +,-,+ at negative infinity, -q^3-q^2, -2: the last two values are -(q-1)^2(3q^3+5q^2+2q+1) and (q-1)^2(q+1)^2(q^2+5). The two distinct y-roots are below -2, and F3(-2) is nonzero so z=-1 is simple. For m=4 the monic cubic F4 in Z=z^3 F4(z+1/z) has signs -,+,-,+ at negative infinity, -q^4-q^2, -2, 2, with the finite values q^2(q^2-1)^3(4q^2+5), -2(q^2-1)^4 and 2(q^8+4q^6+22q^4+4q^2+1). Each interval gives a distinct root, exhausting its degree. The map back by z^2-yz+1=0 gives negative reciprocal pairs for y<-2 and a nonreal conjugate unit-circle pair for -2<y<2; all are simple since y=±2 is excluded in the reductions. This proves the uniform statement, rather than extrapolating finite q samples. At q=1 all roots coalesce at -1, outside the claim. VERIFICATION.md and verify.py were inspected, not executed; the supplied four sample classifications use floating interval midpoints after rational isolation and are corroboration only. The all-coupling certificate is algebraic.

## originality

PASS

The supported distinct result is the exact fixed-graph census at every strictly antiferromagnetic coupling and the contrasting appearance of a circular pair after adding the fourth leaf. Reciprocal reduction, spin grouping, and real-zero methods are not claimed to be new. The checked primary results either impose inapplicable graph conditions, apply only over a coupling range, or concern sets of zeros pooled over graph classes.

## value

PASS

A natural neighboring pair of simple antiferromagnets changes its root type under a one-leaf addition, uniformly throughout the strictly antiferromagnetic regime. The result gives a usable finite benchmark for general zero-location conjectures and distinguishes a persistent effect from a sample-temperature artifact. It does not assert a threshold theorem for all complete bipartite graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
