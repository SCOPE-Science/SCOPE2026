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

# Reproducibility

Run `python3 verify_python.py`. Separately compile and run `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp`. No external libraries are needed.

Both computations independently enumerate canonical partitions of \(m\) rows into at most three classes for \(m=3,5,6\), excluding an impossible constant column. They test every ordered-increasing family of \(m\) columns that might satisfy the diagonal case, never accepting triple reuse of a row-pair edge, and find zero completing families. The candidate-column counts are respectively \(4\), \(40\), and \(121\). Intermediate visited-node totals differ due to traversal/pruning choices; both complete counts are zero. Each program directly checks the displayed \(4\)-by-\(4\), \(6\)-by-\(5\), \(7\)-by-\(7\) tables and their appropriate projections.

The proof that these checks are exhaustive appears in RESULT.md: in a diagonal table, the number of distinct row pairs equals the number of demanded column pairs, requiring exactly one witness per pair. The algorithms enumerate every column equality partition modulo alphabet renaming, and every unordered selection modulo column reordering. No result for unrestricted row counts or larger alphabets is extrapolated from finite search. The nonexistence beyond seven columns is sourced separately from the published maximal-length theorem, not inferred from an experimental cutoff.
