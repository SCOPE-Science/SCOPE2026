---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exact cototient is m=2^(a-1)p^(b-1)(p+1). If b>=2, divide D(m)=2^a p^b by p^(b-2); reducing modulo p forces p|(b-1), since p does not divide 2^(a-1)(p+1). The logarithmic derivative then bounds (a-1+t)/2+(b-1)/p+D(u)/u strictly below 2. It forces a=t=1 and b=p+1; the product rule would give D(2u)=p-1, contradicting the odd parity of u+2D(u). At b=1, cancelling 2^(a-2+t) gives (a-1+t)u+2D(u)=2^(2-t)p. Integrality excludes t>=3; the parity and nonnegativity constraints for each remaining t force a=2. Substitution gives each stated auxiliary equality in both directions, including u=1 at t=2. A squared prime divisor of u would divide D(u) and contradict cD(u)=u-1. The three examples and both bounded lists were reproduced independently; the valuation/parity proof, not the sieve, supplies the unrestricted quantifier.

## originality

PASS

The investigated prior sources cover the equation, examples and auxiliary equations, not the unrestricted two-prime exponent collapse and its prime-constrained iff. This is a bounded best-of-knowledge judgment.

## value

PASS

For a pre-existing arithmetic-derivative equation, an exact natural-support result collapses two unbounded exponents to a single shape n=4p, gives an immediate mod-8 exclusion, and makes the remaining difficulty precise in terms of primary pseudoperfect numbers and an extra primality condition. This is a structural restriction and an iff, not a new numerical table or a claim to have exhausted the prime-constrained families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
