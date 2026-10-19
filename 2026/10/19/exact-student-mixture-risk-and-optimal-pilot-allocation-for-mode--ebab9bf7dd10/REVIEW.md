# Scientific review

## Correctness — PASS

For a fixed pilot, the exact without-replacement correction identity gives conditional unbiasedness and the finite-population factor \((N-a)(N-B)/(N^2(B-a))\). Independent Gaussian nonpilot rows reduce the conditional error to a normal scale mixture. Gaussian OLS and a Schur complement produce the exact \(\chi^2_{a-p+1}\) denominator for every projection; Cramér–Wold justifies the full Student-mixture vector law. The beta integral proves all moment boundaries, including divergence, and the derivative polynomial proves the single budget minimum. Reproducibility checks passed 4,675 tests; universal statements are analytic, not empirical.

## Originality — PASS, with residual bibliographic risk

The originating 2026 model-assisted stochastic-gradient paper states the difference estimator and general fixed-prediction covariance identities, but its accessible full text and kernel-ridge appendix do not state the exact Gaussian pilot-OLS mixture, all moments or the finite-population budget-optimal split. Blanchet et al. (2023) analyze Sobolev nonparametric moment estimation; Stanley et al. (2026) analyze multifidelity pilot covariance uncertainty; neither establishes the present scalar Gaussian finite-population gradient law. Sanguiao Sande and Zhang (arXiv:2003.11423, §2.1 Eq. 1) already give the exact general single-split estimator with weighted OLS, and Riaño (2026; arXiv:2609.04082, §§3–4) explicitly acknowledges it, and supplies a general variance decomposition for a different model-assisted estimator; neither published statement gives this Gaussian OLS error law, moment classification or optimized finite-sample pilot split. The underlying OLS Student distribution, inverse-Wishart moment threshold, sample-splitting and Horvitz–Thompson variance formulas are classical and **not** claimed original. Sitter (1997) discusses a related two-phase regression survey estimator in the accessible abstract; a potentially equivalent unindexed specialized result in that or other survey literature remains a risk. The novelty assertion is limited to the assembled exact distribution, moment profile and sharp allocation comparison for this specific algorithmic specialization.

## Mathematical value — PASS

The source method spends actual gradient evaluations fitting a model to reduce subsequent correction noise. The theorem isolates an otherwise hidden heavy-tail danger at training sizes near feature dimension, computes precisely when the extra modeling expense is worthwhile at equal gradient-query budget, and gives an exact allocation rule rather than relying on a heuristic pilot fraction. These are natural resource and reliability questions for the source's two-stage estimator; the finite-sample moment classification is relevant before any asymptotic SGD theory is invoked. The result makes no unjustified runtime or regularized-model claims.

## Limitations and next validation

A no-intercept OLS specialization of the stated abstract model-assisted architecture, not its kernel-ridge experimental variant; independent isotropic Gaussian features and Gaussian noise; fixed scalar gradient at one iterate; equal gradient-observation budgets only. An independent literature audit remains outstanding, including specialized survey regression treatments unavailable in full text.

Self-review: passed. Independent audit: not yet performed.
