# Geodesic-transversal polynomials of two-row ladders and the six-rung minimality transition

## Finding
Let \(L_n=P_n\square K_2\) be the labeled two-row ladder with \(n\ge2\) columns. Write \(\mathcal T_n(z)=\sum_{S\text{ transversal}}z^{|S|}\) and \(\mathcal M_n(z)=\sum_{S\text{ inclusion-minimal transversal}}z^{|S|}\), where transversals meet every inclusion-maximal geodesic. Then
\[
\mathcal T_n(z)=\big((1+z)^n-1\big)^2+2z^2(1+z)^{n-2}-2z^2\sum_{j=0}^{n-3}(j+1)(1+z)^j,
\]
where a sum whose upper limit is negative is empty. Moreover,
\[
\boxed{\mathcal M_n(z)=3nz^2+\mathbf1_{n\ge6}\frac{n(n-4)(n-5)}3 z^3.}
\]
Every inclusion-minimal transversal has size two if \(2\le n\le5\), and has size two or three if \(n\ge6\). There are exactly \(3n\) minimum transversals, while the number of inclusion-minimal triples is \(n(n-4)(n-5)/3\) when \(n\ge6\). The minimum transversal number is \(2\) for all \(n\ge2\).

## Assumptions and scope
The graph is finite, unweighted, simple and undirected. Its vertices are \(B_1,\dots,B_n\) in one row and \(T_1,\dots,T_n\) in the other; successive vertices in each row and opposite-row vertices of the same column are adjacent. A geodesic is a shortest path between its endpoints. It is maximal if it is not a proper subpath of a longer geodesic (maximality is by path containment, not by length). A transversal is a labeled vertex subset intersecting each maximal geodesic. Inclusion-minimality is with respect to deleting any selected vertex. Empty sums are zero.

## Proof
**1. All maximal geodesics.** A shortest path changes rows at most once, since each row change has a separate unit cost and a second change can be deleted; its column coordinate changes monotonically because the path uses the minimum horizontal distance. Any such path extends to a geodesic from opposite corners unless it already has endpoints at opposite corners. In particular, it can extend horizontally to column \(1\) on one row and column \(n\) on the other; if the path stays in one row, extend it further by a rung at one extremity. Conversely, every opposite-corner shortest path of length \(n\) is maximal, since \(n\) is the diameter. Thus the complete maximal-geodesic family consists of exactly \(2n\) paths, indexed by the choice of starting row and the unique rung column \(c\in\{1,\dots,n\}\):
\[
B_1,B_2,\ldots,B_c,T_c,T_{c+1},\ldots,T_n,
\]
and their row-swapped analogues. The statements remain valid for the four-cycle \(L_2\).

**2. A boundary criterion.** For a candidate set \(S\), define \(b_-=\min\{i:B_i\in S\}\), \(b_+=\max\{i:B_i\in S\}\) and similarly \(t_-,t_+\). Adopt \(\min\varnothing=n+1\) and \(\max\varnothing=0\). A path of the first displayed type misses \(S\) precisely when some switching column \(c\) satisfies \(t_+<c<b_-\). Such an integer exists exactly if \(b_-\ge t_++2\). The symmetric paths have the analogous obstruction. Therefore, for every \(S\subseteq V(L_n)\),
\[
S\text{ is a transversal}\iff b_-\le t_++1\quad\text{and}\quad t_-\le b_++1.
\]

**3. Counting all transversals.** Suppose both rows are represented. The total subset polynomial before imposing the inequalities is \(\big((1+z)^n-1\big)^2\). The two failure events are disjoint: both \(b_-\ge t_++2\) and \(t_-\ge b_++2\) cannot hold for two nonempty rows. In the first failure event fix \(t_+=t\) and \(b_-=b\), with \(1\le t<b-1\le n-1\). The two forced selected vertices contribute \(z^2\); arbitrary other selections occur only in the first \(t-1\) top positions and the last \(n-b\) bottom positions. Summation gives \(z^2\sum_{j=0}^{n-3}(j+1)(1+z)^j\) (for each exponent \(j\) there are exactly \(j+1\) pairs \((t,b)\)). The other failure event contributes identically. When only one row is represented, the boundary criterion requires selecting both endpoint vertices of that row, yielding \(2z^2(1+z)^{n-2}\). Adding gives \(\mathcal T_n(z)\).

**4. Classifying minimal transversals.** No single vertex is a transversal, since each vertex is omitted by at least one maximal geodesic. For a mixed-row pair \(\{B_i,T_j\}\), the boundary criterion reduces exactly to \(|i-j|\le1\). These give \(n+2(n-1)=3n-2\) minimal pairs. Two same-row vertices form a transversal only if they are the two endpoint vertices of that row, giving two more minimal pairs. Hence exactly \(3n\) minimal pairs.

Now let \(S\) be a transversal with no transversal pair. It has vertices in both rows (otherwise the endpoints in one row form a transversal pair). Choose the smallest selected column in either row, relabeling rows if needed to make it \(B_i\). Since no cross-row pair is a transversal, the first selected top vertex \(T_k\) satisfies \(k\ge i+2\). The boundary criterion forces some selected bottom vertex \(B_j\) with \(j\ge k-1\). Since \(|j-k|\le1\) would give a transversal pair, in fact \(j\ge k+2\). The triple \(\{B_i,T_k,B_j\}\) therefore satisfies \(i+2\le k\le j-2\), so it is a transversal by the boundary criterion; its proper two-element subsets are not. Furthermore \((i,j)\ne(1,n)\), since that would itself be a transversal pair. Conversely, for every \(1\le i<j\le n\) and \(i+2\le k\le j-2\) with \((i,j)\ne(1,n)\), the triple \(\{B_i,T_k,B_j\}\) is inclusion-minimal; likewise with rows swapped. Every transversal contains one of these pairs or triples, proving the exhaustive inclusion-minimal classification and absence of larger minimal sets.

For a fixed choice of the doubled row, the number of integer triples \(i<k<j\) with both consecutive gaps at least two is \(\binom{n-2}{3}\), by subtracting \(0,1,2\) from their increasing positions. Among them exactly \(n-4\) have \((i,j)=(1,n)\) when \(n\ge5\); these are excluded. Thus for \(n\ge6\) the number of minimal triples is
\[
2\left(\binom{n-2}{3}-(n-4)\right)=\frac{n(n-4)(n-5)}3.
\]
For \(2\le n\le5\) there are no such triples, as is immediate from the spacing and endpoint restrictions. The claimed \(\mathcal M_n(z)\), transition, and minimum value follow.

## Verification
Run the accompanying standard-library-only program `verify_ladder.py` with `python3 verify_ladder.py`. It builds the graph from its adjacency lists, enumerates all graph-metric shortest paths by breadth-first search, retains precisely those which are not properly contained in a longer shortest path, and checks every vertex subset for \(2\le n\le8\) against the boundary criterion, the all-set polynomial and the minimal-set polynomial. Its observed output was `ALL_LADDER_CHECKS_PASS orders=2..8 graphs= 7 successful_sets= 85577 maximal_geodesics=2n`. These finite checks do not prove the universal identities; the four proof steps above do.

## Relationship to prior work
Manuel, Brešar and Klavžar introduced the maximal-geodesic hitting-set invariant and proved general complexity results and scalar formulas for other families. Their original article does not supply the two-row ladder all-set or inclusion-minimal enumerators. The later geodesic-packing article examines packing-versus-transversal extremal comparisons, especially rook graphs and other graph products, not the present ladder polynomial. Published work on graph geodesics and indexed results about ladder matching complexes or ladder graph domination concern different hypergraphs or constraints; their statements do not imply the enumeration here. The new element is the exact boundary characterization, both polynomials, and the six-rung threshold for nonminimum inclusion-minimal solutions.

## Limitations
The claim concerns standard two-row finite ladders only, not circular ladders or grids of larger fixed width. The independent finite experiments end at eight rungs. No machine-checked infinite proof or independent audit is claimed. Literature searches are not proof of priority; unindexed or differently formulated earlier results may exist.

## References
1. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042, first posted 2021-01-20, https://arxiv.org/abs/2101.08042 .
2. P. Manuel, B. Brešar, S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325, https://arxiv.org/abs/2210.15325 .
