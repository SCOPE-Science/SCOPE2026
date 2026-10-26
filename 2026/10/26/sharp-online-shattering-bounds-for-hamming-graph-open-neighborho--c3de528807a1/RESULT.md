# Sharp online-shattering bounds for Hamming-graph open neighborhoods

## Finding
For every integer \(d\ge1\) and every alphabet size \(q\ge2\), let \(H(d,q)\) be the graph with vertex set \(\{0,\ldots,q-1\}^{d}\), adjacent vertices differing in exactly one coordinate. Let \(\mathcal N_{d,q}=\{\mathbf 1_{N(c)}:c\in V(H(d,q))\}\) be the binary concept class of all *open* neighborhoods; the query domain is the same vertex set. Then
\[
\operatorname{Ldim}(\mathcal N_{d,q})=\begin{cases}
1,&d=1\text{ or }(d,q)=(2,2),\\
2,&(d,q)=(3,2),\\
3,&d\ge2,\ q\ge3\text{ or }d\ge4,\ q=2.
\end{cases}
\]
In particular, \(\operatorname{Ldim}(\mathcal N_{2,3})=3\) although \(\operatorname{VCdim}(\mathcal N_{2,3})=2\). The sharp deterministic realizable mistake bound is at most three, independent of both the dimension and the alphabet size, and is attained already by the nine-center rook graph \(H(2,3)\).

## Assumptions and scope
All graphs and concept classes are finite. Repeated coordinate values are allowed, but the alphabet has at least two symbols. The neighborhood is *open*: \(c\notin N(c)\). We distinguish hypotheses extensionally; in \(H(2,2)\), opposite vertices give duplicate concepts. For any finite version space \(S\) of distinct binary functions, its Littlestone dimension is the maximum depth of a complete binary tree of instance queries such that every root-to-leaf labeled path is realized by some member of \(S\). We use \(\operatorname{Ldim}(S)=0\) for a singleton and, for nonempty \(S\), the recursion
\[
\operatorname{Ldim}(S)=\max_{x:\,S_x^0,S_x^1\ne\varnothing}\bigl(1+\min\{\operatorname{Ldim}(S_x^0),\operatorname{Ldim}(S_x^1)\}\bigr),
\]
with maximum of an empty set equal to zero. Here \(S_x^a\) comprises hypotheses assigning label \(a\) to \(x\). No equivalence-query model or graph-neighborhood homotopy invariant is asserted.

## Proof
**1. Hamming intersection geometry.** Fix vertices \(v,w\). If they agree, \(N(v)\cap N(w)=N(v)\). If they differ in one coordinate, then \(N(v)\cap N(w)\) consists of the \(q-2\) other values on their common coordinate line. If they differ in two coordinates, exactly the two intermediate vertices are common neighbors. If they differ in at least three coordinates, no vertex is adjacent to both. These assertions follow directly by counting the coordinates in which a possible common neighbor differs; they are also established as Lemmas 4.2–4.5 of Adler, Benediktsson and Macpherson [1].

**2. A coordinate-line restriction has dimension at most one.** Let \(L\) be the set of all vertices obtained by varying one coordinate while keeping the others fixed, and let \(A\subseteq L\) be any nonempty set of candidate centers. For an arbitrary query vertex \(x\), there are two possibilities: either \(x\in L\), when the positive centers of \(A\) are \(A\setminus\{x\}\), or \(x\notin L\), when at most one member of \(A\) is adjacent to \(x\). Thus every proper split of \(A\) has a side of cardinality at most one, so \(\operatorname{Ldim}(A)\le1\). Independently, a version space of at most two distinct concepts has Littlestone dimension at most one.

**3. Universal upper bound.** Regard centers as hypotheses and fix the result \(1\) of an initial query \(v\). The surviving centers form \(S=N(v)\). For any subsequent query \(w\), the positive side is \(N(v)\cap N(w)\). By Step 1 it is either the whole \(S\), the empty set, a subset of one coordinate line, or a two-element set. By Step 2, whenever a genuine split occurs its positive side has Littlestone dimension at most one. The recursion therefore gives \(\operatorname{Ldim}(S)\le2\). For an arbitrary initial query the positive branch always has this form, proving \(\operatorname{Ldim}(\mathcal N_{d,q})\le3\) for all parameters. This argument is uniform and does not use finite enumeration.

**4. Exceptional upper bounds.** For \(d=1\), \(H(1,q)\) is a complete graph, and a negative answer identifies the unique center equal to the query, so the dimension is at most one. In \(H(2,2)\), opposite vertices have identical open neighborhoods, leaving exactly two distinct hypotheses, so its dimension is at most one. For \(H(3,2)\), the three centers surviving any first positive answer are the three unit-coordinate neighbors of the queried vertex. Every further query either meets this set in zero vertices, in two vertices, or in all three. Consequently every proper split has one side of size one, giving \(\operatorname{Ldim}(N(v))\le1\) and hence \(\operatorname{Ldim}(\mathcal N_{3,2})\le2\).

**5. Explicit lower-bound trees.** The file `WITNESSES.json` contains complete, depth-three shattered query trees for \(H(2,3)\) and \(H(4,2)\), and a depth-two tree for \(H(3,2)\). Each leaf provides a concrete center whose open-neighborhood indicator realizes all labels along that path. For \(H(2,3)\), the root query is `00`; at depth two the queries are `12` after label zero and `11` after label one; the depth-three queries are `10`, `10`, `10`, and `20` in lexicographic label-path order. For \(H(4,2)\), the root query is `0000`; at depth two the queries are `0001` and `1100`; the depth-three queries are `0010`, `0010`, `1010`, and `1010`. These two trees witness dimension three. In \(H(3,2)\) the root is `000`, followed by `001` after zero and `110` after one, witnessing dimension two. Every nontrivial complete graph \(H(1,q)\) has two distinguishable neighborhood hypotheses, and so does \(H(2,2)\), proving the remaining lower bounds.

To see directly that \(\operatorname{VCdim}(\mathcal N_{2,3})\ge2\), the two query points `00` and `01` are statically shattered by the center queries `12` (neither), `10` (only `00`), `11` (only `01`), and `02` (both), respectively. The published upper bound of two for this case [1, Theorem 4.7] establishes equality.

For \(d\ge2,q\ge3\), the graph \(H(2,3)\) is an induced subgraph obtained by fixing extra coordinates and restricting two coordinates to three symbols. Likewise \(H(4,2)\) is an induced subgraph of every \(H(d,2)\) for \(d\ge4\). Queries and centers restricted to the subgraph retain the exact adjacency labels, so any shattered tree on the smaller graph transfers to the larger one. Combining with Steps 3–4 proves every case.

## Verification
Run `python3 VERIFY.py WITNESSES.json` from the directory containing both files; Python 3 and its standard library suffice. The verifier independently checks each leaf's full labeled path against direct Hamming distance, with 8, 8, and 4 root-to-leaf paths for the three trees. An independently implemented memoized game recurrence checks exact dimensions for \(H(1,q)\), \(2\le q\le6\); \(H(2,q)\), \(2\le q\le5\); \(H(3,2)\), \(H(3,3)\); and \(H(4,2)\). Additional finite checks directly test the intersection and coordinate-line premises for all \(1\le d\le4\), \(2\le q\le5\), with \(q^d\le256\). `VERIFIER_OUTPUT.txt` records the completed run and final `ALL_CHECKS_OK`. These experiments check examples and proof ingredients; the unrestricted parameter range follows only from the proof above.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1], particularly Section 4, study exactly the same neighborhood set system and prove the sharp *VC*-dimension and VC-density bounds. Their Lemmas 4.2–4.5 give the pairwise neighborhood-intersection geometry used and credited in Step 1. Their Theorem 4.7 implies \(\operatorname{VCdim}(\mathcal N_{2,3})=2\) and \(\operatorname{VCdim}(\mathcal N_{4,2})=3\), so the latter supplies a previously known lower bound of three on Littlestone dimension. Neither those VC results nor the pairwise intersection counts alone supply the complete adaptive classification: the uniform local-version-space argument and the depth-three \(H(2,3)\) tree provide the distinguishing steps. Housholder, Mangiapanello and Senger [2] develop VC-dimension thresholds for induced vertex subsets of Hamming graphs rather than the Littlestone dimension of the full neighborhood class. Chase, Freitag and Reyzin [3] concern general applications of Littlestone dimension to query learning and compression, not an exact Hamming-neighborhood formula.

## Limitations
The result concerns binary classification by single open neighborhoods on entire finite Hamming graphs, not unions of neighborhoods, other distance radii, arbitrary metric subspaces, or arbitrary product alphabets. It gives the optimal realizable online *mistake* bound, not PAC sample complexity or randomized label complexity. The original intersection lemmas and the static VC classification are explicitly credited to [1]. Relevant inspected sources do not establish an identical Littlestone formula, but no finite literature search proves global historical priority. Independent scientific audit is not represented as completed.

## References
[1] I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted 2020-07-31. https://arxiv.org/abs/2007.16042

[2] C. Housholder, L. Mangiapanello and S. Senger, *VC-dimension of subsets of Hamming graphs*, arXiv:2505.14641 (2025). https://arxiv.org/abs/2505.14641

[3] H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812 (2023); MFCS 2024. https://arxiv.org/abs/2310.04812
