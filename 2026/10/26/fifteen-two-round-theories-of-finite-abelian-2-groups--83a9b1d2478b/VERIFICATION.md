---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed the exact two-round EF criterion for the restricted relational language {0,R(x,y,z):x+y=z}: equality of the sets of all pointed one-step atomic-diagram profiles P_G(x). Every pair diagram on {0,x,y} reduces to eight predicates x=0,y=0,x=y,2x=0,2y=0,x+y=0,2x=y,2y=x; no nested binary-function terms occur. Using {0,x,-x,2x}, doubling fibres of size 2^r and generic involution/non-involution witnesses, verified the seven pointed types Z,I+/-,IV+/-,L+/- and their occurrence in terms of r=#cyclic summands, t=#order≥4, u=#order≥8, v=#order≥16. These all-exponent conditions give exactly 15 complete signature sets. Independently enumerated all actual pair diagrams for the 15 finite canonical representative groups, checked pairwise distinct signatures and C16 versus C32 equivalence; the retrieved profile_table.json agrees. The last class requires two factors of order at least eight and one of at least sixteen, so minimal order is 8*16=128. Finite signatures corroborate the all-parameter category/fibre proof.

## originality

PASS

Best-of-knowledge PASS for the exact fifteen-class rank-two spectrum and optimal bound 128, not for EF games or general finite-abelian-group distinguishing depth bounds. Mathematically compared the frozen full classification with Gomaa 2007 dissertation chapter 3 and 2010 journal article discussion: broad complexity inequalities do not enumerate or imply precise rank-two equivalence classes in the 2-primary family. Resultary semantic query retrieved other abelian structures and finite-model-theory examples, not this exact spectrum. Older unindexed low-rank classifications remain possible.

## value

PASS

PASS for an exact natural model-theoretic invariant and finite representative principle for all finite abelian 2-groups, which may be arbitrarily large. The language dependence (ternary relational addition, depth exactly two) is motivated and essential; thresholds show precisely which cyclic-factor multiplicities are visible and why exponents beyond 16 become indistinguishable. The bound 128 is a sharp canonical representative limit, not a gratuitous small numerical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
