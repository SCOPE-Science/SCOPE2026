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

The uniform-source expectation is sum of squared retained component sizes divided by N, equivalent to one plus two/N times all-pairs connection probabilities. For a tree plus one new edge, two disjoint arcs on the induced cycle yield gain (2/N) sum W_i W_j p^(d+1-j+i)(1-p^(j-i)). The five symmetry types A-E exhaust all nonedges, and algebraic comparisons eliminate same-class chords and the less favorable hub shortcut. The remaining difference is p^2(1-p)H_(a,b). In the cubic Bernstein basis H has exactly one coefficient sign variation, so Descartes after t=p/(1-p) and H(0)<0<H(1) give a unique simple zero. Independent exact bond-subgraph enumeration of all nonedges for 1<=b<=a<=3 at p=1/8,1/2,7/8 verified 18 cases.

## originality

PASS

The single-source mean connected-component size is an established percolation reliability functional, and motif sensitivity/reversals are prior phenomena. The primary 2013/2015 studies examine network reliability, threshold attacks, and local structural motifs rather than exact maximization over one added nonedge in an arbitrary double star. The present exact five-orbit optimization with unique root H_(a,b) is not implied by the inspected results; earlier edge-augmentation combinatorics remains a priority risk.

## value

PASS

Optimizing the expected percolation component size over all single added nonedges in a family of two-community trees is a natural complete network-design classification. The exact unique algebraic triangle-versus-four-cycle threshold across every a,b provides interpretable structural information beyond generic motif reversals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
