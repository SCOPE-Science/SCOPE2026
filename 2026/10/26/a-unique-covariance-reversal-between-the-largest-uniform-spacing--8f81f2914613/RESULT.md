# A unique covariance reversal between the largest uniform spacing and long-gap count

## Finding

Let \(m\ge 2\) and let \((X_1,\ldots,X_m)\) be the \(m\) spacings of \(m-1\) independent uniform breakpoints of the unit interval. Equivalently, the same joint law describes the \(m\) consecutive circular gaps of \(m\) independent uniform points on a circle of unit circumference. Put
\[
M_m=\max_{1\le i\le m}X_i,\qquad
N_m(t)=\sum_{i=1}^m\mathbf1\{X_i>t\},\qquad H_m=\sum_{j=1}^m\frac1j.
\]
Here \(N_m(t)\) is also the number of uncovered connected gaps after placing clockwise arcs of length \(t\) at the sampled circular points, when zero is assigned to complete coverage. For \(0<t<1\), write \(u_+=\max\{u,0\}\). The exact covariance is
\[
\boxed{\operatorname{Cov}(M_m,N_m(t))
=(1-t)^{m-1}((m-1)t+1-H_m)
+\sum_{r=1}^{m-1}\frac{(-1)^{r+1}}{r(r+1)}\binom{m-1}{r}(1-(r+1)t)_+^m.}
\]
For each \(m\ge2\), there is a **unique** zero \(t_m\in(0,1)\) of this covariance. It is strictly negative for \(0<t<t_m\) and strictly positive for \(t_m<t<1\). Exactly \(t_2=1/2\); when \(m\ge3\),
\[
\frac1m<t_m<\frac12.
\]
The crossover has the sharp growing-dimension location
\[
\boxed{m t_m=\log\log m+\log\log\log m+o(1).}
\]
At the crossover, the expected number of gaps exceeding the cutoff diverges:
\[
\boxed{\mathbb E N_m(t_m)\sim \frac{m}{(\log m)(\log\log m)}.}
\]

## Assumptions and scope

The integer \(m\) is at least two. The random vector has the uniform distribution on the simplex \(\{x_i>0:\sum_i x_i=1\}\), that is, the symmetric Dirichlet law with all concentrations one. The threshold is deterministic and belongs to the open interval \(0<t<1\). All logarithms are natural. No claims are made about nonuniform breakpoint laws, random threshold choices, or unequal Dirichlet parameters. Strict inequalities do not include the trivial endpoint zeros at \(t=0\) and \(t=1\).

## Proof

**1. Exact conditional maximum.** The simplex survival identity for distinct labels and nonnegative shifts with sum at most one is
\[
\Pr\{X_{i_1}>s_1,\ldots,X_{i_r}>s_r\}=(1-\sum_{j=1}^r s_j)_+^{m-1}.
\]
Its inclusion–exclusion consequence for the maximum is the classical Whitworth formula. Integrating its tail yields
\[
\mu_m=\mathbb E M_m=H_m/m.
\]
The marginal density of \(X_1\) is \(f_m(x)=(m-1)(1-x)^{m-2}\) for \(0<x<1\). Conditional on \(X_1=x\), the other components are \((1-x)\) times an independent uniform \((m-1)\)-simplex vector. If \(Z\) is the maximum of that residual vector, set
\[
g_m(x)=\mathbb E[M_m\mid X_1=x]=\mathbb E\max\{x,(1-x)Z\}.
\]
Integrating the residual Whitworth tail gives the finite identity
\[
\boxed{g_m(x)=x+\sum_{r=1}^{m-1}
\frac{(-1)^{r+1}}{r(m-1)}\binom{m-1}{r}
\frac{(1-(r+1)x)_+^{m-1}}{(1-x)^{m-2}}}\qquad(0<x<1).
\]
Because of exchangeability,
\[
C_m(t):=\operatorname{Cov}(M_m,N_m(t))
=m\int_t^1f_m(x)(g_m(x)-\mu_m)\,dx.
\]
Termwise integration, using
\[
(m-1)\int_t^1x(1-x)^{m-2}\,dx
=t(1-t)^{m-1}+\frac{(1-t)^m}{m},
\]
and \(\int_t^1(1-(r+1)x)_+^{m-1}\,dx=(1-(r+1)t)_+^m/[m(r+1)]\), proves the displayed exact covariance formula.

**2. Exactly one covariance zero.** For each fixed \(Z\in[1/(m-1),1]\), the function \(x\mapsto\max\{x,(1-x)Z\}\) is convex. Hence \(g_m\) is convex. Whenever \(0\le x\le1/m\), the second argument wins, so
\[
g_m(x)=\frac{H_{m-1}}{m-1}(1-x),\quad
g_m(0)=\frac{H_{m-1}}{m-1}>\mu_m,\quad
g_m(1/m)=\frac{H_{m-1}}m<\mu_m.
\]
Also \(g_m(1)=1>\mu_m\). Convexity and these strict inequalities imply exactly two crossings \(0<\alpha_m<1/m<\beta_m<1\) of the level \(\mu_m\), with \(g_m-\mu_m\) positive outside and negative between the crossings. (For \(1/m<x<1/2\), the continuously distributed residual maximum produces strict convexity; for \(x\ge1/2\), \(g_m(x)=x\), excluding a plateau at the level.) Therefore
\[
C_m'(t)=-m f_m(t)(g_m(t)-\mu_m)
\]
is negative, then positive, then negative on those three intervals. Since \(C_m(0)=C_m(1)=0\), \(C_m(\alpha_m)<0\), and \(C_m(\beta_m)>0\), exactly one zero lies in \((\alpha_m,\beta_m)\), and the claimed signs follow.

To locate it more sharply, the lower level crossing in the initial linear region is
\[
\alpha_m=\frac1m-\frac{m-1}{m^2H_{m-1}}.
\]
For \(m\ge3\), the elementary inequality \(H_{m-1}>2(m-1)/m\) gives \(\alpha_m>1/(2m)\). The conditional density of \(X_1\) on \([0,1/m]\) is strictly decreasing, so \(\mathbb E[X_1\mid X_1\le1/m]<1/(2m)<\alpha_m\). As \(g_m\) is affine decreasing there,
\[
\mathbb E[g_m(X_1)\mid X_1\le1/m]>\mu_m.
\]
Writing the covariance integral over the *complement* of \([0,1/m]\) gives \(C_m(1/m)<0\). On the other hand the exact formula at \(t=1/2\) simplifies to
\[
C_m(1/2)=2^{1-m}\bigl((m+1)/2-H_m\bigr)>0
\]
for every \(m\ge3\). Hence \(1/m<t_m<1/2\). At \(m=2\), direct simplification gives \(C_2(t)=t(2t-1)/2\) for \(0\le t\le1/2\), and \(C_2(t)=(1-t)(2t-1)/2\) for \(1/2\le t\le1\), giving \(t_2=1/2\).

**3. Critical double-logarithmic scale.** The conditioned simplex has an exact translation-and-rescaling law:
\[
(X_1,\ldots,X_m)\mid\{X_1>t\}
\overset{d}{=}\ (t+(1-t)Y_1,(1-t)Y_2,\ldots,(1-t)Y_m),
\]
where \(Y\sim\operatorname{Dirichlet}(1,\ldots,1)\). Define
\[
Q_m(s)=\Pr\{Y_1+s>\max_{2\le j\le m}Y_j\}.
\]
Shifting the first coordinate of a maximum gives the exact integral identity
\[
\Delta_m(t):=\mathbb E[M_m\mid X_1>t]-\mu_m
=-t\mu_m+(1-t)\int_0^{t/(1-t)}Q_m(s)\,ds,
\]
and \(C_m(t)=m(1-t)^{m-1}\Delta_m(t)\).

Represent \(Y_i=E_i/T_m\) where \(E_i\) are independent unit-rate exponential variables and \(T_m=\sum_iE_i\). The comparison probability for a fixed exponential shift \(w\ge0\) is *exactly*
\[
q_m(w):=\Pr\{E_1+w>\max_{j\ge2}E_j\}
=\frac{e^w}{m}\left[1-(1-e^{-w})^m\right].
\]
A gamma Chernoff bound gives
\[
\Pr\{|T_m/m-1|>m^{-1/4}\}\le2e^{-c\sqrt m}
\]
for some constant \(c>0\) and all sufficiently large \(m\). For \(0\le z\le3\log\log m\), sandwiching the event defining \(Q_m(z/m)\) between the fixed-shift events with shifts \(z(1\pm m^{-1/4})\), and using the exact formula for \(q_m\), gives the **uniform** estimate
\[
Q_m(z/m)=\frac{e^z}{m}(1+o(1)).
\]
Consequently, uniformly at positive \(z=O(\log\log m)\),
\[
m^2\Delta_m(z/m)=-zH_m+(e^z-1)(1+o(1)).
\]
Set \(z_\pm=\log\log m+\log\log\log m\pm\varepsilon\) for arbitrary fixed \(\varepsilon>0\). Since \(H_m\sim\log m\) and \(e^{z_\pm}/(z_\pm H_m)\to e^{\pm\varepsilon}\), the expression is eventually negative at \(z_-\) and positive at \(z_+\). The already-proved unique threshold lies between them, for every fixed \(\varepsilon>0\), proving
\[
m t_m=\log\log m+\log\log\log m+o(1).
\]
Finally \(\mathbb E N_m(t)=m(1-t)^{m-1}\), and the preceding expansion gives the stated diverging critical exceedance count.

## Verification

The standalone standard-library `verify.py` checks the derivative of the finite covariance polynomial against the conditional-maximum formula at 12,298 exact-rational threshold/sample-size pairs, performs 810 rational bisection checks, and makes four independent lattice-simplex Riemann-sum comparisons. These 13,112 finite checks passed. For examples, \(C_3(1/3)=-1/27\), \(C_3(1/2)=1/24\), and \(C_4(1/4)=-25/512\). To reproduce, run `python3 verify.py`. The continuum theorem and asymptotic are justified by the proof, not by these finite computations.

## Relationship to prior work

Holst (1980) gives classical exact distributions of ordered uniform spacings, including the maximum and its mean; the Whitworth identity and exponential representation used above are not claimed as new. Hüsler (1982), Holst and Hüsler (1984), and Holst (1981) study maximum gaps and random circle coverage, including joint limit behavior. Decreusefond and Ferraz (arXiv:1008.5140, first public 2010-08-30) study components in Poisson one-dimensional geometric graphs, including a circle model. The contribution claimed here is the **finite-sample covariance with the threshold-exceedance count, its unique sign reversal, and the critical growing-dimensional double-logarithmic scale**. The 2010 public date identifies the selected motivating arXiv source, not the creation or publication date of this result. Earlier covariance formulations could exist; see limitations.

## Limitations

The proof assumes all gaps have the symmetric unit-concentration Dirichlet law. It does not establish an analogous result for other concentration vectors, nonuniform circle samples, or nonconstant arc radii. The finite computations are checks, not substitutes for the analysis. Historical-priority uncertainty remains: full texts of Hüsler (1982) and Holst–Hüsler (1984) were not available for direct comparison, although their accessible abstracts were inspected. An equivalent formulation in their results or other older work cannot be excluded. No independent mathematical audit is asserted.

## References

1. L. Holst, "On the lengths of the pieces of a stick broken at random," *Journal of Applied Probability* 17 (1980), 623–634. DOI: 10.2307/3212956. Lawfully available text: https://imprs-gw-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf.
2. L. Holst, "On convergence of the coverage by random arcs on a circle and the largest spacing," *Annals of Probability* 9 (1981), 648–655. DOI: 10.1214/aop/1176994370.
3. J. Hüsler, "Random coverage of the circle and asymptotic distributions," *Journal of Applied Probability* 19 (1982), 578–587. DOI: 10.2307/3213515.
4. L. Holst and J. Hüsler, "On the random coverage of the circle," *Journal of Applied Probability* 21 (1984), 558–566. DOI: 10.2307/3213617.
5. L. Decreusefond and E. Ferraz, "On the One dimensional Poisson Random Geometric Graph," first public arXiv posting 2010-08-30, arXiv:1008.5140, https://arxiv.org/abs/1008.5140.
