# Two marked vertices determine colour-refinement orbits in every nonbinary Hamming graph

## Finding

For integers \(q\ge3\) and \(d\ge1\), let \(H(d,q)\) be the graph on \(\{0,\ldots,q-1\}^{d}\) in which two vertices are adjacent exactly when they differ in one coordinate. Give two distinct vertices \(u,v\) different individual colours, and give all other vertices a third initial colour. Put \(b=\operatorname{dist}(u,v)\) and \(a=d-b\), so \(1\le b\le d\).

**Theorem.** Stable ordinary vertex colour refinement produces exactly the orbits of the automorphism group fixing both \(u\) and \(v\) pointwise. There are exactly
\[
(a+1)\binom{b+2}{2}
\]
stable classes, and the partition is stable within at most \(d+1\) refinement rounds. Its classes and their cardinalities are explicitly given below.

For each vertex \(x\), on the \(a\) coordinates where \(u\) and \(v\) agree, let \(s\) count the coordinates where \(x\) differs from their common symbol. On the remaining \(b\) coordinates, let \(r\) count those where \(x\) agrees with \(u\), let \(t\) count those where \(x\) agrees with \(v\), and let \(w=b-r-t\) count those where \(x\) agrees with neither. Then the stable classes are exactly the nonempty sets with fixed \((s,r,t)\), for
\[
0\le s\le a,\qquad r,t\ge0,\qquad r+t\le b.
\]
The class labelled \((s,r,t)\) has precisely
\[
\binom as(q-1)^s\frac{b!}{r!\,t!\,(b-r-t)!}(q-2)^{b-r-t}
\]
vertices. In particular, all admissible classes occur because \(q\ge3\).

The multiset of two distances alone is **not** generally the stable invariant. More precisely, the ordered distance pair together with one count of neighbours determines the complete class label, as proved below.

## Assumptions and scope

The graphs are finite, simple, and undirected. Ordinary one-dimensional Weisfeiler--Leman refinement, also called colour refinement, means that at each round the colour of a vertex is updated injectively from its previous colour and the multiset of previous colours of its neighbours. The round-zero colours individually name exactly the two distinct anchors. The assertion concerns the colour partition of this **single marked graph**; it does not claim that a marked Hamming graph is identifiable among all nonisomorphic graphs by two-variable counting logic.

The integer \(q=2\) is excluded from the displayed class count: an alphabet without a third symbol makes all classes with \(w>0\) empty. The theorem covers all positive dimensions and all anchor distances \(1\le b\le d\). It uses no assumption that \(q\) is prime or a prime power.

## Proof

**Step 1: Normalize the anchors and identify candidate orbits.** Independently relabel the alphabet on each coordinate, and permute the coordinates. We may suppose
\[
u=(0,\ldots,0),\qquad v=(\underbrace{1,\ldots,1}_{b},\underbrace{0,\ldots,0}_{a}).
\]
Coordinate permutations within the first \(b\) positions and within the last \(a\) positions preserve both marked vertices. So do independent symbol permutations on the last \(a\) positions fixing \(0\), and symbol permutations on the first \(b\) positions fixing both \(0\) and \(1\). All these are graph automorphisms. They act transitively on the vertices with a specified triple \((s,r,t)\): first reorder equal-coordinate nonzeros and the three types of unequal-coordinate positions, then adjust the nonanchor symbols independently. Therefore every triple class is contained in a single pointwise-stabilizer orbit. Conversely, we will prove colour refinement distinguishes distinct triples. As every colour-refinement colour is invariant under automorphisms preserving the initial marked colours, these two conclusions together will imply equality of stable colour classes and orbits.

**Step 2: Colour refinement retrieves the two distances.** In any graph with one uniquely coloured anchor \(z\), the colour after round \(k\) distinguishes the distance layers \(0,1,\ldots,k\) of \(z\) from each other and from vertices at greater distance. Induct on \(k\): the uniquely marked layer is isolated at round zero, and the first layer having a neighbour in an already distinguished distance layer is precisely the next distance layer. Because updates retain the previous colour, previously distinguished layers never merge. Apply this observation simultaneously to the two differently marked anchors. More formally, forget one of their initial colour distinctions to get a coarser refinement; refining the original two-colour marking is at least as informative for each anchor individually. All distances from either anchor are at most \(d\), so after round \(d\) a vertex's refined colour determines the ordered pair
\[
h_0=\operatorname{dist}(x,u),\qquad h_1=\operatorname{dist}(x,v).
\]

**Step 3: One further neighbour-count recovers the remaining coordinate information.** For any \(x\), define
\[
T(x)=\#\{y:y\sim x,\ \operatorname{dist}(y,u)=h_0-1,\ \operatorname{dist}(y,v)=h_1-1\}.
\]
Changing one coordinate can decrease both distances only if \(u\) and \(v\) agree at that coordinate and \(x\) does not. Each such coordinate contributes exactly one neighbour, obtained by changing its symbol to the common anchor symbol. At a coordinate where \(u\) and \(v\) differ, no single replacement can simultaneously turn \(x\) into both distinct symbols. Consequently \(T(x)=s\). Since all neighbour distance pairs are determined by the round-\(d\) colours, the multiset of their colours at the next round determines \(T(x)\).

The distance equations follow directly from the coordinate types:
\[
h_0=s+t+w=s+b-r,\qquad h_1=s+r+w=s+b-t.
\]
It follows that \(r=b+T(x)-h_0\) and \(t=b+T(x)-h_1\). Thus round \(d+1\) determines every triple \((s,r,t)\). These triples describe sets transitively permuted by actual anchor-fixing automorphisms, so no refinement round can split a triple class. Hence the round-\(d+1\) partition is exactly the orbit partition and is stable.

**Step 4: Enumerate classes.** Independently choose the \(s\) changed equal-coordinate positions and their \(q-1\) nonanchor symbols. Among the first \(b\) coordinates choose the \(r\) entries equal to \(u\), the \(t\) equal to \(v\), and the other \(w\) entries, whose symbols have \(q-2\) choices each. Multiplication gives the displayed class-size formula. There are \(a+1\) choices of \(s\), and \(\binom{b+2}{2}\) nonnegative pairs \((r,t)\) with sum at most \(b\). Since \(q\ge3\), every choice occurs. This proves the theorem.

**Distance-pair obstruction (smallest useful witness).** In \(H(3,3)\), take \(u=(0,0,0)\), \(v=(0,1,1)\), \(x=(0,2,2)\), and \(y=(2,0,1)\). Both \(x\) and \(y\) have ordered distances \((2,2)\) from \((u,v)\), but \(T(x)=0\) and \(T(y)=1\). Thus the neighbour statistic detects a distinction missed by both distances.

## Verification

The accompanying standard-library programs are `checks/check_refinement.py` and `checks/check_local_statistic.py`. Run each with Python 3 from any directory; neither needs external data or libraries.

The first program independently constructs actual edges, performs canonical exact-colour refinement, and compares all resulting colour classes to the explicitly defined triples and their cardinalities. The second directly enumerates every neighbour's ordered distance pair and checks the local statistic identity and explicit witness. Together they tested 52 parameter choices with \(q\in\{3,4,5,6\}\) and dimensions up to 6 (depending on \(q\)), totaling 16,043 vertex instances. All checks passed, and the observed maximum strict-refinement depth was five. These finite computations corroborate the universally quantified proof but do not replace it.

## Relationship to prior work

Colour-refinement orbit partitions and their refinement properties are studied in Arvind, Köbler, Rattan, and Verbitsky (2015), including the general concept of a *refinable graph*. Arvind and coauthors (2016) analyze the distinct problem of computational complexity of individualizing vertices to attain properties such as discreteness or refinability. Boutin (2009) characterizes determining numbers of Cartesian graph products, including the Boolean hypercube and ternary Cartesian powers. Such determining-number results concern eliminating automorphisms, not necessarily recovering complete orbit partitions by one-dimensional colour refinement. The present formula concerns the entire two-anchor orbit partition of each \(q\)-ary Hamming graph with \(q\ge3\), its exact cell sizes, and its refinement-round upper bound.

Mogilnykh and Valyuzhenich (2019) classify equitable **two-cell** Hamming-graph partitions with a particular eigenvalue. The many-cell partition induced by two individually distinguished vertices is a different object; their inspected definitions and main setup do not assert this orbit formula.

An earlier result for the binary hypercube with arbitrary marked vertices treats \(q=2\) and does not imply the nonbinary three-symbol coordinate classification here. A prior ordered-pair two-dimensional Weisfeiler--Leman result for distance-regular graphs also addresses a different refinement procedure on pairs, initially without marked landmarks.

## Limitations

The result is a within-graph partition theorem, not a graph-identification theorem; no claim is made about arbitrary non-Hamming competitors. The round bound is an upper bound, not asserted to be sharp for every \((q,d,b)\). The technical ingredients are elementary and could occur in specialized literature on Hamming association schemes or equitable partitions; literature searches do not establish an absolute priority claim. The complete publisher text of Boutin (2009) was not available for inspection, so assessment of overlap with that work is limited to its openly accessible abstract and other public metadata. The finite verification ranges do not certify any dimension beyond those tested.

## References

1. D. L. Boutin, “The determining number of a Cartesian product,” *Journal of Graph Theory* **61** (2009), 77–87. DOI: 10.1002/jgt.20368; first online 2009-04-06.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” arXiv:1502.01255 (first posted 2015-02-04).
3. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, and G. Rattan, “The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs,” arXiv:1606.04383 (first posted 2016-06-14).
4. M. Grohe and collaborators, “Dimension Reduction via Colour Refinement,” arXiv:1307.5697 (first posted 2013-07-22).
5. I. Mogilnykh and A. Valyuzhenich, “Equitable 2-partitions of the Hamming graphs with the second eigenvalue,” arXiv:1903.12333 (first posted 2019-03-29).
