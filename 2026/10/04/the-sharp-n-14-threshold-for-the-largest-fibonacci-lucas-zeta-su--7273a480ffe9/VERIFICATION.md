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

The finite part is checked by `verify.py` with exact rational arithmetic. For even \(N\) and even \(j\), it evaluates
\[
N\binom{N-1}{j}a_j^X2^{N-j-1}\frac{\lvert B_{N-j}\rvert}{N-j},
\]
which equals the source term magnitude by the exact special-value identity \(\zeta(1-m)=-B_m/m\). It enumerates every admissible even index at \(N=12,14,16,18,20,22,24\), checks uniqueness of the largest value, and records the runner-up and exact gap.

The replay also checks the source weights in equation (46) and the exact rational inequality used in equation (50). The source proof of Proposition 7 was read through its derivation of the limiting weight gap, the total-variation transfer, and the uniform \(N\ge26\) bound. The finite replay is not used to infer an infinite pattern.

Limits: the verification establishes only the stated Fibonacci and Lucas weight sequences and source normalization. It does not test or claim an analogous threshold for the broader recurrence family.
