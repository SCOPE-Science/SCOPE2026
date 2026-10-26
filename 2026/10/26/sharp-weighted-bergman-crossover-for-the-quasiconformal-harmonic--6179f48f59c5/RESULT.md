# Sharp weighted Bergman crossover for the quasiconformal harmonic Koebe shear

## Finding
For \(\beta>-1\), let \(q\) satisfy
\[
\frac{\beta+2}{3}<q<\frac{\beta+2}{2}.
\]
The harmonic Koebe shear \(F_k=h_k+\overline{g_k}\), \(0\le k<1\), defined below obeys the exact weighted Bergman moment law
\[
\boxed{\lim_{k\uparrow1}(1-k)^{3q-\beta-2}I_{\beta,q}(k)=C_{\beta,q}\in(0,\infty)},
\]
where \(I_{\beta,q}(k)\) is the **unrooted** weighted moment and
\[
C_{\beta,q}=\frac{2^\beta}{\pi}\int_0^\infty\int_{-\infty}^{\infty}x^\beta\big|2\operatorname{Re}H(x-it)\big|^q\,dt\,dx,
\quad H(y)=\frac1{y^2}-\frac2y+2\log\!\left(1+\frac1y\right).
\]
The logarithm is the principal holomorphic branch on the right half-plane. In addition, the complex two-dimensional boundary layer has the locally uniform limit
\[
\lim_{k\uparrow1}(1-k)^3F_k\big(1-(1-k)y\big)=2\operatorname{Re}H(y),\qquad \operatorname{Re}y>0.
\]
Here the domain points are understood for sufficiently large \(k\), depending on the chosen compact subset. Thus the exact growth of the rooted norm is \(I_{\beta,q}(k)^{1/q}\sim C_{\beta,q}^{1/q}(1-k)^{(\beta+2)/q-3}\). The asymptotic is for this concrete family and makes no extremality assertion about a whole function class.

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(0\le k<1\), and \(\kappa(z)=z/(1-z)^2\). The normalized analytic functions \(h_k\) and \(g_k\) are specified by
\[
h_k(0)=g_k(0)=0,\qquad
h_k'(z)=\frac{1+z}{(1-z)^3(1-kz)},\qquad
g_k'(z)=kz\,h_k'(z).
\]
Consequently \(h_k-g_k=\kappa\); \(F_k=h_k+\overline{g_k}\) is the previously known sense-preserving univalent harmonic Koebe shear, with dilatation \(kz\). For \(\beta>-1\) and \(q>0\), fix the explicit normalization
\[
I_{\beta,q}(k)=\frac1\pi\int_{\mathbb D}|F_k(z)|^q(1-|z|^2)^\beta\,dx\,dy.
\]
The integral is finite for each \(k<1\) in the stated range. There is no normalization factor \(\beta+1\). The positive integral defining \(C_{\beta,q}\) is over \(x>0\), \(t\in\mathbb R\).

## Proof
**1. Exact reduction.** Since \(\kappa'(z)=(1+z)/(1-z)^3\), the derivative identities imply \((h_k-g_k)'=\kappa'\), so \(g_k=h_k-\kappa\) with the specified initial values. Set \(\varepsilon=1-k\). Writing \(w=1-z\), integration along the straight segment from \(w\) to \(1\) in the right half-plane gives
\[
h_k(z)=\int_{1-z}^{1}\frac{2-s}{s^3(\varepsilon+ks)}\,ds.
\]
The expression is path-independent because its integrand is holomorphic on the right half-plane.

**2. Boundary-layer profile.** For \(\operatorname{Re}y>0\), define \(u_\varepsilon(y)=\varepsilon^3h_k(1-\varepsilon y)\) for sufficiently small \(\varepsilon\). Direct differentiation gives
\[
u_\varepsilon'(y)=-\frac{2-\varepsilon y}{y^3(1+y-\varepsilon y)}
\longrightarrow -\frac{2}{y^3(1+y)}.
\]
For fixed real \(y>0\), the integral identity is
\[
u_\varepsilon(y)=\int_y^{1/\varepsilon}\frac{2-\varepsilon u}{u^3(1+u-\varepsilon u)}\,du
\longrightarrow \int_y^\infty\frac{2}{u^3(1+u)}\,du.
\]
Dominated convergence applies on the real integration path for all sufficiently small \(\varepsilon\). Primitive evaluation yields
\[
\int_y^\infty\frac{2\,du}{u^3(1+u)}=\frac1{y^2}-\frac2y+2\log(1+y^{-1})=H(y).
\]
The derivatives converge uniformly on compact subsets of \(\operatorname{Re}y>0\), and the normalization at a positive real point fixes the additive constant, proving locally uniform convergence \(u_\varepsilon\to H\) on the entire right half-plane. Since \(\varepsilon^3\kappa(1-\varepsilon y)=O(\varepsilon)\) locally uniformly and \(g_k=h_k-\kappa\), this gives
\[
\varepsilon^3F_k(1-\varepsilon y)=u_\varepsilon(y)+\overline{u_\varepsilon(y)}-\overline{\varepsilon^3\kappa(1-\varepsilon y)}
\longrightarrow 2\operatorname{Re}H(y).
\]

**3. A uniform global majorant.** Put \(d=|1-z|\). For \(k\ge1/2\) and all \(z\in\mathbb D\) there is an absolute constant \(M\) such that
\[
|h_k(z)|+|g_k(z)|+|F_k(z)|\le \frac{M}{d^2(\varepsilon+d)}.
\]
Indeed along \(s=(1-u)(1-z)+u\), \(0\le u\le1\), one has \(|s|\ge c(d+u)\), \(\operatorname{Re}s>0\), and \(|\varepsilon+ks|\ge c(\varepsilon+|s|)\), for universal \(c>0\). Thus the integral of \(|2-s|/(|s|^3|\varepsilon+ks|)\) is bounded by a constant times
\[
\int_0^1\frac{du}{(d+u)^3(\varepsilon+d+u)}\le\frac{1}{2d^2(\varepsilon+d)}.
\]
Finally \(|\kappa(z)|\le d^{-2}\), and \(g_k=h_k-\kappa\) gives the same bound for \(g_k\) and \(F_k\).

**4. Change of scale and dominated convergence.** In polar coordinates \(z=re^{i\theta}\), set
\[
r=1-\varepsilon x,\qquad \theta=\varepsilon t,
\quad 0<x<\varepsilon^{-1},\quad |t|<\pi\varepsilon^{-1}.
\]
The normalized weighted Jacobian is \(\pi^{-1}(1-\varepsilon x)\varepsilon^{\beta+2}x^\beta(2-\varepsilon x)^\beta\,dx\,dt\). Hence
\[
\begin{split}
\varepsilon^{3q-\beta-2}I_{\beta,q}(k)=\frac1\pi\int_0^{\varepsilon^{-1}}\!\int_{-\pi/\varepsilon}^{\pi/\varepsilon}
&(1-\varepsilon x)x^\beta(2-\varepsilon x)^\beta\\
&\times\left|\varepsilon^3F_k\big((1-\varepsilon x)e^{i\varepsilon t}\big)\right|^q\,dt\,dx.
\end{split}
\]
For fixed \(x>0\), \(t\in\mathbb R\), the scaled boundary variable \((1-z)/\varepsilon\to x-it\). The preceding profile therefore gives pointwise convergence of the integrand to \(2^\beta x^\beta|2\operatorname{Re}H(x-it)|^q\).

Uniformly in the changing integration domain, elementary disk geometry gives
\[
|1-(1-\varepsilon x)e^{i\varepsilon t}|\ge c\varepsilon(x+|t|),\qquad
\varepsilon+|1-z|\ge c\varepsilon(1+x+|t|).
\]
The global majorant from Step 3 and \(1\le2-\varepsilon x\le2\) bound the scaled integrand by
\[
M_{\beta,q}\,\frac{x^\beta}{(x+|t|)^{2q}(1+x+|t|)^q}.
\]
Near the origin, polar integration on the right half-plane gives the radial integrability condition \(\beta+2-2q>0\), and at infinity it gives \(\beta+2-3q<0\). Angular integration is finite because \(\beta>-1\). These are exactly the two strict inequalities assumed in the theorem. The dominated convergence theorem now proves the asserted constant and limit.

**5. Strict positivity and exact exponent.** The integral is finite by Step 4. For each real \(x>0\), \(H(x)=\int_x^\infty2/[u^3(1+u)]\,du>0\). Continuity in \(t\) gives a neighborhood of every positive real \(x\) on which \(2\operatorname{Re}H(x-it)\ne0\), so \(C_{\beta,q}>0\). A finite positive limit proves the sharp exponent and the rooted-norm equivalent. In the fixed-parameter regime \(k<1\), the local singularity has at most order two; at \(k=1\), the limiting harmonic Koebe map has a nonvanishing order-three leading term along non-tangential cones. This explains the two distinct integrability thresholds; no additional endpoint logarithmic assertion is made here.

## Verification
The proof rests on analytic identities and a global integrable majorant; finite checks are supplementary. The standalone `checker.py` symbolically differentiates the profile, verifies the first nontrivial Taylor coefficients of \(h_k\), and tests real and nonreal scaled-point convergence for successively decreasing \(1-k\). The test program prints `CHECK_OK` when all checks pass. A separate quadrature check with \(\beta=0\), \(q=0.8\) gave a positive finite model coefficient near \(4.497\), consistent with the integral formula; the analytic majorant, not the quadrature, establishes finiteness for all parameters.

## Relationship to prior work
Wang, Wang, Rasila, and Qiu (2024) introduced the underlying quasiconformal harmonic Koebe shear and its explicit formula. Wang, Qiu, and Rasila (2025) developed the generalized shear family and its univalence, growth, area, and differential invariants. Parashar, Ponnusamy, and Kaliraj (2026) studied coefficient and integral-mean estimates and established fixed-distortion weighted Bergman membership ranges, including \(q<(\beta+2)/2\) in a natural subclass. Das and Rasila (2025) had earlier proved related quasiregular Bergman membership estimates. These constructions and membership estimates are prior work. The result above instead determines the **exact nonuniform norm blow-up coefficient and two-dimensional profile as the distortion tends to infinity**. The examined primary texts do not give this parameter-asymptotic theorem; absence from indexed searches is not a proof of historical priority.

## Limitations
The result is for the explicit quasiconformal Koebe shear, not an extremal statement over all normalized quasiconformal harmonic mappings. It treats only the open range \((\beta+2)/3<q<(\beta+2)/2\); it does not claim the endpoint laws. It gives a convergent integral for the exact leading constant, not a general closed gamma-function evaluation. The asymptotic fixes \(\beta\) and \(q\) before taking \(k\uparrow1\). Historical priority cannot be absolutely established from the literature inspected here.

## References
1. J. Parashar, S. Ponnusamy, and A. S. Kaliraj, *Coefficients and Integral Mean Estimates for \(K\)-Quasiconformal Harmonic Mappings*, first public 2026-08-28, arXiv:2608.28121, https://arxiv.org/abs/2608.28121.
2. Z.-G. Wang, X.-Y. Wang, A. Rasila, and J.-L. Qiu, *On a problem of Pavlović involving harmonic quasiconformal mappings*, first public 2024-05-30, arXiv:2405.19852, https://arxiv.org/abs/2405.19852.
3. Z.-G. Wang, J.-L. Qiu, and A. Rasila, *On generalized harmonic quasiconformal Koebe functions*, first public 2025-05-18, arXiv:2505.12562, https://arxiv.org/abs/2505.12562.
4. S. Das and A. Rasila, *On harmonic quasiregular mappings in Bergman spaces*, first public 2025-07-25, arXiv:2507.19158, https://arxiv.org/abs/2507.19158.
