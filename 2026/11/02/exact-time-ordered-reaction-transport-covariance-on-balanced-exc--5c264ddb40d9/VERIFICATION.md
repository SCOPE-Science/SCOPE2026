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
The attached `verify.py` independently builds the full Markov generator on 512 configurations for a balanced, lane-anisotropic 3-by-3 periodic exclusion lattice, and on 32 configurations for a circulation-balanced five-site cycle. It builds attachment, detachment, and signed hopping jump matrices and uses sparse exponentiation to calculate the ordered two-time covariance densities. Five density choices and two positive lags yield 40 analytical/numerical comparisons, all passed when executed from the packaged script. Stationary probabilities and the generator's row-sum invariance were also checked.

The verification is finite and numerical. The theorem for arbitrary finite connected balanced graphs is established by the analytical uniform-sector invariance, conditional post-event mixture law and exactly solvable particle-number regression, not by numerically enumerating graphs. Homogeneous positive reaction rates, fixed graph, stationary initialization and circulation balance are essential. No external or independent scientific audit was performed.
