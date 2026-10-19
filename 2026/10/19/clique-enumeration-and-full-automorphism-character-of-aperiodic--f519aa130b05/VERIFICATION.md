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
# Reproducible verification

Run `python3 verify.py` (Python 3 standard library, no packages). The code independently constructs the multiplication of distinct Brandt matrix units, the entire graph, maximal cliques by a direct Bron–Kerbosch search, and the complete clique counts for \(2\le n\le5\). It checks the classification, maximal-clique size multiset and count through \(n=6\). For every \(\sigma\in S_n\) and each of the two transposition states, through \(n=6\), it counts the **actually fixed maximal cliques** and compares against the proposed cycle-count character formula.

Observed result: `VERIFY_OK_BRANDT_CLIQUES_CHARACTER`.

This is a finite consistency check, not independent validation of the all-order statement. It does not check literature priority and does not claim a homotopy type, characteristic independence in a matrix algebra, or any larger-semigroup classification. The proof in `RESULT.md` supplies the unbounded argument.
