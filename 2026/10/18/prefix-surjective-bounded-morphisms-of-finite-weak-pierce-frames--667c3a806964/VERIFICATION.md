---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: For nonempty finite weak-order frames P=⊕_{i=1}^h A_i and Q=⊕_{j=1}^k B_j with all a_i,b_j>=2, upward cones at x in A_i equal {x} union higher levels. The bounded-morphism equality f(↑x)=↑f(x) reduces to S_i union {f(x)}=↑f(x), where S_i collects images of earlier levels. Top-level images must lie in B1. If a prefix A_1,...,A_{i-1} maps surjectively onto B_1,...,B_{i-1}, then each f(A_i) lies in B_i; if this nonfinal image is the entire B_i the prefix extends, if singleton all later source levels must map constantly to that world, and if a proper nonsingleton subset its missing target elements rule out any next-level value. The size-at-least-two hypothesis rules out level mixing. For a final level the map may be arbitrary. This proves a unique disjoint prefix/tail normal form for all h,k including h=1. Stirling inclusion-exclusion s(m,n)=Σ_{u=0}^n(-1)^u binom(n,u)(n-u)^m counts each required surjective level. The stated hom count follows. For endomorphisms earlier surjections are permutations; terminal tail rank is 1+Σ_{i<j}a_i and arbitrary final image size t contributes binom(a_h,t)s(a_h,t); idempotent surjective finite maps are identities and final idempotents choose t fixed images with t^(a_h-t) assignments. The formula for |Aut| is ∏a_i!. Independent exhaustive maps tested [2]->[2,2] count4, [2,2]->[2,2] count10 and 5 idempotents, [2,2,2]->same 22 and7 idempotents, [3,2]->[2,2] count26, [2,2]->[2,2,2] count10, and [2,2,2]->[2,2] count6. The n=3-level 2-point rank coefficients 2,4,8,8 have total22. Exact finite checks corroborate but do not replace proof.

## originality

PASS

PASS (qualified): The foundational Bezhanishvili-Bezhanishvili-Moraschini-Stronkowski arXiv:2103.02530 establishes finite Esakia duality and weak-Pierce Boolean cascades, not this explicit prefix-surjection/tail hom-set normal form or its full image-rank, idempotent and unit enumerators in §§2.1,3 inspected. Resultary current exact recurrence for Map(P,Q) of finite weak orders counts ordinary monotone continuous maps, a larger class; its two-state recurrence does not imply these bounded morphism subcounts or the endomorphism rank distribution. Related finite weak-order self-homotopy results classify homotopy classes rather than literal bounded maps. Best-of-knowledge risk from older Pultr-Sichler 1997 full text and semigroup enumeration remains.

## value

PASS

PASS: Bounded morphisms are the actual structure-preserving morphisms in the finite Esakia duality for Boolean-cascade Heyting algebras; a complete explicit classification of all them, not just isotone maps, and exact hom-set, rank and retraction spectra for arbitrary heights and level sizes>=2, is a natural infinite-family algebraic invariant. The prefix-tail theorem rules out large classes of candidate maps structurally and reveals endomorphism/idempotent organization; not an arbitrary numerical slice or mere replay of program output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
