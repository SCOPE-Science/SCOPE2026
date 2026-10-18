# Convex-order endemic prevalence in multi-type SIRS waning models

## Finding
Consider the finite-type, homogeneously mixing, unvaccinated SIRS model in the next section. Define the recovery-immunity duration variable \(H\) by assigning mass \(p_j\) to the positive value \(h_j=1/\omega_j\). Suppose \(\mathcal R_0=\beta/(\mu+\gamma)>1\). There is exactly one endemic equilibrium, with infected fraction \(\widehat I(H)>0\). If two positive, finitely supported duration distributions satisfy \(H_1\preceq_{\mathrm{cx}}H_2\) (convex order: the expectation of every convex function is smaller for \(H_1\)), then
\[
\widehat I(H_1)\leq\widehat I(H_2).
\]
In particular, every nondegenerate mean-preserving spread of one homogeneous duration strictly increases endemic prevalence.

For two subpopulations of proportions \(p\) and \(1-p\), \(0<p<1\), let the mean duration be \(m>0\), and set
\[
 h_1(\sigma)=m\left(1-\sigma\sqrt{\frac{1-p}{p}}\right),\qquad
 h_2(\sigma)=m\left(1+\sigma\sqrt{\frac{p}{1-p}}\right),\qquad
 0\leq\sigma<\sqrt{\frac p{1-p}}.
\]
The endemic fraction \(\widehat I(\sigma)\) is **strictly increasing** on this entire interval, for **every** \(0<p<1\), including \(0<p<1/2\). Its derivative at zero is zero, and its universal leading heterogeneity penalty is
\[
\widehat I(\sigma)=\frac{x_0}{\mathcal R_0}
+\frac{\gamma m^2 x_0[\mu+(\mu+\gamma)x_0]}{C_0(1+\mu m)^3\mathcal R_0^2}\,\sigma^2+o(\sigma^2),
\qquad C_0=1+\frac{\gamma m}{1+\mu m},\quad x_0=\frac{\mathcal R_0-1}{C_0}.
\]
The strictly positive quadratic coefficient does not depend on the split \(p\).

## Assumptions and scope
Let \(k\geq1\) be a finite integer, \(p_j>0\), \(\sum_{j=1}^{k}p_j=1\), and \(\mu,\beta,\gamma,\omega_j>0\). For each fixed type \(j\), normalized susceptible, infectious and recovered fractions \((s_j,i_j,r_j)\) satisfy \(s_j+i_j+r_j=p_j\). Write \(I=\sum_j i_j\). The ODE is
\[
\dot s_j=\mu p_j-\beta s_j I+\omega_jr_j-\mu s_j,\quad
\dot i_j=\beta s_jI-(\gamma+\mu)i_j,\quad
\dot r_j=\gamma i_j-(\omega_j+\mu)r_j.
\]
Types have identical infectivity, susceptibility while susceptible, demographic turnover and recovery rates, and differ *only* in the recovery-immunity waning rate \(\omega_j\). This is the sudden-loss (all-at-once) immunity mechanism, not a gradual waning-of-susceptibility PDE. Heterogeneity comparison varies the empirical distribution of reciprocal rates \(h_j=1/\omega_j\) and keeps \(\mu,\beta,\gamma\) fixed. No vaccination is modeled. The claim concerns equilibrium prevalence, not global attraction or short-time incidence.

## Proof
**1. Exact endemic reduction.** Summing the infectious equilibrium equations at any endemic state gives \(\sum_js_j=1/\mathcal R_0\). With \(x=\mathcal R_0 I>0\), the individual infectious and recovered balances give
\[
i_j=xs_j,\qquad r_j=\frac{\gamma h_j}{1+\mu h_j}xs_j.
\]
Conservation \(p_j=s_j+i_j+r_j\) implies
\[
 s_j=p_j g_x(h_j),\quad
 g_x(h)=\frac{1+\mu h}{1+x+[\mu+(\mu+\gamma)x]h}
 =\left[1+x\left(1+\frac{\gamma h}{1+\mu h}\right)\right]^{-1}.
\]
The sole scalar consistency equation is
\[
 F_H(x):=\mathbb E[g_x(H)]=\frac1{\mathcal R_0}.\tag{1}
\]
For every positive duration, \(g_0(h)=1\), \(\lim_{x\to\infty}g_x(h)=0\), and \(\partial_xg_x(h)<0\). Hence when \(\mathcal R_0>1\), (1) has exactly one positive root. Conversely the above formulas reconstruct positive \(s_j,i_j,r_j\) satisfying each equilibrium equation. The resulting infected fraction is \(\widehat I(H)=x/\mathcal R_0\).

**2. Convex-order comparison.** Put \(B_x=\mu+(\mu+\gamma)x\). Direct differentiation yields
\[
\partial_hg_x(h)=-\frac{\gamma x}{(1+x+B_xh)^2},\qquad
\partial_{hh}g_x(h)=\frac{2\gamma xB_x}{(1+x+B_xh)^3}>0\quad(x,h>0).
\]
For each \(x>0\), \(g_x\) is strictly convex. Consequently \(H_1\preceq_{\mathrm{cx}}H_2\) implies \(F_{H_1}(x)\leq F_{H_2}(x)\). Since both functions strictly decrease from \(1\) to \(0\), their respective roots in (1) are ordered as \(x_1\leq x_2\), proving the stated prevalence inequality. A nondegenerate split of a point mass with its mean preserved gives strict Jensen inequality at every \(x>0\), hence strictly larger prevalence.

**3. Every two-type imbalance.** Set \(q=1-p\). For \(\sigma>0\), the two durations satisfy \(h_2>h_1>0\). Differentiation of the mean-preserving family at fixed \(x>0\) gives
\[
\frac{\partial F}{\partial\sigma}=m\sqrt{pq}\,[g_x'(h_2)-g_x'(h_1)]>0
\]
because \(g_x'\) strictly increases in \(h\). At \(\sigma=0\) the derivative is zero, while comparison of any two distinct values of \(\sigma\) yields a strict inequality by integration. Since \(\partial F/\partial x<0\), implicit differentiation shows \(\widehat I'(\sigma)>0\) for \(\sigma>0\). This argument uses neither \(p\geq1/2\) nor any special value of \(p\).

**4. Quantitative onset.** Write \(H=m(1+\sigma Z)\) with \(\mathbb E Z=0\) and \(\mathbb E Z^2=1\). At \(\sigma=0\) the root of (1) is \(x_0=(\mathcal R_0-1)/C_0\). Taylor expansion, justified by the finite support and positive denominators, gives \(F_\sigma(x_0,0)=0\) and \(F_{\sigma\sigma}(x_0,0)=m^2g_{x_0}''(m)\). Since \(F_x(x_0,0)=-C_0/\mathcal R_0^2\), the implicit-function theorem gives
\[
 \widehat I''(0)=\frac{m^2\mathcal R_0}{C_0}g_{x_0}''(m).
\]
Substituting the derivative in step 2 and \(1+x_0+B_{x_0}m=(1+\mu m)\mathcal R_0\) gives the displayed second-order coefficient, and completes the proof.

## Verification
A standalone script named `verify.py` evaluates symbolic derivatives, performs thousands of independent exact-rational mass-balance and mean-preserving-spread comparisons, and tests numerical roots for a range of group splits and epidemiological parameters. Run `python verify.py` with Python 3 and SymPy (the rational and numerical checks run without SymPy). It passed 5,109 assertions.

For example, with \(p=0.1\), \(m=1\), \(\mu=1/80\), \(\gamma=50\), \(\mathcal R_0=5\), the endemic fractions at \(\sigma=0,0.1,0.2\) are respectively approximately \(0.015878461161\), \(0.016033396184\), and \(0.016775975596\). Exact symbolic inequalities and the equilibrium proof, not these finite checks, establish the theorem for all parameters in scope.

## Relationship to prior work
El Khalifi and Britton introduced the two-waning-class SIRS system and proved its endemic prevalence increases with coefficient of variation under the restriction \(p\geq1/2\) (Proposition 2 of their November 1, 2023 preprint and April 2024 article). They explicitly reported numerical evidence but no proof for \(0<p<1/2\). The present result proves that open side of the claimed comparison and extends it from two classes to arbitrary finite distributions ordered by convex order. Their equilibrium existence and uniqueness for two classes is prior work, not claimed as new; step 1 extends its convenient scalar reduction to finite classes.

Their earlier paper on *gradual* waning compares classical sudden-loss SIRS with different within-person waning profiles; it does not order finite mixtures of sudden-loss durations in convex order. Foutel-Rodier, Charpentier and Guérin obtain convex-order comparisons for **intervals between booster vaccinations** as they affect disease-free stationary susceptibility and the invasion threshold in a different, non-Markovian vaccination model. That comparison is not the endemic-prevalence ordering in (1), and it does not settle the two-type \(p<1/2\) question. Standard Jensen and implicit-function techniques are used, not claimed as new.

## Limitations
The convex order is imposed on *reciprocal waning rates* \(H=1/\omega\), not on rates \(\omega\) themselves. Equal mean recovery-immunity duration is essential to the intended heterogeneity comparison. The theorem addresses fixed type-specific waning, symmetric mixing, and sudden immunity loss; it does not cover partial susceptibility, varying contact intensities, vaccine selection, or empirical epidemic predictions. It compares endemic equilibria when \(\mathcal R_0>1\) and does not prove their global stability. The exact publication-priority assessment is limited by the accessible literature, although the motivating article's final published Proposition 2 retains the missing case.

## References
1. M. El Khalifi and T. Britton, *SIRS epidemics with individual heterogeneity of immunity waning*, arXiv:2311.00592, version 1, first posted 2023-11-01; *Journal of Theoretical Biology* 587 (2024), 111815, doi:10.1016/j.jtbi.2024.111815.
2. M. El Khalifi and T. Britton, *Extending susceptible-infectious-recovered-susceptible epidemics to allow for gradual waning of immunity*, arXiv:2211.09062, first posted 2022-11-16; *Journal of the Royal Society Interface* 20 (2023), 20230042.
3. F. Foutel-Rodier, A. Charpentier and H. Guérin, *Optimal vaccination policy to prevent endemicity: a stochastic model*, arXiv:2306.13633, first posted 2023-06-23; *Journal of Mathematical Biology* 90 (2025), article 10, doi:10.1007/s00285-024-02171-z.
