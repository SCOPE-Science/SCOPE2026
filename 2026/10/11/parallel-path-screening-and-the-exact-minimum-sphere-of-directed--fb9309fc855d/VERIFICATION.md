---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The formula supplies a constructive primal/dual certificate: each edge has potential gap Δ=z_u−z_v≥1; on the longest k paths assign α_i=L/(2k), otherwise α_i=0, and λ_{i,j}=α_i+(j−1)(ℓ_i−j)/2≥0. Direct endpoint and internal-vertex incidence gives Σλ(e_u−e_v)=z, λ is positive only where Δ=1; Σλ=N and dotting by z gives ||z||²=N. Thus c=z/N belongs to the convex hull of contacting edge roots, ||c||²=1/N, and each edge root a of norm²=2 obeys ||a−c||²≤2−1/N. Averaging against λ/N proves every other center y has a root at squared distance at least 2−1/N+||y−c||², proving global minimality and uniqueness. Exact gaps give the asserted contact count, short-edge deficits and two-edge addition invariance. Independently reimplemented exact Fraction checks over 1,360 admissible ordered path lists (2–4 paths and lengths≤6) in addition to analytic argument; bounded enumeration is not the infinite proof.

## originality

PASS

The general minball barycentric criterion and all-contact equal-length graded cases are previously published and are not claimed. Primary directed-edge-polytope face/dimension papers and lattice dissection papers do not compute mixed-path Euclidean minimum spheres. The directly read Resultary rank-variance and semibalanced sphere theorems require a rank function with unit increment on every edge, impossible when directed s→t paths have unequal lengths; they cover only the equal-length special case. The oriented-cycle Ehrhart theorem solves an unrelated integer-lattice invariant. Nontrivial mixed-length exact weights, full contact screening and two-edge insertion stability survive these implication comparisons.

## value

PASS

Mixed-length parallel s→t path networks are a natural infinite family of directed root polytopes. The closed exact center/radius, complete boundary-contact and clearance strata, and counterintuitive invariance under adding length-two paths are substantive structural results not obtained merely by substituting into the already-known graded special case or by recomputing a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
