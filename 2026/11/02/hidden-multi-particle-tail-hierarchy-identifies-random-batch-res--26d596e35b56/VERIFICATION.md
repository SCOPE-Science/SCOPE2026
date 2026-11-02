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
# Verification details

The proof uses the unique two-sided marked Poisson stationary construction, the age process generator for square-free products, exchangeability, classical symmetric stable tails with the specified Fourier convention, dominated convergence using all finite joint age-product moments, and triangular binomial inversion. The analytic arguments cover every fixed finite \(N\ge2\), every \(0<\alpha<2\), and every nonempty random-batch law without numerical discretization.

Run `python3 verify.py` from the containing directory. The script has no nonstandard dependencies. The actual saved script passed **696 exact rational and numerical consistency checks**: complete subset enumeration of hit probabilities, exact reconstruction across several deterministic and random size laws for particle numbers up to nine, factorial moment recursion, envelope and endpoint formulas, and the Cauchy-flight limit with a fully shared Poisson clock. These checks do not establish the asymptotic theorem independently and cannot substitute for its proof.

All source comparisons are limited to the explicitly described accessed content; full literature priority and independent experimental or mathematical verification are not claimed. No independent audit has been performed.
