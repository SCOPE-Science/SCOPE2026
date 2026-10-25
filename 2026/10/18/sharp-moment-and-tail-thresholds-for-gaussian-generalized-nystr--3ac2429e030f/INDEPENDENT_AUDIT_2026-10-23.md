# Independent mathematical audit

## correctness

PASS

The original RESULT.md proves Q=||z||²+||G^+Hz||² via orthogonal decomposition of the retained column space, with z, G and H Gaussian and independent after conditioning. Integrating the Gaussian least-squares density gives a multivariate Student law with denominator df ν=r-s+2 (verify r-k+1 with k=s-1); it correctly supplies X_d(1+Y_k/V_ν), χ² inverse-power moments, mean d(1+k/(r-s)) when r>s, variance cutoff r>=s+3, and regular-variation constant by independent gamma moments. The pooled frontier and Θ tail follow deterministic positive sum/max inequalities, not independence. In square case the rank-one complementary oblique projection a bᵀ/(bᵀa) yields numerator independent normals and spherical inner-product square Beta(1/2,(n-1)/2); the tail coefficient follows E|Z1 Z2|=2/π. Independent seeded direct refits for 3,500 matrices in a bounded instance reproduced residual quantiles close to an independently simulated χ-ratio distribution. These finite checks only corroborate identities and do not prove the infinite tail.

## originality

PASS

PASS on best knowledge: the diagnostic-specific exact joint distribution and sharp oversampling/moment and square angular frontiers were not found as statements of the inspected abstracts, existing general Gaussian approximation bounds or independent indexed results. Classical Student/F/beta-prime distributions and leave-out estimator definitions are prior; the new claim lies in exact diagnostic identification and interpretation. The motivating 2026 article is only accessible here by its full abstract, not its full proof; this material priority risk is explicit and cannot support a whole-paper assertion.

## value

PASS

The estimators are proposed as practical error diagnostics, and the exact moment boundaries distinguish meaningless mean estimation at no oversampling, infinite-variance estimates with one/two extra left columns, and even heavier pair/twin outliers despite an exact full-sketch fit. This natural failure-mode classification is a nontrivial caution relevant to parameter selection, not a generic restatement of Student tails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
