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

The supplied proof is analytical. To reproduce its finite-state checks, run `python check_star.py` with NumPy and SciPy installed, and compare stdout with `check_output.txt`.

The checker constructs the independent finite \(2m\)-state Markov generator from the model transitions. It solves \((sI-Q)u=r\) for absorption transforms and \((-Q)v=\mathbf{1}\), \((-Q)w=2v\) for moments; these are independently compared with the theorem's product and harmonic-number formulas. It also directly evaluates the finite characteristic functions in three large system sizes and three fixed-backscatter cases against the specified asymptotic characteristic functions.

The completed checks compare 720 transforms, 180 mean/variance pairs, twelve crossover configurations at three Fourier arguments each, and three fixed-backscatter large-\(N\) configurations. Largest finite-transform discrepancy: \(1.92\times10^{-15}\); largest finite mean discrepancy: \(6.82\times10^{-13}\); largest finite variance discrepancy: \(1.46\times10^{-10}\). Each finite test passed the stated checker tolerances. The asymptotic comparisons converge numerically; the theorem's infinite-size assertion rests on the characteristic-function proof rather than these numerical examples.

The historical-priority assessment is conditional on the cited and searched literature, not a claim of uniqueness or independently certified priority. Independent audit: not performed.
