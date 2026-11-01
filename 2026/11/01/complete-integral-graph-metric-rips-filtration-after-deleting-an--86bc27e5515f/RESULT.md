# Complete integral graph-metric Rips filtration after deleting an affine-plane parallel class

## Finding

Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\). Delete **all lines in exactly one parallel class**, retaining every affine point and every other line. Let \(G\) be the simple bipartite incidence graph on these retained points and lines, with unit-edge shortest-path metric. Define \(K_r=\operatorname{VR}_{\le r}(V(G))\) to be the abstract simplicial complex whose simplices are the nonempty vertex subsets of diameter at most \(r\). Put \(b=q^3-2q^2+1\). Then, for all real \(r\ge0\),

\[
K_r\simeq
\begin{cases}
\bigvee^{2q^2-1}S^0,&0\le r<1,\\
\bigvee^bS^1,&1\le r<2,\\
(\bigvee^bS^2)\vee(\bigvee^{2(q-1)^q}S^{q-1}),&2\le r<3,\\
\bigvee^{(q-1)^{2q}}S^{2q-1},&3\le r<4,\\
\text{point},&r\ge4.
\end{cases}
\]

The convention \(\bigvee^0 S^d=\text{point}\) is understood; the indicated sphere dimensions may coincide. Consequently, in positive dimensions, the entire persistent homology barcode over **every** field consists of \(b\) degree-one intervals \([1,2)\), \(b\) degree-two intervals \([2,3)\), \(2(q-1)^q\) degree-\(q-1\) intervals \([2,3)\), and \((q-1)^{2q}\) degree-\(2q-1\) intervals \([3,4)\). For \(q=3\), the two degree-two contributions merge. Degree zero has \(2q^2-1\) intervals \([0,1)\) and one essential interval. All integral homology groups are torsion-free.

For \(q=3\), \(G\) is the 18-vertex Pappus graph. Its successive positive-radius homotopy types are \(\bigvee^{10}S^1\), \(\bigvee^{26}S^2\), \(\bigvee^{64}S^5\), and a point.

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, and \(q+1\) disjoint parallel classes of \(q\) lines. Every line contains \(q\) points, every point lies on one line of each parallel class, any two points lie on a unique line, and two nonparallel lines intersect at one point. No Desarguesian or coordinatization assumption is imposed. The construction deletes one **whole** parallel class of lines, not one line and not a parallel class of points. The theorem is conditional on the existence of an affine plane of the stated order; no existence assertion is made for arbitrary integers.

The shortest-path metric is on the finite vertex set only, not on the geometric realization of the graph with points interior to its edges. Rips thresholds are inclusive and use actual graph distance (integer-valued). The graph has \(2q^2\) vertices and \(q^3\) edges.

## Proof

**1. Exact distances.** Denote the retained points by \(P\), retained lines by \(L\), and the removed parallel class by \(\mathcal C\). There are \(q^2\) of each type. Two different points have graph distance two when their unique joining affine line is retained, and distance four when their joining line belongs to \(\mathcal C\). In the second case, choose any retained line through each point from distinct retained directions; they meet at a point, providing a four-edge path. Different retained lines have distance two when they intersect and distance four when they belong to the same retained parallel class: choose two points, one on each parallel line, with their joining line in another retained direction. An incident point and retained line have distance one; a nonincident point and retained line have distance three, via a retained line through the point meeting the given line. The latter exists since \(q\ge3\) and there are \(q\) retained directions. Bipartiteness and nonincidence rule out smaller parity-compatible distances. Thus \(G\) is connected, its diameter is four, and its first Betti number is
\[
b=|E(G)|-|V(G)|+1=q^3-2q^2+1.
\]

**2. The first threshold.** The graph is bipartite and triangle-free, so \(K_1=G\). Every connected graph is a wedge of its cycle-rank number of circles. At \(r=0\), there are \(2q^2\) isolated vertices.

**3. Same-part flag subcomplexes at threshold two.** Group the points by the \(q\) removed parallel lines. Two points are distance two precisely when they belong to **different** such groups; the point-only subcomplex \(A=K_2[P]\) is therefore the join of \(q\) discrete \(q\)-point sets, denoted \(D_q^{*q}\). The retained lines likewise fall into \(q\) parallel classes, each of size \(q\), so the line-only subcomplex \(B=K_2[L]\) is also \(D_q^{*q}\). The discrete space \(D_q\) has reduced integral homology of rank \(q-1\) in degree zero. The join formula, or induction by suspension of smash products, yields
\[
A\simeq B\simeq\bigvee^{(q-1)^q}S^{q-1}.
\]
Because \(q\ge3\), both are simply connected. These are integral homotopy equivalences, not just homology identities.

**4. A two-piece cover at threshold two.** Every mixed edge of \(K_2\) is an **incident** point–line pair (a nonincident pair is distance three). A clique cannot contain two distinct points and two distinct lines, since two points have at most one common affine line. Let \(P(\ell)\) be the points on retained line \(\ell\) and \(L(p)\) the retained lines through point \(p\). Define
\[
X=A\cup\bigcup_{\ell\in L}\Delta(\{\ell\}\cup P(\ell)),\qquad
Y=B\cup\bigcup_{p\in P}\Delta(\{p\}\cup L(p)).
\]
Every simplex of \(K_2\) lies in one of these two subcomplexes, since its mixed part has at most one vertex of one bipartition class. The intersection contains exactly all the vertices and the original incidence edges; indeed no all-point or all-line edge belongs to both, and no mixed triangle does. Thus \(X\cap Y=G\), literally.

Each cone attached to \(A\) in \(X\) has a unique new apex \(\ell\) and its entire base simplex \(\Delta(P(\ell))\) lies in \(A\). Elementary collapses delete the apex and all its incident faces relative to the base; the different apices do not interfere. Hence \(X\searrow A\), and symmetrically \(Y\searrow B\). Both pieces are simply connected; therefore the inclusion maps of the connected graph \(G\) into \(X\) and into \(Y\) are null-homotopic. As all inclusions of finite simplicial subcomplexes are cofibrations, the homotopy pushout for \(K_2=X\cup_G Y\) is the homotopy pushout of two null maps, yielding
\[
K_2\simeq A\vee B\vee\Sigma G
\simeq(\bigvee^{2(q-1)^q}S^{q-1})\vee(\bigvee^bS^2).
\]
Here \(\Sigma G\) denotes the reduced suspension up to homotopy; since \(G\simeq\bigvee^bS^1\), it is a wedge of \(b\) two-spheres. This proves the integral scale-two result, including the coincidence of dimensions for \(q=3\).

**5. The threshold-three join.** By Step 1, the *only* vertex pairs not joined in the distance-three graph are point pairs on the same deleted-class line and retained-line pairs in the same retained parallel class. These forbidden pairs partition \(V(G)\) into \(2q\) disjoint blocks, each of size \(q\). Consequently a simplex of \(K_3\) chooses at most one vertex from each forbidden block. Therefore, as a simplicial complex,
\[
K_3=D_q^{*(2q)}\simeq\bigvee^{(q-1)^{2q}}S^{2q-1}.
\]
At \(r\ge4\), every pair has distance at most four and \(K_r\) is the full simplex. Since distances are integral, these stages exhaust all real thresholds.

**6. Persistence.** The only nontrivial reduced homology degrees at thresholds one, two, and three are respectively degree one; degrees two and \(q-1\); and degree \(2q-1\). For \(q\ge3\) these three groups of degrees occur at disjoint thresholds. Their inclusions into the next threshold induce zero maps for degree reasons. Thus each stage's positive-dimensional classes are born at its own threshold and die at the next, giving the claimed all-field barcode. The integral wedge decompositions preclude torsion. \(\square\)

## Verification

The dependency-free Python 3 program `verify_affine_deletion.py` constructs the coordinate affine planes over prime fields of orders three and five, deletes one complete direction class, and independently computes every shortest-path distance. It checks the cardinalities, diameter, unique partitions into forbidden \(q\)-blocks, and all same-side and mixed distance cases. For the order-three case it exhaustively enumerates **all** faces of both \(K_2\) and \(K_3\), checks the exact two-subcomplex cover/intersection in Step 4, constructs mod-two simplicial boundary matrices, and computes their ranks by exact bitset elimination. The order-five case verifies the graph metric and structural partition without enumerating its exponentially many faces.

From the package directory run `python3 verify_affine_deletion.py` and compare with `verification_output.txt`. For \(q=3\), the program reports \(f(K_2)=(18,81,108,18)\) and \(\beta(K_2;\mathbf F_2)=(1,0,26,0)\); for \(K_3\), \(f=(18,135,540,1215,1458,729)\) and \(\beta=(1,0,0,0,0,64)\). It also verifies the order-five 10-block partition and all distance counts. The calculation is a finite consistency check; the proof for every existing affine plane (including non-Desarguesian planes) is Steps 1–6, independent of finite samples.

## Relationship to prior work

Adamaszek's archive-era *Clique complexes and graph powers* establishes graph-power Rips conventions, cycle-power examples, and girth-controlled square collapses; its girth-at-least-seven stability result does not apply to these girth-six incidence graphs. Larrión–Pizaña–Villarroel-Flores and Kawamura study structural relations and fundamental groups of clique complexes arising from bipartite graph squares, but do not provide the present three-stage all-order integral classification or the explicit high-dimensional third-stage join.

The closest published complete-affine-plane calculation (published result `3087baeea0a4`) retains **all** \(q+1\) parallel classes. Its graph has \(2q^2+q\) vertices and a scale-two wedge of spheres in degrees two and \(q\); it is already contractible at threshold three. Deleting an entire class changes both the vertex set and shortest-path metric and cannot be inferred by restricting that homotopy equivalence; the new graph retains nonzero homology at threshold three in dimension \(2q-1\). The prior projective-plane result (`c3740b96b3c3`) has every pair of lines intersect, so its one-sided flag complex is contractible; it does not determine this parallel-class deletion. The hexagon-packing result (`70b9bc9b3abb`) assumes edge-disjoint six-cycles, whereas these incidence graphs contain multiple hexagons sharing graph edges. Each closest statement and its full primary `RESULT.md` was compared.

The order-three graph is the Pappus incidence graph, for which related Čech-nerve and configuration-space calculations are **different** functors and do not determine this inclusive Rips filtration. No novelty is claimed for graph-power definitions, general join homology, homotopy-pushout techniques, or finite-plane axioms.

## Limitations

The theorem requires an existing affine plane and deletion of **exactly one entire parallel class**, and uses the shortest-path metric on the remaining incidence graph. It neither claims existence of planes of all integer orders nor applies verbatim to arbitrary nets, weighted graphs, or geometric-metric Rips complexes including edge interiors. The proof determines homotopy types and integral persistence but not natural automorphism representations or equivariant homotopy types. The literature search cannot exclude unindexed equivalent computations. The finite checks cover only prime orders three and five; they are not substitutes for the all-order proof.

## References

- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public version 2011-04-03), *Israel Journal of Mathematics* 196 (2013), 295–319. https://arxiv.org/abs/1104.0433
- F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The fundamental group of the clique graph*, *European Journal of Combinatorics* 30 (2009), 288–294. DOI: 10.1016/j.ejc.2007.12.006.
- K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, *Contributions to Discrete Mathematics* 6 (2011), 91–100. DOI: 10.55016/ojs/cdm.v6i2.62059.
- *Affine-plane incidence Rips complexes have two sphere dimensions*, full primary mathematical result (2026). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4/RESULT.md
- *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, full primary mathematical result (2026). https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3/RESULT.md
- *A hexagon-packing classification of scale-two graph Rips complexes*, full primary mathematical result (2026). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb/RESULT.md
