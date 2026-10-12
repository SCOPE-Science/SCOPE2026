# Subcritical clearance coexists with divergent lifetime burden in a multi-order SEIATR model
## Finding
Consider the six-compartment SEIATR system of Elleuch and collaborators with independent Caputo orders \(0<\nu_j<1\). Write \(X=(S,E,I,A,T,R)\), \(N=S+E+I+A+T+R\), and
\[
g(t)=\lambda(t)S(t)=\frac{\beta S(t)[I(t)+\theta A(t)]}{N(t)}.
\]
Its equations are
\[
\begin{aligned}
{}^CD_t^{\nu_S}S&=b-dS-g,\\
{}^CD_t^{\nu_E}E&=g-(\sigma+d)E,\\
{}^CD_t^{\nu_I}I&=p\sigma E-(\kappa+r_I+d)I,\\
{}^CD_t^{\nu_A}A&=(1-p)\sigma E-(r_A+d)A,\\
{}^CD_t^{\nu_T}T&=\kappa I-(r_T+d)T,\\
{}^CD_t^{\nu_R}R&=r_I I+r_A A+r_T T-dR.
\end{aligned}
\]
Define
\[
K_E=\sigma+d,\qquad K_I=\kappa+r_I+d,\qquad
K_A=r_A+d,\qquad K_T=r_T+d
\]
and the source's next-generation threshold
\[
\mathcal R_0=\frac{\beta\sigma}{K_E}
\left(\frac{p}{K_I}+\frac{\theta(1-p)}{K_A}\right).
\]
For \(\mathcal R_0<1\), the disease-free equilibrium \((b/d,0,0,0,0,0)\) is globally asymptotically stable for all admissible initial conditions and every collection of real orders strictly between zero and one, without any rationality assumption. Yet, for any seed \(E(0)+I(0)+A(0)>0\) and \(\kappa>0\), all five literal ordinary-time integrals
\[
\int_0^\infty E(t)\,dt,\quad\int_0^\infty I(t)\,dt,\quad
\int_0^\infty A(t)\,dt,\quad\int_0^\infty T(t)\,dt,\quad
\int_0^\infty g(t)\,dt
\]
are infinite even though every infected and treated coordinate converges to zero. If the six Caputo orders are instead set to one, all five integrals are finite in the same subcritical regime.

## Assumptions and scope
The source parameters satisfy \(b,d,\beta,\sigma>0\), \(\kappa>0\), \(r_I,r_A,r_T\ge0\), \(0<p<1\), and \(0<\theta\le1\). Every order satisfies \(0<\nu_j<1\), and the intended incommensurate source case has at least two distinct orders; the proof also applies to equal orders in this range. Initial coordinates are nonnegative with \(N(0)>0\). The divergent-burden conclusion additionally requires \(E(0)+I(0)+A(0)>0\). We assume \(\mathcal R_0<1\), not the critical case.

The integrals use ordinary Lebesgue integration in the source's normalized time variable. Coefficients are the paper's effective normalized rates, and the theorem is not a claim that infinite numbers of physical infections or actual hospital admissions are observed. The model and result are deterministic; no claims concern estimation or finite-difference simulations.

## Proof
**1. Positive scalar resolvents.** For \(0<\nu<1\) and \(a>0\), define
\[
h_{\nu,a}(t)=E_\nu(-at^\nu),\qquad
k_{\nu,a}(t)=t^{\nu-1}E_{\nu,\nu}(-at^\nu).
\]
The scalar Caputo equation \({}^CD_t^\nu z=-az+f\) has the variation-of-constants representation
\[
z(t)=z(0)h_{\nu,a}(t)+(k_{\nu,a}*f)(t).
\]
The standard Mittag–Leffler complete-monotonicity theorem gives \(h_{\nu,a}\ge0\), \(k_{\nu,a}\ge0\), \(h_{\nu,a}(t)\to0\), and
\[
\int_0^\infty k_{\nu,a}(s)\,ds=\frac1a,
\qquad -h_{\nu,a}'(t)=a k_{\nu,a}(t).
\]
Moreover, the large-time expansion is
\[
h_{\nu,a}(t)\sim \frac{t^{-\nu}}{a\Gamma(1-\nu)}.
\]
In particular \(\int_0^\infty h_{\nu,a}(t)\,dt=+\infty\). These facts hold for irrational as well as rational \(\nu\). Nonnegative kernels give scalar positivity and an order-preserving response to forcing.

**2. Subcritical infected comparison.** Since the model remains nonnegative and \(N(t)>0\), its incidence obeys
\[
0\le g(t)\le \beta[I(t)+\theta A(t)].
\]
Let \(u=(E,I,A)^\mathsf T\), \(D=\operatorname{diag}(K_E,K_I,K_A)\), and
\[
C=\begin{pmatrix}
0&\beta&\beta\theta\\
p\sigma&0&0\\
(1-p)\sigma&0&0
\end{pmatrix},\qquad Q=D^{-1}C.
\]
The positive linear multi-order comparison system
\[
{}^CD_t^{\nu_i}y_i=-D_{ii}y_i+\sum_{j\ne i}C_{ij}y_j,
\qquad y(0)=u(0)
\]
majorizes \(u(t)\) componentwise, by the nonnegative-resolvent Volterra comparison principle (iterating its monotone integral representation on each bounded time interval). Direct matrix multiplication gives
\[
\det(zI-Q)=z(z^2-\mathcal R_0),\qquad
\rho(Q)=\sqrt{\mathcal R_0}<1.
\]
Consequently \(w=(I-Q)^{-1}{\bf1}\) has strictly positive coordinates and \((C-D)w=-D{\bf1}<0\). Choose \(M>0\) with \(u(0)\le Mw\). The constant vector \(Mw\) is a supersolution in the scalar-resolvent representation: because \(Cw\le Dw\) and \(h_{\nu,a}+a\int_0^t k_{\nu,a}(s)ds=1\), every Picard iterate starting below \(Mw\) remains below it. Therefore
\[
0\le u_i(t)\le y_i(t)\le Mw_i\qquad(t\ge0).
\]
Set \(L_i=\limsup_{t\to\infty}y_i(t)\). Since each kernel is integrable, convolution against a bounded function has limiting upper bound at most kernel mass times its upper limit; hence
\[
L_i\le\frac1{D_{ii}}\sum_{j\ne i}C_{ij}L_j,
\qquad L\le QL.
\]
Multiplying by \((I-Q)^{-1}\ge0\) yields \(L\le0\). As \(L\ge0\), this forces \(y(t)\to0\) and \(E(t),I(t),A(t)\to0\).

**3. Completion of global stability.** The treated coordinate has representation
\[
T(t)=T(0)h_{\nu_T,K_T}(t)
+\kappa(k_{\nu_T,K_T}*I)(t),
\]
so \(T(t)\to0\). Likewise, the recovered coordinate has a stable scalar resolvent driven by \(r_I I+r_A A+r_T T\to0\), so \(R(t)\to0\). Finally,
\[
S(t)=\frac bd+[S(0)-b/d]h_{\nu_S,d}(t)
-(k_{\nu_S,d}*g)(t),
\]
and since \(g(t)\to0\), the last convolution vanishes. Thus \(S(t)\to b/d\) and \(N(t)\to b/d>0\). The same uniform supersolution estimates show that small initial infected coordinates stay small, while the scalar stable resolvents bound deviations of \(S,T,R\); hence the disease-free equilibrium is Lyapunov stable. All admissible solutions are global: \(S\) is bounded above by its scalar equation without incidence, infected coordinates by \(Mw\), and \(T,R\) by stable scalar convolution bounds. Positivity and \(b>0\) keep \(N\) strictly positive on every finite interval. Combined with global attraction, this proves global asymptotic stability.

**4. Transfer of infinite ordinary-time mass.** If \(E(0)>0\), positivity of its forcing gives
\[
E(t)\ge E(0)h_{\nu_E,K_E}(t),
\]
whose integral diverges. Similarly, \(I(0)>0\) or \(A(0)>0\) implies divergence of its own time integral. Thus the nonzero seed produces an infinite integral in at least one of \(E,I,A\).

If \(\int_0^\infty E(t)dt=+\infty\), the relations
\[
I(t)\ge p\sigma(k_{\nu_I,K_I}*E)(t),\qquad
A(t)\ge(1-p)\sigma(k_{\nu_A,K_A}*E)(t)
\]
and Tonelli's theorem transfer divergence to both \(I\) and \(A\), because each positive kernel has strictly positive finite mass. If instead \(I\) or \(A\) initially has the divergent integral, then \(S(t)/N(t)\to1\), so for sufficiently large \(t\),
\[
g(t)\ge \frac\beta2[I(t)+\theta A(t)].
\]
It follows that \(\int_0^\infty g(t)dt=+\infty\). Then
\[
E(t)\ge(k_{\nu_E,K_E}*g)(t)
\]
transfers divergence to \(E\), from which it propagates to \(I\) and \(A\). In all cases \(\int_0^\infty g(t)dt=+\infty\). Finally, \(\kappa>0\) and
\[
T(t)\ge\kappa(k_{\nu_T,K_T}*I)(t)
\]
force \(\int_0^\infty T(t)dt=+\infty\). Thus all five asserted nonnegative integrals diverge, despite convergence of their integrands to zero.

**5. Classical boundary.** If all six orders are set to one, the corresponding infected linear majorant is \(y(t)=e^{(C-D)t}u(0)\). Since \(C-D\) is an irreducible Metzler matrix and \(\rho(D^{-1}C)<1\), its spectral abscissa is strictly negative. Hence \(E,I,A\) and \(g\) are bounded by exponentially integrable functions. The treated ordinary differential equation is a stable exponential filter of \(I\), making \(T\) integrable as well. This establishes the strict fractional-versus-classical contrast within the same parameter regime.

## Verification
The standalone checker `verification/verify.py` reconstructs the next-generation comparison matrix from the six source equations, verifies \(\det(zI-Q)=z(z^2-\mathcal R_0)\), checks \((C-D)(I-Q)^{-1}{\bf1}=-D{\bf1}\) symbolically, and replays a strictly positive-rates rational example with \(\mathcal R_0=1/24\). It also checks the exact stable classical eigenvalue condition for that example. These finite computations corroborate the algebra; the uniform convergence and infinite-tail claims follow from the general proof above, not from numerical horizon extrapolation.

For a concrete incommensurate instance, take
\[
(b,d,\beta,\sigma,p,\theta,\kappa,r_I,r_A,r_T)
=(2,1,1/5,1,1/2,1/2,1/2,1/2,1/2,1/2),
\]
with \((\nu_S,\nu_E,\nu_I,\nu_A,\nu_T,\nu_R)=(3/4,1/2,2/3,3/5,4/5,7/10)\) and initial state \((S,E,I,A,T,R)=(2,1,0,0,0,0)\). Then \(\mathcal R_0=1/24\), so all infected and treated states tend to zero while all five integrals still diverge.

## Relationship to prior work
Elleuch et al. (2026) derive the same six-compartment equations, well-posedness, threshold and a local rational-order stability test, and examine cumulative treatment burden over finite simulated horizons. They do not establish a global subcritical clearance result for arbitrary real unequal orders or classify the literal infinite-horizon integrals.

Oumedjber et al. (2026) prove global disease-free stability for a closely related six-compartment **commensurate** Caputo SEIATR model by a single-order weighted Lyapunov function; their result does not directly apply when different equations carry different fractional orders, and it does not determine the nonintegrable all-time burden. The incommensurate two-class SI reaction–diffusion model of Aloui et al. (2026) includes disease-free stability theorems but has neither the exposed/symptomatic/asymptomatic transfer network nor the treated burden. The complete-monotonicity and power-tail properties of Mittag–Leffler functions are established prior mathematical tools, not asserted to be new. The contribution is the exact combined clearance-versus-infinite-burden classification for the source's entire treatment network under its epidemic threshold.

## Limitations
This is an analytic consequence of an idealized Caputo system with all six orders strictly less than one, not a forecast for measured cumulative cases or hospital admissions. Rates are interpreted according to the source's effective normalized-time convention, so unweighted ordinary-time integrals need not equal empirical cumulative event counts. The theorem requires a nonzero seed in \(E,I,A\), \(\kappa>0\), and strictly subcritical \(\mathcal R_0<1\). If \(\kappa=0\), the treated-coordinate divergence need not hold; if no infection is initially present, none of the infection-induced integrals need diverge. It does not settle \(\mathcal R_0=1\), supercritical dynamics, fractional orders equal to one in a mixed-order tuple, or spatially heterogeneous models. It does not question the source's finite-horizon numerical experiments.

## References
1. Z. Elleuch et al., “Incommensurate fractional epidemic dynamics with compartment-specific memory, treatment response, and physics-informed forecasting,” *AIMS Mathematics* 11(7) (2026), 22316–22353. DOI: 10.3934/math.2026903.
2. Y. B. Oumedjber et al., “Fractional Epidemic Dynamics With Memory: Rigorous Analysis, Data-Constrained Learning, and Physics-Informed Forecasting,” *Computational and Mathematical Methods* (2026), article 3732177. DOI: 10.1155/cmm4/3732177.
3. A. Aloui et al., “The Fractional SI Reaction–Diffusion Model with Incommensurate Orders: Stability Analysis and Numerical Simulations,” *Fractal and Fractional* 10 (2026), article 3. DOI: 10.3390/fractalfract10010003.
4. H. Pollard, “The completely monotonic character of the Mittag-Leffler function,” *Bulletin of the American Mathematical Society* 54 (1948), 1115–1116. DOI: 10.1090/S0002-9904-1948-09132-7.
5. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
