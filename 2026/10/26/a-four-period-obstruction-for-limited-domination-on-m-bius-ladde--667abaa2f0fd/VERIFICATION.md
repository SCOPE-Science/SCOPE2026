---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Counting crossing edges E(D,U) from the dominating outside vertices and the ≤1 outside neighbor per inside vertex gives |D|≥n, with equality iff every vertex has one crossing neighbor. Binary coloring crossing a_i=c_i XOR c_(i+1), b_i=c_i XOR c_(i+n) yields a_(i-1)+a_i+b_i=1. Subtract antipodal equations to obtain d_i=a_(i+n)−a_i=(-1)^i d_0, and chord parity b_i≡sum_(j=i)^(i+n-1) a_j (mod2); the even-n case forces alternating a_i, b_i=0 and n divisible4; odd n has no coherent case. For multiples of four there are two alternating a phases times global color complement, exactly four D and two cuts. For all other n the arc D={0,...,n} has n+1 vertices and satisfies both requirements. Independently brute-enumerated every subset for n=3..8 and reproduced equality multiplicity.

## originality

PASS

The half-order lower bound is standard for cubic limited domination, n=3 value is known, and equality is a perfect matching cut problem. The new candidate is an exact Möbius-ladder congruence and count of its equality cuts. Primary work on limited domination in cubic graph families and perfect matching cuts does not state a parameter-complete Möbius-ladder characterization in the inspected statements.

## value

PASS

The exact n mod4 cutoff and the rigidity of equality minimizers form a natural infinite-family domination classification with a meaningful boundary not determined by general half-order bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
