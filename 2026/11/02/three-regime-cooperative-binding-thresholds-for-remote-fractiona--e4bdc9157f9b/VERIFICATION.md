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

# Mathematical verification record

The proof is analytical. Its critical steps are (1) the sine-transform Gram representation of the zero-energy resolvent and a dense-range finite-rank quadratic-form factorization, (2) the integrable-kernel Riemann–Lebesgue limit for \(\alpha<1/2\), (3) the \(\theta^{-1}\) cosine-difference and bounded-remainder split for \(\alpha=1/2\), (4) dominated convergence for \(1/2<\alpha<3/2\), and (5) two-by-two eigenvalue/determinant analysis for cooperative binding. The Green representation and the applicable subcriticality range are independently supported by Gerhat–Krejčiřík–Štampach (2023), arXiv:2307.09919.

The companion `CHECKER.py` was executed successfully with Python 3, `mpmath` and `numpy`. Its printed status was `PASS 35 finite integral, spectral-scaling, and cooperative-binding assertions`; the tested fractional-order \(\alpha=3/4\) pair had normalized limit correlation approximately \(0.36331963264492856\) and coupled largest spectral eigenvalue approximately \(1.181659816322464\), while both individual diagonal eigenvalues were below one. The checker obtains finite Green values from exact gamma/digamma expressions and compares several of them with independent quadrature. It includes the identity \(G_1(m,n)=\min(m,n)\) and verifies the three rescaling regimes at selected parameters.

Finite tests are not an exhaustive or infinite proof. The asymptotic conclusions depend on the explicit dominated-convergence and oscillatory-integral bounds in `RESULT.md`. Numerical evaluation at the exact limiting threshold cannot decide the sign of a finite-parameter difference. Neither a formal theorem prover nor independent external validation has been used.
