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

Pinned RESULT.md contains full dimensional reduction: M(s)=[[1-s^2/2,s],[-s(1-s^2/4),1-s^2/2]] with determinant 1. Independent symbolic SymPy multiplication verified trace(F)-2=(x+y)^2(xy-4)/4 and trace(F)+2=(x(x+y)-4)(y(x+y)-4)/4 for F=M(y)M(x). For a real determinant-one 2x2 matrix, |trace|<2 is power bounded; |trace|>2 yields hyperbolicity. At trace=2 xy=4, F12=-(x+y) nonzero, hence defective. At trace=-2, F=-I only if y=x and x^2=2 by upper-right/diagonal entries, otherwise defective. Therefore sole parabolic stable point is x=y=sqrt(2). Computed exact witness traces: (6/5,8/5) gives -1298/625 despite both steps stable, and (3,6/5) gives 59/250 despite first step hyperbolic. All positive x,y domain only; no implication to nonlinear/adaptive problems.

## originality

PASS

Skeel 1993 already proves variable timesteps may destabilize leapfrog/Verlet and Richardson–Finn 2011 analyze periodic parametric-resonance mechanisms, so general warning is NOT new. Inspected literature does not give exact global velocity-Verlet strictly alternating two-step 2-parameter power-bounded region, the exceptional -I point, and reciprocal hyperbolic-step rescue. Skeel primary original full paper remained inaccessible after lawful OA/arXiv attempts and Oxford authorized tool returned vpn_disconnected; record this explicit equivalence risk, not automatic FAIL. Published Resultary query on alternating Verlet/oscillator phase diagram retrieved other oscillators/integrators, not this exact map.

## value

PASS

Alternating-step stability matters in symplectic integration where each step may be individually stable or not; exact spectral inequalities and parabolic Jordan exceptions offer actionable sharp boundaries and a counterintuitive stable product of individually unstable stages. This is more than a routine formula substitution because it classifies every positive two-step pair including boundary behavior and demonstrates two opposite regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
