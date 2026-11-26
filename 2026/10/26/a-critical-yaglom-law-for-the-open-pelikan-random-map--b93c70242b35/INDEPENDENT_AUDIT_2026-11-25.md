# Independent mathematical audit

## correctness

PASS

The repaired finding is the critical conditioned-time TV limit from the uniform top cell. The reduction is exact: affine surviving branches preserve within-cell uniformity and the top reset has mass p(1-ε) with cell weights 2^{-k-1}. The top-cell initial law δ₀ satisfies the cited critical survival theorem's moment hypothesis, giving S_{n+1}/S_n→λ=ap. The only mass loss is pε times the top-cell mass, hence the conditioned top-cell mass tends to (1-λ)/(pε)=ε/4. Solving the transition recursion backwards in the cell index gives the limit of each next cell from the preceding two, using the actual time-shifted conditioned masses and the survival ratio. Since q/p=a²/4, the limiting generating function obeys (1-aw+a²w²/4)U=(ε/4)(2-aw)/(2-w), which yields U=ε/[(2-w)(2-aw)]. It has nonnegative coefficients and U(1)=1 for 1<a<2. Finite-set truncation then proves TV convergence; on the disjoint uniform cells the interval and cell TV distances agree. The supplied original survival formula is mathematically consistent: 1-f(z) is a/[2(a-1)] times the leading square root, f has positive coefficients in degrees 1 and 2 excluding another return pole on the leading circle, and h(1)=1 gives removable cancellation in the survival transform. The repair no longer claims the amplitude separately. Independent finite corroboration at ε=1/2 propagated exact rational masses by the stated cell recursion and compared the top-cell masses with coefficients of 1/(1-f) through step 24 and Mu=λu at k=0,…,20; those checks do not prove the limit. Frozen checker and output were inspected, not executed.

## originality

PASS

This PASS is for the repaired total-variation Yaglom limit, not for the original presentation of the sharp amplitude as part of the distinct contribution. A separate Resultary record gives the exact amplitude for a broader initial-law class, including this case, and expressly excludes the full conditional Yaglom distribution. Catalogue dates do not establish priority or provenance. Brevitt–Klages already give the critical quasi-stationary law itself. The new content retained is convergence to that law in TV from the given top-cell start, which requires conditioning, the transition recursion and control of total mass beyond knowledge of the survival probability or fixed point.

## value

PASS

At a specifically identified critical line where the usual R-positive asymptotic is inapplicable, the repaired result determines the eventual survivor distribution, not just the total surviving mass or a stationary candidate. In an infinite countable model the normalized masses could drift to infinity; their explicit probability normalization is substantive. The TV limit also determines the full conditioned interval law, a measurable prediction strictly stronger than the known survival asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
