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

# Reproducibility of the adjacent-double universal-cycle theorem

The standalone Python 3 standard-library program `verify.py` enumerates all allowed four-letter words directly and constructs a full overlapping-three-letter directed graph. For alphabet sizes three, four and five, it calculates its rooted directed Laplacian cofactor using exact Bareiss fraction-free elimination. It separately builds the contracted parity-lift graph and calculates its cofactor, checking both against the symbolic formula. Graph balance, number of allowed factors, and connected components are checked from the generated graph itself.

The program also constructs Euler circuits by a deterministic form of Hierholzer's algorithm for alphabet sizes four, five, six and seven, then independently enumerates all circular four-windows and compares their multiplicity counters to the intended target language. `witness_q4.txt` gives the explicitly verified 72-symbol construction for the four-symbol alphabet, with symbols `0`, `1`, `2`, `3`.

Run `python3 verify.py`. Observed output includes rooted cofactors \(0\), \(1{,}327{,}104\), \(427{,}972{,}821{,}516{,}288{,}000\) for alphabet sizes three, four and five, respectively; the execution terminates with `VERIFY_OK`.

Finite examples do not prove the infinite formula. The proof's critical general steps are connectivity and aperiodicity of the non-backtracking complete-graph digraph, the exact Ihara characteristic polynomial, the spectral directed matrix-tree product, invariance of cofactors under contracting forced degree-one paths, and BEST's specified-edge normalization. No external or independent scientific audit is claimed.
