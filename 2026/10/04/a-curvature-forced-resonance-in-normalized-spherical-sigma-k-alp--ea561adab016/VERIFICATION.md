---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a centered geodesic sphere, all principal curvatures equal \(\cot\rho\), so the flow reduces exactly to \(\rho'=-\gamma_0\rho^{a+1}A(\rho)\) with \(A(\rho)=(\rho\cot\rho)^{k\alpha}=1-(k\alpha/3)\rho^2+O(\rho^4)\). With \(x=\rho^{-a}\), \(L=1+a\gamma_0t\), and \(E=x-L\), one has \(dE/dL=A(\rho)-1\), \(x/L\to1\), and hence \(\rho^2=L^{-2/a}(1+o(1))\). Integrating gives the power, logarithmic, and convergent-tail regimes exactly at \(a=2\); expanding \(y=(1+E/L)^{-1/a}\) gives the stated constants. In the resonant case the factor \(\log L=2\log\lambda\) exactly cancels \(1/a=1/2\). The subcritical integral has local integrand \(-(k\alpha/3)r^{1-a}+O(r^{3-a})\), so it converges precisely for \(a<2\).

## originality

PASS

The primary source proves normalized convergence for general convex hypersurfaces and explicitly retains the spherical ambient-curvature contribution only at big-O order in its constant-mode argument. It does not state a nonzero round-family coefficient, the threshold \(a=2\), or the logarithmic resonance. Resultary returned the current record as the only exact-topic finding; the hyperbolic companion concerns a different ambient radial factor.

## value

PASS

The round invariant family is the canonical calibration for any uniform convergence-rate theorem for the full geometric flow. The nonzero \(\lambda^{-2}\) coefficient above threshold and the logarithmic resonance at threshold impose sharp obstructions on possible uniform rates, making this a motivated structural boundary result rather than an arbitrary parameter calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
