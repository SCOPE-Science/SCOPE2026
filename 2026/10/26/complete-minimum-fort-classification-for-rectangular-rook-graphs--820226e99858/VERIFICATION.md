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

# Verification of the minimum-fort theorem

The self-contained Python script \(\texttt{verify.py}\) implements the original definition of a fort (every unselected cell has either zero or at least two selected neighbors) independently of the proof's degree-support shortcut. For each rectangle with \(1\le p\le4\) and \(p\le q\le8\), it exhaustively tests every nonempty subset of cardinality at most the predicted minimum, independently constructs all claimed minimum forts, and asserts equality of the two families. The script also compares the occupancy shortcut with the original condition for all subsets on selected boards having at most 12 cells. Exact integer tests; no probabilistic assumptions or optional libraries. A run's standard output is embedded as \(\texttt{verification_output.txt}\).

The exhaustive experiment is finite; it does not establish the result for rectangles outside its range. General validity follows from the occupancy lemma and case analysis in the proof. Publication priority and independent mathematical validation remain unverified.
