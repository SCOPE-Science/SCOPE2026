# Single-edge annihilation at the sharp lower boundary of nonmatching-complex stability

## Finding
Let \(G\) be the graph on \(\{0,1,2,3,4,5,6\}\) obtained from \(K_6\) on \(\{0,1,2,3,4,5\}\) by deleting edge \(01\) and inserting edges \(06\), \(16\). Write \(G^+=G+01\). For any graph \(T\), let \(\mathrm{NM}_3(T)\) be the abstract simplicial complex whose vertices are the edges of \(T\) and whose faces are edge subsets containing no matching of three disjoint edges.

The inclusion \(\iota:\mathrm{NM}_3(G)\longrightarrow\mathrm{NM}_3(G^+)\) has
\[
\widetilde H_4(\mathrm{NM}_3(G);\mathbb F_2)\cong\mathbb F_2^4,\qquad
\widetilde H_4(\mathrm{NM}_3(G^+);\mathbb F_2)=0.
\]
Consequently \(\iota_*\) on degree-four homology is the zero map with four-dimensional kernel. For context, the same exhaustive computation gives fifth-degree dimensions five and nine respectively.

## Assumptions and scope
All graphs are simple and labeled exactly as above. Face inclusion is the usual inclusion of edge subsets; chains have ordinary simplicial boundaries with coefficients in \(\mathbb F_2\). The claim concerns this one seven-vertex graph pair, not all single-edge additions, integral torsion, or homotopy type. Degree-five map injectivity is already guaranteed by the published link-vanishing theorem and is not asserted as a new result.

## Proof
Let \(E(T)\) be lexicographically ordered and encode each subset by its bitmask. Enumerate all size-three graph matchings \(M\subset E(T)\) by choosing six distinct vertices and the fifteen perfect pairings. A mask \(S\) represents a face precisely when \(M\nsubseteq S\) for each such matching. The two forbidden-matching counts are 42 for \(G\) and 45 for \(G^+\).

The exact enumerations of faces with respectively four, five, six, and seven edges are
\[
 G:(1361,2188,2103,1162),\qquad G^+:(1843,3366,3805,2580).
\]
The five-edge faces are degree-four simplices, and adjacent boundary matrices determine their homology. Standard bitwise Gaussian elimination over \(\mathbb F_2\) yields:
\[
\begin{array}{c|rrr}
 &\operatorname{rank}\partial_4&\operatorname{rank}\partial_5&\operatorname{rank}\partial_6\\\hline
 G&948&1236&862\\
 G^+&1328&2038&1758
\end{array}
\]
These are complete, exact matrix ranks: for instance \(\partial_4\) has a column for every size-five face and a row for every size-four face. By the chain-complex identity, \(\dim\widetilde H_4=f_4-\operatorname{rank}\partial_4-\operatorname{rank}\partial_5\). Therefore the dimensions are \(2188-948-1236=4\) and \(3366-1328-2038=0\). Likewise the fifth-degree dimensions are \(2103-1236-862=5\) and \(3805-2038-1758=9\). Since the target in degree four vanishes, its inclusion-induced homomorphism is zero with the claimed kernel. This proves the finding.

## Verification
Run `python3 verify.py` from the directory containing this document. The standalone standard-library script derives every graph edge, enumerates all six-vertex perfect pairings and all admissible faces, constructs the actual boundary bitvectors, and computes all six stated matrix ranks by exact \(\mathbb F_2\) elimination. It also checks \(\partial_4\partial_5=0\) and \(\partial_5\partial_6=0\) on **every** admissible relevant source face, not on a sample. Successful execution ends in `VERIFY_OK`. These exhaustive calculations are the proof's finite certificates, not extrapolation to an infinite family.

## Relationship to prior work
Linusson, Shareshian, and Welker introduced and classified the homotopy types of complete-graph nonmatching complexes, but did not calculate this inclusion map [1]. Holmsen and Lee explicitly display the subdivided-edge \(K_6\) graph and note its mixed-degree homology, and prove that nonempty face links in \(\mathrm{NM}_3(T)\) have vanishing homology in degrees five and above [2]. Their link theorem, via the deletion/link sequence, implies injectivity in degree five under adding a graph edge. It does not imply injectivity in degree four: the present exact edge-filling calculation shows this adjacent-degree extension fails maximally for the displayed graph. The new contribution is the degree-four inclusion statement, not the known general injection in degree five or the existence of the mixed-degree source example.

## Limitations
All numerical ranks here use \(\mathbb F_2\) coefficients and the exact seven-vertex pair. No claims are made about integer torsion, minimality among all seven-vertex graph pairs, or arbitrary matching parameters. Relevant edge-addition literature for bipartite graphs studies a different category and degree. An equivalent inclusion-map calculation could exist outside the sources inspected.

## References
[1] S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first made public 2004-10-15, https://arxiv.org/abs/math/0410345.

[2] A. F. Holmsen, S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first made public 2020-03-25, https://arxiv.org/abs/2003.11270; especially Figure 1 and Theorem 1.2.
