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

# Verification and scope

The proof in `RESULT.md` establishes first-passage recurrence, a bounded harmonic boundary-value problem, the Markov property in spatial levels, independent exponential interval lengths, and a coupling proof of the marked point-process limit. Its limit holds after all locations have been painted, with fixed positive propulsion speed and sign-flip rate.

Run `python verify.py` with NumPy and SciPy. It independently solves the original backward generator's finite-difference equations and compares them to the exact first-passage orientation probabilities, checks the matrix-exponential kernel, and verifies the singular scaling of positive and negative paint runs. The check reported a maximum absolute grid error below \(10^{-5}\) over the stated nine sample points. These tests cannot by themselves prove recurrence or Poisson convergence; those follow from the analytical arguments.

No independent audit has been performed. General results for Markov-modulated Brownian ascending ladder phases are prior work; the assessed assertion is the explicit marked-island limit, not Markovianity alone.
