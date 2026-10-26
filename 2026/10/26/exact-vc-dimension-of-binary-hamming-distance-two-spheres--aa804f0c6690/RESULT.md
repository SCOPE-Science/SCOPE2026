# Exact VC dimension of binary Hamming distance-two spheres

## Finding
For each integer \(d\ge1\), equip \(Q_d=\{0,1\}^d\) with Hamming distance. Define the *exact-distance-two sphere family* (not the family of radius-two balls) by
\[\mathcal S_{d,2}=\bigl\{S_2(c):c\in Q_d\bigr\},\qquad S_2(c)=\{x\in Q_d:d_H(x,c)=2\}.\]
Then
\[\boxed{\operatorname{VCdim}(Q_d,\mathcal S_{d,2})=\begin{cases}
0,&d=1,\\
1,&d=2,\\
2,&d\in\{3,4\},\\
3,&d=5,\\
4,&d=6,\\
5,&d\ge7.
\end{cases}}\]
Thus the distance-two relation on the Boolean cube has uniformly bounded VC dimension, and the sharp stable bound is attained first in dimension seven.

## Assumptions and scope
All centers and tested points lie in the same whole binary cube. Distances are **equal to** two, not at most two. A finite set \(F\subseteq Q_d\) is shattered when the traces \(S_2(c)\cap F\), as \(c\) ranges over all cube vertices, equal all \(2^{|F|}\) subsets of \(F\). In dimension one all spheres are empty. No conclusion is claimed for alphabets other than binary or for radii other than exactly two.

## Proof
**1. Anchor and graph encoding.** If a nonempty finite \(F\) is shattered, some sphere contains the whole of \(F\). Translation by its center under bitwise XOR preserves all Hamming distances; therefore we may suppose \(F\subseteq S_2(0)\). Every member of \(F\) then has precisely two unit coordinates and is identified with an edge of the complete simple graph on the coordinate set. If \(|F|=6\), the associated simple graph has six distinct edges and a support \(V\) of \(s\le12\) nonisolated vertices. Permutations of coordinates identify isomorphic such edge systems.

**2. Universal finite trace reduction.** Fix an anchored set \(F\) of six weight-two points. For any center \(c\) and any edge \(x\in F\),
\[d_H(x,c)=|c|+2-2|\operatorname{supp}(x)\cap\operatorname{supp}(c)|.\]
A center hitting at least one member of \(F\) must therefore have \(|c|\in\{0,2,4\}\). For nonzero weight \(w\in\{2,4\}\), set \(R=\operatorname{supp}(c)\cap V\), \(a=|R|\). Its trace consists of precisely the graph edges \(e\) satisfying
\[|e\cap R|=w/2,\qquad 0\le w-a\le4.\]
Coordinates outside \(V\) are indistinguishable to all the edges of \(F\); only their number \(w-a\) matters. Thus every *nonempty* trace possible in any ambient dimension already occurs in a model with exactly four additional available coordinates. The center zero realizes the full trace. We may safely grant the empty trace without checking its realizability. Consequently, if this finite over-approximation lacks a pattern, no six-set can be shattered in any dimension.

**3. Complete graph-type certificate.** The attached `verify.py` recursively enumerates all simple graphs without isolated vertices having up to six edges. To add one new edge, it considers (i) two old vertices, (ii) one old and one fresh vertex, and (iii) two fresh vertices, then discards duplicates by exact graph isomorphism. This procedure is exhaustive by deleting any edge and discarding newly isolated vertices. It produces respectively \(1,2,5,11,26,68\) unlabeled graph types for edge counts one through six. For every six-edge representative, it exhaustively forms all \(R\subseteq V\) of sizes zero through four and all admissible center weights \(w\in\{2,4\}\). The verified maximum number of different masks, **even after granting empty and full masks for free**, is \(49<64\). Therefore no shattered six-set exists. Since shattering is hereditary, no shattered set has size greater than five.

**4. Sharp witnesses.** For \(d\ge7\), with coordinate indices \(0,\ldots,d-1\), take the five points with supports \(\{0,i\}\), \(1\le i\le5\), and use coordinate six as a spare. An arbitrary desired subset \(T\subseteq\{1,\ldots,5\}\) is realized as follows (all displayed sets are supports of centers):

- \(|T|=0\): take four of the five leaf coordinates, omitting coordinate zero.
- \(|T|=1\): take the chosen leaf and spare coordinate six.
- \(|T|=2\): take exactly the two chosen leaves.
- \(|T|=3\): take coordinate zero and the three chosen leaves.
- \(|T|=4\): take coordinate zero and the one omitted leaf.
- \(|T|=5\): take the zero center.

The distance identity in step two checks that these center supports produce exactly the six cardinality classes of traces specified. Padding these centers by zero coordinates proves the lower bound for every larger \(d\).

**5. Small dimensions.** By the anchor reduction, to exclude a shattered set of size \(k\) in dimension \(d\) it suffices to examine all \(k\)-subsets of the \(\binom d2\) points in \(S_2(0)\) against every one of the \(2^d\) centers. The checker excludes a shattered set of sizes \(3,3,4,5\) for \(d=3,4,5,6\), examining respectively \(1,20,210,3003\) candidates. It also exhibits (by complete trace checks) star witnesses of sizes \(2,2,3,4\) in those dimensions. At \(d=2\) every sphere is a singleton; thus VC dimension is one. At \(d=1\) all spheres are empty. These cases and the universal six-set obstruction complete the classification.

## Verification
Run `python -m pip install -r requirements.txt` followed by `python verify.py` in a directory containing the two files. The script prints the graph-type counts \(1,2,5,11,26,68\), the all-types six-edge maximum of \(49\) traces, the small-dimensional exhaustive exclusion totals \(1,20,210,3003\), and independently verifies the five-star witness. The code uses exact integers and exact graph-isomorphism tests, not random samples. The correctness of the infinite-dimensional reduction is the mathematical proof above; executing the program checks the finite kernel of that proof.

## Relationship to prior work
Adler, Benediktsson and Macpherson study the **distance-one edge relation** (open neighborhoods) of Johnson and Hamming graphs and establish the Hamming VC upper bound three [1, Sections 1 and 4]; it concerns another binary relation. Coudert, Csikós, Ducoffe and Viennot develop general algorithms for **closed neighborhoods**, including hardness and experiments [2, Sections 3–6]. Neither inspected paper supplies the exact-distance-two Hamming-sphere formula. The distance-two relation is the open-neighborhood relation of the disjoint union of two parity-isomorphic halved-cube graphs; the *whole* disjoint union is essential, since the other parity supplies an empty trace. This is not the distance-one Hamming graph. A radius-two *ball* includes layers zero and one as well as layer two; its shattering dimension does not determine the sphere dimension because subtraction of set families is not an implication-preserving operation. The exact ball classification \(\operatorname{VCdim}=4\) in sufficiently high dimensions, when available, does not imply this radius-two *sphere* classification of value five.

## Limitations
The upper bound is a computer-assisted exact finite proof: the graph-type census and maximum-trace assertion require the supplied checker and the correctness of its graph isomorphism routine. Independently checking the kernel in another system would strengthen the certificate. A literature search of equivalent terms ('second-distance graph', 'halved cube', 'Hamming sphere', and 'distance-two relation') found no decisive prior theorem, but cannot establish absolute priority. No claim of new results on the known ordinary Hamming distance-one relation, on closed radius-two balls, on general q-ary cubes, or on independent external validation is made.

## References
[1] I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted 2020-07-31, https://arxiv.org/pdf/2007.16042 (especially Theorem 1.1 and Section 4).

[2] D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1, publicly posted 2024-05-13, https://arxiv.org/pdf/2405.07588 (especially Sections 2–6).
