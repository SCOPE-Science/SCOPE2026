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

The following exact replay was performed on the standalone files associated with this result:

`python3 verify.py`

The verifier compiles `census.cpp` and `check_independent.cpp` using C++17, reruns their complete independent enumerations, compares the exact output text to `census_report.txt` and `check_report.txt`, and compares the complete independently regenerated list of extremal encodings to `extremal_ids.txt`. It then reconstructs all \(38\) symmetry orbits from first principles in Python, verifies each has \(240\) elements, that none overlap, and that their union is exactly the \(9,120\) independently enumerated automata. It separately tests every representative using literal binary words of lengths \(1\) through \(5\), verifies strong connectivity of every extremizer, and checks the \((3,4),(4,4),(4,5)\) rank-type split. Successful output begins `VERIFY_OK`.

For each transition pair, the primary reverse-BFS proof and the secondary fixed-point proof compute the same mathematically defined shortest pair-merging distances by different algorithms. The proof that all pairs merge if and only if the automaton synchronizes is essential to the interpretation of the census. The computation is exhaustive **only** for five-state binary automata; no algorithmic test of finitely many instances establishes a general theorem in the number of states.

The review reported here concerns this finite claim alone. No independent third-party validation is asserted.
