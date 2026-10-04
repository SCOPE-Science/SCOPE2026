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

The proof was replayed at two levels.

1. **Symbolic check.** For the forbidden-pair Cayley set \(S_n=\{j,j+e_1,\ldots,j+e_n\}\), the even-\(n\) basis \(\{j+e_i\}_{i=1}^n\) and the odd-\(n\) basis \(\{j,j+e_1,\ldots,j+e_{n-1}\}\) were checked directly. Their transformed connection sets are respectively the folded-cube generators and one independent \(K_2\) generator plus the folded-cube generators.

2. **Finite replay.** Running `python3 verify_folded_reduction.py` exhaustively checks all unordered vertex pairs for \(3\le n\le8\). It verifies basis rank, mapped connection sets, bijectivity, and equality between “Hamming distance at least \(n-1\)” and adjacency in the claimed target graph. The script terminates with `VERIFY_OK`.

The finite replay is not used to infer the theorem for larger \(n\); the all-\(n\) conclusion rests on the displayed algebraic proof. No independent audit has been performed.
