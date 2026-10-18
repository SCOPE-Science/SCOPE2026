---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Let T_j be the d=p^j term and p odd, r>=2, p∤a. For j=r, v_p(T_r)=3r-2. For 1<=j<r, m=r-j, Legendre gives v_p(T_j)-(3r-2)=j(p^m-1)+(p^m-1)/(p-1)-3m, strictly positive except (p,r,j)=(3,2,1). For j=0, v_p(T_0)=(p^r-1)/(p-1), strictly greater than 3r-2 except (p,r)=(3,2). In the exception, (T_0,T_1,T_2)/81 reduces to (a,2a,a) mod 3, sum a nonzero. Hence v_p(S)=3r-2, no hidden cancellation. Recomputed integer defining sums for 30 unit cases over p=3,5,7,11 and r=2,3, confirming but not proving the unrestricted valuation.

## originality

PASS

Published Moser-Moser congruence ensures only divisibility by n^2; on p^r it yields 2r, while this exact odd-p-adic valuation 3r-2 and exceptional p=3,r=2 cancellation are not stated in the primary published account reviewed.

## value

PASS

Determines a natural exact local divisibility invariant of the classical Moser–Moser divisor sum uniformly on all odd prime powers beyond r=1, replacing an order-only bound by a sharp exponent. The singular 3-adic cancellation and r-dependence supply a reusable arithmetic refinement, rather than a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
