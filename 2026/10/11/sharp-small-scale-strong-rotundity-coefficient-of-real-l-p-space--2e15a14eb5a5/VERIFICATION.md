---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For any norming (x,J_p(x)) in real Lp, distance from H_{J_p(x)} to each y∈B is exactly 1−J_p(x)(y), attained by z=y+(1−J_p(x)(y))x. The scalar Bregman remainder φ_p(t) is continuous, strictly positive, coercive for p>2, hence has minimum c_p∈(0,1/p) (minimizer in (-1,0)). Integrate the exact inequality |a+b|^p/p−|a|^p/p−|a|^{p−2}ab≥c_p|b|^p; the ball constraint supplies 1−J_p(x)(y)≥c_p||x−y||_p^p and the global lower bound. For any minimizer t_p, two disjoint normalized characteristic functions give unit vectors x_h,y_h with ||x_h−y_h||≥h and supporting slack c_ph^p+O(h^{2p}) for all sufficiently small h; this matches the lower bound. Independently verified quartic factorization (3/2)b²(a+b/3)²+b⁴/12 and p=4 two-atom symbolic h→0 limit 1/12. The finite numerical samples are not proofs.

## originality

PASS

García-Pacheco (2023) Definition 2.1 defines the precise local/global eta, Corollary 2.1 computes only Hilbert eta=epsilon²/2; his Lp-summand Theorem 2.6 is about stereographic projection, not the sharp GLOBAL eta coefficient for all real Lp p>2. Sprung (2019) studies general power-norm Bregman lower/upper controls; it does not establish the matching globally minimized eta with explicit unit-sphere pair. Published scalar Lp-summand local profile has epsilon^p/p, strictly larger than c_p. The inaccessible Xu–Zhang (1989) may have sharp scalar power remainder but does not automatically imply the new global-index upper construction. Originality PASS best-of-knowledge with this residual risk.

## value

PASS

The 2023 strong-rotundity index is a natural non-Hilbert geometric invariant with previously unevaluated exact leading coefficient across p>2 and arbitrary atomicity/dimension≥2. A sharp scalar convexity coefficient alone is insufficient: the nontrivial two-coordinate unit-sphere construction realizes it in the global hyperplane-distance index. Exact c4=1/12 is a reproducible natural benchmark, not a trivial rescaling of Hilbert modulus or a numerical grid calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
