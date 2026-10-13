# Strong self-shading selects a unique phytoplankton equilibrium and its first nutrient correction

## Finding
Fix all positive biological and transport parameters of the disease-free phytoplankton–nutrient subsystem (3.16) of Zhang–Yan–Shi [1], with any finite advection velocity \(\omega\in\mathbb R\). Assume its phytoplankton invasion eigenvalue is strictly positive (the \(R_p>1\) regime of [1]). Let \(\kappa>0\) be the coefficient of phytoplankton self-attenuation in the Lambert–Beer light law, with every other parameter fixed. **There is a finite \(\kappa_0\) such that, for every \(\kappa>\kappa_0\), the subsystem has exactly one strictly positive stationary pair \((S_\kappa,N_\kappa)\).** As \(\kappa\to\infty\), uniformly through two spatial derivatives,
\[
 S_\kappa(x)=\kappa^{-1}u_*(x)+O(\kappa^{-2}),\qquad
 N_\kappa(x)=N^0-\kappa^{-1}n_*(x)+O(\kappa^{-2}).
\]
Here \(u_*>0\) is the **unique** positive solution of the light-only nonlocal boundary-value problem explicitly defined below, and \(n_*>0\) is the explicitly integrated first nutrient-depletion profile. Consequently, the invasion eigenvalue is independent of \(\kappa\), even though the unique equilibrium phytoplankton standing crop tends to zero at the exact inverse-attenuation scale, while the nutrient concentration approaches the input concentration with an explicit nonzero first-order deficit. The threshold \(\kappa_0\) is asserted to exist, not calculated.

## Assumptions and scope
Let the water-column depth be \(X>0\), and put \(d_p,d_n,r,\mu_p,\eta,c_p,\gamma,h,L^0,N^0,l_0,\alpha>0\), with \(\omega\in\mathbb R\). For \(z\ge0\) define \(g(z)=z/(\gamma+z)\), \(f(z)=z/(h+z)\), and, for a biomass profile \(S\),
\[
 \mathcal L_\kappa[S](x)=L^0\exp\!\left(-l_0x-\kappa\int_0^x S(s)\,ds\right).
\]
A **strictly positive disease-free stationary pair** means two \(C^2([0,X])\) functions \(S,N>0\) solving
\[
\begin{aligned}
0&=d_pS''-\omega S'+\bigl[r g(N)f(\mathcal L_\kappa[S])-\mu_p-\eta S\bigr]S,\\
0&=d_nN''-c_prg(N)f(\mathcal L_\kappa[S])S,
\end{aligned}
\]
with \(d_pS'(0)-\omega S(0)=d_pS'(X)-\omega S(X)=0\), \(N'(0)=0\), and \(d_nN'(X)=\alpha(N^0-N(X))\). This is precisely the \(I=V=0\) subsystem of [1], not the full infected dynamics.

Let \(\mathcal D\phi=d_p\phi''-\omega\phi'\) with the same zero-flux boundary conditions, and assume the principal eigenvalue of
\[
 \mathcal D+r g(N^0) f(L^0e^{-l_0x})-\mu_p
\]
is **strictly positive**. This is equivalent to the \(R_p>1\) condition used for phytoplankton invasion in [1]. Notice that its coefficients do not involve \(\kappa\).

The limiting biomass profile \(u_*\) is defined by
\[
\begin{aligned}
0&=d_pu_*''-\omega u_*'+\left[r g(N^0)f(\Lambda_*(x))-\mu_p\right]u_*,\\
\Lambda_*(x)&=L^0\exp\!\left(-l_0x-\int_0^x u_*(s)\,ds\right),\\
d_pu_*'(0)-\omega u_*(0)&=d_pu_*'(X)-\omega u_*(X)=0.
\end{aligned}
\]
The existence and uniqueness of this scalar steady state follow also from the light-only analysis of Hsu and Lou [2]; an independent uniqueness argument is supplied below. Define
\[
 F_*(x)=f(\Lambda_*(x))u_*(x),\quad
 n_*(x)=c_prg(N^0)\left[\frac1\alpha\int_0^X F_*(y)\,dy+\frac1{d_n}\int_x^X\!\int_0^s F_*(y)\,dy\,ds\right].
\]
All convergence and error estimates are in \(C^2([0,X])\) for fixed parameters. No assertion about uniqueness for arbitrary finite \(\kappa\), local stability, or the infected subsystem is made.

## Proof
**1. A uniform photon budget.** At every strictly positive steady state, the nutrient maximum principle gives \(0<N(x)<N^0\) [1, Lemma 3.5]. Integration of the first stationary equation against \(1\) cancels the zero-flux terms and yields
\[
 \mu_p\int_0^X S+\eta\int_0^X S^2
 =r\int_0^X g(N)f(\mathcal L_\kappa[S])S.
\]
Differentiating the Lambert–Beer expression gives the **exact identity**
\[
 \log\frac{h+L^0}{h+\mathcal L_\kappa[S](X)}
 =l_0\int_0^X f(\mathcal L_\kappa[S])\,dx
 +\kappa\int_0^X Sf(\mathcal L_\kappa[S])\,dx.
\]
Set \(u_\kappa=\kappa S_\kappa\). Positivity and monotonicity of \(g\) imply the uniform bound
\[
 0<\int_0^X u_\kappa(x)\,dx\le
 \frac{r g(N^0)}{\mu_p}\log\left(1+\frac{L^0}{h}\right)=:M.
\]
This holds simultaneously for **every** positive steady state and every \(\kappa>0\), rather than for a chosen branch. The nutrient equation and its mixed Neumann–Robin boundary data then give, by two integrations,
\[
 \|N_\kappa-N^0\|_{C^2}\le C\kappa^{-1},
\]
where the first derivative and second derivative bounds follow from \(d_nN_\kappa''=c_pr\kappa^{-1}g(N_\kappa)f(\Lambda_\kappa)u_\kappa\) once the next uniform pointwise estimate is obtained. Initially the mass bound already gives \(\|N_\kappa-N^0\|_{C^1}=O(\kappa^{-1})\).

**2. Pointwise compactness for all equilibria.** Write \(\Lambda_\kappa(x)=L^0\exp(-l_0x-\int_0^x u_\kappa)\) and \(\mathcal D=d_p\partial_{xx}-\omega\partial_x\), with the zero-flux boundary conditions. The rescaled biomass equation is
\[
 (\mu_p-\mathcal D)u_\kappa=
 \left[r g(N_\kappa)f(\Lambda_\kappa)-\frac{\eta}{\kappa}u_\kappa\right]u_\kappa
 \le r g(N^0)f(L^0)u_\kappa.
\]
The positive resolvent \((\mu_p-\mathcal D)^{-1}\) on the compact one-dimensional interval has a bounded nonnegative Green kernel \(G(x,y)\): its existence follows from \(\mu_p>0\) and the reflecting diffusion semigroup, or directly from the second-order Green formula. Applying it to the pointwise inequality yields
\[
 \|u_\kappa\|_\infty\le
 r g(N^0)f(L^0)\,\|G\|_\infty M=:M_\infty.
\]
This uniform pointwise bound, the equations, and the boundary data bound all first and second derivatives of \(u_\kappa,N_\kappa\) uniformly for \(\kappa\ge1\). In particular the profiles are precompact in \(C^1\), and the equations upgrade convergent subsequences to \(C^2\). Every limit along \(\kappa\to\infty\) has \(N=N^0\) and a nonnegative solution \(u\) of the scalar limiting problem. Such a limit cannot be zero. Otherwise normalize \(u_\kappa/\|u_\kappa\|_\infty\); its subsequential positive limit would solve the **linearized invasion eigenproblem with eigenvalue zero**, contradicting the assumed strictly positive principal eigenvalue. The strong maximum principle makes every nonzero limit strictly positive.

**3. Exactly one positive scalar limiting profile.** Existence is provided by the established scalar single-phytoplankton theorem [2, Theorem 1] under the same positive principal-eigenvalue condition. To verify uniqueness directly, suppose \(u_1,u_2>0\) are scalar solutions and \(u_1(0)>u_2(0)\). Write \(H_j(x)=\int_0^xu_j\), \(A_j(x)=r g(N^0)f(L^0e^{-l_0x-H_j(x)})\), and \(W=u_1'u_2-u_1u_2'\). Both zero-flux conditions imply \(W(0)=W(X)=0\). Subtraction of the two equations gives
\[
 W'(x)=\frac\omega{d_p}W(x)+\frac{A_2(x)-A_1(x)}{d_p}u_1(x)u_2(x).
\]
As long as \(u_1>u_2\), \(H_1>H_2\) for \(x>0\), so \(A_1<A_2\) and \(W>0\) for \(x>0\). Consequently \((u_1/u_2)'=W/u_2^2>0\), which preserves \(u_1>u_2\) throughout the interval; but \(W(X)>0\) contradicts the boundary condition. Reverse the indices to rule out \(u_2(0)>u_1(0)\). Equal initial values give equal first derivatives and the same initial accumulated biomass, so ordinary differential equation uniqueness implies \(u_1=u_2\). Denote the unique solution by \(u_*\). By Step 2, **every** family of positive equilibria satisfies \(u_\kappa\to u_*\) and \(N_\kappa\to N^0\) in \(C^2\).

**4. Nondegeneracy and eventual uniqueness for the coupled system.** Put \(\varepsilon=\kappa^{-1}\) and introduce \(H'=u\), \(H(0)=0\). Write the steady equations as a smooth five-dimensional shooting initial-value system for \((u,u',N,N',H)\), parametrized by \(a=u(0)>0\), \(b=N(0)>0\), and \(\varepsilon\), using the initial slopes \(u'(0)=\omega a/d_p\), \(N'(0)=0\). At depth \(X\) define the residuals
\[
 \mathcal F(a,b,\varepsilon)=d_pu'(X)-\omega u(X),\qquad
 \mathcal G(a,b,\varepsilon)=d_nN'(X)-\alpha\bigl(N^0-N(X)\bigr).
\]
At \((a,b,\varepsilon)=(u_*(0),N^0,0)\), both vanish. Since \(N\equiv b\) when \(\varepsilon=0\), \(\mathcal G_a=0\) and \(\mathcal G_b=\alpha>0\). We now check the critical derivative \(\mathcal F_a>0\), rather than assuming it. Differentiating the limiting scalar IVP with respect to \(a\) gives \(z=\partial_a u\), \(j=\partial_a H=\int_0^x z\), with \(z(0)=1\), \(z'(0)=\omega/d_p\). Let \(W=z'u_*-zu_*'\). Because the light-growth coefficient \(A(x,H)=r g(N^0)f(L^0e^{-l_0x-H})\) satisfies \(A_H<0\),
\[
 W'=\frac\omega{d_p}W-\frac{A_H(x,H_*)}{d_p}u_*^2j,
 \qquad W(0)=0.
\]
An initial positive \(z\), the identity \((z/u_*)'=W/u_*^2\), and \(j'=z\) give by continuation \(z>0\), \(j>0\), and \(W>0\) for \(0<x\le X\). Therefore
\[
 \mathcal F_a=\frac{d_pW(X)}{u_*(X)}>0.
\]
The Jacobian of \((\mathcal F,\mathcal G)\) with respect to \((a,b)\) is consequently nonsingular at \(\varepsilon=0\). The finite-dimensional implicit-function theorem gives one smooth positive steady branch for all sufficiently small \(\varepsilon\ge0\), unique in a fixed neighborhood of \((u_*,N^0)\). Step 2 puts **every** positive coupled stationary solution in this neighborhood when \(\varepsilon\) is sufficiently small. Thus this is the **only** positive equilibrium for all sufficiently large \(\kappa\).

**5. First nutrient correction and rates.** Smooth dependence in the same shooting system gives \(u_\kappa=u_*+O(\kappa^{-1})\) in \(C^2\). Set \(n_\kappa=\kappa(N^0-N_\kappa)\). Its differential equation and boundary data are
\[
 -d_n n_\kappa''=c_prg(N_\kappa)f(\Lambda_\kappa)u_\kappa,
 \quad n_\kappa'(0)=0,
 \quad d_n n_\kappa'(X)=-\alpha n_\kappa(X).
\]
Taking the first derivative of the smooth branch at \(\varepsilon=0\) yields the unique solution \(n_*\) displayed in the assumptions; two integrations give that formula directly. Hence \(n_\kappa=n_*+O(\kappa^{-1})\) in \(C^2\). Since \(n_*>0\), the first-order nutrient deficit and the positive inverse-shading standing-crop coefficient are nonzero. This proves all assertions. \(\square\)

## Verification
The derivation uses exact differentiation of the Lambert–Beer law, a positive one-dimensional elliptic resolvent, a zero-flux Wronskian identity, and a nonsingular two-parameter shooting Jacobian. The accompanying `verify.py` solves the limiting three-state and full five-state boundary-value problems numerically for one nonzero advection and checks their convergence, boundary conditions, and the photon identity at five attenuation coefficients; it prints `VERIFY_OK`. The computation corroborates, but does **not** establish, existence, uniqueness, all-parameter convergence, or the implicit-function argument. The mathematical proof above supplies those infinite-domain assertions.

## Relationship to prior work
Zhang–Yan–Shi [1, Theorem 3.6] prove existence of positive disease-free states in the \(R_p>1\) regime and local stability of a branch near the invasion threshold; they expressly state that disease-free **uniqueness for general supercritical parameters is unknown**. The claim here is not unrestricted uniqueness: it proves it in the natural **strong self-shading regime**, and gives the joint biomass–nutrient singular expansion. Hsu–Lou [2, Theorem 1] already prove existence and uniqueness of the **scalar, light-only** steady state, so uniqueness of \(u_*\) alone is **not** claimed as new. Their model does not contain the coupled nutrient BVP or the crowding contribution at positive \(\kappa^{-1}\), and its results do not imply uniqueness for all sufficiently large finite \(\kappa\) of [1] or the first-order nutrient profile. Pang–Nie–Wu [3] analyze a light–crowding **single-field** model for small crowding and large advection; the available abstract does not document a coupled nutrient strong-shading limit, but its full text could not be verified here. Zagaris et al. [4] investigate the linear invasion/first-pattern problem of a different coupled nutrient model; the inspected material does not state this exact nonlinear high-absorption uniqueness/expansion.

## Limitations
The threshold \(\kappa_0\) is nonconstructive and parameter-dependent. The theorem concerns positive **stationary disease-free profiles only**: no local/global stability is asserted, nor any assertion about endemic equilibria, viral invasion, time-periodic solutions, or finite \(\kappa\) below the threshold. The limit requires positive mortality \(\mu_p\), strictly increasing light growth, fixed positive nutrient supply and exchange, fixed transport coefficients, and strict invasion supercriticality. It does not cover the critical invasion eigenvalue, simultaneous diffusion limits, or photoinhibition. The mathematical originality assessment remains subject to possible equivalent results not indexed or present in inaccessible related full texts; no independent audit has occurred.

## References
[1] J. Zhang, Y. Yan and J. Shi, *Modelling phytoplankton-virus interactions: phytoplankton blooms and lytic virus transmission*, Journal of Mathematical Biology **88** (2024), article 77, doi:10.1007/s00285-024-02093-w. Open author PDF: https://jxshix.people.wm.edu/shi/2024-Zhang-Yan-Shi-JMB.pdf. Published online 2024-05-02; Section 2 and Theorem 3.6.

[2] S.-B. Hsu and Y. Lou, *Single Phytoplankton Species Growth with Light and Advection in a Water Column*, SIAM Journal on Applied Mathematics **70** (2010), 2942–2974, doi:10.1137/100782358, Theorem 1 (light-only scalar uniqueness).

[3] D. Pang, H. Nie and J. Wu, *Single phytoplankton species growth with light and crowding effect in a water column*, Discrete and Continuous Dynamical Systems **39** (2019), 41–74, doi:10.3934/dcds.2019003 (publisher abstract/figures and references accessible; full comparison incomplete).

[4] A. Zagaris, A. Doelman, N. N. Pham Thi and B. P. Sommeijer, *Blooming in a Nonlocal, Coupled Phytoplankton-Nutrient Model*, SIAM Journal on Applied Mathematics **69** (2009), 1174–1204, doi:10.1137/070693692.
