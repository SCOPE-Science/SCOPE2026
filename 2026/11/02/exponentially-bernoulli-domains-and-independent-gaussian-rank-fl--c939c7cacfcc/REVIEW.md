# Scientific review: exponentially Bernoulli domains and Gaussian rank fluctuations

## Correctness — PASS

The cyclic-gap argument gives the exact idempotent rank coefficients, with the rank-one correction handled separately. The finite analytic identity for \(A_m(u)\) follows by extracting coefficients from a logarithm whose two reciprocal roots are \(\lambda(u)\) and \(\lambda(u)^{-1}\). The binomial transform gives the precise two-variable polynomial \(H_n(s,u)\), including the empty map. These identities yield exponentially controlled comparison of *every individual domain subset* with Bernoulli weights, not merely a limit for domain cardinality. Local complex dominance of the first exponential term in \(H_n\), plus the explicit first two derivatives of \(\log\lambda(e^v)\), proves the claimed joint central limit and independent residual. The independent `verify.py` checks 56 configurations, including exhaustive direct partial-map enumeration for sizes one through six; finite tests are corroboration and not an infinite proof.

## Originality — PASS relative to inspected sources

Li–Fernandes (arXiv:2207.12823, 2022), specifically Section 3, Lemmas 3.2 and 3.4, gives rank-by-rank idempotent enumeration. Fernandes–Gomes–Jesus (2011) supplies Lucas-number total counts and the binomial partial-map transform. Umar (2011) treats all partial maps, not uniformly sampled idempotents. Therefore the exact finite enumeration and its generating function are mathematical inputs and are **not** claimed as new. The assessed claim is the exponentially strong total-variation product law on the whole domain subset and the joint Gaussian rank/domain fluctuations with an independent Gaussian residual. Searches for equivalent probabilistic formulations, Gaussian/Lucas asymptotics, and published matching research findings located no covering assertion. Because known exact counts permit subsequent asymptotics by analysis, a differently worded published limit remains a priority risk.

## Mathematical value — PASS

The natural random object is a uniformly chosen idempotent in a classical finite transformation monoid. In general, a random idempotent's defined set need not resemble an independent per-point choice. Here its *entire domain subset* has exponentially small total-variation distance from a product law, while the dependent image rank has a precise bivariate Gaussian limit. The Gaussian residual decorrelation separates the effects of random domain selection from the internal cyclic-fiber structure. This goes beyond repeating a finite counting table and is useful for quantitative random-structure questions and sampling.

## Boundaries and residual risks

The model uses cyclically nondecreasing partial transformations and counts the empty map. Asymptotic statements hold as the finite-chain size tends to infinity; there is no assertion of exact coordinate independence at finite size, a local CLT, or universality under changed sampling measures. Possible equivalent limit theorems in older analytic-combinatorial literature could change publication priority. Independent scrutiny is still required.

Self-review: passed. Independent audit: not yet performed.
