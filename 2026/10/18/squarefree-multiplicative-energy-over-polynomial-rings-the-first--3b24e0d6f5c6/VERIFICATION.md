---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Fix prime power q and d≥2. Unique monic U=gcd(A,C), V=A/U, W=C/U, X=B/W=D/V forces deg V=deg W=b and deg U=deg X=a=d-b. Gcd(V,W)=1 and squarefreeness of UV,UW,VX,WX are equivalent to each of U,V,W,X squarefree plus coprimality edges UV,UW,VW,VX,WX; the U-X overlap is allowed. Each of d+1 degree strata starts from q^{2d}. With a and b positive, five distinct edge collisions cost 5/q; each individual degree≥2 variable has a square-linear-factor event costing 1/q. At b=0 only U,X squarefreeness contributes 2/q, at b=d two V,W squarefree plus their mutual coprimality contribute 3/q. In each fixed-d stratum, non-linear irreducibles and pair intersections of distinct linear bad events are O_d(q^-2) uniformly over prime powers, because deg-k prime counts ≤q^k, two independent divisibilities cost q^{-2k}, and two linear bad events impose ≥3 same-prime or ≥4 distinct-prime linear constraints. Summing 2+3+5(d−1)+4(d−2)=9d−8 proves the two-term asymptotic with uniform characteristic error. Exact d=2 strata are (q²−q)², q(q−1)(q−2)² and q(q−1)³; their sum is 3q⁴−10q³+12q²−5q. The d=1 boundary 2q²−q is stated separately. Six local irreducible states (absent; U,X,V,W alone; U and X) yield the exact finite coefficient product. An independently written field-arithmetic checker reproduces direct energy and the parametric strata in 20 cases including GF(4), with all checks passing. Computations corroborate, not prove, the general result.

## originality

PASS

Best-of-knowledge originality survives targeted same-object searches and direct implication checks. The squarefree four-factor second coefficient and six-state prime factor are not delivered by the inspected unrestricted equal-product statement or the 2018 coprimality-graph theorem. This is qualified: complete current full text of the closest 2026 paper was unavailable, and a general Euler-product identity could implicitly contain the coefficient.

## value

PASS

Fixed-degree divisor energy of monic polynomials is a natural object in arithmetic statistics. Restricting each factor to the large squarefree subensemble is mathematically motivated, not an arbitrary q-slice: it exposes the explicit 8(d−1) first-order collision penalty invisible in the unrestricted total. The six-state local Euler product characterizes the exact model and the polynomial identity in degree two provides a useful independent benchmark. The result is modest and first-order, with a classical sieve proof, but its precise previously-unestablished natural restricted invariant and its boundary behavior are sufficiently substantive without a claimed deep downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
