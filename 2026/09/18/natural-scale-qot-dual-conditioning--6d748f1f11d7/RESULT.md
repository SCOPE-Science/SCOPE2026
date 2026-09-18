# Natural-scale strong concavity and sharp Hessian conditioning for quadratically regularized optimal transport

## Statement

Consider quadratically regularized optimal transport with quadratic cost
\[
c(x,y)=\tfrac12|x-y|^2
\]
between probability measures \(\mu\) and \(\nu\) satisfying Assumption 1.1 of González-Sanz--Nutz (2026): their supports \(X,Y\subset\mathbb R^d\) are bounded uniformly convex \(C^{3,\alpha}\) domains (compact intervals when \(d=1\)), and both marginals have positive \(C^{1,\alpha}\) densities bounded above and below. Write
\[
\Gamma_\varepsilon(f,g)
=\int f\,d\mu+\int g\,d\nu
-\frac1{2\varepsilon}\int (f(x)+g(y)-c(x,y))_+^2\,d(\mu\otimes\nu),
\]
and let \((f_\varepsilon,g_\varepsilon)\) be an optimal dual pair. Set
\[
q_\varepsilon(x,y)=f_\varepsilon(x)+g_\varepsilon(y)-c(x,y),
\qquad
\ell=\varepsilon^{1/(d+2)}.
\]
The direct sum \(f\oplus g\) is invariant under the usual gauge transformation \((f,g)\mapsto(f+a,g-a)\). Let
\[
\mathcal H=\{u\oplus v:(u,v)\in L^2(\mu)\times L^2(\nu)\}
\subset L^2(\mu\otimes\nu)
\]
with its induced \(L^2(\mu\otimes\nu)\) norm.

There are constants
\[
\theta,m,M,\rho,\varepsilon_0>0,
\]
depending only on the fixed marginal data and dimension, such that for every \(0<\varepsilon<\varepsilon_0\) the following hold.

### 1. Natural-scale core coercivity

Define the positive-slack core
\[
E_\varepsilon=\{(x,y):q_\varepsilon(x,y)\ge \theta\ell^2\}.
\]
Then for every \(w=u\oplus v\in\mathcal H\),
\[
\boxed{
\int_{E_\varepsilon}(u(x)+v(y))^2\,d\mu(x)d\nu(y)
\ge m\,\varepsilon\,\|u\oplus v\|_{L^2(\mu\otimes\nu)}^2.
}
\tag{1}
\]
Thus the support geometry supplies exactly the \(\ell^{d+2}=\varepsilon\) factor needed to cancel the \(1/\varepsilon\) prefactor in the dual curvature.

### 2. An \(\varepsilon\)-uniform strongly concave neighborhood

Let \(h_\varepsilon=f_\varepsilon\oplus g_\varepsilon\), and regard the dual as a functional \(\Phi_\varepsilon(h)=\Gamma_\varepsilon(f,g)\) on \(\mathcal H\). On the convex set
\[
\mathcal B_\varepsilon
=\{h\in\mathcal H\cap L^\infty:\|h-h_\varepsilon\|_\infty\le \rho\ell^2\},
\]
\(\Phi_\varepsilon\) is \(m\)-strongly concave in the \(L^2(\mu\otimes\nu)\) norm. Equivalently, for \(h_0,h_1\in\mathcal B_\varepsilon\) and \(t\in[0,1]\),
\[
\boxed{
\Phi_\varepsilon((1-t)h_0+th_1)
\ge (1-t)\Phi_\varepsilon(h_0)+t\Phi_\varepsilon(h_1)
+\frac m2 t(1-t)\|h_1-h_0\|_2^2.
}
\tag{2}
\]
The radius is the natural potential scale
\[
\boxed{\rho\ell^2=\rho\varepsilon^{2/(d+2)}},
\tag{3}
\]
which is asymptotically larger than the \(O(\varepsilon)\) neighborhood used in the previously published general PL estimate.

The same neighborhood has gradient Lipschitz constant
\[
\boxed{L_\varepsilon\le M\ell^{-2}=M\varepsilon^{-2/(d+2)}.}
\tag{4}
\]
No Hessian continuity away from the optimizer is required for (2)--(4); the proof integrates the one-dimensional second derivative along line segments, which exists almost everywhere.

### 3. Uniform PL inequality and quadratic growth

For every \(h\in\mathcal B_\varepsilon\),
\[
\boxed{
\|D\Phi_\varepsilon(h)\|_2^2
\ge 2m\bigl(\Phi_\varepsilon(h_\varepsilon)-\Phi_\varepsilon(h)\bigr),
}
\tag{5}
\]
and
\[
\boxed{
\Phi_\varepsilon(h_\varepsilon)-\Phi_\varepsilon(h)
\ge \frac m2\|h-h_\varepsilon\|_2^2.
}
\tag{6}
\]
Using the gradient relation between \(\Phi\) and the pair-space objective \(\Gamma\) established in González-Sanz--Nutz--Riveros Valdevenito (2026), the same PL lower bound remains valid with \(\|D\Gamma_\varepsilon(f,g)\|_{L^2(\mu)\times L^2(\nu)}\) on the left.

Under the smooth-marginal assumptions above, the explicit constant in Theorem 2.5 of the 2026 PL paper specializes, on the regime \(\|h-h_\varepsilon\|_\infty\le \varepsilon\), to a PL curvature coefficient of order \(\varepsilon^{3d+1}\). Equation (5) replaces that degenerating certificate by an \(O(1)\) coefficient under the stronger geometry assumptions, while enlarging the fixed-modulus \(L^\infty\) neighborhood from \(O(\varepsilon)\) to \(O(\varepsilon^{2/(d+2)})\).

### 4. Sharp local Hessian condition number

At the optimizer, the negative Hessian is well-defined under the stated smoothness assumptions and satisfies
\[
-D^2\Phi_\varepsilon(h_\varepsilon)[w,w]
=\frac1\varepsilon\int_{\{q_\varepsilon\ge0\}}w(x,y)^2\,d\mu d\nu.
\tag{7}
\]
Its extremal spectral scales on \(\mathcal H\) obey
\[
\boxed{
\lambda_{\min}(-D^2\Phi_\varepsilon(h_\varepsilon))\asymp 1,
\qquad
\lambda_{\max}(-D^2\Phi_\varepsilon(h_\varepsilon))\asymp \ell^{-2}.
}
\tag{8}
\]
Consequently,
\[
\boxed{
\kappa\bigl(-D^2\Phi_\varepsilon(h_\varepsilon)\bigr)
\asymp \ell^{-2}
=\varepsilon^{-2/(d+2)}.
}
\tag{9}
\]
Thus weak regularization does not make the softest local dual direction flatter: the smallest curvature remains bounded away from zero. The stiffness comes from the largest curvature, which grows on the inverse squared support-thickness scale.

For the linearized gradient-ascent map, (8) identifies the natural locally stable step scale as \(\Theta(\ell^2)\), with best fixed-step contraction factor \(1-\Theta(\ell^2)\). This is a local spectral statement; it does not by itself prove that nonlinear iterates initialized outside \(\mathcal B_\varepsilon\) enter or remain in that neighborhood.

## Proof

### A. Geometry of a fixed positive-slack core

The 2026 geometry paper proves the sharp section scale \(\ell\), uniform two-sided Hessian bounds for the transformed potentials, and the height estimate
\[
\max_y q_\varepsilon(x,y)\asymp\ell^2,
\qquad
\max_x q_\varepsilon(x,y)\asymp\ell^2.
\]
Its equation (4.33) gives, uniformly in the base point, an inner ball of radius \(b\ell\) on which
\[
q_\varepsilon\ge c_0\ell^2.
\]
After decreasing \(\theta>0\), this implies that the row and column degrees of \(E_\varepsilon\),
\[
d_X(x)=\nu\{y:(x,y)\in E_\varepsilon\},
\qquad
d_Y(y)=\mu\{x:(x,y)\in E_\varepsilon\},
\]
satisfy
\[
c\ell^d\le d_X(x),d_Y(y)\le C\ell^d.
\tag{10}
\]
The upper bounds use the outer support balls from Theorem 1.2.

A second ingredient is a uniform overlap estimate. The proof of Lemma 6.4 in the geometry paper shows that if \(|x-x'|\le a\ell\), an inner set of target points of measure at least \(c\ell^d\) has slack at least \(c_1\ell^2\) simultaneously for the two neighboring rows. Reducing \(a\) and \(\theta\) if necessary gives
\[
\nu(E_{\varepsilon,x}\cap E_{\varepsilon,x'})\ge c\ell^d
\qquad (|x-x'|\le a\ell),
\tag{11}
\]
where \(E_{\varepsilon,x}=\{y:(x,y)\in E_\varepsilon\}\). Interchanging the marginals gives the analogous column-overlap estimate.

### B. Core coercivity

Set
\[
I(u,v)=\int_{E_\varepsilon}(u(x)+v(y))^2\,d\mu d\nu.
\]
For fixed \(y\), minimizing over the scalar value \(v(y)\) gives the variance identity
\[
\int_{E_\varepsilon^y}(u(x)+v(y))^2\,d\mu(x)
\ge
\frac1{2d_Y(y)}
\iint_{E_\varepsilon^y\times E_\varepsilon^y}
(u(x)-u(x'))^2\,d\mu(x)d\mu(x').
\]
Integrating in \(y\), applying the degree upper bound in (10), and then using (11),
\[
I(u,v)
\ge c\iint_{|x-x'|\le a\ell}(u(x)-u(x'))^2\,d\mu(x)d\mu(x').
\tag{12}
\]
A standard finite-range Poincaré estimate on a bounded convex domain gives
\[
\iint_{|x-x'|\le a\ell}(u(x)-u(x'))^2\,d\mu(x)d\mu(x')
\ge c\ell^{d+2}\operatorname{Var}_\mu(u).
\tag{13}
\]
This is the natural-scale version of the chaining estimate used in Lemma 3.3 of the 2026 PL paper. Therefore
\[
I(u,v)\ge c\ell^{d+2}\operatorname{Var}_\mu(u).
\tag{14}
\]
By symmetry,
\[
I(u,v)\ge c\ell^{d+2}\operatorname{Var}_\nu(v).
\tag{15}
\]

It remains to control the mean component. Let
\[
M_E=(\mu\otimes\nu)(E_\varepsilon)\asymp\ell^d
\]
and normalize \(\mathbf1_{E_\varepsilon}\,d\mu d\nu/M_E\) to a probability measure. Its two marginals have densities bounded above and below by constants, by (10). Hence its expectation of \(u+v\) differs from \(\int u\,d\mu+\int v\,d\nu\) by at most a constant times
\(\sqrt{\operatorname{Var}_\mu(u)}+\sqrt{\operatorname{Var}_\nu(v)}\). Cauchy--Schwarz on the edge measure and (14)--(15) then yield
\[
\left(\int u\,d\mu+\int v\,d\nu\right)^2
\le C\ell^{-(d+2)}I(u,v).
\tag{16}
\]
Finally,
\[
\|u\oplus v\|_2^2
=\operatorname{Var}_\mu(u)+\operatorname{Var}_\nu(v)
+\left(\int u\,d\mu+\int v\,d\nu\right)^2.
\]
Combining (14)--(16) proves (1), since \(\ell^{d+2}=\varepsilon\).

### C. Strong concavity without Hessian continuity

Choose \(\rho<\theta/2\). If \(h\in\mathcal B_\varepsilon\), then on \(E_\varepsilon\)
\[
h(x,y)-c(x,y)
\ge q_\varepsilon(x,y)-\rho\ell^2>0.
\]
Thus the active set of every point of \(\mathcal B_\varepsilon\) contains the same core \(E_\varepsilon\).

For \(h_t=(1-t)h_0+th_1\), the one-dimensional function \(-\Phi_\varepsilon(h_t)\) is \(C^{1,1}\), and the standard positive-part differentiation formula gives for almost every \(t\)
\[
\frac{d^2}{dt^2}\bigl[-\Phi_\varepsilon(h_t)\bigr]
=\frac1\varepsilon
\int_{\{h_t\ge c\}}(h_1-h_0)^2\,d\mu d\nu.
\tag{17}
\]
The core inclusion and (1) make the right-hand side at least
\(m\|h_1-h_0\|_2^2\). Integrating (17) gives (2). This bypasses the Hessian-continuity difficulty explicitly noted in the earlier gradient-descent paper.

For the upper bound, the uniform lower Hessian bound on the transformed optimal potentials makes \(q_\varepsilon(x,\cdot)\) uniformly strongly concave. Its maximum is \(O(\ell^2)\). Hence
\[
q_\varepsilon(x,y)\ge-\rho\ell^2
\quad\Longrightarrow\quad
|y-\nabla u_\varepsilon(x)|\le C\ell,
\]
and symmetrically in the other coordinate. Therefore every active section throughout \(\mathcal B_\varepsilon\) has marginal measure \(O(\ell^d)\). For a balanced representative of \(w=u\oplus v\),
\[
\int_{\{h_t\ge c\}}(u+v)^2\,d\mu d\nu
\le C\ell^d\|u\oplus v\|_2^2.
\tag{18}
\]
Combining (17)--(18) gives the local smoothness scale \(L_\varepsilon\le C\ell^d/\varepsilon=C\ell^{-2}\), proving (4).

Strong concavity gives (6), and maximizing the strong-concavity upper tangent bound at \(h\) over the displacement to the maximizer gives (5).

### D. Sharp spectral scaling

The lower bound on \(\lambda_{\min}\) follows from (1) because \(E_\varepsilon\subset\{q_\varepsilon\ge0\}\). The upper bound on \(\lambda_{\max}\) follows from the \(O(\ell^d)\) support-section measures exactly as in (18).

For the matching lower bound on \(\lambda_{\max}\), use the constant direct-sum direction \(w\equiv1\). Its norm is one and
\[
\frac1\varepsilon\int_{\{q_\varepsilon\ge0\}}1\,d\mu d\nu
\asymp\frac{\ell^d}{\ell^{d+2}}=\ell^{-2}.
\tag{19}
\]

For a matching \(O(1)\) upper bound on \(\lambda_{\min}\), let \(T\) be the Brenier map and \(S=T^{-1}\). Choose a nonconstant affine scalar function \(a(x)=e\cdot x\) and set \(b(y)=-a(S(y))\). The support localization theorem gives \(|x-S(y)|\le C\ell\) on \(\spt\pi_\varepsilon\), while the product-space norm of \(a\oplus b\) is bounded below independently of \(\varepsilon\). Hence
\[
\frac1\varepsilon\int_{\{q_\varepsilon\ge0\}}(a(x)+b(y))^2\,d\mu d\nu
\le C\frac{\ell^{d+2}}{\varepsilon}\le C.
\tag{20}
\]
This completes (8)--(9).

## Exact periodic sanity model

The scaling in (8) can be seen explicitly in a one-dimensional translation-invariant model on the circle of length \(2\pi\) with normalized Haar measure. When the active radius is \(r<\pi\), the marginal equation gives
\[
r^3=3\pi\varepsilon.
\]
For Fourier mode \(k\ge1\), the two non-gauge Hessian eigenvalues are
\[
\lambda_k^{\pm}
=\frac1\varepsilon\left(\frac r\pi\pm\frac{\sin(kr)}{\pi k}\right).
\]
Thus
\[
\lambda_1^-
=\frac{r-\sin r}{\pi\varepsilon}\longrightarrow\frac12,
\]
whereas the constant gauge-orthogonal mode has
\[
\lambda_{\max}=\frac{2r}{\pi\varepsilon}=\frac6{r^2}.
\]
Hence \(\kappa r^2\to12\). The included artifact evaluates these formulas directly.

## Relation to prior work

- González-Sanz, Nutz and Riveros Valdevenito, *Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport* (arXiv:2509.08547), prove linear convergence and strict positive definiteness of the linearized curvature at a fixed \(\varepsilon\). Their discussion explicitly leaves a rigorous \(L^\infty\)-neighborhood quadratic-growth statement for future work and does not identify the small-\(\varepsilon\) spectral scaling.
- González-Sanz, Nutz and Riveros Valdevenito, *Polyak--Łojasiewicz Inequality for Quadratically Regularized Optimal Transport* (arXiv:2605.27175), prove a general local PL inequality under substantially weaker assumptions. Its explicit proof uses balls of radius \(O(\varepsilon)\), and its displayed constant degenerates rapidly as \(\varepsilon\downarrow0\).
- González-Sanz and Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I* (arXiv:2609.20400), prove the sharp section scale \(\ell=\varepsilon^{1/(d+2)}\), uniform Hessian bounds for the transformed potentials, positive-slack inner balls, overlap estimates, and sharp localization around the Brenier graph. The paper states that these findings can be used to upgrade the earlier PL and algorithmic analysis, but does not state the uniform core-coercivity theorem, the natural-scale strong-concavity neighborhood, or the \(\Theta(\varepsilon^{-2/(d+2)})\) dual-Hessian condition number derived here.

The contribution is therefore the synthesis of those sharp support-geometry estimates into a quantitative optimization theorem with the exact natural scales above. Originality is claimed only to the best of our knowledge.

## Limitations

The result uses the strong smoothness and uniform-convexity hypotheses of arXiv:2609.20400 and does not extend the \(\varepsilon\)-uniform constants to the weaker continuous/semi-discrete setting of arXiv:2605.27175. The local neighborhood is measured in the gauge-invariant \(L^\infty\) norm of the direct sum, not merely in \(L^2\). The linearized step-size conclusion does not prove basin entry or invariance for a nonlinear algorithm. The periodic calculation is a verification model, not part of the proof for bounded convex supports. The motivating geometry paper explicitly anticipates upgrades of the PL and algorithmic theory, so contemporaneous or unpublished overlapping work remains a material originality risk.

## Reproducibility

`artifacts/verify_torus_spectrum.py` evaluates the exact periodic Fourier formulas. `artifacts/verification_output.txt` records the output. The proof of the general theorem is analytic and does not depend on the computation.

## References

1. Alberto González-Sanz and Marcel Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I*, arXiv:2609.20400, 2026. https://arxiv.org/abs/2609.20400
2. Alberto González-Sanz, Marcel Nutz, and Andrés Riveros Valdevenito, *Polyak--Łojasiewicz Inequality for Quadratically Regularized Optimal Transport*, arXiv:2605.27175, 2026. https://arxiv.org/abs/2605.27175
3. Alberto González-Sanz, Marcel Nutz, and Andrés Riveros Valdevenito, *Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport*, arXiv:2509.08547, 2025/2026 revision. https://arxiv.org/abs/2509.08547
4. Dirk A. Lorenz, Paul Manns, and Christian Meyer, *Quadratically regularized optimal transport*, Applied Mathematics & Optimization 83 (2021), 1919--1949. https://doi.org/10.1007/s00245-019-09614-w
