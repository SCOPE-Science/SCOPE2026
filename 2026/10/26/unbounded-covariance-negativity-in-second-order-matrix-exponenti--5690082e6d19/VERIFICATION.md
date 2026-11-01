---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Specialized the actual source METD1 eq(7), METD2 eq(9), and METD2RK constant-forcing correction: K1_ij=f(d_i), K2_ij=f(d_i)+(d_i-d_j)g(d_i) with [Σ,A]=ΣA−AΣ. Exact solution is Gram(e^{-at},e^{-bt}) on [0,1], positive definite for a≠b. Strict decrease of f from its integral makes det sym(K1)=−(f(a)−f(b))²/4<0. sym(K2)_12=[f(a)+f(b)+(a−b)(g(a)−g(b))]/2, and dividing by a gives limit [[0,−g(b)/2],[−g(b)/2,0]] with g(b)>0. Continuity of real symmetric eigenvalues yields the claimed diverging negative slope. Independent finite tests rechecked METD determinant for five parameter pairs, stiffness slopes at a=100,1000,10000 and endpoint a=10,b=1; source tree blob SHA was independently reconstructed. Bounded tests corroborate but do not prove all a,b or the asymptotic.

## originality

PASS

Best-of-knowledge original quantified non-preservation of the actual published full-matrix METD algorithms, beyond familiar exact Lyapunov positivity or convergence-order statements. Closest primary algorithm paper examined at its equations; alternatives are distinct maps; no observed theorem entails both METD1 universal determinant and METD2 unbounded negative spectral slope. General unpublished equivalent matrix-positivity results remain a risk.

## value

PASS

Strong structure loss on a minimal 2-mode PSD rank-one Lyapunov source is scientifically motivated for covariance integration. The unbounded negative eigenvalue survives symmetrization while the exact Gram covariance remains bounded, a quantitative obstruction distinct from the trivial observation that a raw output may be nonsymmetric or that a method is not exactly congruence-preserving. The sharp slope permits stiffness-sensitive benchmarking and distinguishes method order from covariance validity. No claim to all integrators or fixed-operator h→0 instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
