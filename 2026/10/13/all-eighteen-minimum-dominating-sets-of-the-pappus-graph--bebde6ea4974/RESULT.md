# All eighteen minimum dominating sets of the Pappus graph

## Finding

Let \(H\) be the Pappus graph, the cubic incidence graph of the nine-point, nine-line Pappus configuration. A *dominating set* \(S\subseteq V(H)\) is one whose closed neighborhoods cover every vertex. Then

\[
\gamma(H)=5,\qquad \#\{S\subseteq V(H):S\text{ dominating},\ |S|=5\}=18.
\]

For **every** vertex \(v\in V(H)\), the five-vertex set

\[
S_v=N_H(v)\cup\{w\in V(H):d_H(v,w)=4\}
\]

is a minimum dominating set. These are all the minimum dominating sets, with distinct centers \(v\), and they form one orbit under graph automorphisms. Every such set is independent. Among the eighteen vertices, exactly its center is contained in three selected closed neighborhoods, and each of the other seventeen vertices is contained in one selected closed neighborhood. Thus the classification, not the previously tabulated scalar domination number, is the asserted new result.

## Assumptions and scope

Work over \(\mathbb F_3=\{0,1,2\}\), with arithmetic modulo three. The incidence structure has point vertices \(p_{i,a}\), for \(i\in\{0,1,2\}\) and \(a\in\mathbb F_3\), and line vertices \(\ell_{x,y}\), for \(x,y\in\mathbb F_3\). Its only edges are

\[
\ell_{x,y}\sim p_{0,x},\ p_{1,y},\ p_{2,x+y}.
\]

This is \(\mathrm{TD}(3,3)\), equivalently the affine plane of order three with one parallel class removed. Its Levi graph is the Pappus graph; an independent LCF model is checked in the supplied verifier. The graph has eighteen vertices, twenty-seven edges, and degree three. The definition of domination includes vertices in the selected set themselves (closed-neighborhood domination); pairs of points in distinct point classes lie on exactly one line, while points in one class lie on no common line. No assumptions about arbitrary cubic graphs are intended.

## Proof

**Lower bound and possible bipartition counts.** For any five selected vertices, each selected closed neighborhood contains four vertices. Since \(|V(H)|=18\), the degree-three volume bound gives \(|S|\ge\lceil18/4\rceil=5\). Suppose \(S\) is a dominating set of size five. Write \(a\) for the number of selected point-vertices and \(b\) for the number of selected line-vertices, so \(a+b=5\). The \(9-b\) unselected lines must have a selected point as a neighbor; likewise the \(9-a\) unselected points must have a selected line neighbor. Consequently

\[
9-b\le3a,\qquad 9-a\le3b.
\]

Substituting \(b=5-a\) gives \(a\ge2\) and \(a\le3\). Therefore the only cases are \((a,b)=(2,3)\) and \((3,2)\).

**Two selected points.** Let \(a=2\), \(b=3\). Exactly six line-vertices are unselected. The two selected points together are incident with at most six lines, and must dominate all six unselected ones. Equality requires that the two point neighborhoods are disjoint and contain no selected line. Two points in distinct point classes have a common line by the defining incidence rule; two points in the same class have disjoint line neighborhoods. The two selected points therefore occupy two of the three positions in one point class \(\{p_{i,0},p_{i,1},p_{i,2}\}\). All six lines incident with them are unselected. Hence the three selected lines must be precisely the three lines through the third, unselected point \(v\) in that class. Conversely these five vertices dominate every line: each line is incident with exactly one member of the chosen point class, so it is either selected or meets one of the two selected points. They dominate every point: the two chosen points belong to \(S\), the third point \(v\) meets all three selected lines, and each point in another class meets exactly one of those selected lines. There are three point classes and three choices of \(v\) in each, yielding exactly nine sets of this type. They are all independent because the selected lines pass through \(v\) rather than either selected point.

**Three selected points (dual case).** Let \(a=3\), \(b=2\). Dually, the six unselected point-vertices must be incident with the two selected lines, without any common incident point and without an incident selected point. In coordinates, lines \(\ell_{x,y}\) and \(\ell_{x',y'}\) share a point precisely when \(x=x'\), or \(y=y'\), or \(x+y=x'+y'\). For distinct pairs over \(\mathbb F_3\), all three inequalities hold exactly when \(x-y=x'-y'\). Thus the nine lines split into three disjoint *parallel classes* \(\{\ell_{x,y}:x-y=c\}\), each of size three. The two selected lines are two members of one such class; the remaining three selected vertices are precisely the three points of the third, unselected line \(v\). The converse domination verification is the dual of the previous paragraph: each point is either selected or lies on a selected line, and each line is either selected or meets one of the three selected points. There are again \(3\cdot3=9\) choices and all are independent.

**Canonical center, uniqueness, and coverage.** For any point \(v=p_{i,a}\), the two other members of its point class have distance four from \(v\), whereas any point in another point class has distance two. The three neighbors of \(v\) are its incident lines. The dual statement for a line \(v\) follows from the three line parallel classes. Therefore the eighteen sets classified above are exactly \(S_v=N_H(v)\cup\{w:d_H(v,w)=4\}\). Each set has one and only one vertex contained in three of its selected closed neighborhoods: \(v\), which is adjacent to all three selected vertices opposite its own bipartition side. All other vertices have one selected closed-neighborhood witness, by the incidences in the two preceding paragraphs. Thus \(v\) is uniquely recovered from \(S_v\), proving distinctness.

**One automorphism orbit.** Translations \((x,y)\mapsto(x+c,y+d)\), with corresponding point translations \(p_{0,a}\mapsto p_{0,a+c}\), \(p_{1,a}\mapsto p_{1,a+d}\), \(p_{2,a}\mapsto p_{2,a+c+d}\), act transitively on the nine line-vertices and within each of the three point classes. The class-cycle \(p_{0,a}\mapsto p_{1,-a}\), \(p_{1,a}\mapsto p_{2,a}\), \(p_{2,a}\mapsto p_{0,a}\), \(\ell_{x,y}\mapsto\ell_{x+y,-x}\) preserves the incidence rule and cycles the point classes. Thus the automorphisms act transitively separately on the line and point sides. Finally label \(p_{i,a}\) by \(3i+a\) and \(\ell_{x,y}\) by \(9+3x+y\). The permutation whose images in order of labels zero through seventeen are

`(9,13,17,10,14,15,11,16,12,0,6,3,4,1,8,7,5,2)`

is a point–line duality, verified directly by substituting the incidence table. These maps together are vertex-transitive. The canonical construction \(v\mapsto S_v\) is equivariant under automorphisms, so all eighteen optimum sets lie in one orbit. No computation of the full automorphism group is needed for this conclusion. This completes the unrestricted proof.

## Verification

The standalone pure-standard-library program `verify.py` builds the stated \(\mathrm{TD}(3,3)\) incidence graph and independently builds a Hamiltonian LCF model with sequence \([5,7,-7,7,-7,-5]^3\). It verifies an explicit isomorphism, checks all \(2^{18}=262144\) vertex subsets against closed-neighborhood domination, and confirms that precisely eighteen five-vertex sets attain the minimum. It compares those sets with all eighteen distance-four canonical sets, verifies uniqueness of each threefold-dominated center and the other seventeen singleton coverage multiplicities, and constructs a transitive group of 216 verified automorphisms. A successful run prints four `VERIFY_OK` lines. The finite checks are independent corroboration; the proof above establishes the classification without extrapolation.

Run with `python3 verify.py` in the directory containing this result. The verifier has no third-party package dependencies, external data sources, or network operations.

## Relationship to prior work

The Pappus graph and its incidence description are classical; the cubic graph is explicitly studied in Abreu, Labbate, and Sheehan's paper on pseudo two-factor isomorphism and in Goedgebeur's related work. Their stated theorems concern two-factor structure, not minimum dominating-set multiplicities. The **minimum domination number five is already listed in House of Graphs**, and is not claimed to be new. The separate study by Héger and Nagy classifies small dominating sets of **projective-plane** incidence graphs, which have a different incidence structure and are not the eighteen-vertex graph obtained by deleting a parallel class from \(\mathrm{AG}(2,3)\). A later paper on partially balanced incomplete block (PBIB) designs constructed from the Pappus graph studies edge/path association schemes, not minimum ordinary dominating sets. The present claim is the exhaustive structural classification, multiplicity, and automorphism orbit of minimum dominating sets for this specific cubic Levi graph.

## Limitations

This theorem is for the Pappus graph, not for every graph of degree three or every transversal design. It does not enumerate dominating sets of cardinality larger than five or assert anything about minimum *total*, *independent*, or *paired* domination numbers beyond the independence of the eighteen minimum ordinary dominating sets proved here. Published summaries and indexed literature searches may omit earlier tables or an equivalent statement under different incidence-geometric terminology; independent priority checking remains advisable. No independent mathematical audit has been performed.

## References

1. M. Abreu, D. Labbate, J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1 (9 February 2010), https://arxiv.org/abs/1002.1891.
2. J. Goedgebeur, *A counterexample to the pseudo 2-factor isomorphic graph conjecture*, arXiv:1412.3350v1 (10 December 2014), https://arxiv.org/abs/1412.3350.
3. T. Héger, Z. L. Nagy, *Dominating sets in projective planes*, arXiv:1603.02933v1 (9 March 2016), https://arxiv.org/abs/1603.02933.
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html.
5. House of Graphs, *Pappus Graph*, graph record 1248, https://houseofgraphs.org/graphs/1248.
6. *PBIB Designs Constructed Through Edges and Paths of Graphs*, International Journal of Mathematics Trends and Technology 66(5), 2020, https://ijmttjournal.org/public/assets/volume-66/issue-5/IJMTT-V66I5P509.pdf.
