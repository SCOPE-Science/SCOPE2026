---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

After clearing denominators the equation is q(A+B-1)=(A-1)(2B-1) for A=2^a and B=2^b. Since gcd(A+B-1,A-1)=1, the common divisor A+B-1 divides both 2B-1 and 2A-1. Positivity forces A<=B and B<=A, hence A=B and q=A-1. The converse is direct. The finite exact-rational checker is corroborative only.

## originality

PASS

The inspected harmonious/feebly-amicable literature studies the invariant globally, lists examples such as (4,12), and develops abundancy criteria, but targeted searches for Mersenne terminology and the structural slice (2^a,2^b q) found no implication-equivalent classification. Resultary returned the assigned theorem as the exact hit and no broader predecessor. The proof is elementary, but it supplies a complete infinite slice rather than recomputing a known table.

## value

PASS

Powers of two are a canonical support restriction in divisor-sum problems, and the observed Mersenne examples motivate the slice. The theorem completely explains that infinite pattern with an exact converse, rather than reporting isolated computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
