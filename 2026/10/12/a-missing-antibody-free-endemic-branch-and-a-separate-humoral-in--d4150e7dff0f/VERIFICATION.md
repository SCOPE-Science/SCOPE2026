---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: The source Eq.(1) was checked directly on the main mathematical pages of the 30-page primary paper. On A=0, the virus equation yields V=kI/dV; the CTL equation yields strictly increasing I(E)=(dE E−s)(h1+E)/(cE), E>s/dE, with I′=(dE+s h1/E²)/c>0. The infected-cell equilibrium determines S=D(E)(dV+σkI)/(βk), and the susceptible balance gives strictly increasing Fβ(E)=D(E)[dS dV/(βk)+(1+dSσ/β)I(E)]=λ. This has precisely one solution iff β>βc=dS dV(dI+p s/dE)/(kλ). Symbolic differentiation independently checked all five reduced balance equations and the C formula. Transverse antibody eigenvalue ωV/h2−dA crosses zero only at IA=dA dV h2/(ωk), giving finite βA iff λ>DA IA, with exact stated βA>βc. It does not establish full local stability, global attractivity, or a transcritical exchange.

## originality

PASS

The 2026 initiating six-ODE model explicitly enumerates only the disease-free state and an A>0 endemic state, while the exact invariant antibody-free endemic branch with its separate humoral threshold is absent. General virus-immune invasion thresholds predate this, but their formulas and invariant faces do not subsume the precise source-specific scalar equation and bifurcation parameter.

## value

PASS

PASS: A hidden endemic equilibrium changes the equilibrium census of a concrete published six-compartment infection model, and the mathematically different thresholds for viral infection and humoral invasion have direct dynamical interpretation. The explicit monotone reduction provides exact uniqueness and distinguishes local transverse growth from general stability, correcting a source-specific claim without overclaiming disease dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
