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

For constant-control six-compartment compliant/noncompliant SIR equations in Ngo–Parkinson–Wang version 3, summing all six equations forces K=b/delta and summing the three noncompliant equations fixes N*=u uniquely as positive root of q u²+(nu+delta-qK)u-xi b=0. With m=q u fixed, the susceptible 2x2 matrix M(lambda) is an irreducible nonsingular M-matrix with strictly positive inverse; S(lambda),S*(lambda) decrease strictly because d/dlambda=-M^-1 diag(1-alpha,1)(S,S*). The infected transfer matrix V^-1 is strictly positive and self-consistency becomes F(lambda)=beta(P S(lambda)+Q S*(lambda))/J=1, where F(0)=Rinv and F tends to zero. Thus a unique positive scalar lambda (hence positive all six compartments) exists exactly when Rinv>1. Clearing denominator gives the specified quadratic with leading coefficient J(1-alpha)>0. The published printed ratio is demonstrably different from actual next-generation Rinv but is not a new finding. Independent Fraction calculation verified every six-equation residual of the exact (1900/3901,379/85822,366/42911,3775/7802,340/42911,353/42911) witness, lambda=1/25. All-parameter claim relies on M-matrix/monotonic proof, not samples.

## originality

PASS

Ngo–Parkinson–Wang arXiv:2509.09075v3 defines the exact constant-control ODE model and focuses on disease-free states, printed reproduction quotient, and optimal controls; in inspected Sections 2 and Appendix the complete positive-endemic count and quadratic reduction are not proved. Published Resultary SCOPE-the-printed-noncompliance-reproduction-ratio-can-reverse-disease--dc20b8be6a8d already identifies the printed/true reproduction discrepancy and a DFE instability reversal, which are categorically excluded from novelty here. Generic next-generation theory alone does not provide uniqueness of positive equilibria under this nonlinear behavior feedback. The complete model-specific positive-equilibrium count is the retained contribution.

## value

PASS

A complete if-and-only-if and uniqueness theorem for endemic equilibria of a specific six-dimensional model under all stated interior parameters resolves an explicit natural model-analysis gap. The exact quadratic and monotonic feedback eliminate alleged higher-degree ambiguity and prevent interpreting the misprinted threshold as the bifurcation condition. It does not claim stability or policy validity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
