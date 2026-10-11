---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Antiderivative tests in y and z give the two conditional laws. Their first moments imply E[x]=E[y]=-(3/10)E[z] and E[xy]=E[y^2]=E[z], producing q=(9/100)E[y^2], the exact mean segment and variance parabola. Stationarity of y^2/2 and z^2/2 expands to the two nonnegative squared-speed variance defects; zero of either speed on invariant support propagates to x=y and z=x^2, or to x=-(3/10)z with the unique bounded complete y solution y=x, hence only the two equilibria. Stationarity of yz gives E[yz]=(10E[y^2]-3E[z^2])/7, which rearranges exactly to the 7/13 gap. Equality forces y=z, then tangency gives y=z=0 and x=0. The exact verifier checks the equilibria and all algebraic coefficients.

## originality

PASS

Sprott's full foundational article lists the exact Case K equations, equilibria, Lyapunov data and attractor geometry. A full 2001 statistical study of Sprott flows explicitly analyzes generalized B and N, not K. Resultary searches found analogous moment laws for other systems but no exact K equilibrium-segment/variance-defect theorem. Panchev's 2004 all-Sprott analytical paper remains a named access risk, not negative evidence.

## value

PASS

For a canonical member of Sprott's catalogue, the theorem gives a complete low-order stationary geometry: exact barycenter segment, Bernoulli-type variance parabola, two rigid speed defects and a sharp RMS ordering. The package is a natural recurrent-statistics classification, not a one-off simulation or table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
