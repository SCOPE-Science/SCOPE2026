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

Direct differentiation of \(H=x^2+y^2+z^2+w^2\) along the printed vector field cancels identically, and the divergence is identically zero. With \(a,b\ne0\), the origin is the only equilibrium, so every nonzero invariant sphere is compact and contains no equilibrium. The flow direction therefore supplies one zero Lyapunov exponent. Conservation gives \(dH_{\phi_t(p)}D\phi_t(p)=dH_p\); because \(\|dH\|=2R\) on the sphere, the one-dimensional normal quotient has a second zero exponent. Liouville's formula gives zero total exponent sum, leaving an opposite pair \(\lambda,-\lambda\). Independent symbolic reconstruction verified both exact cancellations and the source example's energy.

## originality

PASS

The introducing paper gives the exact ODE, notes zero divergence, reports a four-number spectrum with two positive values, and calls the model conservative hyperchaotic. It does not state the quadratic first integral, invariant-sphere foliation, or the forced two-neutral spectrum. Targeted Resultary searches found the submitted record and analogous first-integral corrections for different systems but no earlier result for the Lu--Yu--Zhu equations. General first-integral and Liouville facts do not cover the source-specific conclusion until the conserved quadratic is identified.

## value

PASS

The invariant changes the exact geometry from an ambient four-dimensional conservative flow to dynamics confined to three-spheres and rules out the paper's defining two-positive-exponent hyperchaos criterion. Because the source uses that classification to motivate an encryption construction, the correction is mathematically and interpretively substantive despite the short algebraic discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
