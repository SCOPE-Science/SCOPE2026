---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible checks

`python3 artifacts/verify.py` executes exact integer computations without external dependencies. It enumerates all primes \(p\le31\) and exponents \(a\ge1\) with \(p^a\le150\), and every multiplier \(2\le q\le p^a\). For each of 825 triples it checks the congruence using `math.comb`, the precise valuation via Legendre's factorial formula, and the same normalized unit independently via digit factorials. The captured output is in `artifacts/verification_output.txt`.

## Proof obligations and limits

The finite checks do not establish the universal theorem. Its two nontrivial proof inputs are the base-\(p\) digit-complement identities and the unit-factorial reduction modulo \(p\); both are proved in RESULT.md. Wilson and Legendre are standard classical results. Higher precision modulo \(p^{a+2}\) is not asserted. No independent audit has been performed.
