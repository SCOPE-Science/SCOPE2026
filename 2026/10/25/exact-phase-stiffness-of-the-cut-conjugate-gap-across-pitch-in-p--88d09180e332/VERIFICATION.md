---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Verified the factorized exponential-map Jacobian source equation F=A sigma^2+B and independently symbolically differentiated at (tau,alpha)=(pi,0): F=0, F_tau=-pi^3(1+4 sigma^2)/2, F_alpha=0, F_alphaalpha=2pi^4 sigma^2. For fixed sigma>0, F_tau!=0 permits an implicit root tau(alpha) with tau″(0)=4pi sigma^2/(1+4sigma^2), so the quadratic coefficient is 2pi sigma^2/(1+4sigma^2). Shift alpha by pi to obtain the other exceptional branch; source exclusion of earlier conjugate times identifies the root as the first conjugate time near phase 0,pi. Differentiation gives kappa′(sigma)=4pi sigma/(1+4sigma^2)^2>0, limits 0 and pi/2. The sigma=0 Heisenberg limit is separately scoped. No uniform expansion as sigma->infinity is asserted.

## originality

PASS

Návrat–Zalabová arXiv:2404.01831 establishes the path-group cut locus, exceptional equality phases and an implicit conjugate-time Jacobian factorization with a broad upper bound. Its inspected Sections 3–4 and Lemma 4.3/Remark 4.3 do not state the explicit kappa(sigma) second-derivative formula. The refinement is short, follows by differentiating their equation but supplies a new exact local invariant and monotone profile. No dominating formula surfaced in Resultary, with possible implicit treatment by subsequent local conjugate-locus researchers remaining a risk.

## value

PASS

For geodesics where loss of global minimality and exponential-map singularity coincide only at exceptional phases, the second-order phase-stiffness is a naturally motivated local sensitivity and conditioning coefficient. The exact pitch dependence, strict monotonicity and saturation at pi/2 are useful quantitative geometry beyond a qualitative equality criterion, without claiming a global conjugate-time formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
