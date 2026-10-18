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

Run `python3 verify_prism.py` with a standard Python 3 interpreter. No third-party packages or network access are required. The script prints `PASS 868 exact rational structural/projection assertions`, followed by the tested ranges.

For clique sizes \(m=3,4,5,6,7,8\), the program reconstructs cycle and cut projections column by column over exact rational numbers and matches their maximum absolute column sums to the two claimed rational expressions. For \(m=3,4,5\), it also verifies the projector identities, the range and annihilation identities, and signed equivariance under simultaneous adjacent transpositions of clique labels and under layer interchange. These statements are evaluated from the embedded source file, not from precomputed external logs.

Limits: the program tests finitely many parameter values. The all-integer proof, uniqueness of the equivariant parametrizations, and global minimization are established symbolically in RESULT.md. The tests are consistency checks and are not exhaustive certification of the infinite assertion. No independent audit or external validation has been performed.
