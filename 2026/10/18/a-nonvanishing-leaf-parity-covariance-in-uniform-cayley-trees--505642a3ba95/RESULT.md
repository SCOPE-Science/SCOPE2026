# A nonvanishing leaf–parity covariance in uniform Cayley trees

## Finding

Let \(T_n\) be uniform among the \(n^{n-2}\) labeled trees on \(\{1,\ldots,n\}\), rooted at vertex \(1\). Let \(B_n\) be the number of vertices at even graph distance from the root (the root is included), and \(L_n\) the number of vertices of degree one. For each integer \(n\ge3\), define
\[
 w_n=\sum_{d=1}^{n-1}(-1)^d\frac{(d+1)(n-2)!}{(n-d-1)!\,n^d},\qquad
 b_n=\frac{n+1}{2}+\frac{n-1}{2}w_n.
\]
Then the **exact** finite-size covariance is
\[
 \operatorname{Cov}(B_n,L_n)=
 \left(1-\frac1n\right)^{n-2}
 \left[2n-1+(n-3)b_{n-1}-nb_n\right],
\]
where \(b_m\) is the same expression with \(n\) replaced by \(m\). In particular,
\[
 \boxed{\operatorname{Cov}(B_n,L_n)=\frac{1}{8e}+O(n^{-1})\quad(n\to\infty).}
\]
The limiting constant is strictly positive. Thus, despite the order-\(\sqrt n\) fluctuations of the parity-class size and the leaf count, their *unscaled* covariance approaches a nonzero finite value. For \(n=3\) it is zero because every three-vertex tree has two leaves; for \(n=4\) it is \(3/32\). The result does **not** assert strict positivity for every finite \(n\ge4\).

A supplementary exact conditional law clarifies the interaction. For \(1\le k\le n-1\), with \(\ell=n-k\),
\[
 \Pr(B_n=k)=\frac{\binom{n-1}{k-1}k^{\ell-1}\ell^{k-1}}{n^{n-2}}.
\]
Given \(B_n=k\), the number of leaves in the even and odd classes are independent empty-box counts: the first comes from \(\ell-1\) independent uniform placements in \(k\) boxes, the second from \(k-1\) independent uniform placements in \(\ell\) boxes. In particular,
\[
 \mathbb E[L_n\mid B_n=k]
 =k\left(1-\frac1k\right)^{\ell-1}
 +\ell\left(1-\frac1\ell\right)^{k-1}.
\]
The empty-word convention applies when an exponent is zero. The conditional occupancy representation follows from the classical bipartite Prüfer encoding; that encoding itself is not claimed as new.

## Assumptions and scope

All trees are simple, unweighted, and uniformly sampled from the labeled Cayley model. Distances are undirected graph distances. A leaf means degree exactly one, including the root when applicable. The root is label \(1\), which has the same distribution as an independent uniform root by exchangeability. No statement is made for nonuniform tree models, non-Cayley trees, or for the joint law of a greedy independent set with the leaf count; equality of one-dimensional distributions is not equality of joint laws.

## Proof

**1. Leaf deletion.** The Prüfer word has length \(n-2\) and independent uniform letters in \(\{1,\ldots,n\}\). A fixed vertex is a leaf precisely when its letter is absent. Hence
\[
 p_n:=\Pr(v\text{ is a leaf})=\left(1-\frac1n\right)^{n-2}.
\]
Conditioned on this event, deleting \(v\) produces a uniform Cayley tree on the other \(n-1\) labels, and the deleted leaf's neighbor is independent and uniform among those labels. This follows either from the leaf-constrained Prüfer enumeration or by counting the \(n-1\) possible attachments to each smaller tree.

Write \(b_m=\mathbb E B_m\). If the root itself is the deleted leaf, its parity class in the original tree consists of the deleted root plus the odd-distance vertices relative to its uniformly selected neighbor in the smaller tree. Hence
\[
 \mathbb E[B_n\mid 1\text{ is a leaf}]=n-b_{n-1}.
\]
If some fixed \(v\ne1\) is the deleted leaf, the original root remains. The new vertex is even-distance precisely when its uniform attachment neighbor lies in the smaller tree's odd-distance class. Therefore
\[
 \mathbb E[B_n\mid v\text{ is a leaf}]
 =b_{n-1}+\frac{n-1-b_{n-1}}{n-1}
 =1+\frac{n-2}{n-1}b_{n-1}.
\]
Since \(L_n\) is the sum of the \(n\) leaf indicators, linearity of covariance gives exactly
\[
 \operatorname{Cov}(B_n,L_n)
 =p_n\Bigl\{n-b_{n-1}+(n-1)\bigl[1+\frac{n-2}{n-1}b_{n-1}\bigr]-nb_n\Bigr\},
\]
which is the asserted formula.

**2. Root-parity mean.** For distinct fixed vertices \(1\) and \(2\), the event that their unique path has \(d\) edges can be counted by choosing its \(d-1\) internal labels in order and then completing this path forest to a labeled tree. The path component has \(d+1\) vertices. Cayley's rooted-forest completion identity yields
\[
 \Pr\bigl(\operatorname{dist}(1,2)=d\bigr)
 =\frac{(d+1)(n-2)!}{(n-d-1)!\,n^d},\qquad 1\le d\le n-1.
\]
Let \(w_n=\mathbb E[(-1)^{\operatorname{dist}(1,2)}]\). By exchangeability, the root contributes one vertex and each of the remaining \(n-1\) contributes probability \((1+w_n)/2\), proving the stated formula for \(b_n\).

**3. Asymptotic extraction.** For integer \(n\ge4\), let \(E_m(z)=\sum_{j=0}^{m}z^j/j!\). Reindexing the finite path sum gives
\[
 w_n=(-1)^{n-1}\frac{(n-2)!}{n^{n-2}}
 \bigl[E_{n-2}(-n)+E_{n-3}(-n)\bigr].
\]
The integral remainder formula for the exponential Taylor series gives the exact identity
\[
 w_n=\int_0^1 e^{-nt}(1-t)^{n-3}(nt-2)\,dt
 +2(-1)^{n-1}\frac{(n-2)!}{n^{n-2}}e^{-n}.
\]
The final term is exponentially small by Stirling's formula. In the integral put \(s=nt\):
\[
 \frac1n\int_0^n e^{-s}(1-s/n)^{n-3}(s-2)\,ds.
\]
For bounded \(s\),
\[
 e^{-s}(1-s/n)^{n-3}
 =e^{-2s}\left[1+\frac{3s-s^2/2}{n}+O\!\left(\frac{1+s^4}{n^2}\right)\right].
\]
For rigor, apply the expansion on \(0\le s\le n^{1/3}\); the complementary integral is exponentially small, while the Taylor remainder on the first region has an integrable polynomial-times-exponential majorant. Thus termwise integration is justified and yields
\[
 w_n=\frac1n\int_0^\infty e^{-2s}(s-2)\,ds
 +\frac1{n^2}\int_0^\infty e^{-2s}(s-2)(3s-s^2/2)\,ds
 +O(n^{-3})
 =-\frac{3}{4n}-\frac{11}{16n^2}+O(n^{-3}).
\]
Consequently,
\[
 b_n=\frac n2+\frac18+\frac1{32n}+O(n^{-2}),
\]
and substitution into the *exact* covariance formula gives
\[
 2n-1+(n-3)b_{n-1}-nb_n=\frac18+O(n^{-1}),
 \qquad p_n=e^{-1}+O(n^{-1}).
\]
Multiplying finishes the proof of the \(1/(8e)\) limit and its stated rate.

**4. Conditional leaf law.** Fix the even-distance vertex set of size \(k\) containing the root. A valid tree must be a spanning tree of the complete bipartite graph with these two vertex classes. The bipartite Prüfer encoding is a pair of independent words: one of length \(\ell-1\) over the \(k\) even vertices, and one of length \(k-1\) over the \(\ell\) odd vertices. In each class a vertex's degree is one plus its multiplicity in the corresponding word. A leaf is therefore an empty box. There are \(k^{\ell-1}\ell^{k-1}\) such trees for each fixed partition, and \(\binom{n-1}{k-1}\) possible even sets, establishing both the distribution and the conditional independence and mean formulas.

## Verification

The standalone `verify.py` checks the formulas using exact rational arithmetic and independent exhaustive Prüfer-word enumeration for every labeled tree on \(2\le n\le7\). It checks the full distribution of the root parity-class size, its conditional leaf mean at every admissible class size, and the covariance formula. It also evaluates the closed form for larger finite orders as a diagnostic; these finite tests do not prove the limit. High-precision numerical quadrature separately agrees with the asymptotic constant for increasing \(n\). Run with `python verify.py` (standard library only).

## Relationship to prior work

Contat (2021, arXiv:2103.03800) establishes the distributional identity between a greedy independent-set size and the even-height class in a uniform Cayley tree, together with Gaussian parity-class fluctuations. It supplies the natural motivation for refining the parity statistic but does not give a joint leaf–parity covariance. Hladký, Nachmias and Tran (2017, arXiv:1711.09788) study local limits and degree frequencies of uniform spanning trees, including the asymptotic leaf fraction; their global leaf–root-parity covariance is not addressed. Dong and Ge (2021, arXiv:2103.05294) enumerate complete-bipartite spanning trees containing prescribed forests; their general counting identity supplies relevant adjacent combinatorics but not the present second-order statistic. Classical Cayley/Prüfer and bipartite spanning-tree counts are acknowledged as background rather than novelty. The contribution asserted here is the exact marked-leaf covariance reduction and its nonzero \(1/(8e)\) asymptotic.

## Limitations

The theorem is restricted to uniform labeled Cayley trees and does not establish a sign classification for all finite sample sizes. The conditional bipartite occupancy law is a known consequence of classical encoding and is included for interpretation and independent finite verification, not asserted as a new standalone theorem. The asymptotic covariance concerns the root-defined even class, not the joint law of any greedy independent-set algorithm with leaves. Potential implicit derivations in older generating-function or joint tree-statistic literature remain a historical-priority risk. No independent validation has been performed.

## References

1. A. Contat, *A surprising symmetry for the greedy independent set on Cayley trees*, arXiv:2103.03800, first public version 2021-03-05. https://arxiv.org/abs/2103.03800
2. J. Hladký, A. Nachmias, T. Tran, *The local limit of the uniform spanning tree on dense graphs*, arXiv:1711.09788, first public version 2017-11-27. https://arxiv.org/html/1711.09788v3
3. F. Dong, J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first public version 2021-03-09. https://arxiv.org/html/2103.05294v2
4. Classical Cayley–Prüfer enumeration and the complete-bipartite spanning-tree formula, as discussed in references 2 and 3.
