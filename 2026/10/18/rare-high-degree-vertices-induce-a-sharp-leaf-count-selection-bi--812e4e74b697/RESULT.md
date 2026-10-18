# Rare high-degree vertices induce a sharp leaf-count selection bias in uniform labeled trees

## Finding

Let \(T_n\) be uniform among all \(n^{n-2}\) unrooted trees on the labeled vertex set \(\{1,\ldots,n\}\), for integer \(n\ge3\). Let \(L_n\) count its degree-one vertices (leaves), and let \(\Delta_n\) be its maximum degree. Let \(k_n\) be positive integers such that
\[
 n\,\Pr\{\operatorname{Poisson}(1)\ge k_n\}\longrightarrow\lambda\in(0,\infty).
\]
Put \(A_n=\mathbf1_{\{\Delta_n\ge k_n+1\}}\). Then
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(L_n,A_n)}{k_n}
       =\frac{\lambda e^{-\lambda}}{e}.}
\]
More precisely, the number \(H_n\) of vertices with degree at least \(k_n+1\) converges in law to \(\operatorname{Poisson}(\lambda)\), and
\[
\begin{aligned}
 \mathbb E[L_n\mid A_n=0]
 &=\mathbb E L_n-\frac{\lambda}{e}k_n+o(k_n),\\
 \mathbb E[L_n\mid A_n=1]
 &=\mathbb E L_n+\frac{\lambda e^{-\lambda}}{e(1-e^{-\lambda})}k_n+o(k_n).
\end{aligned}
\]
Hence the two conditional expectations differ by
\[
\frac{\lambda}{e(1-e^{-\lambda})}k_n+o(k_n).
\]
The known marginal maximum-degree transition and the fixed-degree leaf-count asymptotics do not alone specify this diverging, sub-central-limit-scale selection bias.

## Assumptions and scope

Uniform means every labeled unrooted tree has equal probability. The threshold sequence may follow any subsequence satisfying the displayed condition; no interpolation between integer transition windows is asserted. Since
\[
\Pr\{\operatorname{Poisson}(1)\ge k\}
=\frac{e^{-1}}{k!}\bigl(1+O(k^{-1})\bigr)
\qquad(k\to\infty),
\]
the condition entails \(k_n\to\infty\), \(n/k_n!\to e\lambda\), and \(k_n^2/n\to0\). In fact \(k_n\sim\log n/\log\log n\). The result concerns conditional *means*, not a new central limit theorem or a pointwise law for every possible integer threshold.

## Proof

**1. Exact occupancy representation.** In the Prüfer code of \(T_n\), each of the \(m=n-2\) entries is independently uniform on \(\{1,\ldots,n\}\). If \(X_i\) is the number of entries equal to \(i\), then \(\deg(i)=1+X_i\). Consequently
\[
L_n=\sum_{i=1}^n\mathbf1_{\{X_i=0\}},\qquad
H_n=\sum_{i=1}^n\mathbf1_{\{X_i\ge k\}},\qquad
\mu_n:=\mathbb E L_n=n(1-1/n)^m,
\]
where \(k=k_n\) below. For \(r\ge1\), write \(E_{n,r}=\{X_1,\ldots,X_r\ge k\}\), and \(J=X_1+\cdots+X_r\). By symmetry, with falling factorial \((z)_{\underline r}\),
\[
\mathbb E[(H_n)_{\underline r}]=(n)_{\underline r}\Pr(E_{n,r}),
\quad
\operatorname{Cov}(L_n,(H_n)_{\underline r})
=(n)_{\underline r}\mathbb E[(L_n-\mu_n)\mathbf1_{E_{n,r}}].
\]

**2. Rare high-occupancy factorial moments.** For fixed \(r\), the probability of exactly \(k\) balls in each of the specified \(r\) boxes is
\[
\Pr(X_1=\cdots=X_r=k)
=\frac{(m)_{\underline{rk}}}{n^{rk}(k!)^r}
(1-r/n)^{m-rk}
=\frac{e^{-r}}{(k!)^r}(1+o(1)).
\]
Here \(rk=o(\sqrt n)\), which follows from the threshold assumption. Relative probabilities for increasing any of the \(r\) loads above \(k\) are bounded successively by \(2/(k+1)\) for all sufficiently large \(n\). Indeed, the ratio between a load vector and the vector obtained by increasing its \(i\)-th coordinate is
\[
\frac{m-J}{n(j_i+1)(1-r/n)}\le\frac{2}{k+1}.
\]
Thus the mass on \(E_{n,r}\) is dominated by the all-\(k\) vector, with relative error \(O_r(k^{-1})\). Moreover \(\mathbb E[J\mid E_{n,r}]=rk+O_r(1)\). It follows that
\[
\mathbb E[(H_n)_{\underline r}]\longrightarrow\lambda^r
\quad\text{for each fixed }r.
\]
For later dominated convergence, note also the uniform bound
\[
\mathbb E[(H_n)_{\underline r}]
\le (n/k!)^r,
\]
obtained from \(\mathbf1_{\{X_i\ge k\}}\le(X_i)_{\underline k}/k!\) and the multinomial factorial-moment identity. Since \(n/k!\) stays bounded, the probability generating functions converge term by term on \([0,1]\) to \(\exp(\lambda(t-1))\); hence \(H_n\Rightarrow\operatorname{Poisson}(\lambda)\), with \(\Pr(H_n=0)\to e^{-\lambda}\).

**3. The mixed factorial moments.** Given \(X_1=j_1,\ldots,X_r=j_r\ge1\), the remaining \(m-J\) balls are independent uniform draws among \(n-r\) boxes. Therefore the exact conditional leaf expectation is
\[
F_n(r,J):=\mathbb E[L_n\mid X_1=j_1,\ldots,X_r=j_r]
=(n-r)\left(1-\frac1{n-r}\right)^{m-J}.
\]
For fixed \(r\) and \(J=O_r(k)\), Taylor expansion using \(k^2/n\to0\) gives
\[
F_n(r,J)-\mu_n=\frac{J-2r}{e}
             +O_r\left(\frac{(J+1)^2}{n}\right).
\]
The geometric bound on the conditional excess loads established in step 2 permits averaging the expansion on \(E_{n,r}\), giving
\[
\frac1k\,\mathbb E[L_n-\mu_n\mid E_{n,r}]\longrightarrow\frac r e.
\]
Combining with step 2 yields the key limit
\[
\boxed{\frac1k\operatorname{Cov}(L_n,(H_n)_{\underline r})
\longrightarrow\frac r e\lambda^r}\qquad(r\text{ fixed}).
\]

**4. Uniform summation and the maximum event.** We justify exchanging the limit and inclusion-exclusion over all \(r\). For \(r\le m/k\), \(n-r\ge n/2\) eventually; the function \(b(1-1/b)^t\), for \(b\in[n/2,n]\), \(0\le t\le m\), has bounded partial derivatives in \(b,t\). Comparing \((b,t)=(n-r,m-J)\) to \((n,m)\), we obtain
\[
|F_n(r,J)-\mu_n|\le C(J+r)
\quad\text{on }E_{n,r}.
\]
For \(rk>m\), the event is impossible. Otherwise multinomial factorial moments imply
\[
\begin{aligned}
\mathbb E\prod_{i=1}^r(X_i)_{\underline k}
   &=\frac{(m)_{\underline{rk}}}{n^{rk}}\le1,\\
\mathbb E\left[J\prod_{i=1}^r(X_i)_{\underline k}\right]
   &=\left(rk+\frac{r(m-rk)}n\right)
      \frac{(m)_{\underline{rk}}}{n^{rk}}
      \le r(k+1).
\end{aligned}
\]
It follows that, for one absolute constant \(C\),
\[
\left|\operatorname{Cov}(L_n,(H_n)_{\underline r})\right|
\le C r(k+2)(n/k!)^r.
\]
The right-hand side divided by \(k r!\) is uniformly summable in \(r\). The exact finite identity
\[
\mathbf1_{\{H_n=0\}}
=\sum_{r=0}^n\frac{(-1)^r}{r!}(H_n)_{\underline r}
\]
thus allows dominated convergence:
\[
\begin{aligned}
\lim_{n\to\infty}\frac1k
\operatorname{Cov}(L_n,\mathbf1_{\{H_n=0\}})
&=\frac1e\sum_{r=1}^\infty\frac{(-1)^r r\lambda^r}{r!}\\
&=-\frac{\lambda e^{-\lambda}}e.
\end{aligned}
\]
Since \(A_n=1-\mathbf1_{\{H_n=0\}}\), the asserted covariance follows. Finally
\[
\begin{aligned}
\operatorname{Cov}(L_n,A_n)
&=\Pr(A_n=1)\bigl(\mathbb E[L_n\mid A_n=1]-\mu_n\bigr),\\
-\operatorname{Cov}(L_n,A_n)
&=\Pr(A_n=0)\bigl(\mathbb E[L_n\mid A_n=0]-\mu_n\bigr).
\end{aligned}
\]
Use \(\Pr(A_n=0)\to e^{-\lambda}\) to obtain both conditional mean expansions. This proves the theorem.

## Verification

A separate exact finite-occupancy computation is provided in `verify.py`. Define \(D(b,s;k)\) as the number of functions assigning \(s\) labeled balls to \(b\) labeled bins with every bin load below \(k\). With \(D(0,0;k)=1\), \(D(0,s;k)=0\) for positive \(s\), it satisfies
\[
D(b,s;k)=\sum_{j=0}^{\min(k-1,s)}\binom{s}{j}D(b-1,s-j;k).
\]
In particular, for \(m=n-2\), the exact identity
\[
\operatorname{Cov}(L_n,A_n)
=\frac{n\bigl((n-1)^mD(n,m;k)-n^mD(n-1,m;k)\bigr)}{n^{2m}}
\]
can be compared with direct exhaustive enumeration of Prüfer codes. Execute `python3 verify.py` with a standard Python 3 interpreter; it uses only the Python standard library. Exact rational comparisons across small sizes, plus larger exact dynamic-programming cases, provide checks of the combinatorial identities. They are not a substitute for steps 2–4 of the infinite proof.

## Relationship to prior work

Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation* (2011), Section 18.4, Theorem 18.23 and Example 18.24, already gives the critical two-point maximum-degree transition for uniform labeled trees and the associated Poisson count of top-degree vertices. Its Section 20.2 discusses Gaussian fluctuations and covariances of **fixed-degree** counts. Those marginal theorems are not claimed as new. Neither their individual statements nor their ordinary-scale joint limits determine the \(k_n\)-order conditional difference proved here. The proof above supplies its own mixed factorial-moment control at the moving critical degree threshold.

Carr, Goh and Schmutz (1994) studied maximum-degree distributions in labeled trees. The available abstract is consistent with an earlier marginal maximum result; its complete text was not accessible for a decisive historical comparison. The present contribution is specifically the *sharp mixed leaf/critical-maximum selection-bias coefficient*, not an additional proof of a known marginal extreme law.

## Limitations

The result applies to uniform labeled Cayley trees and to subsequences with a finite positive critical rare-hub intensity. It makes no claim for unlabeled trees, nonuniform models, fixed \(k\), intensity tending to zero/infinity, or a full joint local limit theorem for the leaf count. Historical priority remains uncertain where complete older source texts are inaccessible. Finite exact checks establish only finite cases; the asymptotic statement uses the analytic factorial-moment argument.

## References

1. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1, publicly submitted 2 December 2011; especially Section 18.4, Example 18.24 and Section 20.2.
2. R. Carr, W. M. Y. Goh, and E. Schmutz, *The maximum degree in a random tree and related problems*, Random Structures & Algorithms **5** (1994), 13–24, DOI:10.1002/rsa.3240050104. Historical comparison from accessible abstract and reference material; complete article unavailable.
