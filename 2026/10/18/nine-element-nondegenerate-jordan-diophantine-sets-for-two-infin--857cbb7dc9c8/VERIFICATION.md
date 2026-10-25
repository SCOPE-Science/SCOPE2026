---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

A=(a,b,d), B=(e,f,g) have Jordan product (ae,(b(e+g)+f(a+d))/2,dg), and square (x,y,z)²=(x²,y(x+z),z²). For Q={1,3,8,120}, seeds (b,r)=(18,6),(10,10), the nine distinct nonzero matrices consist of two symmetric four-element wings (a,2b,0),(0,2b,a) and center (0,2b,0). For six same-wing pairs, ac+1 is square with roots h∈{2,3,5,11,19,31}; direct exact divisibility of b(a+c)+r by h±1 gives integral square root. For cross-wing/center pairs, the target (1,b(a+c)+r,1) or (1,ba+r,1) squares because b,r are even. Every Jordan product is nonzero. Scaling offdiagonal by nonzero t and diagonal by 2 where required preserves all squares and gives N=(1,6t,1),(1,10t,1),(4,12t,4),(4,20t,4) for all nonzero integer t. The external Theorem 4.2 gives ≤9, so exactly 9; union of r divisible by 6 or 10 among evens gives relative 1/3+1/5−1/15=7/15 (and analogous 12 or 20 among multiples 4). Independent exhaustive enumeration of all 36 pair-squares and nondegeneracy for twelve signed scalings (432 verified pairs) agreed. Finite check corroborates the explicitly uniform scaling proof and published upper bound.

## originality

PASS

The original published Theorem4.2 proves the uniform nine upper bound and Proposition4.4 leaves precisely the 8-or-9 maximum for equal-diagonal nonzero offdiagonal parameters. The new two explicit nine-tuples settle positive-density infinite congruence families inside those open cases. The original known N=I matrix quadruple Q is credited; the integer divisibility seeds and nonzero off-diagonal lifts are the additional findings.

## value

PASS

Settling the top alternative of a published sharp 8-or-9 extremal problem for infinitely many nonzero offdiagonal parameters of positive relative density is independently useful. Exact integer square-root divisibilities and scaling are mathematically substantive constructions, not known-table recomputation or arbitrary isolated numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
