---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: Over the PID Fq[T], factor each nonzero rank-one matrix uniquely up to q−1 nonzero scalars as M=g u v^T with g monic content and both u,v primitive. Height degree adds exactly. Monic polynomial content contributes (1−qwz)^−1; primitive k-vector series is (q^k−1)(1−qz)/(1−q^k z). Multiplication yields exact bivariate rational generating function; dominant simple/double pole yields the geometric law and square-vs-rectangular growth transition. Independently enumerated every coefficient array of degree ≤1 for (q,m,n)=(2,2,2),(2,2,3),(3,2,2), including polynomial minors and gcd, agreeing with every joint cell.

## originality

PASS

PASS best of knowledge: Afifurrahman 2026 Theorem 2.1 supplies rank-one 2×2 total bounded-degree enumeration; that special case is explicitly credited. The actual new statement refines to Smith-content joint distribution for all rectangular m,n with limiting law; searches of Segre height-zeta and Resultary did not find a theorem implying its exact coefficients.

## value

PASS

PASS: Height and invariant-factor content are intrinsic natural parameters in polynomial-matrix arithmetic. Their exact joint count and limit law provide reference enumerations for rank-one polynomial matrices beyond the previously known unweighted 2×2 count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
