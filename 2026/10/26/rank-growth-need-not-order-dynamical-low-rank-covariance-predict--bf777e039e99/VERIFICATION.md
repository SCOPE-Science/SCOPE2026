---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The factor equation has S'=U^TQU positive semidefinite, so the positive minimum eigenvalue of S cannot decrease; the Stiefel factor stays compact and S grows at most linearly. For B_r=I-P_r, the exact covariance defect is the initial positive semidefinite defect plus the integral of B_r Q B_r. Independently, in the range graph chart L=Y_BA(Y_AA)^(-1), L'(0)=Q_BA(Y_AA(0))^(-1). Differentiating Y'=Q-B_rQB_r gives D''_11=0, D''_13=-q12*q23/a, and D''_33=2*q23^2/b for D=Y2-Y1. The first derivative and initial form vanish on span(e1,e3). Substituting the stated z gives the coefficient -b*q12^2/(4*a^2) while the e2 form tends to b; smoothness gives both signs throughout a punctured time interval. The rank-one example yields -1/18. In dimension two the rank-two projector is the identity, so the established comparison with the full covariance rules out a counterexample there. A separate graph-chart integration gives z^TDz/t^2=-0.055661185 and -0.055567722 at t=0.01 and 0.001, respectively.

## originality

PASS

The closest indexed records show loss of positivity of numerical outputs. This theorem instead compares two exact continuous trajectories that individually remain positive semidefinite and satisfy the full-covariance bound. The primary DLR sources establish the common equation and algorithms, not this cross-rank obstruction. Pass is bounded by the comparisons below, not a priority guarantee.

## value

PASS

A minimal-dimensional exact counterexample separates comparison with the unprojected covariance from ordering successive modeling ranks. The open coupling condition and rank-one forcing isolate a concrete projector-rotation mechanism and rule out explaining the phenomenon as a time-stepping artifact. It informs when rank hierarchies can be used as ordered covariance approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
