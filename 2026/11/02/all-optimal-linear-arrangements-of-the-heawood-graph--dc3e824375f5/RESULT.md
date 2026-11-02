# All optimal linear arrangements of the Heawood graph

## Finding

Let \(H\) be the point-line incidence graph of the Fano plane. Thus \(H\) has fourteen vertices (seven points and seven lines) and twenty-one edges. For a bijective vertex ordering \(\pi=(v_1,\ldots,v_{14})\), let \(\operatorname{pos}_{\pi}(v)\) be the position of \(v\), and define its linear-arrangement cost by
\[
L(\pi)=\sum_{\{u,v\}\in E(H)}\bigl|\operatorname{pos}_{\pi}(u)-\operatorname{pos}_{\pi}(v)\bigr|.
\]

**Theorem.** The minimum cost is \(69\), and exactly \(1{,}548{,}288\) distinct vertex permutations attain it. More precisely, an ordering is minimum-cost **if and only if** it is built as follows:

1. Choose an induced six-cycle \(C\) and a vertex-disjoint induced six-cycle \(C'\) of \(H\), as an *ordered pair*.
2. List the six vertices of \(C\), starting anywhere and successively growing one contiguous arc of \(C\) at each stage.
3. List the two vertices outside \(C\cup C'\) in either order.
4. List the six vertices of \(C'\) in an order whose **reverse** starts anywhere and successively grows one contiguous arc of \(C'\).

There are \(28\) choices of \(C\), precisely three choices of \(C'\) for each \(C\), exactly \(96\) valid internal orders per six-cycle, and two orders for the remaining pair. Hence the exact count factors as
\[
28\cdot 3\cdot 96^2\cdot 2=1{,}548{,}288.
\]
Every such optimal ordering also attains cutwidth \(7\), which is the cutwidth of \(H\).

## Assumptions and scope

The Fano plane has point set \(P=\mathbb F_2^3\setminus\{0\}\), with a line equal to \(\{a,b,a+b\}\) for each pair of different points \(a,b\in P\). Its Levi graph \(H\) has vertex set consisting of the seven points and seven lines, with a point adjacent to a line exactly when incident. Vertex permutations are counted **without** quotienting by graph automorphisms, reversal, or point-line duality. The graph is simple and three-regular. Since two points lie on a unique common line and the graph is bipartite, it has girth at least six; the Fano triangles give six-cycles, so its girth is exactly six.

For \(S\subseteq V(H)\), write \(e(S)\) for the number of edges induced by \(S\) and \(\partial S\) for its edge boundary. Define the constrained minimum \(\beta_k=\min\{|\partial S|:|S|=k\}\). In the above vertex ordering, its \(k\)-vertex prefix is \(S_k=\{v_1,\ldots,v_k\}\), with \(S_0=\varnothing\).

## Proof

**1. Exact constrained cut profile.** Three-regularity gives, for every set \(S\) of size \(k\),
\[
|\partial S|=3k-2e(S).
\]
If \(1\le k\le5\), the induced subgraph is acyclic by girth six. Therefore \(e(S)\le k-1\) and \(|\partial S|\ge k+2\). An induced path along a six-cycle attains equality for every such \(k\).

For \(k=6\), at most six edges can be induced. Indeed, seven edges would require a cycle; every such cycle would use all six vertices, and any further edge would be a chord creating a shorter cycle. Six induced edges are attained exactly by a six-cycle. Thus \(\beta_6=6\), and the boundary minimizers of cardinality six are precisely the vertex sets of induced six-cycles.

For \(k=7\), let \(p\) and \(q\) be the numbers of selected points and lines, so \(p+q=7\). If \(p\le2\) or \(q\le2\), then \(e(S)\le6\): two selected points share just one line, so among any five chosen lines at most one meets both selected points, and the dual argument covers two selected lines. Otherwise, the possibilities are \((p,q)=(3,4)\) and \((4,3)\), which are dual. With three selected points, if they are collinear, any four lines contain at most six incidences with them; if they are noncollinear, only their three pair-joining lines can meet two selected points, while every other line meets at most one. Four selected lines therefore have at most \(2+2+2+1=7\) incidences. Hence \(e(S)\le7\) and \(|\partial S|\ge7\). A six-cycle together with any outside vertex adjacent to it induces exactly seven edges: an outside vertex cannot have two neighbours on the six-cycle, as that would create a four-cycle. Thus \(\beta_7=7\).

Since \(|\partial S|=|\partial(V(H)\setminus S)|\), the remaining minima follow by complementation. The complete exact profile, indexed by \(k=0,1,\ldots,14\), is
\[
(\beta_0,\ldots,\beta_{14})=(0,3,4,5,6,7,6,7,6,7,6,5,4,3,0).
\]
Its sum is \(69\) and its maximum is \(7\).

**2. The disjoint-hexagon geometry.** Every six-cycle corresponds to a noncollinear triple of Fano points together with its three pair-joining lines. Of the \(\binom73=35\) triples of points, seven are lines, so there are exactly \(28\) six-cycles.

Fix any noncollinear triple. An invertible change of coordinates sends it to the basis \(e_1,e_2,e_3\). Write \(a=e_1+e_2\), \(b=e_2+e_3\), \(c=e_1+e_3\), and \(d=e_1+e_2+e_3\). The points outside the fixed triple are \(a,b,c,d\), with \(a,b,c\) collinear. Exactly three noncollinear triples can be selected from these four points, namely the triples consisting of \(d\) and two of \(a,b,c\); their associated side-lines do not coincide with any side-line of the first triangle. Thus each six-cycle has exactly three vertex-disjoint six-cycle mates.

For example, take the mate with point triple \(d,a,b\). The six-cycle of the first triangle uses lines \(\{e_1,e_2,a\}\), \(\{e_2,e_3,b\}\), and \(\{e_1,e_3,c\}\); the mate uses \(\{a,b,c\}\), \(\{a,d,e_3\}\), and \(\{b,d,e_1\}\). The two uncovered vertices are the point \(c\) and the line \(\{c,d,e_2\}\). They are incident, and each is adjacent to exactly one vertex on each six-cycle. Permuting \(e_1,e_2,e_3\) establishes the same conclusion for either other mate and, by coordinate symmetry, for every ordered disjoint pair.

**3. The arrangement lower bound and its equality case.** An edge whose endpoints occupy positions \(i<j\) crosses exactly the \(j-i\) prefix cuts between them. Summing over all edges gives the identity
\[
L(\pi)=\sum_{k=1}^{13}|\partial S_k|\ge\sum_{k=1}^{13}\beta_k=69.
\]
Choose an ordered disjoint pair \(C,C'\) of six-cycles. A growing contiguous arc of \(C\) supplies a boundary-minimizing prefix for sizes one through six. Either of the two remaining vertices has exactly one neighbour on \(C\), so adjoining it gives a size-seven minimizing prefix; adjoining the other gives a size-eight prefix complementary to \(C'\), hence also minimizing. Reading a growing arc of \(C'\) backwards at the end makes the complements of all remaining prefixes optimal. Every prescribed ordering therefore has \(L(\pi)=69\).

Conversely, since \(69\) is achievable, an optimal ordering must realize \(|\partial S_k|=\beta_k\) for **every** \(k\); all summands independently meet their lower bounds. Its first six vertices therefore form an induced six-cycle \(C\); its last six vertices also form an induced six-cycle \(C'\), because their complement is a minimizing eight-vertex set. The two cycles are disjoint. Within \(C\), for prefixes of sizes at most five, minimizing the cut requires inducing exactly \(k-1\) edges, hence a connected path; in a six-cycle these are exactly the contiguous arcs. The same holds when the last six vertices are read in reverse. Therefore every optimal ordering has precisely the asserted structure, with no extra cases.

**4. Exact enumeration and cutwidth.** On a fixed six-cycle, the first vertex has six choices. The next four vertices each have two possible arc extensions; the last vertex is forced. There are \(6\cdot2^4=96\) orders. Section 2 provides \(28\cdot3=84\) ordered disjoint pairs, and the two uncovered vertices can appear in either order. This yields \(84\cdot96\cdot2\cdot96=1{,}548{,}288\), with no duplicates because the first and last six-vertex sets determine the cycle pair uniquely. Finally every vertex ordering has cutwidth at least \(\beta_7=7\), whereas the exhibited orders attain boundary \(\beta_k\le7\) at every cut; thus \(\operatorname{cw}(H)=7\).

## Verification

Two independent, standalone Python 3 scripts accompany this result. Both use only the standard library and can be invoked from the directory holding the artifacts:

```
python3 verify_subset_dp.py
python3 verify_fano_structure.py
```

The first script constructs the Fano incidence graph using a cyclic difference set, exhaustively evaluates all \(2^{14}=16{,}384\) vertex subsets, checks the complete cut profile, and runs a cost-minimizing and counting dynamic program over every subset. It independently counts chains of constrained cut minimizers. It returns minimum cost \(69\) and \(1{,}548{,}288\) optimal permutations.

The second script constructs the Fano plane independently from nonzero binary coordinate vectors and its seven three-point lines. It enumerates all \(28\) noncollinear-triangle six-cycles and \(84\) ordered disjoint pairs, checks the residual point-line incidence property for each pair, explicitly generates all \(96\) arc orders per cycle, and checks a complete minimizing layout for each pair. Its structural product also returns \(1{,}548{,}288\). These finite checks corroborate the self-contained proof; none is extrapolated to a larger graph family.

## Relationship to prior work

Horton, Parker, and Borie established the general relationship between cardinality-constrained minimum cuts, nested solutions, and linear arrangement: the cut-profile sum is a universal lower bound and is attained exactly when nested cut minimizers exist. Their general theorem is credited here and does **not** itself supply the Heawood-specific profile, optimizer classification, or enumeration.

Baez's 2015 account identifies the Heawood graph with the Fano-plane incidence graph and records its \(28\) six-cycles. Dejter's work on the Coxeter graph also describes its classical construction as the cubic disjointness graph of the Heawood six-cycles, so the count of three disjoint mates per cycle is not novel by itself. Those previously known structural facts are credited. The proposed new statement is the constrained-cut profile together with the necessary-and-sufficient layout-optimizer classification and exact count, obtained by combining the known six-cycle structure with tight prefix-cut conditions.

## Limitations

This is a theorem for the fourteen-vertex Heawood graph, not for arbitrary finite-projective-plane incidence graphs. The permutation count is for distinct, named vertices with no symmetry quotient. A broader prior-work coincidence cannot be ruled out solely by indexed literature searches. The correctness verification is a proof plus independent finite checks; no external scholarly audit is claimed.

## References

1. S. B. Horton, R. Gary Parker and R. B. Borie, *On minimum cuts and the linear arrangement problem*, Discrete Applied Mathematics **103** (2000), 127–139, DOI: `10.1016/S0166-218X(00)00173-6`; dated 15 July 2000 in the publisher record.
2. John Baez, *Heawood Graph*, AMS Visual Insight, 1 August 2015, `https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/`.
3. Italo J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:`1002.1960`, first publicly posted 9 February 2010; see Section 1 for the Coxeter-graph description via disjoint Heawood six-cycles.
4. L. H. Harper, *Optimal Assignments of Numbers to Vertices*, Journal of the Society for Industrial and Applied Mathematics **12** (1964), 131–135, DOI: `10.1137/0112012` (historical background on optimal numbering).
