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

For q=2^m >=4, generator columns E_a=(1,a,a^2,a^3)^T and T_a=(0,1,0,a^2)^T have rank four. Projecting to first/third rows excludes <=2 circuits and all 3-/4-circuits involving fewer than three evaluation columns except derivative triples. Three distinct value columns and T_d have determinant zero iff d^2=ab+ac+bc; Hasse derivative of P(X)=(X-a)(X-b)(X-c) gives this unique d distinct from a,b,c, and proper subtriples are independent. Fix d and substitute u=(a-d)^(-1): u+v+w=0 proves PG(m-1,2) Steiner lines, (q-1)(q-2)/6 pure-value 3-helper repairs of D_d, binom(q-1,2) two-helper D_d repairs and same number of 3-helper V_a repairs. For any V_a, projection forces >=2 other V coordinates in every arbitrarily large helper set, giving <=(q-2)/2 disjoint sets; explicit primitive-power disjoint pairs and d_i=a+sqrt(g^(4i+1)) attain it since gcd(4,q-1)=1. Nonzero column multipliers do not change circuits. Finite q=4,8,16 checks are supporting tests, not an all-field proof.

## originality

PASS

The code construction and Hasse-jet interpretation are not new; inspected NRT MDS/duality results and a general univariate multiplicity dual description do not state the exact ordinary-Hamming small-circuit supports, projective Steiner line incidences, or sharp unrestricted disjoint value-coordinate availability. An older finite-geometry equivalence is a real priority risk.

## value

PASS

Complete small-circuit classification, explicit locality/availability and a geometric Steiner design interpretation are natural structural invariants relevant to local repair; disjoint-availability optimum for arbitrary (not merely minimal) helper sets is nontrivial and not a parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
