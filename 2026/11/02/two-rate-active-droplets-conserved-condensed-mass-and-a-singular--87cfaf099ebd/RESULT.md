# Two-rate active droplets: conserved condensed mass and a singular tumbling layer

## Finding

For the one-dimensional local-Poisson-reset run-and-tumble kinetic model of Grange, allowing different strictly positive tumbling intensities in the dilute gas and dense liquid phases gives an **exactly solvable stationary two-phase interface problem**. The liquid-phase tumbling intensity changes the droplet width strictly monotonically, but it does not change either the liquid mass or the threshold for existence of a positive-width droplet. In the infinite liquid-tumbling limit, the positive-width droplet collapses weakly to a point mass with a nontrivial explicitly identified inner-layer shape.

Here is the precise theorem. Fix the total mass \(M>0\), run-speed parameter \(v_0>0\), reset intensity \(r>0\), density threshold \(\rho_m>4\), and tumbling intensities \(\alpha_g,\alpha_l>0\). Put
\[
\chi_g=\frac{\sqrt{r(r+\alpha_g)}}{v_0},\qquad
\chi_l=\frac{\sqrt{r(r+\alpha_l)}}{v_0},\qquad
\beta=\frac{\chi_l}{\chi_g},\qquad
\mu=\frac{M\chi_g}{2}.
\]

Within the class of symmetric stationary states having exactly one liquid region \((-b,b)\), \(b>0\), and a low-density, decreasing gas outside, a two-phase solution exists **if and only if** \(\mu>1\). It is unique in that class. Its half-width is
\[
\boxed{b=\frac{1}{\rho_m\chi_l}
\log\left(\frac{\beta\mu+\sqrt{1+\beta^2(\mu^2-1)}}{1+\beta}\right).}
\]
The phase masses are
\[
\boxed{M_{\rm gas}=\frac2{\chi_g},\qquad
M_{\rm liq}=M-\frac2{\chi_g}.}
\]
Thus both the threshold \(M\chi_g=2\) and the condensed mass are independent of \(\alpha_l\), despite the nontrivial dependence of \(b\) and the profile on \(\alpha_l\). At fixed \(M,r,\alpha_g,v_0,\rho_m\) with \(\mu>1\), the half-width \(b\) is strictly decreasing in \(\alpha_l>0\).

For the singular limit, write \(u_0=\operatorname{arcosh}\mu\). As \(\alpha_l\to\infty\),
\[
\boxed{\rho_m\chi_l b\longrightarrow u_0,\qquad
b\sim\frac{v_0u_0}{\rho_m\sqrt{r\alpha_l}},\qquad
\frac{\rho_l(0)}{\rho_m\beta}\longrightarrow\sqrt{\mu^2-1}.}
\]
Let \(X\) be sampled with density proportional to the liquid-phase mass and let \(Y=\rho_m\chi_l X\). The conditional distribution of \(Y\) converges to the even probability density
\[
\boxed{f_\infty(y)=
\frac{\sinh(u_0-|y|)}{2(\mu-1)}\,\mathbf1_{\{|y|<u_0\}}.}
\]
As finite mass measures, the stationary spatial profiles converge weakly to
\[
\boxed{\left(M-\frac2{\chi_g}\right)\delta_0+
\rho_{g,0}(|x|)\,dx,}
\]
where the nonnegative gas profile \(\rho_{g,0}\) is specified explicitly below and has total two-sided mass \(2/\chi_g\). In particular, faster tumbling in the dense phase contracts its width to zero **without removing any condensed mass**.

## Assumptions and scope

The density of right- and left-moving particles is \(\rho_+(x)\), \(\rho_-(x)\), with \(\rho=\rho_++\rho_-\) and \(\sigma=\rho_+-\rho_-\). Particles reset independently to the origin at rate \(r\), and their orientation is independently randomized with equal probabilities at each reset. Between resets, the speed and tumble intensity depend only on the *local total density*:
\[
v(\rho)=\begin{cases}v_0(1-\rho/\rho_m),&0\le\rho<\rho_m,\\ v_0/\rho_m,&\rho\ge\rho_m,\end{cases}
\qquad
\alpha(\rho)=\begin{cases}\alpha_g,&0\le\rho<\rho_m,\\\alpha_l,&\rho\ge\rho_m.\end{cases}
\]
A tumble randomizes the orientation; its actual reversal rate is \(\alpha(\rho)/2\). Away from the reset origin and interfaces, the stationary kinetic equations are
\[
0=-\partial_x(v\rho_+)-\frac{\alpha}{2}(\rho_+-\rho_-)-r\rho_+,
\quad
0=+\partial_x(v\rho_-)+\frac{\alpha}{2}(\rho_+-\rho_-)-r\rho_-.
\]
At each phase boundary, both orientation-resolved advective fluxes are continuous, equivalently \(R=v\rho\) and \(S=v\sigma\) are continuous. The sought branch has \(\rho\ge\rho_m\) on \(|x|<b\) and \(0<\rho<\rho_m/2\) on \(|x|>b\), with \(\rho(x)\to0\) as \(|x|\to\infty\). The profile is even in \(\rho\) and odd in \(\sigma\); the source at zero has strength \(rM\) only in the equation for \(\rho\). There is no claim of uniqueness among arbitrary multi-interface or nonsymmetric weak solutions, nor of dynamical stability or a finite-particle microscopic limit.

## Proof

**1. Outer gas.** On the positive half-line, the stationary equations give
\[
S'=-r\rho,\qquad R'=-(r+\alpha)\sigma.
\]
In a homogeneous phase, \(S^2-rR^2/(r+\alpha)\) is constant. In the gas phase it vanishes because both fluxes decay at infinity. Since \(S(x)=r\int_x^\infty\rho(y)\,dy>0\), the correct sign is
\[
\sigma_g=\eta_g\rho_g,\quad
\eta_g=\sqrt{\frac{r}{r+\alpha_g}}.
\]
Consequently \((1-2\rho_g/\rho_m)\rho_g'=-\chi_g\rho_g\). The liquid-side density at the interface is \(\rho_l(b^-)=\rho_m\), giving \(R_l(b^-)=v_0\). Continuity of \(R\) requires \(\rho_g(b^+)(1-\rho_g(b^+)/\rho_m)=1\). For \(\rho_m>4\), only the smaller root can follow a positive decaying gas branch:
\[
y_b:=\rho_g(b^+)=\frac{\rho_m}{2}\left(1-\sqrt{1-\frac4{\rho_m}}\right)<\frac{\rho_m}{2}.
\]
The unique gas profile \(\rho_{g,b}(x)\) on \(x>b\) is the unique \(\rho\in(0,y_b]\) satisfying
\[
\log\frac{\rho}{y_b}-\frac{2(\rho-y_b)}{\rho_m}=-\chi_g(x-b).
\]
Equivalently \(\rho_{g,b}(x)=-\rho_mW_0[-(2y_b/\rho_m)e^{-2y_b/\rho_m-\chi_g(x-b)}]/2\), using the principal Lambert branch. The reference limiting gas profile is \(\rho_{g,0}(z)=\rho_{g,b}(b+z)\) for \(z\ge0\); it does not depend on \(b\) or \(\alpha_l\). Continuity of \(S\) gives \(S_l(b^-)=S_g(b^+)=v_0\eta_g\). Integrating \(S'=-r\rho\) from \(b\) to infinity gives the exact half-gas mass
\[
\int_b^\infty\rho_g(x)\,dx=\frac{S_g(b)}{r}=\frac{v_0\eta_g}{r}=\frac1{\chi_g}.
\]

**2. Inner liquid and matching.** Put \(\eta_l=\sqrt{r/(r+\alpha_l)}\), \(k=\rho_m\chi_l\), and \(z=k(b-x)\). The liquid velocity is the constant \(v_l=v_0/\rho_m\). Hence \(\rho_l''=k^2\rho_l\). The two interface conditions are \(\rho_l(b)=\rho_m\) and \(\sigma_l(b)=\rho_m\eta_g\). Their unique solution is
\[
\boxed{\rho_l(x)=\rho_m[\cosh z+\beta\sinh z],\quad
\sigma_l(x)=\rho_m\eta_l[\sinh z+\beta\cosh z],\qquad 0\le x\le b.}
\]
These functions solve both stationary kinetic equations because \(v_l\partial_x\sigma_l=-r\rho_l\) and \(v_l\partial_x\rho_l=-(r+\alpha_l)\sigma_l\). They obey \(\rho_l\ge\rho_m\) and \(0<\sigma_l<\rho_l\), since \(\sigma_l/\rho_l\) lies between \(\eta_g\) and \(\eta_l\), both less than one. The gas has \(0<\sigma_g<\rho_g\), so all orientation densities are nonnegative.

**3. Exact mass equation and uniqueness.** With \(u=kb\), integration of the positive-half liquid density gives
\[
\int_0^b\rho_l(x)\,dx
=\frac1{\chi_l}[\sinh u+\beta(\cosh u-1)].
\]
Adding the half-gas mass and using \(\beta=\chi_l/\chi_g\) yields
\[
\frac{M\chi_l}{2}=\sinh u+\beta\cosh u,
\quad\text{or}\quad \beta\mu=\sinh u+\beta\cosh u.
\]
The right-hand side is strictly increasing on \(u\ge0\), with value \(\beta\) at zero; hence a unique positive solution exists precisely when \(\mu>1\). Solving the quadratic in \(e^u\) gives the displayed width formula. The resulting inward/outward half-space flux at the origin is \(S(0^+)=rM/2\), so reflection produces the correct point source of total strength \(rM\). This verifies global weak stationarity, both interface conditions, and exact mass normalization. The formula also gives the liquid and gas masses stated above.

If \(\alpha_l=\alpha_g\), then \(\beta=1\), \(u=\log\mu\) and the liquid is a pure decaying exponential; this is exactly the uniform-tumble special case of the motivating paper. The gas-only branch, when present, depends on \(\alpha_g\) alone; for \(2<M\chi_g<\rho_m/2\), a gas-only and a two-phase stationary profile coexist. No stability assertion follows from their existence.

**4. Strict width monotonicity.** Hold \(M,r,\alpha_g,v_0,\rho_m\) fixed. The half-liquid mass \((M-2/\chi_g)/2\) is fixed. For each fixed \(b>0\), the integral of \(\rho_m[\cosh(k(b-x))+\beta\sinh(k(b-x))]\) over \(0\le x\le b\) is strictly increasing in \(\chi_l\) (both \(k\) and \(\beta\) increase), and for fixed \(\chi_l\) it is strictly increasing in \(b\). Uniqueness of the mass-matching width therefore forces \(b\) to decrease strictly as \(\alpha_l\) increases.

**5. Singular dense-phase layer.** With \(\mu>1\) fixed, \(\beta\to\infty\) as \(\alpha_l\to\infty\). Divide the mass equation by \(\beta\):
\[
\mu=\cosh u+\beta^{-1}\sinh u.
\]
Since \(0<u<\operatorname{arcosh}\mu\) and the right-hand side is monotone, \(u\to u_0=\operatorname{arcosh}\mu\). This proves the width and center-height limits. For a fixed rescaled coordinate \(y=kx\), the conditional liquid measure has density
\[
\frac{\rho_l(y/k)}{kM_{\rm liq}}\mathbf1_{\{|y|<u\}}
=\frac{\cosh(u-|y|)+\beta\sinh(u-|y|)}{\chi_lM_{\rm liq}}
\mathbf1_{\{|y|<u\}}.
\]
Because \(\chi_l=\beta\chi_g\) and \(\chi_gM_{\rm liq}=2(\mu-1)\), it converges pointwise and in \(L^1\) (compact uniformly bounded supports and dominated convergence) to the displayed \(f_\infty\). Its integral equals one because \(\cosh u_0=\mu\). The unscaled liquid support shrinks to zero while its mass remains exactly \(M_{\rm liq}\); hence its measures converge weakly to \(M_{\rm liq}\delta_0\). Finally the translated gas branches converge in \(L^1\) to \(\rho_{g,0}(|x|)\), by the explicit profile, exponential decay and dominated convergence. Combining the two measures proves the claimed weak limit.

## Verification

Run `python verify.py` with Python 3 and no third-party packages. The provided executable checks gas and liquid ODE residual identities on several parameter families, nonnegative orientation populations, flux and mass matching, gas-mass quadrature, the uniform-rate reduction, strict width monotonicity, and numerical convergence to the singular-layer constants and shapes. In the present run all **594** finite checks passed. The exact theorem follows from the five analytic steps above; numerical checks alone do not certify universal quantifiers or limits.

## Relationship to prior work

Grange (2026), arXiv:2610.26149, derives the fixed-\(\alpha\) local-reset MIPS steady gas/droplet profiles, their onset and droplet optimization, and a finite return-velocity extension. The fixed-\(\alpha\) phase mass \(M-2/\chi\) and critical-rate law are thus previously known. The present extension changes the **local tumbling generator itself** from one rate to different gas/liquid rates. It requires a two-mode liquid solution rather than the paper's single exponential; the result here is the complete matching law, strict width response to the second rate, and a singular inner-layer/delta-condensation limit when the liquid tumbling becomes arbitrarily rapid. Evans and Majumdar (2018), arXiv:1808.06450, analyze homogeneous one-particle resetting with velocity randomization, not density-induced phase coexistence. Cates and Tailleur (2012), arXiv:1206.1805, motivate density-dependent motility and kinetic effects in MIPS but do not give these reset-interface formulas. A related classification with general concave gas flux and **one common tumbling intensity** accounts for the gas-flux mechanism; it does not cover the second intensity or the singular inner profile. The originality assessment is best-knowledge, not independent priority certification.

## Limitations

This is an exact statement about stationary solutions of the specified *mean-field kinetic PDE*, conditional on symmetric one-droplet structure, a decreasing lower-density gas branch, and interface flux continuity. It does not prove global uniqueness among all weak steady solutions, selection from generic initial conditions, metastability/lifetime, stochastic finite-population condensation, or convergence of the time-dependent PDE. The distributional point mass arises only as \(\alpha_l\to\infty\) **after** taking stationary profiles, not at finite \(\alpha_l\). The assumption \(\rho_m>4\) excludes the branch-point interface case \(\rho_m=4\). The principal literature-risk is a possibly broader unlocated transfer-matrix/inhomogeneous-RTP theorem that subsumes a part of the matching calculation; no such explicit two-phase conclusion was located in checked material.

## References

1. P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149 (first publicly posted 2026-10-19), https://arxiv.org/abs/2610.26149.
2. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, J. Phys. A 51 (2018), 475003, arXiv:1808.06450, https://arxiv.org/html/1808.06450v2.
3. M. E. Cates and J. Tailleur, *When are active Brownian particles and run-and-tumble particles equivalent? Consequences for motility-induced phase separation*, EPL 101 (2013), 20010, arXiv:1206.1805, https://arxiv.org/abs/1206.1805.
