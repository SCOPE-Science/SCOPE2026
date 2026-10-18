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

Run `python3 verify_clique_prism.py` with Python 3 and no dependencies outside the standard library. The deterministic output is included in `verification_output.txt`. The checker constructs each clique prism's graph and independently evaluates connected components of induced subgraphs, comparing every tested subset with the claimed face classification. It computes the reduced mod-two simplicial Betti vector for \(n=5,6,7,8,9\) using exact binary boundary matrices, and checks signed fixed-face Lefschetz character sums over all \(S_5\times C_2\) elements, plus 120 fixed-seed \(S_6\times C_2\) elements. All checks pass in the recorded execution.

The cited 2014 multiple-chessboard shellability theorem is the infinite-parameter topological input. The equivariant formulas are proved by exact orbit factorization on signed fixed faces, not by guessing from finite values. The code does not formally certify the external shellability theorem or exhaust all larger parameters. No independent scientific audit was performed.
