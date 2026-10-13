# Explicit supercritical-mass extinction in a heterogeneous SIS lockdown model

## Finding

In the immobile-susceptible, mobile-infected, mass-action SIS model of Salako and Wu, infection **can decay to zero despite a total population strictly above the spatially integrated recovery-to-transmission ratio**, and it can do so in the exact population window that Remark 3.6 of [1] leaves open.

**Theorem (an explicit open-window extinction example).** On \(\Omega=(0,1)\), impose Neumann boundary conditions on the infected component and let
\[
\partial_t S=-\beta(x)I(S-r),\qquad
\partial_t I=10\partial_{xx}I+\beta(x)I(S-r),
\qquad\partial_x I(0,t)=\partial_x I(1,t)=0,
\]
with
\[
 c(x)=\cos(\pi x),\qquad \beta(x)=1-\frac34c(x),\qquad
 \gamma(x)=2\beta(x),\qquad r(x)=\frac{\gamma(x)}{\beta(x)}=2,
\]
and initial susceptible density
\[
 S_0(x)=\frac94+c(x).
\]
Let \(\psi\) be the positive principal Neumann eigenfunction of
\[
 10\psi''+\beta(x)\left(S_0(x)-r(x)+\frac1{100}\right)\psi
       =\lambda\psi,\qquad \psi'(0)=\psi'(1)=0,
\]
uniquely normalized by \(\|\psi\|_\infty=1\), and set \(I_0=\psi/10000\). Then \(S_0>0\), \(I_0>0\), and the unique global solution satisfies
\[
 0<I(x,t)\leq 10^{-4}e^{-t/25}\quad(x\in[0,1],\ t\geq0).
\]
In particular, infection becomes extinct uniformly, although its conserved total population \(N\) satisfies
\[
 \boxed{\quad
 \max\!\left\{\int_0^1 S_0\,dx,\ \int_0^1r\,dx\right\}
 =\frac94<N<\frac94+\frac1{800}\leq N^*_{S_0,r}.
 \quad}
\]
Here \(N^*_{S_0,r}\) is *precisely* the threshold in [1, equation (3.4)], not a newly defined surrogate. Consequently alternative (i), disease extinction, in [1, Theorem 3.3] **does occur** in the open interval posed in its Remark 3.6. The example makes no assertion that all initial conditions with the same \(N\) become extinct.

## Assumptions and scope

The domain is the unit interval with classical Neumann boundary condition for \(I\). Susceptibles have zero dispersal; infecteds disperse at rate \(d_I=10\). Transmission and recovery rates are positive, smooth, and nonconstant, with \(\beta\in[1/4,7/4]\), \(\gamma=2\beta\). Both initial components are smooth and strictly positive. The relative-risk profile \(S_0-r=1/4+\cos(\pi x)\) changes sign. The family of admissible tests in the source definition is
\[
 N^*_{S_0,r}:=\sup_{\substack{\ell\in C([0,1];[0,1])\\
 \sigma(10,\beta\ell(S_0-r))\leq0}}
 \int_0^1\bigl(\ell S_0+(1-\ell)r\bigr)\,dx,
\]
where \(\sigma(d,h)\) denotes the largest Neumann eigenvalue of \(d\partial_{xx}+h\), given by its Rayleigh quotient. All strict inequalities below hold with explicit rational margins; no finite spatial discretization is used as a proof.

## Proof

**1. A strictly negative Neumann principal eigenvalue.** Put
\[
 f=S_0-r=\frac14+c,\qquad
 V=\beta f=\frac14+\frac{13}{16}c-\frac34c^2.
\]
Because \(\int_0^1c=0\), \(\int_0^1c^2=1/2\), and \(\|V\|_\infty\leq2\),
\[
 \int_0^1 V=-\frac18.
\]
For any real \(u\in H^1(0,1)\) let \(m=\int_0^1u\) and \(v=u-m\), with \(w=\|v\|_2\). The mean-zero Neumann Poincare inequality \(\int_0^1|v'|^2\geq\pi^2w^2>9w^2\), Cauchy--Schwarz, and \(\|V\|_\infty\leq2\) give
\[
 \begin{aligned}
 \int_0^1\bigl(Vu^2-10|u'|^2\bigr)
 &\leq-\frac18m^2+4|m|w+2w^2-90w^2\\
 &\leq-\frac1{16}m^2-24w^2
 \leq-\frac1{16}\|u\|_2^2,
 \end{aligned}
\]
where the middle inequality follows from \(4|m|w\leq m^2/16+64w^2\). This is an infinite-dimensional bound for **all** \(H^1\) test functions, not a truncation. The Rayleigh variational principle therefore yields
\[
 \sigma(10,V)\leq-\frac1{16}.
\]

**2. Construct an admissible witness strictly above \(\int S_0\).** Set
\[
 \ell(x)=1-\frac{1-c(x)}{200}=\frac{199+c(x)}{200}\in[0.99,1].
\]
Since \(\|\beta\ell f-V\|_\infty\leq1/50\), the same Rayleigh bound implies
\[
 \sigma(10,\beta\ell f)\leq-\frac1{16}+\frac1{50}
   =-\frac{17}{400}<0.
\]
Using \(\int_0^1(1-c)f\,dx=-1/4\), we obtain
\[
 \int_0^1\bigl(\ell S_0+(1-\ell)r\bigr)\,dx
 =2+\int_0^1\ell f\,dx=\frac94+\frac1{800}.
\]
Thus this **explicit admissible** \(\ell\) proves \(N^*_{S_0,r}\geq9/4+1/800\), without evaluating the supremum.

**3. A positive initial infection decays exponentially.** Let \(\delta=1/100\). The Neumann principal eigenvalue is 1-Lipschitz in the \(L^\infty\) potential by the Rayleigh formula. Therefore
\[
 \lambda=\sigma(10,V+\delta\beta)
 \leq-\frac1{16}+\frac7{400}
 =-\frac9{200}< -\frac1{25}.
\]
Standard principal-eigenvalue theory for continuous potentials yields the stated strictly positive \(C^2\) eigenfunction \(\psi\) with the prescribed normalization; see [1, Lemma 2.4]. The model has a unique global nonnegative solution by [1, Proposition 3.1], and parabolic strict positivity applies because \(I_0>0\).

For \(J(x,t)=\int_0^tI(x,s)\,ds\), solve the first equation *exactly* at each \(x\):
\[
 S(x,t)-r(x)=f(x)e^{-\beta(x)J(x,t)}.
\]
In particular
\[
 |S(x,t)-S_0(x)|
 \leq\|f\|_\infty\|\beta\|_\infty J(x,t)
 =\frac{35}{16}J(x,t).
\]
As long as \(S(\cdot,t)\leq S_0+\delta\), the infected equation has potential at most \(V+\delta\beta\). The scalar parabolic comparison principle, the Neumann boundary condition, and \(\lambda<-1/25\) then give
\[
 I(x,t)\leq\varepsilon e^{-t/25}\psi(x)
 \leq\varepsilon e^{-t/25},\qquad \varepsilon=10^{-4}.
\]
Consequently \(J(x,t)\leq25\varepsilon\), so
\[
 \|S(\cdot,t)-S_0\|_\infty
 \leq\frac{35}{16}\cdot25\varepsilon
 =\frac7{1280}<\frac1{100}=\delta.
\]
The strict margin closes the bootstrap by continuity: at a first exit from \(S\leq S_0+\delta\), the last estimate would still hold, a contradiction. Thus the comparison holds for every \(t\geq0\). This proves uniform exponential infection extinction. The susceptible identity and integrability of \(I\) also give a uniform disease-free limit \(S_\infty=2+f e^{-\beta J_\infty}\).

**4. The mass belongs to the previously unresolved open interval.** Spatial integration of the sum of the equations conserves total population. Initially,
\[
 N=\int_0^1(S_0+I_0)\,dx
 =\frac94+\frac1{10000}\int_0^1\psi(x)\,dx.
\]
The normalization \(0<\psi\leq1\) implies
\[
 \frac94<N\leq\frac94+\frac1{10000}
 <\frac94+\frac1{800}\leq N^*_{S_0,r}.
\]
Also \(\int_0^1r=2\) and \(\int_0^1S_0=9/4\). Uniform infection extinction yields \(\int_0^1 S_\infty=N\), and its profile meets alternative (i) of [1, Theorem 3.3]. Every inequality and normalization used in the theorem has been established.

## Verification

Run \(\texttt{python verify\_cosine\_sis.py}\) using Python's standard library. It checks, in exact rational arithmetic, the cosine-polynomial coefficients, moments, Rayleigh upper bounds, admissible test \(\ell\), bootstrap margin, and the strictly nested mass interval. Expected output begins with `VERIFY_OK`. The code verifies the arithmetic of the certificate, **not** spectral existence or the full PDE comparison; these follow from the analytic arguments and standard stated results above. No numerical PDE trajectories are needed.

## Relationship to prior work

Salako and Wu [1, Remark 3.6] expressly ask whether extinction can occur for \(\max\{\int S_0,\int r\}<N<N^*_{S_0,r}\), although their Theorem 3.3 covers both possible asymptotic alternatives. This theorem gives an explicit positive, nonconstant-rate, mixed-sign instance that realizes the extinction alternative; Corollary 3.5 of [1] assumes conditions inapplicable here. It does not contradict Theorem 3.3.

Castellano and Salako [2] study multiple *endemic equilibria* and small but **positive** susceptible diffusion in a mass-action SIS model; their results and parameter examples do not imply this exact time-dependent initial-value construction at zero susceptible diffusion. Their earlier work [3] investigates asymptotic endemic-equilibrium profiles as both diffusion coefficients become small; it is related but distinct. Deng [4] imposes Dirichlet boundary conditions, so its population accounting and invasion mechanism differ. These comparisons limit, but do not eliminate, the possibility of an independently known equivalent example.

## Limitations

This is an existence counterexample, not a classification of **all** initial conditions, nor a result for heterogeneous \(\gamma/\beta\), nonzero susceptible dispersal, or multi-dimensional domains. It uses a principal eigenfunction specified by a well-posed boundary-value problem rather than an elementary closed-form expression. It proves \(N^*_{S_0,r}\) exceeds an explicit lower bound, not its exact value. The spectral estimate is deliberately conservative. Publication originality cannot be guaranteed by database searches; full text of [3] could not be obtained, so an unindexed equivalent remains a residual originality risk. Independent audit has not been conducted.

## References

1. R. B. Salako and Y. Wu, *On degenerate reaction-diffusion epidemic models with mass action or standard incidence mechanism*, European Journal of Applied Mathematics 35 (2024), 634--661. DOI `10.1017/S0956792523000359`; first public preprint `arxiv:2311.06434v1` (2023-11-10). In particular Lemma 2.4, Proposition 3.1, Theorem 3.3, equation (3.4), Corollary 3.5, Remark 3.6.
2. K. Castellano and R. B. Salako, *Multiplicity of endemic equilibria for a diffusive SIS epidemic model with mass-action*, SIAM Journal on Applied Mathematics 84 (2024), 732--755. DOI `10.1137/23M1613888`; preprint `arxiv:2307.15155`.
3. K. Castellano and R. B. Salako, *On the effect of lowering population's movement to control the spread of an infectious disease*, Journal of Differential Equations 316 (2022), 1--27. DOI `10.1016/j.jde.2022.01.031`.
4. K. Deng, *Asymptotic behavior of a diffusive SIS epidemic model with mass action infection mechanism*, Discrete and Continuous Dynamical Systems--B 29 (2024). DOI `10.3934/dcdsb.2024019`.
