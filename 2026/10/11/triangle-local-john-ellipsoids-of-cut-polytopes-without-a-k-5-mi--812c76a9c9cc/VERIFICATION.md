---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducing the finite exact-rational checks

Run `python3 verify.py` with Python 3.9 or newer; the file uses only the standard library. Expected final status begins `EXACT_VERIFY_PASS` and reports 22 graph instances, 1,522 cycle-facet inequalities, and 12,840 cut assignments. The verifier constructs induced cycles and triangle incidence, checks strict-concavity stationarity/complementarity certificates for each supplied positive rational covariance, and exhaustively verifies each signed-cycle inequality for the enumerated graph cuts. It also checks the exact ellipsoid-support versus facet-slack inequality and whether every observed equality has the asserted class.

The representative graphs are wheels with outer cycles of lengths 4 through 10, triangle books with 1 through 10 pages, a path, a chordless square, a chordless pentagon, \(K_4\), and a cactus with an edge-disjoint triangle and square. These finite checks do not establish the \(K_5\)-minor-free statement universally. Universality follows from the cut-switching diagonalization, the published facet characterization, the cycle-length inequality, and strict concavity proved in `RESULT.md`.

No independent audit has been performed. The statement is limited to finite simple graphs excluding a \(K_5\) minor, and it concerns only maximum-volume *inscribed* Euclidean ellipsoids in standard cut-incidence coordinates.
