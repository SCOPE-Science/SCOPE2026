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
# Verification record

Run `python semigroup_checker.py` using Python 3; it requires only the standard library. The program passed, terminating with `VERIFY_OK: finite semigroup, Apery, gap and type arithmetic checks` for primes \(5,7,11,13,17\) and exponents \(2,3\), plus \((5,4)\) and \((7,4)\). Its shortest-path algorithm computes Apéry residues independently of the proposed closed formula, enumerates all gaps below the conductor, and checks pseudo-Frobenius values and all Riemann–Roch dimensions in the tested finite ranges.

The infinite theorem is deduced from the algebraic curve's quotient equation, tame genus calculation, local valuations and Weierstrass gap count in RESULT.md. Numerical tests alone do not certify any untested characteristic or exponent. There has been no independent audit.
