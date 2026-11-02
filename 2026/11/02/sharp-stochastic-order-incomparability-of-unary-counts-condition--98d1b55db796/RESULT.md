# Sharp stochastic-order incomparability of unary counts conditioned on root degree in uniform plane trees

## Finding

Let \(T_{n,k}\) be a uniformly selected rooted ordered plane tree with exactly \(n+1\) vertices, conditioned on its root having exactly \(k\) children, where \(n\ge2\) and \(1\le k\le n\). Let \(U_{n,k}\) count **nonroot vertices with exactly one child**. Then for every \(1\le k\le n-2\), the laws of \(U_{n,k}\) and \(U_{n,k+1}\) are incomparable in usual stochastic order. Put \(e=n-k\). The incomparable directions are witnessed by consecutive upper-tail thresholds:

\[
\frac{\Pr(U_{n,k+1}\ge e-1)}{\Pr(U_{n,k}\ge e-1)}=\frac{2n-k-1}{k+1}>1,
\qquad
\Pr(U_{n,k+1}\ge e)=0<\Pr(U_{n,k}\ge e).
\]

This holds for **all** eligible sizes and adjacent root degrees. At the sole remaining adjacent boundary, \(k=n-1\), we instead have \(U_{n,n-1}=1\) and \(U_{n,n}=0\) almost surely. Thus \(n=3\) is the first size with incomparability. The complete conditional mass function is

\[
\Pr(U_{n,k}=u)=
\frac{\binom nu\,[z^{n-k-u}]\bigl(1+z^2/(1-z)\bigr)^{n-u}}
{\binom{2n-k-1}{n-k}},\qquad 0\le u\le n,
\]

where coefficients at negative indices are zero. The notation \([z^j]G(z)\) denotes the coefficient of \(z^j\).

## Assumptions and scope

A rooted ordered plane tree is a finite rooted tree in which the children of each vertex are linearly ordered. Every tree with the prescribed total size and root outdegree receives equal probability. Only **nonroot** outdegree-one vertices are counted; allowing the root would change the statistics. A random tree with a fixed root degree is equivalent, by deleting the root, to a uniform ordered forest of \(k\) nonempty plane trees on \(n\) total vertices. The notation \(X\le_{\mathrm{st}}Y\) means \(\Pr(X\ge t)\le\Pr(Y\ge t)\) at all real thresholds \(t\). Incomparability means neither of the two stochastic inequalities holds.

## Proof

**1. Degree-word enumeration.** An ordered forest of \(k\) nonempty plane trees with \(n\) vertices is encoded by the preorder list of its nonnegative outdegrees \(d_1,\ldots,d_n\). Their sum is \(n-k\). The generalized cyclic lemma for walks with increments \(d_i-1\ge-1\), total \(-k\), shows that among the \(n\) indexed cyclic shifts of every such degree list exactly \(k\) give valid ordered forests (counting indexed shifts even for periodic lists). Consequently any statistic invariant under cyclic rotation of the outdegree list has its number of forests equal to \(k/n\) times the number of its unrestricted nonnegative degree lists.

The total number of unrestricted lists is the coefficient \([z^{n-k}](1-z)^{-n}=\binom{2n-k-1}{n-k}\). Hence the forest count is
\[
F_{n,k}=\frac{k}{n}\binom{2n-k-1}{n-k}.
\]
Fixing exactly \(u\) outdegrees equal to one means choosing their locations, assigning degree one to them, and assigning degrees from \(\{0,2,3,\ldots\}\) to the others. The corresponding generating function is \(\binom nu z^u(1+z^2/(1-z))^{n-u}\). Applying the same cyclic lemma and dividing by \(F_{n,k}\) gives the stated probability mass function for every \(1\le k\le n\) and \(0\le u\le n\).

**2. Two extreme levels and a gap.** Set \(e=n-k\). Every unary vertex contributes exactly one of the \(e\) child edges in the forest; therefore \(U_{n,k}\le e\). Equality requires every vertex to have outdegree zero or one, i.e. each of the \(k\) components must be a directed path. The \(k\) positive component sizes form a composition of \(n\), yielding exactly \(\binom{n-1}{k-1}\) such forests. The level \(e-1\) is impossible: after assigning \(e-1\) child edges to unary vertices, the one remaining edge cannot be assigned to another vertex without creating an additional unary vertex or a vertex of outdegree at least two, which would require at least two remaining edges. Thus
\[
\Pr(U_{n,k}=e)=\frac{\binom nk}{\binom{2n-k-1}{e}}>0,
\qquad \Pr(U_{n,k}=e-1)=0.
\]

For a forest with \(k+1\) components, the maximum unary count is \(e-1\), with probability
\[
\Pr(U_{n,k+1}=e-1)=\frac{\binom n{k+1}}{\binom{2n-k-2}{e-1}}.
\]
The adjacent ratio reduces exactly to
\[
\frac{\binom n{k+1}/\binom{2n-k-2}{e-1}}
{\binom nk/\binom{2n-k-1}{e}}=\frac{2n-k-1}{k+1}.
\]
When \(k\le n-2\), the ratio exceeds one because its numerator exceeds its denominator by \(2(e-1)>0\). At threshold \(e-1\), the old forest's tail contains only its probability at \(e\) (the \(e-1\) level is absent); the new forest's tail contains only its probability at \(e-1\). The new upper tail is therefore strictly larger. At threshold \(e\), the new tail is zero and the old one is positive. These two contradictory inequalities prove stochastic incomparability without extrapolating from finite examples.

**3. Terminal boundary and first size.** For \(k=n-1\) the forest has exactly one edge, so precisely one nonroot vertex has one child; for \(k=n\) all \(n\) components are isolated and there are no unary vertices. Both assertions are deterministic. For \(n=2\) there is only this boundary; for \(n=3\), \(k=1\) lies in the incomparable regime. This exhausts all adjacent comparisons.

## Verification

Run `python3 verify.py` from the directory containing the standalone script. Python 3.10+ and the standard library suffice. The checker independently enumerates every ordered tree through \(11\) total vertices and compares all root-degree/unary-count cells with the coefficient formula. It also verifies the count identities, upper support gaps, both opposing exact tails and the terminal boundary for every \(2\le n\le44\). Execution completed with **26,310 exact assertions passed**. Enumerating finitely many trees does not prove the assertion for every \(n\); the cyclic-lemma argument and symbolic binomial-ratio proof above establish the unrestricted claim.

For the minimal example \(n=3\), conditioned root degrees \(1\) and \(2\) yield \(\Pr(U_{3,1}=0)=\Pr(U_{3,1}=2)=1/2\) and \(U_{3,2}=1\) almost surely; the upper tails cross at thresholds \(1\) and \(2\).

## Relationship to prior work

The enumerations of uniform plane forests and their degree sequences are classical; no claim of novelty is made for cyclic lemmas, compositions, Galton–Watson tree representations, or the coefficient formula viewed as an instance of general degree-sequence enumeration. Janson (2011) discusses uniform plane forests and their conditioned allocation representations, while Janson (2013) analyzes asymptotic degree and fringe-subtree statistics. Drmota and Gittenberger (1999) consider degree-count distributions in tree families including plane trees and forests. The specific contribution assessed here is the **all-size, all-adjacent-root-degree stochastic-order obstruction with the exact two-threshold ratio and its unique terminal exception**. This is not an ordering of leaves, of tree heights, or of random recursive trees.

## Limitations

The result concerns **adjacent root degrees** and nonroot unary counts only. It does not classify nonadjacent root-degree comparisons or stochastic order of other degree statistics. The counting formula is an exact finite-sample law but is derived from established enumeration methods; implicit coverage by an earlier general multivariate degree-count theorem is a real historical-priority risk. The full text of the 1999 degree-distribution paper was not accessible in the consulted sources, so its abstract alone cannot establish that the present theorem is absent. The computation supplies finite checks, not an independent proof or independent external review.

## References

1. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1 (public December 2, 2011), Sections 1 and 11.8. https://arxiv.org/abs/1112.0510
2. S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, arXiv:1312.1211v1 (public December 4, 2013; MSC 60C05). https://arxiv.org/abs/1312.1211
3. M. Drmota and B. Gittenberger, *The distribution of nodes of given degree in random trees*, Journal of Graph Theory 31 (1999), 227–253. https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0118%28199907%2931%3A3%3C227%3A%3AAID-JGT6%3E3.0.CO%3B2-6
