---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For m=2^a p^b, sigma(m)=(2^(a+1)-1)(1+p+...+p^b). If sigma(m) has only prime factors 2,p with both present, first odd factor must be p^c and second, which is 1 mod p, must be a power of 2; parity makes b odd. If b>=3, writing 1+p+...+p^b=(p+1)(1+p²+...+(p²)^(t-1)) creates a nontrivial odd divisor: an odd divisor of t leads to an odd cyclotomic factor, and if t is a power of 2 then p^(2^(j+1))+1 is 2 mod 8 but greater than two. Hence b=1, p+1=2^s. From 2^(a+1)-1=p^c, even c fails mod 8 and odd c>1 gives a nontrivial odd quotient of two powers of two; thus c=1 and a=s-1. Exponent membership forces s<=A; the converse sigma(2^(s-1)p)=2^s p is immediate. An independent exact divisor-sum enumeration checked p in {3,5,7,11,31,127} and A in {2,3,5,8}.

## originality

PASS

I compared the final biconditional and uniqueness to the SAME-OBJECT Atanassov–Sándor 2023 paper in full, especially the divisor-sum section. It derives factorization, necessary parity and Mersenne-based sufficient examples, but does not establish that all choices force b=c=1; its conclusion identifies remaining sigma cases for further study. The earlier 2020 Set paper supplies definitions alone. Semantic Resultary queries found other two-prime divisor problems, not this singleton fiber. The 2024 Set monograph is a specific residual priority risk.

## value

PASS

The Set(n,sigma) fiber is the object introduced in this exact research program. Proving nonemptiness is equivalent to a sharp Mersenne-prime condition AND that every nonempty fiber has precisely one member closes the natural entire two-prime exponent-one family rather than reporting examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
