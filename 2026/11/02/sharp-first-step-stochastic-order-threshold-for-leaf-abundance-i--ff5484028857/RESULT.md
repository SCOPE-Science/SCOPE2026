# Sharp first-step stochastic-order threshold for leaf abundance in fixed-root forests

## Finding

Fix integers \(k\ge2\), \(m\ge2\), and \(n=k+m\). Choose uniformly among the labeled forests on \([n]\) with exactly a prescribed set \(R\) of \(k\) roots, one root in each component, and orient every edge away from its root. Let \(B\) be the total number of edges whose parent is a root, and let \(L\) be the number of **undirected degree-one vertices**, excluding isolated vertices. Then \(1\le B\le m\), and for every \(1\le r\le m\),

\[
L\mid(B=r)\ \stackrel{d}{=}\ U_{k,r}+V_{m,m-r},
\]

where the summands are independent: \(U_{k,r}\) is the number of boxes containing exactly one ball after \(r\) independent uniform throws into \(k\) boxes, and \(V_{m,t}\) is the number of empty boxes after \(t\) independent uniform throws into \(m\) boxes.

The conditional means are **strictly increasing** with root-edge count:
\[
\mathbb E[L\mid B=r]
=m\left(1-\frac1m\right)^{m-r}
+r\left(1-\frac1k\right)^{r-1},
\qquad
\mathbb E[L\mid B=r+1]>\mathbb E[L\mid B=r].
\]

Nevertheless the first two conditional distributions have a sharp stochastic-order boundary:
\[
L\mid(B=1)\ \le_{\mathrm{st}}\ L\mid(B=2)
\quad\Longleftrightarrow\quad m\le2k.
\]

For \(m>2k\), they are **incomparable in first-order stochastic order**. The failure is already visible at the minimal leaf count:
\[
\Pr(L=2\mid B=1)=\frac{m!}{m^{m-1}},\qquad
\Pr(L=2\mid B=2)=\frac{m!}{2k\,m^{m-2}},
\]
so the latter mass is larger precisely when \(m>2k\), even though its mean is greater.

A second, distinct obstruction occurs whenever \(2\le k\le m-2\): the distributions at \(B=k\) and \(B=k+1\) are incomparable, since
\[
\Pr(L=n-1\mid B=k)=\frac{k!}{k^k}m^{1-(m-k)}>0,
\qquad \Pr(L=n-1\mid B=k+1)=0,
\]
while the mean strictly increases. No complete characterization of the remaining adjacent pairs is asserted.

## Assumptions and scope

All vertices are distinctly labeled. The set \(R\subset[n]\) of roots is fixed in advance and has size \(k\), so every sampled forest has precisely \(k\) components. An isolated root has undirected degree zero and does not count as a leaf. A nonroot vertex is a leaf exactly when its outdegree is zero; a root is a leaf exactly when its outdegree is one. The conditional event \(B=r\) has positive probability for every integer \(r\in[1,m]\). Only the fixed-root uniform model is covered; changing the root-set distribution or the meaning of leaf can change the conclusions.

## Proof

**1. Fixed-root outdegree representation.** The classical forest-volume identity, for \(S=[n]\) and a fixed root set \(R\), is
\[
\sum_{F:\operatorname{roots}(F)=R}\prod_{v\in S}x_v^{c_v(F)}
=\left(\sum_{v\in R}x_v\right)
 \left(\sum_{v\in S}x_v\right)^{m-1},
\]
where \(c_v(F)\) is the number of children of vertex \(v\). In particular, there are \(k n^{m-1}\) such forests. Comparing coefficients shows that the entire outdegree vector of a uniformly chosen forest is distributed as the occupancy vector of \(m-1\) independent uniform labels in \([n]\), plus one extra independent uniform label in \(R\). This is an equality of distributions, not a claim that arbitrary parent assignments always make forests.

Let \(B\) count all labels in \(R\) in this code, including the distinguished extra root label. Therefore \(B=1+\operatorname{Bin}(m-1,k/n)\). Conditional on \(B=r\), the \(r\) labels landing in \(R\) are iid uniform over \(R\), the other \(m-r\) labels are iid uniform over the \(m\) nonroots, and these two label collections are independent. Root vertices of undirected degree one are precisely singleton-occupancy root boxes, while nonroot leaves are precisely empty nonroot boxes. This proves the distributional identity.

**2. Strict conditional-mean increase.** Put \(q=1-1/m\) and \(a=1-1/k\). Standard indicator counting for empty and singleton occupancy gives the mean formula. Its adjacent difference is
\[
\Delta_r=q^{m-r-1}+a^{r-1}\left(1-\frac{r+1}{k}\right).
\]
For \(r\le k-1\), both terms are nonnegative and the first is positive. If \(r\ge k\), write \(t=r+1-k\ge1\). The magnitude of the negative term is
\[
\frac{t}{k}a^{k+t-2}
=a^{k-1}\frac tk a^{t-1}
\le a^{2(k-1)}\le\frac14.
\]
Indeed, \(t a^{t-1}/k\) is maximized for integer \(t=k-1\) or \(t=k\), with value \(a^{k-1}\), and \(a^{k-1}\le1/2\) for \(k\ge2\). Meanwhile \(q^{m-r-1}\ge q^{m-2}>e^{-1}>1/4\). Hence \(\Delta_r>0\) for every adjacent pair.

**3. Exact first-step stochastic comparison.** Let \(Z=V_{m,m-2}\), necessarily \(Z\ge2\). Construct the occupancy experiment for \(V_{m,m-1}\) by throwing one additional nonroot ball. If \(J\) indicates that it lands in an empty box, then \(\Pr(J=1\mid Z=z)=z/m\) and \(V_{m,m-1}=Z-J\). Thus \(L\mid(B=1)\) has law \(Z+1-J\). On the other hand \(L\mid(B=2)\) has law \(Z+W\), where \(W=0\) with probability \(1/k\) and \(W=2\) otherwise, independently of \(Z\).

If \(m\le2k\), then \(z/m\ge2/m\ge1/k\) for every possible \(z\). Couple \(W\) and \(J\), conditional on \(Z=z\), so that the event \(W=0\) is contained in \(J=1\) and has conditional probability \(1/k\). This retains the stated conditional laws and makes \(Z+W\ge Z+1-J\) pointwise. Therefore the asserted stochastic domination holds.

Conversely, the minimum possible leaf count in either conditional law is two. At \(B=1\), obtaining two leaves requires the \(m-1\) nonroot balls to land in distinct boxes. At \(B=2\), it requires the two root balls to coincide and the \(m-2\) nonroot balls to land in distinct boxes. Their respective probabilities are the two displayed factorial fractions, whose ratio is \(m/(2k)\). If \(m>2k\), the second law has more probability at its minimum, contradicting stochastic domination in the increasing direction. The strict mean inequality from step 2 excludes stochastic domination in the reverse direction. Hence the claimed equivalence and incomparability.

**4. Saturation obstruction.** Suppose \(2\le k\le m-2\). At \(B=k\), all \(k\) root balls can occupy distinct roots and the remaining \(m-k\ge2\) nonroot balls can occupy one nonroot. Exactly \(n-1\) vertices then have degree one, with the positive probability displayed above. At \(B=k+1\), at most \(k-1\) roots have degree one, and because \(m-k-1\ge1\) nonroot balls remain, at most \(m-1\) nonroots are leaves. Thus \(L\le n-2\) surely. The strict conditional-mean increase again excludes the opposite stochastic order.

## Verification

The standalone \(\texttt{verify.py}\) enumerates all parent functions with specified roots through eight labeled vertices, rejects cycles, and independently counts forests by root-edge number and undirected degree-one vertices. It compares those exact empirical fractions with a separate occupancy recurrence, and checks the exact first-step ordering threshold, strict mean monotonicity, and saturation obstruction for additional parameter pairs. Executing \(\texttt{python verify.py}\) produced \(\texttt{PASS: 2975 exact assertions}\). The finite computation checks instances and the modeling correspondence; the universal result relies on the preceding proof.

## Relationship to prior work

Pitman's forest-volume identity and fixed-root conditional forest law provide the established coefficient formula used in step 1, and are **not** claimed as new. Classical occupancy formulas similarly underlie the empty- and singleton-cell variables. The additional assertions assessed here are the all-size strict conditional-mean increase for undirected leaf counts, the exact first-step stochastic-order threshold \(m=2k\), and the saturation-based failure despite increasing means. They compare the *distributions*, not merely the availability of an enumerator. No source inspected in this study states or directly proves those cross-parameter comparisons, although older implicit coverage remains possible.

## Limitations

The stochastic-order equivalence applies only to \(B=1\) versus \(B=2\). The second failure mechanism is proved only for \(2\le k\le m-2\); no claim is made that these are the only failing adjacent pairs. This result does not apply to unrooted forests sampled without a fixed root set, does not count isolated roots as leaves, and establishes neither independence nor a general comparison for variance or entropy. Historical implicit coverage cannot be excluded by database searches alone. Independent external validation has not been performed.

## References

1. J. Pitman, *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, Séminaire Lotharingien de Combinatoire 46 (2001), Article B46h, especially forest-volume formula (5), coefficient formula (6), and Section 3.2. https://www.mat.univie.ac.at/~slc/s/s46pitman.pdf ; institutional report 593 (June 1, 2001): https://statistics.berkeley.edu/tech-reports/593.
2. J. Pitman, *Coalescent random forests*, University of California, Berkeley Technical Report 457 (September 1, 1996), later Annales de l'Institut Henri Poincaré, Probability and Statistics 34 (1998), 339–383. https://statistics.berkeley.edu/tech-reports/457.
