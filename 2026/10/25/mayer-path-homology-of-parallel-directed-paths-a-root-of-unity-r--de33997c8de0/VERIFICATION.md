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

The proof is self-contained in RESULT.md. The executable `verify.py` is Python 3 standard-library code. It constructs every directed allowed path for each finite configuration, computes the forbidden-face matrix exactly over a suitable prime field with an element of exact multiplicative order \(N\), then calculates its invariant two-chain kernel and the ranks of the first boundary, second boundary, and composite second differential. It also exhaustively checks that no invariant allowed paths of length three or more survive in each sample and compares all homology dimensions with the closed formulas.

The execution covered 2,688 graph/order configurations: \(r=2,3,4\), arm lengths in \(\{2,3,4,5\}\), and \(N\in\{3,4,5,6,7,8,10,12\}\). Cases with two arms are controls only. The output ends with `EXACT_MODULAR_CHECK_OK`. The checker uses finite characteristic and finite parameter bounds; the algebraic proof covers arbitrary complex primitive roots, infinitely many arm lengths, and every \(N\ge3\). No independent scientific audit or external certification has been performed.
