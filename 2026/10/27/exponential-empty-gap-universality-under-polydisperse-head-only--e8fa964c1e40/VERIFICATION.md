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

# Reproducibility and proof checks

The theorem is analytic. To reproduce the finite continuum tests, install NumPy and run `python reproduce_gap_law.py` from the extracted package. The code enumerates space-time Poisson proposals, implements head-only acceptance using an exact interval union, and computes all maximal uncovered gaps inside a central observation interval.

At constant head intensity \(R=1\) and \(t=2\), a two-length law \(0.17/1.7\) with asymmetric orientation probability \(0.3\) gave 35,196 sampled gaps and mean length 0.491605 versus the theoretical 0.5. The measured length-weighted tail ratios at thresholds 0.1, 0.3, 0.6, and 1.0 were 0.816012, 0.543597, 0.296893, and 0.132783, versus 0.818731, 0.548812, 0.301194, and 0.135335.

For a time-dependent head input \(R(s)=2s\), with exposure \(\Lambda(1.5)=2.25\), a two-length law \(0.15/2\) and orientation probability \(0.82\) gave 20,637 sampled gaps and mean 0.445951 versus the theoretical 0.444444. Measured tail ratios were 0.799412, 0.511936, 0.262605, and 0.107785 versus 0.798516, 0.509156, 0.259240, and 0.105399. Both scripted scenarios pass the stated tolerances.

The decisive mathematical checks are the independent Poisson split into head locations inside, left, and right of the tested interval, the independent half-line killing construction, and the identity between empty-interval probabilities and count-intensity gap lengths. Simulations do not prove distributional identities, and the finite observation window does not implement the infinite line literally. No external scientific validation has been performed.
