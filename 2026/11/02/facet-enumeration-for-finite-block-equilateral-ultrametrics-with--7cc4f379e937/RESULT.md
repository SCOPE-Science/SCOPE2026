# Facet enumeration for finite block-equilateral ultrametrics with independent cluster scales

## Finding

Let \(k\ge2\), and partition a finite set \(M=A_1\sqcup\cdots\sqcup A_k\) into nonempty clusters of cardinalities \(m_i=|A_i|\ge1\). Choose independent real parameters \(0<t_i<1\), and define
\[
d(x,y)=\begin{cases}
0,&x=y,\\
t_i,&x\ne y\text{ and }x,y\in A_i,\\
1,&x\in A_i,\ y\in A_j,\ i\ne j.
\end{cases}
\]
The real Lipschitz-free unit ball has exactly
\[
\boxed{F(M,d)=(2^k-2)\prod_{i=1}^{k}(2^{m_i}-1)}
\]
facets, for *every* independent choice of cluster scales. More precisely, its dual unit ball has the following complete vertex classification, modulo common additive constants. Split the clusters into a nonempty lower class and a nonempty upper class. In each lower cluster \(A_i\), choose a nonempty set of anchor points at potential \(0\) and give all its remaining points potential \(t_i\). In each upper cluster \(A_i\), choose a nonempty set of anchors at potential \(1\) and give its remaining points potential \(1-t_i\). These, and only these, are the extreme potentials. Every choice gives a different vertex.

At the simultaneous equilateral endpoint \(t_1=\cdots=t_k=1\), the count is \(2^N-2\), where \(N=\sum_i m_i\). For the natural example of two three-point clusters, the count is \(98\) throughout the strict parameter region, compared with \(62\) at the equilateral endpoint. The formula includes the previously treated disjoint-pair special case but applies to clusters of arbitrary cardinality and independent positive scales.

## Assumptions and scope

The metric is an ultrametric: distances within each equilateral cluster are strictly less than the common cross-cluster distance, and the strong triangle inequality follows by inspecting whether a triple meets one or more clusters. We work over real scalars, with a fixed but arbitrary basepoint \(o\in M\). Put
\[
P=\{f:M\to\mathbb R:f(o)=0,\ |f(x)-f(y)|\le d(x,y)\ \text{for all }x,y\in M\}.
\]
It is the dual unit ball of \(\mathcal F(M,d)\), a full-dimensional polytope of dimension \(N-1\) containing \(0\) in its interior. Vertices of \(P\) are in bijection with facets of the polar primal unit ball. We may translate any potential by a common constant and then renormalize it at \(o\).

## Proof

**Tight-edge criterion.** Given a feasible potential \(f\), let \(G_f\) be the undirected graph on \(M\) with an edge \(xy\) precisely when \(|f(x)-f(y)|=d(x,y)\). The active linear constraint rows are signed incidence vectors of these edges, whose span modulo constants has rank \(N-c(G_f)\), where \(c(G_f)\) is the number of connected components. Thus an extreme potential is exactly a feasible potential with \(G_f\) connected. This may also be seen directly: connected tight edges force all increments of two midpoint summands, while a disconnected tight graph permits a sufficiently small perturbation of one component that misses the basepoint, preserving all finitely many strict cross-component inequalities.

**The two global anchor values.** A connected tight graph must contain an edge between distinct clusters, since \(k\ge2\). Such an edge has metric length \(1\), so the potential oscillates by at least \(1\). But every pair of points in \(M\) has distance at most \(1\), hence \(\max f-\min f=1\). Subtract the minimum, putting all potential values in \([0,1]\) and attaining both endpoints. Every tight cross-cluster edge must join one potential \(0\) and one potential \(1\); there are no other tight cross-cluster edges.

**Exhausting the clusters.** Each cluster \(A_i\) must contain at least one endpoint value \(0\) or \(1\). Otherwise it has no tight edge to any other cluster; as the tight graph is connected and there are at least two clusters, this is impossible. No cluster can contain both \(0\) and \(1\), because its diameter is \(t_i<1\). Call a cluster with a zero a *lower* cluster and one with a one an *upper* cluster.

All values in a lower cluster belong to \([0,t_i]\), because a zero is present. A point with value strictly between \(0\) and \(t_i\) cannot be incident to a tight intra-cluster edge (all intra-cluster potential differences are then strictly less than \(t_i\)); it cannot be incident to a tight cross-cluster edge either, since such an edge joins values \(0\) and \(1\). That point would be isolated, contradicting connectedness. Thus every lower-cluster value is \(0\) or \(t_i\), and at least one value is \(0\). The symmetric argument shows that every upper-cluster value is \(1-t_i\) or \(1\), with at least one value \(1\). At least one cluster is lower and one upper, since the global values \(0\) and \(1\) must occur and cannot occur in the same cluster.

**Sufficiency.** Conversely, choose any such lower/upper partition and any nonempty anchor subset within every cluster. All potentials lie in \([0,1]\), so cross-cluster differences are at most \(1\); within a cluster, the only possible nonzero difference is \(t_i\), so all its metric constraints hold. Every zero-anchor is tightly joined to every one-anchor in a different cluster, forming a connected complete bipartite core. Any nonanchor lies at the opposite value within its own cluster, and is tightly joined to each of that cluster's anchors by an edge of length \(t_i\). Hence the tight graph is connected and the potential is extreme.

**Counting and uniqueness.** There are \(2^k-2\) ways to choose nonempty lower and upper sets of clusters. Conditional on the type of cluster \(A_i\), its nonempty anchor set may be chosen in exactly \(2^{m_i}-1\) ways; all other local values are forced. Each resulting potential has global minimum \(0\) and maximum \(1\). Its lower/upper cluster types and anchor sets can be recovered from its values, because \(0<t_i<1\). Thus distinct choices are not related by additive constants, and the number of vertices of \(P\), hence facets of the polar free-space ball, is the stated product.

**Equilateral endpoint.** If all \(t_i\) reach \(1\), every pair of distinct points has distance one. The same criterion shows that its dual vertices are precisely the nonconstant \(\{0,1\}\)-valued potentials modulo constants, giving \(2^N-2\) facets. This endpoint statement is already classical and is included solely for the geometric comparison.

## Verification

The standalone standard-library file `ultrametric_cluster_facets_checker.py` independently enumerates all dual vertices for ten small rational test metrics and reconstructs the claimed state set. In every test, each scale is a positive multiple of \(1/4\) below one; after setting \(f(o)=0\), all vertices must lie on the quarter-grid because their tight graph has a spanning tree and all tight differences are quarter-integral. Every coordinate lies between \(-1\) and \(1\), giving a finite exhaustive grid for these exact cases. The checker tests all metric inequalities, the exact tight-graph connectivity criterion, and equality with the predicted list. It prints `ALL_EXACT_CASES_PASS: 10`. Heterogeneous parameters and clusters of size three are included, notably \((m_1,m_2)=(3,3)\) with lengths \((1/4,3/4)\). Run with `python ultrametric_cluster_facets_checker.py`.

This finite enumeration tests the implementation of the classification only on the listed rational instances. The proof above, rather than enumeration, establishes the result for every positive integer cluster size and every real \(0<t_i<1\).

## Relationship to prior work

Montrucchio and Pistone characterize dual extreme Lipschitz potentials for general finite metric spaces via paths of tight edges (Theorem 3.1), and treat the equilateral metric in Proposition 5. These results justify the framework but do not enumerate independently scaled clusters of arbitrary size. Gordon and Petrov give structural tight-graph arguments and explicit face numbers for *generic* metrics; the highly degenerate clustered ultrametrics here are not in their generic regime. Aliaga characterizes extreme molecules in the *primal* Lipschitz-free ball; this is distinct from counting facets through extreme *dual* functionals.

A separately published count for an equilateral metric with independently shortened disjoint pairs is recovered when every cluster has cardinality one or two: if there are \(r\) pairs among \(N\) points, then \(k=N-r\), and the displayed formula becomes \(3^r(2^{N-r}-2)\). The disjoint-pair theorem and its proof are prior work, **not** claimed as new. Here the clusters may instead be cliques of arbitrary size, with overlapping short edges inside each cluster; every intra-cluster length can also vary independently of those of other clusters. Previously studied complete-multipartite metrics use *longer* same-part distances \(1<t<2\), whereas the present metrics have *shorter* same-part distances \(0<t_i<1\); the former formulas do not imply this result. The proposed addition is the uniform all-cluster facet count and complete dual state classification across this new natural family.

## Limitations

The statement concerns finite real Lipschitz-free spaces, at least two nonempty clusters, internal equilateral distances, and a common cross-cluster distance, normalized to one. It does not determine all face numbers or cover nested multilevel ultrametrics with non-equilateral clusters. The prior disjoint-pair special case and the equilateral endpoint are not originality claims. The method relies on the standard tight-graph criterion; originality pertains to the exhaustive cluster classification and product count. A previously unindexed equivalent generalization remains a bibliographic risk; independent scientific assessment has not been performed.

## References

- R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first publicly available 2021-02-01. https://arxiv.org/abs/2102.01219
- J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848 (2016), Sections 1–2. https://arxiv.org/abs/1608.06848
- L. Montrucchio and G. Pistone, *Kantorovich distance on a finite metric space*, arXiv:1905.07547 (2019), Theorem 3.1 and Proposition 5. https://arxiv.org/abs/1905.07547
- M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019). https://arxiv.org/abs/1911.10642
- *Facet enumeration for equilateral metrics with independently shortened pairs*, published mathematical record, October 2026; its precise pair special case and scope are compared in the preceding section.
- *Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls*, published mathematical record, October 2026; treats the complementary interval with longer intra-cluster distances.
