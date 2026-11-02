# Exact root-attachment covariance profile for the Wiener index of random recursive trees

## Finding

For every integer \(n\ge2\), let \(T_n\) be a uniformly random recursive tree on the vertex set \(\{1,\ldots,n\}\): vertex \(j\), independently for each \(j=2,\ldots,n\), chooses one parent uniformly from \(\{1,\ldots,j-1\}\). Let \(D_n\) be the number of children of root \(1\), and let \(W_n\) be the Wiener index, the sum of graph distances over unordered pairs of distinct vertices. Let \(I_j\) be the indicator that vertex \(j\) attaches directly to root \(1\).

Write \(H_m=\sum_{k=1}^m k^{-1}\) and \(H_m^{(2)}=\sum_{k=1}^m k^{-2}\). The complete exact arrival-by-arrival covariance profile is

\[
\operatorname{Cov}(I_j,W_n)
=\frac{n(n+1)}{j(j+1)}
\left(3-\frac{j+1}{j-1}H_{j-1}\right)
\qquad(2\le j\le n).
\]

This covariance is exactly zero for \(j=2,3\) and **strictly negative for every \(4\le j\le n\)**. Consequently the root degree and Wiener index obey the closed finite-size law

\[
\boxed{\operatorname{Cov}(D_n,W_n)=n(n+1)\left(\frac32-H_{n-1}^{(2)}\right)+(n+1)H_{n-1}-3n.}
\]

The covariance is zero for \(n=2,3\), negative for every \(n\ge4\), and satisfies

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(D_n,W_n)}{n^2}
=\frac32-\frac{\pi^2}{6}<0.
\]

## Assumptions and scope

All parent choices are mutually independent and uniform on older vertices; no conditioning on tree shape or degree is imposed. The root child count \(D_n\) is the outdegree of vertex \(1\), not the number of leaves. The Wiener index uses graph distance in the underlying **undirected** tree and counts each unordered pair exactly once. The displayed local identity applies to every pair of integers \(n\ge j\ge2\); the global formula applies to every integer \(n\ge2\). All covariances are under the uniform recursive-tree probability measure.

## Proof

**1. A one-step Wiener recurrence.** For a fixed tree with \(m\ge1\) vertices, adjoining vertex \(m+1\) to parent \(U\) adds

\[
m+\sum_{v=1}^m d(U,v)
\]

to the Wiener index. Since \(U\) is independent and uniform over the existing vertices, and every unordered distance is counted twice when summing over possible parents,

\[
\mathbb E[W_{m+1}\mid T_m]
=\left(1+\frac2m\right)W_m+m.
\tag{1}
\]

Writing \(a_m=\mathbb EW_m\), recurrence (1), \(a_1=0\), and a telescoping sum yield

\[
a_m=m(m+1)H_m-2m^2.
\tag{2}
\]

If \(S_m=\sum_{v=1}^m d(1,v)\) is the total root path length, the expected depth of vertex \(v\) is \(H_{v-1}\) by the independent uniform-parent recursion. Therefore

\[
\mathbb ES_m=\sum_{v=2}^m H_{v-1}=m(H_m-1).
\tag{3}
\]

**2. The influence of one arrival.** Fix \(j\ge2\). All parent choices before time \(j\) are independent of \(I_j\), while \(\mathbb P(I_j=1)=1/(j-1)\). On the event \(I_j=1\), the new vertex attaches to the root, giving an expected Wiener increment \((j-1)+\mathbb ES_{j-1}\). Without conditioning, (1) gives increment \((j-1)+2a_{j-1}/(j-1)\). Hence

\[
\delta_j:=\mathbb E[W_j\mid I_j=1]-\mathbb E W_j
=\mathbb ES_{j-1}-\frac{2a_{j-1}}{j-1}
=3(j-1)-(j+1)H_{j-1},
\tag{4}
\]

using (2)--(3). Subsequent parents remain uniform and independent of the event \(I_j=1\). Applying the same recurrence (1) conditionally, the difference of conditional and unconditional means is multiplied at each later step \(m\to m+1\) by \((m+2)/m\). Consequently

\[
\mathbb E[W_n\mid I_j=1]-\mathbb EW_n
=\delta_j\prod_{m=j}^{n-1}\frac{m+2}{m}
=\delta_j\frac{n(n+1)}{j(j+1)}.
\tag{5}
\]

For any Bernoulli indicator \(I\), \(\operatorname{Cov}(I,Y)=\mathbb P(I=1)(\mathbb E[Y\mid I=1]-\mathbb EY)\). Multiplying (5) by \(1/(j-1)\) proves the claimed local covariance identity.

**3. Strict signs.** Define \(g_j=\frac{j+1}{j-1}H_{j-1}\). Directly \(g_2=g_3=3\). For \(j\ge3\),

\[
g_{j+1}-g_j
=\frac{j+2}{j^2}-\frac{2H_{j-1}}{j(j-1)}
\ge\frac{j-2}{j^2(j-1)}>0,
\tag{6}
\]

since \(H_{j-1}\le1+(j-2)/2=j/2\). Thus \(3-g_j<0\) for every \(j\ge4\), and the two initial coefficients vanish. This also proves the global strict sign for all \(n\ge4\).

**4. Exact summation and asymptotics.** As \(D_n=\sum_{j=2}^n I_j\), covariance linearity and the local formula give

\[
\begin{aligned}
\frac{\operatorname{Cov}(D_n,W_n)}{n(n+1)}
&=3\sum_{j=2}^n\frac1{j(j+1)}
-\sum_{j=2}^n\frac{H_{j-1}}{j(j-1)}\\
&=\frac32-\frac3{n+1}
-H_{n-1}^{(2)}+\frac{H_{n-1}}n.
\end{aligned}
\tag{7}
\]

Indeed \(\sum_{j=2}^n[j(j+1)]^{-1}=1/2-1/(n+1)\), while exchanging the finite sums gives

\[
\sum_{j=2}^n\frac{H_{j-1}}{j(j-1)}
=\sum_{k=1}^{n-1}\frac1k\left(\frac1k-\frac1n\right)
=H_{n-1}^{(2)}-\frac{H_{n-1}}n.
\]

Multiplying (7) by \(n(n+1)\) yields the stated closed formula. Finally \(H_{n-1}^{(2)}\to\pi^2/6\) and \(H_{n-1}=O(\log n)\), which proves the limit.

## Verification

The standalone script `verify.py` independently constructs all recursive trees with \(2\le n\le8\), computes their Wiener indices by breadth-first graph distances, and checks each exact local covariance and the aggregated formula with rational arithmetic. This covers \(5913\) trees and \(28\) arrival-size pairs. It also checks exact rational agreement of the finite sum and closed form for every size from \(2\) through \(150\). Execute `python3 verify.py` using Python's standard library. These finite tests corroborate but do not replace the all-size argument above.

## Relationship to prior work

Neininger, *The Wiener Index of Random Trees* (manuscript dated 2001; published 2002), derives the Wiener-index expectation and a bivariate limit law with **total root path length**; its Theorem 1.2 supplies a check on (2), but the root's child count is a different observable. Grübel and Michailow, *Random Recursive Trees: A Boundary Theory Approach* (first public preprint June 30, 2014), develop almost-sure Wiener/path-length limit theory; their Section 3.3 does not state the arrival-conditioned covariance profile. A separately published exact root-attachment covariance for **total root path length** has a different expression and does not imply the corresponding Wiener covariance without extra second-order subtree information. The present claim is precisely the local root-attachment/Wiener covariance profile, its strict sign threshold, and its summed law; the known mean formula and general recursion are not asserted to be new.

## Limitations

Only uniform recursive trees and their root-attachment indicators are treated. The claim does not establish covariance or stochastic ordering in nonuniform attachment models, nor independence at the zero-covariance indices. Vanishing covariance is weaker than independence. Scholarly and published-record searches cannot establish unique historical priority; unexamined sources could imply this profile by another method.

## References

1. R. Grübel and I. Michailow, *Random Recursive Trees: A Boundary Theory Approach*, arXiv:1406.7614, publicly submitted June 30, 2014. https://arxiv.org/abs/1406.7614
2. R. Neininger, *The Wiener Index of Random Trees*, manuscript September 19, 2001, published in *Combinatorics, Probability and Computing* 11 (2002), 587–597, doi:10.1017/S0963548302005321. Author manuscript: https://www.math.uni-frankfurt.de/~neiningr/w-ind.pdf
3. G. O. Munsonius, *On Tail Bounds for Random Recursive Trees*, *Journal of Applied Probability* 49 (2012), 566–581, doi:10.1239/jap/1339878805 (abstract-level comparison only).
