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
# Reproducibility and boundaries

Run `python verify.py` from the extracted package using Python 3 and SymPy (see `requirements.txt`). The code symbolically checks the critical deleted-matching entry, existing-edge decomposition, same-side transition polynomial, and negative discriminant. It also checks the polynomial sign brackets controlling the comparison with intact complete bipartite networks.

Recorded successful execution:

`VERIFY_OK: 3 symbolic orbit identities; nonnegativity certificates;  10020 exact direct matrix entries for n=3..11, 5 steps per n`

For every integer \(n=3,\ldots,11\), the checker independently builds the \(2n\)-vertex graph Laplacian, expands the RK4 matrix with exact rational arithmetic, and compares each entry at five rational timesteps to its spectral orbit expression. It additionally compares full-matrix nonnegativity with the claimed threshold on both sides of that threshold. It is not an exhaustive test of all integers or real steps, and the claimed all-parameter theorem relies on the explicit analytical sign proof in `RESULT.md`.

The method applies only to completed classical RK4; this is not an independent mathematical certification.
