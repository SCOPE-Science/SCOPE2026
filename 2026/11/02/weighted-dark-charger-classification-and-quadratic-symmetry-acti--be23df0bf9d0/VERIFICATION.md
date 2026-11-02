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

The included `verify_weighted_dark.py` was run with Python, NumPy and SciPy; it reported `PASS: 1800 independent numeric matrix, leakage and local-product readout assertions`. The executable constructs the full \(8\times8\) Hamiltonian and tests 300 independent choices of the coupling strengths (including equality), detuning, duration, initial battery phase and excited population, and charger state. For each choice it compares full-matrix reduced populations and generic arbitrary-charger leakage with independent closed forms. It explicitly computes normalized conditional charger density matrices, constructs product measurement axes orthogonal to the appropriate Bloch vectors and tensor contractions, and checks conditional excited probabilities of all 4 outcomes. For vanishing-probability branches the conditional state is undefined and is excluded. Tests use numerical tolerance, not infinite proof; full quantification relies on the preceding algebraic Rabi-block and Pauli-expectation derivations. The code requires `numpy` and `scipy`, and contains no external files or network calls.
