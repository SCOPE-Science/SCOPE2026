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

# Verification for odd-cycle reduced-magic capacity

The symbolic two-qubit \(C_5\) test constructs explicit nonidentity Hermitian Pauli matrices with exact odd-cycle anticommutation. It checks that the characteristic polynomial for **each of 32 sign choices** is \(\lambda^4-10\lambda^2+5\), independently of the analytic Majorana-mode diagonalization. An independently assembled signed-affine linear program over all signed maximal independent-set vertices is solved for 256 random pure states; its optimum matches the three-facet formula to the stated floating tolerance. One top eigenstate explicitly saturates the odd-cycle term.

A separate k-qubit Jordan--Wigner matrix implementation independently checks every pairwise Pauli commutation relation and the exact predicted extreme spectral values for canonical models \(C_5,C_7,C_9,C_{11},C_{13},C_{15},C_{17}\) and multiple random sign vectors. It prints the predicted crossover. Run `python verify.py`; dependencies are specified in `requirements.txt`. The output terminates with `VERIFY_OK` after successful assertions. No external files, network access, pseudorandom secrets, or third-party datasets are required.

These finite symbolic and numerical tests cannot establish the all-length theorem, the classification of every representation, or scientific priority. Those rely on the separate analytic proof and comparison with primary research. Tolerances apply only to numerical eigenvalues and linear-programming results.
