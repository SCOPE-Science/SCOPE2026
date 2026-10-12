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

## Reproduction
Execute `python3 verify.py` in a Python 3 environment with standard library only. The program checks the algebraic inversion witness over fields of orders \(5,7,9,11,13,17,25\), and exhaustively verifies the six normalized length-five evaluation permutations and all their pairs and triples. The observed final marker is `VERIFY_OK`. No downloaded inputs are required.

## Proof boundary
The all-prime-power claim follows from finite-field power sums, a dimension estimate in the common parity-check hyperplane, and the polynomial root bound. Seven tested fields provide reproducibility checks only. The conic proof uses nondegeneracy and elementary projective-plane incidence. The exact source's relevant sections were inspected, but an unindexed prior statement remains possible. No external independent audit was performed.
