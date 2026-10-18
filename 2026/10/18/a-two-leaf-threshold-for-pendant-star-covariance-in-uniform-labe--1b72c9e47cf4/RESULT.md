# A two-leaf threshold for pendant-star covariance in uniform labelled trees

## Finding

Let \(T_n\) be uniformly distributed over the \(n^{n-2}\) trees on \([n]\), and let \(L_n\) be its number of degree-one vertices. For integers \(1\le k\le n-3\), define \(S_{n,k}\) to be the number of vertices having degree exactly \(k+1\), exactly \(k\) leaf neighbours, and one remaining (necessarily nonleaf) neighbour. These are pendant \(k\)-star centres. When \(k=2\), they are the degree-three cherry centres studied in the random-labelled-tree literature.

**Theorem (sharp covariance threshold).** For all integers \(n\ge4\) and \(1\le k\le n-3\), set
\[
 f_n=n\left(1-\frac1n\right)^{n-2},\qquad
 h_b=b\left(1-\frac1b\right)^{b-1},\qquad b=n-k-1.
\]
Then
\[
 \mathbb E S_{n,k}=n\binom{n-1}{k}\frac{(n-k-1)^{n-k-2}}{n^{n-2}}>0,
\]
\[
 \boxed{\operatorname{Cov}(L_n,S_{n,k})
 =\mathbb E S_{n,k}\,[k+h_{n-k-1}-f_n].}
\]
The sign is strictly **negative** if \(k=1\), and strictly **positive** for every \(k\ge2\). There are no zero cases in this stated range. In particular, attaching one prescribed leaf to a degree-two vertex is negatively associated in covariance with the global leaf total, whereas every pendant star with at least two leaves has positive covariance with that total.

More precisely, for distinct prescribed vertices \(v,a_1,\ldots,a_k\), write \(E_{v,A}\) for the event that \(v\) has degree \(k+1\) and the vertices of \(A=\{a_1,\ldots,a_k\}\) are leaves adjacent to \(v\). If \(Z_{b,b-1}\) counts empty boxes in \(b\) boxes after \(b-1\) independent uniform allocations, then the complete conditional law is
\[
 \boxed{(L_n\mid E_{v,A})\ \overset d=\ k+Z_{n-k-1,n-k-2}.}
\]
For every fixed \(k\ge1\), as \(n\) tends to infinity through \(n\ge k+3\),
\[
 k+h_{n-k-1}-f_n\longrightarrow k-\frac{k+2}{e},
\]
\[
 \frac{\operatorname{Cov}(L_n,S_{n,k})}{n}
 \longrightarrow\frac{e^{-(k+1)}}{k!}\left(k-\frac{k+2}{e}\right).
\]
For \(k\ge2\), despite the positive conditional mean shift, \(L_n\mid E_{v,A}\) and \(L_n\) are **not comparable in first-order stochastic order**: the conditional mean is higher, but the conditional law assigns zero probability to \(L_n=n-1\), whereas the unconditional star probability is positive.

## Assumptions and scope

All trees are simple, undirected and vertex-labelled; the distribution is uniform across Cayley trees, **not** uniform across unlabelled shapes, random recursive trees, or leaf-labelled binary phylogenetic trees. The integer ranges \(n\ge4\), \(1\le k\le n-3\) ensure the nonleaf neighbour outside a specified pendant \(k\)-star exists. The number \(S_{n,k}\) counts centres, equivalently choices of a centre and its entire \(k\)-element set of leaf neighbours; it does not count arbitrary \(k\)-subsets among more than \(k\) leaf neighbours.

## Proof

**1. Counting the marked local event.** Fix \(v\) and a \(k\)-element subset \(A\subseteq[n]\setminus\{v\}\). Deleting the leaves of \(A\) sends every tree satisfying \(E_{v,A}\) bijectively to a tree on \(m=n-k\ge3\) labelled vertices in which \(v\) is a leaf. Conversely, reattaching the specified \(k\) leaves to \(v\) reconstructs the original tree, with \(\deg(v)=k+1\). By the Prüfer correspondence, a tree on \(m\) labels has \(v\) as a leaf exactly when its \(m-2\)-letter Prüfer code omits \(v\). There are \((m-1)^{m-2}\) such trees. Hence
\[
 \Pr(E_{v,A})=\frac{(n-k-1)^{n-k-2}}{n^{n-2}}.
\]
Summing its indicator over the \(n\binom{n-1}{k}\) pairs \((v,A)\) gives the asserted \(\mathbb E S_{n,k}\); in the stated range no centre is counted more than once.

**2. Conditional leaf law.** Under \(E_{v,A}\), deleting \(A\) yields a uniform Cayley tree on \(m=n-k\) labels conditional on \(v\) being a leaf. Its Prüfer word has \(m-2=n-k-2\) independent uniform entries in the remaining \(m-1=n-k-1\) labels. The original \(k\) vertices of \(A\) are leaves, but \(v\) is *not* a leaf in the original tree. All other leaves correspond exactly to labels absent from that conditional Prüfer word. This proves the displayed conditional law. In the unconditional tree, a vertex is a leaf if and only if its label is absent from a uniform length-\(n-2\) Prüfer code, so \(\mathbb E L_n=f_n\). Taking conditional expectations gives
\[
 \mathbb E(L_n\mid E_{v,A})=k+h_{n-k-1}.
\]
Now expand \(L_n S_{n,k}\) as the sum of \(L_n\mathbf1_{E_{v,A}}\) over all marked events and subtract the product of means. This proves the exact covariance identity.

**3. Uniform strict sign bounds.** For integers \(b\ge2\) and \(n\ge4\), the following inequalities hold:
\[
 \frac{b+\frac12}{e}<h_b<\frac{b+\frac34}{e},\qquad
 \frac{n+\frac32}{e}<f_n<\frac{n+\frac{45}{16}}{e}\quad(n\ge5).
\]
The lower bounds follow from the elementary logarithm series. Explicitly,
\[
 1+(b-1)\log(1-1/b)>\frac1{2b},\qquad
 1+(n-2)\log(1-1/n)>\frac3{2n},
\]
because after retaining the first two negative terms of the logarithm, the remaining series is bounded by a geometric tail using \(1/j\le1/3\) for \(j\ge3\). Exponentiation and \(e^t>1+t\) give the lower bounds.

For the upper bound on \(h_b\), write \(\delta_b=1+(b-1)\log(1-1/b)\). Keeping its first two terms gives \(\delta_b\le(b+1)/(2b^2)\). When \(b\ge4\), use \(e^u\le(1-u)^{-1}\) for \(0\le u<1\), yielding
\[
 eh_b-b\le\frac{b(b+1)}{2b^2-b-1}\le\frac34.
\]
The last inequality is equivalent to \(2b^2-7b-3\ge0\), valid for \(b\ge4\). For \(b=2,3\), direct substitution with \(e<11/4\) proves the same strict inequality. Finally, \((1-1/n)^n<e^{-1}\) shows
\[
 ef_n<n\left(\frac n{n-1}\right)^2
 =n+\frac{n(2n-1)}{(n-1)^2}.
\]
The final fraction decreases for \(n>1\), and for \(n\ge5\) it is at most \(45/16\). These are all analytic inequalities, not numerical extrapolations.

For \(k=1\), \(b=n-2\), so the lower bound for \(f_n\) and upper bound for \(h_b\) imply
\[
 1+h_{n-2}-f_n<1-\frac{11}{4e}<0
\]
using \(e<11/4\). For \(k\ge2\), necessarily \(n\ge5\); the other two bounds imply
\[
 k+h_{n-k-1}-f_n
 > k-\frac{k+53/16}{e}
 \ge 2-\frac{85}{16e}>0
\]
using \(e>85/32\). Both elementary numerical bounds on \(e\) follow from its factorial series. This proves the complete sign classification.

**4. Asymptotics and non-ordering.** Taylor expansion of the same logarithms gives
\[
 f_n=\frac{n}{e}+\frac3{2e}+O(n^{-1}),\qquad
 h_b=\frac b e+\frac1{2e}+O(b^{-1}).
\]
Together with \(\mathbb E S_{n,k}\sim ne^{-(k+1)}/k!\) for fixed \(k\), these imply the limits. A tree on \(n\ge k+3\) vertices satisfying \(E_{v,A}\) has degree \(k+1\) at \(v\), so cannot be an \(n\)-vertex star; hence its leaf count is at most \(n-2\). Meanwhile an unconditional Cayley tree is a star with probability \(n/n^{n-2}>0\), and has \(n-1\) leaves. Thus the conditional distribution cannot dominate the unconditional one. For \(k\ge2\), its strictly larger mean rules out the opposite domination as well.

## Verification

The standalone `verify.py` uses only the Python standard library. It enumerates **all** Prüfer words for \(4\le n\le8\) (respectively \(16,125,1296,16807,262144\) trees), reconstructs every adjacency list, and independently checks \(\mathbb E L_n\), \(\mathbb E S_{n,k}\), \(\operatorname{Cov}(L_n,S_{n,k})\), and each marked-event conditional leaf distribution via exact rational arithmetic. It additionally checks the analytic sign formula for all \(4\le n\le250\) and admissible \(k\). The saved script passed **30,743 exact comparisons**; the general proof does not depend on this finite test.

Run: `python verify.py`.

## Relationship to prior work

Junk, Schmidt and Weber (arXiv:1911.02952, 2019; Arch. Math. 2020), Section 3, define strict cherries with degree-three centres and compute their occurrence probability, expectation, and second moment in uniform labelled trees. Their expectation equals our \(k=2\) marginal \(\mathbb E S_{n,2}\). That known marginal is explicitly not a claimed contribution. Their inspected result does not give the joint moment with the total leaf count, the opposite \(k=1\) sign, the all-\(k\) threshold, or the marked conditional occupancy law.

Janson (arXiv:2005.13832, 2020; Combin. Probab. Comput. 2021), especially Section 9 and Remark 9.3, treats uniform labelled trees within the global limit theory for conditioned Galton–Watson trees; it does not supply a finite-size covariance sign threshold between leaves and pendant-star centres. It confirms that the Cayley model is a natural combinatorial-probability object. Other phylogenetic cherry/pitchfork literature uses rooted binary evolutionary-tree distributions, not the uniform Cayley law considered here.

## Limitations

The theorem is only for uniform **labelled** Cayley trees and the exact-degree pendant-star definition. It does not assert stochastic ordering for \(k=1\), or any joint central-limit theorem. The asymptotic formulas fix \(k\) while \(n\to\infty\); no uniform-in-\(k\) assertion is made. The exact probabilities follow from classical Prüfer enumerations, and older unlocated mixed-profile theorems might imply the sign result; independent historical-priority assessment remains outstanding.

## References

- Junk, L., Schmidt, S. and Weber, M. *Almost all trees have quantum symmetry*. arXiv:1911.02952 (first public posting 2019-11-07); *Archiv der Mathematik* 115 (2020), 367–378. doi:10.1007/s00013-020-01476-x. See Section 3, Lemmas 3.5–3.8.
- Janson, S. *Tree limits and limits of random trees*. arXiv:2005.13832 (first public posting 2020-05-28); *Combinatorics, Probability and Computing* 30 (2021), 849–893. doi:10.1017/S0963548321000055. See Section 9 and Remark 9.3.
- Choi, K. P., Thompson, A. and Wu, T. *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*. arXiv:2002.12643 (2020). Different sampling models, cited for the distinction from binary phylogenetic cherries.
