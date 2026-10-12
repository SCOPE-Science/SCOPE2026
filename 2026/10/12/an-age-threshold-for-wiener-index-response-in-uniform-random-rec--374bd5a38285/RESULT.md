# An age threshold for Wiener-index response in uniform random recursive trees

## Finding

Let \(T_n\) be a uniform random recursive tree on the vertex set \(\{1,\ldots,n\}\), where each vertex \(i\ge2\) independently selects its parent \(P_i\) uniformly from \(\{1,\ldots,i-1\}\). Let \(W_n=\sum_{1\le a<b\le n}d_{T_n}(a,b)\) be the Wiener index. Define \(H_m=\sum_{j=1}^{m}1/j\), with \(H_0=0\), and \(w_n=n(n+1)H_n-2n^2\).

**Theorem.** For every triple of integers \(n\ge i\ge2\) and \(1\le v<i\),
\[
\mathbb E[W_n\mid P_i=v]-w_n
=\frac{n(n+1)}{i(i+1)}
\left[(i-1)\left(H_{v-1}+1+\frac2v\right)-(i+1)H_{i-1}\right]. \tag{1}
\]
For \(i=2,3\), the right side vanishes for every admissible \(v\). For each \(i\ge4\), it is negative at \(v=1,2\), strictly increases with \(v\) thereafter, and is positive at \(v=i-1\). Writing \(\tau_i\) for the least \(v\in\{2,\ldots,i-1\}\) for which the right side of (1) is nonnegative, the threshold obeys
\[
\boxed{\displaystyle\lim_{i\to\infty}\frac{\tau_i}{i}=e^{-1}}. \tag{2}
\]
The threshold is the first nonnegative index; equality at that index is possible and is not excluded.

Let \(K_n=\deg_{T_n}(1)=\sum_{i=2}^n\mathbf1\{P_i=1\}\) be the number of children of the root, and let \(H_m^{(2)}=\sum_{j=1}^m1/j^2\). Then
\[
\boxed{\operatorname{Cov}(K_n,W_n)=n(n+1)\left[\frac32-\frac3{n+1}-H_{n-1}^{(2)}+\frac{H_{n-1}}n\right]}. \tag{3}
\]
This covariance is zero for \(n=2,3\), strictly negative for every integer \(n\ge4\), and
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,W_n)}{n^2}=\frac32-\frac{\pi^2}{6}<0}. \tag{4}
\]

## Assumptions and scope

The sample space consists of the \((n-1)!\) increasing, rooted, labelled trees, each equally likely. Equivalently, all choices \(P_i\) are independent, with \(P_i\) uniform among the earlier labels. Distances use unit edge lengths. No statement is made about uniform Cayley trees, preferential attachment, or nonuniform parent choices. The results are exact for every indicated finite integer; the limits concern the same model as the size grows.

## Proof

**1. Wiener mean.** If a tree on \(m\) vertices receives a new leaf at a vertex \(U\), and \(S_u(T_m)=\sum_{a=1}^m d_{T_m}(u,a)\), then
\[
W_{m+1}=W_m+m+S_U(T_m).
\]
Because \(U\) is uniform among all existing vertices and \(\sum_u S_u=2W_m\),
\[
\mathbb E[W_{m+1}\mid T_m]=(1+2/m)W_m+m.
\]
Starting with \(W_1=0\), substitution shows \(\mathbb E W_m=w_m=m(m+1)H_m-2m^2\) for every \(m\ge1\), using \(H_{m+1}=H_m+1/(m+1)\).

**2. Expected distances from a vertex of prescribed age.** For \(m\ge v\), let \(s_v(m)=\mathbb E[S_v(T_m)]\). For \(v\ge2\), at its birth, vertex \(v\) attaches to a uniform earlier vertex and therefore
\[
s_v(v)=v-1+\frac{2w_{v-1}}{v-1}=2vH_{v-1}-3(v-1).
\]
The same formula gives \(s_1(1)=0\) when read at \(v=1\). Each later leaf has expected distance \(1+s_v(m)/m\) from vertex \(v\); consequently
\[
s_v(m+1)=(1+1/m)s_v(m)+1.
\]
Dividing by \(m+1\) and telescoping yields, for all \(m\ge v\ge1\),
\[
s_v(m)=m\left(H_m+H_{v-1}-3+\frac2v\right). \tag{5}
\]
The expression for \(v=1\) also follows directly from the initial condition.

**3. Response to the parent choice at time \(i\).** The law of \(T_{i-1}\) does not depend on \(P_i\). By the leaf-addition formula and (5), the conditional excess Wiener mean at time \(i\), compared with the unconditional mean, is exactly
\[
\delta_{i,v}=s_v(i-1)-\frac{2w_{i-1}}{i-1}
=(i-1)\left(H_{v-1}+1+\frac2v\right)-(i+1)H_{i-1}.
\]
Every subsequent independent uniform attachment multiplies the already-established mean difference by \(1+2/m\) at transition \(m\to m+1\). Thus the difference at time \(n\) is
\[
\delta_{i,v}\prod_{m=i}^{n-1}(1+2/m)
=\delta_{i,v}\frac{n(n+1)}{i(i+1)},
\]
which proves (1), including the empty product for \(n=i\).

**4. Sharp age transition.** Let \(g(v)=H_{v-1}+1+2/v\). Directly, \(g(1)=g(2)=3\), and
\[
g(v+1)-g(v)=\frac{v-1}{v(v+1)}>0\qquad(v\ge2).
\]
For \(i=3\), \(3(i-1)-(i+1)H_{i-1}=0\). Its increment on replacing \(i\) by \(i+1\) is
\[
2-H_{i-1}-\frac2i<0\qquad(i\ge3).
\]
Thus the response at \(v=1,2\) is strictly negative for \(i\ge4\). The responses average to zero over the \(i-1\) equiprobable parents (law of total expectation); monotonicity then forces the last response to be strictly positive. These facts establish the indicated threshold and the signs without a sign assumption at its crossing point.

For every fixed \(a\in(0,1)\), take \(v_i=\lfloor ai\rfloor\). Harmonic-sum asymptotics imply
\[
g(v_i)-\frac{i+1}{i-1}H_{i-1}\longrightarrow 1+\log a.
\]
This limit changes sign precisely at \(a=e^{-1}\); monotonicity pins \(\tau_i/i\) between any two positive constants on opposite sides of \(e^{-1}\), proving (2).

**5. Exact root-degree covariance.** Parent choices are mutually independent and \(K_n=\sum_{i=2}^n\mathbf1\{P_i=1\}\), so linearity of covariance and (1) give
\[
\operatorname{Cov}(K_n,W_n)
=n(n+1)\sum_{i=2}^n
\left[\frac3{i(i+1)}-\frac{H_{i-1}}{i(i-1)}\right].
\]
Use the telescoping identities
\[
\sum_{i=2}^n\frac3{i(i+1)}=\frac32-\frac3{n+1},\qquad
\sum_{i=2}^n\frac{H_{i-1}}{i(i-1)}=H_{n-1}^{(2)}-\frac{H_{n-1}}n.
\]
This proves (3). Every summand from \(i\ge4\) in its unsimplified parent-response expression is strictly negative, while the terms for \(i=2,3\) vanish. Hence the asserted signs follow. Finally \(H_{n-1}^{(2)}\to\pi^2/6\) and \(H_{n-1}/n\to0\), proving (4).

## Verification

The independent, standard-library-only program `verify.py` exhaustively enumerates all \(46{,}233\) recursive trees at orders \(2\) through \(9\), directly computes graph distances, and confirms \(120\) distinct conditional parent-age identities and all \(8\) covariance formulas across those orders. It also checks \(3{,}689\) exact rational mean and averaging identities over larger parameter ranges. Numerical threshold values for \(i=100,1000,10000\) are supplied as illustrations and not as proof of the infinite limit. Run with `python3 verify.py`.

## Relationship to prior work

Neininger (2002) gives the Wiener mean and limiting variance and covariance with **internal path length** for uniform random recursive trees. The mean \(w_n\) is an input here, though it is also rederived above. Grübel and Michailow (2014/2015) give almost-sure limit theory for recursive-tree Wiener and path-length functionals. Holmgren and Janson (2014) develop fringe-tree and degree statistics. The claim here instead resolves the mixed **specific-parent-choice/Wiener** regression, its \(e^{-1}\) change-of-sign threshold, and the exact root-degree/Wiener covariance. These mixed statements are not consequences of the displayed marginal Wiener mean, Wiener/path-length covariance, or the separate degree marginals.

## Limitations

This is an exact expectation and covariance statement, not a conditional distribution or a central limit theorem. The sign transition is about conditional *means*: modifying a parent in a particular tree need not move the Wiener index in the corresponding direction. The finite checker corroborates but does not certify the infinite assertions; those follow from the analytic proof. The literature comparison is not a guarantee of historical uniqueness. Earlier distance-distribution and joint-enumerator literature, particularly Dobrow (1996), may contain an indirectly equivalent identity; its complete text was not available for comparison.

## References

1. R. Neininger, “The Wiener Index of Random Trees,” *Combinatorics, Probability and Computing* **11** (2002), 587–597. DOI: `10.1017/S0963548302005321` (first published online 2002-11-21).
2. R. Grübel and I. Michailow, “Random recursive trees: A boundary theory approach,” arXiv:`1406.7614v1` (2014-06-30); *Electronic Journal of Probability* **20** (2015), paper 37. Primary classification 60C05.
3. C. Holmgren and S. Janson, “Limit laws for functions of fringe trees for binary search trees and recursive trees,” arXiv:`1406.6883v1` (2014-06-26).
4. R. P. Dobrow, “On the distribution of distances in recursive trees,” *Journal of Applied Probability* **33** (1996), 749–757. DOI: `10.2307/3215356` (abstract and bibliographic comparison; full text not inspected).
