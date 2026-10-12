# Finite-mean survival is the sharp endemic-equilibrium condition in an age-structured HIV model

## Finding

For the within-host HIV model of Vivas-Cruz, Martínez-Lázaro and Vargas-De-León [1], the published reproduction-number test must be accompanied by a **finite-mean infection-age residence condition** in order to yield a positive equilibrium in its stated \(L^1\) phase space. This gives a sharp classification, including two distinct ways in which a formally positive age profile escapes the phase space.

Let \(S(a)=\exp(-\int_0^a s(u)\,du)\), \(\sigma=\int_0^\infty s(a)S(a)\,da=1-S(\infty)\), and \(m=\int_0^\infty S(a)\,da\). Suppose \(\sigma>0\). Write
\[
 d=\delta+\frac{r\mu}{\eta+\mu},\qquad
 \mathcal R_0=\frac{\psi\lambda p\sigma}{\gamma c d}.
\]
Then the nonnegative stationary problem in \(\mathbb R_+\times L^1_+(0,\infty)\times\mathbb R_+^3\) has a strictly infected equilibrium **if and only if** \(\mathcal R_0>1\) **and** \(m<\infty\). Such an equilibrium is unique. The infection-free equilibrium always exists and is the only nonnegative equilibrium if either condition fails. Thus \(\mathcal R_0\) alone is not a sufficient endemic-existence test in this phase space.

The article [1, Section 1] permits positive bounded **integrable** \(s\). Under precisely this assumption \(S(\infty)>0\), hence \(m=\infty\). Consequently, its printed positive-equilibrium criterion (Theorem 2.1) does not yield an equilibrium in its specified \(L^1\) state space, even when \(\mathcal R_0>1\). This is a statement about the equations and their functional setting, **not** about the paper's individual finite-grid simulations or a proved global trajectory limit.

A sharp separation persists even when every new infection eventually transactivates. In the family \(s(a)=k/(1+a)\) with \(k>0\), one has \(\sigma=1\) for every \(k\), while \(m<\infty\) exactly for \(k>1\). Thus the reproduction number is *independent* of \(k\), but positive finite-mass endemic equilibria exist only above the exact tail exponent \(k=1\). At fixed \(\mathcal R_0>1\), the total stationary infection-age mass diverges like \(1/(k-1)\) as \(k\downarrow1\).

There is also an exact transient mass identity. For any nonnegative mild solution with initial density \(i_0\in L^1\) and new-infection influx \(J(t)=\lambda T(t)V(t)\), define \(M(t)=\int_0^\infty i(a,t)\,da\) and \(K(t)=\int_0^t S(a)\,da\). For all \(t\ge0\),
\[
 M(t)=\int_0^t J(t-a)S(a)\,da+R(t),\qquad
 0\le R(t)\le\|i_0\|_1.
\]
If \(m=\infty\) and \(J(t)\to j>0\), then \(M(t)/K(t)\to j\). For integrable \(s\), the **unconditional** lower bound \(M(t)\ge S(\infty)\int_0^t J(u)\,du\) holds. Hence uniformly bounded infection-age mass forces finite total infection influx in the model's stated integrable-hazard regime. The assertion about \(J(t)\to j\) is conditional; convergence of \(J\) for arbitrary solutions is not established here.

## Assumptions and scope

Consider time \(t\ge0\), infection age \(a\ge0\), strictly positive parameters \(\psi,\gamma,\lambda,r,\delta,\eta,\mu,p,c\), and a nonnegative locally integrable hazard \(s\) with \(0<\sigma\le1\). For the transient mass formula assume a nonnegative mild solution whose influx \(J\) is locally bounded, with initial infection-age density \(i_0\in L^1_+(0,\infty)\). The model is
\[
\begin{aligned}
 \dot T&=\psi-\gamma T-\lambda TV,\\
 \partial_t i+\partial_a i&=-s(a)i,\quad i(0,t)=\lambda T(t)V(t),\\
 \dot A&=\int_0^\infty s(a)i(a,t)\,da-(r+\delta)A+\eta L,\\
 \dot L&=rA-(\eta+\mu)L,\\
 \dot V&=pA-cV.
\end{aligned}
\]
The stationary density must belong to \(L^1_+(0,\infty)\), not merely be finite at every finite age. The original paper's bounded, positive, integrable hazards are a subcase. The broader locally integrable class is used to locate the exact condition and its heavy-tail boundary.

## Proof

**1. Stationary transport and the necessary moment.** At an equilibrium write \(J=\lambda TV\). The age equation and boundary condition give the unique locally integrable profile \(i(a)=JS(a)\) almost everywhere. Since \(S'(a)=-s(a)S(a)\) almost everywhere and \(S(0)=1\), monotone integration yields
\[
 \int_0^\infty s(a)S(a)\,da=1-S(\infty)=\sigma.
\]
For \(J>0\), the profile belongs to \(L^1\) exactly when \(m<\infty\); its norm is \(Jm\). This argument uses the entire infinite age interval, not a finite discretization.

**2. Reduction of the algebraic balances.** From the last two stationary equations \(L=rA/(\eta+\mu)\) and \(A=cV/p\). The \(A\)-equation therefore becomes \(J\sigma=dA=dcV/p\). If \(V=0\), the preceding identities and transport boundary give \(A=L=J=i=0\), and the \(T\)-equation gives the unique infection-free state \(T=\psi/\gamma\). If \(V>0\), then \(T>0\), \(J>0\), and cancellation in \(\lambda TV\sigma=dcV/p\) yields
\[
 T=\frac{dc}{\lambda p\sigma}=\frac{\psi}{\gamma\mathcal R_0}.
\]
The \(T\)-balance forces \(V=\gamma(\mathcal R_0-1)/\lambda\), so positivity is equivalent to \(\mathcal R_0>1\). The remaining coordinates are uniquely determined:
\[
\begin{aligned}
 T_*&=\frac{\psi}{\gamma\mathcal R_0},&
 V_*&=\frac{\gamma}{\lambda}(\mathcal R_0-1),\\
 A_*&=\frac{c\gamma}{p\lambda}(\mathcal R_0-1),&
 L_*&=\frac{r}{\eta+\mu}A_*,\\
 J_*&=\psi\left(1-\frac1{\mathcal R_0}\right),&
 i_*(a)&=J_*S(a).
\end{aligned}
\]
Conversely, if \(m<\infty\) and \(\mathcal R_0>1\), the displayed profile is in \(L^1\), each balance is satisfied, and every infected coordinate is strictly positive. This proves existence, necessity, and uniqueness in the specified phase space. Observe that \(m<\infty\) itself forces \(S(\infty)=0\), hence \(\sigma=1\); the displayed formula remains valid.

**3. Two exact failure mechanisms.** When \(s\) is integrable, \(H=\int_0^\infty s(a)\,da<\infty\), so \(S(a)\ge e^{-H}>0\) for every age. Thus \(m=\infty\). For an explicit source-admissible choice take \(s(a)=(\log2)e^{-a}\). It has \(\sigma=1/2\), and with every constant rate equal to one except recruitment \(\psi=6\), the formulas give \(d=3/2\), \(\mathcal R_0=2\), and the formal coordinates \((T_*,A_*,L_*,V_*,J_*)=(3,1,1/2,1,3)\). Yet \(i_*(a)\to3/2\), excluding \(i_*\in L^1\).

For \(s(a)=k/(1+a)\), integration gives \(S(a)=(1+a)^{-k}\) and \(\sigma=1\) for every \(k>0\), but
\[
 m=\int_0^\infty(1+a)^{-k}\,da=\begin{cases}1/(k-1),&k>1,\\ \infty,&0<k\le1.\end{cases}
\]
Take all constant rates equal to one except \(\psi=3\). Then \(\mathcal R_0=2\) for all \(k>0\) and \(J_*=3/2\). For \(k>1\), the actual endemic equilibrium has total age mass \(3/[2(k-1)]\); for \(k\le1\), the same formal profile is not in \(L^1\). The precise threshold and divergence are therefore independent of any numerically estimated reproduction-number crossing.

**4. Transient convolution and conditional escape.** The method of characteristics gives \(i(a,t)=J(t-a)S(a)\) for \(0\le a<t\), and \(i(a,t)=i_0(a-t)S(a)/S(a-t)\) for \(a\ge t\). Integration proves the stated identity, with
\[
 R(t)=\int_0^\infty i_0(b)\frac{S(b+t)}{S(b)}\,db\in[0,\|i_0\|_1].
\]
If \(m=\infty\), then \(K(t)\to\infty\). Suppose \(J(t)\to j>0\). For any \(\varepsilon>0\), choose \(U\) so that \(|J(u)-j|<\varepsilon\) for \(u\ge U\). Splitting the convolution at influx times \(u=U\), its large-\(u\) discrepancy is bounded by \(\varepsilon K(t)\); its fixed-length early-\(u\) discrepancy is bounded by a constant times \(U\), because \(S\le1\). The initial contribution is bounded by \(\|i_0\|_1\). Division by \(K(t)\) and then \(\varepsilon\downarrow0\) yields \(M(t)/K(t)\to j\). If \(H<\infty\), \(S(a)\ge e^{-H}\) in the convolution, giving the unconditional lower bound. In that case \(K(t)/t\to e^{-H}\); for \(s(a)=1/(1+a)\), \(K(t)=\log(1+t)\).

## Verification

All stationary coordinates were substituted into the five equations and the infection-age boundary law, with exact symbolic cancellation. The two rational-parameter examples and the exact power-law integrals were separately checked with the standalone `verify.py` (standard-library rational arithmetic), which prints `VERIFY_OK`. The checker is a finite algebraic consistency aid; the infinite-interval integrability criterion and convolution limit are proved above analytically, not inferred from sampled ages or a finite grid. Run with `python3 verify.py` from the directory containing this file.

## Relationship to prior work

The defining model, its \(L^1\) phase space, positive integrable hazard hypothesis, and Theorems 2.1–2.2 appear in [1, Sections 1–2]. The equilibrium coordinates printed in [1] coincide with the algebraic formulas above; the difference is that the age profile must also be integrable. This work identifies the missing infinite-age condition and its exact sharp boundary, rather than claiming the transport characteristic formula itself is new.

The intracellular transactivation model in [2] motivates the same biological transitions and derives the hazard from a waiting-time distribution; it does not supply the present finite-mean correction to [1]. The age-structured HIV existence results of [3] impose a positive lower bound on infected-cell removal, which forces exponential survival and excludes the nonintegrable-survival regime treated here. The older model in [4] derives an age-survival infected state with an explicit positive background death rate in its examples. Thus the broad principle that a stationary age density is proportional to survival is classical, but those results do not establish the exact existence failure under [1]'s printed integrable-hazard assumption or the invariant-reproduction-number tail transition for its transactivation subsystem.

## Limitations

No assertion is made that every supercritical trajectory has positive limiting infection incidence, that the total age mass necessarily diverges without that condition, or that either equilibrium is globally stable. Finite-age numerical simulations and their limiting age-boundary conventions are not adjudicated here. The power-law family lies outside [1]'s integrable-hazard restriction when \(k>0\); it is an explicit natural extension to establish the sharp boundary. The counterexample with \(s(a)=(\log2)e^{-a}\) is within [1]'s stated bounded integrable hazard assumptions. The claim concerns exact equations, with potential unindexed overlapping work remaining an originality risk.

## References

[1] L. X. Vivas-Cruz, C. Martínez-Lázaro and C. Vargas-De-León, *A mathematical and numerical study of an age-dependent transactivation model for dynamics of HIV infection*, AIMS Mathematics **10** (2025), 14560–14595. DOI: 10.3934/math.2025656. First published 2025-06-26. Full text: https://www.aimspress.com/aimspress-data/math/2025/6/PDF/math-10-06-656.pdf.

[2] C. L. Althaus and R. J. De Boer, *Intracellular transactivation of HIV can account for the decelerating decay of virus load during drug therapy*, Molecular Systems Biology (2010). DOI: 10.1038/msb.2010.4. Full text: https://link.springer.com/article/10.1038/msb.2010.4.

[3] X. Wang, J. Yang and F. Xu, *Analysis and control of an age-structured HIV-1 epidemic model with different transmission mechanisms*, Advances in Difference Equations (2018), article 36. DOI: 10.1186/s13662-017-1455-0. Full text: https://link.springer.com/article/10.1186/s13662-017-1455-0.

[4] P. W. Nelson, M. A. Gilchrist, D. Coombs, J. M. Hyman and A. S. Perelson, *An age-structured model of HIV infection that allows for variations in the production rate of viral particles and the death rate of productively infected cells*, Mathematical Biosciences and Engineering **1** (2004), 267–288. DOI: 10.3934/mbe.2004.1.267. Full text: https://www.aimspress.com/aimspress-data/mbe/2004/2/PDF/1551-0018_2004_2_267.pdf.
