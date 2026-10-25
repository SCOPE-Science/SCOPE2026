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

For b*Delta(a,b) nonzero over algebraic closure F17, y²=x Q(x³), Q=t³+t²+at+b, has genus4. The Cartier operator has a sparse 4x4 matrix with independent blocks: scalar B=[t^8]Q^8 and two disjoint vector blocks (A,E) and (C,D), so rank=1_{B!=0}+1_{(A,E)!=0}+1_{(C,D)!=0}. Independently expanded Q^8 over F17 and checked A=b^6(8b-6a²), E=-2a²+5ab+8a-2b+5. Substituting b=5a² solves (A,E)=0 at three points (4,12),(10,7),(13,12), which have nonzero discriminant. Exact symbolic resultant Res_b(C,D)=3a³(a-6)^12(a+4)(a+7)(a-4) and specialized gcds at a=0,6,13,10,4 rule out other common zeros even in algebraic closure: (0,0) excludes b=0, (6,12) singular. Evaluating B yields rank0 at (13,12) -> a=4, rank1 at other two -> a=3, rank2 when B=0 elsewhere -> a=2, rank3 otherwise -> a=1. The resultant and gcd computations, not a prime-field census, justify completeness over all algebraic extensions.

## originality

PASS

Best-of-knowledge mathematical implication assessment, comparing identical objects/parameters and stronger results rather than title similarity; known preliminary counts, matrix formulas and examples are credited, not treated as new.

## value

PASS

Completing every a-number stratum for a natural two-parameter genus-four family with order-six automorphism is a meaningful geometric classification. The exact two rank-one points, unique rank-zero point and rank-two divisor distinguish the superspecial locus from intermediate nonordinary Jacobians; those precise exceptions could be useful in moduli and arithmetic stratification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
