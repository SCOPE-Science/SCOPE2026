# Exact Kendall-inversion covariance with every long-displacement threshold

## Finding

Let \(\pi\) be uniform on the symmetric group \(S_n\), where \(n\ge2\). Write \(I_n\) for its number of Kendall inversions, and for an integer \(1\le t<n\) let \(H_{n,t}\) be the number of positions at which the permutation moves a label a distance at least \(t\):
\[
I_n=\sum_{1\le i<j\le n}\mathbf1\{\pi(i)>\pi(j)\},\qquad
H_{n,t}=\sum_{i=1}^{n}\mathbf1\{|\pi(i)-i|\ge t\}.
\]
Then their covariance is exactly
\[
\boxed{\operatorname{Cov}(I_n,H_{n,t})
=\frac{(n-t)(n-t+1)\bigl(2nt-n+t^2-t+1\bigr)}{6n(n-1)}>0.}
\]

More generally, for every nondecreasing function \(f:\{0,\ldots,n-1\}\longrightarrow\mathbb R\), let
\(F_f=\sum_{i=1}^n f(|\pi(i)-i|)\). Then
\[
\operatorname{Cov}(I_n,F_f)
=\sum_{t=1}^{n-1}\bigl(f(t)-f(t-1)\bigr)
\frac{(n-t)(n-t+1)(2nt-n+t^2-t+1)}{6n(n-1)}\ge0.
\]
The inequality is strict if and only if \(f\) is nonconstant. Thus every genuinely increasing symmetric displacement penalty is strictly positively correlated, in the covariance sense, with inversion count.

Among integer thresholds, the covariance has an exact maximizing transition. Define
\[
\alpha_n=\frac{\sqrt{3n^2-2}-n}{2}.
\]
If \(\alpha_n\) is not an integer, its unique maximizer is \(t=\lceil\alpha_n\rceil\). If \(\alpha_n\) is an integer, both \(t=\alpha_n\) and \(t=\alpha_n+1\) and no others maximize the covariance. In particular, every maximizing threshold satisfies \(t/n\longrightarrow(\sqrt3-1)/2\). This optimization concerns **covariance**, not correlation.

## Assumptions and scope

The sample space is all \(n!\) bijections \(\pi:\{1,\dots,n\}\to\{1,\dots,n\}\), each equally likely. Displacements use the absolute difference between a position and the value at that position, with both indexed from one. The threshold \(t\) must be an integer in \(\{1,\dots,n-1\}\); for \(t\ge n\) the count is identically zero. The penalty \(f\) is any deterministic real-valued function on the finite set of allowed displacements, with no continuity or smoothness assumption. Covariances are ordinary population covariances, not sample covariances. For \(n=2\) the sole threshold is \(t=1\); the theorem includes this boundary.

## Proof

Set \(c=(n+1)/2\). Condition on the event \(\pi(i)=j\), where \(1\le i,j\le n\). The remaining values are in a uniform random order. Pairs of positions excluding \(i\) contribute conditional expectation \((n-1)(n-2)/4\) inversions. The \(i-1\) positions before \(i\) exceed \(j\) with probability \((n-j)/(n-1)\), whereas the \(n-i\) positions after \(i\) fall below \(j\) with probability \((j-1)/(n-1)\). Hence
\[
\mathbb E[I_n\mid\pi(i)=j]
=\frac{(n-1)(n-2)}4
+\frac{(i-1)(n-j)+(n-i)(j-1)}{n-1}.
\]
Using \(\mathbb E I_n=n(n-1)/4\), direct expansion gives the exact centered conditional expectation
\[
\boxed{\mathbb E[I_n\mid\pi(i)=j]-\mathbb E I_n
=-\frac{2(i-c)(j-c)}{n-1}.}
\]
Since \(\Pr\{\pi(i)=j\}=1/n\), linearity of covariance yields
\[
\operatorname{Cov}(I_n,H_{n,t})
=-\frac{2}{n(n-1)}\sum_{\substack{1\le i,j\le n\\|i-j|\ge t}}(i-c)(j-c).
\]
For each fixed diagonal distance \(d\in\{1,\ldots,n-1\}\), pair the upper and lower diagonals and expand the quadratic sum:
\[
\begin{aligned}
S_d
&=\sum_{|i-j|=d}(i-c)(j-c)\\
&=2\sum_{i=1}^{n-d}(i-c)(i+d-c)\\
&=\frac{(d-n)(2d^2+2dn-n^2+1)}6.
\end{aligned}
\]
Summing this cubic polynomial over \(d=t,\ldots,n-1\) gives, by the usual formulas for sums of powers,
\[
\sum_{d=t}^{n-1}S_d
=-\frac{(n-t)(n-t+1)(2nt-n+t^2-t+1)}{12}.
\]
Inserting it into the conditional-covariance identity proves the formula. Its numerator is strictly positive, since \(n-t\ge1\) and
\[
2nt-n+t^2-t+1=n(2t-1)+t(t-1)+1>0
\]
for all indicated \(n,t\).

Every nondecreasing penalty has the exact layer-cake representation
\[
f(d)=f(0)+\sum_{t=1}^{n-1}\bigl(f(t)-f(t-1)\bigr)\mathbf1\{d\ge t\},
\]
valid for each \(d\in\{0,\ldots,n-1\}\). Summation over all positions, followed by covariance, proves the claimed nonnegative combination of strictly positive terms. If \(f\) is nonconstant and nondecreasing, at least one coefficient is positive, proving strictness; if constant, covariance is zero.

Finally let \(c_{n,t}=\operatorname{Cov}(I_n,H_{n,t})\). Its exact first difference is
\[
\boxed{c_{n,t+1}-c_{n,t}=
\frac{(t-n)(2t^2+2nt-n^2+1)}{3n(n-1)}}
\qquad(1\le t\le n-2).
\]
The quadratic factor is strictly increasing for nonnegative \(t\), with unique positive root \(\alpha_n=(\sqrt{3n^2-2}-n)/2\). Since \(t-n<0\), the sequence increases when \(t<\alpha_n\), decreases when \(t>\alpha_n\), and has one equal adjacent pair when \(t=\alpha_n\) is integral. This proves the maximizing-threshold classification. The asymptotic ratio follows by dividing \(\alpha_n\) by \(n\) and taking the limit.

## Verification

Run `python3 check.py` with Python 3's standard library. The verifier enumerates every permutation for orders \(2\le n\le8\), computes mixed moments and covariances by exact fractions without using the conditional-expectation proof, and compares them with the closed form. It also checks the finite-difference identity and maximizing thresholds for orders through \(n=500\). One recorded execution passed 124,865 exact assertions/checks while enumerating 46,232 permutations in total. These checks corroborate the algebra but are not proofs for unbounded \(n\); the preceding conditional-expectation and summation arguments establish the theorem for all indicated parameters.

For an independent comparison with a previously known special case, summing the threshold covariances produces the published formula
\[
\operatorname{Cov}\left(I_n,\sum_{i=1}^n|\pi(i)-i|\right)
=\frac{(n+1)(n^2+1)}{30}.
\]
This summed identity is **not** asserted as new.

## Relationship to prior work

Diaconis and Graham (1977) investigated Spearman's footrule, its relation to Kendall inversions, and associated limiting theory. Jiang (2011) analyzed joint/asymptotic relationships among permutation ranking metrics, including Kendall inversions and the Spearman family of absolute-displacement powers. Petersen and Guay-Paquet (2014) derived a generating function for the total displacement, \(\sum_i|\pi(i)-i|\), via weighted Motzkin paths. Ekhad and Zeilberger (2021) explicitly computed the joint inversion/total-displacement covariance displayed above and studied the joint generating function. Dimitrov and Khare (2021) established a general moment method for permutations counted by bivincular patterns.

The evaluated covariance at **each** distance threshold, strict positivity for **every** increasing distance penalty, and the exact optimizing threshold are the present contribution. Neither the total-displacement marginal law nor the bivariate law of inversion count and total displacement determines the separate threshold counts: for example, in order four, \(\pi=(2,1,4,3)\) and \(\pi=(1,3,4,2)\) each have two inversions and total displacement four, but their numbers of displacements at least two are zero and one, respectively. This distinguishes the claimed invariant from previously published aggregates. It does not rule out implicit prior derivations through more general methods.

## Limitations

These are covariance statements, not assertions of stochastic monotonicity, positive association of the complete joint law, or universal positive correlation after normalization optimization. No limiting joint distribution or tail inequality is proved. An earlier specialized identity may implicitly cover the threshold covariance; the historical-priority assessment is necessarily incomplete. In particular, the complete 1977 article could not be obtained for a page-by-page comparison. Independent scientific and historical verification has not been performed.

## References

1. P. Diaconis and R. L. Graham, “Spearman's Footrule as a Measure of Disarray,” *Journal of the Royal Statistical Society B* 39 (1977), 262–268, https://doi.org/10.1111/j.2517-6161.1977.tb01624.x (abstract and publication metadata inspected; full text unavailable).
2. Y. Jiang, “Asymptotic independence of Spearman’s uniform metric with other metrics,” arXiv:1110.0807v1 (4 October 2011), https://arxiv.org/html/1110.0807v1 (primary category statistics theory, full HTML inspected).
3. T. K. Petersen and M. Guay-Paquet, “The generating function for total displacement,” arXiv:1404.4674v1 (18 April 2014), https://arxiv.org/html/1404.4674v1 (full HTML text inspected).
4. S. B. Ekhad and D. Zeilberger, “An Experimental (yet fully rigorous!) Study of a certain ‘Measure Of Disarray’ that 12-year Noga Alon Proved was always Even,” arXiv:2109.14089v2 (2021), https://arxiv.org/html/2109.14089v2 (full HTML text inspected, especially joint generating function and covariance section).
5. S. Dimitrov and N. Khare, “Moments of permutation statistics and central limit theorems,” arXiv:2109.09183v1 (2021), https://arxiv.org/html/2109.09183v1 (full HTML text inspected for general coverage).
