---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n=mr,m,r≥2, cyclic block maps f_a(jr+u)=r(j+1 mod m)+(u+a_j mod r), Σa_j≡1 modr, are single n-cycles because f_a^m translates each block by one. The sign of f_a^t(x)−x for t not divisible by m is determined by block order; for t multiple m it is determined by internal rotation, so all r^(m−1) choices give one signature. Conversely for any n-cycle with that signature, g=f^m has exactly m r-cycles and exactly m descending points, at the block maxima. Every finite permutation cycle must have a descent, forcing g-orbits to equal the consecutive blocks, then monotonicity of all other entries forces their standard rotation. Commuting f and g makes f permute blocks, whose time-one sign inequalities force the successor block permutation; rotational equivariance then forces an internal translation on each block with sum shifts one. Thus no other cycles lie in that fiber. Independent complete n-cycle enumeration for n=4,6,8,9 verified exact fibers 2,3,4,8,4,9 across six factorizations; full proof holds for all m,r.

## originality

PASS

Fuhrmann–Gröger–Passeggi (Oct 2026) introduce precisely the point/time left-right orbit signature and prove prime-cycle rigidity, explicitly showing composite nonuniqueness with a four-point example. The present all-composite exact fiber formula plus converse classifies an infinite family beyond mere existence of nonuniqueness. The Resultary prime-cycle quadratic reconstruction note addresses only prime p, not composite ambiguity counts. Classical one-step excedance-set enumerations are strictly weaker data and cannot directly give all-power fibers. Best-of-knowledge priority remains qualified for unindexed combinatorics.

## value

PASS

The complete full-signature fiber is a natural inverse-identification invariant for periodic orbit ordering; the theorem exposes exactly r^(m−1) indistinguishable n-cycles and an exponential lower bound in even length despite observing all x,t comparisons. The complete converse and explicit family make this an independently useful nonidentifiability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
