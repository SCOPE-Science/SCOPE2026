---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

In V=C e_- ⊕ W ⊕ C e_+, the quadratic form restricted to span(e_-,u,e_+,v) is 2ac+2 B(u,v)bd. Its symmetric matrix determinant is B(u,v)^2, independently rechecked symbolically; smooth rank-4 section iff nonorthogonal, whereas B(u,v)=0 makes ac=0, two planes meeting in m=P<span(u,v)>. For distinct orthogonal isotropic u,v, span(e_-+tv,u) and span(v,u+se_+) are isotropic one-parameter line families joining the extremal endpoint lines via m. The source Corollary 2.7 places the reduced chain in the quotient. Any off-diagonal reducible chain must have the unique m through u,v; source Theorem 3.12 establishes irreducible boundary E, and the incidence divisor I is irreducible. Hence E→I birational. Diagonal exceptional scheme not classified.

## originality

PASS

The initiating paper explicitly asserts that disjoint extremal lines always span a smooth quadric in Example 4.8, yet disjointness holds for distinct u,v and rank four additionally needs B(u,v)≠0. The orthogonality divisor, its two-component replacement orbit chain and birational boundary image are a concrete correction not implied by the asserted smooth case. No equivalent correction found in actual semantic primary/Resultary searches; absence of hits alone is not novelty evidence.

## value

PASS

The missing locus is a codimension-one incidence divisor, not an isolated exception: the argument restores surjectivity and identifies the image of the unique boundary divisor of a genuine Fano Chow quotient. The singular/reducible degeneration changes orbit-cycle geometry and matters for endpoint contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
