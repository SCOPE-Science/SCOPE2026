# A sharp strong-reinfection floor and two-scale endemic branches in an SEIRV model

## Finding

Consider the five-compartment SEIRV model with independent primary-transmission parameter \(\beta>0\) and recovered-class reinfection parameter \(B>0\), specified below. For **every fixed** choice of strictly positive demographic, progression, recovery, and disease-mortality rates, and every vaccine-inefficacy \(0<\sigma<1\), define
\[
A=\alpha+\mu,\quad M=\mu+\alpha\sigma,\quad
K=\frac{(\gamma+\mu)(\delta+\mu+\theta)}{\gamma},\quad
H=K-\delta>0,\quad c=\frac{\Lambda M}{A\mu},
\]
\[
\beta_\infty=\frac{H}{c},\qquad \beta_*=\frac{K}{c},\qquad
L=\frac{\Lambda\beta_\infty^2[\mu M+A\alpha\sigma^2]}{A^2\mu^2}>0.
\]
There is a finite \(B_0\), depending on these fixed rates, such that whenever \(B>B_0\) the **globally sharp subcritical positive-equilibrium threshold** \(\beta_c(B)\) exists in \((\beta_\infty,\beta_*)\). For \(0<\beta<\beta_c(B)\) there are no strictly positive equilibria; at \(\beta=\beta_c(B)\) there is exactly one, with a double positive infected root; and for \(\beta_c(B)<\beta<\beta_*\) there are exactly two. Its sharp singular asymptotics are
\[
\boxed{\beta_c(B)=\beta_\infty+\frac{2\sqrt{\delta\mu L}}{c\sqrt{B}}+O(B^{-1}),\qquad
I_c(B)=\sqrt{\frac{\delta\mu}{L}}\,B^{-1/2}+O(B^{-1}).}
\]
Consequently the lower critical vaccinated-disease-free reproduction number obeys
\[
\boxed{\mathcal R_0^C(B)=1-\frac{\delta}{K}
+\frac{2\sqrt{\delta\mu L}}{K\sqrt B}+O(B^{-1}).}
\]
In particular, ever stronger reinfection cannot drive this *equilibrium-existence* threshold below the strictly positive limit \(1-\delta/K\). For all sufficiently large \(B\), the critical threshold decreases strictly with \(B\).

There is a simultaneous **two-scale branch-separation law**. For any fixed \(\beta\) satisfying \(\beta_\infty<\beta<\beta_*\), let \(J_\beta>0\) be the unique root of \(P_\beta(J_\beta)=H\), with \(P_\beta\) defined below. The infected coordinates of the two positive equilibria satisfy
\[
I_-(B)=\frac{\mu(K-c\beta)}{B(c\beta-H)}+O(B^{-2}),\qquad
I_+(B)=J_\beta-\frac{\delta\mu}{B J_\beta[-P_\beta'(J_\beta)]}+O(B^{-2}).
\]
All error constants in these statements may depend on the fixed biological parameters; the branch expansions hold with \(\beta\) fixed strictly inside the stated interval. No claim is made about dynamical stability.

## Assumptions and scope

Fix real \(\Lambda,\alpha,\mu,\gamma,\delta,\theta>0\), vaccine inefficacy \(0<\sigma<1\), and primary transmission \(\beta>0\). Study equilibria of the autonomous system
\[
\begin{aligned}
\dot S&=\Lambda-\beta SI-(\alpha+\mu)S,\\
\dot E&=\beta SI+\beta\sigma VI+B RI-(\gamma+\mu)E,\\
\dot I&=\gamma E-(\delta+\mu+\theta)I,\\
\dot R&=\delta I-BRI-\mu R,\\
\dot V&=\alpha S-\beta\sigma VI-\mu V.
\end{aligned}
\]
A *strictly positive equilibrium* has all five coordinates positive. The result concerns equilibrium existence and the asymptotic regime \(B\to\infty\) while all other rates remain fixed. The vaccinated-disease-free reproduction number is \(\mathcal R_0=c\beta/K\). The asymptotic notation refers to that limit; it does not represent a uniform estimate as \(\mu\to0\), \(\delta\to0\), or \(\beta\) approaches either endpoint of the fixed-\(\beta\) interval.

## Proof

**1. Exact reduction and elementary signs.** Solving the susceptible, exposed, recovered, and vaccinated equilibrium equations in terms of an arbitrary infected level \(I>0\) gives
\[
S=\frac{\Lambda}{A+\beta I},\quad
E=\frac{\delta+\mu+\theta}{\gamma}I,\quad
R=\frac{\delta I}{\mu+BI},\quad
V=\frac{\alpha\Lambda}{(A+\beta I)(\mu+\beta\sigma I)}.
\]
All reconstructed coordinates are strictly positive. Substitution into the exposed equation and division by \(I>0\) yields the exact scalar condition
\[
F_B(I,\beta)=P_\beta(I)+\frac{\delta BI}{\mu+BI}-K=0,
\quad P_\beta(I)=\frac{\Lambda\beta(M+\beta\sigma I)}{(A+\beta I)(\mu+\beta\sigma I)}.
\]
This confirms, independently, the scalar reduction given in Khan–Wang–Liu–Xiong, Lemma B.1. Write the equivalent identity
\[
F_B(I,\beta)=c(\beta-\beta_\infty)
-[P_\beta(0)-P_\beta(I)]-\frac{\delta\mu}{\mu+BI}.
\tag{1}
\]
The function \(P_\beta\) is strictly decreasing with respect to \(I\ge0\), tends to zero as \(I\to\infty\), and satisfies \(P_\beta(0)=c\beta\). Indeed, it is the sum of \(\Lambda\beta/(A+\beta I)\) and \(\Lambda\alpha\beta\sigma/[(A+\beta I)(\mu+\beta\sigma I)]\). The derivative of \(P_\beta\) with respect to \(\beta\) at fixed \(I\ge0\) is strictly positive, since, setting \(x=\beta I\), its numerator after multiplication by the positive denominator \((A+x)^2(\mu+\sigma x)^2/\Lambda\) is
\[
A\mu M+2A\mu\sigma x+\sigma^2\mu x^2>0.
\tag{2}
\]
In particular \(F_B(I,\beta)<0\) for all \(I>0\) when \(\beta\le\beta_\infty\). Moreover, when \(\beta<\beta_*\),
\[
F_B(0,\beta)=c\beta-K<0,\qquad
\lim_{I\to\infty}F_B(I,\beta)=-H<0.
\tag{3}
\]

For \(\beta<\beta_*\), clearing the strictly positive denominators for \(I\ge0\) produces a cubic whose leading coefficient is \(-H B\beta^2\sigma<0\) and whose constant term is \(A\mu^2(c\beta-K)<0\). This polynomial tends to positive infinity at negative infinity and is negative at zero, so it has a strictly negative real root (counting multiplicity). Consequently it has **at most two positive roots** counted with multiplicities, regardless of the signs of its other coefficients. This prevents any hidden positive-equilibrium branches.

**2. Blow-up of the critical fold.** Set \(\varepsilon=B^{-1/2}\), \(\beta=\beta_\infty+\varepsilon z\), and \(I=\varepsilon y\), where \(y>0\). Let
\[
G(y,z,\varepsilon)=\varepsilon^{-1}F_{\varepsilon^{-2}}(\varepsilon y,\beta_\infty+\varepsilon z).
\]
Using (1), the exact reinfection deficit is \(\delta\mu\varepsilon/(y+\mu\varepsilon)\); thus the apparent singularity at \(\varepsilon=0\) is removable. The resulting function extends smoothly to \(\varepsilon=0\) on any compact set with \(y>0\), with
\[
G(y,z,0)=cz-Ly-\frac{\delta\mu}{y},\qquad
L=-P_{\beta_\infty}'(0)>0.
\]
Here direct differentiation yields the explicit \(L\) in the theorem. The limiting function has a unique, strictly concave maximum in \(y>0\). It simultaneously satisfies \(G=G_y=0\) only at
\[
y_0=\sqrt{\frac{\delta\mu}{L}},\qquad
z_0=\frac{2\sqrt{\delta\mu L}}c.
\]
At this point, \(G_z=c>0\) and \(G_{yy}=-2\delta\mu/y_0^3<0\), so the Jacobian of \((G,G_y)\) with respect to \((z,y)\) is nonsingular. The smooth implicit-function theorem provides a unique nearby nondegenerate fold \(z(\varepsilon)=z_0+O(\varepsilon)\), \(y(\varepsilon)=y_0+O(\varepsilon)\), yielding the two displayed critical asymptotics.

**3. This is the global subcritical threshold, not just a local fold.** Choose any fixed \(C>z_0\). Evaluating \(G(y_0,C,\varepsilon)\) shows that for sufficiently small positive \(\varepsilon\) the function \(F_B\) is positive somewhere at \(\beta=\beta_\infty+C\varepsilon\). It is negative everywhere when \(\beta\le\beta_\infty\). Its pointwise strict monotonicity in \(\beta\) from (2) gives a unique crossing of the global maximum through zero in this interval.

To exclude an unobserved remote fold, suppose \(\beta\in[\beta_\infty,\beta_\infty+C\varepsilon]\) and \(F_B(I,\beta)\ge0\). Equation (1) forces
\[
0\le P_\beta(0)-P_\beta(I)\le cC\varepsilon,\qquad
\frac{\delta\mu}{\mu+BI}\le cC\varepsilon.
\]
Since the strictly decreasing family \(P_\beta\) has slope bounded away from zero near \((I,\beta)=(0,\beta_\infty)\), the first bound implies \(I\le C_1\varepsilon\), uniformly. The second implies \(I\ge C_2\varepsilon\) for a fixed \(C_2>0\) once \(\varepsilon\) is small. Thus every nonnegative or zero value of \(F_B\) in the entire critical strip has \(y\) in a fixed compact subinterval of \((0,\infty)\). On that compact set \(G_{yy}\to-2\delta\mu/y^3<0\) uniformly. Hence a zero-valued global maximum must be the **unique** fold already found by the implicit-function theorem. Strict monotonicity in \(\beta\), endpoint negativity (3), and the cubic root bound then imply exactly zero, one double, or two positive roots in the respective regimes stated. Along the fold, differentiation of \(F_B(I_c(B),\beta_c(B))=0\) gives
\[
\beta_c'(B)=-\frac{\partial_B F_B(I_c(B),\beta_c(B))}{\partial_\beta F_B(I_c(B),\beta_c(B))}<0,
\]
because \(\partial_B F_B=\delta\mu I/(\mu+BI)^2>0\). The limit in reproduction-number coordinates follows from \(\mathcal R_0=c\beta/K\).

**4. Fixed-\(\beta\) separation of the endemic branches.** Fix \(\beta_\infty<\beta<\beta_*\). For the small root put \(I=s/B\). As \(B\to\infty\), the scalar equation tends uniformly on compact positive \(s\)-intervals to
\[
c\beta+\frac{\delta s}{\mu+s}-K=0.
\]
Because \(c\beta<K\) and \(c\beta>H=K-\delta\), this has exactly one positive solution \(s_0=\mu(K-c\beta)/(c\beta-H)\), with strictly positive derivative. Smooth implicit continuation in \(1/B\) gives \(I_-(B)=s_0/B+O(B^{-2})\).

For the large root, on any compact interval bounded away from \(I=0\),
\[
F_B(I,\beta)=P_\beta(I)-H-\frac{\delta\mu}{BI}+O(B^{-2}).
\]
Strict decrease of \(P_\beta\), together with \(P_\beta(0)=c\beta>H\) and \(P_\beta(\infty)=0\), produces a unique \(J_\beta>0\) with \(P_\beta(J_\beta)=H\). Because \(P_\beta'(J_\beta)<0\), the implicit-function theorem gives the large-branch expansion in the finding. For all sufficiently large \(B\) both distinct positive roots exist, and the cubic bound shows they exhaust the list.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to reconstruct the scalar equation from the five stationarity equations, verify its subcritical sign pattern for a parameter example, check the rational constants in the limiting floor and fold coefficients, and test the sign structure of the cleared cubic. Execute from the extracted package directory with `python3 verify.py`; a successful run prints `VERIFY_OK`. The proof of the unbounded-parameter asymptotics and of uniqueness is analytic and does **not** rely on finite numerical checks.

For the explicit rational rates \(\alpha=2,\mu=1,\sigma=1/2,\Lambda=5,\gamma=3,\delta=2,\theta=1\), one gets
\[
A=3,\quad M=2,\quad K=16/3,\quad H=10/3,\quad c=10/3,\quad
\beta_\infty=1,\quad\beta_*=8/5,\quad L=35/18.
\]
Consequently \(z_0=\sqrt{35}/5\) and \(y_0=6/\sqrt{35}\). At \(\beta=6/5\), \(B=100\), the exact signs \(F_B(0,\beta)=-4/3<0\), \(F_B(1/10,\beta)=5051/22737>0\), and \(F_B(1/2,\beta)=-281/663<0\) certify two endemic equilibria without rounding. Their fixed-\(\beta\) low-root leading constant is \(s_0=2\); the high-root limit is \(J_\beta=(\sqrt{94}-8)/6>0\).

## Relationship to prior work

Khan, Wang, Liu, and Xiong (2026), §§2, 5, 7 and Appendix B.1, introduced the five-state model, derived precisely its scalar equilibrium equation, proved the existence of a **finite-reinfection** subcritical fold, and computed the corresponding threshold by bisection. Their Figure 6 shows decreasing critical reproduction numbers at a few finite reinfection strengths. The present contribution neither rediscovers their fold nor their cubic: it identifies its **exact positive strong-reinfection floor**, proves its **sharp inverse-square-root approach**, and resolves the two distinct asymptotic endemic scales as recovered-class reinfection diverges. The source also established criteria concerning local stability; no additional stability theorem is asserted here.

The 2022/2023 reinfection analysis of Wang and colleagues concerns a different SEIRE mechanism and previously established reinfection-driven backward bifurcation; the model-specific singular coefficients and branch scalings above do not follow from the cited abstract or threshold results. The SVEIRE tuberculosis model of Sulayman–Abdullah–Mohd (2021) also exhibits reinfection and imperfect-vaccine backward bifurcation but includes additional treated/reinfection flows, so its epidemic state equations are not equivalent to those above. These general mechanisms and earlier threshold methods remain prior art.

## Limitations

This is a mathematical **equilibrium** result for the printed autonomous model, not a claim that any epidemic will attain the extremely large reinfection rates considered or that the upper branch is always dynamically stable. The small and large equilibrium branches are not jointly uniform as \(\beta\) approaches \(\beta_\infty\) or \(\beta_*\). The coefficients involve dimensional parameters in the units of the model; the limiting ratio \(H/K\) is dimensionless. Structural sensitivity to additional immunity classes, density-dependent demography, or a biologically constrained dependence between \(B\) and \(\beta\) is unproved. The analysis does not establish novelty against every unindexed paper; a fully downloadable publisher PDF and the complete contents of some related older articles were unavailable during literature comparison.

## References

1. A. Khan, L. Wang, J. Liu, M. Xiong, *Dynamics of an SEIRV endemic model: effects of reinfection*, Journal of Biological Dynamics 20 (2026), article 2713881, DOI: `10.1080/17513758.2026.2713881`. First published online 2026-08-08. https://www.tandfonline.com/doi/full/10.1080/17513758.2026.2713881
2. S. Wang and coauthors, *Backward bifurcation, basic reinfection number and robustness of an SEIRE epidemic model with reinfection*, International Journal of Biomathematics 16 (online 2022; volume 2023), DOI: `10.1142/S1793524522501327`.
3. F. Sulayman, F. A. Abdullah, M. H. Mohd, *An SVEIRE Model of Tuberculosis to Assess the Effect of an Imperfect Vaccine and Other Exogenous Factors*, Mathematics 9 (2021), article 327, DOI: `10.3390/math9040327`.
