# A twenty-two-vertex sign reversal and geometric root–degree-profile covariance in random recursive trees

## Finding

Let \(T_n\) be a uniform random recursive tree on labels \(1,\ldots,n\), where each vertex \(j\ge2\) independently selects a parent uniformly from \(1,\ldots,j-1\). Let \(D_n\) be the number of children of the root (vertex \(1\)), and let \(N_{k,n}\) count **all** vertices with exactly \(k\) children, including the root. The tree model is not a plane-oriented recursive tree.

For every \(n\ge2\), with \(H_m=\sum_{j=1}^m j^{-1}\) and \(H_0=0\),
\[
\operatorname{Cov}(D_n,N_{1,n})=\frac{1}{n-1}\left(\frac n4-\frac32H_{n-2}-\frac{1}{2(n-1)}\right).
\]
This covariance is exactly zero at \(n=2\), strictly negative for every \(3\le n\le21\), and strictly positive for every \(n\ge22\). In particular, the first strictly positive size is exactly \(22\), not a numerical or asymptotic estimate.

More generally, for **every fixed integer** \(k\ge0\),
\[
\lim_{n\to\infty}\operatorname{Cov}(D_n,N_{k,n})=2^{-k-1}.
\]
Consequently, for any fixed \(K\ge0\),
\[
\lim_{n\to\infty}\operatorname{Cov}\!\left(D_n,\sum_{k=0}^K N_{k,n}\right)=1-2^{-K-1}.
\]
The existing leaf identity \(\operatorname{Cov}(D_n,N_{0,n})=(n-2)/[2(n-1)]\) is included as a benchmark and is **not** claimed as new. The new content is the sharp one-child sign transition and all-fixed-degree root cross-covariance profile.

## Assumptions and scope

All vertices are counted once in \(N_{k,n}\), including the distinguished root. Outdegree always means the number of children in the rooted tree, not the undirected degree. The size \(n\) is a positive integer; the sign theorem concerns \(n\ge2\); the fixed-degree limit takes \(n\to\infty\) while holding \(k\) fixed. There is no claim of uniformity in \(k\), nor an all-finite-size positivity statement for \(k\ge2\). The model has independently chosen parents across births, with each existing vertex equally likely to receive a new child.

## Proof

Put \(B_n(z)=\sum_{v=1}^n z^{\deg^+(v)}\), and define the polynomial expectations \(\mu_n(z)=\mathbb E[B_n(z)]\), \(\rho_n(z)=\mathbb E[z^{D_n}]\), and \(A_n(z)=\operatorname{Cov}(D_n,B_n(z))\), where covariance is coefficientwise in \(z\). Initially \(B_1(z)=1\), \(D_1=0\), and \(A_1(z)=0\).

If a parent of outdegree \(r\) is selected at size \(n\), adding a new leaf changes \(B_n(z)\) by \(1+(z-1)z^r\). The root's degree increases exactly when the selected parent is the root. Uniform parent choice therefore gives
\[
\begin{aligned}
\rho_{n+1}(z)&=\left(1+\frac{z-1}{n}\right)\rho_n(z),\\
\mu_{n+1}(z)&=\left(1+\frac{z-1}{n}\right)\mu_n(z)+1,\\
A_{n+1}(z)&=\left(1+\frac{z-1}{n}\right)A_n(z)
+\frac{z-1}{n}\left(\rho_n(z)-\frac{\mu_n(z)}n\right).
\end{aligned}
\tag{1}
\]
The last identity follows from the law of total covariance: conditional expectations contribute the first term, while the conditional covariance of selecting the root and changing the degree enumerator is \((z-1)(z^{D_n}/n-B_n(z)/n^2)\).

Solving the first two recurrences gives the exact polynomial identity, interpreted by cancellation at \(z=2\),
\[
\rho_n(z)=\prod_{j=1}^{n-1}\left(1+\frac{z-1}{j}\right),\qquad
\mu_n(z)=\frac{n+(1-z)\rho_n(z)}{2-z}.
\tag{2}
\]
For \(n\ge2\), extracting coefficients \(z^0,z^1\) yields
\[
\Pr(D_n=0)=0,\quad \Pr(D_n=1)=\frac1{n-1},\quad
\mathbb E N_{0,n}=\frac n2,\quad
\mathbb E N_{1,n}=\frac n4+\frac1{2(n-1)}.
\tag{3}
\]
Write \(a_{k,n}=\operatorname{Cov}(D_n,N_{k,n})\), \(m_{k,n}=\mathbb E[N_{k,n}]\), \(p_{k,n}=\Pr(D_n=k)\), and use the convention that all coefficients with index \(-1\) are zero. Extracting coefficient \(z^k\) from the third recurrence gives the exact, all-size update
\[
a_{k,n+1}=\left(1-\frac1n\right)a_{k,n}+\frac{a_{k-1,n}}n
+\frac{p_{k-1,n}-p_{k,n}}n
-\frac{m_{k-1,n}-m_{k,n}}{n^2}.
\tag{4}
\]
For \(k=0\), (3) and (4), with \(a_{0,2}=0\), give \(a_{0,n}=(n-2)/[2(n-1)]\). Substituting this identity and (3) into (4) at \(k=1\) gives for \(n\ge2\)
\[
a_{1,n+1}=\left(1-\frac1n\right)a_{1,n}
+\frac1n\left(\frac14-\frac{3}{2(n-1)}+\frac1{2n(n-1)}\right).
\tag{5}
\]
Since \(a_{1,2}=0\), multiply (5) by \(n\), telescope, and use
\(\sum_{t=2}^{n-1}(t-1)^{-1}=H_{n-2}\) and \(\sum_{t=2}^{n-1}[t(t-1)]^{-1}=1-(n-1)^{-1}\). This proves the displayed formula for \(a_{1,n}\).

Let \(F(n)=n/4-(3/2)H_{n-2}-1/[2(n-1)]\). An exact subtraction gives
\[
F(n+1)-F(n)=\frac{n^2-7n+2}{4n(n-1)}>0\quad(n\ge7).
\tag{6}
\]
Direct rational evaluation shows \(F(3),\ldots,F(7)<0\), \(a_{1,21}=-4997771/1034633600<0\), and \(a_{1,22}=2470115/651819168>0\). Equations (6) and these finite boundary checks prove the unique transition for all integers \(n\ge2\).

For the general fixed-\(k\) limit, define \(u_k=2^{-k-1}\). From (2), \(m_{k,n}/n\to u_k\) for each fixed \(k\): the coefficient of \(z^k\) in \(n/(2-z)\) is \(nu_k\), while the coefficient of \((1-z)\rho_n(z)/(2-z)\) is bounded uniformly in \(n\) for fixed \(k\), since \(\rho_n\) is a probability generating polynomial. Also \(p_{k,n}\to0\): for every fixed \(0<s<1\), \(p_{k,n}s^k\le\rho_n(s)\to0\), using the product (2).

Rearrange (4) as
\[
a_{k,n+1}=\left(1-\frac1n\right)a_{k,n}+\frac{b_{k,n}}n,
\qquad b_{k,n}=a_{k-1,n}+p_{k-1,n}-p_{k,n}-\frac{m_{k-1,n}-m_{k,n}}n.
\tag{7}
\]
The recurrence implies \(a_{k,n}=(n-1)^{-1}\sum_{t=1}^{n-1}b_{k,t}\) for \(n\ge2\), because \(a_{k,1}=0\). For \(k=0\), \(b_{0,n}\to u_0\), so Cesàro convergence proves \(a_{0,n}\to u_0\). If \(a_{k-1,n}\to u_{k-1}\), then \(b_{k,n}\to u_{k-1}-(u_{k-1}-u_k)=u_k\). Induction and Cesàro convergence give \(a_{k,n}\to u_k\) for every fixed \(k\), completing the proof.

## Verification

The standalone Python 3 checker `verify.py` performs an independent exhaustive parent-array enumeration through \(n=9\), computes the entire finite covariance vector by exact rational arithmetic, and compares it with the recurrence (4). It also checks the degree-profile generating identity (2) at five rational values of \(z\), the explicit one-child formula through \(n=110\), the rational sign boundary, and the polynomial identity (6). Its recorded run completed **637 exact assertions** successfully. These finite tests are independent corroboration; the quantified infinite assertions are proved in the preceding section rather than inferred from enumeration.

To reproduce: `python3 verify.py` in a directory containing the standalone file. The implementation requires only the Python standard library.

## Relationship to prior work

Janson's [asymptotic degree-distribution theorem](https://www2.math.uu.se/~svantejs/papers/sj155.pdf) establishes the limiting outdegree frequencies \(u_k\), joint central limit theorems, and covariances *between global degree-count variables*. Those statements do not identify the mixed covariance between a **distinguished root's** degree and the global degree profile. The present analysis uses a different, root-marked covariance recurrence and resolves both the finite 22-vertex sign change and the unscaled fixed-degree covariance limits. The established \(k=0\) leaf formula is context, not claimed as new.

Backhausz and Móri's [study of lower levels](https://arxiv.org/abs/1112.1250) concerns degree distributions among vertices at fixed tree levels, not the full profile crossed with root degree. Acan and Hitczenko's [degree covariance analysis](https://arxiv.org/abs/1411.5756) treats **plane-oriented** recursive trees and covariances between global degree counts, a distinct model and statistic. The older Mahmoud–Smythe work on degree-count central limits is acknowledged as a related historical source. An unidentified earlier explicit root-marked identity remains possible; the cited sources do not establish that the present exact formula was previously published.

## Limitations

The limit holds for each *fixed* outdegree class and cannot be summed over all classes: for each finite \(n\), \(\sum_k a_{k,n}=\operatorname{Cov}(D_n,n)=0\), whereas \(\sum_{k\ge0}2^{-k-1}=1\). The nonuniformity arises because the root degree itself grows with \(n\); contributions from growing degree classes balance the positive fixed-class limits. No concentration or central limit theorem, no finite-sample sign classification for every \(k\), and no independent priority certification are asserted.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. [Author manuscript](https://www2.math.uu.se/~svantejs/papers/sj155.pdf); DOI: [10.1002/rsa.20046](https://doi.org/10.1002/rsa.20046). The publisher lists first online availability November 16, 2004.
2. H. M. Mahmoud and R. T. Smythe, *Asymptotic joint normality of outdegrees of nodes in random recursive trees*, Random Structures & Algorithms 3 (1992), 255–266. DOI: [10.1002/rsa.3240030305](https://doi.org/10.1002/rsa.3240030305).
3. Á. Backhausz and T. F. Móri, *Degree distribution in the lower levels of the uniform recursive tree*, [arXiv:1112.1250](https://arxiv.org/abs/1112.1250), first posted December 6, 2011.
4. H. Acan and P. Hitczenko, *On the covariances of outdegrees in random plane recursive trees*, [arXiv:1411.5756](https://arxiv.org/abs/1411.5756), first posted November 21, 2014.
