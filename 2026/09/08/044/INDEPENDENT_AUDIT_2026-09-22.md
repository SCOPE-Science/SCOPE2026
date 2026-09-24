# Independent three-axis audit — record 2026/09/08/044

Review date (UTC): 2026-09-24  
Reviewer: separate AI audit under the SCOPE historical-record campaign

## Source identity

- Source path: `2026/09/08/044`
- Audited source tree: `3c14999fd5e63616dd83e15010fce69caf8eada7`
- `RESULT.md` blob: `8017c9327168f4f770a02215a27b4bd06b13ac80`
- Historical audit files were not used as the proof of this campaign verdict.
- No repair to `RESULT.md` is required.

## Claim audited

For every connected simple graph on 4, 5, or 6 vertices, the associated right-angled Coxeter group's spherical growth series is computed exactly by the Steinberg denominator from the graph's clique vector. The record gives the complete 6/21/112-class census, finite/subexponential/exponential regime counts, rigorous growth-rate intervals, and asserts that the minimum exponential growth rate in each stratum is the golden ratio, with exactly 1/2/3 minimizers for n=4/5/6 and next exponential rate at least 2.

## Correctness — PASS

I independently enumerated connected unlabelled graphs on 4, 5, and 6 vertices and obtained exactly 6, 21, and 112 isomorphism classes. For each graph I independently computed its clique counts and the exact polynomial
`M_G(t)=sum_k (-1)^k c_k t^k (1+t)^(omega-k)`. This reproduces the claimed regime counts: finite/subexponential/exponential = 1/2/3 for n=4, 1/2/18 for n=5, and 1/3/108 for n=6.

Independent positive-root calculations over all 139 polynomials reproduce the claimed minima. At n=4 the unique exponential minimizer has `M=1-t-t^2`, hence growth rate phi. At n=5 there are exactly two minimizers, with denominators `1-t-t^2` and `(1-t)(1-t-t^2)`. At n=6 there are exactly three, with denominators `1-t-t^2`, `(1-t)(1-t-t^2)`, and `(t^2+t-1)^2`. In every stratum the next exponential rate is 2. The displayed n=4 and n=5 witness edge sets independently give the stated clique data and denominators.

The algebraic use of Steinberg's formula is also correct for RACGs: spherical subsets are graph cliques and their finite-parabolic growth polynomials are `(1+t)^k`, giving `1/W_G(t)=sum_k (-1)^k c_k t^k/(1+t)^k`. With nonnegative spherical-growth coefficients, the least positive pole determines the exponential rate. Boundary cases with a root at t=1 do not invalidate the census because the exponential rows have a smaller positive root when one exists, while pure `(1-t)^k` rows are the subexponential cases.

## Originality — PASS, qualified to the literature checked

The novelty is not that the golden ratio can occur as a RACG growth rate. Kolpakov--Talambutsa, *Spherical and geodesic growth rates of right-angled Coxeter and Artin groups are Perron numbers* (arXiv:1809.09591), explicitly gives a small RACG example with spherical growth rate phi and proves the general Perron-or-1 theorem. The surviving claim audited here is the exact complete connected-graph census for n=4..6, including the full denominators, regime split, exact minimizing witness sets, and the next-rate gap.

Terragni, *On the growth of a Coxeter group* (arXiv:1312.3437), proves diagram-order monotonicity and a universal lower bound near 1.13 for non-spherical non-affine Coxeter systems; it does not enumerate the connected-graph RACG strata or determine their exact minimizers. Terragni, *Data about hyperbolic Coxeter systems* (arXiv:1503.08764), tabulates growth for pre-minimal hyperbolic Coxeter systems, a different restricted class rather than all connected graph-defined RACGs on 4--6 vertices. Searches using `right-angled Coxeter`, `small connected graphs`, `growth rate`, `golden ratio`, and the exact 6/21/112 strata did not locate a prior table covering this finite census.

Thus, to the best of the inspected literature, the exact small connected-graph census and minimizer/gap statement are not already tabulated, while the known general theory and known occurrence of phi are explicitly subtracted from the novelty claim.

## Scientific value — PASS

The surviving contribution is a complete exact benchmark over the first nontrivial connected RACG graph strata: 139 isomorphism classes with exact rational growth series and certified growth rates, plus exact identification of all minimum-exponential-growth witnesses and the gap to the next rate. That is useful for regression-testing Coxeter growth computations, checking monotonicity heuristics, and calibrating general lower-bound/minimal-growth results on a finite domain. It is not presented as a new general minimal-growth theorem beyond n=6.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS**, qualified to the literature checked
- Scientific value: **PASS**
- Disposition: **passed**

This is a computational/literature audit, not Lean verification or human expert attestation.
