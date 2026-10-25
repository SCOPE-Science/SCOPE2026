# Independent mathematical audit

## correctness

PASS

For iid Poisson(lambda), R=|X-Y| and t=2lambda. Skellam Bessel recurrence yields ER=t r(t), E R²=t, r=e^-t(I0+I1), hence Var(R)-ER=t[1-r-tr²]. Strict Turán log-concavity implies I_k/I0<(I1/I0)^k for k>=2, giving r>1-u, u=I1/I0. Every positive crossing of H=r+tr²=1 has H′=r²(1-r-u)/((1-r)(1+u))<0. Since H>1 near t=0 and H→2/pi<1 at infinity, there is exactly one zero, with under- then overdispersion. Independently recomputed high-precision root t≈3.4778659345393811113, lambda≈1.73893296726969055. The source rational-series verifier supplies certified 3.4778<t*<3.4780. No unequal-rate claim.

## originality

PASS

Best-of-knowledge noncoverage is supported by the statement-level comparisons below; this is not a proof of absolute bibliographic novelty.

## value

PASS

A natural statistic exhibits a sharp phase reversal of dispersion relative to its own expectation despite both individual Poisson order statistics being underdispersed. Exact global uniqueness, orientation and certified cutoff are motivated and nontrivial; not merely a numerical root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
