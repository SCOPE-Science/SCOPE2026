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

# Reproduction of algebraic evidence

Execute `python verify_commuter.py` using Python 3, SymPy and NumPy in the same directory. The script reads no external files and checks the normalized characteristic polynomial identity exactly, the endpoint derivative, the stationary-point resultant, the radical optimal fraction, both exact eigenvalue-one invasion crossings, and two rational demonstrations. The actual run returned `VERIFY_OK` with limiting minimum \(p_*=0.3178372451957822\), normalized spectral minimum \(0.8836634939894802\), and invasion fractions approximately \(0.1420008375225536\) and \(0.5761809806592646\).

The code also compares finite grids of eigenvalues for six parameter settings; these are tests of the computations, not a proof of absence of other critical points. The proof of uniqueness for **all** valid parameters is the sign argument from the exact characteristic quadratic in `RESULT.md`. The script's reproducibility depends on the named third-party Python libraries; no network fetch or original paper file is required to run it. The scientific scope excludes periodically switched infection matrices, the singular fully commuting case, and nonlinear threshold dynamics exactly at equality.
