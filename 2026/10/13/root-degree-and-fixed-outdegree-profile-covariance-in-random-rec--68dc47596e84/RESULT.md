# Root-degree and fixed-outdegree profile covariance in random recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree on labels \(1,\ldots,n\). Write \(D_n\) for the number of children of vertex \(1\), and \(Y_{n,k}\) for the number of vertices having exactly \(k\) children. Define
\[
B_n(z)=\sum_{k\geq0}Y_{n,k}z^k,\qquad
h_n(z)=\operatorname{Cov}(D_n,B_n(z)).
\]

**Theorem.** For every real \(0\leq\rho<1\), uniformly for complex \(|z|\leq\rho\),
\[
h_n(z)=\frac{1}{2-z}+O_\rho\!\left(n^{-(1-\rho)}\log(n+1)\right).
\]
Consequently, for each fixed integer \(k\geq0\),
\[
\lim_{n\to\infty}\operatorname{Cov}(D_n,Y_{n,k})=2^{-(k+1)}.
\]
In particular, all fixed positive-outdegree classes have strictly positive covariance with the root degree for sufficiently large trees. For each fixed integer \(K\geq0\),
\[
\lim_{n\to\infty}\operatorname{Cov}\left(D_n,\sum_{k=0}^{K}Y_{n,k}\right)
=1-2^{-(K+1)},
\]
while the complementary count of vertices with more than \(K\) children has limiting covariance \(-1+2^{-(K+1)}\). This demonstrates noncommutation of summing the degree classes with taking the large-tree limit: \(h_n(1)=0\) for every \(n\), whereas \(\lim_{z\uparrow1}\lim_{n\to\infty}h_n(z)=1\).

The \(k=0\) case agrees with the previously known finite identity \(\operatorname{Cov}(D_n,Y_{n,0})=(n-2)/(2(n-1))\) for \(n\geq2\). The additional fixed positive-outdegree limits, uniform generating-function limit, and escape of compensating covariance are the substantive conclusions here.

## Assumptions and scope

Independently for every integer \(j=2,\ldots,n\), vertex \(j\) selects one parent uniformly from \(\{1,\ldots,j-1\}\). Outdegree means number of children, not undirected graph degree. All covariances concern the same randomly generated tree. The displayed generating-function bound holds on every fixed closed disk strictly inside the unit circle; no uniform estimate through \(z=1\) is asserted. The fixed-class limit does not assert finite-sample positivity for every \(n\). Only finite real moments are involved, so the complex covariance notation extends by bilinearity.

## Proof

Write \(c=z-1\) and
\[
a_n(z)=\mathbb E B_n(z),\qquad b_n(z)=\mathbb E z^{D_n},\qquad h_n(z)=\operatorname{Cov}(D_n,B_n(z)).
\]
At size one, \(a_1=b_1=1\) and \(h_1=0\). If \(P\) is the uniformly chosen parent of the next vertex and \(I=\mathbf1\{P=1\}\), then, conditional on \(T_n\),
\[
D_{n+1}=D_n+I,\quad B_{n+1}(z)=B_n(z)+1+c z^{\deg^+(P)}.
\]
Taking conditional first and mixed moments gives the exact recurrences
\[
\begin{aligned}
a_{n+1}&=(1+c/n)a_n+1,\\
b_{n+1}&=(1+c/n)b_n,\\
h_{n+1}&=(1+c/n)h_n+(c/n)b_n-(c/n^2)a_n.
\end{aligned}
\]
The second equation yields the finite product
\[
b_n(z)=\prod_{j=1}^{n-1}\left(1+\frac{z-1}{j}\right).
\]
Substitution into the first recurrence, checked at \(n=1\), gives
\[
a_n(z)=\frac{n}{2-z}+\frac{1-z}{2-z}b_n(z).
\]
Set \(g_n(z)=h_n(z)-(2-z)^{-1}\). The third recurrence becomes exactly
\[
g_{n+1}(z)=\left(1+\frac{z-1}{n}\right)g_n(z)+\frac{z-1}{n}b_n(z)
\left(1+\frac{z-1}{n(2-z)}\right).
\]
Fix \(\rho<1\) and put \(\delta=1-\rho>0\). For every \(|z|\leq\rho\) and integer \(j\geq2\),
\[
\left|1+\frac{z-1}{j}\right|\leq1-\frac{\delta}{j}.
\]
Therefore, uniformly on this disk, \(|b_n(z)|\leq C_\rho n^{-\delta}\), and the transition product from size \(j\) to \(n\) is bounded by \(C_\rho(j/n)^\delta\) for \(n\geq j\geq2\). Since \(2-z\) is bounded away from zero, iterating the last inhomogeneous recurrence from the bounded initial value \(g_2\) yields
\[
|g_n(z)|\leq C_\rho n^{-\delta}\left(1+\sum_{j=2}^{n-1}\frac1j\right)
\leq C'_\rho n^{-\delta}\log(n+1).
\]
This proves the uniform disk estimate. Cauchy's coefficient formula on any fixed circle \(0<\rho<1\) now shows that for each fixed \(k\), the coefficient of \(z^k\) in \(h_n(z)\) approaches that of \((2-z)^{-1}=\sum_{k\geq0}2^{-(k+1)}z^k\). Since \(B_n(z)=\sum_kY_{n,k}z^k\), the fixed-class formula follows. The finite cutoff claim follows by adding finitely many coefficients. Finally, \(\sum_{k\geq0}Y_{n,k}=n\) identically; hence \(h_n(1)=\operatorname{Cov}(D_n,n)=0\), which gives the complementary count and proves noncommutation.

## Verification

The standalone `CHECK.py` uses exact rational recurrences for all generating-polynomial coefficients and independently enumerates every recursive tree through nine vertices, checking each mixed covariance against the recurrence. It additionally checks the known exact root–leaf covariance and \(h_n(1)=0\) through size sixty. Run `python3 CHECK.py` with Python 3 and no third-party dependencies. Finite computations are checks of formulas only; the analytic estimates above establish the infinite limit.

## Relationship to prior work

Janson (2004 online publication) obtained asymptotic distributions and covariances for the **global degree counts** in random recursive trees; those statements do not directly give the mixed covariance with the distinguished root's degree. Addario-Berry and Eslava (2015 preprint) study the high-degree end of this profile, giving joint degree tails and extreme-value behavior. The root's outdegree is a label-sensitive statistic, whereas their coalescent degree-count representation works with unlabeled degree multisets. Neither inspected result explicitly supplies the fixed-degree cross-covariance or its mass-escape phenomenon. Existing root–leaf covariance results cover the special \(k=0\) identity, which is not claimed here as new.

## Limitations

The available full text of Janson's paper could not be inspected, so an implicit formula for the distinguished-root joint statistic there remains a historical originality risk. The proof covers fixed outdegree classes, not a uniform profile for degrees growing with \(n\). The statement does not characterize the precise location or magnitude of the compensating negative individual-degree covariances. The finite computations do not establish the infinite statement; the analytic proof does.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83; first published online 16 November 2004, DOI: 10.1002/rsa.20046.
2. L. Addario-Berry and L. Eslava, *High degrees of random recursive trees*, arXiv:1507.05981 (first submitted 21 July 2015); MSC 60C05, 05C80.
