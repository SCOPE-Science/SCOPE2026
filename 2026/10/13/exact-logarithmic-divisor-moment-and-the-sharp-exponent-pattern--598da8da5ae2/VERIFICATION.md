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
# Verification

The proof is symbolic. Its critical steps are: (1) the unique divisor parametrization by independent exponent coordinates; (2) the exact mean and variance of a uniform integer on \(\{0,\ldots,a\}\); (3) Cauchy--Schwarz with weights \(a_i(a_i+2)\) and \(a_i/(a_i+2)\); (4) the equality condition \((a_i+2)\log p_i=\text{constant}\); and (5) a classical prime-in-doubling-interval construction showing asymptotic sharpness at fixed exponent pattern.

The bundled `verify.py` directly checks every integer \(2\le n\le20000\). It compares the direct divisor sum \(\sum_{d\mid n}(\log d)^2\) with the factorization formula, verifies the exponent-pattern lower bound, verifies equality for all prime powers in the range, verifies strictness for every tested integer having at least two distinct prime factors, and checks the closed squarefree coefficient for support sizes \(1\) through \(8\).

The recorded output is in `verification_output.txt`. Floating-point enumeration is regression evidence only and does not certify the infinite theorem or the sharpness limit.
