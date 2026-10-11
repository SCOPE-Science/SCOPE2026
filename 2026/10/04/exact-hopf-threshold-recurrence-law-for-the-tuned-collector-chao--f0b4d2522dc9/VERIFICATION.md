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

With \(d=1-M^2\), \(q=y-Mz\), and the submitted storage function \(H\), direct differentiation from the printed flow gives exactly \(\dot H=((\beta-MY)/(MY^2))z^2+(\alpha/(MY^4))z^4\). An independent symbolic differentiation in this audit reproduced that identity. For \(\beta\le MY\), the displayed \(H\) is positive definite and radially unbounded, and LaSalle's largest invariant subset of \(z=0\) is only the origin, proving global asymptotic stability including the nonhyperbolic boundary. At \(\beta=MY\) the characteristic polynomial factors as stated. For compact invariant measures, integrating \(\dot H\) gives the exact moment ratio; Cauchy-Schwarz and support domination give the two bounds, and the equality cases are excluded by invariance of a hypothetical nonzero constant-|z| trajectory.

## originality

PASS

The full primary article was read: it derives the same admittance model, gives the equilibrium, characteristic polynomial, divergence and numerical chaotic parameter set, but does not state the Lyapunov storage identity, the global stability theorem through the Hopf boundary, or the invariant-measure fourth/second moment law. Focused Resultary searches returned the submitted record and other different-vector-field recurrence laws, not a prior same-system theorem.

## value

PASS

The theorem turns the source's local Hopf surface into a global recurrence boundary and gives an exact stationary amplitude law on the supercritical side. That connects local bifurcation, global stability and recurrent statistics for a published physical oscillator and yields a sharp, experimentally interpretable RMS/support constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
