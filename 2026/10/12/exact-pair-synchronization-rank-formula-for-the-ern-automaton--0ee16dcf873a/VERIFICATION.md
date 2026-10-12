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

Run `python3 verify.py` beside `certificate.json`.

For every \(n\) from \(2\) through \(80\), the verifier constructs all singleton and pair states of the power automaton. It builds both outgoing transitions and the reverse graph, then computes the exact distance from every pair to the singleton layer by breadth-first search.

For each pair it independently evaluates
\[
\min\{(j-i)n-i,\ (n-j+i)n-j\}
\]
and checks equality with the graph distance. It also verifies that each generator lowers the proposed rank by at most one and that at least one generator always lowers it by exactly one.

As secondary consequences, the verifier checks the full weight range, the unique hardest pair, and the exact sum of pair weights. These finite checks validate the formulas and indexing; the all-\(n\) theorem follows from the symbolic rank proof in `RESULT.md`.
