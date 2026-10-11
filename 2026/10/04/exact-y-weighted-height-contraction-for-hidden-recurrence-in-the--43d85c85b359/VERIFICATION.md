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

On every bounded complete support trajectory, variation of constants gives y(t)=integral_{-infinity}^t exp(-(t-u))x(u)^2 du. Equality y=0 would force x=0 on an entire backward half-orbit and then zdot=1 there, contradicting bounded completeness, so y>0. Generator invariance with arbitrary antiderivative test functions of x gives E[yz|x]=-a. The same argument in z and y yields E[x|z]=1/4 and E[x^2|y]=y, hence Ex=1/4 and Ey=1/16+Var(x). Since D=E[(1-4x)^2]=16 Var(x), Ey=(1+D)/16 and y-weighting gives E_nu[z]=-16a/(1+D). If D=0 then x=1/4 on the support; bounded completeness of ydot=1/16-y forces y=1/16 and tangency of xdot forces z=-16a, so the measure is the equilibrium Dirac mass. The strict excursion conclusions then follow from equivalence of mu and the positive y-weighted measure. The exact verifier independently checks the polynomial and moment algebra.

## originality

PASS

The Wang--Chen and follow-up dynamics literature studies the same flow through equilibrium stability, chaos, coexistence, bifurcations and global geometry. The forcing-specific conditional stationary law E[yz|x]=-a and its y-weighted height contraction were not found in those inspected sources or in the Resultary stationary-flow search. Previously published stationary identities for the degenerate a=0 Sprott-E equations cover only the unchanged y and z equations and do not imply the forcing-specific yz law.

## value

PASS

The theorem converts a numerically studied hidden-recurrence/coexistence flow into exact invariant-measure constraints that separate the equilibrium from every non-equilibrium recurrent state and force observable height excursions. This is a natural structural diagnostic for the system, not a routine equilibrium calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
