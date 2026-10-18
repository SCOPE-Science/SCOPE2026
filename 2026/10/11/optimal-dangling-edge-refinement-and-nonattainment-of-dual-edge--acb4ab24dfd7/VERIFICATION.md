---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For exposed dual circular arcs of an extremal unit-diameter set in R³, the original Bogosel Proposition11 supplies actual exposed dual-incidence replacement and +2 diametral pairs under each interior dangling insertion. The dual arc is a circle radius rho=√(1−s²/4) with minor angle phi<pi; chord subarc f_L(t)=2rho sin(t/2), spherical-distance subarc f_theta(t)=2asin(rho sin(t/2)). Only the original dual pair contribution changes, giving the exact additive subdivision identity for both q=L,theta. Differentiation yields f_L″=−(rho/2)sin(t/2) and f_theta″=−rho(1−rho²)sin(t/2)/(2(1−rho² sin²(t/2))^{3/2}), strictly negative since s>0. Jensen proves unique equal-angle finite r optimum and f(t)/t strictly decreasing yields increasing positive gain. Cubic expansions give the stated sharp positive r^{-2} coefficients with O(r^{-4}). Any finite extremal configuration has an exposed dual pair and strict midpoint insertion increases each J_q, so no finite maximizer; Bogosel Theorem15 bounds global J_theta, and L≤theta bounds J_L. Source symbolic verifier fully read and own numerical monotonic gains for s=0.5,1 checked; universal claim comes from geometric lemma plus calculus.

## originality

PASS

The exact local refinement formula relies on Bogosel’s earlier dangling-edge identity, but a unique optimal equal-angle partition for fixed r, strict improvement for every finite configuration, sharp r^{-2} rate and global finite-set nonattainment are new consequences not established by the cited primary statement.

## value

PASS

The distinction between a finite configuration maximum and a bounded supremum is structural in the constant-width dual-product extremal problem. Explicit optimal placements for every finite subdivision budget and sharp inverse-square discretization rates are useful for rigorous approximations and rule out finite maximizers, independently of the unknown global supremum value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
