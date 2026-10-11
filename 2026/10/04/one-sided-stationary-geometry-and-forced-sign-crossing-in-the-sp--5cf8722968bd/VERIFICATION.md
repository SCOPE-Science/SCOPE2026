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

For every bounded complete trajectory, backward variation of constants in \(\dot y+y=x^2\) gives \(y(t)=\int_0^\infty e^{-s}x(t-s)^2ds\ge0\); equality would force an entire past half-orbit with \(x=y=0\), contradicting boundedness because then \(\dot z=1\). Thus compact invariant support lies in \(y>0\). Generator stationarity applied to arbitrary one-coordinate C1 primitives gives the three conditional expectation laws. Their expectations yield \(E[x]=1/4\), \(E[y]=E[x^2]\), and hence the exact variance defect. Equality forces the unique equilibrium. Finally, if a non-equilibrium invariant measure lived in one closed z-half-space, \(y>0\) and \(\int yz=0\) would force \(z=0\), then invariance forces the equilibrium; periodic sign crossing follows by continuity. The bundled exact-arithmetic checker independently confirms the equilibrium algebra but is not used for the measure-theoretic proof.

## originality

PASS

The same-object Wei--Wang primary paper was inspected at the vector-field definition and explicitly identifies the zero-extension case as Sprott E. Its focus is chaotic behavior and synchronization, not compact invariant-measure conditional laws. Targeted Resultary searches for Sprott E stationarity, conditional expectations, positive-y support and sign crossing returned related stationary identities for other chaotic flows but no prior Sprott-E theorem. The original 1994 Sprott paper and later bifurcation/control literature provide dynamical context but no located implication of the submitted stationary geometry.

## value

PASS

The theorem gives exact invariant-measure constraints for a classical chaotic flow: a strict one-sided support geometry, sharp mean/variance rigidity and unavoidable two-sided recurrence in z. These statements apply to every compact invariant probability measure and immediately constrain every periodic or recurrent compact state, so they are structurally motivated rather than a numerical attractor observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
