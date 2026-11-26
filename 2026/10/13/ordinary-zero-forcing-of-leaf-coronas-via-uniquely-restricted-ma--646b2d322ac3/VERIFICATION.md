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

Fire initially blue leaves into white roots first. A root without an initially selected leaf cannot force another root: its white leaf blocks such a force until it forces the leaf, at which point all its original neighbors are already blue. Hence a successful sequence yields distinct donors in D, one per initially empty pair U, with no edge from an earlier donor to a later target. The matched endpoints have no alternating cycle. Conversely, using dependencies from every other adjacent target to a donor's own target, unique restriction makes the dependency digraph acyclic; processing a topological order clears U and every remaining leaf can then be forced. Fixed D,U give weight x^{n-|U|}(1+x)^{|D|}, with no overcounting. In a clique the successful cases are U empty and |U|=1 with a donor. For minimality, a doubly selected pair can lose its root without changing the criterion. If there is no empty pair, exactly one selection per pair and at least one selected leaf, keep such a leaf and delete the choice in any other pair (possible for n>=2, even for the all-leaf set); this fills an implicit case in the written proof. The all-root set and the one-empty-pair sets with one choice per other pair are therefore exactly the minimal sets. The minimum coefficient, upper number and boundary n=2 follow. Frozen verification files and output were inspected, not executed; the reported finite coverage is supplementary.

## originality

PASS

Credit constrained matching as prior machinery and the same-day leaf-corona power-domination record for an exact overlap on leaf-only seeds. The supported contribution is the ordinary all-seed transfer and weighted enumeration, with the exact clique minimal-set classification and correction of the earlier blanket minimality assertion. No priority is inferred from same-day indexing.

## value

PASS

The structural test replaces trajectories in an arbitrary corona with a matching problem on the base cut and also counts all initial sets by size. The clique case resolves a concrete earlier minimality issue and separates minimum from inclusion-minimal sets. These uses do not depend on a claim of efficient general enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
