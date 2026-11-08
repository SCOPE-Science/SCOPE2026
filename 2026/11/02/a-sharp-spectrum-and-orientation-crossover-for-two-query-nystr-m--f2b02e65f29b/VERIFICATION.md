---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS — In dimension two, derived exact residual R=A−(Au)(Au)^T/(u^TAu)=det(A)(Ju)(Ju)^T/(u^TAu) and conditional Rademacher quadratic variance 4R_12². Gaussian polar/angular integration gives E[x⁴/(t²x²+y²)²]=(2t+1)/(2t³(t+1)²), E[x²y²/D²]=1/[2t(t+1)²], E[y⁴/D²]=(t+2)/[2(t+1)²], hence displayed Nyström and 2-probe Hutchinson variances. Independently SymPy-factorized exact difference and strict derivative of Q(t); numerical unique root t*=1.752931245525 and exact t=2 θ=π/4 example N=29β²/9 versus H=9β²/2 agree. At t=1 H variance 0, N=β²/2. For all d≥3 positive-definite block diag(A2,δI), residual PSD bounded by A yields dominated convergence of variance as δ→0, preserving strict opposite ordering at different orientations but identical eigenvalues. Two counted matrix-vector products per estimator; mixed Gaussian sketch/Rademacher probe is explicitly NOT original all-Gaussian Nyström++.

## originality

PASS

PASS, qualified — Persson–Cortinovis–Kressner Nyström++ already uses Gaussian sketch and randomized correction with high-probability bounds (Algorithm 5, read in full ar5iv text); it uses all-Gaussian probes, not exact one-Gaussian/one-Rademacher two-query design. Gambhir–Stathopoulos–Orginos show SVD deflation can increase trace-estimator variance; this qualitative orientation harm is prior art. Current exact all-orientation 2x2 crossover and same-spectrum positive-definite higher-dimensional perturbation were not identified as an immediate prior consequence, though the algebra uses classical variance identities.

## value

PASS

PASS — Sharp basis-orientation/condition-number decision boundary between two well-defined scalable stochastic trace estimators at equal query budget, demonstrating spectrum alone cannot rank them, extending as strict reversal to all dimensions via a natural positive tail. It is explicitly not a global optimality result for 2x2 where two deterministic coordinate probes give exact trace; the value is in the randomized-estimator comparison and exact phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
