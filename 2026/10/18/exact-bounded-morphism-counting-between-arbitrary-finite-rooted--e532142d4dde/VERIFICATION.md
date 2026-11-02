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

For every nonempty finite unordered rooted tree T,U, with xRy iff y lies in the inclusive descendant cone, the forth/back condition is exactly f(T_x)=U_{f(x)}. A surjective map must send the root to the target root and the root-fixed condition is sufficient for surjectivity. Given s->t, child c->u must have u in U_t and its cone image is U_u. An immediate child v of t lies in U_u precisely when u=t or u=v. Thus missing a nonempty set J of target children forbids u=t and u in J, yielding B_c(t,J) =A_c(t)-F_c(t)-sum_{v in J}F_c(v), while J=empty gives A_c(t). Independent child-cone choices and inclusion-exclusion give the displayed F_s(t) recurrence with an empty product of 1. Induction on source cones proves all states. A source leaf maps to a leaf target with count 1, to a nonleaf target with count 0; one-node target admits exactly one constant map from any source. The root-fixed count N(T,U)=F_root(T)(root(U)) covers all surjective maps, including equal-order automorphism boundary. A_c subtree sums take O(m) per source state, while enumerating child subsets in target-degree Delta takes O(|children(s)| Delta 2^Delta) per (s,t); sum over source edges yields O(n m max(1,Delta) 2^Delta) big-integer operations and O(nm+2^Delta) integer cells (streamed). The source script was read, its two DPs and independent direct-check source were inspected. A separate implementation compared direct cone-image enumeration, positive coverage states and inclusion-exclusion for 196 rooted-shape pairs, corresponding to 62,778 root-fixed functions, plus 81 star pairs and binary-to-chain heights 0–4. All passed. Finite checks corroborate, not replace, the induction; counts and bit costs are not unit-time machine complexity.

## originality

PASS

No inspected existing result states or implies the number of surjective bounded morphisms between every pair of finite rooted trees equipped with the single reflexive-descendant relation, or its O(n m max(1,Delta) 2^Delta) arithmetic-operation bound. Modal logic references give the forth/back definition, not enumeration. Prior weak-order mapping-space counts allow arbitrary order-preserving maps, not the back condition, and restrict to ordinal sums of antichains. Rooted-tree embedding and unordered inclusion results count or decide injective patterns rather than noninjective open quotients. Best-of-knowledge judgment; specialized prior open-map enumeration remains a priority risk.

## value

PASS

Exact cardinalities of bounded-morphism quotient maps are a natural modal-frame invariant distinct from image existence, truth preservation and injective tree pattern counts. The formula handles arbitrary unbounded-height unordered rooted source and target shapes, and converts the local back condition into an explicit all-pair count and target-branching fixed-parameter arithmetic algorithm. The classical star-to-star surjection formula and the full binary-to-two-chain sequence illustrate nontrivial multiplicity beyond a yes/no image test. It is a reusable structural counting result for all finite rooted tree frames, not an arbitrary finite slice; no broader lower bound, bit-FPT result, or combinatorial classification of distinct isomorphism-orbits is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
