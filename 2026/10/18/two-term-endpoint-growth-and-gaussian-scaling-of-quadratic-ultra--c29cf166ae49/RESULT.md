# Two-term endpoint growth and Gaussian scaling of quadratic ultraspherical projection

## Finding

Let \(a>0\), and let \(\mu_a\) be probability measure on \([-1,1]\) with density
\[
 d\mu_a(y)=\frac{\Gamma(a+\tfrac12)}{\sqrt\pi\,\Gamma(a)}(1-y^2)^{a-1}\,dy.
\]
Let \(P_a\) be the orthogonal projector in \(L^2(\mu_a)\) onto \(\operatorname{span}\{1,y,y^2\}\), extended as an integral operator to \(L^1(\mu_a)\) and \(L^\infty(\mu_a)\). Write \(\phi(t)=e^{-t^2/2}/\sqrt{2\pi}\) and \(Q=\int_1^\infty\phi(t)\,dt\). Then, as \(a\to\infty\),
\[
 \boxed{\|P_a\|_{L^1\to L^1}=\|P_a\|_{L^\infty\to L^\infty}
   =4\phi(1)a+7\phi(1)+4Q-1+o(1).}
\]
Here \(4\phi(1)=\sqrt{8/(\pi e)}\) and \(7\phi(1)+4Q-1\approx1.32841608735983165\). There exists \(a_0>0\) such that for every real \(a\ge a_0\), the **only** evaluation points maximizing the projector's pointwise Lebesgue function are \(x=\pm1\). No numerical value of \(a_0\) is asserted.

For \(\Lambda_a(x)=\int_{-1}^1|K_a(x,y)|\,d\mu_a(y)\), the normalized full spatial profile satisfies
\[
 \boxed{\sup_{|x|\le1}\left|\frac{\Lambda_a(x)}a-4\phi(1)x^2\right|\longrightarrow0.}
\]
Consequently, \(\Lambda_a(x_a)/\|P_a\|\to1\) for an arbitrary sequence \(x_a\in[-1,1]\) if and only if \(|x_a|\to1\).

A distinct central Gaussian regime holds locally uniformly in \(z\in\mathbb R\):
\[
 \boxed{\Lambda_a\!\left(\frac{z}{\sqrt{2a+1}}\right)\longrightarrow
 \mathbb E\left|1+zZ+\frac{(z^2-1)(Z^2-1)}2\right|,\quad Z\sim N(0,1).}
\]
Thus the concentration scale has a finite Hermite-kernel profile even though the global sharp amplification grows linearly in \(a\).

## Assumptions and scope

All assertions are for real \(a>0\), with the asymptotic assertions as \(a\to\infty\) at **fixed projection degree two**. Domain and target use the same probability measure \(\mu_a\); the norm on \(L^\infty\) is the essential-supremum norm and is unchanged when the scalars are complex. The central scaling requires \(|z|\le\sqrt{2a+1}\), automatically true for each fixed \(z\) eventually. The source of the large parameter is the Jacobi/Gegenbauer weight exponent, not polynomial degree or ambient dimension.

## Proof

**1. Exact normalized kernel.** Put \(s=\mathbb E_{\mu_a}Y^2\) and \(v=\operatorname{Var}_{\mu_a}(Y^2)\). Beta moments give
\[
 s=\frac1{2a+1},\qquad
 \mathbb E Y^4=\frac3{(2a+1)(2a+3)},\qquad
 v=\frac{4a}{(2a+1)^2(2a+3)}.
\]
The three functions \(1\), \(y/\sqrt s\), \((y^2-s)/\sqrt v\) are orthonormal in \(L^2(\mu_a)\). Thus the exact reproducing kernel is
\[
 K_a(x,y)=1+\frac{xy}s+\frac{(x^2-s)(y^2-s)}v.
\]
Its symmetry gives \(\|P_a\|_{1\to1}=\|P_a\|_{\infty\to\infty}=\max_{|x|\le1}\Lambda_a(x)\), since bounded sign inputs attain the kernel integral at a fixed evaluation point, and continuity allows essential suprema to approach boundary points. This includes the complex case.

**2. Spatial normalization and unique large-parameter maximizers.** Set \(Z_a=\sqrt{2a+1}Y\). It has variance one and converges in law, with moments of every fixed order, to \(Z\sim N(0,1)\). The exact rescaled kernel is
\[
 K_a\!\left(x,\frac{z}{\sqrt{2a+1}}\right)
 =1+\sqrt{2a+1}\,xz
 +\frac{2a+3}{4a}\big((2a+1)x^2-1\big)(z^2-1).
\tag{1}
\]
Dividing by \(a\) gives \(x^2(z^2-1)+R_a(x,z)\), where
\[
 \sup_{|x|\le1}|R_a(x,z)|\le C a^{-1/2}(1+|z|+z^2),\qquad a\ge1.
\]
The second moments of \(Z_a\) are identically one, and its fourth moments are bounded. Hence the reverse triangle inequality and moment convergence give, uniformly for \(|x|\le1\),
\[
 \frac{\Lambda_a(x)}a=x^2\mathbb E|Z_a^2-1|+O(a^{-1/2})
 \longrightarrow x^2\mathbb E|Z^2-1|=4\phi(1)x^2.
\tag{2}
\]
This establishes the leading norm constant and the iff criterion for asymptotically maximizing evaluations.

For every \(a>0\), \(\Lambda_a\) is differentiable in \(x\): the polynomial \(K_a(x,\cdot)\) is nonzero and has at most two roots, a null set for the measure. Differentiation under the integral yields
\[
 \Lambda'_a(x)=\mathbb E[\operatorname{sgn}(K_a(x,Y))\,\partial_x K_a(x,Y)].
\]
For any fixed \(\delta\in(0,1)\), formula (1) implies, uniformly for \(x\in[\delta,1]\), that \(a^{-1}\partial_x K_a\to2x(Z_a^2-1)\) in \(L^1\), while the sign of \(K_a\) agrees with that of \(Z_a^2-1\) except on a set of vanishing weighted mass. Indeed, truncate to a bounded \(z\)-interval, exclude \(\big||z|-1\big|\le\eta\), apply uniform convergence there, and then let the interval expand and \(\eta\downarrow0\). Uniform Gaussian-type tails and uniform bounded density near \(\pm1\) justify these limits. Therefore
\[
 \sup_{\delta\le x\le1}\left|\frac{\Lambda'_a(x)}a-8\phi(1)x\right|\to0.
\tag{3}
\]
Taking \(\delta=1/2\), (3) shows strict increase on \([1/2,1]\) when \(a\) is sufficiently large. Meanwhile (2) shows every \(0\le x\le1/2\) has \(\Lambda_a(x)/a\le\phi(1)+o(1)\), whereas \(\Lambda_a(1)/a\to4\phi(1)\). Symmetry \(\Lambda_a(-x)=\Lambda_a(x)\) proves that \(\pm1\) are the only global maximizers for all sufficiently large \(a\).

**3. Hermite scaling at the center.** Substitute \(x=z/\sqrt{2a+1}\) in (1):
\[
 K_a\!\left(\frac z{\sqrt{2a+1}},\frac t{\sqrt{2a+1}}\right)
 =1+zt+\frac{2a+3}{4a}(z^2-1)(t^2-1).
\]
The coefficient tends to \(1/2\), giving the reproducing kernel of the first three probabilists' Hermite modes. Uniform integrability of the quadratic polynomial in \(Z_a\), uniformly for \(z\) in each compact set, gives the displayed Gaussian central-profile limit.

**4. Constant-order endpoint correction.** At \(x=1\), equation (1) is exactly
\[
 K_a\!\left(1,\frac z{\sqrt{2a+1}}\right)
 =a(z^2-1)+\sqrt{2a+1}\,z+\frac{3z^2-1}{2}.
\tag{4}
\]
The density \(p_a\) of \(Z_a\) satisfies the weighted expansion
\[
 p_a(z)=\phi(z)\left[1-\frac{H_4(z)}{8a}\right]+o(a^{-1}),
 \qquad H_4(z)=z^4-6z^2+3,
\tag{5}
\]
where the error is \(o(a^{-1})\) in \(L^1\) with any fixed polynomial weight. To prove (5), expand the exact density
\[
 p_a(z)=\frac{\Gamma(a+1/2)}{\sqrt\pi\,\Gamma(a)\sqrt{2a+1}}
 \left(1-\frac{z^2}{2a+1}\right)^{a-1}\mathbf1_{|z|<\sqrt{2a+1}},
\]
using the gamma-ratio expansion and Taylor's formula on \(|z|\le a^{1/12}\). Outside this region it is bounded by \(Ce^{-cz^2}\) uniformly for \(a\ge2\), so polynomial-weighted remainders are negligible.

Set \(\varepsilon=a^{-1/2}\), \(f(z)=z^2-1\), \(g(z)=\sqrt2\,z\), and \(h(z)=(3z^2-1)/2\). Dividing (4) by \(a\) gives \(f+\varepsilon g+\varepsilon^2h+O(\varepsilon^3|z|)\). Since \(f\) has simple zeros at \(\pm1\), splitting its absolute-value integral at the two perturbed roots gives
\[
 \begin{aligned}
 \int|f+\varepsilon g+\varepsilon^2h|\phi
 &=\int|f|\phi+\varepsilon\int g\operatorname{sgn}(f)\phi\\
 &\quad+\varepsilon^2\left(\int h\operatorname{sgn}(f)\phi
 +\sum_{r\in\{-1,1\}}\frac{g(r)^2\phi(r)}{|f'(r)|}\right)+o(\varepsilon^2).
 \end{aligned}
\tag{6}
\]
Here \(\int\) is over \(\mathbb R\); the first-order term vanishes by parity. With \(Q=\int_1^\infty\phi\), Gaussian tail-moment recurrence gives
\[
 \int|f|\phi=4\phi(1),\quad
 \int h\operatorname{sgn}(f)\phi=6\phi(1)+4Q-1,\quad
 \sum_r\frac{g(r)^2\phi(r)}{|f'(r)|}=2\phi(1),\quad
 -\frac18\int|f|H_4\phi=-\phi(1).
\]
Combining (4)--(6) yields
\[
 \Lambda_a(1)=4\phi(1)a+[6\phi(1)+4Q-1]+2\phi(1)-\phi(1)+o(1)
 =4\phi(1)a+7\phi(1)+4Q-1+o(1).
\]
By Step 2, this equals the global endpoint norm for all sufficiently large \(a\), concluding the proof.

## Verification

For every real \(a>0\), the two roots of the endpoint polynomial \(K_a(1,y)\) are
\[
 u_\pm=\frac{-1\pm\sqrt{2a+4}}{2a+3},\qquad
 K_a(1,y)=\frac{2a+1}{2}\big((2a+3)y^2+2y-1\big).
\]
Therefore the **exact endpoint value** (not claimed equal to the global norm for small \(a\)) is
\[
 \Lambda_a(1)=1-2\int_{u_-}^{u_+}K_a(1,y)\,d\mu_a(y).
\]
The embedded `check.py` uses exact rational beta moments to check projection reproduction and arbitrary-precision integration between these roots to compare against the two-term coefficient. It also tests the scaled kernel and central Hermite convergence numerically. These finite checks support, but do not replace, Steps 1--4.

## Relationship to prior work

Classical Gegenbauer-to-Hermite asymptotics, including those surveyed in DLMF §18.15(vi), describe orthogonal polynomials at large weight parameters. The 2012 hyperinterpolation work of Wade examines estimates for cubature-based polynomial operators as polynomial degree changes; it does not state a fixed-degree-two, large-parameter sharp projection norm. Sobrino's 2022 paper develops parameter asymptotics of norms of **individual** Gegenbauer polynomials, not the maximized absolute three-mode reproducing kernel. Earlier studies of weighted Fourier--Gegenbauer/Jacobi projection bounds, including Levesley--Kushpel and Luther--Mastroianni, concern different varying degrees and/or weighted function norms. The present result adds endpoint rigidity, a sharp order-one correction, and a matched central Gaussian profile. A comprehensive historical-priority claim is not made.

## Limitations

The proof gives no explicit value for the threshold \(a_0\), no exact global optimizer classification for small \(a\), and no asymptotics for degrees larger than two or for asymmetric Jacobi weights. The Gaussian kernel limit itself is classical; the claimed contribution is the global endpoint norm with its nonleading constant and maximizing-point rigidity, paired with a precise central-profile contrast. Older Fourier--Gegenbauer projection literature could not all be inspected in full, so historical overlap remains a risk. The verification script is not a formal proof or independent audit.

## References

- J. Wade, *On hyperinterpolation on the unit ball*, first public arXiv version 2012-09-19, arXiv:1209.4328, https://arxiv.org/abs/1209.4328.
- N. Sobrino, *Parameter and q asymptotics of Lq-norms of hypergeometric orthogonal polynomials*, arXiv:2204.11242v1, https://arxiv.org/html/2204.11242v1.
- NIST Digital Library of Mathematical Functions, §18.15(vi), https://dlmf.nist.gov/18.15.vi.
- J. Levesley and A. Kushpel, *On the Norm of the Fourier--Gegenbauer Projection in Weighted Lp Spaces*, Constructive Approximation 15 (1999), 369--379, https://doi.org/10.1007/s003659900113.
- U. Luther and G. Mastroianni, *Fourier Projections in Weighted L-infinity Spaces*, Chemnitz preprint 99-10 (1999), https://www.tu-chemnitz.de/mathematik/preprint/1999/PREPRINT_10.php.
