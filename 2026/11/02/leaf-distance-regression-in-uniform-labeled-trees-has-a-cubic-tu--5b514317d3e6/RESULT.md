# Leaf–distance regression in uniform labeled trees has a cubic turning point

## Finding

For a uniformly sampled labeled tree \(T\) on \(n\ge3\) vertices, fix two distinct vertices \(a,b\). Let \(D=\operatorname{dist}_T(a,b)\) and let \(L\) be the number of degree-one vertices. For every integer \(1\le k\le n-1\),
\[
\boxed{\mathbb E[L\mid D=k]=\left(n-k-1+\frac{2k}{k+1}\right)\left(\frac{n-1}{n}\right)^{n-k-2}.}
\]
In particular, for \(1\le k\le n-2\),
\[
\boxed{\mathbb E[L\mid D=k+1]-\mathbb E[L\mid D=k]=\left(\frac{n-1}{n}\right)^{n-k-3}\frac{2(n-1)-k(k+1)^2}{n(k+1)(k+2)}.}
\]
For every \(n\ge4\), the mean is strictly increasing at integer \(k\) satisfying \(k(k+1)^2<2(n-1)\), strictly decreasing when the reverse inequality holds, and equal at the unique possible integer solution of equality. Hence it has one peak or a two-point flat peak, with every maximizing \(k\) obeying \(k\sim(2n)^{1/3}\). For \(n=3\) the regression is constant at \(2\).

The result is part of a **complete conditional leaf law**. Conditional on a specified ordered \(a\)-to-\(b\) path with \(s=k+1\) vertices, choose any \(r\) distinct vertices outside that path and \(q\) of its two endpoints, where \(0\le r\le n-s\) and \(q\in\{0,1,2\}\). The probability that all these \(r+q\) vertices are leaves equals
\[
\boxed{P_{n,s}(r,q)=\frac{s-q}{s}\left(\frac{n-r-q}{n}\right)^{n-s-1}}
\]
whenever \(s>q\); it is \(0\) when \(s=q\). Path-interior vertices cannot be leaves. The formula is independent of the path labels and so also applies after conditioning only on \(D=k\), with the specified vertices understood relative to the realized path. In particular, the conditional probability-generating function is
\[
\boxed{\mathbb E[z^L\mid D=k]=\sum_{r=0}^{n-s}\sum_{q=0}^{2}\binom{n-s}{r}\binom{2}{q}P_{n,s}(r,q)(z-1)^{r+q}.}
\]

## Assumptions and scope

The sample space consists of all \(n^{n-2}\) unrooted trees on the labeled vertex set \(\{1,\dots,n\}\), all equally likely. No edges are weighted. The vertices \(a\ne b\) are fixed in advance; the path between them is the unique simple path. A leaf always means an undirected degree-one vertex. The distance \(k\) ranges over the full support \(1,\dots,n-1\); \(n\ge3\) excludes the isolated two-vertex special case. When \(s=n\), the displayed power has exponent \(-1\) and remains well-defined because \(n-r-q\ge1\) whenever \(s>q\). No path interior vertex can contribute to \(L\).

## Proof

**Rooted-forest count.** For a labeled set of \(N\) vertices and a specified root subset of size \(h\) with \(1\le h\le N\), the number of forests in which every component contains exactly one root is \(hN^{N-h-1}\). Orienting all edges toward roots, the directed matrix-tree theorem gives the determinant of the \((N-h)\)-square minor of \(NI-J\), which is \(hN^{N-h-1}\). When \(N=h\), the determinant of the empty matrix equals \(1\) and the formula also gives \(1\).

**Conditioning on a path.** Fix a simple path \(P\) from \(a\) to \(b\) involving exactly \(s\) labeled vertices. Every spanning tree containing \(P\) is obtained by adjoining a forest rooted at its \(s\) vertices. There are exactly \(s n^{n-s-1}\) such trees. Containing \(P\) is equivalent to having \(P\) as the unique \(a\)-to-\(b\) path.

Require any \(r\) specified off-path vertices and any \(q\) selected path endpoints to be leaves. If \(q=s\), this is impossible since \(n\ge3\). Otherwise, delete the \(q\) chosen endpoints and their forced path edges. Delete the \(r\) chosen off-path leaves and their incident edges. The remaining graph is a forest rooted at the \(s-q\) surviving path vertices on \(N=n-r-q\) vertices; there are \((s-q)N^{N-(s-q)-1}\) such rooted forests. Each removed off-path leaf must be attached to one of these \(N\) surviving vertices, with \(N^r\) independent attachment choices; the removed path endpoints are then reattached along their prescribed path edges. The number of admissible trees is therefore \((s-q)(n-r-q)^{n-s-1}\). Dividing by the unconditional path-containing count proves \(P_{n,s}(r,q)\).

All conditional joint inclusion probabilities of the \(n-s+2\) eligible leaf indicators are given by \(P_{n,s}(r,q)\). Expanding \(z^L=\prod_v(1+(z-1)\mathbf1_{\{v\text{ leaf}\}})\) and grouping the subsets by their off-path count \(r\) and endpoint count \(q\) proves the polynomial identity. Because every path realization of length \(k\) has the same conditional law, the identities remain valid when conditioning only on \(D=k\).

**Mean.** For one off-path vertex the inclusion probability is \(((n-1)/n)^{n-s-1}\). For one endpoint it is \((s-1)/s\) times that same factor. There are \(n-s\) off-path vertices and two endpoints, yielding the claimed mean with \(s=k+1\).

**Turning point.** Subtract the explicit mean at successive lengths and factor; this gives exactly the displayed first-difference identity. Its prefactor and denominator are strictly positive for the stated ranges. The sign is that of \(2(n-1)-k(k+1)^2\). The function \(k\mapsto k(k+1)^2\) is strictly increasing for positive integers, so there can be at most one zero and precisely one transition from positive to negative differences (for \(n\ge4\), the first difference is positive and the final one negative). Every maximizing integer is within one integer step of the positive real root of \(x(x+1)^2=2(n-1)\), which equals \((2n)^{1/3}(1+o(1))\). The \(n=3\) case follows directly by substitution. This completes the proof.

## Verification

The included standalone \(\texttt{VERIFY.py}\) independently enumerates all Prüfer words for \(3\le n\le8\), decodes each tree, reconstructs the unique marked path and leaf indicators, and checks the exact distance counts, conditional means, and all eligible marked-leaf inclusion cases. It also checks the finite-difference signs using exact rational arithmetic for \(3\le n<150\). Executing \(\texttt{python3 VERIFY.py}\) produced: `PASS: 280,391 trees enumerated; 11,214 exact assertions`. The infinite statements rely on the displayed forest-count proof, not on the finite verification.

## Relationship to prior work

Remmel and Williamson (2010) count labeled trees with a given set or number of leaves, without conditioning on the distance between two specified vertices. Their leaf-count enumeration motivates the question but does not state the path-conditioned joint inclusion law or the cubic turning-point theorem. Bousquet-Mélou and Chapuy (2012) give stronger general enumerations by height and offspring degree in rooted Cayley trees; these could be summed to recover joint leaf/distance quantities but do not present the explicit conditional regression or its sharp unique sign reversal in the inspected sections. The preexisting published finding *Exact negative regression between endpoint degree and distance in a uniform Cayley tree* treats the degree distribution at one marked endpoint and hence overlaps with the endpoint-only special case. **That special case is not claimed as new**. The new claim concerns the full eligible-vertex inclusion law together with the conditional total-leaf regression and its cubic turning point. Traditional rooted-forest counting is explicitly used as an input, not claimed as new.

## Limitations

The model is uniform labeled trees only, not weighted spanning trees or simply generated trees with arbitrary offspring laws. The theorem is exact for all admissible finite \(n\), but the claimed research contribution is not an independent historical-priority certification; broader enumerators could yield the formula after nontrivial summation. The complete full text of the closest published endpoint-degree finding and several older random-tree sources was not independently accessible here. The exhaustive computer checks cover finite sizes and cannot establish the infinite result on their own. An independent scientific audit has not been performed.

## References

- J. B. Remmel and S. G. Williamson, *Ranking and unranking trees with a given number or a given set of leaves*, arXiv:1009.2060v1 (10 September 2010), https://arxiv.org/abs/1009.2060 .
- M. Bousquet-Mélou and G. Chapuy, *The vertical profile of embedded trees*, Electronic Journal of Combinatorics 19(3) (2012), P46, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p46/pdf/ .
- S. Janson, *The Wiener index of simply generated random trees*, Random Structures & Algorithms 22 (2003), https://doi.org/10.1002/rsa.10074 .
- *Exact negative regression between endpoint degree and distance in a uniform Cayley tree*, published record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae .
