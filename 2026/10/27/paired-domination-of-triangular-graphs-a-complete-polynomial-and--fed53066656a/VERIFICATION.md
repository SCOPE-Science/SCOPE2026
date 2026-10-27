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

# Reproducibility and limitations

`verify.py` exhaustively checks every vertex subset of triangular graphs for \(n=3,4,5,6\), computes domination from the original graph adjacency relation, tests induced-subgraph perfect matching with a direct memoized subset dynamic program, and independently compares the even-component criterion. It additionally checks the optimum cardinalities and exact minimum counts.

`full_n7.py` checks all \(2^{21}=2{,}097{,}152\) vertex subsets at \(n=7\) using the original paired-domination definition and reports every polynomial coefficient, without implementing the claimed component criterion.

`count_min.py` enumerates every selected edge set of the proposed minimum cardinality for \(3\le n\le8\). It checks the original selected-edge component-parity condition and evaluates the three residue-class optimum formulas independently. At \(n=8\), this entails \(\binom{28}{6}=376{,}740\) edge subsets.

Run in an ordinary Python 3 environment without third-party libraries: `python verify.py`, `python full_n7.py`, then `python count_min.py`. The expected stdout of these three commands is preserved consecutively in `CHECKS.txt` and was regenerated from these actual scripts.

There are \(8+64+1024+32768=33864\) subsets in the first implementation and \(2{,}097{,}152\) in the second. For \(n=7\), the nonzero coefficients of the polynomial at degrees \(4,6,8,10,12,14,16,18,20\) are respectively \(630,44002,199815,352485,293930,116280,20349,1330,21\). The optimum counts for \(n=3\) through \(8\) are \(3,12,200,840,630,168056\). A separate formal-series symbolic calculation for \(n\le7\) matched the complete exhaustive polynomial coefficient lists; that auxiliary calculation is not needed to replay the published standard-library tests.

All experiments are finite and do not prove the infinite result. The combinatorial pairing lemma, labeled connected-graph exponential formula, and defect-based optimum classification supply the infinite proof. No independent mathematical audit has been performed.
