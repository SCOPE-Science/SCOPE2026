# Transform gaps and metric lower certificates for Satterthwaite Gamma approximation

## Statement

Let \(G_1,\ldots,G_N\) be independent Gamma random variables in shape-scale parametrization,
\[
G_i\sim \mathcal G_{\alpha_i,\beta_i},
\qquad \alpha_i>0,\quad \beta_i>0,
\]
and put
\[
S=\sum_{i=1}^N G_i,\qquad
A=\sum_{i=1}^N \alpha_i\beta_i,\qquad
B=\sum_{i=1}^N \alpha_i\beta_i^2.
\]
Thus \(\mathbb ES=A\) and \(\operatorname{Var}(S)=B\).

The Satterthwaite moment-matched Gamma law is
\[
U\sim\mathcal G_{\alpha,\beta},
\qquad
\beta=\frac BA,\qquad
\alpha=\frac{A^2}{B},
\]
so that \(U\) has the same mean and variance as \(S\).

Define the mean-size-biased scale weights
\[
w_i=\frac{\alpha_i\beta_i}{A},
\qquad \sum_i w_i=1,
\]
and the scale-heterogeneity functional
\[
V_\beta=\sum_i w_i(\beta_i-\beta)^2.
\]
Then \(\beta=\sum_iw_i\beta_i\).

### Theorem 1: every higher cumulant is underestimated

For every integer \(r\ge 3\),
\[
\kappa_r(S)-\kappa_r(U)
=
(r-1)!\,A
\left[
\sum_iw_i\beta_i^{\,r-1}
-\left(\sum_iw_i\beta_i\right)^{r-1}
\right]
\ge 0.
\]
The inequality is strict unless all scales \(\beta_i\) are equal.

In particular,
\[
\boxed{\;
\kappa_3(S)-\kappa_3(U)=2A\,V_\beta .
\;}
\]
Because the first two cumulants agree, the standardized-skewness defect is exactly
\[
\gamma_1(S)-\gamma_1(U)
=
\frac{2A\,V_\beta}{B^{3/2}}.
\]

Thus scale heterogeneity produces a one-sided hierarchy: the two-moment Gamma match gets the first two cumulants exactly but underestimates every cumulant from order three onward.

### Theorem 2: global Laplace- and moment-generating-function gaps

Let
\[
L_X(s)=\mathbb E e^{-sX},\qquad s>0,
\]
and let \(M_X(t)=\mathbb E e^{tX}\) where finite. Then
\[
\boxed{\;
L_S(s)\le L_U(s)\qquad\text{for every }s>0,
\;}
\]
while
\[
\boxed{\;
M_S(t)\ge M_U(t)
\qquad
\text{for }0<t<\frac1{\max_i\beta_i}.
\;}
\]
Both inequalities are strict for every admissible positive transform parameter whenever the scales are not all equal.

More quantitatively, writing \(M=\max_i\beta_i\),
\[
\log\frac{L_U(s)}{L_S(s)}
\ge
\frac{A\,V_\beta\,s^3}{3(1+sM)^3},
\qquad s>0,
\]
and
\[
\log\frac{M_S(t)}{M_U(t)}
\ge
\frac{A\,V_\beta\,t^3}{3},
\qquad 0<t<M^{-1}.
\]

Hence the Satterthwaite law is separated from the exact Gamma convolution not only by the third moment: the separation has a fixed sign at every positive Laplace-transform point and every common positive MGF point.

### Theorem 3: explicit lower certificates in the same smooth metrics used by Gamma-Stein upper bounds

Let
\[
d_1(X,Y)
=
\sup_{\|h'\|_\infty\le1}
|\mathbb Eh(X)-\mathbb Eh(Y)|
\]
be the \(1\)-Wasserstein distance in smooth-test form, and let
\[
d_2(X,Y)
=
\sup_{\|h''\|_\infty\le1}
|\mathbb Eh(X)-\mathbb Eh(Y)|
\]
be the second-order Zolotarev ideal metric, finite here because the first two moments match.

Set
\[
\Delta(s)=L_U(s)-L_S(s)\ge0.
\]
Then
\[
\boxed{\;
d_1(S,U)
\ge
\sup_{s>0}\frac{\Delta(s)}s,
\qquad
d_2(S,U)
\ge
\sup_{s>0}\frac{\Delta(s)}{s^2}.
\;}
\]
The transforms are explicit:
\[
L_S(s)=\prod_i(1+s\beta_i)^{-\alpha_i},
\qquad
L_U(s)=(1+s\beta)^{-A/\beta}.
\]
Consequently the lower certificates are directly computable from the same Gamma parameters as the Satterthwaite approximation.

Using Theorem 2 gives the fully explicit heterogeneity-only bounds
\[
d_1(S,U)
\ge
\sup_{s>0}
\frac{(1+s\beta)^{-A/\beta}}s
\left[
1-\exp\left\{
-\frac{A\,V_\beta s^3}{3(1+sM)^3}
\right\}
\right],
\]
and
\[
d_2(S,U)
\ge
\sup_{s>0}
\frac{(1+s\beta)^{-A/\beta}}{s^2}
\left[
1-\exp\left\{
-\frac{A\,V_\beta s^3}{3(1+sM)^3}
\right\}
\right].
\]

For a third-order smooth ideal metric
\[
d_3^\star(X,Y)
=
\sup_{\operatorname{Lip}(h'')\le1}
|\mathbb Eh(X)-\mathbb Eh(Y)|,
\]
applied to the standardized variables
\[
X=\frac{S-A}{\sqrt B},\qquad
Y=\frac{U-A}{\sqrt B},
\]
the cubic test \(h(x)=x^3/6\) yields the particularly simple obstruction
\[
\boxed{\;
d_3^\star(X,Y)
\ge
\frac{A\,V_\beta}{3B^{3/2}}.
\;}
\]

### Corollary: exactness characterization

The following are equivalent:

1. the scales \(\beta_1,\ldots,\beta_N\) are all equal;
2. \(V_\beta=0\);
3. \(S\) is exactly Gamma with the Satterthwaite parameters;
4. equality holds in either transform comparison at one positive admissible transform point;
5. \(\kappa_r(S)=\kappa_r(U)\) for one, hence every, \(r\ge3\).

Thus the scale-heterogeneity functional \(V_\beta\) is an exact obstruction to Satterthwaite exactness.

## Proof

### Cumulants

For a shape-scale Gamma variable,
\[
\kappa_r(\mathcal G_{a,b})=(r-1)!\,a b^r.
\]
Independence therefore gives
\[
\kappa_r(S)
=(r-1)!\sum_i\alpha_i\beta_i^r
=(r-1)!\,A\sum_iw_i\beta_i^{r-1}.
\]
For the matched Gamma,
\[
\kappa_r(U)
=(r-1)!\,\alpha\beta^r
=(r-1)!\,A\beta^{r-1}.
\]
Since \(x\mapsto x^{r-1}\) is strictly convex on \((0,\infty)\) for \(r\ge3\), Jensen's inequality proves Theorem 1. At \(r=3\), the Jensen gap is exactly \(V_\beta\).

### Laplace-transform inequality

Write
\[
g_s(x)=\frac{\log(1+sx)}x
=\int_0^s\frac{du}{1+ux}.
\]
For every \(s>0\), \(g_s\) is strictly convex because
\[
g_s''(x)
=
\int_0^s\frac{2u^2}{(1+ux)^3}\,du>0.
\]
The two Laplace transforms satisfy
\[
\log L_S(s)
=
-A\sum_iw_i g_s(\beta_i),
\qquad
\log L_U(s)
=
-A g_s(\beta).
\]
Jensen therefore gives \(L_S(s)\le L_U(s)\), strictly under nonconstant scales.

Moreover, for \(x\le M\),
\[
g_s''(x)
\ge
\frac{2s^3}{3(1+sM)^3}.
\]
Strong convexity thus yields
\[
\sum_iw_i g_s(\beta_i)-g_s(\beta)
\ge
\frac{s^3}{3(1+sM)^3}V_\beta,
\]
which proves the quantitative logarithmic gap.

### MGF inequality

For \(0<t<M^{-1}\), define
\[
h_t(x)=\frac{-\log(1-tx)}x
=\int_0^t\frac{du}{1-ux}.
\]
Again \(h_t\) is strictly convex, with
\[
h_t''(x)
=
\int_0^t\frac{2u^2}{(1-ux)^3}\,du
\ge \frac{2t^3}{3}.
\]
Now
\[
\log M_S(t)
=
A\sum_iw_i h_t(\beta_i),
\qquad
\log M_U(t)
=
A h_t(\beta).
\]
Jensen and strong convexity give both MGF claims.

### Metric certificates

For every \(s>0\),
\[
q_s(x)=\frac{1-e^{-sx}}s
\]
satisfies \(\|q_s'\|_\infty\le1\). Hence
\[
d_1(S,U)
\ge
|\mathbb E q_s(S)-\mathbb E q_s(U)|
=
\frac{L_U(s)-L_S(s)}s.
\]
Taking the supremum proves the \(d_1\) certificate.

Likewise
\[
r_s(x)=\frac{e^{-sx}}{s^2}
\]
has \(\|r_s''\|_\infty\le1\), so
\[
d_2(S,U)
\ge
\frac{L_U(s)-L_S(s)}{s^2}.
\]
The quantitative forms follow by writing
\[
L_U-L_S
=
L_U\left(1-\exp\{-\log(L_U/L_S)\}\right)
\]
and substituting the logarithmic lower bound from Theorem 2.

Finally, the standardized variables have matching first two moments, while
\[
\mathbb EX^3-\mathbb EY^3
=
\frac{\kappa_3(S)-\kappa_3(U)}{B^{3/2}}
=
\frac{2A V_\beta}{B^{3/2}}.
\]
Since \(x^3/6\) has \(1\)-Lipschitz second derivative, the displayed \(d_3^\star\) lower bound follows.

## Context and significance

Bailly, Rapin, Swan and von Sachs (2026) recently derived explicit Gamma-Stein upper bounds for Satterthwaite approximation in \(d_1\), \(d_2\), and, by smoothing, Kolmogorov distance. Their bounds are expressed directly through discrepancies between the summand scales and the matched scale. The results above provide a complementary obstruction theory: scale heterogeneity forces a signed transform gap, an exact third-cumulant defect, and explicit lower certificates in the same \(d_1\) and \(d_2\) metrics.

The transform comparison is stronger than merely observing that the third moments differ. It holds for every positive Laplace parameter and every common positive MGF parameter, and its Jensen-gap representation quantifies the effect of heterogeneity through \(V_\beta\).

Older work on weighted Gamma sums establishes majorization and stochastic-order inequalities when coefficient vectors vary, and Covo and Elalouf (2014) studied single-Gamma approximations to sums of independent Gamma variables from an infinitely-divisible viewpoint. Those works are important surrounding literature; the originality claim here is limited to the explicit moment-matched transform sandwich, its size-biased scale-variance gap, and the resulting \(d_1/d_2\) lower certificates.

## Limitations

- The result assumes independent Gamma summands with positive shapes and scales.
- The Laplace-transform and MGF inequalities do not by themselves imply a one-crossing theorem or ordinary stochastic ordering of \(S\) and \(U\).
- The \(d_1\) and \(d_2\) lower certificates are explicit but are not claimed to be optimal; exponential transform tests can be conservative when the common mean is large.
- The result does not produce a Kolmogorov lower bound.
- The full text of Covo and Elalouf (2014), a particularly relevant prior source on single-Gamma approximation, was not inspected. Its abstract and bibliographic descriptions were checked. It could contain a related transform observation, so originality is asserted only to the best of our knowledge.
- Majorization literature on weighted Gamma sums may imply special cases, particularly when summands share a common shape. No claim is made that the general idea of using convexity of Gamma transforms is new.

## References

1. G. Bailly, F. Rapin, Y. Swan, R. von Sachs, "Explicit Gamma-Stein Bounds for Satterthwaite's Approximation", arXiv:2609.17880 (2026). https://arxiv.org/abs/2609.17880
2. S. Covo, A. Elalouf, "A novel single-gamma approximation to the sum of independent gamma variables, and a generalization to infinitely divisible distributions", Electronic Journal of Statistics 8 (2014), 894-926. https://doi.org/10.1214/14-EJS914
3. M. E. Bock, P. Diaconis, F. W. Huffer, M. D. Perlman, "Inequalities for linear combinations of gamma random variables", Canadian Journal of Statistics 15 (1987), 387-395. https://doi.org/10.2307/3315257
4. S. C. Kochar, "Stochastic Comparisons of Weighted Sums of Random Variables", in Stochastic Comparisons with Applications (2022), pp. 233-255. https://doi.org/10.1007/978-3-031-12104-3_9