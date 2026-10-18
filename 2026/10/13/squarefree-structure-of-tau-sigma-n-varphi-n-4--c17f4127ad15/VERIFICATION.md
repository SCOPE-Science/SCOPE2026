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

The complete squarefree domain splits into n=1, odd prime, n=2, odd composite with at least two odd prime factors, and 2 times at least two odd prime factors, or 2q. The first two exceptional n=1,2 do not have four divisors after sigma+phi; odd primes do. For either composite with at least two odd prime factors, both multiplicative sigma and phi are multiples of 4, their sum exceeds 8, yet the only multiple of 4 with exactly four divisors is 8. For n=2q (q odd prime), sigma+phi=4q+2=2(2q+1), so tau=4 iff 2q+1 is prime. This proves the unbounded iff and bijection without assuming Sophie Germain infinitude. I separately recomputed exact arithmetic through n<=2000; the attached source verifier has a logically stronger but still finite cutoff of 500000, and its output was not treated as a proof.

## originality

PASS

Best-of-knowledge original exact description of the squarefree portion of the OEIS A067350 predicate. Its published sequence and OEIS A065387 supply examples and the two-prime identity, and A097646 notes the Sophie Germain family for a DIFFERENT equation, but the audited iff excludes arbitrary larger squarefree supports using the modulus-four obstruction. Strongest risk is an elementary observation appearing in unindexed comments; no literature absence establishes priority.

## value

PASS

The squarefree part is a canonical and exhaustive infinite arithmetic subclass of a public divisor-count sequence. Its exact classification and bijection with Sophie Germain primes resolve a real structural question and convert its infinitude into a classical open problem, rather than computing another finite prefix. The classification leaves nonsquarefree members untouched.

The dated certificate retains the supplied scientific assessment, sources and limitations.
