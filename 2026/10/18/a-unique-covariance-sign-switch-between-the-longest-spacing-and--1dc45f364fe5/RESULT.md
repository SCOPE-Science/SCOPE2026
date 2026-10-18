# A unique covariance sign switch between the longest spacing and threshold exceedances

## Finding

Let \(m\ge2\). Break a unit interval at \(m-1\) independent uniform points, forming the exchangeable spacings \((X_1,\ldots,X_m)\). Let \(M_m=\max_iX_i\) and \(N_m(t)=\sum_{i=1}^m\mathbf1\{X_i>t\}\), for \(0\le t\le1\). Write \(H_m=\sum_{r=1}^m1/r\) and \(u_+=\max\{u,0\}\).

The exact finite-sample covariance is
\[
\begin{aligned}
C_m(t)&:=\operatorname{Cov}(M_m,N_m(t))\\
&=\bigl[1+(m-1)t-H_m\bigr](1-t)^{m-1}\\
&\quad+\sum_{j=1}^{m-1}\frac{(-1)^{j+1}}{j(j+1)}\binom{m-1}{j}\bigl(1-(j+1)t\bigr)_+^m.
\end{aligned}
\]

For each integer \(m\ge2\) there is exactly one \(\tau_m\in(0,1)\) such that
\[
C_m(t)<0\quad(0<t<\tau_m),\qquad C_m(\tau_m)=0,\qquad C_m(t)>0\quad(\tau_m<t<1).
\]
For \(m=2\), \(\tau_2=1/2\). For every \(m\ge3\),
\[
\frac1m<\tau_m<\frac12.
\]
These inequalities describe all interior threshold values; \(C_m(0)=C_m(1)=0\) trivially.

## Assumptions and scope

The break points are independent \(\operatorname{Uniform}[0,1]\); the spacings have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. A gap equals a deterministic threshold with probability zero, so using strict versus weak exceedance is immaterial for \(t\in(0,1)\). The sign theorem holds at each finite integer dimension without limits in \(m\). The statistic \(M_m\) is the largest gap, not the largest of independent unnormalized exponential spacings.

## Proof

**1. Exact covariance.** The uniform-simplex formula gives, for distinct coordinates and nonnegative shifts with sum at most one,
\[
\Pr\{X_{i_1}>a_1,\ldots,X_{i_r}>a_r\}=
\left(1-\sum_{h=1}^r a_h\right)_+^{m-1}.
\]
For \(u\ge t\), inclusion–exclusion over the other \(m-1\) gaps yields
\[
\Pr\{X_1>t,M_m\le u\}
=\sum_{j=0}^{m-1}(-1)^j\binom{m-1}{j}
\left[(1-t-ju)_+^{m-1}-(1-(j+1)u)_+^{m-1}\right].
\]
Using \(\mathbb E[M_m\mathbf1_{\{X_1>t\}}]=\Pr\{X_1>t\}-\int_t^1\Pr\{X_1>t,M_m\le u\}\,du\), the integral of the \(j=0\) term is \((m-1)(1-t)^m/m\); for each \(j\ge1\), the integral of the bracket equals \((1-(j+1)t)_+^m/[mj(j+1)]\). Thus
\[
\mathbb E[M_m\mathbf1_{\{X_1>t\}}]
=(1-t)^{m-1}-\frac{m-1}{m}(1-t)^m
-\sum_{j=1}^{m-1}\frac{(-1)^j}{mj(j+1)}\binom{m-1}{j}(1-(j+1)t)_+^m.
\]
Since \(\Pr\{X_1>t\}=(1-t)^{m-1}\), exchangeability gives \(\mathbb E[M_mN_m(t)]=m\mathbb E[M_m\mathbf1_{\{X_1>t\}}]\) and \(\mathbb E[N_m(t)]=m(1-t)^{m-1}\). Finally \(\mathbb E M_m=H_m/m\), obtained by integrating the classical maximum-spacing inclusion–exclusion law, gives the displayed expression.

**2. Exactly one sign change.** Define the conditional regression \(g_m(x)=\mathbb E[M_m\mid X_1=x]\). Given \(X_1=x\), the other \(m-1\) gaps are \((1-x)\) times a fresh uniform-simplex vector, whose maximum we call \(Q_{m-1}\). Hence
\[
g_m(x)=\mathbb E\max\{x,(1-x)Q_{m-1}\}.
\]
For every fixed value of \(Q_{m-1}\), the expression inside the expectation is the maximum of two affine functions of \(x\). Consequently \(g_m\) is convex and continuous. Let \(\mu_m=H_m/m\). Because \(Q_{m-1}\ge1/(m-1)\) almost surely,
\[
g_m(x)=(1-x)\frac{H_{m-1}}{m-1}\quad(0\le x\le1/m).
\]
In particular \(g_m(0)=H_{m-1}/(m-1)>\mu_m\), while \(g_m(1/m)=H_{m-1}/m<\mu_m\). Moreover \(g_m(x)=x\) for \(x\ge1/2\), so \(g_m(1)>\mu_m\). Convexity and these strict inequalities imply that \(g_m(x)-\mu_m\) has exactly two zeros \(a_m\in(0,1/m)\) and \(b_m\in(1/m,1)\), is positive outside \([a_m,b_m]\), and negative inside. To exclude a zero interval at the upper boundary, note that the law of \(Q_{m-1}\) has a positive density on \((1/(m-1),1)\) when \(m\ge3\), making \(g_m\) strictly convex on \((1/m,1/2)\); above \(1/2\), it is the strictly increasing function \(x\). The case \(m=2\) follows directly from \(g_2(x)=\max(x,1-x)\).

The marginal density of \(X_1\) is \(f_m(x)=(m-1)(1-x)^{m-2}\), positive on \((0,1)\), and the tower property gives
\[
C_m(t)=m\int_t^1\bigl(g_m(x)-\mu_m\bigr)f_m(x)\,dx,
\qquad C_m'(t)=-m\bigl(g_m(t)-\mu_m\bigr)f_m(t).
\]
Thus \(C_m\) is strictly decreasing on \((0,a_m)\), strictly increasing on \((a_m,b_m)\), and strictly decreasing on \((b_m,1)\). Because \(C_m(0)=C_m(1)=0\), necessarily \(C_m(a_m)<0\) and \(C_m(b_m)>0\). The intermediate strictly increasing segment crosses zero exactly once, proving the sign theorem.

**3. Bounds on the switch.** Substitution into the exact formula yields
\[
C_m(1/m)=\frac{1-(1+H_{m-1})(1-1/m)^{m-1}}{m}.
\]
This is zero for \(m=2\) and strictly negative for \(m\ge3\). Indeed, for \(m=3\) the required inequality is \(5/2>9/4\); for \(m\ge4\), use \(1+H_{m-1}\ge17/6>e>(m/(m-1))^{m-1}\). At \(t=1/2\), almost surely \(N_m(1/2)=\mathbf1_{\{M_m>1/2\}}\), since at most one gap exceeds one half. For \(m\ge3\), both events \(M_m>1/2\) and \(M_m<1/2\) have positive probability, so \(\operatorname{Cov}(M_m,\mathbf1_{\{M_m>1/2\}})>0\) by conditioning on the event and its complement. For \(m=2\), \(N_2(1/2)=1\) almost surely and \(C_2(1/2)=0\). This proves all bounds.

## Verification

The standalone `verify.py` evaluates the covariance at rational thresholds using exact `Fraction` arithmetic, compares it with a distinct conditioning-and-quadrature calculation, and brackets the unique roots numerically. Execute `python verify.py` with SciPy installed. It reports 539 exact grid evaluations, 44 independent quadrature comparisons, 10 root checks, and endpoint and conditional-mean identities. These finite computations check implementations and special cases; the preceding argument proves the full claim for all \(m\ge2\).

## Relationship to prior work

The maximum-spacing distribution and its moment \(\mathbb E M_m=H_m/m\) are classical. Schlemm's 2014 complete preprint derives maximum-spacing moments and a Gumbel limit. Bose, Dasgupta and Maulik's 2008 complete preprint treats limits of Dirichlet maxima. Neither inspected work supplies the finite-sample mixed covariance \(\operatorname{Cov}(M_m,N_m(t))\), its unique sign change, or the stated bracket. The earlier works of Pyke, Holst and Darling are relevant foundations of random spacings and stick breaking; their inaccessible or incompletely inspected texts limit the strength of any priority claim. The contribution asserted here is specifically the exact **joint dependence** and complete sign classification, not the marginal spacing laws.

## Limitations

The theorem concerns symmetric Dirichlet spacings with unit concentration, not arbitrary Dirichlet parameters, nonuniform break points, or independent gaps. It makes no claim of independent validation or exhaustive historical priority review. The full texts of some older, plausibly relevant classical random-spacing references were not accessible for direct comparison, so an equivalent formula could already occur there. The numerical tests are not substitutes for a proof.

## References

1. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114v1 (public preprint, 23 May 2014), https://arxiv.org/abs/1405.6114.
2. A. Bose, A. Dasgupta and K. Maulik, *Maxima of Dirichlet and triangular arrays of gamma variables*, arXiv:0803.3518 (2008), https://arxiv.org/abs/0803.3518.
3. L. Holst, *On the lengths of the pieces of a stick broken at random*, Journal of Applied Probability 17 (1980), 623–634, doi:10.2307/3212956.
4. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B 27 (1965), 395–436, doi:10.1111/j.2517-6161.1965.tb00602.x.
5. D. A. Darling, *On a class of problems related to the random division of an interval*, Annals of Mathematical Statistics 24 (1953), 239–253, doi:10.1214/aoms/1177729030.
