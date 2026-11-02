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

Independently reconstructed the exact right-to-left group-labelled composition law (f,a)∘(h,b)=(f∘h,(b_i a_{h(i)})); idempotent labels on im(f) equal 1. The product P of commuting idempotents is an idempotent satisfying P E_j=P. Its label vector a defines diagonal D=(id,a), making D P D^-1=(p,1), after which the label comparison in (p,1)(D E_j D^-1)=(p,1) forces all conjugated labels to 1. The diagonal stabilizer of the base family comprises s_i=s_{p(i)}, precisely W^c, so orbit-stabilizer gives |W|^(n-c). The base projection is injective on any commuting-idempotent subsemigroup and its full lift set is one orbit. An independent nonabelian S3 enumeration identified 145 labelled idempotents over n=3, verified all 8,137 commuting ordered triples, direct gauge untwisting and rank profile {1:7884,2:252,3:1}. This finite check corroborates rather than proves the arbitrary W,k theorem.

## originality

PASS

Same-object and stronger-implication search compared: The natural equivalent views are simultaneous conjugation of commuting retractions, trivialization of a family of group-valued labels/cocycles, and classification of idempotent semilattice lifts; none of the inspected results establishes the simultaneous statement. Those prior structural results share the ambient monoid but their conclusions do not imply the exact higher-arity single-orbit conjugacy theorem without the simultaneous product argument. The new argument adds the idempotent common-product gauge, which directly establishes the missing simultaneous compatibility rather than deriving it from independent per-map label choices. A semantic Resultary query was executed for this problem. All source limitations and possible hidden equivalences are retained as residual risks, not misreported as proof of absolute priority.

## value

PASS

Commuting idempotents encode compatible retractions and semilattices in finite transformation semigroups. The theorem identifies a genuinely uniform simultaneous normalization even for noncommutative group labels and supplies a natural exact fiber-count transfer across all finite arities, including semilattice maximality; this is a structural statement not just a single-idempotent renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
