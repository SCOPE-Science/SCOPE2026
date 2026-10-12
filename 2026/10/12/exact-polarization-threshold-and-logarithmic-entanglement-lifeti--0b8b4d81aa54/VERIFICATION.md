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
# Reproducibility and verification

The theorem is established by direct two-qubit linear algebra, an exact factorization of the partial-transpose discriminant, and a monotone geometric iterate. Symbolic identities for the population map and factored threshold are tested by `verify.py`, independently of random sampling. Its numerical checks additionally construct the joint unitary matrix, trace out a new ancilla each collision, take partial-transpose eigenvalues, and compare 12,600 resulting negativity values with the formula. The deterministic random seed is specified in the script. Execute `python verify.py` after installing `requirements.txt`; the observed success marker is `VERIFY_OK 12600 matrix comparisons; symbolic identities passed`.

Random tests are not an exhaustive infinite-dimensional or all-parameter certificate; completeness is provided by the written polynomial factorization for all \(k\ge1\), \(m\in[0,1]\), and \(\theta\in[0,\pi/2]\). A human independent scientific audit has not been performed.
