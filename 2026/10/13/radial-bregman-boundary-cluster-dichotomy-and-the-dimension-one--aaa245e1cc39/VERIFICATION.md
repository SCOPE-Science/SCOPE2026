---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Writing x=Re1 and y=rv with c=<e1,v>, direct differentiation gives D_phi(x,y)=A(r)+R h_prime(r)(1-c), A(r)=h(R)-h(r)-h_prime(r)(R-r). The supporting-line inequality yields 0<=A(r)<=h(R)-h(r)->0. In dimension one every interior boundary approach is eventually radial and D->0. If h_prime is bounded, the gradient norm is bounded and D->0 for any approach in every dimension. In dimensions >=2 and h_prime->infinity, for any a>=0 choose c=1-a/(R h_prime) to obtain D=A+a; for divergent limit choose c=1-1/sqrt(h_prime), which gives D=A+R sqrt(h_prime)->infinity. Both cosine choices are admissible and yield y->x. The bounded-domain sublevel condition is automatic because y lies in the ball. Independent concrete Hellinger-style and quadratic radial identities were verified, not taken as a universal numerical proof.

## originality

PASS

Ou–Latafat–Themelis, Assumption 2.4 and Example 2.5, explicitly distinguish the one-dimensional Hellinger example from higher-dimensional failure, but not all radial finite-boundary convex profiles or their entire extended boundary cluster sets. The exact necessary-and-sufficient radial-slope threshold and all finite attainable limits refine that example; no direct broader source coverage identified. Residual risk of an equivalent earlier convex analysis limit lemma remains.

## value

PASS

The classification answers a natural analytic kernel-eligibility question: under finite closed-ball boundary values, whether every interior approach has vanishing Bregman divergence. It identifies the exact radial steepness/dimension threshold and not just a negative example; the full continuum of attainable boundary defects reveals the magnitude and geometry of failure. This can guide use of sufficient Bregman-zone hypotheses without falsely claiming optimizer divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
