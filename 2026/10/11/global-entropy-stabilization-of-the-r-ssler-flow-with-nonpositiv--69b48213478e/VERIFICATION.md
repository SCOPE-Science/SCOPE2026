---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Independently verified the translated vector field and the exact derivative of V=[(x-ap)^2+(y+p)^2]/2+z-p-p log(z/p): Vprime=a(y+p)^2-(c-ap)(z-p)^2/z under ap^2-cp+b=0. For a<=0 the equilibrium polynomial is strictly decreasing on p>=0, hence unique p>0 and c-ap>0. z solves a positive integrating-factor equation, so z0>=0 enters or remains in z>0. Properness of V on z>0 (blow-up for z→0+, z→infinity, and x/y infinity) gives global existence. LaSalle zero-derivative invariant set is E: at a=0 derivative vanishes on z=p but zdot=p*x enforces x=0 then xdot=-y-p forces y=-p, so equality boundary is handled. Integrating Vprime yields exact finite initial budget as t→∞; compact two-sided invariant K can have max V only at E by backward recurrence, and a stationary measure must be supported on E by integrating derivative and invariance.

## originality

PASS

Original Rössler (1976) full two-page paper treats the standard positive-feedback chaotic parameters, and later inspected equilibrium bifurcation and harmonic-balance studies predominantly assume positive a. Related indexed Rössler invariant-measure constraints explicitly restrict to positive-parameter regimes and do not imply this closed a<=0 all-initial-state global theorem. Exact entropy cancellation and boundary a=0 rigidity appear not to be mathematically covered by inspected sources; older unindexed Lyapunov arguments remain a priority risk.

## value

PASS

The nonpositive feedback half-space including a=0 is a natural damping boundary of one of the best studied chaotic ODEs. The exact nonlinear logarithmic energy and global basin classification eliminate all nontrivial compact recurrent dynamics and give an energy budget for every initial state, a meaningful structural contrast to classical positive-a chaos.

The dated certificate retains the supplied scientific assessment, sources and limitations.
