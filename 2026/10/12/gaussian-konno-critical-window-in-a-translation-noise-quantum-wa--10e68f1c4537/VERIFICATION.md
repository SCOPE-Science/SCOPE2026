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

# Reproducible numerical checks

Run `python verify_crossover.py` from the extracted package with NumPy 1.24 or newer. The script reconstructs the three-Kraus density-matrix channel independently of the binomial-convolution formula for three coin angles, lengths one through six and five classical-step probabilities. For each of those 90 cases it verifies the probabilities against independent convolution (maximum absolute error less than \(2\times10^{-12}\)), checks total mass one, and checks reflection symmetry. These give 270 finite tests. Additional 27 tests cover normalization and low moments of the Konno density at three angles, second and fourth coherent-walk asymptotic moments, a finite critical-window binomial moment computation, and a strict sign check for the fourth cumulant. The checked output was `VERIFY_OK 297 independent Kraus/mixture, Konno moments, critical moments`.

The analytic theorem is established in RESULT.md, not by these samples. A finite comparison cannot certify a limit law, absence of hidden literature, or correctness of every untested parameter. No independent validation or external certification was performed.
