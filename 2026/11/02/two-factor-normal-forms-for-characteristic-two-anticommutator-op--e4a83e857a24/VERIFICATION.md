---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the (E11,I,E12,E21) basis, direct multiplication gives T(a,v)(h,t,z)=(0,ω(v,z),hv+az). Reading the image of E11 and the two off-diagonal units recovers the parameters of a product (r,s,u,d) uniquely. Two factors give r=a₂a₁, s=a₂v₁, u=a₁v₂ and d=ω(v₂,v₁). If r≠0 this forces d=ω(u,s)/r and the converse follows by taking a₁=1, a₂=r. If r=0, at least one of u,s vanishes; any scalar d is realizable by nondegeneracy of ω, including when both vectors vanish (set a₁=a₂=0). On the trace-zero image of any generator, T(a₃,v₃)T(a₂,v₂) agrees with T(a₃a₂,a₂v₃), reducing every longer word. Among single factors exactly T(0,v≠0) are not twofold, and the identity is separate since the nonempty words kill I. Over F_q the r≠0 stratum has (q−1)q⁴ rank-two maps, the r=0 stratum has 2q³−q maps of rank one except for zero, and the extra q²−1 single factors have rank two. This gives the stated ranks and order; none of the structural steps requires a perfect field. Independent closure enumeration on all 16 vectors over F₂ returned 34 maps with ranks (1,13,19,0,1).

## originality

PASS

The characteristic-two obstruction is already explicit in the closest Jordan multiplication paper. The supported distinct contribution is the complete two-factor normal form, exceptional one-factor maps, and finite rank distribution for the unnormalized M₂(k) composition monoid. No inspected equivalent result or stronger implication was found.

## value

PASS

The monoid is the first nontrivial size for the characteristic-two analogue of an established generation problem. Knowing the prior obstruction alone cannot determine whether a proposed operator is attainable. The normal form decides attainability and minimal word length and gives rank counts uniformly over all finite fields of this characteristic, rather than an arbitrary small-field census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
