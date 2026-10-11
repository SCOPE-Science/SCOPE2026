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

The two conditional laws follow from generator identities for arbitrary antiderivatives of \(x\) and \(z\). Independently, setting \(d=y-x\) and \(F=xd-(c-a)x^2/(2a)\), direct symbolic differentiation gives \(LF=a d^2+(\rho-z)x^2\). Integrating under an invariant measure yields the exact defect identity. Equality forces \(d=0\) and \((\rho-z)x^2=0\) in the support; invariance leaves precisely \((0,0,0)\) and \((\pm\sqrt{b\rho},\pm\sqrt{b\rho},\rho)\). Strict excursion and sign-change conclusions then follow from positivity and zero mean of \(d\).

## originality

PASS

The Chen literature inspected at full-text level treats symmetry, dissipativity, equilibrium bifurcations and trajectory geometry. The 2003 trajectory paper proves alternating crossings of two specific Poincare projections, which is related to but does not state the invariant-measure identity, exact defect, or equality characterization. Targeted searches found no same-model stationary-moment theorem.

## value

PASS

The exact defect converts the natural nonzero-equilibrium height \(\rho=2c-a\) into a universal stationary excursion law and identifies every zero-defect invariant measure. This is a substantive structural statement about a canonical chaotic flow, not merely a numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
