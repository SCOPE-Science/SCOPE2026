# Universal coalescing-pole limits and sharp Laplace-dependence decay

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry geodesic distance \(d\), and let \(U_1,U_2,\ldots\) be independent with continuous probability density \(g\) on \(\mathbb T\), with \(g_0=g(0)>0\). Fix \(\beta>1\) and set \(\alpha=1/\beta\). Choose \(a_n\in[0,1/2]\) with \(a_n\to0\), and suppose \(\delta_n=n g_0 a_n\to\delta\in[0,\infty]\), allowing \(\delta=\infty\). Define, almost surely,
\[
T_{n,0}=(n g_0)^{-\beta}\sum_{i=1}^{n}d(U_i,0)^{-\beta},\qquad
T_{n,1}=(n g_0)^{-\beta}\sum_{i=1}^{n}d(U_i,a_n)^{-\beta}.
\]
Then \((T_{n,0},T_{n,1})\) converges weakly to a finite, nonnegative pair \((X_0,X_\delta)\). For all \(s,t>0\), put \(C_\beta=2\Gamma(1-\alpha)\) and
\[
f_s(x)=1-\exp(-s|x|^{-\beta})\quad(x\ne0),\qquad f_s(0)=1,
\]
\[
J_\delta(s,t)=\int_{\mathbb R} f_s(x)f_t(x-\delta)\,dx
\quad(0\le\delta<\infty),\qquad J_\infty(s,t)=0.
\]
The complete bivariate Laplace law is
\[
\boxed{\mathbb E\exp(-sX_0-tX_\delta)
=\exp\{-C_\beta(s^\alpha+t^\alpha)+J_\delta(s,t)\}.}
\]
Both marginals are positive strictly \(\alpha\)-stable with Laplace transform \(\exp(-C_\beta s^\alpha)\). The ratio of the joint transform to the product of marginal transforms is exactly \(\exp J_\delta(s,t)\); thus it remains meaningful despite infinite marginal means.

For every fixed \(s,t>0\), \(J_\delta(s,t)\) is continuous and **strictly decreasing** in finite \(\delta\ge0\). Its two sharp endpoints are
\[
\boxed{J_0(s,t)-J_\delta(s,t)
=\frac{\beta s t\,\Gamma(2+\alpha)}{(s+t)^{2+\alpha}}\delta^2+o(\delta^2)
\quad(\delta\downarrow0),}
\]
\[
\boxed{J_\delta(s,t)=C_\beta\bigl(t s^\alpha+s t^\alpha\bigr)
\delta^{-\beta}+o(\delta^{-\beta})\quad(\delta\to\infty).}
\]
At \(\delta=0\), \(X_\delta=X_0\) almost surely; at \(\delta=\infty\), the marginals are independent. Every finite positive \(\delta\) gives a dependent pair that is **not jointly stable**, notwithstanding its strictly stable marginals. Thus the microscopic center-separation scale \((n g_0)^{-1}\) supports a genuinely non-stable intermediate law.

## Assumptions and scope
The circle has length one and \(g\) is nonnegative, continuous, integrates to one, and is strictly positive at the first center. The same \(g\) is used for every sample size. Independence is assumed across sample points. The pole power \(\beta>1\) is essential here: it makes the limiting far-field shot-noise sums finite. The centers are distinct or coincident according to \(a_n\), but must both approach zero. The values at exact poles may be assigned arbitrarily since these events have probability zero.

The designation \(\delta=\infty\) means \(n g_0 a_n\to\infty\) **while still** \(a_n\to0\). The theorem does not assert the same normalization for centers separated by a fixed macroscopic distance where the local density could differ.

## Proof
**Step 1 (one-pole scale).** For \(s>0\), the function \(f_s\) is even, bounded by one, integrable on \(\mathbb R\), and satisfies \(f_s(x)\sim s|x|^{-\beta}\) at infinity. The substitution \(u=sx^{-\beta}\) and an integration by parts give
\[
\int_{\mathbb R}f_s(x)\,dx
=2\Gamma(1-1/\beta)s^{1/\beta}=C_\beta s^\alpha.
\]

**Step 2 (joint triangular-array Laplace limit).** Set \(L_n=n g_0\) and represent the circle by signed local coordinates \(y=L_nu\) of circumference \(L_n\). Let \(d_{L_n}\) denote geodesic distance on this length-\(L_n\) circle. Independence yields
\[
\mathbb E e^{-sT_{n,0}-tT_{n,1}}
=\left(1-\frac{A_n(s,t)}n\right)^n,
\]
where
\[
A_n(s,t)=\int_{-L_n/2}^{L_n/2}
\frac{g(y/L_n\bmod1)}{g_0}
\left(1-e^{-s|y|^{-\beta}-t d_{L_n}(y,\delta_n)^{-\beta}}\right)dy.
\]
Using \(1-e^{-u-v}=(1-e^{-u})+(1-e^{-v})-(1-e^{-u})(1-e^{-v})\), split \(A_n\) into two marginal terms and an overlap term. By integrability of \(f_s\), continuity of \(g\), and \(a_n\to0\), each marginal tends to its corresponding \(C_\beta s^\alpha\) or \(C_\beta t^\alpha\). If \(\delta_n\to\delta<\infty\), the overlap tends to \(J_\delta(s,t)\) by local dominated convergence and an integrable tail bound. If \(\delta_n\to\infty\), the centers' circular separation tends to infinity. For any fixed \(R\), the second kernel is uniformly small on the radius-\(R\) neighborhood of the first center; outside this neighborhood the first kernel has arbitrarily small integral for sufficiently large \(R\). Since \(g/g_0\) is bounded, the overlap tends to zero. Thus \(A_n\to C_\beta(s^\alpha+t^\alpha)-J_\delta\), and the displayed \(n\)-th power converges to the asserted transform.

For finite \(\delta\), the limit has the constructive representation
\[
(X_0,X_\delta)=\left(\sum_{z\in\mathcal P}|z|^{-\beta},\ \sum_{z\in\mathcal P}|z-\delta|^{-\beta}\right)
\]
with \(\mathcal P\) a unit-rate Poisson point process on \(\mathbb R\). There are almost surely finitely many points near either pole and none exactly at a pole; outside bounded neighborhoods the total expected contribution is finite since \(\beta>1\). Thus both coordinates are finite almost surely. The Poisson Laplace functional gives precisely the limit transform. The infinite-separation transform similarly defines two independent one-pole copies. This establishes joint weak convergence by uniqueness and continuity of Laplace transforms.

**Step 3 (strict Laplace dependence).** For \(s,t>0\), \(f_s(|x|)\) and \(f_t(|x|)\) are strictly decreasing functions of positive radius. By the layer-cake representation, \(J_\delta\) is an average over overlaps of two centered intervals translated apart by \(\delta\). Every overlap length is nonincreasing under separation. Given \(0\le\delta_1<\delta_2\), a positive-measure family of interval radii has partial overlap throughout the interval between those separations, giving strict decrease. Since \(f_s,f_t\) are integrable, translation continuity in \(L^1\) gives continuity of \(J_\delta\). Strict positivity holds for each finite separation because both kernels are positive away from their centers.

**Step 4 (small separation).** All derivatives of \(f_s\) extend continuously through zero (the exponential is flat there), and the derivatives needed here are integrable. Differentiation under the convolution and integration by parts yield \(J'_0=0\) and
\[
J''_0=-\int_{\mathbb R}f'_s(x)f'_t(x)\,dx.
\]
For positive \(x\), \(f'_s(x)=-\beta s x^{-\beta-1}e^{-s x^{-\beta}}\). Hence the substitution \(u=(s+t)x^{-\beta}\) evaluates the integral as
\[
\int_{\mathbb R}f'_s(x)f'_t(x)dx
=\frac{2\beta s t\,\Gamma(2+1/\beta)}{(s+t)^{2+1/\beta}}.
\]
Taylor's theorem at zero gives the stated exact quadratic coefficient.

**Step 5 (large separation).** Split \(\mathbb R\) into neighborhoods \(|x|<\delta/3\), \(|x-\delta|<\delta/3\), and the remainder. Dominated convergence after multiplication by \(\delta^\beta\) shows that the first neighborhood contributes asymptotically \(t\delta^{-\beta}\int f_s\), and the second contributes \(s\delta^{-\beta}\int f_t\). On the remainder both distances are at least \(\delta/3\), and the product is bounded by a constant times \(|x|^{-\beta}|x-\delta|^{-\beta}\); its integral is \(O(\delta^{1-2\beta})=o(\delta^{-\beta})\). Inserting Step 1 gives the far-field coefficient.

**Step 6 (joint stability obstruction).** A change of variables gives the exact scaling identity
\[
J_\delta(cs,ct)=c^\alpha J_{\delta c^{-\alpha}}(s,t),\qquad c>0.
\]
For finite positive \(\delta\), Step 3 makes this different from \(c^\alpha J_\delta(s,t)\) whenever \(c\ne1\). Therefore the joint Laplace exponent cannot be homogeneous of degree \(\alpha\). Any nonnegative jointly \(\alpha\)-stable vector with the stated drift-free stable marginals must have a homogeneous Laplace exponent. Hence this intermediate pair is not jointly stable. The coincident and independent endpoint cases are, respectively, a diagonal stable pair and a pair of independent stable coordinates.

## Verification
The standalone program `verify_two_pole.py` checks the exact zero-separation integral, strict finite-grid decrease, Laplace scaling, both asymptotic constants, and finite-circle convergence under both uniform and nonuniform continuous densities. Its executed output is in `verify_two_pole_output.txt`: 183 numerical assertions passed. Numerical assertions do not certify strict inequalities for a continuum or asymptotics; those rely on Steps 1–6.

To reproduce, run `python verify_two_pole.py` with Python 3 and SciPy installed. All numerical integrals are one-dimensional and deterministic.

## Relationship to prior work
Bassols Cornudella and Castro (2026, arXiv:2609.22499v1, originally submitted 2026-09-18) prove one-pole conditional Poisson and stable limits for absorbing Markov chains. The present statement concerns a different, simpler independent-sample model, but its essential question is the behavior when **two inverse-distance observables have moving, coalescing poles**; no single-pole limit identifies their joint dependence.

The Poisson shot-noise Laplace functional and its multi-location application are established prior theory (e.g. Olson and Andrews, arXiv:2406.05212v1, Section II-A and Section IV-B). Consequently the generic Poisson Laplace identity, the one-point stable marginal, and the shot-noise representation are **not claimed to be new**. The subject of this finding is the universal microscopic coalescence window and its exact strictly monotone Laplace-dependence profile, including both explicit sharp endpoint coefficients and non-stability at every intermediate separation.

## Limitations
The result does not extend the 2026 theorem to genuinely conditioned absorbing Markov trajectories; it treats independent observations with a continuous density. It does not address \(\beta\le1\), discontinuous or vanishing local densities, or fixed macroscopically separated poles with different local intensities. General shot-noise theory may contain an equivalent quantitative spatial-dependence result not identified in the inspected sources; independent historical-priority review is warranted. The comparison with prior theory establishes a best-knowledge distinction, not proof of global uniqueness.

## References
1. B. Bassols Cornudella and M. M. Castro, *Conditional Stable Laws and Rare-Event Limits for Absorbing Markov Chains*, arXiv:2609.22499v1 (first public submission 2026-09-18). https://arxiv.org/abs/2609.22499
2. N. R. Olson and J. G. Andrews, *A Matrix Exponential Generalization of the Laplace Transform of Poisson Shot Noise*, arXiv:2406.05212 (first public submission 2024-06-07), especially Section II-A and the multi-location shot-noise formulation in Section IV-B. https://arxiv.org/abs/2406.05212
