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

# Reproducibility and proof limits

The standalone scripts use only Python 3 standard-library modules and reconstruct Johnson graph vertices and edges from the mathematical definitions. Execute `python check_pair_spectra.py` and `python check_ef_types.py` from the directory holding the scripts. Compare their standard output with `pair_spectra_output.txt` and `ef_types_output.txt`, respectively.

The first script builds each line graph through incidence bitsets and examines **every** unordered pair of its vertices, recording third-vertex common, one-sided, and neither-sided witness presence. It verifies the exact predicted signature sets for all sixteen permitted parameter pairs with \(4\le n\le10\). The largest constructed graph has \(3150\) vertices.

The second script uses independent set-intersection and endpoint-set graph construction and computes full three-round types by listing every third-choice quantifier-free atomic diagram (including repeated selections), every second-choice rooted type, and every first-choice rooted type. It checks three separating representatives and four further graphs in the stable class, including \(L(J(7,3))\).

The infinite theorem is supported by the explicit mathematical proof in `RESULT.md`: the uniform degree and edge-count inequalities, the complete octahedral boundary case, and the constructions and obstructions for induced matchings. Finite scripts corroborate these critical signatures but cannot prove an unbounded classification. The literature comparison is best-knowledge rather than comprehensive priority certification. Independent review is not yet performed.
