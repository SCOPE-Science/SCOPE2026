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

# Reproducibility and limits

The file `verify.py` is a self-contained Python 3 script using only the standard library. Execute `python verify.py` from the same directory.

The reference execution passed 2,239 finite assertions. For rings of small sizes it checks exact cyclic run-count multiplicities and normalized stationary weights, compares five conditional moments against exhaustive configuration enumeration, and checks **every** finite-state global balance equation with rational rates on a family of fixed-composition rings. For larger sizes it evaluates stable run-count sums and compares the scaled mean and intensity variance with their analytical limits.

For \(\alpha=1.7\), \(\rho=0.37\), \(\lambda=2.5\), the verifier reported:

| \(N\) | \(\mathbb E[C(C-1)]\) | \(\mathbb E[j_N]\) | \(\operatorname{Var}(j_N)/N\) | \(N\mathbb E[B_N]\) |
|---:|---:|---:|---:|---:|
| 500 | 0.0924054103 | 0.6289081223 | 2.6577632717 | 0.1471423732 |
| 2000 | 0.0930309515 | 0.6289770680 | 2.6693752630 | 0.1477854670 |
| 8000 | 0.0931877128 | 0.6289942693 | 2.6722811231 | 0.1479463588 |

The analytical targets are \(\mathbb E[C(C-1)]\to0.09324\), \(\mathbb E[j_N]\to0.629\), \(\operatorname{Var}(j_N)/N\to2.67325\) and \(N\mathbb E[B_N]\to0.148\).

The infinite-size theorem comes from the explicit analytic combinatorics and dominated-convergence proof in `RESULT.md`. Finite enumeration and numerical convergence do not independently certify infinite-size asymptotics. The observable is a one-time conditional jump intensity, not the time-integrated current, temporal covariance or shot noise. Independent audit has not been performed.
