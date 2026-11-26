---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For order (u,v,w), the map on the reciprocal y over three seasons is y↦(y+1+u+uv)/P. It has a unique positive attracting fixed point exactly for P>1; rotating the formula gives the other phases. For P≤1 the map instead drives y to infinity, and each within-period phase does so as well. For P>1, after canceling the mean's common factor (P−1)/3, the oriented mean difference is (b−a)/A−(c−a)/B+(c−b)/C, where A,B,C are the two-factor products for pairs ab,ac,bc respectively. I checked the expanded identity (b−a)BC−(c−a)AC+(c−b)AB=(b−a)(c−a)(c−b)(P−1)Q as an exact polynomial over the integers. Putting back the common factor gives the claimed formula and strictly positive sign. The example for (1/2,2,8) gives difference 36603/271700 by rational arithmetic. All permutations for periods one or two are phase shifts, and the two classes for three distinct rates have the stated strict inequality. In the unbounded-ratio family (1/t,t,t³), the leading reciprocal denominator for (a,b,c) is 1/(2+1/t) and for (a,c,b) is 1/(2+t), with the remaining terms O(t^−3) and O(t^−2), respectively. Their quotient is asymptotic to t/2.

## originality

PASS

Existing work already shows that three-season order can matter, and gives general periodic mean formulas. The supported distinct result is the strict ordering of the two growth-rate permutation classes with a fixed denominator, its exact positive gap and its unbounded relative advantage; neither a bare order effect nor the mean formula alone is new.

## value

PASS

At the shortest period permitting a noncyclic reordering, the persistence threshold is order-invariant but the positive arithmetic mean has a universal strict ranking and can change by an unbounded factor. This separates viability from abundance in a naturally parameterized model, rather than merely illustrating order dependence with a chosen numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
