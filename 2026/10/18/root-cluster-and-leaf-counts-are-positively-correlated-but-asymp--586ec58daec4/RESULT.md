# Root-cluster and leaf counts are positively correlated but asymptotically decorrelate in percolated recursive trees

## Finding

Let \(T_n\) be the uniform rooted recursive tree on arrival labels \(1,\dots,n\): vertex \(j\ge2\) chooses one of \(1,\dots,j-1\) uniformly as its parent, independently across arrivals. Retain each edge independently with probability \(r\), independently of the tree. Write \(R_n\) for the number of vertices in the retained-edge component containing vertex \(1\), and \(L_n\) for the number of vertices with **no children in the original, unpercolated tree**.

For all integers \(n\ge2\) and \(0\le r\le1\),
\[
\operatorname{Cov}(R_n,L_n)
=\frac{r(1-r)(n-2)}{2(1+r)(n+r-1)}
\prod_{j=1}^{n-1}\left(1+\frac rj\right).
\]
The covariance is strictly positive for every \(n\ge3\) and \(0<r<1\), while it vanishes at the indicated boundary parameters. For fixed \(0<r<1\),
\[
\operatorname{Cov}(R_n,L_n)\sim
\frac{r(1-r)}{2(1+r)\Gamma(1+r)}\,n^r.
\]
Despite this divergent covariance, the correlation tends to zero at the **same exponent** for every fixed interior retention probability:
\[
\operatorname{Corr}(R_n,L_n)\sim \frac{c(r)}{\sqrt n},\quad
c(r)=\frac{\sqrt{12}\,r(1-r)}{2(1+r)\Gamma(1+r)\sqrt{\frac{2}{\Gamma(1+2r)}-\frac{1}{\Gamma(1+r)^2}}}>0.
\]

## Assumptions and scope

All parent choices and edge-retention indicators are mutually independent. Leaves are defined by outdegree zero in the *original* rooted tree; they are not degree-one vertices of the percolated forest. The root is a leaf only when \(n=1\). The displayed finite-size covariance also applies at \(n=2\), when \(L_2=1\) deterministically. The correlation result requires \(n\ge3\) and \(0<r<1\), since boundary cases have zero variance in at least one statistic. The limit holds with \(r\) fixed, not in regimes where \(r\) depends on \(n\).

## Proof

Let \(\mathcal F_n\) contain all parent choices and retention indicators through stage \(n\). Let \(K_n\) count original-tree leaves that also belong to the retained root component. Put \(A_n=\mathbb E R_n\), \(B_n=\mathbb E L_n\), and \(C_n=\operatorname{Cov}(R_n,L_n)\).

When vertex \(n+1\) arrives, let \(U\) be its uniform parent, let \(Y\) indicate that \(U\) is an old leaf, and let \(X\) indicate that the new edge is retained **and** \(U\) lies in the old retained root component. The updates are
\[
R_{n+1}=R_n+X,\qquad L_{n+1}=L_n+1-Y,\qquad K_{n+1}=K_n+X-\mathbf1_{\{U\text{ is a root-component leaf}\}}.
\]
Conditional on \(\mathcal F_n\),
\[
\mathbb E X=\frac{rR_n}{n},\quad
\mathbb E Y=\frac{L_n}{n},\quad
\mathbb E(XY)=\frac{rK_n}{n}.
\]
Consequently
\[
A_{n+1}=\left(1+\frac rn\right)A_n,\quad
B_{n+1}=\left(1-\frac1n\right)B_n+1,\quad
\mathbb E K_{n+1}=\left(1-\frac1n\right)\mathbb E K_n+\frac r n A_n.
\]
With \(A_1=B_1=\mathbb E K_1=1\), these recurrences give, for \(n\ge2\),
\[
A_n=\prod_{j=1}^{n-1}\left(1+\frac rj\right)
=\frac{\Gamma(n+r)}{\Gamma(1+r)\Gamma(n)},\qquad
B_n=\frac n2,\qquad \mathbb E K_n=\frac{r}{1+r}A_n.
\]
The last identity is checked at \(n=2\) and follows inductively thereafter.

Conditional covariance and the law of total covariance yield
\[
\begin{aligned}
C_{n+1}&=\left(1+\frac rn\right)\left(1-\frac1n\right)C_n
+\frac r{n^2}\mathbb E(R_nL_n)-\frac r n\mathbb E K_n\\
&=\left(1+\frac{r-1}{n}\right)C_n
+\frac{r(1-r)}{2(1+r)}\frac{A_n}{n}, \qquad n\ge2.
\end{aligned}
\]
Since \(C_2=0\), division by \(A_{n+1}=(1+r/n)A_n\) shows that \(D_n=C_n/A_n\) satisfies
\[
D_{n+1}=\frac{n+r-1}{n+r}D_n+\frac{r(1-r)}{2(1+r)(n+r)},\qquad D_2=0.
\]
The multiplier telescopes, giving \(D_n=\frac{r(1-r)}{2(1+r)}\frac{n-2}{n+r-1}\). This proves the covariance identity and strict sign assertion.

For correlation, one further exact second-moment recurrence is needed. As \(X\) is a Bernoulli indicator conditional on the history,
\[
\mathbb E\big[R_{n+1}(R_{n+1}+1)\mid\mathcal F_n\big]
=\left(1+\frac{2r}{n}\right)R_n(R_n+1).
\]
Thus
\[
\operatorname{Var}(R_n)=2\frac{\Gamma(n+2r)}{\Gamma(1+2r)\Gamma(n)}-A_n-A_n^2.
\]
Similarly, from \(L_{n+1}=L_n+1-Y\), \(Y\mid\mathcal F_n\sim\operatorname{Bernoulli}(L_n/n)\), and \(B_n=n/2\) for \(n\ge2\),
\[
\operatorname{Var}(L_{n+1})=\left(1-\frac2n\right)\operatorname{Var}(L_n)+\frac14,
\]
so \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\). For fixed \(0<r<1\), gamma-ratio asymptotics now give
\[
\operatorname{Var}(R_n)\sim v(r)n^{2r},\qquad
v(r)=\frac{2}{\Gamma(1+2r)}-\frac1{\Gamma(1+r)^2}>0.
\]
Indeed \(g(r)=\Gamma(1+2r)/\Gamma(1+r)^2\) strictly increases from \(1\) to \(2\) on \([0,1]\), because the digamma function is strictly increasing; hence \(v(r)>0\) for interior \(r\). Dividing the covariance asymptotic by the square roots of these two variance asymptotics proves the asserted \(n^{-1/2}\) correlation law and constant.

## Verification

The accompanying `verify.py` uses exact fractions to enumerate all recursive parent arrays and all edge-retention configurations for \(2\le n\le7\), with five rational retention probabilities. It independently compares the six expectations, covariances and variances \(\mathbb E R_n\), \(\mathbb E L_n\), \(\mathbb E K_n\), \(\operatorname{Cov}(R_n,L_n)\), \(\operatorname{Var}(R_n)\), and \(\operatorname{Var}(L_n)\) to the derived exact formulas. It also tests the covariance recurrence and leading asymptotic on additional parameters. This finite enumeration corroborates, but does not replace, the all-parameter proof above.

## Relationship to prior work

The model is the uniform-attachment case of the broadcasting/percolation trees of Desmarais, Holmgren and Wagner [1]. Their full original manuscript provides distributional results for the root cluster and for coloured leaves in separate sections, but the inspected results do not identify the finite mixed covariance between root-component size and **uncoloured original-tree leaf count**. Kürsten [2] obtains exact marginal root-cluster moments, which are used as background and are not claimed here. A publicly indexed calculation of \(\operatorname{Cov}(D_n,L_n)=(n-2)/(2(n-1))\) for root outdegree \(D_n\) is consistent with the \(r\downarrow0\) derivative of the present formula, but it does not imply the finite-\(r\) formula or the universal decorrelation scale. Althaus, Hartung and Steiner [3] focus on majority/root reconstruction rather than this mixed shape–percolation covariance.

## Limitations

The theorem concerns the root-connected retained component of a **uniform** recursive tree, not arbitrary preferential attachment laws or other component statistics. The positive-covariance statement does not imply positive association or a stochastic ordering of the joint law. The analysis does not establish a joint central limit theorem, nor uniformity in retention parameters approaching either endpoint. Exhaustive tests cover only the stated finite sizes. An earlier joint generating-function identity may imply the same covariance; external priority and independent mathematical audit remain open.

## References

[1] C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1 (first public 28 October 2021), https://arxiv.org/abs/2110.15050.

[2] R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275v1 (2015), https://arxiv.org/abs/1512.05275.

[3] E. Althaus, L. Hartung and R. Steiner, *A Random Walk Approach to Broadcasting on Random Recursive Trees*, Journal of Theoretical Probability (2026), https://doi.org/10.1007/s10959-026-01519-z.
