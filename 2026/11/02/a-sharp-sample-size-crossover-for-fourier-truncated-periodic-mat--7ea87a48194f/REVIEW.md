# Scientific review

## Correctness — PASS

The proof is self-contained once Fourier character orthogonality and standard lattice Riemann-sum convergence are accepted. All quantifiers are stated: fixed dimension \(d\ge1\), smoothness \(\nu>0\), every cutoff \(m\ge1\), every \(N\ge1\), and every joint asymptotic sequence \(N=N(m)\). The diagonal/off-diagonal expectation is exact; shared-index covariance vanishes by Haar conditioning; the pointwise positive-Fourier envelope yields the variance bound. The asymptotic constants follow from integrable, explicitly specified tail integrals. The supplied verifier passed 115 check groups; no infinite conclusion is inferred solely from finite checks.

## Originality — PASS, qualified

The strongest motivating comparison is Barnett–Greengard–Rachh (2023), Section 4, which discusses the random-location Frobenius error and predicts an off-diagonal improvement in a different, nonperiodic Fourier-grid setting. That text does not establish the exact finite-sample formula, uniform relative concentration or critical sample-size law for the periodic covariance spectral cutoff. Bachmayr et al. (2019/2020) address periodization, Fourier eigenvalue decay and equispaced sampling; Puchkin et al. (2023) address empirical covariance estimation rather than deterministic Fourier truncation at iid design sites. Existing general Fourier and degenerate-U-statistic tools supply ingredients, and specialized prior results may exist. The record searches and own-work comparisons did not identify a statement subsuming the complete claimed conclusion. This remains a self-review, non-independent priority judgment.

## Value — PASS

The paper-motivated mathematical gap is whether a large-sample Fourier truncation error exponent remains predictive when covariance matrices are formed at finitely many random sites. The answer has a sharp transition at \(N\asymp m^d\), the scale of the retained Fourier feature count: below it diagonal bias fixes the error exponent, while above it off-diagonal averaging reveals an additional \(d/2\) exponent. The result gives exact constants and a uniform-in-bandwidth concentration guarantee, directly useful when choosing spectral cutoffs and comparing experiments with differing data sizes. It is not a generic restatement of a pointwise Fourier tail bound.

## Closest literature, limitations, risks

The primary scientific source is Barnett–Greengard–Rachh, arXiv:2305.11065 (2023), Section 4 and Conjecture 9. Related sources are Bachmayr–Graham–Nguyen–Scheichl, arXiv:1905.13522 (2019), and Puchkin–Noskov–Spokoiny, arXiv:2308.14739 (2023). The periodic Haar model is not the nonperiodic EFGP algorithm, and no claim is made about nonuniform sampling, other spectral windows, posterior means or operator norms. Search noncoverage does not certify absolute priority; a specialized earlier kernel-U-statistic spectral approximation result could subsume the formula or its limit.

Self-review: passed. Independent audit: not yet performed.
