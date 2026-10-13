# Negative plateau–nesting covariance in uniform Stirling permutations

## Finding
Let \(\sigma\) be a uniformly random Stirling permutation of order \(n\). Denote by \(P_n\) its number of adjacent equal pairs (plateaux) and by \(D_n\) the total number of entries strictly inside all doubled labels. Then for every integer \(n\ge1\),
\[
\operatorname{Cov}(P_n,D_n)
=\frac{2\cdot4^n}{3\binom{2n}{n}}-\frac{8n+4}{9}.
\]
In particular, \(\operatorname{Cov}(P_1,D_1)=0\), and \(\operatorname{Cov}(P_n,D_n)<0\) for every \(n\ge2\). Moreover,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(P_n,D_n)}n=-\frac89.
\]
The equivalent tree formulation is \(\operatorname{Cov}(L_n,H_n)=\frac{4^n}{3\binom{2n}{n}}-\frac{4n+2}{9}\), where \(L_n\) is leaf count and \(H_n\) is the sum of depths of the \(n\) nonroot vertices in a uniform plane-oriented recursive tree with root \(0\) and other vertices labelled \(1,\ldots,n\).

## Assumptions and scope
A Stirling permutation is a word \(\sigma=(\sigma_1,\ldots,\sigma_{2n})\) containing two copies of each label in \(\{1,\ldots,n\}\), such that entries between the two copies of a label \(j\) are all larger than \(j\). Choose the word uniformly among its \((2n-1)!!\) possibilities. Put
\[
P_n=\sum_{i=1}^{2n-1}\mathbf1\{\sigma_i=\sigma_{i+1}\},\qquad
D_n=\sum_{j=1}^n\bigl(\operatorname{pos}_2(j)-\operatorname{pos}_1(j)-1\bigr),
\]
where \(\operatorname{pos}_1(j)<\operatorname{pos}_2(j)\) are the indices of label \(j\). Endpoint padding with zeros, sometimes used to define ascents and descents, does not alter the plateau count. All expressions are exact, not asymptotic, for every positive integer \(n\).

## Proof
**Tree correspondence and path length.** In the established depth-first contour bijection [1], each label represents the two traversals of its edge in a rooted ordered increasing tree. The tree has a root labelled \(0\), the other vertices labelled \(1,\ldots,n\), and vertex labels increase along root-to-leaf paths. A label \(j\) forms a plateau precisely when its vertex has no children. The number of entries strictly inside the two appearances of \(j\) equals twice the number of strict descendants of that vertex. Writing \(L_n\) for leaf count and \(H_n=\sum_{v=1}^n\operatorname{depth}(v)\) for total path length, we have, deterministically,
\[
P_n=L_n,\qquad D_n=2(H_n-n).
\]
Indeed, the total number of ancestor-descendant pairs with nonroot ancestor is \(\sum_{v=1}^n(\operatorname{depth}(v)-1)=H_n-n\).

**Uniform insertion and conditional moments.** A tree with \(n\) nonroot vertices has exactly \(2n+1\) available ordered child positions: a vertex of outdegree \(d\) has \(d+1\) positions. Inserting the next labelled vertex uniformly among these positions gives the uniform tree distribution at every size [1]. For a particular tree let \(H=H_n\), \(L=L_n\), and \(W=\sum_{v\text{ leaf}}\operatorname{depth}(v)\). Let \(d\) be the depth of the randomly chosen insertion parent, and \(B\) the indicator that this parent is a leaf. Then
\[
H_{n+1}=H+d+1,\quad L_{n+1}=L+1-B,\quad W_{n+1}=W+d+1-Bd.
\]
Since a vertex at depth \(d(v)\) contributes \(\deg^+(v)+1\) slots,
\[
\sum_{\text{slots}}\bigl(d+1\bigr)=2H+n+1,\quad
\sum_{\text{slots}}B=L,\quad
\sum_{\text{slots}}Bd=W.
\]
(The first identity uses \(\sum_v\deg^+(v)d(v)=H-n\).) Thus, with \(q=2n+1\),
\[
\begin{aligned}
\mathbb E[H_{n+1}\mid T_n]&=H+(2H+n+1)/q,\\
\mathbb E[L_{n+1}\mid T_n]&=L+1-L/q,\\
\mathbb E[W_{n+1}\mid T_n]&=W+(2H+n+1-W)/q,\\
\mathbb E[L_{n+1}H_{n+1}\mid T_n]&=\frac{(q+1)LH+nL+(q+2)H+n+1-W}{q}.
\end{aligned}
\]

**Closure of the mixed-moment recurrence.** Initially, at \(n=1\), the single edge tree has \(H_1=L_1=W_1=1\). The conditional equations show inductively that
\[
\mathbb E[L_n]=\frac{2n+1}{3},\qquad
\mathbb E[W_n]=\frac23\mathbb E[H_n]+\frac{n+2}{9}.
\]
For the second identity, substitute the displayed expression for \(\mathbb E[W_n]\) and the conditional recurrence for \(\mathbb E[H_{n+1}]\) into that for \(\mathbb E[W_{n+1}]\); both sides agree and have the same initial value. Substitute both mean identities into the preceding mixed-moment equation, and subtract the product of the two updated means. Writing \(c_n=\operatorname{Cov}(L_n,H_n)\) gives the closed recurrence
\[
c_1=0,\qquad c_{n+1}=\frac{2n+2}{2n+1}c_n-\frac29.
\]
A direct substitution verifies its unique solution
\[
c_n=\frac13\frac{(2n)!!}{(2n-1)!!}-\frac{4n+2}{9}
=\frac{4^n}{3\binom{2n}{n}}-\frac{4n+2}{9}.
\]
Finally \(D_n=2(H_n-n)\) multiplies this covariance by two, proving the announced formula. The recurrence starts at zero and subtracts \(2/9\) at every subsequent step while multiplying the previous negative term by a strictly positive factor, so its value is strictly negative for every \(n\ge2\). By the central-binomial estimate \(4^n/\binom{2n}{n}\sim\sqrt{\pi n}\), division by \(n\) yields the stated limit.

## Verification
The self-contained Python 3 standard-library file `verify.py` enumerates every Stirling permutation through order \(7\), independently decodes each word as a depth-first traversal of the increasing plane tree, checks \(P_n=L_n\) and \(D_n=2(H_n-n)\), checks all conditional insertion identities for every tree through order \(5\), and computes exact-rational mixed moments through order \(7\). It also checks the closed expression and strict finite sign through order \(1000\). Run `python3 verify.py` from the directory containing this file. Finite enumeration corroborates but does not replace the preceding proof for all orders.

## Relationship to prior work
Janson [1] establishes the uniform tree--Stirling-permutation contour correspondence, the identification of plateaux with leaves, and the marginal leaf distribution; it also relates each single-label spacing to a subtree size. Janson, Kuba and Panholzer [2] extend the correspondence and study joint local ascent/descent/plateau statistics. Kuba and Panholzer [3] give exact distributions for **individual** repeated-label spacings and for counts of blocks of specified sizes; those are not the sum of all spacings jointly with plateau count. Lundblad and Wagner [4] analyze normalized total/leaf path lengths in increasing trees and introduce a multivariate generating-function equation encoding leaves and path lengths; their asymptotic comparison does not provide the finite covariance formula or strict negativity here. Their exact generating-function framework may support an alternative derivation, which is a priority risk. The present statement does not claim to originate the bijection, marginal plateau law, individual spacing law, or generic generating-function framework.

## Limitations
This theorem concerns uniform ordinary (two-copy) Stirling permutations and the specified pair of aggregate statistics only. It does not establish a full bivariate distribution, a non-Gaussian joint limit, covariance for higher-copy generalizations, or historical priority against every implicit extraction from general multivariate generating functions. The documentary comparison supports the explicitly evaluated covariance and its strict sign, not a claim that no earlier work could derive them. Independent external validation has not been performed.

## References
[1] S. Janson, *Plane recursive trees, Stirling permutations and an urn model*, arXiv:0803.1129v1 (public submission 7 March 2008), https://arxiv.org/pdf/0803.1129 ; relevant pp. 1–5.

[2] S. Janson, M. Kuba and A. Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, arXiv:0805.4084 (2008), https://arxiv.org/pdf/0805.4084 ; relevant introduction, bijections and joint local-statistics sections.

[3] M. Kuba and A. Panholzer, *Analysis of Statistics for Generalized Stirling Permutations*, author preprint dated 4 June 2010, https://www.dmg.tuwien.ac.at/kuba/preprintStirblock.pdf ; relevant pp. 2–3, 19 and 22–25.

[4] J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, LIPIcs 381, Article 2, DOI:10.4230/LIPIcs.AofA.2026.2, https://drops.dagstuhl.de/storage/00lipics/lipics-vol381-aofa2026/LIPIcs.AofA.2026.2/LIPIcs.AofA.2026.2.pdf ; relevant pp. 1–7 and 12–14.
