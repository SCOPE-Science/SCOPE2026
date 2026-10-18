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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 standard libraries only. It enumerates each of the \(n!\) uniform open directed Hamiltonian paths and the distinct directed Hamiltonian cycles for every \(3\le n\le7\). Every coordinate mean and covariance entry is accumulated as an exact rational number. The program checks the operators, all five spectral projections of every directed-edge coordinate basis vector, the consistency of the decomposition, and exact arbitrary-weight variance identities.

Actual execution from the accompanying source returned:

`PASS 47656 exact covariance and spectral assertions (all paths and oriented cycles for n=3..7)`

The exhaustive checks cover only the stated finite sizes. The all-size result follows from edge-contraction probabilities, all-dimensional orthogonal decomposition and the spectral theorem in RESULT.md. No independent audit, human certification, or formal proof-assistant verification has been performed.
