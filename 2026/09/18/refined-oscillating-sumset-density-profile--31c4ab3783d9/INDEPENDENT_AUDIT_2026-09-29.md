# Independent audit — 2026-09-29

Record: `2026/09/18/refined-oscillating-sumset-density-profile--31c4ab3783d9`  
Assigned and audited source tree: `d3091e44d2a00f69b6d4eeb927e4903b4d4fc5cd`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `c77e3265b763707aa13279859c9891a6450d457b`  
Disposition: **passed**

## Correctness

**independently_supported**. The refinement of Leonetti's CRT construction checks. For a stage with coordinate densities eta_i, the relevant bad sumset is the union of the all-in box and the r boxes with exactly one coordinate outside; its exact density is prod eta_i + sum_j (1-eta_j) prod_{i!=j} eta_i. Sending all eta_i to 2 delta gives r(2 delta)^(r-1)-(r-1)(2 delta)^r, exactly the advertised improvement over the crude (r+1)(2 delta)^(r-1) union bound. The passage from stage-period counts to lower asymptotic density uses the same rapidly growing CRT blocks as the source construction, so endpoint errors vanish. Substituting delta=alpha^(1/r) yields the stated Lambda(alpha) bound. Independently optimizing its logarithm gives the stationary equation (log 2) r^2+r-log(1/alpha)=0 and reproduces the stated alpha*sqrt(log(1/alpha))/(2 sqrt(log 2))*exp(2 sqrt(log 2*log(1/alpha))) asymptotic. The lower bound Lambda(alpha)>=2 alpha is also valid here: if lower density of A+A were below 2 alpha, Kneser's theorem would make A+A eventually periodic; an eventually periodic set has equal upper and lower densities, contradicting the required upper density one.

## Originality

**qualified_supported**. Leonetti's July 2026 preprint is the direct prior work and supplies the oscillating-density CRT family and the looser lower-density estimate. Current targeted searches found no public source giving this exact overlap count, the optimized density profile Lambda(alpha), or the resulting log Lambda/log alpha -> 1 refinement. Bienvenu and older density-sumset work concern related projection/density phenomena rather than this profile. The originality claim is therefore accepted narrowly as a sharpened analysis of a very recent construction. An unpublished Ruzsa manuscript mentioned in the surrounding literature remains inaccessible and is not claimed to have been read.

## Scientific value

**meaningful_quantitative_refinement**. The record converts a qualitative negative result into a much sharper asymptotic profile for how small the lower density can be while the sumset upper density is one, and pairs it with the classical 2 alpha floor. The main value is the asymptotically near-linear exponent, not merely a constant-factor improvement at fixed r.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/refined-oscillating-sumset-density-profile--31c4ab3783d9
- https://arxiv.org/abs/2609.20206
- https://arxiv.org/abs/2602.19014
- https://arxiv.org/abs/2502.09438
- https://arxiv.org/abs/1902.02512
## Limitations

- The theorem sharpens one specific CRT construction and does not identify the exact extremal function Lambda(alpha).
- The optimized statement is asymptotic as alpha tends to zero; finite-alpha optimal choices of r are only bounded by the displayed discrete minimum.
- The source problem and Leonetti construction are very recent, so concurrent unindexed refinements cannot be excluded.
- The unpublished Ruzsa manuscript referenced in the surrounding literature was not accessible and was not treated as read evidence.
