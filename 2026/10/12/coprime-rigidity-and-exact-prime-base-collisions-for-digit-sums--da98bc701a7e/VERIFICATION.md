---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Assume a=gq,c=gr with gcd(q,r)=1 and q>1. Choose m divisible by ord_a(b), n_m=(b^m-1)/a, giving S_b(a n_m)=m(b-1). Let ell=ord_q(b), B=b^ell, write r=hq+s (1<=s<q), and A=s(B-1)/q integer in [1,B-2]. For m=K ell, X_K=s(b^m-1)/q has K equal base-B digits A; hence S_b(X_K)=K S_b(A)<=m(b-1)-K. Subtraction of fixed h borrows through at most bounded low blocks since A>0, and the high h*b^m block stays disjoint, so S_b(c n_m)<=m(b-1)-K+O(1), contradiction as K grows. Interchange a,c to prove equality. For prime p strip valuation powers which append zero digits, giving iff p-free cores equal. Repeated block identity checked on exact bounded instances, but proof is symbolic.

## originality

PASS

Pongsriiam 2021 explicitly raises the unrestricted digit-sum quasi-injectivity question, for which b shifts give immediate collisions. Coprime rigidity and complete prime-base modulo-shift classification are not implications of those trivial collisions or the source’s established quasi-injectivity theorems for other arithmetic functions.

## value

PASS

Resolves a precise nontrivial rigidity remainder after removing unavoidable positional degeneracy from a published open-style multiplier question, uniformly in all bases and completely for prime bases. Repeated-block contradiction is a useful exact finite-state digit argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
