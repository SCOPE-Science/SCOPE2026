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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and its standard library, without third-party packages or external data. The script reconstructs the allowed length-three words and the reduced Laplacian afresh; evaluates exact reduced cofactors by fraction-free Bareiss elimination for every applicable two-equal-symbol or three-distinct-symbol case with \(2\le q\le6\); and separately checks the rank-three determinant by rational arithmetic. For \(q=2\) and \(q=3\), it performs direct complete Euler-tour enumeration with a fixed first edge. It asserts the two closed formulas and selected independent large-integer values, then prints `ALL_CHECKS_PASS`.

These computations test finitely many alphabet sizes. The all-alphabet theorem depends on the displayed exact identities \(A^2=J\), \(L'=L-XY^T\), the determinant lemma, the directed matrix-tree theorem, and BEST. The proofs of those identities and theorem hypotheses appear in `RESULT.md`. The direct tour enumeration uses edges as distinct labeled triples, consistent with identifying positional rotations but not reversals or alphabet permutations.

The first motivating open source was publicly posted 2009-04-25 (arXiv:0904.3997v1). Unindexed equivalent literature, including records unavailable in full text, could affect a priority assessment. Independent scientific validation has not been performed.
