---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For 0<z=lambda*V/r<1, the healthy plant balance gives S+I=K(1-z). The infected-plant and infected-vector balances reconstruct S=K(1-z)/(1+Az), I=AzS, V=rz/lambda, U=(aK/R)(1+Az)/(1-z), with A=r exp(-m tau1)/m and R=a K^2 beta lambda exp(-m tau1-mu tau2)/(m mu). All are strictly positive. The remaining vector equation is exactly Q(z)=0, Q=((1-z)^2-H)H-q h z(1-z)^3 and H=(1+Az)/R+h z(1-z), h=r/(aK lambda), q=mu exp(mu tau2)/b. Independent symbolic reconstruction confirms this elimination without spurious divisions. Q has degree <=4, Q(0)=(R-1)/R^2, Q(1)=-(1+A)^2/R^2. If R>1 the opposite endpoint signs prohibit 4 distinct interior roots of a quartic; if R<=1, U>aK while the positive vector balance forces U<U+V<a(S+I)<aK, contradiction. For the stated positive delays log(2) both survival factors are 1/2, (A,R,h,q)=(20,200,1/250,40), and 10^6 Q=155984 z^4-367168 z^3+262224 z^2-67040 z+4975. Four exact sign-change intervals (1/10,1/5),(3/10,2/5),(3/5,2/3),(1,3/2) imply exactly three distinct physical roots and one nonphysical root, all simple. The implicit-function theorem gives an open parameter-and-delay neighborhood. Symbolic residual verification and rational signs corroborate the proof; no stability or finite-experiment-to-infinity inference.

## originality

PASS

Important partial prior coverage: the unconditional *upper bound* of three positive scalar roots already follows directly from the 2023 published quartic together with its displayed positive constant and linear coefficients by Descartes rule (or from its physical endpoint signs after a coordinate change). That upper bound alone is NOT original. The prior 2016 zero-delay paper anticipates possibly three/five algebraic candidate roots, which is also NOT novel. However, the inspected primary texts do not exhibit any exact, feasible THREE-coexistence parameter vector with both delays strictly positive, four disjoint rational root certificates, and persistence as a nonempty open full-parameter region. This substantive sharpness/attainment witness is the originality-bearing portion of the combined theorem. Related 2020 two-delay virus model replaces Leslie-Gower vector crowding by constant vector influx and does not imply it. Bounded Resultary and literature search found no stronger statement implying the exact feasible positive-delay witness; priority is best-of-knowledge.

## value

PASS

The model is a specifically published delayed plant-vector system whose authors analyzed a unique-branch regime. Whether three fully positive coexistence states are simultaneously feasible, and whether the maximal multiplicity occurs in an open region with BOTH delays nonzero, are natural bifurcation-structure questions. The upper-bound inequality is cheap given prior quartic data, but the exact rational witness resolves the nontrivial feasibility/attainment issue and supplies three distinct simple full-state branches; this is more substantive than a random tiny parameter check. It is a meaningful constructive mathematical example, not a claim to a complete stability or biological phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
