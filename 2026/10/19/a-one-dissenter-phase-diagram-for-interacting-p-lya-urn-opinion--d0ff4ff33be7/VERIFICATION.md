---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At any fixed point unequal majority entries would have oppositely ordered neighbor averages on loopless K_n, contrary to strict monotonicity of their shared map. Setting x=f(y,g) reduces the majority equation to y(y−1)(A−Cy)=0 after positive denominator clearing, with A=h(g+n−2)−(n−1) and C=(g−1)(1−h)(n−2)>0. Hence the interior root is y=A/C, admissible exactly when 0<A<C; the endpoint roots merge at the stated thresholds. Evaluating its odds at y=1/2 and taking endpoint differences give the flip formula and positive width. At each consensus boundary the positive Perron vector of the two-class quotient lifts to the full Jacobian; its determinant at I changes sign at h0 or h1. Tang et al., Theorem 4, includes equality and excludes the two boundary limits in the open window under these model hypotheses. Theorem 3 plus increments bounded by 1/(t+1) forces convergence to one point of the finite fixed set, therefore to the unique interior point almost surely in that window. At that point the derivative of the scalar residual has sign C y(1−y)/D>0, giving det(I−B*)>0; the second quotient eigenvalue is negative and the majority-difference drift eigenvalues are −1−b/(n−1). This proves local stability for continuous time, not convergence of individual binary declarations. Independently inverted the majority equation in odds at 300 rational cases and reproduced the fixed point, window/flip and closed stability determinant exactly (python3 /workspace/branches/reproduce_reviews.py 5); no stochastic assertion is inferred from the sample.

## originality

PASS

Support is for the explicit loopless one-dissenter phase diagram, including the interior frequencies, reversal threshold, width and local stability calculation. Do not credit the general spectral consensus criterion or equilibrium approach. The strongest distinct catalogue match also covers interior uniqueness and deterministic selection as qualitative claims; it does not supply the quantitative one-dissenter solution.

## value

PASS

In this minimal heterogeneous complete-graph model the explicit frequency and flip threshold tell when a privately biased majority nevertheless declares the opposite opinion more often, an effect neither endpoint condition reveals. The nonzero width locates the whole mixed regime, and the drift analysis explains its local stability. These are usable precise predictions, rather than merely applying an existing consensus theorem to a smaller graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
