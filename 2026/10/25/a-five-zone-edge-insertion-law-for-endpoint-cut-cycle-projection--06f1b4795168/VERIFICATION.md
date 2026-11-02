---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all m,n>=2, the canonical Euclidean cut projection on K_{m,n} has entry delta_{i,k}/n+delta_{j,l}/m-1/(mn). The new intrapart edge incidence b=e_{x0}-e_{x1} is a Laplacian eigenvector with eigenvalue n and effective resistance 2/n. Sherman–Morrison on the zero-sum subspace yields L^+=L0^+-bb^T/[n(n+2)], with new-edge coupling s_i/(n+2) and diagonal 2/(n+2). Three complete column types (far, touched, new) give touched cut q0+d, touched cycle p0+d+2/[n(n+2)], and new norms 2(n+1)/(n+2), 3n/(n+2). Direct sign checking across m=n+2 and orbit maxima gives exact two-parameter formulas, including m=2,3 and n=2,3,4. For n>=5 this yields five consecutive zones (m=2 Q↓P↑; m=3 Q unchanged and P↑; 4<=m<=2n-2 both unchanged; 2n-1<=m<=2n+1 Q unchanged P↑; m>=2n+2 both ↑). Independently recomputed all projector entries from grounded incidence/Laplacian inverses with exact rationals for 36 (m,n) pairs, including m=11..14,n=5,6 threshold boundaries, and matched the closed formulas without using the rank-one update in the verifier. Arbitrary integers follow from the analytic matrix identities and inequalities, not finite enumeration.

## originality

PASS

The general literature establishes Lipschitz-free graph spaces, transportation cycle projections and rank-one Laplacian formulas; these ingredients do not assert the exact induced edge-l1 cut/cycle norm change for the two-parameter graph H_{m,n}. Related small insertion and cross-edge deletion records have different families/quantifiers. The full five-zone asymmetric insertion phase diagram is a specific new classification to best of knowledge, qualified by possible obscure electrical-network norm tables.

## value

PASS

Canonical graph cut/cycle orthogonal projections arise naturally in graph transportation, Lipschitz-free spaces, and electrical networks. An elementary-seeming single-edge operation changes their endpoint norms nonmonotonically, with exact sharp thresholds and distinct onsets for cut versus cycle. The complete all-m,n classification and boundary exceptions expose an informative structural sensitivity not apparent from generic rank-one formulas alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
