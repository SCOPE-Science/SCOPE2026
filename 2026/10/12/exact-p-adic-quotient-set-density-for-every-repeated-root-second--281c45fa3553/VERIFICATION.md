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

# Verification of repeated-root quotient-set density

## Symbolic argument
The proof uses the exact recurrence identity, the ultrametric valuation rule, density of positive integers in \(\mathbb Z_p\), and Euler's theorem modulo prime powers. It covers all integers \(a,x_0,x_1\), all primes \(p\), and every target in \(\mathbb Q_p\), including the exceptional zero and unit-limit targets. The finite checks below are supplemental.

## Replayable checks
Run `python3 verify.py` alongside this file. The command's recorded terminal output is in `verification.out`; it should end with `VERIFY_OK`. The script checks \(891\) integer parameter triples through index \(30\), \(460\) valuation-rigidity cases, and \(23\) constructive four-digit \(p\)-adic approximations using exact fractions.

## Limits
The verifier does not enumerate infinitely many indices, every prime, every target, or all precision levels. Infinite correctness rests on the proof in `RESULT.md`, not on program output. The originality comparison is literature-limited; independent audit is not performed.
