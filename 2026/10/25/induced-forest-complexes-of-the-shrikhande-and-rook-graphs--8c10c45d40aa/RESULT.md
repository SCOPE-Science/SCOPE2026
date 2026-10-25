# Induced-forest complexes of the Shrikhande and rook graphs

## Finding

For a finite simple graph \(G\), let \(\mathcal F(G)\) denote the simplicial complex of all vertex subsets \(A\subseteq V(G)\) for which the induced graph \(G[A]\) is a forest. Let \(\mathrm{Sh}\) be the sixteen-vertex Shrikhande graph, and let \(R=K_4\square K_4\) be the sixteen-vertex rook graph. There are integral homotopy equivalences

\[
\mathcal F(\mathrm{Sh})\simeq \bigvee^{141}S^5\vee\bigvee^{36}S^6,
\qquad
\mathcal F(R)\simeq \bigvee^{33}S^5\vee\bigvee^{72}S^6.
\]

Both graphs have strongly regular parameters \((16,6,2,2)\), exactly thirty-two triangles, and maximum induced-forest order seven. Thus their equal strongly regular parameters and equal minimum feedback-vertex-set number nine do not determine the integral homotopy type of the induced-forest complex.

## Assumptions and scope

All graphs are finite, simple, undirected and loopless. Label the vertices of each graph by integers \(4a+b\) for \((a,b)\in\{0,1,2,3\}^2\). The vertices of \(\mathrm{Sh}\) are adjacent exactly when their difference modulo four is one of \((1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\). The vertices of \(R\) are adjacent exactly when they have equal first or equal second coordinate (and are distinct).

The face \(A\) is encoded by its sixteen-bit indicator mask \(m(A)=\sum_{v\in A}2^v\). In the augmented complex, the empty face is included for reduced homology. A face with \(k\) vertices has simplicial dimension \(k-1\). The claimed equivalences concern the underlying geometric realizations; no equivariant claim is made.

## Proof

**Face enumeration and graph consistency.** The independent verifier checks the common-neighbor condition for every pair of graph vertices; both graphs have degree six, every distinct pair has exactly two common neighbors, and both have thirty-two triangles. For every one of the \(2^{16}=65,536\) vertex subsets, two distinct acyclicity algorithms agree: union-find rejects the first edge closing a cycle, while a depth-first traversal detects a nonparent visited neighbor. The numbers of faces of cardinalities \(0,1,\ldots,7\) are, respectively,

\[
(1,16,120,528,1440,2352,1952,512) \quad\text{for }\mathrm{Sh},
\]
\[
(1,16,120,528,1392,2160,1728,576) \quad\text{for }R.
\]

No larger faces exist. In particular, both have maximum induced-forest size seven, while their reduced Euler characteristics are \(-105\) and \(39\).

**Acyclic matching certificate.** Order the faces by increasing binary mask. Starting with every face unmatched, for each vertex index \(v=0,1,\ldots,15\), traverse this order and match \(m\) with \(m+2^v\) whenever \(v\notin m\) and both faces are still unmatched. The complete matched face-poset Hasse diagram is directed upward along pairs and downward along all other codimension-one incidences. Topological sorting visits all vertices of each directed graph, proving acyclicity. The exact incidence totals are \(34,656\) for \(\mathrm{Sh}\) and \(32,608\) for \(R\). The matchings contain \(3,370\) and \(3,204\) pairs, respectively. After matching the augmented empty face with vertex zero, the remaining critical-cell vectors in dimensions \((4,5,6)\) are

\[
(2,143,36) \quad\text{for }\mathrm{Sh},\qquad
(4,37,72) \quad\text{for }R.
\]

To pass to ordinary unreduced homotopy, delete the augmented empty-face pair from the matching and retain its vertex as one critical zero-cell. This preserves acyclicity; the empty face is not a cell of the geometric realization. Forman's discrete Morse theorem supplies a CW model with that zero-cell and precisely the displayed higher-dimensional critical cells.

**Signed integral attaching degrees.** Give a simplex the vertex-increasing orientation. Its boundary coefficient is \((-1)^i\) on the face obtained by removing the vertex at zero-based position \(i\). For each dimension \(j\), reduce the signed boundary onto the free abelian group of critical \(j\)-cells by the following terminating gradient-path recursion. A critical \(j\)-face projects to its basis vector; a \(j\)-face that is the upper element of a matched pair projects to zero; and if \(s\) is the lower element of \((s,u)\), its projection is

\[
P(s)=-\epsilon(s,u)\sum_{\substack{t\subset u,\;|t|=|s|\\t\ne s}}\epsilon(t,u)P(t),
\]

where \(\epsilon(t,u)\in\{1,-1\}\) is the signed incidence. Applying this recursion to each critical upper cell gives the integral Morse boundary matrices. The entire differential \(\partial^{\mathrm M}_6:C^{\mathrm M}_6\to C^{\mathrm M}_5\) is zero for each graph. The differential \(\partial^{\mathrm M}_5:C^{\mathrm M}_5\to C^{\mathrm M}_4\) contains a unimodular maximal minor in each case. For \(\mathrm{Sh}\), its critical-five-cell columns with zero-based positions \((7,8)\) give

\[
\begin{pmatrix}1&0\\1&1\end{pmatrix}\quad\text{with determinant }1.
\]

For \(R\), the critical-five-cell columns at positions \((0,1,2,4)\) give

\[
\begin{pmatrix}1&1&0&0\\0&-1&-1&1\\1&0&1&0\\0&0&1&0\end{pmatrix}
\quad\text{with determinant }-1.
\]

These matrices are reconstructed rather than trusted from logs. The two critical-four-cells of \(\mathrm{Sh}\), and four of \(R\), are thus killed primitively by higher cells; no integral torsion is introduced. The resulting reduced integral homology has ranks \((141,36)\) and \((33,72)\) in dimensions five and six, respectively.

**From integral homology to homotopy.** The ordinary Morse CW models have one zero-cell and no cells in dimensions one, two or three. Their four-skeleta are wedges of four-spheres. Each five-cell attaching map into such a wedge is classified by its integral vector of degrees because \(\pi_4(\bigvee S^4)\cong\bigoplus\mathbb Z\). The unimodular maximal minors permit homotopy changes of cellular bases and cancellation of the four-/five-cell pairs. The remaining five-skeleton is a wedge of \(141\) or \(33\) five-spheres. Every six-cell attaches to this wedge by an element of \(\pi_5(\bigvee S^5)\cong\bigoplus\mathbb Z\), fully detected by its signed degree vector. The zero sixth Morse differential, preserved under the cancellations, makes all these attaching maps nullhomotopic. The asserted integral wedge decompositions follow.

## Verification

Run `python3 verify.py` from a directory containing the standalone `verify.py`. It uses only Python standard-library modules and produces `VERIFY_OK` on success. The delivered `verify_output.txt` records the exact output of this command and is not substituted for rerunning it.

The program checks every graph edge and nonedge pair, two independent induced-cycle predicates over all \(65,536\) masks for each graph, every face incidence of the complete directed Morse Hasse diagram, both signed Morse differentials, the displayed determinant certificates, and independent full simplicial boundary ranks over \(\mathbb F_2\). The independently computed nonzero reduced mod-two Betti numbers agree with the integral wedge ranks; the mod-two computation alone is *not* used to assert integral torsion-freeness.

## Relationship to prior work

Taylan's 2015 paper introduces the general devoid-complex construction \(D(G;\mathcal H)\) for vertex subsets avoiding a specified family of induced subgraphs and develops discrete-Morse methods. Taking \(\mathcal H\) to be the family of cycles gives the present induced-forest construction, but the paper's explicit family classifications concern paths, cycles and forests with other forbidden families, not either graph in this theorem. Carnero Bravo subsequently studies the vertex-induced forest filtration and proves structural and family-specific results for paths, cycles, double stars, cactus graphs and selected products. The inspected calculations do not give these two sixteen-vertex complex types.

Previously available homotopy classifications for the ordinary independence complexes, higher-independence complexes, triangle-avoidance complexes, neighborhood complexes and Čech complexes of these strongly regular graphs concern distinct simplicial conditions. Their numerical and homotopy conclusions cannot be substituted for the present acyclic-induced-subgraph restriction; the exact forest complexes and the two mixed-dimensional integral classifications are separately computed here.

## Limitations

These are finite, exact results for the two explicitly defined graphs, not a classification of all strongly regular graphs, all graphs with the same parameters, or every stage of a forest filtration. The wedge equivalences are nonequivariant. The proof relies on a reproducible finite exhaustive Morse certificate rather than an unassisted closed-form combinatorial matching argument. Although focused searches did not identify an equivalent previously published calculation, an unindexed or uninspected prior treatment could exist. Independent mathematical review has not been performed.

## References

1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, publicly available 27 January 2015, https://arxiv.org/abs/1501.06754.
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly available 25 July 2023, https://arxiv.org/abs/2307.13271.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI 10.1006/aima.1997.1650. Discrete Morse theory is used only via its standard acyclic matching theorem.
