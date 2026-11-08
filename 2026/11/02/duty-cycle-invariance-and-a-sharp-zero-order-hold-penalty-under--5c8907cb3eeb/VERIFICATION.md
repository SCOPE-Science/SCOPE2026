---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For bounded periodic scalar a,b with inf |b|>0 and positive noise sigma, variation of constants conditional on the sampled state gives R(K)=(G+int_S v)^2+sigma² int_S v² for v=e^(A(tau)-A(s)) b(s)K(s). Splitting v into its constant mean and L²-orthogonal residual uniquely minimizes R at v=-G/(ell+sigma²), giving R_*=G²sigma²/(ell+sigma²) and an admissible shape independent of S placement. Independent increments imply E X_(k tau)²=R^k X0²; bounded within-period moments yield full-time stability iff R<1. Constant-coefficient ZOH square-completion yields ell_ZOH=(2/a)tanh(a tau/2), strict ell_ZOH<tau and ratio (a tau/2)coth(a tau/2). Independent computation at a=tau=1,sigma²=.15 yields shaped 0.963789926<1 versus ZOH 1.031765975>1.

## originality

PASS

Qualified best-of-knowledge comparison of mathematical statements and known implications: exact assessed full claim not found covered in the cited primary sources or relevant published mathematical findings; specific old ingredients and all access limitations are explicitly credited. A failed search is not a proof of novelty.

## value

PASS

This solves a motivated actuator allocation and sampled-feedback feasibility problem: precise necessary/sufficient noisy activation duration for arbitrary measurable on-sets with no gain constraint, and a strict quantifiable implementation penalty when waveform shaping is forbidden. It identifies robust-looking placement invariance under explicitly limited assumptions rather than a routine bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
