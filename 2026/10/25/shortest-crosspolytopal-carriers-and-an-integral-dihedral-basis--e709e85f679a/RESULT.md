# Shortest crosspolytopal carriers and an integral dihedral basis for the Brinkmann independence complex

## Finding
Let \(B\) be the 21-vertex Brinkmann graph and \(K=\operatorname{Ind}(B)\) its ordinary independence complex. Then
\[
K\simeq\bigvee^7 S^4,\qquad
\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^7.
\]
Every other reduced integral homology group vanishes. A nonzero fourth-homology class supported on an induced subcomplex needs at least ten graph vertices. Exactly 21 supports attain that bound; each is five disjoint graph edges and hence carries the octahedral four-sphere \( (S^0)^{*5}\). All 21 inclusion classes are primitive. The full automorphism group \(D_7\) has three orbits of seven such spheres. Two distinct orbits each form a unimodular basis of the entire integral fourth homology, while the third has rank six. For either basis orbit,
\[
\widetilde H_4(K;\mathbb Z)\cong_{\mathbb Z[D_7]}\mathbb Z[D_7/\langle s\rangle],
\]
where \(s\) is a reflection. This is an **integral** permutation-lattice isomorphism; it does not merely compare rational characters.

## Assumptions and scope
The graph is explicitly specified on the vertex set \(\{0,1,\ldots,20\}\): in the following adjacency encoding each pair with first endpoint the dictionary key is an undirected edge, and no other edges occur.

```python
ED={0:[2,5,7,13],1:[3,6,7,8],2:[4,8,9],3:[5,9,10],
    4:[6,10,11],5:[11,12],6:[12,13],7:[15,20],
    8:[14,16],9:[15,17],10:[16,18],11:[17,19],
    12:[18,20],13:[14,19],14:[17,18],15:[18,19],
    16:[19,20],17:[20]}
```

This is the graph encoded in the independently available SageMath Brinkmann graph generator. A face of \(K\) is any independent vertex subset, with the empty face included. All homology is reduced unless explicitly indicated, and oriented simplices use increasing vertex labels. A geometric carrier on a set \(W\) means a class in the image of \(\widetilde H_4(K[W];\mathbb Z)\to\widetilde H_4(K;\mathbb Z)\).

The two explicit automorphisms used below are permutations written as lists of images of \(0,1,\ldots,20\):

```python
r=(1,2,3,4,5,6,0,8,9,10,11,12,13,7,15,16,17,18,19,20,14)
s=(0,6,5,4,3,2,1,13,12,11,10,9,8,7,20,19,18,17,16,15,14)
```

They satisfy \(r^7=s^2=1\), \(srs=r^{-1}\), and generate all 14 graph automorphisms.

## Proof
**Exact integral Morse reduction.** Enumerating all nonempty independent subsets gives the face vector, by simplex dimension,
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(21,168,658,1344,1400,665,106).
\]
For each vertex \(v=0,\ldots,20\) in order, pair the currently unmatched face \(\sigma\) with \(\sigma\cup\{v\}\) whenever both remain unmatched; traverse candidate faces by the deterministic order implemented in the accompanying checker. This matches 2,176 pairs, leaving one critical vertex, eight critical four-faces, and one critical five-face. Directly orienting each unpaired face incidence downwards and each paired incidence upwards gives a directed graph with 4,362 nodes and 19,418 arrows. A complete topological sort visits every node, verifying acyclicity. The integral Morse boundary of the sole critical five-cell, in increasing order of critical four-faces, is
\[
\partial_5^{\mathrm M}=(1,-2,1,1,-1,-1,1,-1).
\]
This boundary vector is primitive. The Morse model is a point with eight four-cells and one five-cell, so its attaching map \(S^4\to\bigvee^8S^4\) represents this vector in \(\pi_4(\bigvee^8S^4)\cong\mathbb Z^8\). A unimodular change of basis reduces it to a unit coordinate, cancelling one four-cell against the five-cell, giving \(\bigvee^7S^4\). In particular there is no integral torsion.

**Sharp support threshold.** A general flag-complex lemma states that if an induced subcomplex carries a nonzero reduced degree-\(d\) homology class then its vertex support has cardinality at least \(2d+2\). For \(d=0\), two disconnected vertices are necessary. Inductively, choose a support \(W\) minimal under deletion that still carries the class, and consider any \(v\in W\). Since deleting \(v\) kills that class, the deletion–link exact sequence makes \(\widetilde H_{d-1}(\operatorname{lk}_{K[W]}(v))\ne0\). The link must have at least \(2d\) vertices by induction. As the complex is not a cone, \(v\) has at least one forbidden neighbor among the remaining vertices, proving \(|W|\ge2d+2\). If equality holds, each vertex has exactly one forbidden neighbor; hence the missing edges form a perfect matching and the induced flag complex is \((S^0)^{*(d+1)}\). The same argument applies to the smallest support carrying any nonzero image class in the ambient homology. With \(d=4\), the sharp bound is ten.

**Exact minimal-carrier census and coordinates.** A ten-vertex carrier must therefore be the complement of five forbidden pairs, i.e. its induced graph must be five vertex-disjoint edges and no others. Exhaustive recursive enumeration of five-edge induced matchings of the displayed graph gives exactly 21. For an induced matching \(\{(a_j,b_j):1\le j\le5\}\), the fundamental cycle is the signed sum
\[
 z=\sum_{\epsilon\in\{0,1\}^5}(-1)^{\sum_j\epsilon_j}
 [c_1(\epsilon_1),\ldots,c_5(\epsilon_5)],
\]
with \(c_j(0)=a_j\), \(c_j(1)=b_j\), and brackets oriented by increasing vertex labels. Each one has zero simplicial boundary. The displayed Morse differential, whose first entry is one, identifies the integral homology coordinates with the seven remaining critical four-cell coordinates after eliminating the first by the boundary vector. Every one of the 21 cycles has coordinate gcd one, so all are primitive and nontrivial.

**The two integral orbit bases.** The 14 automorphisms split the 21 induced matchings into three seven-element orbits. The orbit seeded by
\[
\{(0,7),(3,9),(4,11),(8,16),(12,18)\}
\]
has an explicit seven-by-seven matrix of projected coordinates for its successive images under \(r\):

```text
-1  1  0 -1  0  0  0
-1  1  0  0 -1  1 -1
-1  0  0  0 -1  1  0
-1  0  0 -1  0  0  0
-1  1  0 -1  0  1  0
-1  1  1  0 -1  1 -1
-1  0  0  0  0  0  0
```

Its exact determinant is \(+1\). A second orbit, seeded by \(\{(0,7),(3,9),(6,12),(8,14),(11,19)\}\), has determinant \(-1\) in the same integral coordinates. The remaining orbit has rank six. Thus either of the first two is an integral homology basis. For the first basis orbit \(z_j=r^jz_0\) (indices modulo seven), the reflection satisfies \(s z_j=z_{-j}\) with no sign. The rotation cyclically permutes the basis. Therefore the full **integral** action is exactly that on the seven cosets of a reflection subgroup, as claimed. The second basis orbit also has unsigned permutation action, with a shifted reflection axis.

## Verification
Execute `python verify_brinkmann.py` after installing the versions specified in `requirements.txt`. The program rebuilds the entire 4,362-face complex, certifies the acyclic 2,176-pair matching, evaluates the signed integral Morse differential, enumerates all 21 induced five-matchings, checks their actual simplicial boundaries and integer homology coordinates, exhaustively computes all 14 graph automorphisms, and checks the three orbit ranks, determinant units and reflection signs. Its final status line is `VERIFY_OK_BRINKMANN_INTEGRAL_SHORTEST_SPHERE_ORBITS`. These finite exhaustive verifications prove the specific displayed graph calculation; the general ten-vertex threshold uses the preceding induction, not extrapolation from finite tests.

## Relationship to prior work
Brinkmann and Meringer introduced the distinguished graph in the study of minimum-order four-regular four-chromatic graphs of girth five. Meringer's later graph-generation work cites their 1997 note. Engström's 2005 paper develops independence-complex topology, particularly folds and classes of directed-tree and anti-Rips constructions, but does not compute this Brinkmann graph or its integral automorphism lattice. The new statement refines the mere homotopy rank with two explicit unimodular shortest-support orbit bases. General flag-complex support bounds alone do not imply the graph-specific census, integral basis or dihedral action. Other graph homology calculations for different named graphs do not determine this one.

## Limitations
This is an exact theorem only for the explicitly encoded Brinkmann graph and its ordinary independence complex; no classification of all four-regular girth-five graphs is asserted. The oldest 1997 source was accessible through its bibliographic record and abstract, but its full text could not be inspected; a relevant result hidden there or in unindexed work is a residual priority risk. The 1999-03-15 public-source date attached to this finding is the earliest fully day-verified consulted source explicitly citing the graph, not its actual 1997 initial publication date. The graph-specific finite checks are reproducible but have not received independent mathematical audit.

## References
1. G. Brinkmann and M. Meringer, *The Smallest 4-Regular 4-Chromatic Graphs with Girth 5*, Graph Theory Notes of New York **32** (1997), 40–41 (primary graph source; full text unavailable during this comparison).
2. M. Meringer, *Fast Generation of Regular Graphs and Construction of Cages*, Journal of Graph Theory **30** (1999), 137–146; first published 1999-03-15. DOI: `10.1002/(SICI)1097-0118(199902)30:2<137::AID-JGT7>3.0.CO;2-G`.
3. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:`math/0508148v1`, initially public 2005-08-08; sections 2–4 inspected.
4. SageMath, `BrinkmannGraph` implementation, `sage/graphs/generators/smallgraphs.py`, public source-code graph encoding, `https://github.com/sagemath/sage/blob/develop/src/sage/graphs/generators/smallgraphs.py`.
