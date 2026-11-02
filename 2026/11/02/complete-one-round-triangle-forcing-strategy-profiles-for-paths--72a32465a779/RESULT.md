# Complete one-round triangle-forcing strategy profiles for paths and cycles

## Finding

The degree-preserving Builder--Chooser triangle game begins with a finite simple graph \(G\). Builder first chooses a matching \(M\), deletes its edges, adds one new vertex adjacent to every endpoint of \(M\), and then assigns each edge of the resulting graph to one of two named parts. Chooser retains either part. A **winning one-round plan** is a matching together with such an ordered two-part edge assignment for which each part contains a triangle.

For each path \(P_n\) with \(n\ge2\) and each simple cycle \(C_n\) with \(n\ge4\), let \(W_{P_n}(y)\) and \(W_{C_n}(y)\) count matching choices that admit at least one winning edge assignment, weighted by \(y^{|M|}\). The following **closed rational generating functions** hold as formal power series:

\[
\sum_{n\ge2} W_{P_n}(y)x^{n-1}
=\frac{y^3x^5(1-x)}{(1-x-yx^2)(1-x-yx^3)^2},
\]
\[
\sum_{n\ge4} W_{C_n}(y)x^n
=\frac{x^4y^2(1-x)\left(2(1-x)^2+yx^3\right)}
{(1-x-yx^2)(1-x-yx^3)^2}.
\]

The formulas enumerate all successful matching choices, not merely optimal ones. For example, the initial winning-matching polynomials are
\[
W_{P_6}(y)=y^3,\quad W_{P_7}(y)=2y^3,\quad
W_{P_8}(y)=3y^3+y^4,
\]
\[
W_{C_4}(y)=2y^2,\quad W_{C_5}(y)=0,\quad
W_{C_6}(y)=2y^3,\quad W_{C_7}(y)=7y^3.
\]

There is also a complete two-parameter distribution and an exact count of the edge assignments themselves. For an initial matching \(M\), let \(h(M)\) denote the number of surviving edges between distinct matching edges after the growth operation, and let \(m=|E(G)|\). In a path or simple cycle every such edge is disjoint from the others, so the grown graph has exactly \(h(M)\) **edge-disjoint triangles**, sharing at most the new vertex. For every \(M\), the number of winning ordered two-part edge assignments equals
\[
\boxed{2^{m+|M|-3h(M)}\left(8^{h(M)}-2\cdot7^{h(M)}+6^{h(M)}\right).}
\]
In particular this expression vanishes precisely when \(h(M)<2\). Its sum over all matchings is the exact number of complete winning one-round plans (matching and ordered partition), without any further graph search.

Finally, if Builder chooses uniformly among **all** matchings of \(P_n\) or \(C_n\), and independently assigns every resulting edge to one of the two named parts with equal probability, the probability that the resulting one-round plan wins tends to \(1\) exponentially fast as \(n\to\infty\). More precisely, the failure probability is \(O(q^n)\) for \(q=\lambda_{7/8}/\varphi<1\), where \(\varphi=(1+\sqrt5)/2\) and \(\lambda_t\) is the largest positive real root of \(\lambda^3-\lambda^2-t\lambda-(1-t)=0\). Numerically \(q\approx0.986963\).

## Assumptions and scope

Graphs are finite, undirected, simple, and have labelled vertices and thus distinguishable edges. \(P_n\) is the path on \(n\) vertices for every \(n\ge2\). \(C_n\) is the cycle on \(n\) vertices for every \(n\ge4\); the triangle \(C_3\), which already contains the target at time zero, is excluded. Matchings include the empty matching. The two edge-assignment parts are named, and an edge belongs to exactly one part; empty parts are allowed but cannot be winning. In the probability statement the matching is uniform among all matchings, not conditioned on its size, and the partition is an independent uniform assignment of each surviving/grown edge. All generating-function identities are formal identities over integer coefficients, not assertions about an analytic domain.

For exact coefficients, define \(a_P(n,k,j)\) and \(a_C(n,k,j)\) to be the numbers of matchings with \(k\) edges and \(h(M)=j\). For \(k\ge1\),
\[
a_P(n,k,j)=\binom{k-1}{j}\binom{n-2k+1}{k-j}\qquad(0\le j<k),
\]
where out-of-range binomial coefficients are zero. For a cycle with \(n>2k\),
\[
a_C(n,k,j)=\frac nk\binom{k}{j}\binom{n-2k-1}{k-j-1}\qquad(0\le j<k).
\]
For \(n=2k\), the only nonzero cyclic coefficient with \(k\ge1\) is \(a_C(2k,k,k)=2\). In either graph the empty matching has \(a_G(n,0,0)=1\). All other coefficients are zero. Consequently,
\[
W_G(y)=\sum_{k\ge0}y^k\sum_{j\ge2}a_G(n,k,j),
\]
and the all-plan count is
\[
\mathcal S(G)=\sum_{k\ge0}\sum_{j\ge2}a_G(n,k,j)
2^{m+k-3j}(8^j-2\cdot7^j+6^j).
\]

## Proof

**1. Exact triangle structure.** Number the path edges consecutively, or the cycle edges cyclically. A matching has no two consecutive selected edges. Between two consecutive selected edges there is a unique *gap* of unselected edges (in the path, consider only internal gaps). An edge of the original graph outside the matching survives between two matching endpoints if and only if the corresponding gap contains **exactly one** unselected edge. Thus \(h(M)\) is the number of these unit gaps. Cross-edges from two distinct unit gaps cannot share an endpoint: each selected edge has one endpoint exposed to its preceding gap and its other endpoint exposed to its succeeding gap. The same holds for the two unit gaps of the alternating perfect matchings of \(C_4\). Since \(P_n\) and \(C_n\), for the stated ranges, are triangle-free, every triangle after the growth operation consists of the new vertex and exactly one cross-edge. These \(h(M)\) triangles are edge-disjoint.

**2. Winning condition and partition multiplicity.** A successful ordered edge assignment must contain a triangle in each part. Because all triangles are edge-disjoint, such an assignment exists exactly when \(h(M)\ge2\): put one full triangle in each part. There are \(m+k\) edges after replacing a matching of size \(k\). Each triangle has three edges and hence eight possible assignments. Among the \(8^j\) assignments on \(j\) disjoint triangles, the number exhibiting at least one entirely first-part triangle and at least one entirely second-part triangle is \(8^j-2\cdot7^j+6^j\) by inclusion--exclusion. The other \(m+k-3j\) edges can be assigned freely. This proves the partition formula, including the zero cases.

**3. Path gap counting.** For \(k\ge1\), write selected edge indices as \(i_1<\cdots<i_k\) with \(i_{r+1}-i_r\ge2\). Put \(g_r=i_{r+1}-i_r-2\ge0\) and let \(a=i_1-1\), \(b=n-1-i_k\). Then
\[
a+b+\sum_{r=1}^{k-1}g_r=n-2k.
\]
A unit cross-gap is exactly a zero \(g_r\). Choose the \(j\) zero positions; each of the other \(k-1-j\) gaps must be positive. Subtracting one from each positive gap leaves \(n-3k+1+j\) to distribute over \(k+1-j\) nonnegative variables (the adjusted gaps and two boundaries). Stars and bars gives \(a_P(n,k,j)\).

To obtain the path generating function, mark the number of unit gaps by \(t\), the matching size by \(y\), and the number of path edges by \(x\). A single positive internal gap contributes \(x/(1-x)\); a unit gap contributes \(t\). The two free boundary slacks contribute \((1-x)^{-2}\). Including the empty matching, the complete profile is given below; the auxiliary \(P_1\) is the one-vertex path and contributes only an empty matching:
\[
\sum_{n\ge1}\sum_M y^{|M|}t^{h(M)}x^{n-1}
=\frac1{1-x}+\frac{xy}{(1-x)^2}
\frac1{1-yx^2\left(t+\frac{x}{1-x}\right)}.
\]
Write \(A=yx^3/(1-x)\) and \(B=yx^2\). Keeping only powers \(t^j\) with \(j\ge2\) and then putting \(t=1\), the second term becomes
\[
\frac{xy}{(1-x)^2}\frac{B^2}{(1-A)^2(1-A-B)},
\]
which simplifies to the asserted rational path series.

**4. Cycle gap counting.** Fix a cyclically ordered list of \(k\ge1\) selected edges. Let \(g_1,\ldots,g_k\ge1\) be the numbers of unselected edges in the cyclic gaps. Then \(\sum g_i=n-k\). Choosing a distinguished selected edge gives \(n\) choices of its starting location, but each matching is thereby counted exactly \(k\) times. For \(j<k\), choose the \(j\) gaps equal to one, subtract two from each remaining gap, and distribute the surplus \(n-3k+j\). This gives \(a_C(n,k,j)\). If all \(k\) gaps equal one, then \(n=2k\) and precisely two alternating perfect matchings occur.

For the rational cyclic series, each gap contributes \(t x+x^2/(1-x)\), while the preceding selected edge contributes \(y x\). The standard distinguished-edge count therefore gives the nonempty matching series
\[
x\frac{\partial}{\partial x}
\left[-\log\left(1-yx\left(tx+\frac{x^2}{1-x}\right)\right)\right].
\]
In the formal logarithm, discard the terms with zero or one unit gap. Their complement is \(-\log(1-r)-r\) with
\[
r=\frac{yx^2(1-x)}{1-x-yx^3}.
\]
Differentiating gives \(xr r'/(1-r)\), which simplifies exactly to the claimed rational cycle series. Its initial term is \(2y^2x^4\), accounting for the two matchings of \(C_4\).

**5. Random-strategy robustness.** Conditional on \(h(M)=j\), a uniformly random ordered edge assignment succeeds with probability
\[
1-2(7/8)^j+(3/4)^j.
\]
For \(0\le t<1\), the complete matching profile at \(y=1\) has its dominant positive pole at the inverse of the positive root \(\lambda_t\) of \(\lambda^3-\lambda^2-t\lambda-(1-t)=0\). Indeed the common gap denominator simplifies to \(1-x-tx^2-(1-t)x^3\). The total number of matchings of \(P_n\) is \(F_{n+1}\), and of \(C_n\) is \(F_{n-1}+F_{n+1}\), both growing as a positive constant times \(\varphi^n\). For \(t<1\) the pole is strictly larger than \(\varphi^{-1}\), hence \(\lambda_t<\varphi\). The failure probability is at most \(2\mathbb E[(7/8)^{h(M)}]\), which is \(O((\lambda_{7/8}/\varphi)^n)\) for either graph family. No conjectured statement is needed.

## Verification

The included standalone standard-library program `verify.py` reconstructs every labelled path and cycle in the ranges \(2\le n\le16\) and \(4\le n\le16\), enumerates all their matchings, constructs the graph after the growth step, and counts the resulting triangles. It checks every \((k,j)\) coefficient against the two closed formulas and checks the two rational generating functions at four separate integer substitutions. For smaller graphs it also enumerates every ordered two-part edge assignment directly and compares against the partition formula. Its output from an actual execution is:

```text
ALL_MATCHING_PROFILES_OK 28 graph_cases 9945 matchings
PARTITION_COUNT_CHECKS_OK 198 matchings 85 full_exhaustions 113 zero_triangle_shortcuts
RATIONAL_GENERATING_FUNCTIONS_OK 112 specializations
VERIFY_OK
```

For 85 matching choices with at least one triangle, every two-colour edge assignment is enumerated; the other 113 small-graph matching choices have no triangle and therefore admit no successful partition. These are finite consistency checks; the unrestricted results are established by the proof above.

## Relationship to prior work

András London's *A Degree-Preserving Builder--Chooser Game*, arXiv:2605.26695v1 (first posted 2026-05-26 UTC), defines this exact game and proves the one-round criterion for triangle-free seed graphs using the matching number of cross-edges. In particular, its Corollary 3.2 and Theorem 3.3 give the **existence thresholds** for paths and cycles. Those results and the edge-disjoint-triangle forcing mechanism are prior work, not newly claimed here. The present formulas quantify **every growth matching and every winning binary edge assignment**, and establish a random-strategy success law that does not follow from the threshold statements alone without further counting.

The Goulden--Jackson cluster method and its weighted-word extensions provide general tools for counting specified patterns in words. Their applicability to binary encodings is acknowledged. The specific path/cycle game-dependent profiles, two-part winning assignment multiplicities, and exponential random-strategy conclusion are the results claimed here; no claim of inventing pattern-counting methods is made.

## Limitations

The count concerns the exact degree-preserving matching-replacement rule, the triangle target, and **one round** only. It is not a formula for forcing larger cliques, general tree seeds, arbitrary graph families, or multi-round optimal play. The two assignment parts are ordered/named; an unordered partition count requires handling the interchange of part names separately. The asymptotic assertion uses uniform random matchings of all sizes and independently fair binary edge assignments; other sampling distributions may behave differently. As with any literature comparison, previously unindexed equivalent results cannot be ruled out by search alone.

## References

1. A. London, *A Degree-Preserving Builder--Chooser Game*, arXiv:2605.26695v1, 2026-05-26. https://arxiv.org/abs/2605.26695 ; full manuscript https://arxiv.org/pdf/2605.26695 . Particularly Definition 2.1 and Theorem 3.1, Corollary 3.2, Theorem 3.3.
2. I. P. Goulden and D. M. Jackson, *An Inversion Theorem for Cluster Decompositions of Sequences with Distinguished Subsequences*, Journal of the London Mathematical Society (2), 20 (1979), 567--576. https://doi.org/10.1112/jlms/s2-20.3.567 .
3. E. J. Kupin and D. S. Yuster, *Generalizations of the Goulden--Jackson cluster method*, Journal of Difference Equations and Applications 16 (2010), 1463--1480. https://doi.org/10.1080/10236190902841976 .
