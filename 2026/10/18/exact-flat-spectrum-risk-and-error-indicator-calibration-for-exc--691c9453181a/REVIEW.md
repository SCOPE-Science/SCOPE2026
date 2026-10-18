# Self-review

## Correctness — PASS
The statement specifies \(n\ge r\ge1\), \(k\ge1\), the raw standard-Gaussian sketch, \(A=\lambda P\), and \(c=f(\lambda)\ne0\) with \(f(0)=0\). The proof verifies each exact Nyström projector, reduces each left-out residual to a chi-square energy, then computes pair covariance by conditioning on the other \(k-2\) probes and integrating the squared angle of two independent Gaussian directions in \(r-k+2\) dimensions. The variance and sample-error expectation are algebraic consequences; \(k\ge r+1\) is deterministic. Exact rational and seeded Gaussian checks pass, but the proof—not simulation—supports all dimensions and budgets.

## Originality — PASS with residual bibliographic risk
The closely related 2026 FlexTrace paper defines the estimator and gives bias/MSE bounds, not the computed flat-spectrum covariance in its inspected algorithm/theory. The foundational 2023 XNysTrace work defines the posterior error indicator and proves a general correlation-dependent calibration identity. Here the nontrivial additional input is the exact correlation \(1/(r-k+4)\) and its all-budget closed-form consequences; it does not claim the generic estimator or calibration identity as new. Hallman's 2025 XTrace variants and the 2023 normalized-probe option have different formulations. Earlier unindexed special-case calculations remain possible; database search alone is not taken to certify uniqueness.

## Mathematical value — PASS
Flat nonzero eigenvalues are a natural benchmark where the Nyström approximation reaches the true matrix exactly at the rank. The surprising quantitative issue is that the *raw Gaussian* exchangeable leave-one-out estimator still has nonvanishing absolute risk at this budget while its usual error indicator becomes arbitrarily optimistic in expectation as rank grows. A single additional probe removes this error. The exact calibration factor distinguishes error estimation from sketch reconstruction and directly informs a diagnostic for the published algorithm.

## Source comparisons and limitations
Sources read for mathematical comparisons: Madhavan–Alexanderian–Saibaba (arXiv:2603.05721v1, Algorithm 3.1 and Theorems 3.2–3.5), Epperly–Tropp–Webber (arXiv:2301.07825, equations (8), (9), (16), Proposition 2 and Proposition 5, plus normalization discussion), and Hallman (arXiv:2512.02316v1, Algorithms 1–2 and the related-work section). The two-point spectral assumption and raw unnormalized Gaussian probes are essential. The calibration correction is unbiased for risk only in expectation within this model. No claim is made for arbitrary eigenvalues, concentration, independently certified novelty, or floating-point behavior.

Self-review: passed. Independent audit: not yet performed.
