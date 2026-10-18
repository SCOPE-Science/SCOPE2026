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

# Reproducibility and verification

Run `python3 verify.py` with Python 3's standard library from the directory containing the program. The observed successful output is `VERIFICATION_OK 5485`. No external packages or remote services are needed.

The tests (i) build finite integration matrices and recompute their self-commutators, (ii) compare the matrices with the closed diagonal/off-diagonal formulas for complex and real binomial coefficients, (iii) compare exact rational formulas for their entries, (iv) check scaled cubic coefficients, (v) test remote positive witness vectors and negative-tail dominance in multiple parameter ranges, and (vi) use high-precision Decimal arithmetic to check both critical fourth-order signs and finite positive tent-function witnesses at the lower critical ratio. All tests use the packaged program, not an unspecified external artifact.

Finite tests cannot prove any assertion quantified over all exponents, coefficients, matrix sizes, or infinitely many eigenvalues. The infinite claims depend on the asymptotic expansions, the tail-form identity, the min–max principle and standard trace-class facts established in `RESULT.md`. This check is not an independent audit or a machine-checked formal proof.
