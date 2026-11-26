---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For residuals P=X−x, Q=Y−y, differentiate P(f(y),y)=Q(g(y),y)=0 to get det(I−J)=det D(P,Q)=P_x Q_x(f′−g′). At an interior equilibrium P_x=−rx, Q_x=y/x, giving the factor −ry. H(0+)=1−1/(βb)<0 and every positive-y zero is an interior equilibrium because g(y)>0. At the first such zero H′≥0, with strict inequality if transverse. Hence p(1)=det(I−J)≤0 excludes strict Schur stability; at equality 1 is a multiplier, while strict negativity puts a real characteristic root above 1. The stated rx≤2 saddle test additionally requires transversality: writing A=βbxS(1+2cy)>0 and B=by e^{r(1−x)}S(1+2cy)>0, p(−1)=(2−rx)(1+A)+B>0, locating the other root strictly between −1 and 1. The displayed rx≤2 is a sufficient cutoff, not an iff threshold; no nonlinear conclusion follows just from H′=0. A fresh bisection/Jacobian reproduction (lower_equilibrium_reproduction.py with its output in the private numerical evidence; the frozen verification/verify.py was only inspected) agreed with the determinant test and gave multipliers 0.010601260510 and 1.019517400112 at r=1, and −1.994045049924 and 1.019721561378 at r=3, with (β,b,c)=(2,0.49,3). Those bounded checks reproduce the local examples, not a global root count. The analytic statement is conditional on exactly two positive equilibria and does not establish that hypothesis for arbitrary parameters.

## originality

PASS

The planar nullcline determinant identity is general and not itself new. The strongest same-map indexed overlap reports a separate result on instability of a lower equilibrium under the same two-equilibrium assumption, without naming or giving that result. This could refer to the frozen finding itself; it is evidence of overlap in the instability claim, not evidence of a distinct earlier theorem covering the model-specific Jury conclusion including the explicit saddle cutoff. Credit the supported joint refinement for this exact model, not novelty of the determinant technique or proof of priority for the lower-instability observation alone.

## value

PASS

The nullcline slope and a simple parameter cutoff settle a practical gap between counting coexistence equilibria and identifying their local dynamics in a concrete model. The lower unstable multiplier and the additional saddle conclusion supply analytic information beyond the numerical examples, while separating nontransverse and possible repeller cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
