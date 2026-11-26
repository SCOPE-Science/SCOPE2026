---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

I checked the geometry and recovered the arithmetic independently with python3 /workspace/audit_quartic.py. Smoothness can also be checked directly: on e1=0 the constrained partials agree only if all xi solve z^3+e2 z=constant, because the e2-square term has zero derivative. With two distinct values, the value of odd multiplicity is zero, and the patterns (4,1) and (2,3) fail the surface equation. With three distinct values a,b,c, their sum is zero and ab+ac+bc=e2; for multiplicities (3,1,1) this forces a=0 for the triple value, hence b=c, and for (2,2,1) the singleton is zero by e1=0 and the pair values again coincide. One value would give only the zero vector. Thus it is a smooth quartic K3. In a separate F4-to-F16 quadratic-tower implementation I enumerated normalized projective points, finding (20,554), and found all 60 F16-lines from pairs of these points (five distinct zeros force the binary quartic restriction to vanish). Their F4-Frobenius permutes them in 30 transpositions. Direct intersections and exact rational ranks give rank G=20 and rank G(I+P)=rank G(I-P)=10. The published rank-20 span gives the upper bound, and the intersection pairing identifies the two ranks with the two eigenspace dimensions. The two actions on untwisted H2 are therefore +4 and -4 with multiplicity ten each; inverting the permutation for geometric Frobenius has no effect. The 22-dimensional K3 trace formula then gives remaining traces 3 and -23 for F and F squared. Newton's identity gives product 16, hence residual factor X^2-3X+16 and discriminant -55. The H0 and H4 factors complete the stated zeta function in all extensions. No claim is made about other twists or the line complement.

## originality

PASS

The marked surface, smoothness, lines and rank-20 lattice are known. The supported distinct content is the explicit arithmetic Frobenius action and residual quadratic for this marked F4-form. The exact surface zeta is also reproduced in a later Resultary record, where it is expressly antecedent arithmetic rather than the new claim. No earlier independent source of that formula was established in the checked literature.

## value

PASS

This is a distinguished line-maximal characteristic-two K3, with a naturally specified base-field form. The complete polynomial separates the descent of the known divisor-class span from the residual arithmetic and determines every extension count. In particular, the exact ambient zeta is an input for arithmetic calculations on its line complement, as the later complement study explicitly illustrates. The result is not merely a line-orbit recount.

The dated certificate retains the supplied scientific assessment, sources and limitations.
