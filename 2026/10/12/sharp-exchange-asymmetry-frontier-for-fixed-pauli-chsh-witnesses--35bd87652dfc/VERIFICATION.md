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

Run `python3 verify.py` using only the Python 3 standard library. The executed verifier returned:

`VERIFY_OK 13720 exact-rational witness and numerical-state checks`

The tests reconstruct the Bell-basis operator exactly, evaluate both signs of extremizers for 860 rational parameter pairs (1,720 checks), and sample 12,000 deterministic positive density matrices (3,000 of each rank one through four). Each random sample checks the upper bound on the absolute Bell value and the structural norm identity \(\|\rho-S\rho S\|_2^2=2d^2\). Independent of numerical sampling, the proof relies on the rank-one antisymmetric block, Schur complement positivity, and attained pure-state witnesses; no finite random sample proves all-state optimality.

The analytic scope is all positive unit-trace matrices on two qubits; the Bell operator's Pauli axes remain fixed. Reproducing the verifier does not constitute an independent scientific audit.
