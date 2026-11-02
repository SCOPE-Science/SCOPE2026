# A 236-point covariance reversal for crossings and blocks in uniform set partitions

## Finding

Let \(\Pi_n\) be a uniformly random set partition of \([n]=\{1,\ldots,n\}\), let \(K_n\) be its number of blocks, and let \(X_n\) count pairs of crossing successor arcs in its standard linear diagram. Then
\[
\operatorname{Cov}(K_n,X_n)<0\quad(4\le n\le235),\qquad
\operatorname{Cov}(K_n,X_n)>0\quad(n\ge236).
\]
For \(n\le3\), \(X_n=0\) identically. In particular, the covariance never vanishes for \(n\ge4\) and changes sign exactly once. At the boundary, its approximate values are \(-0.2772510890\) for \(n=235\) and \(+0.1897902290\) for \(n=236\). All sign assertions are proved with exact integer arithmetic and an analytic infinite-tail argument.

An exact Bell-number expression underlies the sign classification. Write \(B_m\) for the \(m\)th Bell number and
\[
\begin{aligned}
D_n={}&(2n+9)(B_nB_{n+2}-B_{n+1}^{2})
+5B_{n+1}B_{n+2}+4B_nB_{n+1}\\
&-5B_nB_{n+3}+(4n+2)B_n^2.
\end{aligned}
\]
Then, for every \(n\ge1\),
\[
4B_n^2\operatorname{Cov}(K_n,X_n)=D_n.
\]

## Assumptions and scope

A block \(\{b_1<\cdots<b_t\}\) contributes the successor arcs \((b_i,b_{i+1})\), \(1\le i<t\). Two distinct arcs \((a,b)\), \((c,d)\) cross when \(a<c<b<d\) or \(c<a<d<b\); only such pairs are counted. The probability law is uniform over the \(B_n\) set partitions, not uniform over a fixed number of blocks. The covariance is the ordinary finite-population covariance under that law. \(S(n,k)\) denotes a Stirling number of the second kind, with \(S(n,0)=0\) for \(n\ge1\). Every integer size \(n\ge1\) is covered; there are no continuous or weighted-partition extensions asserted.

## Proof

**1. Exact crossing-count polynomial.** For \(T_n(z)=\sum_{k=1}^n S(n,k)z^k\), define \(Q_n(z)=\sum_{\pi}X(\pi)z^{K(\pi)}\). The fixed-block crossing mean, established in [1, Theorem 2.3, formula (2.9)], gives the exact identity
\[
\sum_{\pi:K(\pi)=k}X(\pi)
=\left[\frac n2(k-1)-\frac52\binom{k}{2}\right]S(n,k)
+\frac32(n+1-k)S(n,k-1).
\]
Summing it against \(z^k\) yields
\[
Q_n(z)=-\frac54z^2T_n''(z)
+\left(\frac n2z-\frac32z^2\right)T_n'(z)
+\left(\frac{3n}{2}z-\frac n2\right)T_n(z).
\]
The source's definition of linear arc crossings agrees with the preceding definition; this alignment is also checked by independent enumeration of partitions with at most eight elements.

**2. Covariance identity.** Put \(\mu_n=\mathbb E K_n\), \(v_n=\operatorname{Var}(K_n)\), and \(\kappa_{3,n}=\mathbb E[(K_n-\mu_n)^3]\). Under the exponentially tilted law with partition weight proportional to \(z^{K_n}\), \(Q_n(z)/T_n(z)\) is the mean crossing count. Differentiating at \(z=1\) therefore gives \(\operatorname{Cov}(K_n,X_n)\). Equivalently, use \(\operatorname{Cov}(K_n,K_n(K_n-1))=\kappa_{3,n}+(2\mu_n-1)v_n\) to obtain
\[
\operatorname{Cov}(K_n,X_n)
=\frac{2n-10\mu_n-1}{4}v_n
-\frac54\kappa_{3,n}+\frac32(n-\mu_n).
\tag{1}
\]
The Bell moments are \(T_n(1)=B_n\), \(T_n'(1)=B_{n+1}-B_n\), \(T_n''(1)=B_{n+2}-3B_{n+1}+B_n\), and \(T_n'''(1)=B_{n+3}-6B_{n+2}+8B_{n+1}-B_n\), by repeated use of \(T_{n+1}(z)=z(T_n(z)+T_n'(z))\). Substitution in (1) and simplification gives \(4B_n^2\operatorname{Cov}(K_n,X_n)=D_n\), exactly as displayed in the finding.

**3. A strict positive tail.** The polynomials \(T_n\) have only real nonpositive zeros. A direct induction starts with \(T_1(z)=z\). If the zeros of \(T_n\) are simple, real and nonpositive, the logarithmic derivative \(1+T_n'(z)/T_n(z)=1+\sum_i(z-\rho_i)^{-1}\) is strictly decreasing between adjacent roots and has exactly one zero in each such interval, as well as one to the left of the smallest root. Thus \(T_n+T_n'\) has \(n\) distinct negative zeros, and multiplication by \(z\) completes the induction. Consequently \(T_n(z)/B_n\), the probability-generating function of \(K_n\), factors into Bernoulli probability-generating functions. The third cumulant of a Bernoulli variable of success probability \(p\) is \(p(1-p)(1-2p)\); additivity of cumulants therefore gives
\[
|\kappa_{3,n}|\le v_n.\tag{2}
\]

The log-concavity theorem for \(B_n/n!\) [2, Theorem 1] implies that \(B_{n+1}/((n+1)B_n)\) is nonincreasing with \(n\). The exact Bell recurrence and integer arithmetic verify
\[
5B_{801}<801B_{800}.\tag{3}
\]
Hence for every \(n\ge800\), \(5B_{n+1}<(n+1)B_n\), so \(5\mu_n=5(B_{n+1}/B_n-1)<n-4\). Combining this with (1) and (2) yields
\[
\operatorname{Cov}(K_n,X_n)
\ge\frac{n-5\mu_n-3}{2}v_n+\frac32(n-\mu_n)>0,
\qquad n\ge800.
\]
Here \(v_n>0\) and \(\mu_n<n\), since at least two different block counts have positive probability.

**4. Exact finite classification.** Compute \(B_0=1\) and \(B_{m+1}=\sum_{j=0}^{m}\binom mj B_j\) with unbounded integers. Evaluate the above \(D_n\) at every \(4\le n\le799\). The included independent script `verify.py` asserts, without floating-point sign tests, that \(D_n<0\) at all 232 sizes \(4\le n\le235\), and \(D_n>0\) at all 564 sizes \(236\le n\le799\), and separately checks (3). This is exhaustive over the finite range, not a sampling argument. The exact finite checks and the proven tail cover every \(n\ge4\).

## Verification

Run `python verify.py` using Python 3.9 or later; only the standard library is required. The script independently derives the relevant statistics from Stirling-number recurrences at small sizes, enumerates all partitions for \(4\le n\le8\), evaluates the Bell-number integer certificate for every \(4\le n\le799\), checks the exact tail inequality \(5B_{801}<801B_{800}\), and brackets the two boundary covariances by rational inequalities. It completed with 849 exact assertion groups/instances. Arbitrary finite testing alone does not establish the infinite-tail assertion: that follows from the root-factorization and log-concavity argument in the proof.

## Relationship to prior work

Kasraoui [1] already proves the conditional expected number of crossings at every fixed block count, and that identity is an essential input here, not a newly claimed result. Chern, Diaconis, Kane and Rhoades [3] give a general shifted-Bell-number algebra for set-partition statistics, which covers the possibility of obtaining mixed moments by other calculations. Their generic framework is not claimed new. Their later distributional study [4] and Kasraoui's limit study [5] concern marginal crossing behavior. The contribution assessed here is the exact joint covariance formula together with its sharp, global, sign-changing size classification and the finite-certificate/analytic-tail proof. No claim is made that this establishes absolute historical priority against every unpublished or inaccessible source.

## Limitations

This theorem applies only to standard linear successor-arc crossings in uniformly sampled set partitions. It does not address enhanced crossings, nestings, circular crossing conventions, other measures on partitions, or monotonicity of covariance beyond its sign. The all-size proof uses the published log-concavity theorem [2], whose hypotheses are satisfied by the Bell numbers. No independent external audit or historical-priority certification has been performed.

## References

[1] A. Kasraoui, *Average values of some Z-parameters in a random set partition*, Electronic Journal of Combinatorics **18** (2011), P228, Theorem 2.3. Full text: https://arxiv.org/pdf/1304.4813 ; journal: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p228 .

[2] N. Asai, I. Kubo and H.-H. Kuo, *Bell numbers, log-concavity, and log-convexity*, arXiv:math/0104137 (public version dated 2001-04-12), Theorem 1. https://arxiv.org/pdf/math/0104137 .

[3] B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Closed expressions for averages of set partition statistics*, arXiv:1304.4309, especially the polynomial-statistics framework. https://arxiv.org/pdf/1304.4309 .

[4] B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Central limit theorems for some set partition statistics*, arXiv:1502.00938. https://arxiv.org/pdf/1502.00938 .

[5] A. Kasraoui, *On the limiting distribution of some numbers of crossings in set partitions*, arXiv:1301.6540. https://arxiv.org/pdf/1301.6540 .
