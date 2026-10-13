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

# Reproducibility and limits

Run `python3 artifacts/verify_pauli_flat.py` from the root of these files, using only the Python 3 standard library. This script constructs the 15 Hermitian two-qubit Pauli matrices, checks every row/column product and pairwise commutation in the Peres–Mermin square, exhaustively loops through 32,768 sign vectors, and establishes that every vector violates at least one contextual product sign. For every 127th assignment it directly checks the rank-one contextual projector against all 15 Pauli expectations. It also checks the all-positive candidate with exact integer Gaussian matrix operations, using \(Q=12\omega\) to avoid fractional arithmetic: \(\operatorname{Tr}Q=12\), \(\operatorname{Tr}(QP)=4\) for all 15 nonidentity Paulis, and \(\operatorname{Tr}(Q^2)=96\). The characteristic polynomial test for \(H=\sum_{P\ne I_4}P\) is \(H^4-30H^2-72H-27I_4=0\), consistent with eigenvalues \(-3,-3,3\pm2\sqrt3\).

Successful execution prints `VERIFY_OK: 32768 sign vectors, 98304 frustrated contexts, exact rank-one witnesses, 15 Pauli expectations, and characteristic identity`. The 32,768 cases are exhaustive only for the **finite sign alphabet**. The state-space theorem does not follow merely from finite enumeration: the universal positivity inequality and separable decomposition are supplied as analytic arguments in `RESULT.md`. Matrix arithmetic involves small integral Gaussian components that remain exactly representable in Python's complex implementation. No independent audit, hardware validation, or unrestricted large-qubit certification is claimed.
