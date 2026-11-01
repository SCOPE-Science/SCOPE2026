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

# Analytic and numerical verification

The exact probability identity was checked by independent edge-crossing normalization: Gaussian normal scores are centered and divided by an independent radius, and the width-weighted offset has expected Gaussian span \(2\mu_m\). The inequality \(N\ge r(m-r)\) restricts the offset to the expected order-statistic interval. Each edge crosses for an offset interval of length \(|G_i-G_j|\), which gives the same mean as the distribution’s first moment. The cases \(m=3\) and \(m=4\) give, respectively, two section vertices almost surely and the exact tetrahedron probability \(0.288535543072\ldots\) of a four-vertex section.

The included standard-library verifier `verify.py` computes order-statistic integrals and checks exact edge summation for \(m=3,4,5,6,8,10,12\). It additionally checks Gaussian-range-weighted simulations for \(m=4,8,12\) with 90,000 samples each. Program output ends with `ALL_CHECKS_PASSED`.

The expectation asymptotic requires \(\mu_m\sim\sqrt{2\log m}\), a standard Gaussian maximum result. The rare macroscopic law also uses uniform-integrable central order-statistic quantile convergence. The random-exponent law uses \(L^1\) convergence of normalized Gaussian range, exact total variation control of range reweighting, standard Gaussian tail exponents and binomial concentration. None of these infinite steps is inferred from finite numerical enumeration.

No external independent mathematical review has been performed. The theorem is restricted to invariant affine hyperplanes of regular simplices and fixed \(0<q<1/4\).
