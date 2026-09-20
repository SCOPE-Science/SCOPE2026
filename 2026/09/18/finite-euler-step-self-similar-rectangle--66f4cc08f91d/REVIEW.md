# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof uses the exact endpoint equation and Green kernel stated in arXiv:2609.20674v1 together with Proposition 2.4's two ingredients: $b_n(t)\asymp t^{-1}$ and integrability of every other endpoint. Negativity of the Green kernel makes all endpoints nonincreasing, so an elementary tail-integral estimate upgrades integrability to $x(t)=o(t^{-1})$. Substitution into the exact $b_n$ equation then yields $b_n'=-c_n b_n^2(1+o(1))$, from which the endpoint, mass, and weighted-moment constants follow. The $L^1$ similarity profile follows from the scaled endpoint limits. The Green-field limit follows from the uniform kernel expansion $tK_m(y/t,z/t)\to-\min(y,z)$ on bounded sets.

Potential failure modes were checked explicitly: the constant in the rightmost Riccati law is $c_n$ rather than a sum of heights because every inner endpoint is $o(b_n)$; the moment constant is $1/c_n$ rather than $1/c_n^2$ because the outer contribution is $c_n b_n^2$; and the similarity stream function scales as $t^2G$ because the kernel contributes one power of $t^{-1}$ and $d\theta$ contributes another. A direct numerical integration of the exact endpoint dynamics is consistent with all three constants and with the scaled Green field.

## Originality

**PASS, to the best of our knowledge.** The source paper was read through its full HTML, including the step-function evolution and Proposition 2.4. It states only two-sided comparability for the mass and rightmost endpoint, an upper bound for the weighted moment, and integrability of the other endpoints; it does not state the exact constants, the rectangular similarity profile, or the limiting rescaled Green/transport field.

Searches covered the source title and arXiv identifier together with terms such as exact asymptotics, self-similar step functions, rightmost endpoint, $1/t$ decay, and rectangular profile. No source-specific correction or comment containing these conclusions was located. Repository overlap searches by source identifier and by equivalent mathematical terminology also found no existing SCOPE record.

The closest prior literature inspected was Elgindi–Murray–Said, *On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications* (arXiv:2211.08418; Ann. Sci. Éc. Norm. Supér. 58 (2025)), which establishes qualitative relaxation to finite-jump states, and Cao–Fan–Qin, arXiv:2608.16755, which treats the distinct $m=3$ problem. The freely accessible journal sample for the former contains its abstract and introductory theorem statement but not the full body; the arXiv abstract was also inspected. This leaves a residual possibility that an equivalent quantitative asymptotic is buried in the unavailable portion of that publication or in older literature under different variables. The source paper itself cites the earlier relaxation result as background and nevertheless presents its $t^{-1}$ step estimates only up to comparability, which weighs against direct prior coverage, but does not eliminate that residual risk.

The originality claim therefore excludes the scale-invariant Euler reduction, finite-step transport, Green-kernel formula, endpoint monotonicity, regulated-profile relaxation, and generic similarity-variable techniques. It is restricted to the exact source-specific finite-step limits and the resulting explicit self-similar rectangle/Green-field mechanism.

## Value

**PASS.** The result converts the estimates that underpin the source's finite-step dynamics into a sharp asymptotic description. The universal law $t\|g(t)\|_{L^1(0,\pi/m)}\to1$ is independent of all step heights and positions, while the only parameter retained by the leading similarity profile is the rightmost height $c_n$. The explicit limiting field $V_*(y)=y(c_ny-1)$ explains dynamically why the two similarity jump locations are stationary. This gives a compact asymptotic model for the building blocks used in the source paper's nonlinear construction and distinguishes leading-order universal behavior from finer initial-data dependence.

## Limitations

The result is confined to finitely many positive, disjoint ordered intervals for $m\ge4$. It does not extend the law to arbitrary regulated data, infinite stacks, or $m=3$, and it does not quantify the convergence rate. Numerical verification is supportive only and is not independent validation.
