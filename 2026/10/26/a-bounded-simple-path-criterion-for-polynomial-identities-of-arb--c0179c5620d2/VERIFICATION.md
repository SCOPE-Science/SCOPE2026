---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Two based simple cycles at the same vertex are prefix-free, giving a free two-generator subalgebra over any field (and a free subalgebra of every finite rank by coding). A vertex-simple path of length d contains the line-quiver subalgebra UT_(d+1); isolating the coefficient of one longest word by superdiagonal matrix units disproves any proposed nonzero degree-d identity when such paths are unbounded. For sufficiency, in the support of any one path each internal edge of a strongly connected component lies on a simple cycle, by taking a shortest return path. Two internal outgoing edges at a vertex would give two such cycles through it. Thus each component is an isolated vertex internally or a simple directed cycle, of size at most L+1. The support path crosses its components in a chain without revisits. Replacing each internal segment by a simple one gives a vertex-simple path crossing the same components, so there are at most L+1 of them and at most N=(L+1)^2 vertices in all. For the standard identity, use basis paths, ignoring the zero case where no product concatenates. The endpoint multigraph has at most N vertices. All its Euler trails with fixed endpoints expand to the same original path: the intercomponent arrows are forced in order because a trail never returns to a component, and inside each strongly connected block the expansion maps to one original component, whose paths are determined by starting vertex and length. An all-length-zero block expands to a stationary path, including the degenerate case omitted by the cycle wording in the record. For each endpoint pair independently, signed cancellation also follows by substituting a matrix unit for each endpoint arrow in M_N(F) and applying Amitsur–Levitzki, which verifies the same cancellation over every field without needing a separate Swan proof. The ray's LPA has GK-dimension zero by the cited acyclic case, and its path algebra is non-PI by the necessity argument. The v1 reference should point to v2 for Lemma 6.7 and Open Question 6.9; this does not change the theorem.

## originality

PASS

Credit the arbitrary-quiver equivalence and bound in terms of vertex-simple length. The finite-quiver result, its path-expansion lemma and cancellation method, and the infinite-ray example are established antecedents. The ray's GK comparison follows directly from the prior ray result plus Rangaswamy and is not separately credited as new.

## value

PASS

A complete classification with a usable uniform identity degree distinguishes genuine infinite path obstructions from mere infinitude of the quiver. The path-support compression supplies a quantitative bridge from local graph structure to a global identity and separates the ordinary path-algebra condition from the previously known Leavitt growth condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
