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

# Verification details

Running `python3 verify.py` from the directory containing that program requires no third-party package and recomputes all exact finite premises of the theorem. It exhaustively constructs recursively defined complete rank-four formula types for uncoloured connected half-graphs through parameter eight, and for side-coloured half-graphs at parameters seven, eight and nine. The reported class partition and equalities are exact consequences of the complete finite type recursion, not heuristic tests or selected graph properties.

The independent symbolic component is the factor-composition lemma for the side-coloured graph language: Duplicator combines winning local games because every cross-edge is controlled by factor order and the side predicate. The graph of parameter \(n+k\) is the sum of those at parameters \(n\) and \(k\); hence a finite labelled eight-to-nine identity extends to all parameters at least eight, and the separate uncoloured seven-to-eight equality completes the proof.

`verify_output.txt` is the recorded output of this program. Reproducibility permits checking the finite premises, but is not an independent external audit. No claim is made about ranks other than four, apart from the script's labelled sanity checks at lower ranks.
