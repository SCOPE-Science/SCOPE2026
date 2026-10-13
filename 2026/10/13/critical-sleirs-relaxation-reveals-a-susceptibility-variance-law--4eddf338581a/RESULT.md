# Critical SLEIRS relaxation reveals a susceptibility-variance law at fixed reproduction number

## Finding

The Pan–Tang SLEIRS model separates ordinary susceptible individuals \(S\) from lower-risk, self-protecting individuals \(L\), and adds exposed \(E\), symptomatic infected \(I\), and recovered \(R\). On the invariant simplex
\[
\Omega=\{(S,L,E,I,R)\ge0:S+L+E+I+R=1\},
\]
the dynamics are
\[
\begin{aligned}
\dot S&=\mu\rho+\sigma\rho R-\alpha S(E+I)-\mu S,\\
\dot L&=\mu(1-\rho)+\sigma(1-\rho)R-\beta L(E+I)-\mu L,\\
\dot E&=(\alpha S+\beta L)(E+I)-(\delta+\mu)E,\\
\dot I&=\delta E-(\gamma+\mu)I,\\
\dot R&=\gamma I-(\sigma+\mu)R.
\end{aligned}
\]
The source's reproduction number is
\[
\mathcal R_0=\frac{A}{\delta+\mu}
\left(1+\frac{\delta}{\gamma+\mu}\right),
\qquad A=\rho\alpha+(1-\rho)\beta.
\]
Its disease-free theorem assumes the strict inequality \(\mathcal R_0<1\). At the omitted boundary \(\mathcal R_0=1\), the disease-free equilibrium remains globally asymptotically stable; more importantly, the whole state relaxes with an exact \(t^{-1}\) profile.

Put
\[
\begin{gathered}
a=\delta+\mu,\quad b=\gamma+\mu,\quad r=\sigma+\mu,\\
h=\delta/b,\quad k=1+h,\\
B=\rho\alpha^2+(1-\rho)\beta^2,\quad
G=\frac{\sigma\gamma h}{r},\quad H=1+\frac{Ah}{b},\\
K=\frac{k(kB-GA)}{\mu H}.
\end{gathered}
\]
Then \(K>0\). For every initial state in \(\Omega\) with \(E(0)+I(0)>0\),
\[
\begin{aligned}
tE(t)&\to\frac1K,&
tI(t)&\to\frac{h}{K},&
tR(t)&\to\frac{\gamma h}{rK},\\
t(\rho-S(t))&\to\frac{\rho(k\alpha-G)}{\mu K},&&
t((1-\rho)-L(t))&\to\frac{(1-\rho)(k\beta-G)}{\mu K}.
\end{aligned}
\]
The two susceptible limits are signed. In particular, \(L\) can approach its disease-free fraction from above when \(k\beta<G\).

The exposed, symptomatic, and new-exposure integrals satisfy
\[
\begin{aligned}
\int_0^tE(s)\,ds&\sim\frac{\log t}{K},\\
\int_0^tI(s)\,ds&\sim\frac{h\log t}{K},\\
\int_0^t(\alpha S(s)+\beta L(s))(E(s)+I(s))\,ds&\sim\frac{a\log t}{K}.
\end{aligned}
\]

The exact coefficient detects heterogeneity that the threshold cannot. With the same mean exposure \(A\), \(\rho\), and all other rates, write
\[
\alpha=A+(1-\rho)\Delta,\qquad
\beta=A-\rho\Delta,
\qquad0<\Delta<\frac{A}{\rho}.
\]
The positivity range ensures \(\alpha>\beta>0\). Because
\[
B=A^2+\rho(1-\rho)\Delta^2,
\]
we have the **exact variance law**
\[
\boxed{
K(\Delta)=\frac{k(kA^2-GA)}{\mu H}
+\frac{k^2\rho(1-\rho)}{\mu H}\Delta^2.
}
\]
Thus the leading decay coefficient strictly increases with contact-risk contrast at fixed \(\mathcal R_0=1\), and the leading cumulative-incidence coefficient \(a/K\) strictly decreases.

## Assumptions and scope

All rates \(\mu,\sigma,\delta,\gamma,\alpha,\beta\) are positive; \(0<\rho<1\) and \(\alpha>\beta\), as in the motivating model. The initial condition is arbitrary in the closed nonnegative simplex \(\Omega\). There are no spatial, delayed, stochastic, or externally imported infection terms.

Criticality means \(Ak=a\), precisely the source's \(\mathcal R_0=1\). The critical asymptotic profile requires \(E(0)+I(0)>0\). If no infected compartment is initially occupied, the infected subsystem remains identically zero and this algebraic tail does not arise. The recovered-only state still converges exponentially to the disease-free equilibrium.

The theorem refers to asymptotic trajectories of the deterministic model, not a stochastic interpretation of an epidemic finite population or a universal law for all SLEIRS equations.

## Proof

**1. Critical global stability.** For positive \(S,L\), define
\[
V=S-\rho+\rho\log\frac{\rho}{S}
+L-(1-\rho)+(1-\rho)\log\frac{1-\rho}{L}
+E+\frac{A}{b}I.
\]
Every term is nonnegative. At criticality \(Ak=a\), direct differentiation using the five printed equations yields the **exact** identity
\[
\dot V
=-\frac{\mu(S-\rho)^2}{S}
-\frac{\mu(L-(1-\rho))^2}{L}
+\sigma R\left(1-\frac{\rho^2}{S}-\frac{(1-\rho)^2}{L}\right).
\]
By Cauchy–Schwarz and the simplex constraint,
\[
\frac{\rho^2}{S}+\frac{(1-\rho)^2}{L}
\ge\frac1{S+L}\ge1.
\]
Consequently \(\dot V\le0\), with equality only when \(S=\rho\), \(L=1-\rho\). The simplex then forces \(E=I=R=0\). Because the strictly positive recruitment terms make \(S,L>0\) for every positive time, each solution enters a compact \(V\)-sublevel away from those coordinate boundaries. LaSalle's principle proves global attraction. Positivity of \(V\) and invariance of the compact simplex give Lyapunov stability. Thus the disease-free equilibrium is globally asymptotically stable also at equality.

**2. The infected direction.** Let
\[
y=(E,I)^\mathsf T,\quad c(t)=\alpha S(t)+\beta L(t),
\]
and define the infected weight
\[
W=E+\frac{A}{b}I.
\]
At \(Ak=a\), the exact balance is
\[
\dot W=(c(t)-A)(E+I).
\]
Global convergence shows \(c(t)\to A\). For a trajectory with initially nonzero infection, \(W(t)>0\) for all finite times, and
\[
\frac{\dot W}{W}\to0.
\]
The infected linearization at the disease-free state is the irreducible Metzler matrix
\[
M=\begin{pmatrix}A-a&A\\\delta&-b\end{pmatrix}.
\]
Its zero eigenvalue is simple, with positive right eigenvector \(v=(1,h)^\mathsf T\) and positive left eigenvector \(w=(1,A/b)^\mathsf T\). Their pairing is
\[
w^\mathsf Tv=H=1+\frac{Ah}{b}.
\]
The other eigenvalue equals \(-Ah-b<0\). The nonlinear forcing in the infected equation is
\[
(c(t)-A)(E+I)(1,0)^\mathsf T=o(W).
\]
Projecting onto the stable complement of \(v\) yields a scalar stable equation driven by \(o(W)\). This forcing is negligible relative to \(W\): given any sufficiently small \(\varepsilon>0\), eventually \(|(\log W)'|<\varepsilon\), so
\[
W(s)\le e^{\varepsilon(t-s)}W(t)
\quad\text{for }s\le t
\]
within that tail; convolution against the exponentially decaying stable semigroup proves
\[
\frac{y(t)}{W(t)}\to\frac vH.
\]
In particular
\[
\frac{I(t)}{E(t)}\to h,
\qquad\frac{E'(t)}{E(t)}\to Ak-a=0.
\]
This is a genuine limit argument for arbitrary positive-infection initial data, not just a local numerical center-manifold expansion.

**3. Stable-filter ratios.** The linear recovered equation gives
\[
\frac{R(t)}{E(t)}\to\frac{\gamma h}{r}.
\]
Indeed the input is asymptotic to \(\gamma hE\), and \(E'/E\to0\), so a stable scalar convolution divides asymptotically by its decay rate \(r\).

Set \(s=\rho-S\) and \(\ell=(1-\rho)-L\). Then
\[
\begin{aligned}
\dot s&=-\mu s+\alpha S(E+I)-\sigma\rho R,\\
\dot\ell&=-\mu\ell+\beta L(E+I)-\sigma(1-\rho)R.
\end{aligned}
\]
The same scalar stable-filter argument yields
\[
\frac{s(t)}{E(t)}\to e_S:=\frac{\rho(k\alpha-G)}\mu,
\qquad
\frac{\ell(t)}{E(t)}\to e_L:=\frac{(1-\rho)(k\beta-G)}\mu,
\]
where \(G=\sigma\gamma h/r\). The right-hand side for \(e_L\) need not be positive.

**4. Exact scale.** With \(c-A=-\alpha s-\beta\ell\),
\[
\frac{\dot W}{E^2}
=-(E+I)\frac{\alpha s+\beta\ell}{E^2}
\to-k(\alpha e_S+\beta e_L)
=-\frac{k(kB-GA)}\mu.
\]
Since \(W/E\to H\),
\[
\left(\frac1W\right)'=-\frac{\dot W}{W^2}
\to \frac{k(kB-GA)}{\mu H^2}=
\frac KH.
\]
The constant is strictly positive. Indeed \(B\ge A^2\), \(G<\delta\), and \(kA=a=\delta+\mu\), so
\[
kB-GA\ge A(kA-G)>A\mu>0.
\]
Integrating the derivative limit gives \(tW(t)\to H/K\), hence
\[
tE(t)\to\frac1K.
\]
Multiplying by the established ratios proves each of the five component limits.

Finally, \(E(t)\sim1/(Kt)\) and \(I(t)\sim h/(Kt)\). Since \(c(t)(E+I)\sim Ak/(Kt)=a/(Kt)\), the three cumulative logarithmic laws follow from integration. The weighted second-moment identity
\[
B-A^2=\rho(1-\rho)(\alpha-\beta)^2
\]
then proves the exact heterogeneity comparison for fixed \(A\) and other rates.

## Verification

A standalone checker computes exact rational quantities for the critical parameter set
\[
\rho=\frac12,\quad \mu=\sigma=\delta=\gamma=1,
\quad \alpha=\frac53,\quad\beta=1.
\]
It verifies
\[
A=\frac43,\quad B=\frac{17}9,\quad
G=\frac14,\quad H=\frac43,\quad K=\frac{45}{16},
\]
with the predicted limits
\[
\begin{aligned}
tE&\to\frac{16}{45},& tI&\to\frac8{45},& tR&\to\frac4{45},\\
t(\rho-S)&\to\frac25,&
t((1-\rho)-L)&\to\frac29.
\end{aligned}
\]
It also checks the exact variance identity. Numerical integration from the interior simplex corroborates all five asymptotic constants at late time with less than one percent relative error. Exact rational tests and the ODE replay are supporting checks; neither substitutes for the proof of the infinite-time limits.

## Relationship to prior work

Pan and Tang (2024), equations (2.2) and (3.4), define this five-compartment model and its \(\mathcal R_0\). Their Theorem 1 treats disease-free global stability for the strict region \(\mathcal R_0<1\), and their numerical study does not present the complete critical-rate asymptotic vector.

The literature on differential susceptibility is considerably older. Hyman and Li (2009) analyze heterogeneous susceptibility with staged disease progression and establish reproduction-number and strict-threshold results for distinct model classes. Bonzi, Fall, Iggidr, and Sallet (2011) obtain disease-free global stability at the closed threshold in broader differential susceptibility/infectivity settings. More recently, Bichara (2023) proves global threshold dynamics for a general multi-group framework, including equality. These general stability results are **not** claimed as novel here. Bichara's printed general model uses constant susceptible recruitment and an infection-to-recovered flow; it does not have this paper's immunity-loss feedback from recovered individuals into two susceptible classes. In the inspected relevant material, no source states the present full asymptotic profile or its exact variance-sensitive coefficient.

General critical-slowing behavior in other epidemic equations does not imply this five-compartment protection-contrast coefficient; the distinct susceptible feedback pathways must be analyzed explicitly.

## Limitations

This is a deterministic, well-mixed, exactly critical result. It does not claim a higher-order logarithmic correction, data-fitted forecast, or a stochastic analogue. The heterogeneous comparison holds at fixed weighted mean transmission and all other rates; it is not a claim that increasing one transmission rate while leaving the other unchanged improves outcomes. When \(E(0)+I(0)=0\), there is no algebraic infected tail. A general source might imply the leading formula after a nontrivial model-specific reduction, and some relevant older texts are accessible only in part; those originality residuals remain.

## References

1. X. Pan and L. Tang, “A new model for COVID-19 in the post-pandemic era,” *AIMS Mathematics* **9** (2024), 21255–21272. DOI: 10.3934/math.20241032.
2. J. M. Hyman and J. Li, “Epidemic models with differential susceptibility and staged progression and their dynamics,” *Mathematical Biosciences and Engineering* **6** (2009), 321–332. DOI: 10.3934/mbe.2009.6.321.
3. B. Bonzi, A. A. Fall, A. Iggidr, and G. Sallet, “Stability of differential susceptibility and infectivity epidemic models,” *Journal of Mathematical Biology* **62** (2011), 39–64. DOI: 10.1007/s00285-010-0327-y.
4. D. M. Bichara, “Characterization of differential susceptibility and differential infectivity epidemic models,” *Journal of Mathematical Biology* **88** (2024), article 3; first published online 2023. DOI: 10.1007/s00285-023-02023-2.
