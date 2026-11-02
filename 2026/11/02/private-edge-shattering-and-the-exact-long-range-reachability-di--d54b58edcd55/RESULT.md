# Private-edge shattering and the exact long-range reachability dimension of paths

## Finding

Let \(T\) be a finite undirected tree with vertex set \(V(T)\). For each orientation \(\omega\) of **all** edges of \(T\), define the Boolean function \(h_\omega(u,v)\) to be \(1\) precisely when \(\omega\) contains a directed path from \(u\) to \(v\). The possible queries are ordered pairs of distinct vertices. A query support \(Q\) is *shattered* when every binary assignment on its members equals the restriction of some \(h_\omega\).

**Tree shattering theorem.** A finite set \(Q\) of ordered-pair reachability queries is shattered by the family of all edge orientations of \(T\) if and only if both conditions hold:

1. *Directional compatibility:* whenever the unique undirected paths of two queries share an edge, they traverse that edge in the same direction.
2. *Private-edge condition:* the undirected path of each query in \(Q\) contains an edge belonging to no path of any other query in \(Q\).

For the path \(P_{m+1}\) on \(m+1\) vertices, restrict the query domain to ordered pairs at graph distance at least \(d\), where \(m\ge1\) and \(1\le d\le m\). Write \(m=q(d+1)+r\) with integers \(q\ge0\) and \(0\le r\le d\). Then the exact VC dimension of the resulting orientation-reachability concept class is

\[
\boxed{\operatorname{VCdim}(P_{m+1};d)=2q+\mathbf 1_{\{r=d\}}.}
\]

In particular, distance at least two yields \(2\lfloor m/3\rfloor+\mathbf 1_{\{m\bmod 3=2\}}\), while permitting neighboring vertices (\(d=1\)) yields dimension \(m\). The formulas concern the fixed undirected skeleton with arbitrary edge orientations; they make no claim about graph reconstruction when the skeleton is unknown.

## Assumptions and scope

All graphs are finite and simple. An orientation independently chooses one of the two directions on each edge. Directed reachability is interpreted through a nonempty directed path; queries always involve distinct vertices. An empty support is shattered. The distance restriction is imposed on the *undirected* path skeleton, not on a randomly selected orientation. The main equivalence holds for every finite tree and every subset of its ordered-pair queries. The explicit dimension formula holds for an undirected path of \(m\) edges and integer thresholds \(1\le d\le m\). A singleton tree has no allowed query and dimension zero.

## Proof

**Proof of the tree criterion.** Each ordered pair \((u,v)\) has one simple undirected path \(P_{uv}\). Since the skeleton is a tree, \(h_\omega(u,v)=1\) if and only if every edge on \(P_{uv}\) is oriented from \(u\) toward \(v\). If \(Q\) is shattered, its all-one labeling is feasible. Therefore all query paths prescribe mutually consistent directions on shared edges. Fix a member \(a\in Q\), and use shattering to realize the labeling in which every member other than \(a\) is positive and \(a\) is negative. If every edge of \(P_a\) belonged to some other member's path, those positive members would force all of \(P_a\) to point in the positive direction, a contradiction. Hence \(P_a\) has a private edge.

Conversely assume both conditions. There is a consistent partial orientation realizing all members positively. For any desired binary labeling of \(Q\), preserve the prescribed positive orientation on every edge used by a positive member; for each negative member choose one of its private edges and orient it oppositely to the direction requested by that member. These chosen private edges are distinct and lie on no other query path. Complete all still-unoriented edges arbitrarily. Then every positive query is true and each negative query is false. Every labeling is realized, proving the equivalence.

**Interval lemma.** Consider \(k\ge1\) distinct integer intervals contained in \(\{1,\ldots,m\}\), each having at least \(d\) points, with at least one private point per interval. None is contained in another: a contained interval could have no private point. Consequently, after ordering by left endpoints, both left endpoints \(L_1<\cdots<L_k\) and right endpoints \(R_1<\cdots<R_k\) are strictly increasing. For every \(i\le k-2\), interval \(i+1\) must possess a point outside the union of intervals \(i\) and \(i+2\). Otherwise it could have no private point. Hence \(L_{i+2}\ge R_i+2\), and thus

\[
R_{i+2}\ge R_i+d+1.
\]

As \(R_1\ge d\) and (when \(k\ge2\)) \(R_2\ge d+1\), induction gives

\[
R_{2s}\ge s(d+1),\qquad R_{2s+1}\ge s(d+1)+d.
\]

Every right endpoint is at most \(m\). Therefore the number of intervals is at most \(2q+\mathbf 1_{\{r=d\}}\), where \(m=q(d+1)+r\) and \(0\le r\le d\). This argument also covers \(k=1\); there are no intervals if \(m<d\).

**Sharp construction.** Divide the first \(q(d+1)\) path edges into \(q\) consecutive blocks of \(d+1\) edges. Within each block take the two intervals of \(d\) edges starting at its first and second edges. The first has its first edge private; the second has its last edge private. Intervals from different blocks have disjoint edges. If \(r=d\), add the interval consisting of the final \(d\) edges, which is disjoint from the previous blocks. Orient the entire skeleton consistently from left to right, and use the left-to-right ordered-pair queries associated with these intervals. Directional compatibility and private edges hold. By the tree criterion, the resulting \(2q+\mathbf 1_{\{r=d\}}\) queries are shattered. Together with the interval lemma this proves the formula for every admissible \(m,d\).

## Verification

The attached standalone Python 3 program `verify.py` reconstructs reachability truth tables by direct enumeration of all orientations on small trees, compares literal shattering with the two-condition path criterion on 22,332 support instances, and independently optimizes the private-point interval problem for all 28 parameter pairs \(2\le d\le m\le8\). It reproduces the final message `ALL_TREE_REACHABILITY_CHECKS_PASS`. The program makes no appeal to the proof to generate the literal orientation truth tables. Its finite checks corroborate but do not replace the unrestricted argument above. Execute from the directory containing the file using `python3 verify.py`.

## Relationship to prior work

The ordered-pair path-query model is studied in Janardhanan and Reyzin, *On Learning a Hidden Directed Graph with Path Queries*, arXiv:2002.11541 (first publicly posted 2020-02-26), with an emphasis on hidden-graph reconstruction. Their Section 2 defines the Boolean reachability query and Sections 3.1–3.2 study query complexity for strongly connected components and directed rooted almost-trees. Their inspected text does not provide the shattering characterization for all orientations of a known undirected tree, or the distance-threshold VC formula for paths. Wang and Honorio, *Reconstructing a Bounded-Degree Directed Tree Using Path Queries*, arXiv:1606.05183 (2016), precedes this work on reconstruction of directed rooted trees and is relevant background; it is not identified as establishing the present capacity result.

The interval lemma is a statement about irredundant interval systems with prescribed minimum cardinality, but its direct use here crucially involves an all-one feasibility constraint across directed reachability predicates. The exact capacity formula is not an implication of generic VC bounds, of path-query reconstruction algorithms, or of the standard VC dimension of the interval set system in which *intervals themselves* are hypotheses (a distinct dual viewpoint).

## Limitations

The exact formula is proved only for a **path skeleton**; the general tree result is a criterion for individual shattered supports, not a closed VC formula for every tree and distance threshold. The proof considers static VC shattering, not Littlestone dimension or worst-case adaptive reconstruction query complexity. Historical priority remains subject to broader human verification; no claim of formal independent certification is made.

## References

1. M. V. Janardhanan and L. Reyzin, *On Learning a Hidden Directed Graph with Path Queries*, arXiv:2002.11541, first submitted 2020-02-26. https://arxiv.org/abs/2002.11541
2. Z. Wang and J. Honorio, *Reconstructing a Bounded-Degree Directed Tree Using Path Queries*, arXiv:1606.05183, first submitted 2016-06-16. https://arxiv.org/abs/1606.05183
3. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia and G. J. Woeginger, *VC-Dimensions for Graphs*, Technical Report TR-255 (1994), https://carleton.ca/scs/research/scs-technical-reports/technical-reports-1994/tr-255-vc-dimensions-for-graphs/ (different path-set system).
