# Geodesic packing and transversal censuses of complete split graphs

## Finding

Let \(r\ge 1\) and \(s\ge 2\) be integers. The *complete split graph* \(G_{r,s}=K_r\vee\overline{K_s}\) has a specified \(r\)-vertex clique \(C\) and a specified \(s\)-vertex independent set \(I\), with all cross-edges present. A maximal geodesic is a shortest path not properly contained as a contiguous subpath in any other shortest path. A geodesic packing is an unordered collection of pairwise vertex-disjoint maximal geodesics. A geodesic transversal is a vertex subset intersecting every maximal geodesic; it is *inclusion-minimal* if no proper subset is a transversal.

Define \(P_{r,s}(z)=\sum_{\mathcal P}z^{|\mathcal P|}\), where the empty packing is included, and define \(T_{r,s}(z)=\sum_{S}z^{|S|}\), over all inclusion-minimal geodesic transversals. Then

\[
P_{r,s}(z)=\sum_{t=0}^{\min(r,\lfloor s/2\rfloor)}\ \sum_{u=0}^{\lfloor(r-t)/2\rfloor}
\binom rt\frac{s!}{2^t(s-2t)!}\frac{(r-t)!}{2^u u!(r-t-2u)!}\,z^{t+u},
\qquad T_{r,s}(z)=z^r+rs\,z^{r+s-2}.
\]

The second formula counts multiplicities when the displayed monomials have the same degree (in particular, when \(s=2\)). Set \(h=\min(r,\lfloor s/2\rfloor)\). The geodesic packing and transversal numbers, and their gap, satisfy

\[
\operatorname{gpack}(G_{r,s})=\left\lfloor\frac{r+h}{2}\right\rfloor,\quad
\operatorname{gt}(G_{r,s})=r,\quad
\operatorname{gt}(G_{r,s})-\operatorname{gpack}(G_{r,s})=\left\lceil\frac{r-h}{2}\right\rceil.
\]

In particular, \(\operatorname{gpack}(G_{r,s})=\operatorname{gt}(G_{r,s})\) **if and only if** \(s\ge2r\). For \(s\ge3\), the clique \(C\) is the unique minimum transversal; for \(s=2\), exactly \(1+2r\) minimum transversals exist.

Every maximum packing is structurally specified by the formula below. Write
\[
A_{r,s}(t,u)=\binom rt\frac{s!}{2^t(s-2t)!}\frac{(r-t)!}{2^u u!(r-t-2u)!}
\]
for feasible nonnegative integers \(t,u\), and put \(k=\lfloor(r+h)/2\rfloor\). The exact number of maximum packings is
\[
[z^k]P_{r,s}(z)=A_{r,s}\left(h,\left\lfloor\frac{r-h}{2}\right\rfloor\right)
+\mathbf1_{\{r+h\text{ odd}\}}A_{r,s}\left(h-1,\frac{r-h+1}{2}\right).
\]
Thus optimal packings use exactly \(h\) three-vertex geodesics, except in the odd-parity case when \(h-1\) such paths are also possible. In the saturation range \(s\ge2r\), there are exactly \(s!/(2^r(s-2r)!)\) maximum packings.

## Assumptions and scope

Graphs are finite, simple, undirected, and explicitly vertex-labelled. Paths are counted without orientation (a path and its reversal are one object). Geodesic packings are sets of paths, not partitions of vertices; unused vertices are allowed. All statements concern exactly the integer domain \(r\ge1\), \(s\ge2\). The assertion for \(\operatorname{gt}\) itself is also a special case of a previously published join theorem; the new contribution is the complete paired census, packing number and maximum-packing classification, inclusion-minimal transversal census, and exact equality threshold for this family.

## Proof

**Step 1 (all maximal paths).** Vertices in \(C\) are pairwise adjacent and adjacent to every vertex in \(I\), while two distinct vertices of \(I\) are at distance two. Hence the graph has diameter two. Its length-two geodesics are exactly the paths \(a-c-b\), where \(c\in C\) and \(a,b\in I\) are distinct. Such paths are automatically maximal because no longer geodesic exists. Every clique edge \(c-d\) is a maximal geodesic: a length-two shortest path containing it would have to end in a non-neighbor of one endpoint, but each clique endpoint is universal. Conversely, every clique–independent edge \(c-a\) extends to \(a-c-b\) with \(b\in I\setminus\{a\}\), which exists because \(s\ge2\). Thus maximal geodesics comprise precisely (i) the two-vertex edges within \(C\) and (ii) the three-vertex paths with two endpoints in \(I\) and one center in \(C\).

**Step 2 (enumeration).** Suppose a packing chooses \(t\) paths of type (ii) and \(u\) of type (i). The \(t\) centers are a \(t\)-subset of the \(r\) clique vertices, chosen in \(\binom rt\) ways. Since each center is individually distinguished, assigning to these centers pairwise disjoint unordered pairs from \(I\) has \(s!/(2^t(s-2t)!)\) possibilities. From the remaining \(r-t\) clique vertices choose an unordered matching of size \(u\), in \((r-t)!/(2^u u!(r-t-2u)!)\) ways. All choices give vertex-disjoint maximal paths, and each packing determines its parameters and choices uniquely. Summing over \(t\) and \(u\) proves \(P_{r,s}\). Equivalently, its formal bivariate exponential generating function, extended to nonnegative \(r,s\) as a block-counting identity, is
\[
\sum_{r,s\ge0}\frac{x^r y^s}{r!s!}P_{r,s}(z)
=\exp\!\left(x+y+\frac z2x^2+\frac z2xy^2\right).
\]

**Step 3 (maximum packings).** For fixed \(t\), the greatest possible \(u\) is \(\lfloor(r-t)/2\rfloor\), giving \(t+u=\lfloor(r+t)/2\rfloor\). The admissible values satisfy \(0\le t\le h\). This expression is nondecreasing in \(t\), so its largest value occurs at \(t=h\). If \(r+h\) is even, no smaller \(t\) attains the same value; if \(r+h\) is odd, precisely \(t=h\) and \(t=h-1\) do. This proves the claimed maximum, multiplicity and parity alternatives. The last alternatives include \(h-1\ge0\), since \(h\ge1\) in the stated domain.

**Step 4 (all minimal transversals).** Every transversal meets each clique edge, so it omits at most one clique vertex. If no clique vertex is omitted, inclusion-minimality forces the transversal to be \(C\) itself. If one clique vertex \(c\) is omitted, each path \(a-c-b\) must meet the transversal; hence at most one independent vertex can also be omitted. Inclusion-minimality forces exactly one independent vertex \(i\) to be omitted, yielding \((C\setminus\{c\})\cup(I\setminus\{i\})\). Conversely, \(C\) is minimal because deleting any clique vertex exposes a length-two path through it. Each alternative set is minimal: deleting another clique vertex exposes their maximal clique edge, and deleting another independent vertex exposes a length-two geodesic centered at the omitted clique vertex. For \(r=1\), the clique-edge deletion case is vacuous. There are \(rs\) distinct alternative sets, establishing \(T_{r,s}\). The minimum cardinality is \(\min\{r,r+s-2\}=r\), because \(s\ge2\). The packing-transversal equality and gap follow by substitution in Step 3; equality requires \(h=r\), equivalently \(s\ge2r\).

## Verification

The accompanying dependency-free `verify_split_geodesics.py` independently enumerates shortest paths in labelled complete split graphs, tests maximality by contiguous-subpath containment, enumerates vertex-disjoint families by mask dynamic programming, and tests all vertex subsets for inclusion-minimal hitting. It compares both complete polynomials and the cardinality claims. It checked 22 graph profiles with \(r+s\le9\): 3,592 vertex subsets, 414 maximal-geodesic objects, and 15,576 memoized packing states. A separate 5,000-profile exact-integer arithmetic sweep tests the packing-size and saturation identities for \(1\le r\le50\), \(2\le s\le100\). These finite checks supplement but do not replace the proof for all parameters.

## Relationship to prior work

Manuel, Brešar and Klavžar introduced and analyzed geodesic packing in `arXiv:2210.15325` (first public version 27 October 2022), including complexity, trees and selected graph products, and noted the balanced complete-bipartite packing number. Peterin and Semanišin established a general join theorem for the *geodesic transversal number* (`DOI:10.1007/s40314-022-01834-1`, Theorem 3.5). That general theorem already implies the scalar equality \(\operatorname{gt}(G_{r,s})=r\), so this scalar is not asserted as new. The inspected papers do not state or imply the present whole-family geodesic packing distribution, maximum-packing multiplicities, inclusion-minimal transversal distribution or exact equality boundary as a combined classification. Searches of accessible related research did not identify identical formulas; this is not a claim of exhaustive priority verification.

## Limitations

No theorem is asserted for arbitrary split graphs outside the complete-join family or for \(s<2\), where the geodesic types change. The displayed exponential generating function is an auxiliary block-counting identity, not a definition of the graph problem for degenerate parameters. The proofs are purely finite combinatorial; the experimental checks cannot establish the unbounded-parameter statements independently. Unindexed or inaccessible literature could contain equivalent results, and independent mathematical audit has not been performed.

## References

1. P. Manuel, B. Brešar, S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325v1 (27 October 2022), https://arxiv.org/abs/2210.15325 ; journal version *Applied Mathematics and Computation* 459 (2023), 128277, DOI:10.1016/j.amc.2023.128277.
2. I. Peterin, G. Semanišin, *Geodesic transversal problem for join and lexicographic product of graphs*, *Computational and Applied Mathematics* 41 (2022), article 128, DOI:10.1007/s40314-022-01834-1; author preprint: https://mp.feri.um.si/osebne/peterin/clanki/2021_iIpgs_geod_trans_JLP.pdf.
3. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1 (20 January 2021), https://arxiv.org/abs/2101.08042.
