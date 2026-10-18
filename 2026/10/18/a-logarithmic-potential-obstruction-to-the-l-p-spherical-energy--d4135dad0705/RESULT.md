# A logarithmic-potential obstruction to the \(L_p\)-spherical energy conjecture

## Finding

Let \(\mu_p\), for \(p>1\), be the bivariate \(L_p\)-spherical probability measure on \([-1,1]^2\) with both marginals uniform on \([-1,1]\). For any probability measure \(\mu\) on that square, let \(\mathcal E_\beta(\mu)=\iint\|z-w\|_2^\beta\,\mu(dz)\mu(dw)\), for \(0<\beta<2\).

**Theorem.** There exist \(\beta_0>0\), a smooth function \(g\) compactly supported in \((-1/4,1/4)^2\) whose two one-dimensional marginal integrals both vanish, and a fixed nonzero real \(t\), such that for every \(0<\beta<\beta_0\):

1. \(d\nu_\beta(z)=(f_{3-\beta}(z)+t g(z))\,dz\) is a probability measure with both marginals uniform on \([-1,1]\), where \(f_p\) is the density of \(\mu_p\).
2. \(\mathcal E_\beta(\nu_\beta)>\mathcal E_\beta(\mu_{3-\beta})\).

Consequently the proposed \(p=3-\beta\) optimizer in Conjecture 9 of Bernard, Müller and Oesting is not optimal for *any sufficiently small positive* \(\beta\). The theorem does not supply a numerical value for \(\beta_0\), nor the globally optimal copula.

## Assumptions and scope

For \(p>1\) define \(B_p=\{(x,y): |x|^p+|y|^p<1\}\) and
\[
f_p(x,y)=\frac{\mathbf 1_{B_p}(x,y)}{4\Gamma(1-1/p)\Gamma(1+1/p)}\bigl(1-|x|^p-|y|^p\bigr)^{-1/p}.
\]
This is the centered version of the circular bivariate \(L_p\)-spherical copula in the cited paper. Its marginals have density \(1/2\) on \((-1,1)\), as follows by substituting \(y=(1-|x|^p)^{1/p}v\) and using
\[
\int_0^1(1-v^p)^{-1/p}\,dv=\Gamma(1+1/p)\Gamma(1-1/p).
\]
The affine change \((x,y)\mapsto((x+1)/2,(y+1)/2)\) produces an ordinary copula and only rescales the expected power distance by \(2^{-\beta}\); hence comparisons are identical in the two coordinate systems. All probability measures compared in the theorem have exactly the same uniform marginals.

## Proof

**1. The limiting logarithmic potential.** Put \(Q=(-1/4,1/4)^2\), \(\mu_0:=\mu_3\), and
\[
L(z)=\int\log\|z-w\|_2\,\mu_3(dw),\qquad z\in Q.
\]
The logarithmic singularity is locally integrable in two dimensions, and \(f_3\) is locally bounded on \(Q\); therefore \(L\) is continuous there. Distributionally, the planar fundamental-solution identity gives
\[
\Delta L(z)=2\pi f_3(z)\quad\text{on }Q,
\]
because \(\Delta\log\|z\|_2=2\pi\delta_0\).

**2. This potential is not additively separable.** If \(L(x,y)=A(x)+B(y)\) on \(Q\), then \(\Delta L=A''(x)+B''(y)\) there, so the continuous function \(f_3\) would also be a sum of a function of \(x\) and a function of \(y\). That is impossible. Indeed, set \(a=1/8\), \(s=a^3\), \(h(u)=(1-u)^{-1/3}\), and \(K_3=[4\Gamma(2/3)\Gamma(4/3)]^{-1}>0\). All four points in the following difference lie in \(Q\), and
\[
f_3(a,a)+f_3(0,0)-f_3(a,0)-f_3(0,a)
=K_3\,[h(2s)+h(0)-2h(s)]>0,
\]
since \(h''(u)=\frac49(1-u)^{-7/3}>0\) for \(0\le u\le 2s\). Every additively separable function has zero such rectangle difference. Thus \(L\) is not additively separable on \(Q\).

**3. A smooth perturbation preserving both marginals.** Nonseparability and continuity yield \(x_1,x_2,y_1,y_2\in Q\) for which the rectangle difference of \(L\) is nonzero. Choose smooth nonnegative unit-integral bumps \(u_i\), respectively \(v_j\), supported sufficiently close to \(x_i\), respectively \(y_j\), so that
\[
g(x,y)=[u_1(x)-u_2(x)][v_1(y)-v_2(y)],\qquad A_0:=\int_Q L(z)g(z)\,dz\ne0.
\]
Then \(\int g(x,y)\,dy=\int g(x,y)\,dx=0\) for all \(x,y\), and also \(\int g=0\). The densities \(f_p\), for \(2\le p\le3\), are uniformly bounded away from zero on the compact support of \(g\). Therefore any sufficiently small fixed \(|t|>0\) leaves \(f_{3-\beta}+tg\) nonnegative for all \(0<\beta<1\), with its marginal densities unchanged.

**4. Convergence of the first variation.** For \(p=3-\beta\), let
\[
\Phi_\beta(z)=\int\|z-w\|_2^\beta\,\mu_{3-\beta}(dw).
\]
As \(\beta\downarrow0\), the measures \(\mu_{3-\beta}\) converge weakly to \(\mu_3\). One way to see this is the conditional representation: \(|X|\) is uniform on \((0,1)\), the two signs are independent fair signs, and, given \(|X|=u\),
\[
|Y|=(1-u^p)^{1/p}V_p^{1/p},\qquad V_p\sim\operatorname{Beta}(1/p,1-1/p).
\]
The law in this representation depends continuously on \(p\) near \(3\). Moreover, for each fixed \(z\in Q\),
\[
\frac{\Phi_\beta(z)-1}{\beta}\longrightarrow L(z).
\]
To justify the logarithmic singularity, on a sufficiently small disk about \(z\), all \(f_p\) near \(p=3\) are uniformly bounded, so \(\int_{\|z-w\|<\delta}|\log\|z-w\||\,\mu_p(dw)\) tends uniformly to zero as \(\delta\downarrow0\). Away from that disk, the difference quotient of \(r^\beta\) converges uniformly to \(\log r\). The same estimates, with \(z\) ranging over the fixed compact support of \(g\), show
\[
\frac1\beta\int\Phi_\beta(z)g(z)\,dz\longrightarrow A_0,
\]
using \(\int g=0\). Also, since \(g\) is bounded and compactly supported,
\[
\frac1\beta\iint\|z-w\|_2^\beta g(z)g(w)\,dz\,dw
\longrightarrow B_0:=\iint\log\|z-w\|_2\,g(z)g(w)\,dz\,dw,
\]
which is finite; the constant term again vanishes because \(\int g=0\).

**5. Strict improvement.** The quadratic expansion of energy is exact:
\[
\mathcal E_\beta(\mu_{3-\beta}+tg\,dz)-\mathcal E_\beta(\mu_{3-\beta})
=2t\int\Phi_\beta(z)g(z)\,dz
+t^2\iint\|z-w\|_2^\beta g(z)g(w)\,dz\,dw.
\]
After division by \(\beta\), its limit as \(\beta\downarrow0\) is \(2tA_0+t^2 B_0\). Choose the sign of the fixed, nonzero \(t\) to agree with \(A_0\), and its magnitude small enough both to preserve density positivity and to ensure \(2tA_0+t^2B_0>0\). The original energy difference is therefore strictly positive for every sufficiently small \(\beta>0\). This proves the theorem.

## Verification

The obstruction needs no finite-domain census or floating-point inference. The key verifiable identity is \(\Delta\log\|z\|_2=2\pi\delta_0\); the decisive strict sign is the positive second difference of \(h(u)=(1-u)^{-1/3}\) at \(0,s,2s\), with \(s=1/512\). Because \(h''\ge4/9\) on that interval, the difference is strictly larger than \(4s^2/9\). The accompanying standalone checker reproduces this elementary algebraic sign check and a high-precision diagnostic. The full conclusion for a continuum of exponents follows from the analytic limit and the signed perturbation proof, not from numerical tests.

## Relationship to prior work

Bernard, Müller and Oesting (first public arXiv version, June 21, 2022) introduced the \(L_p\)-spherical copulas, established their bivariate density, and formulated Conjecture 9 that \(p=3-\beta\) maximizes the generalized expected distance for all \(0<\beta<2\). The present theorem contradicts the universal quantifier of that conjecture near the endpoint \(\beta=0\). Their distributional construction and marginal identities remain valid.

Bernard and Müller (2020) establish the spherical maximizer at the specific exponent \(\beta=1\); this does not cover the small positive exponents treated here. Perlman and Wellner (2011) characterize the Euclidean circular copula, not the proposed \(p=3-\beta\) power-energy optimizer. The argument exploits the two-dimensional logarithmic potential rather than a comparison of a finite set of numerical candidate energies.

## Limitations

The proof establishes existence of a fixed smooth, margin-preserving perturbation and some positive exponent interval, but does not give explicit locations for the bump supports, a numerical \(\beta_0\), the largest interval of failure, the optimum energy, or the maximizing copula. It does not negate the proved \(\beta=1\) optimality result. Priority among as-yet-uninspected works under different terminology remains a bibliographic uncertainty; no independent audit has been performed.

## References

1. C. Bernard, A. Müller, M. Oesting, *\(L_p\)-norm spherical copulas*, arXiv:2206.10180v1 (2022), Section 3 and Conjecture 9. https://arxiv.org/abs/2206.10180 . Journal of Multivariate Analysis 201 (2024), 105262, https://doi.org/10.1016/j.jmva.2023.105262 .
2. C. Bernard, A. Müller, *Dependence uncertainty bounds for the energy score and the multivariate Gini mean difference*, arXiv:2004.11770v1 (2020), Theorem 11. https://arxiv.org/abs/2004.11770 .
3. M. D. Perlman, J. A. Wellner, *Squaring the Circle and Cubing the Sphere: Circular and Spherical Copulas*, Symmetry 3 (2011), 574–599. https://doi.org/10.3390/sym3030574 .
