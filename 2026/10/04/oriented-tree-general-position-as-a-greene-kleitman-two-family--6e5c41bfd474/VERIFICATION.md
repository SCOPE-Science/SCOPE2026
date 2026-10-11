---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In an oriented tree, if \(x<y<z\) in reachability order, the directed \(x\)-to-\(y\) and \(y\)-to-\(z\) paths cannot share an edge with opposite traversal and concatenate to the unique underlying \(x\)-to-\(z\) tree path; therefore that path is directed and, because no alternative route exists, geodesic. Conversely any directed geodesic containing three selected vertices orders them into a three-element reachability chain. Hence directed general-position sets are exactly two-families. Greene–Kleitman at \(k=2\) then gives the chain-partition min–max formula. The bundled exhaustive replay through six vertices is a stress test, not the universal proof.

## originality

PASS

The closest 2026 primary paper studies directed general position, gives only a leaf lower bound and an exact arborescence case for oriented trees, and explicitly poses as Problem 5.2 the task of finding a formula for the general-position number of any tree. The classical Greene–Kleitman theorem supplies the poset min–max once a two-family has been identified, and Cameron gives a broader acyclic-digraph path-partition min–max, but neither source identifies directed general-position sets of an arbitrary oriented tree with reachability-poset two-families. Fresh Resultary and alias searches found no earlier statement of that bridge.

## value

PASS

The result answers an explicitly posed class-wide problem by converting a directed metric invariant into a standard poset two-family invariant. This is a motivated structural lemma with immediate algorithmic and extremal consequences, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
