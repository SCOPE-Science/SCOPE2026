# Five exact higher-independence homotopy types for Möbius ladders and their dihedral characters

## Finding
Let \(M_{2n}\) be the Möbius ladder. For the **two-independence** (also called dissociation) complex, five consecutive natural cases admit exact **integral homotopy** classifications:

| \(n\) | Graph | Homotopy type of \(\operatorname{Ind}_2(M_{2n})\) | Critical sphere dimension | Sphere rank |
|---|---|---|---|---|
| 4 | \(M_8\), Wagner graph | \(S^2\) | 2 | 1 |
| 5 | \(M_{10}\) | \(\bigvee^9 S^3\) | 3 | 9 |
| 6 | \(M_{12}\) | \(\bigvee^6 S^3\) | 3 | 6 |
| 7 | \(M_{14}\) | \(S^4\) | 4 | 1 |
| 8 | \(M_{16}\) | \(\bigvee^{31} S^5\) | 5 | 31 |

These cases cover every residue class of \(n\) modulo \(4\) and the first repetition. Each homotopy equivalence is proved by a finite, completely specified acyclic discrete-Morse matching, **not** by extrapolation. The natural dihedral action \(D_{2n}\), of order \(4n\), has an explicitly determined rational character on the unique nonzero reduced homology group in each case.

Define \(r(i)=i+1\) and \(s(i)=-i\), with indices taken modulo \(2n\). The following rows give \(\chi(r^k)\) and \(\chi(sr^k)\), respectively, for \(0\le k<2n\). Each character is on reduced rational homology in the stated sphere dimension:

| \(n\) | Rotation characters | Reflection characters | Dimension of invariant homology |
|---|---|---|---|
| 4 | \((1,-1,1,-1,1,-1,1,-1)\) | \((-1,1,-1,1,-1,1,-1,1)\) | 0 |
| 5 | \((9,1,-1,1,-1,1,-1,1,-1,1)\) | \((1,1,1,1,1,1,1,1,1,1)\) | 1 |
| 6 | \((6,1,-1,-2,3,1,2,1,3,-2,-1,1)\) | \((0,2,0,2,0,2,0,2,0,2,0,2)\) | 1 |
| 7 | \((1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1)\) | \((1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1)\) | 0 |
| 8 | \((31,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1)\) | \((-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3)\) | 0 |

## Assumptions and scope
For \(n\in\{4,5,6,7,8\}\), take the finite simple graph on \(\{0,1,\ldots,2n-1\}\) with undirected edges \(\{i,i+1\}\) for indices modulo \(2n\) and \(\{i,i+n\}\) for \(0\le i<n\). A subset \(F\) is a face of \(\operatorname{Ind}_2(M_{2n})\) precisely when every component of the induced graph on \(F\) has at most two vertices. Equivalently, no vertex of \(F\) has two distinct neighbors in \(F\); equivalently, \(F\) contains no three-vertex subset with at least two induced edges. The empty face is included as usual but is not a nonempty cell of the face poset used below. The sphere-wedge assertions are assertions of ordinary integral homotopy equivalence for **exactly** these five graphs. Rational dihedral modules are determined by character values; no claim of equivariant homotopy equivalence is made.

## Proof
**Step 1 — reconstruct all faces.** Use a bitmask \(f\in\{1,\ldots,2^{2n}-1\}\) for a nonempty subset. Test that, for each bit \(i\) present, the intersection of the bitmask with the three graph neighbors of \(i\) has cardinality at most one. This constructs the entire abstract simplicial complex without truncation. The resulting nonempty-face counts for \(n=4,5,6,7,8\) are respectively \(78,232,685,2046,6078\).

**Step 2 — define explicit matched face pairs.** Starting with all nonempty faces unmatched, process the vertex labels in this fixed order:

```
4: [7,2,3,6,4,0,5,1]
5: [6,0,4,8,2,5,1,7,9,3]
6: [7,8,3,1,4,10,6,11,2,9,0,5]
7: [0,2,10,12,8,4,1,11,5,3,6,13,7,9]
8: [10,3,5,2,4,15,11,12,0,1,6,7,14,9,13,8]
```

At each stage labeled \(v\), match **every** presently unmatched face \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\), provided the latter is also presently unmatched. Remove both partners permanently before the next stage. The explicit program `check_matching.py` deterministically reconstructs all such pairs; no unprovided certificate file is required.

**Step 3 — check the entire gradient graph, not just critical counts.** Form the full Hasse diagram of nonempty faces: one directed edge for every inclusion of codimension one. Reverse orientation along each chosen matched edge (from smaller to larger); orient every other covering edge from larger to smaller. Topological sorting traverses *all* vertices, ruling out directed cycles and hence certifying an acyclic partial matching. For the five cases, the total covering-relation counts are \(192,720,2556,8946,30384\), and the matching-pair counts are \(38,111,339,1022,3023\). The complete sets of unmatched faces have critical-cell signatures, respectively, \(\{0:1,2:1\}\), \(\{0:1,3:9\}\), \(\{0:1,3:6\}\), \(\{0:1,4:1\}\), and \(\{0:1,5:31\}\), where keys denote dimensions. All of these are recomputed from the finite edge and face definitions, rather than assumed as input to acyclicity.

**Step 4 — conclude integral homotopy.** Forman's discrete Morse theorem gives a CW complex with one zero-cell and, for each case, exactly the displayed number of cells in one fixed dimension \(d\ge2\), with no other cells. All attaching maps for those \(d\)-cells factor through the single zero-cell because there are no intermediate-dimensional cells. Such a CW complex is a wedge of the indicated number of \(d\)-spheres. This proves each integral homotopy equivalence, not merely a field-homology calculation.

**Step 5 — determine dihedral characters.** Define the simplicial action by permuting vertex labels with \(r(i)=i+1\) and \(s(i)=-i\). For every \(g\in D_{2n}\), the trace of its action on the oriented simplicial chain group of dimension \(j\) is the signed count of \(g\)-fixed \((j+1)\)-vertex faces, with sign given by the orientation permutation. The alternating sum of these traces, minus the empty-face correction \(1\), equals the reduced Lefschetz number. As reduced homology is nonzero only in degree \(d\), the trace on \(\widetilde H_d\) is \((-1)^d\) times that reduced Lefschetz number. The independent program `check_homology_symmetry.py` computes all \(4n\) elements' signed traces and gives the displayed characters. Averaging each full character over the group yields the displayed invariant dimension.

## Verification
The two separately implemented Python programs and their exact recorded standard outputs are embedded with this result. Run them with Python 3 (standard library only):

```
python3 check_matching.py
python3 check_homology_symmetry.py
```

`check_matching.py` enumerates all nonempty faces, constructs **every** matched pair, enumerates **every** codimension-one covering relation, checks the complete directed gradient graph for acyclicity by topological sorting, and tests the complete critical signature. `check_homology_symmetry.py` reconstructs the same faces by a logically different test (absence of a connected induced triple), independently computes all mod-two boundary ranks, and calculates signed Lefschetz characters for all rotations/reflections. Its homology cross-check is mod-two only; the **integral homotopy** conclusion instead follows from the acyclic matching with only zero-dimensional and \(d\)-dimensional critical cells. Recorded output is not itself a substitute for re-executing and examining the supplied algorithms.

## Relationship to prior work
Agarwal and Basak, arXiv:2608.30601 (first version August 31, 2026; revised version September 14, 2026), determine the homotopy types of **ordinary** independence and perfect-matching complexes of Möbius and circular ladders, with a periodic dependence on the ladder parameter. Their main results and the full accessible revised primary text were examined: the complexes there are not the **two-independence** complexes classified here, and their stated theorems do not imply these five homotopy types or the present dihedral characters. Deshpande and Singh (2021) investigate higher-independence complexes of several different graph families, including complete multipartite graphs, whiskered graphs, cycles, and certain trees. Published matching-complex and total-cut-complex records for Möbius ladders also concern different face predicates. The neighboring untwisted pentagonal prism has a separately reported two-independence homotopy type of eleven three-spheres; the twisted ten-vertex ladder here yields nine. Similar graph names therefore do not imply identical topological statements.

## Limitations
The finding establishes **five particular values only**; it neither proves a periodic law nor classifies \(\operatorname{Ind}_2(M_{2n})\) for \(n\ge9\). Nonzero homology representations are determined over \(\mathbb Q\), not an integral equivariant module isomorphism. The proof uses exhaustive finite combinatorics up to sixteen graph vertices, with source code and two distinct face-enumeration strategies available for reproduction. Identified literature and published-record comparisons are substantial but do not exclude unindexed or unavailable earlier equivalences; originality remains subject to later independent checking. No independent scientific audit has been performed.

## References
1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, first public arXiv version August 31, 2026, arXiv:2608.30601v1. https://arxiv.org/abs/2608.30601v1 .
2. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (September 14, 2026), complete primary text https://arxiv.org/html/2608.30601v2 .
3. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, Journal of the Ramanujan Mathematical Society 36 (2021), 53–71, https://www.mathjournals.org/jrms/2021-036-001/2021-036-001-007.html .
4. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650 .
