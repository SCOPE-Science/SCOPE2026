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

# Verification

The standalone `verify_clique_cycle.py` uses only the Python standard library (`fractions.Fraction`). It constructs the unweighted graph Laplacian from edges, solves a grounded rational system for **every edge column**, and independently solves the smaller massive cycle Laplacian for the Green kernel. It compares absolute column sums of the canonical cut projector and complementary cycle projector against both closed formulas, then verifies that each rim-edge orbit dominates the clique-edge orbit. All calculations use exact rational arithmetic.

Checked parameter pairs: \((3,5),(3,6),(3,7),(4,5),(4,6),(5,5),(6,5)\). The total number of checked edge columns is \(30+36+42+50+60+75+105=398\). The test output gives exactly \(352/145\) and \(353/145\) at \((3,5)\), and \(53/21\) and \(158/63\) at \((3,6)\), with every checked assertion passing.

To reproduce: run `python3 verify_clique_cycle.py` with a standard Python installation. No internet, external libraries, or unstated input files are needed. This is independent exact-arithmetic evaluation of finitely many instances, not an exhaustive test of the infinite family. The proof of the full theorem, including all inequalities and the fixed-clique asymptotics, is in `RESULT.md`.
