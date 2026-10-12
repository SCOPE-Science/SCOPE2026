# High-resource predator-invasion limits and reentrant invasion under smooth maturation

## Finding

In the age-structured role-reversal predator–prey renewal model of Suarez, Cameron, Fagan, and Levy [1], the predator-free prey abundance is \(X=r/a>0\). The adult and juvenile maturation weights are
\[
A_\nu(z)=\frac{1}{1+e^{-\nu(z-T)}},\qquad
J_\nu(z)=\frac{1}{1+e^{\nu(z-T)}}=1-A_\nu(z),\qquad z\geq0,
\]
where \(T>0\) is maturation age and \(0<\nu<\infty\) is its smoothness parameter. Write \(F(X)=X\) for the paper's original adult-feeding birth law, or \(F(X)=h\tanh(X/h)\) with \(h>0\) for its suggested saturated variant. More generally suppose \(F\) is continuous, nonnegative, \(F(0)=0\), \(F(X)=O(X)\) as \(X\downarrow0\), and \(F(X)/X\to L\in[0,\infty)\) as \(X\to\infty\).

For the positive baseline mortality \(\mu_B(z)\equiv m>0\), let \(\tilde B\) be nonnegative, bounded and integrable, supported on \([T,\infty)\). Fix \(g,k,\mu_M,\rho,\zeta>0\). The exact predator invasion reproduction integral is
\[
\mathcal R_F(X)=\int_0^\infty
\left[kF(X)A_\nu(z)+(1-e^{-\zeta X})\tilde B(z)\right]
\exp\!\left[-(m+\mu_Me^{-\rho X})z-gX\int_0^z J_\nu(s)\,ds\right]dz.
\]
Then \(\mathcal R_F\) is continuous on \((0,\infty)\), and its *sharp two-endpoint limits* are
\[
\boxed{\lim_{X\downarrow0}\mathcal R_F(X)=0,\qquad
\lim_{X\to\infty}\mathcal R_F(X)=\frac{ kL}{g}e^{-\nu T}.}
\]
For the original, linear prey-to-birth law \(F(X)=X\), the large-resource limit is strictly positive, \((k/g)e^{-\nu T}\), despite increasingly strong juvenile predation. For the saturated birth law \(F(X)=h\tanh(X/h)\), it is zero. These distinctions concern the exact smooth age model and do not arise by replacing the maturation weights with sharp characteristic functions before taking the high-resource limit.

**An explicit double invasion transition exists for both birth laws.** Fix
\[
T=1,\ \nu=10,\ g=\frac1{100},\ k=3,\ m=\frac1{10},\
\mu_M=\frac1{100},\ \rho=\zeta=1,
\qquad
\tilde B(z)=\frac{(z-1)e^{-(z-1)}}{100}\mathbf1_{\{z\geq1\}}.
\]
Use the prey equation \(\dot x=x(r-ax+s y_1-b y_2)\) with \(a=1\), \(r=X\), \(s=1/200\), \(b=4\), and either \(F(X)=X\) or \(F(X)=100\tanh(X/100)\). In both cases
\[
\mathcal R_F(1)>\frac{5643}{5000}>1,
\]
while \(\mathcal R_F(X)<1\) for all sufficiently small and for all sufficiently large positive \(X\). Thus there are at least two distinct positive values \(X_-<1<X_+\) for which \(\mathcal R_F(X_-)=\mathcal R_F(X_+)=1\). The predator population fails the linear invasion test at low and high prey-resource abundance but passes it at the intermediate abundance \(X=1\). No assertion is made that these are the only crossings, or that invasion entails nonlinear persistence.

## Assumptions and scope

We use the paper's original coupled ODE and age-structured renewal equation [1], with prey abundance \(x(t)\), predator age density \(u(t,z)\), and juvenile and adult masses \(y_1(t)=\int_0^T u(t,z)dz\) and \(y_2(t)=\int_T^\infty u(t,z)dz\):
\[
\dot x=x(r-a x+s y_1-b y_2),\qquad
\partial_t u+\partial_z u=-\mu(x,z)u,\qquad
u(t,0)=\int_0^\infty B_F(x,z)u(t,z)dz,
\]
with \(a,r,s,b>0\),
\[
B_F(x,z)=kF(x)A_\nu(z)+(1-e^{-\zeta x})\tilde B(z),\qquad
\mu(x,z)=gxJ_\nu(z)+m+\mu_Me^{-\rho x}.
\]
All parameters indicated as positive are strictly positive; the additional nonnegative birth profile is not identically zero in the example. The constant \(m>0\) is a permitted special case of the source's continuous positive baseline mortality. The saturated form is the birth saturation proposed in [1, Section 7.1]. That section also saturates the positive juvenile contribution to prey growth. Either choice of juvenile-growth saturation has the same predator-free prey equation and the same predator invasion linearization, so the conclusion applies to the combined saturation variant as well. The result is an invasion-threshold assertion at \((x,u)=(r/a,0)\), not a global ecological attractor classification.

For every fixed \(X>0\), \(B_F(X,\cdot)\) is bounded, while \(\mu(X,z)\ge m\). This ensures the reproduction integral and its exponentially weighted counterparts are finite near zero growth. The functions \(A_\nu,J_\nu\) are strictly positive at every finite age, including at birth. This neonatal leakage of the smoothed maturation function is essential to the nonzero large-resource limit for unsaturated birth.

## Proof

**1. Reduction to the invasion integral.** At \(u=0\), the prey equation is logistic and the positive equilibrium is \(X=r/a\), with prey-only linear eigenvalue \(-r<0\). Linearizing the predator equation at \((X,0)\), changes in the prey coordinate enter only as products with the zero predator density. Hence the predator block is the constant-environment renewal equation with birth \(B_F(X,z)\) and mortality \(\mu(X,z)\). Along characteristics, the survival probability to age \(z\) is
\[
S_X(z)=\exp\!\left[-\eta_Xz-gXH_\nu(z)\right],\quad
\eta_X=m+\mu_Me^{-\rho X},\quad H_\nu(z)=\int_0^z J_\nu(s)ds.
\]
A separable growing mode \(u(t,z)=e^{\lambda t}v(z)\) has \(v(z)=v(0)e^{-\lambda z}S_X(z)\). Its boundary condition becomes
\[
1=\int_0^\infty B_F(X,z)S_X(z)e^{-\lambda z}\,dz.
\]
At \(\lambda=0\) this right-hand side is \(\mathcal R_F(X)\). It decreases strictly from a value above one to zero as \(\lambda\) grows from zero to infinity when \(\mathcal R_F(X)>1\), giving a positive invasion eigenvalue. When \(\mathcal R_F(X)<1\), the positive convolution kernel has total mass below one; by \(\eta_X\ge m\), it also has an exponential moment. A sufficiently small positive exponential weighting preserves the mass-below-one condition, so the renewal series and the deaths of initial cohorts decay exponentially. Thus the strict tests correspond, respectively, to linear predator invasion and non-invasion. No claim is made at equality beyond a zero characteristic root.

**2. Low-resource limit and continuity.** The birth kernel obeys
\[
0\le B_F(X,z)\le kF(X)+(1-e^{-\zeta X})\tilde B(z),\qquad S_X(z)\le e^{-mz}.
\]
Therefore
\[
0\le \mathcal R_F(X)\le \frac{kF(X)}m+(1-e^{-\zeta X})\|\tilde B\|_{L^1},
\]
which goes to zero as \(X\downarrow0\). On each compact positive \(X\)-interval, dominated convergence with a multiple of \(e^{-mz}\) proves continuity.

**3. High-resource boundary layer.** Fix any \(\delta\in(0,T)\) and set \(c_\delta=\min_{0\le z\le\delta}J_\nu(z)>0\). On \([0,\delta]\), substitute \(w=Xz\):
\[
\begin{aligned}
&kF(X)\int_0^\delta A_\nu(z)e^{-\eta_Xz-gXH_\nu(z)}dz\\
&\quad=k\frac{F(X)}X\int_0^{X\delta}
A_\nu(w/X)e^{-\eta_Xw/X-gXH_\nu(w/X)}dw.
\end{aligned}
\]
For fixed \(w\), \(XH_\nu(w/X)\to J_\nu(0)w\) and \(\eta_X w/X\to0\). The integrand is bounded by \(e^{-gc_\delta w}\), while \(F(X)/X\) is bounded for all large \(X\). Dominated convergence gives
\[
\lim_{X\to\infty}kF(X)\int_0^\delta A_\nu(z)S_X(z)dz
=\frac{kLA_\nu(0)}{gJ_\nu(0)}.
\]
The complementary birth integral over \([\delta,\infty)\) is at most
\[
\frac{kF(X)}m e^{-gXH_\nu(\delta)},
\]
which vanishes since \(F(X)=O(X)\) for large \(X\) and \(H_\nu(\delta)>0\). The basal-birth contribution, supported at ages at least \(T\), is bounded above by \(\|\tilde B\|_{L^1}e^{-gXH_\nu(T)}\) and also vanishes. Finally,
\[
\frac{A_\nu(0)}{J_\nu(0)}=e^{-\nu T},
\]
proving the announced limit. In particular \(L=1\) for \(F(X)=X\) and \(L=0\) for \(F(X)=h\tanh(X/h)\).

**4. Explicit reentrance.** For the displayed example at \(X=1\), both choices of \(F\) obey \(F(1)>99/100\): this is immediate for the linear case, while for the saturated case \(\tanh t\ge t-t^3/3\) for \(t\ge0\) (the difference has derivative \(t^2-\tanh^2t\ge0\)), applied at \(t=1/100\), yields \(100\tanh(1/100)\ge1-1/30000>99/100\). For ages \(1\le z\le2\), \(A_\nu(z)\ge1/2\). On the whole age interval \([0,2]\), \(\mu(1,z)\le 1/100+1/10+1/100=3/25\), hence \(S_1(z)\ge e^{-6/25}>19/25\), using \(e^{-t}>1-t\) for \(t>0\). The nonnegative basal-birth term can be omitted for a lower bound, and therefore
\[
\mathcal R_F(1)>\int_1^2\frac{3}{2}\frac{99}{100}\frac{19}{25}\,dz
=\frac{5643}{5000}>1.
\]
The low-resource limit in Step 2 is below one for sufficiently small positive \(X\). The high-resource limit in Step 3 is zero for saturated birth, and \(300e^{-10}<1\) for linear birth, since \(e^{10}>1+10+10^2/2!+10^3/3!+10^4/4!>300\). Continuity yields at least one root \(X_-\in(0,1)\) and another \(X_+\in(1,\infty)\). This proves both a low-to-high and a high-to-low switch in the strict linear invasion criterion; it does not assume either crossing is transversal.

**5. Comparison with sharp maturation.** If one instead sets the two maturation functions equal to exact step indicators before taking \(X\to\infty\), births of the \(kF(X)\) type begin only at \(z\ge T\), after incurring the factor \(e^{-gXT}\). When \(F(X)=O(X)\), the corresponding reproduction integral consequently tends to zero. Thus the positive high-resource limit for linear feeding is specifically a finite-smoothness effect. The two iterated limits as \(\nu\to\infty\) both vanish; no noncommutation claim is needed.

## Verification

The standalone standard-library program `verify.py` implements the stated kernel and the closed-form juvenile hazard integral
\[
H_\nu(z)=\frac{\log(1+e^{\nu T})-\log(1+e^{\nu(T-z)})}{\nu}.
\]
It checks the exact rational lower bound \(5643/5000>1\), the rational Taylor lower bound \(e^{10}>300\), and the hyperbolic-tangent estimate, then independently quadratures \(\mathcal R_F(0.001)\) and \(\mathcal R_F(1)\) for both feeding laws. Running `python3 verify.py` returned `VERIFY_OK exact bounds and independent finite-quadrature checks`. Finite numerical integration is not used to establish the infinite-range limits, the existence of threshold roots, or the spectral conclusion: those rest on the analytical proof above.

## Relationship to prior work

Suarez, Cameron, Fagan, and Levy [1] introduce the exact age-structured coefficients, prove well-posedness, and numerically explore long-run dynamics. They also propose saturation of the \(kx\) birth term in Section 7.1. The present result is not a claim to have introduced the renewal reproduction number or the renewal eigenvalue criterion, both standard. It identifies the sharp abundance-asymptotic law produced by their particular smooth juvenile/adult coefficients and establishes an explicit two-transition counterexample for both the original and saturated birth forms. The source's phase diagrams vary maturation age and juvenile consumption, not the full high-abundance invasion curve with its neonatal boundary layer. Standard age-structured renewal theory [2] provides the analytical framework but does not by itself supply the model-specific limit, the distinction between the two source birth laws, or the concrete parameter inequalities. Stage-based role-reversal models [3] have different maturation mechanisms and cannot directly cover a finite-sigmoid neonatal boundary layer.

## Limitations

The assertion concerns a deterministic infinite-age renewal model at the predator-free equilibrium. It does not prove a globally attracting predator-free state, nonlinear coexistence, a unique interval of invadability, transversality at the two threshold crossings, or a biologically realistic numerical abundance scale. The positive high-resource limit for linear feeding results from the sigmoid assigning a strictly positive adult fecundity weight at birth; it should not be interpreted as actual reproduction by newborn predators. Constant baseline mortality is an admissible special case, not a theorem covering every unbounded age-mortality profile. For saturated birth the high-resource limit is zero, but this alone does not rule out intermediate nonlinear attractors. No independent audit has been performed.

## References

[1] L. C. Suarez, M. K. Cameron, W. F. Fagan, and D. Levy, *A predator-prey model with age-structured role reversal*, arXiv:2502.19748v1 (first public 2025-02-27), https://arxiv.org/html/2502.19748v1 ; *Journal of Mathematical Biology* 92, 73 (2026), https://doi.org/10.1007/s00285-026-02402-5 .

[2] B. Perthame, *Transport Equations in Biology*, Birkhäuser (2007), especially age-structured renewal equations. This source supplies classical renewal background, not the asymptotic computation here.

[3] J. Li, X. Liu, and C. Wei, *The impact of role reversal on the dynamics of predator-prey model with stage structure*, *Applied Mathematical Modelling* 104, 339–357 (2022), https://doi.org/10.1016/j.apm.2021.11.029 . Only bibliographic/abstract material was available for direct comparison; no whole-document noncoverage assertion is made.
