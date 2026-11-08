# Review: A hidden co-occupation threshold below fitness condensation

## Correctness — PASS

The exact single-site generator has birth rate \(\ell n+b_\zeta(\ell)/v\), death rate \((1+\zeta)n\), and total-clearing rate \(r(\ell)\). Stationary first and factorial-second moments satisfy respectively \((d+r)m_1=a\) and \((2d+r)m_2=2(\ell+a)m_1\), with \(d=1+\zeta-\ell>0\) and \(a=b_\zeta/v\). These yield the stated integral after multiplying by \(v\) and taking \(v\to\infty\). The self-consistency denominator is uniformly positive, and the density is bounded for every \(0<\nu<1\). Endpoint comparison establishes the sharp integrability condition \(2\nu<1\). At the marginal exponent a two-sided comparison proves the coefficient \(4/C^2\); above it endpoint rescaling yields the integral \(J_\nu\) and its explicit beta-integral value. A standalone exact-rational and independent truncated-chain test supports the algebra and numerical constants; it is not an infinite-proof certificate.

## Originality — PASS, qualified

The direct motivating source, P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates* (arXiv:2311.12414v1, 2023-11-21), is inspected through its site master equation, stationary mean formula and condensation discussion. It does not identify the finite-mean divergent *within-site* integrated second-factorial-moment phase at \(\nu=1/2\). S. Kapodistria, T. Phung-Duc and J. Resing, *Linear birth/immigration-death process with binomial catastrophes* (2015 preprint), Lemma 5.4, already provides the general stationary factorial-moment formula for total catastrophes. Its pointwise consequence is expressly not claimed as novel; it does not classify a self-consistent continuous-fitness integral or its critical exponents. P. Grange's earlier 2019 resetting work treats a different resetting mechanism. Related disordered zero-range processes are not the same local-clearing model. The principal residual risk is that an unlocated later paper already integrates these general moment formulas or proves a stronger encompassing result; publication priority is not certified.

## Mathematical value — PASS

The model's known density-condensation boundary is \(\nu=1\). A separate \(\nu=1/2\) boundary for the natural number of ordered pairs co-occupying a site predicts diverging local crowding while the average population stays finite. The threshold and coefficients do not depend on the detailed fitness-density profile, subject to the stated endpoint assumptions. This is a physically motivated phase distinction, not an arbitrary numerical slice or merely a restatement of known pointwise moments. The statement is intentionally restricted to diagonal observables and an iterated limit; it does not advertise finite-network variance or new distributional laws.

## Closest sources and limits

- Grange (2023), arXiv:2311.12414v1, especially generating-function equation (31), stationary formula (44), and Section 5.2: the exact underlying model, first-moment condensation and ownership of the baseline object.
- Kapodistria–Phung-Duc–Resing (2015), Eurandom Preprint 2015-006, Lemma 5.4: generalized local factorial moments with total catastrophes, covering the unintegrated algebra.
- Grange (2019), arXiv:1910.05991: earlier global-reset and nonconserving zero-range treatment, not the same local-clearing fitness asymptotics.

Self-review: passed. Independent audit: not yet performed.
