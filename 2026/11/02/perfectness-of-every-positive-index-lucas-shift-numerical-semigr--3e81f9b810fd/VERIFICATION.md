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

The accompanying `CHECK.py` is standalone Python 3 standard-library code. Execute `python3 CHECK.py` to reconstruct minimum Apéry representatives via Dijkstra's algorithm using actual semigroup generators, and independently compute unrestricted minimum coin counts via a dynamic program. It checks every residue at 16 indices, the no-local-maximum and endpoint inequalities, and all positive integers through each corresponding Frobenius number.

Observed result: `VERIFY_OK a_range=2..17 residues=9345 integer_positions=69001 zero_isolated_gaps=16`.

This finite validation is not offered as a proof for unbounded indices. The infinite proof derives from the established Lucas Apéry formula in Robles-Pérez–Rosales and the two digit lemmas proved in `RESULT.md`. Inputs and all prerequisites are openly specified; there is no external computation or independent mathematical audit.
