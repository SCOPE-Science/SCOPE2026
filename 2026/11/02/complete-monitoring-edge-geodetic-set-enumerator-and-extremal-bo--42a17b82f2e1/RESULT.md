# Complete monitoring-edge-geodetic set enumerator and extremal boundaries for cycles

## Finding

Let \(C_n\) be the simple unweighted cycle on \(n\ge3\) labeled vertices. A vertex set is *monitoring edge-geodetic* (MEG) if deleting each individual edge increases the shortest-path distance between some two selected vertices. Put \(m=\lfloor n/2\rfloor\). The complete MEG-set enumerator by selected cardinality is

\[
\mathcal M_n(z)=\sum_{S\text{ MEG}}z^{|S|}
=(1+z)^n-1-nz(1+z)^m+\frac n2\mathbf1_{\{2\mid n\}}z^2.
\]

Equivalently, for every integer \(0\le k\le n\), the exact number of MEG-sets of size \(k\) is

\[
a_{n,k}=\binom nk-\mathbf1_{\{k=0\}}-n\binom m{k-1}
+\mathbf1_{\{2\mid n,\ k=2\}}\frac n2,
\]

where out-of-range binomial coefficients are zero.

All inclusion-minimal MEG-sets are either three-vertex MEG-sets, or, when \(n=2m\), unions of two distinct antipodal vertex pairs. The number of minimal three-vertex sets is

\[
a_{2m+1,3}=\frac{(2m+1)m(m+1)}6,\qquad
 a_{2m,3}=\frac{m(m-1)(m-2)}3.
\]

For even order, there are \(\binom m2\) additional inclusion-minimal four-vertex MEG-sets (one when \(n=4\)). No other inclusion-minimal MEG-sets exist.

Every inclusion-maximal non-MEG set is one of the \(n\) cyclic blocks of \(m+1\) consecutive vertices. Thus the largest non-MEG set has size \(m+1\), and every vertex subset of size at least \(m+2\) is MEG; the latter bound is sharp.

If each vertex is independently available as a probe with probability \(p\), the exact probability that the available probes monitor all edges is

\[
R_n(p)=1-(1-p)^n-np(1-p)^{n-m-1}
+\frac n2\mathbf1_{\{2\mid n\}}p^2(1-p)^{n-2}.
\]

## Assumptions and scope

Vertices are labeled cyclically by residues in \(\{0,\ldots,n-1\}\). All graph edges have unit length. An unordered selected pair monitors an edge precisely when that edge lies in **every** geodesic joining its endpoints, equivalently when deletion of the edge increases their distance. There are no loops or multiple edges, and \(n\ge3\). A *clockwise gap* is the positive number of cycle edges between successive selected vertices in cyclic order. The claimed classifications refer to inclusion-minimal successful and inclusion-maximal unsuccessful sets, not merely extremal cardinalities.

## Proof

**1. Circular gap criterion.** Suppose \(S\) has at least two selected vertices, and let \(g_1,\ldots,g_k\) be its clockwise gaps; all are positive integers with sum \(n\). A path of length strictly less than \(n/2\) joining two cycle vertices is their unique shortest path. When two vertices are antipodal (possible only for even \(n\)), both length-\(n/2\) arcs are geodesics, so no edge on either arc is monitored by this pair.

If each selected gap has length strictly less than \(n/2\), its two endpoints uniquely monitor every edge in that gap, hence \(S\) is MEG. Conversely, if some gap has length \(g\ge n/2\), any path between selected vertices that contains an edge of the gap must traverse its full length, since there are no selected vertices in its interior. Such a path has length at least \(g\), so it cannot be a unique shortest path; consequently no edge in that gap is monitored. Thus

\[
S\text{ is MEG}\quad\Longleftrightarrow\quad
\max_i g_i<n/2
\quad\Longleftrightarrow\quad
\max_i g_i\le\lfloor(n-1)/2\rfloor.
\]

Singletons and the empty set are non-MEG because the graph has edges. For comparison, this gap condition is equivalent to the corresponding regular-polygon vertices not lying in any *closed* semicircle, or to the center belonging to the strict planar interior of their convex hull. We do not treat that reformulation itself as a novelty claim.

**2. Enumerating all MEG-sets.** Let \(h=\lceil n/2\rceil\) and \(m=n-h=\lfloor n/2\rfloor\). Fix \(k\ge2\). A non-MEG set has a selected clockwise gap of length at least \(h\). For each possible initial vertex (\(n\) choices) and gap length \(g\ge h\), choose its remaining \(k-2\) selected vertices among the \(n-g-1\) vertices outside the two gap endpoints. The number of such gap incidences is

\[
n\sum_{g=h}^{n-k+1}\binom{n-g-1}{k-2}
=n\binom{n-h}{k-1}=n\binom m{k-1}.
\]

There cannot be two disjoint gaps of length at least \(h\), except when \(n\) is even and the set consists of two antipodal points, whose two gaps are both length \(n/2\). There are exactly \(n/2\) such sets, each counted twice. Hence the number of bad \(k\)-sets is \(n\binom m{k-1}-\mathbf1_{\{2\mid n,\ k=2\}}n/2\). Together with the single empty set and \(n\) singletons, subtraction from \(\binom nk\) proves every coefficient of \(\mathcal M_n\).

**3. Inclusion-minimal successes.** No set of size below three is MEG (for \(n\ge3\)), so every successful triple is inclusion-minimal. Suppose a successful set has \(k\ge4\) selected vertices with cyclic gaps \(g_1,\ldots,g_k\), indices modulo \(k\). Deleting the selected vertex between \(g_i\) and \(g_{i+1}\) merges those two gaps; the resulting set is bad exactly if \(g_i+g_{i+1}\ge h\). Minimality therefore forces

\[
2n=\sum_{i=1}^k(g_i+g_{i+1})\ge kh.
\]

For odd \(n=2m+1\), \(h=m+1\) and \(4h>2n\); hence \(k\ge4\) is impossible. For even \(n=2m\), \(h=m\), so \(k\le4\). At \(k=4\), equality forces all four consecutive pair sums to equal \(m\), whence the gap sequence is \((a,m-a,a,m-a)\) with \(1\le a<m\). Its four vertices form two distinct antipodal pairs, and every such union has all gaps less than \(m\) but deletion of any one vertex produces a gap of \(m\). Choosing two among the \(m\) antipodal pairs gives exactly \(\binom m2\) such minimal sets. In particular, for \(n=4\) no successful triple exists but the unique four-vertex set succeeds.

A successful triple has positive gaps \((a,b,c)\), summing to \(n\), each at most \(\lfloor(n-1)/2\rfloor\). Inclusion-exclusion on compositions gives \(m(m+1)/2\) ordered triples of gaps when \(n=2m+1\), and \((m-1)(m-2)/2\) when \(n=2m\). Selecting the starting vertex and dividing by three (each labeled triple has three starts) yields exactly the displayed triple counts.

**4. Inclusion-maximal failures.** Fix an inclusion-maximal bad set. It has at least two vertices, since adding vertices to a set of size zero or one still leaves a bad set for \(n\ge3\). Choose a long selected gap of length \(g\ge h\). If an unselected vertex were outside the interior of that gap, adding it would leave the gap untouched, contradicting maximality. Thus all vertices outside its interior belong to the bad set. If \(g>h\), adding the first interior vertex after a gap endpoint would leave a gap of length \(g-1\ge h\), also contradicting maximality. Thus \(g=h\), and the selected set is exactly one consecutive block of \(n-h+1=m+1\) vertices. Conversely, adding any missing vertex splits the single gap of length \(h\) into positive lengths smaller than \(h\), so every such block is maximal bad. Distinct block-starting positions yield exactly \(n\) sets and prove the universal threshold \(m+2\).

**5. Independent availability.** Each selected vertex has weight \(p\), each omitted vertex weight \(1-p\). Consequently \(R_n(p)=(1-p)^n\mathcal M_n(p/(1-p))\), initially for \(0\le p<1\), and by polynomial continuity also at \(p=1\). Substitution proves the stated expression.

## Verification

The standalone program `verify.py` independently constructs the original vertex distances in \(C_n\) and the distances after deletion of each edge. It enumerates **every** subset for each \(3\le n\le13\), then checks all coefficients, inclusion-minimal configurations, inclusion-maximal bad blocks, and maximum bad cardinality. The program prints `VERIFY_OK`. This finite exhaustive check is independent of the circular-gap implementation; the preceding combinatorial argument proves the statements for all \(n\ge3\).

Reproduce using `python3 verify.py 13` with Python 3 standard library. No external files or dependencies are needed.

## Relationship to prior work

Dev, Dey, Foucaud, Krishna and Ramasubramony Sulochana introduced MEG-sets in arXiv:2210.03774 (first public version 2022-10-07) and computed the minimum size for cycles, including the four-cycle exception. That scalar minimum is prior work, not a new contribution here. Haslegrave (arXiv:2210.08955) proved complexity and product bounds. The papers arXiv:2403.09122 and arXiv:2409.19067 study structural bounds and algorithms for further graph classes. Their inspected cycle-relevant statements do not give this entire all-subset polynomial or both inclusion-extremal families.

The circular-gap criterion has a classical semicircle/convex-hull interpretation. The equivalence is explicitly noted because exact circular-point enumerations under different terminology could predate this graph formulation. The present claim is the complete cycle-MEG enumerator and combined minimal/maximal classifications, not priority over elementary polygon geometry or the already known scalar MEG number.

## Limitations

The claim is restricted to unweighted simple cycles. It does not cover paths, chorded cycles, weighted circles, edge-geodetic sets without monitoring uniqueness, or arbitrary products. The computations run only through cycle order thirteen; infinite validity depends on the written proof. An unindexed prior semicircle-counting or combinatorial-cycle result might already imply some or all of the enumerator; independent priority verification is outstanding.

## References

1. S. R. Dev, S. Dey, F. Foucaud, N. Krishna, and L. R. Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774 (first posted 2022-10-07), especially the cycle minimum theorem. https://arxiv.org/abs/2210.03774
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955 (2022). https://arxiv.org/abs/2210.08955
3. F. Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122 (2024). https://arxiv.org/abs/2403.09122
4. F. Foucaud et al., *Algorithms and complexity for monitoring edge-geodetic sets in graphs*, arXiv:2409.19067 (2024). https://arxiv.org/abs/2409.19067
