---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Writing u=x+iy, R=|u|^2 and B=z+R/10, the equations u'=[A_mu+i(1+eB)]u, z'=-B give d/dt(exp(i e z)u)=exp(i e z)(A_mu+i)u, exactly conjugating to e=0. H_e is globally analytic invertible and forward completeness follows from negative radial derivative at R>=9 plus linear z equation. At q=(3/2,0,0) for mu=.001,e=.01, direct rational differentiation yields Jacobian [[97/9600,-4009/4000,0],[4027/4000,1199/336000,3/200],[-3/10,0,-1]]. Its cubic coefficients are all positive but a1*a2-a3=-61700626728323/2709504000000000<0, so it is not Hurwitz. The contrast relies on the specific mu=.001,e=.1 global Hurwitz property cited as Theorem 1/Lemma 3 of Castañeda--Rebollo-Perdomo, not independently re-proved from the original global discriminant certificate.

## originality

PASS

The gauge rotation follows structurally from the source cylindrical angular equation, so it may be implicit to experts; the inspected abstract does not state global time-preserving conjugacy for all e or exhibit strictly positive conjugate parameters with opposite global pointwise Hurwitz status. Best-of-knowledge PASS with heightened priority risk due inaccessible full original.

## value

PASS

The strict rational counterexample within one positive-parameter polynomial family cleanly separates flow equivalence from the coordinate-dependent pointwise Jacobian Hurwitz test; gauge elimination is a structural simplification relevant to the original dynamical-system study.

The dated certificate retains the supplied scientific assessment, sources and limitations.
