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

# Exact proof-bound verifier

Execute `python3 verify.py`. This uses only the Python 3 standard library, integer arithmetic and `fractions.Fraction`. It derives the two finite branches from the independently proved polynomial identity in `RESULT.md` and verifies them without a search cutoff on \(c\) or \(q\).

The program reconstructs \(d!P_d(X)\) in \(\mathbb Z[X]\), performs exact monic division by \(X+d+1\), checks the zero remainder and three independent positive evaluations, and compares the critical value with its exact rational-sum expression. It factors each \(d!\) and generates every divisor. It factors each \(K_d\) by primes through \(d\) and asserts that the residual cofactor is \(1\), then checks each odd exceptional prime by strict monotonicity and binary search. Every branch-(A) candidate is tested with exact integer \(d\)-th roots. Complete stored output is in `verification_output.txt`.

Expected terminal line:

`VERIFY_OK exponent_set=9,11,13,15,17,19,21,23,25 candidate_checks=639114 exact_integer_arithmetic=PASS`

The root routine begins at a proven power-of-two upper bound, applies integer Newton steps, and verifies the final root by exact powers. An auxiliary independent test compared it to a separate arbitrary-precision integer-root implementation on \(2500\) randomized instances. The substantive mathematical completeness comes from the factorial-divisor/exceptional-prime dichotomy, **not** from scanning \(c\) to an arbitrary maximum. The result proves nothing about exponent \(d\ge27\), even exponents or external independent validation.
