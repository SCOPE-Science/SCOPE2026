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

# Scientific verification

The standalone `verify.py` program reconstructs two steps of the coin–hypercube unitary, computes the reduced coin states directly from amplitudes and verifies their purities. It does not insert the analytic two-step formula into the propagation. Exact arithmetic comparisons also evaluate the distinct-row/column Haar fourth-moment expression and the dimension-three crossover. Using the fixed seed 20261019 and NumPy, the script performed 40 assertion groups across dimensions 2 through 9 and simulated 36,000 independent Haar coin pairs. All assertions passed; the empirical means agreed with the exact formulas within five Monte Carlo standard errors for each measured purity.

The theorem's proof rests instead on coordinate-flip path-collision enumeration and Haar-moment identities, valid in every integer dimension at least two. The checks do not establish properties of later times, arbitrary graph shifts, non-Haar noise, samplewise monotonicity, or independence from random rather than deterministic initial coin states. No independent audit has been performed.
