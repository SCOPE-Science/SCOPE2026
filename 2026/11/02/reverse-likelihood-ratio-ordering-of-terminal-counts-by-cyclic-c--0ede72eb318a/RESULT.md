# Reverse likelihood-ratio ordering of terminal counts by cyclic-core size in uniform random mappings

## Finding

For every integer \(n\ge 2\), sample a function \(F:[n]\to[n]\) uniformly from the \(n^n\) self-maps. Let \(C\) be the number of vertices lying on a directed cycle of the functional digraph, and let \(Z\) be its number of vertices of indegree zero. Write \(p_{n,m}(z)=\Pr(Z=z\mid C=m)\). Then for every \(1\le m_1<m_2\le n\),
\[
p_{n,m_1}(z_1)p_{n,m_2}(z_2)
\le p_{n,m_1}(z_2)p_{n,m_2}(z_1)
\quad\text{whenever }z_1<z_2.
\]
Thus the conditional kernel is reverse totally positive of order two. Equivalently,
\[
Z\mid(C=m_2)\ \le_{\mathrm{lr}}\ Z\mid(C=m_1).
\]
The orders are strict in the stochastic sense for different feasible cyclic-core sizes: for each \(m_1<m_2\), at least one upper-tail probability is strictly larger under \(m_1\); all upper-tail probabilities are no smaller. In particular, if \(g\) and \(h\) are nondecreasing real functions on their respective finite domains, then
\[
\operatorname{Cov}(g(C),h(Z))\le0,
\]
strictly so if both functions are strictly increasing.

The exact, nondegenerate conditional law is also expressed by the \(r\)-Stirling numbers of the second kind:
\[
p_{n,m}(z)=\frac{(n-m)!}{z!\,n^{n-m-1}}
S_m(n-1,n-z),\quad 1\le m<n,\quad1\le z\le n-m.
\]
Here \(S_r(N,q)\) counts partitions of \([N]\) into \(q\) nonempty blocks with its first \(r\) elements in mutually distinct blocks. At \(m=n\) the law is the point mass at \(z=0\), and outside the displayed support the probability is zero.

## Assumptions and scope

The map images \(F(1),\ldots,F(n)\) are independent uniform elements of \([n]\); loops and cycles of every length are permitted. Each connected component has one directed cycle. The integer \(C\) is between \(1\) and \(n\); for \(C=m<n\), the integer \(Z\) is between \(1\) and \(n-m\). All probabilities are finite, exact and conditional on positive-probability events. The likelihood-ratio order is defined by its cross-product inequalities above, which remain meaningful when supports contain zeros.

## Proof

**1. Conditional forest encoding.** Fix the set of \(m\) cyclic vertices. The map restricted to these vertices is a permutation. Every other vertex belongs to a tree directed toward one of those roots; conditional on the cyclic set, the forest is uniform among labeled forests with these specified roots. Put \(t=n-m\ge1\). A generalized leaf-deletion/Prüfer code represents each such forest uniquely by \(t-1\) symbols of \([n]\), followed by one symbol from the set of \(m\) roots. All \(m n^{t-1}\) codes are equally frequent. The final symbol is a root, so the \(t\) noncyclic indegrees equal the occurrence counts of their labels among the \(t-1\) unrestricted symbols. Accordingly \(Z\) has the law of the number of absent labels among \(t\) designated labels in \(t-1\) independent uniform draws from \([n]\).

For exactly \(z\) absent designated labels, choose them in \(\binom tz\) ways. Of the remaining \(t-z\) designated labels every one must occur; the \(m\) root labels may occur arbitrarily. Adjoin \(m\) distinguished dummy elements, placing one in each labeled root box. The resulting partition has \(n-1=m+t-1\) elements and \(n-z=m+t-z\) nonempty blocks, with all distinguished elements in separate blocks. There are \(S_m(n-1,n-z)(t-z)!\) assignments to the actual boxes. Hence the number of allowed length-\(t-1\) code words is
\[
\binom tz(t-z)!S_m(n-1,n-z)=\frac{t!}{z!}S_m(n-1,n-z).
\]
Division by \(n^{t-1}\) proves the exact conditional law. For \(t=0\), the map is a permutation, so \(Z=0\).

**2. Log-concavity of each fixed-distinguished-element Stirling row.** For fixed \(r\ge1\), the recurrence
\[
S_r(N+1,q)=q S_r(N,q)+S_r(N,q-1)
\]
and the initial value \(S_r(r,r)=1\) give
\[
B_{N+1,r}(x)=(x+r)B_{N,r}(x)+xB'_{N,r}(x),
\qquad B_{N,r}(x)=\sum_{q=r}^{N}S_r(N,q)x^{q-r}.
\]
Every \(B_{N,r}\) has only simple negative zeros (unless it is constant). Indeed, if \(B\) has simple roots \(a_1<\cdots<a_d<0\), at such a root the transformed polynomial \((x+r)B+xB'\) equals \(a_iB'(a_i)\). Its signs alternate at consecutive roots, its sign at \(0\) is positive, and its sign toward negative infinity is opposite to that at \(a_1\). Consequently it has one root in each of the \(d+1\) intervals \(( -\infty,a_1),(a_1,a_2),\ldots,(a_d,0)\), exhausting its degree. The constant case starts with the root \(-r\). By Newton's inequalities, \(q\mapsto S_r(N,q)\) is log-concave on its contiguous positive support. In particular the ratios \(S_r(N,q-1)/S_r(N,q)\) are nondecreasing in \(q\).

**3. The cross-parameter comparison.** It suffices to compare adjacent \(m-1\) and \(m\), where \(2\le m\le n-1\). Set \(N=n-1\), \(q=n-z\), and \(a_q=S_{m-1}(N-1,q)\). Deleting the \(m\)-th distinguished element from a partition that violates its separation condition shows
\[
S_m(N,q)=S_{m-1}(N,q)-(m-1)a_q.
\]
The ordinary Stirling recurrence gives \(S_{m-1}(N,q)=q a_q+a_{q-1}\). Whenever \(m\le q\le N-1\), these identities imply
\[
\frac{S_m(N,q)}{S_{m-1}(N,q)}
=1-\frac{m-1}{q+a_{q-1}/a_q}.
\]
The denominator is **strictly increasing** in \(q\): the first term increases, and the second is nondecreasing by step 2. Thus this ratio is strictly increasing in \(q\). At \(q=N\), both Stirling numbers equal \(1\), so the ratio equals \(1\), still larger than its earlier values. If \(m=N\), there is only one common support point and no interior comparison is needed.

For any \(z\) in the common positive support, step 1 yields
\[
\frac{p_{n,m-1}(z)}{p_{n,m}(z)}
=\frac{n-m+1}{n}\frac{S_{m-1}(N,n-z)}{S_m(N,n-z)}.
\]
Since \(q=n-z\) decreases with \(z\), the right-hand side is strictly increasing in \(z\) whenever at least two common positive support points exist. The extra highest \(z=n-m+1\) occurs only for \(m-1\), strengthening the comparison. Therefore \(p_{n,m-1}\) dominates \(p_{n,m}\) in likelihood-ratio order. The final adjacent comparison \(m=n-1\) versus \(m=n\) compares point masses at \(1\) and \(0\). Transitivity gives the stated order for every pair \(m_1<m_2\) and all cross-products, including zeros.

**4. Covariance consequence.** Likelihood-ratio order implies first-order stochastic order, so \(m\mapsto\mathbb E[h(Z)\mid C=m]\) is nonincreasing for every nondecreasing \(h\). The covariance identity using an independent copy \(C'\),
\[
2\operatorname{Cov}(g(C),h(Z))
=\mathbb E\!\left[(g(C)-g(C'))
(\mathbb E[h(Z)\mid C]-\mathbb E[h(Z)\mid C'])\right],
\]
is nonpositive for nondecreasing \(g\). Strictness for strictly increasing \(g,h\) follows because distinct conditional laws have strict stochastic dominance at some threshold and every feasible \(C\) value has positive probability.

## Verification

The standalone file `VERIFY.py` executes using only the Python standard library. It checks the \(r\)-Stirling recurrence, its deletion identity, the exact code-word formula against independent inclusion-exclusion, and log-concavity. It checks adjacent reverse two-by-two minors through \(n=38\) and all separated minors through \(n=17\). It also independently enumerates every self-map through \(n=6\) and compares the joint \((C,Z)\) counts against the formula. On execution the verifier completed 114389 exact integer assertions. The infinite theorem is proved by the arguments above; these finite checks are not substitutes for the proof.

## Relationship to prior work

Hansen and Jaworski study cyclic points and component-size distributions in random mappings and show how fixed cyclic sets produce rooted forests. Pitman develops multinomial and deletion constructions for labeled rooted forests. Broder introduced \(r\)-Stirling numbers, and Maamra–Mihoubi prove the log-concavity of a more general Stirling family. These are prior foundations, not new claims. An earlier exact conditional law for \((C,Z)\) gives the relevant count distribution and a decreasing conditional mean but does not establish the present likelihood-ratio ordering. The comparison here proves a cross-row inequality for all event thresholds, not merely a formula for the rows or an inequality for the mean.

## Limitations

The theorem is for independent *uniform* map images; no heterogeneous image-probability or biased-mapping extension is claimed. Strictness applies to nontrivial order comparisons, not to every matrix minor, because structural zeros and one-point supports force equality in some minors. Historical coverage by broader total-positivity results or older random-mapping literature cannot be excluded conclusively. Only the stated finite model and algebraic ordering have been proved. No external independent audit has been performed.

## References

1. J. C. Hansen and J. Jaworski, *A new random mapping model*, first arXiv posting 2006-03-22, arXiv:math/0603529, https://arxiv.org/abs/math/0603529.
2. J. Pitman, *The multinomial distribution on rooted labeled forests*, Statistics Technical Report 499 (1998), https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/499.pdf.
3. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/.
4. A. Z. Broder, *The \(r\)-Stirling numbers*, Discrete Mathematics 49 (1984), 241–259, https://doi.org/10.1016/0012-365X(84)90161-4.
5. M. S. Maamra and M. Mihoubi, *The \((r_1,\ldots,r_p)\)-Bell polynomials*, first arXiv posting 2012-12-13, arXiv:1212.3191, https://arxiv.org/abs/1212.3191.
