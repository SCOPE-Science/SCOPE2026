---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The slit disk D_s deletes (-1,0]x{0} from the open disk; h_m(x)=prod_{j=0}^{m}(x+1-j/m) has m+1 distinct roots t_j in [-1,0], including t_m=0. The piecewise semialgebraic graph f_m uses +h_m above the negative slit, -h_m below, and 0 for x>=0; h_m(0)=0 makes it continuous on its domain. The explicit homotopy F((x,y,z),s)=(((1-s)(x+|x|)+(x-|x|))/2,(1-s)y,z) fixes x<0 and the sign of y until endpoint, and shrinks x>=0 inside the closed disk where z=0. It preserves the graph closure and fixes the two-branch limiting graph A_m. A_m has m+1 vertices at the roots and 2m edges, so graph cycle rank E-V+1=m, homotopy a wedge of m circles, H1=Z^m and pi1 free F_m. Michel Proposition3.3 establishes pair homeomorphism from bounded cornet CAD cell to slit disk; Proposition3.5 transfers its semialgebraic section with closure homeomorphism, yielding bounded CAD cell in R^4. The construction is for EVERY integer m>=1, not finite numerical samples; no assertion on R^3 or higher homology.

## originality

PASS

Michel arXiv:2601.09795 Propositions3.3,3.5,3.10 yield a slit-disk/cornet section and one-loop closure; remark that infinitely many distinct counterexamples may be constructed does NOT imply unbounded Betti rank, because infinitely many spaces can share b1=1. The new polynomial with m+1 alternating branch intersections explicitly creates m independent cycles and proves the uniform deformation/section transfer. Davenport-Locatelli-Sankaran's regular-CAD theorem assumes a stronger well-based setting, therefore cannot bound arbitrary exotic CAD closures. Resultary semantic search found no equivalent unbounded-rank theorem, with ordinary indexing limitation.

## value

PASS

An intrinsically motivated topological boundary: CAD cells are contractible, yet their closures in fixed ambient dimension four can have arbitrarily high first Betti number and arbitrary finite free fundamental-group rank. It upgrades Michel's one-loop example to an explicit quantified unboundedness family and rules out uniform closure homology bounds without regularity assumptions. A full homotopy classification is neither needed nor claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
