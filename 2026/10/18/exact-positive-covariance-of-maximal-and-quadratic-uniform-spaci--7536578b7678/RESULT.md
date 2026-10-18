# Exact positive covariance of maximal and quadratic uniform spacings

## Finding
Let \(m\geq2\) and let \((S_1,\ldots,S_m)\) be the \(m\) successive gap lengths formed by \(m-1\) independent uniform points on \([0,1]\), including the two boundary gaps. Put
\[
M_m=\max_{1\leq i\leq m} S_i,\qquad G_m=\sum_{i=1}^{m} S_i^2.
\]
Here \(G_m\) is Greenwood's quadratic spacing statistic. With \(H_m=\sum_{j=1}^m1/j\) and \(H_m^{(2)}=\sum_{j=1}^m1/j^2\), the complete finite-sample covariance is
\[
\boxed{\operatorname{Cov}(M_m,G_m)
=\frac{H_m^2+H_m^{(2)}-2H_m}{m(m+1)(m+2)}>0.}
\]
Moreover, the Pearson correlation satisfies the sharp decay law
\[
\operatorname{Corr}(M_m,G_m)
\sim\frac{\sqrt6}{2\pi}\frac{(\log m)^2}{\sqrt m}
\quad(m\to\infty).
\]
Thus the two classical, differently normalized indicators of spacing irregularity are strictly positively correlated at every nontrivial finite sample size, even though their linear correlation vanishes asymptotically at the displayed rate.

## Assumptions and scope
The sample consists of exactly \(m-1\) independent, continuously distributed uniform observations on \([0,1]\), with boundary locations \(0\) and \(1\). Equivalently, the vector of \(m\) gaps is uniform on the \((m-1)\)-simplex, i.e. Dirichlet with all concentration parameters equal to one. The claim is exact for every integer \(m\ge2\) and only for this normalized null model. Ties have probability zero. We make no statement about power under alternatives, dependence of nonlinear functions, or asymptotic *independence* in distribution; asymptotic uncorrelatedness does not itself imply independence.

## Proof
The gap vector is uniform on the simplex. For a fixed subset of \(j\) distinct coordinates and \(0\le t\le1/j\), let \(A_{j,t}\) denote the event that each of those gaps exceeds \(t\). Translation of those \(j\) coordinates by \(t\) leaves a simplex scaled by \(s=1-jt\), so
\[
\Pr(A_{j,t})=s^{m-1}.
\]
Conditionally on \(A_{j,t}\), the transformed gaps are \(t+sU_i\) in the selected positions and \(sU_i\) elsewhere, where \((U_i)\) is again uniform Dirichlet. Its ordinary moments are \(\mathbb E U_i=1/m\) and \(\mathbb E\sum_iU_i^2=2/(m+1)\). Consequently,
\[
\mathbb E[G_m\mathbf1_{A_{j,t}}]
=(1-jt)^{m-1}\left(jt^2+\frac{2jt(1-jt)}m+\frac{2(1-jt)^2}{m+1}\right).
\]
Because \(M_m=\int_0^1\mathbf1_{\{M_m>t\}}\,dt\), apply inclusion-exclusion to the union of the \(m\) events \(\{S_i>t\}\), multiply by the nonnegative statistic \(G_m\), and integrate. For every \(j\ge1\), the integral appearing in the \(j\)-th inclusion-exclusion term is
\[
\begin{aligned}
I_{m,j}&=\int_0^{1/j}(1-jt)^{m-1}
\left(jt^2+\frac{2jt(1-jt)}m+\frac{2(1-jt)^2}{m+1}\right)dt\\
&=\frac{2}{m(m+1)(m+2)}\left(\frac1{j^2}+\frac{m+1}{j}\right),
\end{aligned}
\]
by substituting \(u=1-jt\) and integrating polynomials. The binomial-harmonic identities
\[
\sum_{j=1}^m(-1)^{j+1}\binom mj\frac1j=H_m,\qquad
\sum_{j=1}^m(-1)^{j+1}\binom mj\frac1{j^2}=\frac{H_m^2+H_m^{(2)}}2
\]
follow by integrating the binomial expansion of \(1-(1-z)^m\), and then integrating once more after dividing by \(z\). They yield
\[
\mathbb E[M_mG_m]
=\sum_{j=1}^m(-1)^{j+1}\binom mj I_{m,j}
=\frac{H_m^2+H_m^{(2)}+2(m+1)H_m}{m(m+1)(m+2)}.
\]
The standard Dirichlet moment and extreme-spacing tail integrations give \(\mathbb E G_m=2/(m+1)\) and \(\mathbb E M_m=H_m/m\). Subtracting the product of means proves the boxed covariance.

For strict positivity put \(C_m=H_m^2+H_m^{(2)}-2H_m\). Then \(C_1=0\) and
\[
C_{m+1}-C_m
=\frac{2(H_m-1)}{m+1}+\frac{2}{(m+1)^2}>0
\quad(m\ge1),
\]
so \(C_m>0\) for \(m\ge2\).

For the Pearson normalization, the same Dirichlet moments and integration of the maximum-spacing tail give
\[
\begin{aligned}
\operatorname{Var}(M_m)&=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)},\\
\operatorname{Var}(G_m)&=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.
\end{aligned}
\]
Indeed \(\mathbb E M_m^2=(H_m^2+H_m^{(2)})/[m(m+1)]\), while \(\mathbb E G_m^2=4(m+5)/[(m+1)(m+2)(m+3)]\). Finally \(H_m=\log m+\gamma+o(1)\) and \(H_m^{(2)}\to\pi^2/6\), so
\[
\operatorname{Cov}(M_m,G_m)\sim (\log m)^2/m^3,\quad
\operatorname{Var}(M_m)\sim\pi^2/(6m^2),\quad
\operatorname{Var}(G_m)\sim4/m^3,
\]
which proves the stated correlation asymptotic.

## Verification
An independent exact-rational reconstruction uses independent rate-one exponential variables \(E_1,\ldots,E_m\), their sum \(T\), and ordered values \(X_{(j)}=\sum_{i\le j}E_i/(m-i+1)\). The simplex gaps equal \((E_i/T)\) in distribution and are independent of \(T\), hence
\[
\mathbb E[M_mG_m]
=\frac{\mathbb E[X_{(m)}\sum_{j=1}^mX_{(j)}^2]}{m(m+1)(m+2)}.
\]
The included standalone script `checks/exact_replay.py` evaluates the independent exponential-rank numerator by exact third moments and matches the closed form, as well as both marginal variances, for every integer \(m\) from \(2\) to \(30\). It is a finite check, not the proof of the universal quantifier. Run with `python checks/exact_replay.py` using only the Python standard library.

## Relationship to prior work
Holst (1980) established classical broken-stick extreme-spacing representations and moments. Rao and Kuo (1984) studied the Greenwood test, its asymptotic distributions, and its higher-step versions. Royen (2010) established exact marginal laws for the Dirichlet quadratic sum and upper-tail inequalities involving its maximum coordinate; the latter do not determine their exact mixed moment. Bairamov, Berred and Stepanov (online 2008; journal 2010) analyzed exact and limiting laws of ordered uniform spacings, including the maximal gap. Their findings supply the two established marginal objects but do not state the displayed mixed maximal-gap/Greenwood covariance or the sharp finite-sample correlation decay. The distinct Dirichlet aggregated-risk regime of Hashorva (2014 preprint) treats tail equivalence with fixed dimension and nonconstant radial risks; its theorems do not specialize to this growing-dimension null-statistic covariance. The result here concerns only that cross-moment and its consequences, not first discovery of uniform-spacing marginal distributions or the Dirichlet representation.

## Limitations
Only symmetric Dirichlet parameter one, normalizing total gap length to one, is covered. The rate is about Pearson linear correlation, not total-variation, conditional, rank, or nonlinear independence. There may be a formula equivalent to this mixed moment in a broader ordered-Dirichlet-moment reference not located in the literature comparison. The calculation does not provide a joint null density or a combined-test critical value.

## References
1. L. Holst, “On the Lengths of the Pieces of a Stick Broken at Random,” *Journal of Applied Probability* 17 (1980), 623–634. DOI: https://doi.org/10.2307/3212956.
2. J. S. Rao and M. Kuo, “Asymptotic Results on the Greenwood Statistic and Some of its Generalizations,” *Journal of the Royal Statistical Society, Series B* 46 (1984), 228–237. DOI: https://doi.org/10.1111/j.2517-6161.1984.tb01292.x. Open manuscript: https://escholarship.org/content/qt9b00w65w/qt9b00w65w_noSplash_da50acc4f3d0182348ff623b32140d2b.pdf.
3. I. Bairamov, A. Berred, and A. Stepanov, “Limit results for ordered uniform spacings,” *Statistical Papers* 51 (2010), 227–240; first published online 10 April 2008. DOI: https://doi.org/10.1007/s00362-008-0134-3. Accessible text: https://dm.ieu.edu.tr/Ism/BaiBerredStep_StatisticalPapers.pdf.
4. E. Hashorva, “Extremes of Aggregated Dirichlet Risks,” *Journal of Multivariate Analysis* 133 (2015), 334–345. Preprint: https://arxiv.org/abs/1404.3304 (initial public posting 12 April 2014).
5. T. Royen, “The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood’s statistic,” arXiv:1008.4059 (24 August 2010). https://arxiv.org/abs/1008.4059.
