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

The analytic proof diagonalizes the normalized Choi partial transpose by total spin and proves the spectrum for every spin \(j\ge 1/2\). The negativity formula follows from an exact finite polynomial sum, not from interpolation or numerical fitting. The singularity condition is algebraically equivalent to the negative Pell equation.

The bundled `verify.py` reconstructs the spin matrices, Kraus operators, normalized Choi state and partial transpose for eight spins \(j=1/2,1,3/2,2,5/2,3,7/2,4\), compares all eigenvalues with the theorem, checks the closed negativity formula, and searches the singularity equivalence through \(j=500\). Replaying the packaged file gives `VERIFY_OK spins=8 max_j=4 pell_first=2,14,84`.

The finite replay is a regression check only. It does not certify the infinite family; the infinite statement rests on the Clebsch--Gordan decomposition, the swap parity identity, the closed weighted sum, and the exact Pell transformation given in `RESULT.md`.
