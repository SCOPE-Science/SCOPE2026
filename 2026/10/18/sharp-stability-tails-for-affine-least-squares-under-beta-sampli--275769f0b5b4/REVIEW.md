# Self-review

## Correctness — PASS
The sample Gram reduction gives an exact identity for \(K_n>t\) as a mean-dependent thin tube around the sample diagonal. Orthonormal coordinates supply the Jacobian \(\sqrt n\), and endpoint localization gives a convergent interior integral, a critical logarithm, or a rescaled finite corner integral. The moment threshold follows from positive two-sided tail asymptotics. Exact event identities and coefficient normalizations were recomputed using the enclosed verifier. Risk: the asymptotic claims require the fixed-parameter limit; finite Monte Carlo alone cannot establish them.

## Originality — PASS
The original Jacobi random least-squares paper determines the stability norm and high-probability sampling rates, not its all-sample-size exact catastrophic tail coefficient. Royen proves a related pure-power small-sample-variance exponent and logarithm; a published three-point Beta-variance classification also covers analogous endpoint competition. Neither determines the *mean-dependent* instability tube coefficient \(C_{\rm bulk},C_{\rm crit},C_{\rm corner}\) for the least-squares norm for arbitrary fixed \(n\). A stronger joint mean/variance asymptotic theorem could subsume this calculation, so novelty is supported by the inspected comparisons but is not independently certified.

## Value — PASS
Random least-squares stability is a numerical conditioning diagnostic: the leading constants quantify catastrophic sample clustering rather than only high-probability boundedness. The exact boundary \(p<\min(n-1,n\alpha,n\beta)\) distinguishes finite mean, variance and higher moments, including the uniform-sampling thresholds of three and four points. The endpoint contribution also identifies which kind of beta sampling density dominates ill-conditioning. Scope is strictly affine polynomials and fixed beta parameters, not general polynomial degree or uniform finite-sample bounds.

## Closest literature and limitations
Xu–Zhang (arXiv:2407.10221), Royen (arXiv:0810.1572), Cohen–Davenport–Leviatan (arXiv:1111.4422), Jebalia–Karoui (arXiv:2208.02891), and the public three-sample Beta-variance phase result were compared at the level of hypotheses and implications. The sample-variance exponent is old; the new claim is the exact mean-dependent coefficient for affine least-squares stability. Residual risk: equivalent results under joint small-ball or generalized Vandermonde-conditioning terminology.

Self-review: passed. Independent audit: not yet performed.
