# Complete self-inverse rank enumerator for finite wheel partial-isometry monoids

## Finding
For every integer \(n\ge5\), the rank-generating polynomial of all self-inverse partial distance-preserving injections of the wheel graph \(W_n\) is given by
\[
\boxed{J_n(z)=(1+z)F_n(z)+n(z^2+2z^3+2z^4).}
\]
Here \(F_n(z)\) is an explicit finite partition sum defined below. It counts involutive partial isometries supported entirely on the rim. In particular, the hub-exchanging contributions occur only in ranks two, three, and four. This is an enumeration of all involutions of the **inverse monoid**, including the empty map and the partial identities; it is not merely the number of involutions of its unit group.

## Assumptions and scope
Let \(W_n\) have vertex set \(\{0,1,\ldots,n\}\), hub \(0\), all spokes \(\{0,i\}\), and rim edges \(\{i,i+1\}\) with the rim indices reduced modulo \(n\). Distances are shortest-path distances in **the wheel**, not shortest-path distances in the cycle alone. Let \(\operatorname{PIso}(W_n)\) be the monoid of partial injections preserving those pairwise distances. Its inverse operation is the ordinary inverse partial bijection. Set
\[
J_n(z)=\sum_{\substack{\alpha\in\operatorname{PIso}(W_n)\\\alpha=\alpha^{-1}}}z^{|\operatorname{dom}(\alpha)|}.
\]
For any positive integer \(j\), set \(a_1=1\) and \(a_j=2\) when \(j\ge2\). For each nonnegative integer \(m\), put
\[
I_j(m)=\sum_{t=0}^{\lfloor m/2\rfloor}\frac{m!}{2^t t!(m-2t)!}\,a_j^{m-t}.
\]
For \(1\le k\le n-1\), define
\[
f_{n,k}=\sum_{\substack{m_1,\ldots,m_k\ge0;\;\sum_{j=1}^{k}jm_j=k\\r:=\sum_{j=1}^{k}m_j,\;1\le r\le n-k}}
\frac{n(r-1)!}{\prod_{j=1}^{k}m_j!}\binom{n-k-1}{r-1}
\prod_{j=1}^{k}I_j(m_j).
\]
Thus \(r\) is the number of connected components of the induced rim subgraph. Define the polynomial
\[
F_n(z)=1+\sum_{k=1}^{n-1}f_{n,k}z^k+
\left(n+1+\mathbf 1_{2\mid n}\right)z^n.
\]
All summations are finite; the summand at given \(k\) is taken only for feasible multiplicities satisfying the displayed inequalities. The polynomial \(F_n(z)\) depends on the **induced cycle adjacency** on rim subsets, not on the metric of the original cycle.

## Proof
**1. The rim-only case.** In a wheel, distinct rim vertices are at wheel distance one if adjacent on the rim and two otherwise. A self-inverse partial injection has the same domain and image, say \(S\). When \(0\notin S\), preservation of wheel distances is therefore equivalent to the map being an involutive automorphism of the induced graph \(C_n[S]\).

For any proper nonempty rim subset \(S\) of cardinality \(k\), the induced graph \(C_n[S]\) is a disjoint union of paths. Let \(m_j\) be the number of path components on exactly \(j\) vertices, so that \(\sum_j jm_j=k\) and \(r=\sum_jm_j\). There are \(n-k\) omitted rim vertices, and the component run count obeys \(r\le n-k\).

The number of such **labeled** rim subsets with fixed component multiplicities is
\[
N_n(m_1,\ldots,m_k)=\frac{n(r-1)!}{\prod_{j=1}^{k}m_j!}\binom{n-k-1}{r-1}.
\]
Indeed, choose an oriented start vertex for one of the \(r\) cyclic one-runs (\(n\) possibilities), choose the cyclic ordering of the component lengths (\(r!/\prod_jm_j!\) possibilities), and distribute the \(n-k\) omitted vertices as positive gaps among those \(r\) runs (\(\binom{n-k-1}{r-1}\) possibilities). Each labeled subset is counted exactly \(r\) times by the marked choice of starting run, giving the stated factor.

Path automorphisms have \(a_j\) choices, with \(a_1=1\) and \(a_j=2\) for \(j\ge2\). An involution of the disjoint union permutes its equal-length path components by an involution. For \(m\) components of length \(j\), choosing \(t\) transposed pairs takes \(m!/(2^tt!(m-2t)!)\) choices. For each fixed component choose one of its \(a_j\) involutive internal automorphisms; for each transposed pair choose one of the \(a_j\) isomorphisms in the forward direction, with the reverse direction then forced. Thus the factor is exactly \(I_j(m)\). Components of different lengths cannot be mixed, so the number for a fixed \(S\) is \(\prod_jI_j(m_j)\). Summing over the labeled rim subsets gives \(f_{n,k}\).

For the empty rim subset, there is only the empty map. For the entire rim, its automorphism group is dihedral of order \(2n\). That group has one identity, \(n\) reflections, and an additional involutive half-turn exactly when \(n\) is even. The coefficient of \(z^n\) in \(F_n(z)\) is therefore \(n+1+\mathbf1_{2\mid n}\). This completes the proof that \(F_n\) counts the rim-only case.

**2. The fixed-hub case.** If \(0\) lies in the domain of a self-inverse partial isometry and is fixed, deleting it leaves an arbitrary involutive partial isometry supported in the rim. Conversely every such rim-only involution extends uniquely by fixing the hub, because all hub-to-rim distances are one. Consequently the combined contribution of the maps omitting or fixing the hub is \((1+z)F_n(z)\).

**3. The exchanged-hub case.** It remains to consider \(\alpha(0)=v\ne0\). Since \(\alpha=\alpha^{-1}\), necessarily \(\alpha(v)=0\). For any other vertex \(x\) in its invariant domain, preservation of both \(d(0,x)=1\) and \(d(v,x)=1\) forces \(x\) and its image to lie among the two rim neighbors of \(v\). The restriction to any chosen subset of those two neighbors may be any involution: there is one on the empty subset, two on one-vertex subsets altogether, and two on the entire two-vertex subset. Each such partial involution preserves all wheel distances: both neighbors are adjacent to \(v\) and to the hub, and exchanging them preserves their mutual distance. For each choice of \(v\), the rank contribution is
\[
z^2(1+2z+2z^2).
\]
These cases are disjoint over the \(n\) rim choices of \(v\), and disjoint from the rim-only and hub-fixed cases. Their sum is \(n(z^2+2z^3+2z^4)\), proving the formula for every \(n\ge5\).

## Verification
The included standalone `wheel_self_inverse_checker.py` uses only Python's standard library. It independently enumerates every involutive partial permutation of each wheel vertex subset and verifies preservation of every pairwise wheel distance. It compares the resulting full rank vectors to the integer-partition formula for every integer \(3\le n\le9\); all comparisons passed. The theorem is stated for \(n\ge5\) in the studied wheel family, while the small additional test cases exercise boundary behavior.

For example, for \(n=5\) the vector of coefficients of \(J_5(z)\), in order of ranks zero through six, is \((1,6,30,50,40,16,6)\). For \(n=7\) the vector is \((1,8,56,140,210,168,70,22,8)\). The total number of involutive partial isometries for these two instances is \(149\) and \(683\), respectively. Invoke `python wheel_self_inverse_checker.py` to reproduce the comparisons; exhaustive experiments serve as independent finite checks, not as a proof for all \(n\).

## Relationship to prior work
Fernandes, *On the monoid of partial isometries of a wheel graph* (arXiv:2307.16257; first posted 30 July 2023), defined and analyzed this inverse monoid, determined its Green relations, and its generating rank. It does not state the present involution-rank enumerator, which instead uses induced-path automorphism groups and cyclic run enumeration. Jajcay, Jajcayová, Szakács and Szendrei, *Inverse monoids of partial graph automorphisms* (arXiv:1809.04422), describe the structure and characterization of the general inverse monoids of partial graph automorphisms but do not provide these wheel involution coefficients. Fernandes and Paulista's work on partial isometries of a **cycle with the cycle's own metric** describes dihedral restrictions; the wheel rim's metric is different for longer cycles, and the wheel involution classes include additional hub-swapping maps.

## Limitations
This establishes exactly the involution-rank polynomial of the wheel monoid, not the rank distribution of all partial isometries, nor their commuting-pair enumerator. The general formula is proved combinatorially; finite exhaustive checks only test the stated small values. Literature inspection does not exclude the possibility of an unindexed or independently obtained equivalent counting formula.

## References
1. V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257 (2023), DOI: 10.1142/S1793557123502388. https://arxiv.org/abs/2307.16257
2. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (2018). https://arxiv.org/abs/1809.04422
3. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics 47 (2023), 1746–1760, DOI: 10.55730/1300-0098.3460. https://journals.tubitak.gov.tr/math/vol47/iss6/10/
