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

Holdener--Holdener give that \(N\) is an odd square, \(q\) is its least prime factor, and any other prime \(r\) is at least \(q+1\). Assuming two-prime support, Euler-factor bounds force \(r<q+3+4/(q-2)\), leaving \(r=q+2\) except the \((3,7)\) case. When \(r=q+2\), the exact abundancy identity forces the two divisor sums to be pure powers of the opposite prime; modulo \(r\) this gives incompatible congruences differing by a factor four. For \((3,7)\), the order of 3 modulo 7 gives the contradiction. The verifier checks the cutoff, special order and a large finite regression grid.

## originality

PASS

The full Holdener--Holdener paper was inspected: Proposition 23 stops at at least two distinct prime factors, and the conclusion explicitly leaves the prime quasi-friendly-divisor question open. The audited proof eliminates the remaining two-prime-support case. Ryan's 2002 full text was not accessible and remains an explicit residual risk.

## value

PASS

Eliminating the entire two-prime-support branch is a natural structural advance toward the source's explicit existence question for prime quasi-friendly divisors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
