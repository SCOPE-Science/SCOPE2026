---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Let u=Ab,v=b. Gaussian regression gives Sv=αSu+√(||b||²-α²||Ab||²)Z with Z independent standard Gaussian. Then (Su)^T(Sv)/||Su||²=α+β N/R where R²∼χ²_s, N∼N(0,1) independent, so H^{-1}=α+(β/√s) t_s. The reciprocal denominator has strictly positive finite density at zero for β>0; hence P(|H|>z)∼(2√s/β) f_t(-√s α/β)/z and E|H|^p finite iff 0<p<1, with negative risk F_t(-√s α/β). Using weights λ_i²b_i²/||Ab||² on q_i=1/λ_i∈[1/L,1/μ], α=Eq, β²=Var q; the Bhatia–Davis bound gives β²/α²≤(L-μ)²/(4μL), attained for two endpoint eigenvalues and b∝(√(L/μ),1). Thus optimal negative risk is F_t(-2√(s μL)/(L-μ)). Eigenvector β=0 exception handled. Independent Gaussian simulations at four spectral/row settings matched Student probabilities. No simulation is used to infer infinite moments.

## originality

PASS

Güttel–Liu–Nyman (arXiv:2607.10354) Section 5.3 defines the same sketched harmonic generalized pencil and proves positive-real spectral guarantees under good sketch embeddings. Its fully inspected methods do not present the unconditional Gaussian reciprocal Student distribution, infinite-moment threshold, or sharp optimal negative event. Classical Gaussian regression, Student ratios, and bounded-support variance inequality are acknowledged tools, not claimed new. Best-of-knowledge new in specific sketched harmonic application.

## value

PASS

Quantifies precise rare instability of the original sketched harmonic one-dimensional pencil despite positive-definite A; gives exact unconditional heavy-tail exponent, divergence of absolute expectation and a dimension-free sharp condition-number-dependent negative Ritz probability with explicit extremizer, directly relevant to interpreting embedding-conditioning assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
