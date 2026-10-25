---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For finite complete multipartite K_(n_i), matching number is nu=min(floor(n/2),n-p), p=max part: each matched edge consumes >=1 vertex outside any largest part, and complete multipartite perfect-matching criterion on any 2nu chosen vertices yields matching nu (if p>=nu explicitly match across largest part). To span arbitrary complete-graph k-matching difference polynomial for k<=nu, strongly induct on number of within-part forbidden edges. Fix uv inside part A: |V\A|>=k. If an outside vertex w is unused, use xu-xv=(xu-xw)+(xw-xv) to replace forbidden pair by valid cross-part edges. If all outside vertices used by other k-1 edges, one other edge st lies wholly outside A, and (xu-xv)(xs-xt)=(xu-xs)(xv-xt)-(xu-xt)(xv-xs) yields two cross-part products, strictly reducing forbidden count. Each operation preserves disjointness, so induction closes exactly. Characteristic-zero two-row Specht dimension C(n,k)-C(n,k-1) and Dunkl-matching duality are credited from arXiv:2609.34260, not independently invented. Own independent SymPy rational rank computation for profiles (2,2),(3,2),(2,2,1),(4,2) in all degrees agrees; finite checks corroborate but do not prove the infinite induction. All k>nu have no matchings; connectivity n-p gives iff saturation under relevant k range.

## originality

PASS

Best-of-knowledge assessment from exact implication comparisons of same mathematical objects; known special cases and general mechanisms are credited; actual full primary texts read when accessible and residual priority risk recorded. The retained exact result is not proved covered by the identified sources.

## value

PASS

Matching-difference k-saturation and Dunkl subalgebra Hilbert series were explicit structural questions in the founding 2026 paper. Giving complete all-degree ranks for every positive complete multipartite part profile, including unbalanced and large missing-edge cliques, and proving connectivity suffices exactly in this broad canonical family solves a motivated case not covered by the complement-matching sufficient condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
