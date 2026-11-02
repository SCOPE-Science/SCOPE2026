---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For self-adjoint 0<=F<=qI, the centered operator F-qI/2 has norm <=q/2. Therefore H u=(q/2)u+(F-qI/2)Pu+(G-qI/2)(I-P)u gives ||Hu||<=q/2+(q/2)(||Pu||+||(I-P)u||)<=q(1+sqrt(2))/2 for every dimension. In dimension 2, P=diag(1,0) and rank-one F,G projectors onto symmetric vectors at angle pi/8 produce a symmetric H with norm exactly C=(1+sqrt(2))/2. Scaling and small positive-definite perturbation establish iff damping threshold qcrit=2/(1+sqrt(2)). The supplied same-generator backward-Euler example A=diag(1/2000,5), F=(I+A/2)^(-2), G=(I+A)^(-1), P=ones(2,2)/2 has exact ||H e1||^2-1=31863808011974591697209/39416723919275164992358416>0 (independently rederived using rational arithmetic), while G-F is positive diagonal and H is similar via positive diagonal scaling to G-(G-F)^(1/2)P(G-F)^(1/2), Hermitian lying strictly between F and G: spectrum inside (0,1). This is transient one-step growth, not divergence.

## originality

PASS

The map H_P(x)=G(x)+F(Px)-G(Px) is explicitly prior work in projection-based parareal. The newly evaluated sharp norm over positive self-adjoint F,G, its universal threshold, and common-generator backward-Euler counterexample are not established by the inspected nonlinear convergence bounds or single-eigenmode coarse-propagator estimates. Earlier exact generic block-projection inequalities remain a plausible unindexed equivalent.

## value

PASS

For time-parallel splitting, knowing that both propagators are strictly contractive spectrally is not sufficient to guarantee no one-step Euclidean norm growth. The exact sharp universal damping boundary, optimizing 2D extremizer and dissipative common-ODE example isolate a physically/numerically motivated structural stability issue; it is not a claim of full iteration divergence or nonlinear convergence failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
