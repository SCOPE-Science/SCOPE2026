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

# Verifiable computation and limits

The primary proof is given in `RESULT.md`. Two source files and two outputs accompany it:

- `artifacts/verify_hamming_symbolic.py` enumerates exact ordered-triple equality-partition orbits, every permitted extension, every twenty-seven-state last-round transition, and all rank-four types through dimension fourteen. It checks the identities \(T^{C}=T^{C+1}\) for each of the twenty-seven singleton input states and all permitted coordinate partitions, establishing the finite-state saturation lemma for all larger dimensions.
- `artifacts/verify_hamming_direct.py` independently enumerates complete Hamming graph vertex sets and all fourth-vertex choices for selected smaller dimensions, comparing their uncompressed pair types to the symbolic calculation.
- `artifacts/symbolic_output.txt` and `artifacts/direct_output.txt` record the respective executions.

Replay from the package root using `python3 artifacts/verify_hamming_symbolic.py` and `python3 artifacts/verify_hamming_direct.py`; no third-party Python dependencies are required. The finite-boundary assertion covers dimensions one through fourteen in each of three alphabet regimes, while the analytic capped-composition proof covers all larger dimensions. The direct check covers smaller cases only, not the infinite theorem. No independent audit or external proof certification has been performed.
