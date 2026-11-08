---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For finite rooted-tree ancestor posets, every idempotent regressive order-preserving selfmap is the deepest-fixed-ancestor projection e_S for a unique subset S containing the root: order-preserving forces a fixed ancestor s<=x to lie below e(x), and idempotence fixes e(x). Hence 2^(n−1) idempotents exactly. For ordered pair (S,U), compare the two deepest fixed ancestors along each root path; disagreement occurs iff 10 and 01 both appear after a common 11 and before the next common 11 on some prefix. The finite automaton with inherited states 0,A,B and vertex labels 11 reset / 00 stay / 10 A / 01 B yields precisely F_v(0)=2P_0+P_A+P_B, F_v(A)=P_0+2P_A, F_v(B)=P_0+2P_B; root forced 11 gives c(T)=prod_children F_w(0). Leaf values (4,3,3), one-vertex count 1, stars 4^k and chain recurrence a_0=1,a_1=4,a_m=4a_(m−1)−2a_(m−2) are correct. Independent exhaustive pairwise-composition checks on every recursive labeled rooted tree of orders 1..7 (874 rooted trees, up to 2^12 ordered pairs each) agreed exactly with DP; chain 1,4,14,48,164,560,1912 and stars 1,4,16,64,256,1024,4096. Enumeration supports, but does not prove, the unrestricted theorem, which follows by unique paths and conditional subtree independence. O(n) arithmetic updates excludes big-integer bit complexity. No assertion for arbitrary posets or unordered pairs.

## originality

PASS

Best-of-knowledge novelty for the exact arbitrary-rooted-tree ordered commuting-idempotent pair count and its three-state recursion. The 2011 Ganyushkin–Mazorchuk full primary paper proves the Catalan chain monoid identity and its 2^(n−1) idempotents; Pantazi–Spircu supplies further chain idempotent decompositions; these are prior inputs, not claimed new. A materially closer 1996 Solomon tree Catalan-monoid paper exists, but its full text could not be read; title/abstract concern local endomorphism presentations, not the exact ordered-pair count, and priority risk is explicit. The two complete published Resultary comparisons count different transformations or retraction images. Search noncoverage is not proof of novelty; no decisive dominating statement was found.

## value

PASS

The commutation proportion among the natural idempotents of a finite poset transformation monoid is a meaningful semigroup invariant. The three-state recursion gives a uniform, shape-sensitive exact value for every finite rooted tree, rather than a table for chosen small trees or a presentation-only restatement. Star and chain extremes demonstrate distinct behavior: stars have full idempotent commutativity while the chain fraction follows a nontrivial second-order recurrence. Researchers comparing commutativity graphs/centralizers of tree transformation monoids can use the exact recurrence. The result does not claim asymptotics or maximal commuting families. Its value is a reusable classification of a natural invariant, not mere code correctness or novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
