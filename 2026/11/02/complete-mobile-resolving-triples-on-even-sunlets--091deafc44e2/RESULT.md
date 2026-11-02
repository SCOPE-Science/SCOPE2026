# Complete mobile resolving triples on even sunlets

## Finding

For every integer \(m\ge 2\), let \(S_{2m}=C_{2m}\circ K_1\) be the even sunlet with cycle vertices \(c_i\) and their pendant leaves \(\ell_i\), indexed by \(i\in\mathbb Z/(2m)\mathbb Z\). Let \(\operatorname{mmd}_c\) denote completely mobile metric dimension: the fewest distinctly positioned robots that initially resolve every graph vertex and can each visit every graph vertex through single-edge moves, one robot at a time, without collisions or loss of resolution.

**Theorem.** For every \(m\ge2\), \[\operatorname{mmd}_c(S_{2m})=3.\] Moreover, for any three distinct cycle indices \(a,b,c\), the three core vertices \(\{c_a,c_b,c_c\}\) resolve the full sunlet if and only if the three positive clockwise gaps between successive indices are each at most \(m\). **Every** such three-core resolving configuration is completely mobile, and the exact number of labelled-vertex, unordered three-core resolving configurations is
\[\frac{m(m-1)(m+4)}3.\]
The graph of all these three-core configurations, adjacent under single-token slides along cycle edges maintaining resolution, is connected. For \(m=2\), exactly four resolving two-vertex sets exist, the sets of two pendant leaves whose attachment points are adjacent; all are frozen under resolving-preserving single-edge moves.

## Assumptions and scope

Graphs are finite, undirected, unweighted, and simple. The cycle has \(2m\ge4\) vertices. All resolving sets use ordinary shortest-path distance in the **entire sunlet**, not only on its cycle. Robots are individually distinguishable, cannot share a vertex, and move one at a time along an existing edge. Complete mobility requires a (possibly different) finite legal move sequence for each robot and destination; the proof in fact supplies a repeating patrol for all three robots. The enumerator counts vertex subsets in the fixed labelled sunlet, not automorphism classes and not configurations involving leaves.

## Proof

**1. A gap characterization.** Let \(d_C\) denote the distance on the even cycle. For any core landmark \(c_a\), the distance to \(c_i\) is \(d_C(a,i)\), and the distance to \(\ell_i\) is \(d_C(a,i)+1\). Any two nonantipodal landmarks resolve the *cycle locations* of same-layer vertices, and any three distinct core landmarks contain such a pair. Thus same-layer vertices are distinguished by every three-core set.

Suppose, then, that a core vertex \(c_i\) and a leaf \(\ell_j\) are not distinguished by three core landmarks with index set \(A\). This requires \(d_C(i,a)-d_C(j,a)=1\) for every \(a\in A\). For fixed distinct \(i,j\), the set of cycle indices satisfying this one-unit difference is contained in \(m\) consecutive indices. Here is a direct check. By rotation and reflection put \(i=0\) and \(j=t\) with \(1\le t\le m\). If \(t\) is even, there are no such indices by cycle parity. If \(t=1\), they are precisely \(\{1,2,\ldots,m\}\). If \(t=2s+1\ge3\), they are precisely the two indices \(s+1\) and \(m+s\), whose clockwise separation is \(m-1\). (For \(i=j\), the required difference is zero.) The asserted containment follows in all cases.

Three cycle vertices lie in some arc comprising \(m\) consecutive vertices exactly when at least one of their three clockwise gaps is at least \(m+1\). Hence if every gap is at most \(m\), all cross-layer pairs are also distinguished. Conversely, if a gap is at least \(m+1\), the landmarks all lie in an arc of \(m\) consecutive cycle vertices; after a rotation this arc is \(\{0,1,\ldots,m-1\}\). For every landmark \(a\) in this arc,
\[d(c_{-1},c_a)=a+1=d(\ell_0,c_a).\]
The distinct vertices \(c_{-1}\) and \(\ell_0\) are therefore not resolved. This establishes the if-and-only-if claim.

**2. Enumeration.** There are \(\binom{2m}{3}\) cycle triples. An invalid triple has a unique gap longer than \(m\); two such gaps are impossible because the gaps sum to \(2m\). Starting the long gap at one of the \(2m\) indexed cycle vertices and fixing its length \(L\), the other two gaps have \(2m-L-1\) positive ordered choices. Summing \(L=m+1,\ldots,2m-2\), the number of invalid triples is \(2m(m-1)(m-2)/2\). Subtraction gives
\[\binom{2m}{3}-m(m-1)(m-2)=\frac{m(m-1)(m+4)}3.\]

**3. Legal moves and complete mobility.** Fix a clockwise cyclic order of the three **individual labelled robots** on the core. Write their positive clockwise gap vector as \((g_1,g_2,g_3)\); its entries are between \(1\) and \(m\) and sum to \(2m\). A one-step slide of one robot transfers one unit between the two gaps incident to that robot; since there are three gaps, every pair of gap coordinates is incident to a shared robot. Given any two valid gap vectors, whenever they differ choose a surplus coordinate and a deficit coordinate, and transfer one unit from the former to the latter. The donor is at least \(2\), the receiver at most \(m-1\), so the move is collision-free, preserves all three upper bounds, and reduces the \(\ell_1\)-difference from the target by \(2\). Thus any admissible gap vector can be reached with the original robot identities in their fixed cyclic order.

For \(m\ge3\) choose the admissible target gap vector \((m-1,m-1,2)\). Every gap is at least \(2\) and at most \(m-1\). Moving its three robots clockwise, in front-to-back order, translates the whole configuration one cycle vertex clockwise by three legal slides: any intermediate gap is only one larger or smaller than its initial size, so remains between \(1\) and \(m\). Repeating translates each original robot around all \(2m\) core vertices. The same reasoning, from any initial admissible triple, first reaches this target gap vector and then performs the patrol. It also proves connectivity of the **unlabelled** three-core configuration graph: a target gap vector can be reached, then its absolute rotation can be chosen freely.

For \(m=2\), each resolving core triple omits one of the four cycle vertices. Repeatedly sliding the core robot immediately preceding the hole clockwise into that hole cycles the vacancy counterclockwise, and all three individually labelled robots eventually traverse the entire four-cycle. The four three-core configurations form a connected reconfiguration cycle.

Finally, if a robot sits at \(c_i\) in a resolving set, it may move to the unused pendant \(\ell_i\) and back without losing resolution: for each graph vertex \(v\ne\ell_i\), \(d(v,\ell_i)=d(v,c_i)+1\), so all pairs not involving \(\ell_i\) retain their distinguishing coordinates from this robot, while the new occupied vertex \(\ell_i\) distinguishes itself by its zero coordinate. At every cycle vertex the corresponding detour lets the arriving robot visit its pendant leaf. Therefore **each of the three robots visits every vertex**.

**4. Sharp lower bound.** For \(m\ge3\), no pair of vertices resolves \(S_{2m}\), even if either landmark is a leaf. Associate to each landmark its core attachment projection. Distances to a leaf landmark add one to distances to its projection, for every vertex other than that very leaf; the witness vertices selected below are always distinct from the landmarks. If the two projections coincide or are antipodal, the distinct leaves \(\ell_{p-1}\) and \(\ell_{p+1}\) adjacent around the first projected location \(p\) have the same two-distance signatures. Otherwise, after rotation/reflection take the projections at \(0\) and \(a\), with \(1\le a\le m-1\). For \(a\le m-2\), the distinct vertices \(c_{-2}\) and \(\ell_{-1}\) have the same distances to both projections: respectively \(2\) and \(a+2\). For \(a=m-1\), use \(c_{-2}\) and \(\ell_1\), each at distances \(2\) and \(m-1\) from projections \(0,a\). Adding the possible one-unit offsets for leaf landmarks preserves both equalities. Thus no two-landmark resolving set exists for \(m\ge3\).

For \(m=2\), inspection of the seven dihedral pair types (two core-core types, three core-leaf types, and two leaf-leaf types) shows that exactly the four adjacent-leaf pairs resolve. Moving either pendant landmark inward gives a core-leaf pair, none of which resolves; hence no resolving pair is mobile. One robot is insufficient in every case. Together with the three-robot construction, the lower bound and all assertions follow. \(\square\)

## Verification

The standalone script `verify_sunlet.py` builds each sunlet and independently computes all-pairs shortest paths from adjacency lists. It enumerates every two-vertex candidate and every three-core candidate for even circumferences \(4,6,8,10,12,14,16\), checks the exact gap rule and cardinalities, verifies all pendant-detour replacements, and explores **labelled** core-only robot moves from every admissible core triple to confirm that each robot can visit every core vertex. It finds exactly \(4,14,32,60,100,154,224\) admissible core triples respectively, no resolving pair except four frozen adjacent-leaf pairs for circumference four, and all required labelled core patrols. Run with `python3 verify_sunlet.py`. Finite computation corroborates, but does not substitute for, the quantified proof above.

## Relationship to prior work

Camacho Moreno, Kuziak, Shallcross, Tuite and Yero [1] introduce complete mobility for resolving robots and prove a two-robot result for **odd** unicyclic graphs with at most one pendant path per cycle vertex. Their odd-cycle theorem does not cover even sunlets, nor does it supply this even-core triple gap classification, cardinality or individually labelled patrols. The earlier ordinary/static metric-dimension study of sunlets by Ali, Rahim and Ali [2] does not impose the complete-mobility move requirement; the present claim concerns the stronger dynamic parameter and a classification of core-only mobile triples. The distinction is already visible in the four-cycle sunlet, which has resolving pairs but requires three completely mobile robots. No priority claim is made for the basic cycle-distance identity or standard metric-dimension definitions.

## Limitations

This is an exact result only for unweighted even sunlets with one leaf per core vertex. The count concerns core-only triples, not every mixed core/leaf three-robot configuration; no formula is asserted for their number. The result does not determine a shortest total patrol length, heterogeneous pendant lengths or other unicyclic graphs. The mathematical review is not an independent audit, and other literature under different terminology remains a priority risk.

## References

[1] J. C. Camacho Moreno, D. Kuziak, E. Shallcross, J. Tuite, I. G. Yero, *Completely mobile robots in graphs with a resolving property*, arXiv:2610.13339 (first public 2026-10-09), https://arxiv.org/abs/2610.13339.

[2] M. Ali, M. T. Rahim, G. Ali, *On Three Families of Graphs with Constant Metric Dimension*, Journal of Combinatorial Mathematics and Combinatorial Computing 91 (2014), 115–121, https://combinatorialpress.com/article/jcmcc/Volume%20091/vol-091-paper%207.pdf.
