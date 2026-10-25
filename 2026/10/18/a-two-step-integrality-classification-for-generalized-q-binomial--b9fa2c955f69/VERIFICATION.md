---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Direct telescoping in Q(q) gives H_{n,k,2k}=[n+1]_{q^k}Q_{n,k}²/[2k]_q, Q=prod_{m=1}^n[k]_{q^m}. For n>=2, isolate denominator 1+q; for n odd extract 1+q^k from [n+1]_{q^k}; for k even extract 1+q from [k]_q. Both branches factor into explicitly nonnegative q-integers. For even n and odd k numerator at q=-1 is k^(n-1), proving genuine simple pole. n=1 reduces to [k]_q. Comparison of gcd(n,2k)|k with nu2(n)<=nu2(k) establishes exact false-negative locus; 30 independent exact symbolic n,k polynomial-or-pole checks passed.

## originality

PASS

The 2008 source explicitly proposes the general gcd criterion and proves j=1 results; the full natural two-step specialization and infinite counterexample family are not supplied by its stated results. This is a correction of a mathematical conjecture, rather than a renaming of the known polynomial ratio.

## value

PASS

Complete all-parameter positive-coefficient classification on the minimal nontrivial natural shifted slice and an infinite obstruction family to a previously stated general criterion are reusable results; exact residue gives mechanism, not a mere single instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
