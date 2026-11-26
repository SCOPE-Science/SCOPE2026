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

The source's factorization manifold gives exactly the stated planar flow. The square is forward invariant and an interior orbit cannot hit a face. At I=0, tau<4 rules out positive B equilibria and the origin has eigenvalues 203/437 and -2. On the infection nullcline the behavior-nullcline residual has opposite endpoint signs and (1-B)^2 h'(B) >= 15185/28800, giving exactly one endemic equilibrium. The stated Jacobian there has trace 8387/52440, determinant 1075/6992 and negative discriminant. A small outward-pointing quadratic level set excludes that repeller from the omega-limit of every other orbit. For L=I exp(-30B), the logarithmic derivative is at least (R-1)-(R+60)I. If L <= epsilon exp(-30), with epsilon=(R-1)/(2(R+60)), this is strictly positive. This yields a positive trajectory-dependent lower bound on I, then a lower bound on B; the upper-face bounds keep both variables below one. Hence every nonequilibrium interior orbit has a nonempty compact omega-limit set without equilibria and Poincare–Bendixson applies. Near q_c=1 the admissible nullcline interval ends at 203/(640 q_c), its slope bound persists by continuity on a fixed neighborhood of the original interval, the endemic repeller persists by the implicit-function theorem, and the log-barrier still holds since R q_c<3/2.

## originality

PASS

The same vector field is in Plank et al., but neither the inspected low-tau analysis nor its supplement covers this repelling endemic point and global periodic omega-limit result. A later catalog record mentions periodic solutions in the Plank reduction, without supplying the parameters or global conclusion; its proved theorem is for a different SIS–logit system. This decision credits that qualitative overlap, not novelty of behavioral oscillations in general.

## value

PASS

The witness identifies an autonomous periodic regime in the published two-variable model even when a positive-behavior disease-free equilibrium is absent. Showing periodic omega-limits for every nonstationary interior trajectory and persistence below full protection is materially stronger than showing a locally unstable equilibrium or plotting a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
