# Unique optimal Luce LIS paths and an exact quadrature for exponential weights

## Finding

Fix \(\beta\ge0\). For each \(n\ge1\), let \(\tau_n\) be the Luce random permutation with weights \(\theta_k^{(n)}=e^{-\beta(k-1)/n}\), for \(1\le k\le n\). The asymptotic theorem of Borga and Dubach identifies \(\mathrm{LIS}(\tau_n)/(2\sqrt n)\) in probability with a constant \(K_\beta\) given by a variational supremum. The present theorem evaluates that supremum exactly by one scalar quadrature and proves uniqueness of the maximizing curve among **all** admissible right-continuous nondecreasing curves, without assuming absolute continuity.

Put \(g(y)=-(1-y)\log(1-y)\) for \(0\le y<1\) and \(g(1)=0\). For \(\beta>0\) and \(C>\sqrt{\beta/e}\), set
\[
d_C(y)=\sqrt{C^2-\beta g(y)},\qquad
T_\beta(C)=\int_0^1\frac{dy}{2d_C(y)(C+d_C(y))}.
\]
There is a **unique** \(C_\beta>\sqrt{\beta/e}\) satisfying \(T_\beta(C_\beta)=1\). For \(\beta=0\), put \(C_0=1/2\). Then
\[
\boxed{K_\beta=\frac12\int_0^1\frac{dy}{d_{C_\beta}(y)}
=C_\beta+\frac12\int_0^1\frac{dy}{C_\beta+d_{C_\beta}(y)}.}
\]
Define the increasing \(C^1\) function \(y_\beta:[0,1]\to[0,1]\) by
\[
t=\int_0^{y_\beta(t)}\frac{dz}{2d_{C_\beta}(z)(C_\beta+d_{C_\beta}(z))}.
\]
The unique maximizer in the Luce variational principle is
\[
\boxed{u_\beta^*(t)=e^{\beta t}[-\log(1-y_\beta(t))],\qquad 0\le t<1.}
\]
In particular, \(u_\beta^*\in C^1([0,1))\), \(u_\beta^*(0)=0\), it is strictly increasing, and \(u_\beta^*(t)\to\infty\) as \(t\uparrow1\). The constants obey
\[
K_0=1,\qquad K_\beta=1+\frac\beta8+O(\beta^2)\ (\beta\downarrow0),
\qquad \lim_{\beta\to\infty}\frac{K_\beta}{\sqrt\beta}=\frac1{\sqrt e}.
\]

## Assumptions and scope

The admissible class consists of every nondecreasing, right-continuous finite-valued \(u:[0,1)\to[0,\infty)\). For such a function, the derivative \(u'(t)\) exists and is nonnegative almost everywhere, and the defining functional is
\[
A_\beta(u)=\int_0^1\sqrt{e^{-\beta t}u'(t)\exp(-e^{-\beta t}u(t))}\,dt.
\]
A singular continuous part or jump part of \(u\) earns no direct contribution to this Lebesgue integral. Limits as \(t\uparrow1\) may be infinite. The pre-existing probabilistic limit theorem, not reproved here, states \(K_\beta=\sup_u A_\beta(u)\) and the above LIS normalization for these positive regular weights. No finite-sample concentration improvement or geodesic convergence is claimed.

## Proof

**1. Bounded coordinate and singular components.** Set \(y(t)=1-\exp(-e^{-\beta t}u(t))\). Every competitor gives \(0\le y(t)<1\), \(y(0)\ge0\), and \(y(1-)=\lim_{t\uparrow1}y(t)\in[0,1]\). The chain and product rules for bounded-variation functions imply that the distributional derivative of \(y\) on \((0,1)\) has the form
\[
dy=(b(t)-\beta g(y(t)))\,dt+d\nu,
\qquad b=e^{-\beta t}u'\exp(-e^{-\beta t}u)\ge0,
\]
where \(\nu\) is a nonnegative singular measure (the push-forward of the nonnegative singular/jump increments of \(u\)). This remains valid if \(u\) has dense jumps, by the BV chain rule and monotone approximation on compact subintervals. Consequently \(A_\beta(u)=\int_0^1\sqrt b\,dt\). Notice \(g'(y)=1+\log(1-y)\) and \(g''(y)=-1/(1-y)<0\), so \(g\) is strictly concave and has unique maximum \(1/e\) at \(y=1-e^{-1}\).

**2. Scalar shooting and the canonical curve.** For fixed \(\beta>0\), \(T_\beta(C)\) is strictly decreasing and continuous on \((\sqrt{\beta/e},\infty)\), and tends to zero at infinity. At \(C\downarrow\sqrt{\beta/e}\), its integrand has a logarithmically nonintegrable peak near the nondegenerate maximum of \(g\); hence \(T_\beta(C)\to\infty\). The intermediate value theorem supplies the unique root. For \(\beta=0\), \(T_0(C)=1/(4C^2)\). Inverting its defining integral gives \(y_\beta(0)=0\), \(y_\beta(1)=1\), and
\[
y_\beta'=2d_{C_\beta}(y_\beta)(C_\beta+d_{C_\beta}(y_\beta))
=(C_\beta+d_{C_\beta}(y_\beta))^2-\beta g(y_\beta)>0.
\]
Thus the proposed \(u_\beta^*\) is admissible, smooth for \(t<1\), strictly increasing, and its integrand parameter is
\[
b_\beta(t)=(C_\beta+d_{C_\beta}(y_\beta(t)))^2.
\]
Changing variables from \(t\) to \(y\) gives
\[
A_\beta(u_\beta^*)=\int_0^1\sqrt{b_\beta(t)}\,dt
=\frac12\int_0^1\frac{dy}{d_{C_\beta}(y)}.
\]
Using \(T_\beta(C_\beta)=1\), elementary denominator subtraction also gives the second expression for \(K_\beta\).

**3. A global calibration, including singular competitors.** Define the positive continuous weight \(p(t)=1/(2\sqrt{b_\beta(t)})\). Differentiating the defining first integral yields \(p'(t)=\beta p(t)g'(y_\beta(t))\). It holds in the integrable sense up to the endpoint (\(p\) remains positive and finite). For any competitor, the tangent inequalities for the concave maps \(z\mapsto\sqrt z\) and \(g\) give
\[
A_\beta(u)-A_\beta(u_\beta^*)
\le\int_0^1 p(b-b_\beta)\,dt
\le\int_0^1p\,d(y-y_\beta)-\int_0^1p\,d\nu
+\int_0^1\beta p g'(y_\beta)(y-y_\beta)\,dt.
\]
BV integration by parts and \(p'=\beta p g'(y_\beta)\) reduce the right side to
\[
p(1)(y(1-)-1)-p(0)y(0)-\int_0^1p\,d\nu\le0.
\]
This proves global maximality against jumps, singular continuous curves, and arbitrary absolutely continuous curves simultaneously. Equality forces \(y(0)=0\), \(y(1-)=1\), \(\nu=0\), and \(b=b_\beta\) almost everywhere by strict concavity of the square root. The ODE \(y'=b_\beta-\beta g(y)\) with \(y(0)=0\) has a unique solution on every compact interval in \([0,1)\), because \(g\) is locally Lipschitz on \([0,1)\). Thus \(y=y_\beta\), hence \(u=u_\beta^*\). Uniqueness is proved in the full original admissible class.

**4. Sharp parameter endpoints.** Since \(\int_0^1g(y)dy=1/4\), expanding \(T_\beta(C)\) at \((\beta,C)=(0,1/2)\) and applying the implicit-function theorem gives \(C_\beta=1/2+3\beta/16+O(\beta^2)\). Expanding the displayed \(K_\beta\) integral gives \(K_\beta=1+\beta/8+O(\beta^2)\). For large \(\beta\), write \(C_\beta^2=\beta(1/e+\varepsilon_\beta)\) with \(\varepsilon_\beta>0\). If \(\varepsilon_\beta\ge\varepsilon>0\) along a subsequence, \(T_\beta(C_\beta)=O(1/\beta)\), contradicting its value one. Hence \(C_\beta/\sqrt\beta\to1/\sqrt e\). Finally
\[
0<K_\beta-C_\beta=\frac12\int_0^1\frac{dy}{C_\beta+d_{C_\beta}(y)}\le\frac1{2C_\beta},
\]
which proves the claimed \(K_\beta/\sqrt\beta\) limit.

## Verification

The accompanying `verify.py` numerically solves the one-dimensional shooting equation, verifies the two equivalent formulas for \(K_\beta\), integrates the smooth optimizer ODE, and compares against ten independent smooth competitors at each of eleven representative \(\beta\)-values. The recorded execution has 249 passing assertions and prints reproducible values, including \(K_1\approx1.1275887687\) and \(K_4\approx1.5005182165\). Numerical integration close to the critical shooting threshold can report a harmless roundoff warning; the proof of the strict integral crossing is analytic. These tests do not certify the infinite-dimensional theorem, which is proved by the displayed calibration.

## Relationship to prior work

Borga and Dubach (2026, arXiv:2610.30382v1), Lemma 3.14 and Remark 3.15, establish the Luce LIS variational functional and explicitly state that existence, uniqueness, and even a plausible formula for the optimal curve are unresolved. They discuss the same Mallows-like exponential weights, giving a nonsharp lower bound but not the exact optimizing curve or value. The present result proves uniqueness and supplies a scalar quadrature *only for this exponential-weight subfamily*, thereby settling a concrete instance of their stated question. Borga, Chatterjee and Diaconis (2025, arXiv:2509.07729) establish the associated Luce permuton limit and other statistics, not this optimization. General iid increasing-subsequence and limiting-curve theory precedes both works; its generic variational framework is acknowledged, not presented here as new.

## Limitations

The optimal-path theorem concerns \(f(t)=e^{-\beta t}\) with \(\beta\ge0\), not arbitrary decreasing weights, and uses the known probabilistic identification of the LIS constant. Uniqueness of the continuum maximizing path alone does **not** prove convergence of finite discrete LIS geodesics to that path. Numerical values are illustrative, not rigorously interval-certified approximations; an earlier broad optimal-control theorem might independently imply part of the calibration. Historical-priority checking is necessarily qualified pending independent review. No independent mathematical audit has been conducted.

## References

1. J. Borga and V. Dubach, *The longest increasing subsequences of Luce permutations and permutons*, arXiv:2610.30382v1 (first public 2026-10-21), particularly Theorem 3.13, Lemma 3.14, Remark 3.15 and the Mallows-like example. https://arxiv.org/html/2610.30382v1
2. J. Borga, S. Chatterjee and P. Diaconis, *Permuton and local limits for the Luce model*, arXiv:2509.07729 (first public 2025-09-09). https://arxiv.org/abs/2509.07729
3. J.-D. Deuschel and O. Zeitouni, *On increasing subsequences of iid samples*, arXiv:math/9803035 (1998), prior general i.i.d. increasing-subsequence theory. https://arxiv.org/abs/math/9803035
