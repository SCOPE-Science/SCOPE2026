---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Barmak-Miniana's covering construction has underlying points \((x,g)\) and exactly one lifted Hasse edge over each base Hasse edge. Consequently the number and identity pattern of immediate successors and predecessors of \((x,g)\) is the same as for \(x\). Since a finite-poset beat point is exactly a point covered by one point or covering one point, beat type is preserved and reflected. If \(x\) is deleted from the base, its entire fiber consists of pairwise incomparable beat points with independent lifted witnesses, so that fiber can be removed by successive Stong strong deformation retracts. Iterating a base reduction to a core \(C\) leaves the induced regular cover over \(C\); reflection of beat points makes it beat-point-free. Its set is \(C\times G\), giving \(|\operatorname{core}E|=|G|\,|\operatorname{core}B|\). For the 13-point projective-plane core and the published connected \(\mathbb Z/2\)-coloring, this gives a 26-point core universal cover. The source-package incidence calculation gives a connected closed triangulated surface with Euler characteristic 2, hence weak type \(S^2\); differing core cardinalities exclude finite-space homotopy equivalence with the six-point minimal sphere model.

## originality

PASS

The full G-colorings paper was inspected. It gives the explicit Hasse-edge cover, the Stong beat-point criterion, and the projective-plane universal-cover coloring, and even uses beat deletions in a different infinite example, but does not state fiberwise beat-point reflection or core-cardinality multiplication. Targeted searches for regular finite-poset coverings with Stong cores/beat points found no earlier theorem. The result is a short structural lemma assembled from the covering's local combinatorics, but it is not a parameter substitution or a special case of a located stronger core theorem; it produces a reusable exact core invariant.

## value

PASS

The fiberwise beat-point lemma gives an exact, reusable structural law for Stong cores under a natural class of finite coverings. Its projective-plane application cleanly separates weak homotopy type from finite-space homotopy type by producing a 26-point beat-point-free universal cover of weak type \(S^2\).

The dated certificate retains the supplied scientific assessment, sources and limitations.
