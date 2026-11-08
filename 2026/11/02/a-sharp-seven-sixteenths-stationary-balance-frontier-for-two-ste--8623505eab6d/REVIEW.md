# Independent mathematical audit

## correctness

PASS

Starting from the actual frozen coefficients c0=(3κ−1)/(3−κ), c1=4(1−κ)/(3−κ), β0=2κ²/D, β1=4κ/D, β2=2/D, D=(3−κ)(1+κ), the 2×2 Markov projector reduces the first coordinate exactly to x_t=[x0+tβ2x∞]/[1+tβ2], x0=c1u+c0v and x∞=(1+κ)²m−2κu−κ²v. Since both interpolation weights are positive, all t>0 and all vertices (u,v)∈[0,1]² are in [0,1] exactly when both endpoint affine functions preserve that square. The x0 test gives κ≥1/3. The stiff endpoint is minimized at u=v=1, yielding (1+κ)²(1−m)≤1; the maximum at u=v=0 then also ≤1 because m≤1/2. Solving the interval nonemptiness gives m≥7/16; violations at small or large finite t explicitly witness necessity. Independent rational matrices and endpoint comparisons gave CASE2_OK. Finite checks are corroboration of the all-history algebraic reduction.

## originality

PASS

The named optimized two-step A-/L(κ)-stable family and its coefficients are prior work, not claimed novel. The exact stationary-mass-dependent unconditional simplex preservation of the coupled two-state system with arbitrary two independent probability histories differs from scalar decay positivity for a specified starter and generic SSP monotonicity results. Main Jensen–Ketcheson–Lóczi 2026 preprint accessible as abstract but full text inaccessible through arXiv and OA, with Oxford returning vpn_disconnected, so its appendices could conceivably imply this special case; this is an explicit residual originality risk, not a fabricated definitive negative finding.

## value

PASS

A complete sharp transition between feasible and infeasible positivity-preserving methods under strong Markov generator imbalance is mathematically and numerically meaningful. Quantifiers over all simplex histories and all positive steps make the seven-sixteenths boundary more than a small numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
