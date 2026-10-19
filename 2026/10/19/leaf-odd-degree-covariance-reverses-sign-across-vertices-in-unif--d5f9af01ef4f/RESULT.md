# Leaf–odd-degree covariance reverses sign across vertices in uniform labeled trees

## Finding
For every integer \(n\ge2\), sample a labeled tree \(T_n\) uniformly among all \(n^{n-2}\) labeled trees on \(\{1,\dots,n\}\). Let \(L_n\) be its number of leaves (vertices of degree one) and \(O_n\) its number of vertices whose degrees are odd. Define
\[
 u_n=\left(1-\frac1n\right)^{n-2},\quad
 v_n=\left(1-\frac2n\right)^{n-2},\quad
 w_n=\left(1-\frac3n\right)^{n-2},\quad
 z_n=\left(1-\frac4n\right)^{n-2}.
\]
Here the powers are ordinary integer powers and \(0^0=1\), relevant only for \(n=2\). The exact covariance is
\[
 \boxed{\operatorname{Cov}(L_n,O_n)=\frac n2\left[u_n+(n-1)w_n-nu_nv_n\right].}
\]
It is zero for \(n=2,3\), and strictly positive for every \(n\ge4\). However, for any two distinct vertices \(i\ne j\) and every \(n\ge3\),
\[
 \operatorname{Cov}\left(\mathbf1\{\deg(i)=1\},\mathbf1\{\deg(j)\ \mathrm{odd}\}\right)
 =\frac{w_n-u_nv_n}2<0.
\]
The analogous same-vertex covariance is \(u_n(1-v_n)/2>0\), giving an exact local-negative/global-positive reversal.

For \(n\ge4\), the complete marginal moments are
\[
 \mathbb E[L_n]=nu_n,\qquad \mathbb E[O_n]=\frac n2(1+v_n),
\]
\[
 \operatorname{Var}(L_n)=nu_n+n(n-1)v_n-n^2u_n^2,
\]
\[
 \operatorname{Var}(O_n)=\frac n4[1+(n-1)z_n-nv_n^2].
\]
In particular,
\[
 \lim_{n\to\infty}\frac{\operatorname{Cov}(L_n,O_n)}n
 =\frac{e^2-3}{2e^3}>0,
\qquad
\lim_{n\to\infty}\operatorname{Corr}(L_n,O_n)
=\frac{e^2-3}{e^3\sqrt{(e^{-1}-2e^{-2})(1-5e^{-4})}}
\approx0.7353446771.
\]

## Assumptions and scope
The tree is **uniform over labeled Cayley trees**, not uniform over unlabelled shapes, random recursive trees, or a conditioned Galton–Watson family. Every odd-degree vertex, including each leaf, is included in \(O_n\). In a two-vertex tree both counts equal two. In a three-vertex tree both counts equal two. The covariance claim holds for all integers \(n\ge2\); the strict statement starts at four vertices; the nondegenerate Pearson correlation is defined here only for \(n\ge4\). No claim is made about arbitrary tree distributions.

## Proof
A tree on \(n\) labeled vertices corresponds bijectively to a Prüfer word of length \(N=n-2\). For a uniformly sampled tree this word consists of \(N\) independent uniform symbols from \(\{1,\ldots,n\}\). Write \(C_i\) for the number of occurrences of symbol \(i\); then \(\deg(i)=1+C_i\). Define \(X_i=\mathbf1\{C_i=0\}\) and \(Y_i=\mathbf1\{C_i\ \mathrm{even}\}\), so \(L_n=\sum_i X_i\) and \(O_n=\sum_iY_i\).

A zero-count calculation and a parity transform yield
\[
 \mathbb EX_i=u_n,\quad
 \mathbb E(-1)^{C_i}=v_n,\quad
 \mathbb EY_i=\frac{1+v_n}2.
\]
For \(i\ne j\), independence across positions in the Prüfer word gives
\[
 \mathbb E[X_i(-1)^{C_j}]=\left(1-\frac3n\right)^{n-2}=w_n,
\quad
 \mathbb E[X_iY_j]=\frac{u_n+w_n}2.
\]
Therefore
\[
 \operatorname{Cov}(X_i,Y_j)=\frac{w_n-u_nv_n}2\quad(i\ne j),\qquad
 \operatorname{Cov}(X_i,Y_i)=\frac{u_n(1-v_n)}2.
\]
Summing \(n\) diagonal and \(n(n-1)\) off-diagonal contributions proves the exact formula.

For \(n\ge3\), compare the positive bases \(1-3/n\) and \((1-1/n)(1-2/n)=1-3/n+2/n^2\). With exponent \(n-2>0\), this gives \(w_n<u_nv_n\). At \(n=2,3\), the explicit formula gives zero. For \(n\ge4\), division by \(nu_n/2>0\) reduces positivity to
\[
 1+(n-1)\left(\frac{n-3}{n-1}\right)^{n-2}
 > n\left(\frac{n-2}n\right)^{n-2}.
\]
For fixed \(n\), put \(f_n(x)=x(1-2/x)^{n-2}\) for \(x\in[n-1,n]\). Its derivative is
\[
 f_n'(x)=\left(1-\frac2x\right)^{n-3}\left(1+\frac{2(n-3)}x\right)<1.
\]
Indeed, for \(k=n-3\ge1\) and \(t=2/x\in(0,1)\), the strict Bernoulli inequality \((1-t)^{-k}>1+kt\) implies \((1-t)^k(1+kt)<1\). The mean value theorem gives \(f_n(n)-f_n(n-1)<1\), which is exactly the displayed strict inequality. Thus the covariance is positive for every \(n\ge4\).

For the variances, note that \(\mathbb EX_iX_j=v_n\) for \(i\ne j\), and \(\mathbb E(-1)^{C_i+C_j}=z_n\). Pair summation produces the two stated variance identities. Their limits follow by expanding \((1-a/n)^{n-2}=e^{-a}[1+(2a-a^2/2)/n+O(n^{-2})]\) for each fixed \(a\in\{1,2,3,4\}\). In particular,
\[
 \frac{\operatorname{Var}(L_n)}n\to e^{-1}-2e^{-2},\quad
 \frac{\operatorname{Var}(O_n)}n\to\frac{1-5e^{-4}}4.
\]
Both limits are positive. Combining these limits with the covariance limit proves the asserted correlation limit.

## Verification
Run the accompanying standard-library script \(\texttt{verify.py}\) using \(\texttt{python verify.py}\). It enumerates all \(n^{n-2}\) Prüfer words at every order \(2\le n\le8\) and independently reconstructs the complete pair of means, covariance, and both variances by exact rational arithmetic. It also checks the strict finite-sign statements and numerical limits. Its output is `PASS 489 exact/limit checks` and the correlation approximately `0.7353446771259898`. These finite checks corroborate the complete analytic proof and do not certify all orders by themselves.

## Relationship to prior work
Prüfer's bijection and degree-count multinomial structure are classical. Drmota and Gittenberger (1999) prove joint asymptotic normality and covariance formulas for **finitely many prespecified exact vertex degrees** in random labeled trees; their published Theorem 2.3 contains a degree-class covariance matrix. This supplies strong relevant background but does not itself state the exact all-size leaf-versus-odd-degree sign theorem, since the latter pools all odd degrees and includes the finite-size strict inequality and opposite signs at two scales. Barbour and Gnedin (2008) analyze small-frequency occupancy counts in an infinite model, whereas Bartroff and Goldstein (2012) study normal approximation for single fixed-frequency counts in a uniform multinomial occupancy model. All three provide context for degree/occupancy fluctuations rather than an explicit prior version of this result.

## Limitations
The identity is an exact two-statistic covariance statement, not a joint distribution or a conditional-regression monotonicity theorem. An earlier general degree-profile generating function might imply it after additional summation; the historical priority comparison is therefore provisional. The correlation limit establishes persistence of linear dependence only for the uniform labeled-tree model.

## References
1. Drmota and Gittenberger, The distribution of nodes of given degree in random trees, Journal of Graph Theory 31 (1999), 227–253, DOI 10.1002/(SICI)1097-0118(199907)31:3<227::AID-JGT6>3.0.CO;2-6. The published date is 21 July 1999; a lawful full-text preprint is available from the authors' institutional page at `https://www.dmg.tuwien.ac.at/bgitten/preprints/nodedeg.pdf`.
2. Barbour and Gnedin, Small counts in the infinite occupancy scheme, arXiv:0809.4387 (2008), `https://arxiv.org/abs/0809.4387`.
3. Bartroff and Goldstein, A Berry–Esseen bound for the uniform multinomial occupancy model, arXiv:1202.0909 (2012), `https://arxiv.org/abs/1202.0909`.
