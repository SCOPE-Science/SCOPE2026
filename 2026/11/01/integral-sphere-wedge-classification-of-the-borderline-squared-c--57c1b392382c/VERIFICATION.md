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

# Executable verification

Run `python3 verify.py`. Python 3.9 or later and the standard library are sufficient. No external downloads or files are needed. The expected last line is `BORDERLINE_SQUARED_CYCLE_FINITE_INTEGRAL_HOMOTOPY_VERIFIED`.

Across all 28 inputs with \(n=k+5\) and \(8\le n\le35\), the checker enumerates exactly 125,853 maximal faces and 335,867 nonempty faces, constructs 150,171 disjoint Morse pairs, and checks 1,393,910 oriented Hasse incidences by a full topological sort. For every input, it checks the number of critical zero-, three- and four-cells and explicitly eliminates matched cells to compute every signed critical boundary column over \(\mathbb Z\). These columns are either zero or one of the primitive columns \(e_i-e_{n-7}\); there are exactly \(n-8\) distinct nonzero columns.

For \(n=8,9,10,11,12,13,14,16,20\), the script independently reduces all simplicial boundary matrices over \(\mathbf F_2\) and asserts the predicted homology ranks. For every \(n\le18\), it independently compares the five-deletion-run facet characterization with actual breadth-first-search connectivity of every survivor-induced graph. The run-gap equivalence for all larger \(n\) is proved in the accompanying mathematical argument, not guessed from those smaller checks.

The case \(n=35\), \(k=30\) has 39,200 nonempty faces, 17,367 pairs, 28 critical three-cells and 4,437 critical four-cells, with 27 primitive signed boundary columns, yielding \(\widetilde H_3\cong\mathbb Z\) and \(\widetilde H_4\cong\mathbb Z^{4410}\). The supplied `verify.out` records execution results for all 28 cases. No computation or proof is asserted outside the prescribed finite interval, and no independent audit has been performed.
