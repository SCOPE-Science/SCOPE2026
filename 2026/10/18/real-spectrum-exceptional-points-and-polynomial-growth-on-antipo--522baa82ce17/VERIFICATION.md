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

Run `python verify_antipodal_pt.py` with NumPy and SymPy. The checker reconstructs the ring Hamiltonian and reports: five symbolic characteristic-polynomial factorizations, five exact endpoint Jordan-nullity patterns, five selected interior Jordan eigenspace checks, 272 numerical non-antipodal first-order perturbation checks, and 112 real-spectrum checks below the complexification threshold. It checks finite matrices only. The proof for every \(m\ge2\) is the reflection/tridiagonal argument in RESULT.md; no finite computation is asserted to certify infinitely many sizes.

Time evolution means the matrix exponential \(e^{-itH}\) in the Euclidean operator norm. The \(\Theta(t)\) and \(\Theta(t^2)\) statements follow analytically from exact Jordan-block sizes, not numerical propagation. Independent scientific review or replication has not been performed.
