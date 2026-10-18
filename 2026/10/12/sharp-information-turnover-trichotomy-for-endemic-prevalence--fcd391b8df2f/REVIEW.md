# Independent mathematical audit

## correctness

PASS

Starting from Fang--Liu--Du reduced SIRM equilibrium equation (19), with k=a/b, u1=σu0 and c=(p+μ)(R0−1)>0, the endemic equation is βI+k u1 I/(1+k u2 I)=c. Its derivative in I is β+k u1/(1+k u2 I)^2>0, so exactly one positive root exists; the partial derivative in k is u1 I/(1+k u2 I)^2>0, giving strict dI/dk<0. Clearing denominators produces βk u2 I²+[β+k(u1−cu2)]I−c=0 and the rationalized positive quadratic root. Comparing signs of d=u1−cu2 proves: d>0 gives kI→c/d; d=0 gives √k I→sqrt(c/(βu2)); d<0 gives I→(c−u1/u2)/β. Independently checked representative parameter triples, exact quadratic residual formula, monotone k values, and scaled limits at k=10^10. Assumes β,u1,u2,k>0 and R0>1; no claims about stability, finite-k eradication, or delay.

## originality

PASS

A very close published Resultary/SCOPE result, "Information-dependent vaccination shifts endemic burden at a fixed invasion threshold" (2026-10-04), on exactly the Fang--Liu--Du endemic equation ALREADY proves strict variation in a,b,u0,u2, including k=a/b monotonicity; the current monotonicity must not be credited as new. That result takes u0→infinity (with k fixed), finding u0 I→Cb/(aσ); its statement and full proof do NOT supply the distinct k→infinity limit at fixed u0, where the k u1/(1+k u2 I) saturation creates three qualitatively distinct behaviors separated by u1=cu2. Fang's original full SIRM paper also gives existence/uniqueness but not the sharp 1/k,1/sqrt(k),positive-floor trichotomy. Accordingly originality survives narrowly in the global information-turnover asymptotic trichotomy, not comparative statics in isolation. Exact close comparison included; specialized older results might encode the same threshold.

## value

PASS

Information growth-to-decay turnover is a natural physical control ratio in the motivating epidemic model, and the ratio of saturation-limited vaccination u1/u2 to endemic drive c is a genuine qualitative regime divider. Unlike a bare derivative sign, the rates and positive floor distinguish when arbitrarily rapid information response can suppress endemic prevalence to zero, when suppression slows at critical balance, and when a positive floor persists. This sharp trichotomy supplies a motivated interpretation not contained in the prior four-parameter monotonicity theorem despite elementary quadratic algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
