# Scientific review: effort-driven shared–pooled richness covariance transition

## Correctness — PASS

The two-survey occupancy law is precisely stated: each of two surveys contains \(n\ge1\) independent uniform draws from the same set of \(m\ge2\) species. Equations (5)--(7) in `RESULT.md` reconstruct diagonal and off-diagonal species-level covariances, and yield the displayed finite covariance exactly. The ratio \(R_x\) is strictly increasing by an explicit derivative argument; strict signs at small and large effort and irrationality of \(\sqrt{(m-1)/m}\) exclude an integer equality. A fixed-ratio expansion around \(n\sim cm\), together with the unique positive root of \(e^c=1+2c\), proves the limiting threshold. Direct exact enumeration of independent paired surveys reproduced 25 finite cases, independently of the closed-form covariance. These tests support but do not replace the proof. The asymptotic statement is a limit of the discrete threshold, not an assertion of finite-\(m\) equality.

## Originality — PASS, with a residual search risk

Chao et al. (2005, online 2004-12-17) give the ecological shared/pooled incidence counts and their ratio, plus compositional-similarity estimators. The inspected complete article does not provide covariance of the two count variables across repeated equal-source uniform surveys or the one-switch length law. Colwell et al. (2012) derive individual richness rarefaction means and variances, not this joint two-survey covariance. Published occupancy results on \(\operatorname{Cov}(K,K_r)\), consecutive discoveries and occupied-indicator precision concern observables different from \((|A\cap B|,|A\cup B|)\); neither their statements nor direct implications give the strict survey-length classification and the constant \(\alpha\). The comparison also explicitly considered those stronger-coverage and equivalent-formulation possibilities. There remains a credible risk that a classical two-sample occupancy reference has the same identity under alternative vocabulary; no claim of exhaustive global novelty or independent assessment is made.

## Mathematical value — PASS

Shared richness and pooled richness are the numerator and denominator counts underpinning ecological incidence similarity. Their covariance determines part of the joint uncertainty of these basic counts and cannot be inferred from either mean alone. Even in a homogeneous community under independent identical sampling, changing only survey effort reverses the covariance sign. The strict single transition, no-integer-tie theorem and universal asymptotic threshold near \(1.256431\,m\) provide a concrete sampling-design boundary rather than an arbitrary finite instance. This does not establish confidence intervals from noisy field data, and extension to heterogeneous species or unequal independent survey lengths is open here.

Self-review: passed. Independent audit: not yet performed.
