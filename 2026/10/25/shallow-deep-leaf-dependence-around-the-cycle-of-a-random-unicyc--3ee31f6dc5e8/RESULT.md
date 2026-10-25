# Shallow–deep leaf dependence around the cycle of a random unicyclic graph

## Finding

Let \(G\) be uniformly sampled from all connected, simple, labeled unicyclic graphs on \(n\ge3\) vertices, and condition on its unique cycle having \(k\) vertices, with \(3\le k\le n\). Put \(m=n-k\). Every degree-one vertex lies outside the cycle. Let \(J\) count degree-one vertices **adjacent to the cycle** (distance one), and let \(H\) count degree-one vertices **not adjacent to the cycle** (distance at least two).

For integers \(r,s\ge0\) with \(r+s\le m\), define \((x)_{\underline t}=x(x-1)\cdots(x-t+1)\), with \((x)_{\underline0}=1\), and
\[
\mathcal F(q,k)=
\begin{cases}
1,&q=k,\\
kq^{q-k-1},&q>k.
\end{cases}
\]
Then **all mixed factorial moments** of the two cycle-interface leaf classes are
\[
\boxed{\mathbb E[(J)_{\underline r}(H)_{\underline s}\mid K=k]
=(m)_{\underline{r+s}}\,
\frac{k^r(m-r-s)^s\mathcal F(n-r-s,k)}{\mathcal F(n,k)}.}
\]
The factor \(0^0\) in this formula is interpreted as \(1\); when \(s>0\) and \(m-r-s=0\) its value is zero. The displayed moments determine the entire finite joint distribution of \((J,H)\). Equivalently, its probability-generating polynomial is
\[
\mathbb E[z^Jw^H\mid K=k]
=\sum_{r+s\le m}\frac{(z-1)^r(w-1)^s}{r!s!}\,
\mathbb E[(J)_{\underline r}(H)_{\underline s}\mid K=k].
\]

For \(m\ge2\) the covariance is **strictly negative**. Explicitly,
\[
\boxed{\operatorname{Cov}(J,H\mid K=k)
=\frac{m(m-1)k}{n^2}\left[
(m-2)\left(1-\frac2n\right)^{m-3}
-m\left(1-\frac1n\right)^{2m-4}\right]<0.}
\]
For \(m=0\) or \(m=1\) the covariance is zero. If \(k/n\to\alpha\in(0,1)\) as \(n\to\infty\), then
\[
\boxed{\frac{\operatorname{Cov}(J,H\mid K=k)}n
\longrightarrow-\alpha(1-\alpha)^2(1+\alpha^2)e^{-2(1-\alpha)}.}
\]
Thus the negative dependence between shallow and deeper pendant leaves has a nonvanishing linear scale.

## Assumptions and scope

The graphs are undirected, simple, connected, and uniformly distributed on the fixed labeled vertex set; their unique cycle is the graph's two-core. The conditioning \(K=k\) has positive probability for each admissible \(k\). The result is finite and exact for all \(3\le k\le n\), with the stated endpoint conventions. The covariance and scaling results concern only this conditional distribution; they do not assert unconditional sign or a joint central limit theorem.

## Proof

**Cycle decomposition and forest count.** Fix a set of \(k\) cycle vertices and a cyclic ordering. Removing the \(k\) cycle edges leaves a forest on all \(n\) vertices, with exactly the cycle vertices as prescribed roots. Conversely, each such forest reconstructs precisely one graph with the fixed cycle. By the rooted-forest enumeration of Cayley and its extensions (see Pitman, Section 2.1), the number of rooted forests on \(q\) labeled vertices with these \(k\) designated roots is \(\mathcal F(q,k)\). Therefore the forest is conditionally uniform, and its distribution depends on the cycle only through \(n,k\).

**Marked leaves.** Mark disjoint ordered lists of \(r\) and \(s\) off-cycle vertices. Require the first \(r\) to be leaves adjacent to the cycle, and the remaining \(s\) to be leaves at distance at least two. Delete all \(r+s\) marked leaves. This leaves a rooted forest with exactly \(k\) fixed roots on \(n-r-s\) vertices. Conversely, each deleted first-class leaf can be reattached to any of the \(k\) cycle roots; each second-class leaf can be reattached to any of the \(m-r-s\) surviving off-cycle vertices. These choices neither introduce cycles nor change the leaf status of the marked vertices, because their attachments are outgoing toward surviving parents. Hence the number of completions is exactly
\[
k^r(m-r-s)^s\mathcal F(n-r-s,k).
\]
There are \((m)_{\underline{r+s}}\) choices of the two ordered lists. Dividing by \(\mathcal F(n,k)\) proves the joint factorial-moment identity, including the boundary \(n-r-s=k\).

**Covariance and sign.** For \(m\ge2\), the cases \((r,s)=(1,0),(0,1),(1,1)\) give
\[
\begin{aligned}
\mathbb EJ&=\frac{mk}{n}\left(1-\frac1n\right)^{m-2},\\
\mathbb EH&=\frac{m(m-1)}n\left(1-\frac1n\right)^{m-2},\\
\mathbb E[JH]&=\frac{m(m-1)k(m-2)}{n^2}\left(1-\frac2n\right)^{m-3}.
\end{aligned}
\]
The third expectation is zero when \(m=2\), so the covariance is negative there. For \(m\ge3\), its ratio to \(\mathbb EJ\mathbb EH\) is
\[
\frac{\mathbb E[JH]}{\mathbb EJ\mathbb EH}
=\frac{m-2}{m}\left(\frac{n}{n-1}\right)^2
\left(1-\frac1{(n-1)^2}\right)^{m-3}<1,
\]
since \(m\le n-3\) and
\[
m(n-1)^2-(m-2)n^2=2n(n-m)+m>0.
\]
This proves strict negativity. For \(m=0,1\), \(H=0\) deterministically.

**Asymptotic constant.** If \(m/n\to\beta=1-\alpha\in(0,1)\), a logarithmic expansion of the preceding ratio gives
\[
\frac{\mathbb E[JH]}{\mathbb EJ\mathbb EH}
=1+\frac{-2/\beta+2-\beta}{n}+o(n^{-1}).
\]
The two displayed first moments satisfy \(\mathbb EJ/n\to\alpha\beta e^{-\beta}\) and \(\mathbb EH/n\to\beta^2e^{-\beta}\). Multiplying these expressions yields
\[
\operatorname{Cov}(J,H)/n\to
-\alpha\beta^2(2-2\beta+\beta^2)e^{-2\beta}
=-\alpha(1-\alpha)^2(1+\alpha^2)e^{-2(1-\alpha)}.
\]

## Verification

The standalone, standard-library script `unicyclic_leaf_verify.py` enumerates all rooted forests with designated roots for \(4\le n\le9\), checks every admissible factorial moment in the theorem, and compares the exact signs. It also independently enumerates connected simple unicyclic graphs for \(3\le n\le7\), recovers the unique cycle by iteratively stripping leaves, and checks the same moments. In the recorded execution, all \(203\) rooted-forest comparisons over \(223729\) forests and all \(70\) graph comparisons over \(72193\) graphs passed. These finite checks are not substituted for the all-size proof.

## Relationship to prior work

Pitman's *Coalescent Random Forests* establishes the fixed-root forest enumeration and broader coalescent formulas used in the proof; those enumerations are antecedents, not new claims. The ordinary total-leaf marginal \(J+H\) has an existing exact cycle-length/leaf-count enumeration, and no novelty is claimed for that marginal. The specific two-class **parent-on-cycle versus parent-off-cycle** joint law is not determined by the marginal total-leaf distribution or by the uncolored degree counts of a rooted forest. The inspected unicyclic-component literature by Janson and by Ben-Naim–Krapivsky concerns cycle/component sizes and graph evolution, not this parent-class joint dependence. Janson's full paper was unavailable for direct comparison, so priority is subject to that qualification.

## Limitations

This is a statement about uniformly selected connected **simple** labeled unicyclic graphs conditional on their cycle length, not about a general growing random-graph process or a multigraph ensemble. An earlier joint root-adjacency count may exist under another name; a negative search result does not establish priority. The finite program verifies small cases but does not certify the infinite proof or supply independent validation.

## References

1. J. Pitman, *Coalescent Random Forests*, Berkeley Technical Report 457 (September 1, 1996), Section 2.1, especially formula (6), and Section 6. https://statistics.berkeley.edu/tech-reports/457 .
2. S. Janson, *Cycles and Unicyclic Components in Random Graphs*, Combinatorics, Probability and Computing 12 (2003), 27–52. https://doi.org/10.1017/S0963548302005412 .
3. E. Ben-Naim and P. L. Krapivsky, *Unicyclic Components in Random Graphs*, Journal of Physics A 37 (2004), L189–L196, first arXiv posting March 18, 2004. https://arxiv.org/abs/cond-mat/0403453 .
