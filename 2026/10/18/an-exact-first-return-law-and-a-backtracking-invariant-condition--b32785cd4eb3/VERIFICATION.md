---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For the directed-edge memory walk d>=3 and positive alpha,gamma, q=alpha/(alpha+(d−1)gamma), r=gamma/(alpha+(d−1)gamma) with q+(d−1)r=1, the outward first-return PGF H and inward state B obey H=zq+z(1−q)HB and B=zr+z(1−r)HB. Elimination gives z(1−r)H²−[1+(q−r)z²]H+qz=0 and unique analytic origin branch H~qz. At z=1 the physical root is q/(1−r)<1; implicit differentiation gives H’/H=(1+r−q)/(1−r−q), hence E[T|return]=2(d−1)/(d−2), independent of alpha/gamma though return probability alpha/(alpha+(d−2)gamma) varies. Discriminant factors (1−lambda²z²)(1−eta²z²) and transfer from unique positive square-root singularity give the exact m^-3/2 prefactor and lambda^(2m) tail. Independently enumerated first-hit radial probabilities for d=3,q=r=1/3: 1/3,2/27,8/243,40/2187,224/19683; return probability1/2 and conditional mean4. Endpoints alpha=0/gamma=0 excluded; d=2 excluded.

## originality

PASS

The two-state first-return law and universal *conditional* mean across all positive backtracking preferences are not stated by the 2026 node2vec recurrence result or the ordinary-simple-walk first-return distribution. General weighted nonbacktracking resolvents may algebraically specialize to this formula and are a documented priority risk; the exact conditional-mean cancellation is a distinct statement.

## value

PASS

First-return distributions and conditional excursion durations are natural random-walk invariants used to distinguish transient trajectory behavior. The exact invariance of E[T|return] across an entire backtracking family, alongside varying return probability and tail rate, is a nontrivial structural cancellation with a clear motivated comparison, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
