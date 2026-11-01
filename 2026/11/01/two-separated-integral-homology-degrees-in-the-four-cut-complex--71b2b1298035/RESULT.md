# Two separated integral homology degrees in the four-cut complex of the triangular graph on six points

## Finding
Let \(T=J(6,2)=L(K_6)\) be the triangular graph on the fifteen two-element subsets of a fixed six-element set. Its ordinary four-cut complex \(\Delta_4(T)\) is defined using complements of *disconnected* four-vertex induced subgraphs. Then
\[
\widetilde H_i(\Delta_4(T);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{67},&i=8,\\
\mathbb Z^{15},&i=10,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is pure of dimension \(10\) and has nonzero homology strictly below its top dimension. It is therefore not Cohen–Macaulay over any field and, consequently, not shellable. The degree-nine reduced homology vanishes integrally, leaving two nonadjacent nonzero homology degrees.

## Assumptions and scope
The vertex set of \(T\) is \(\binom{[6]}{2}\); distinct vertices \(a,b\) are adjacent precisely when \(a\cap b\ne\varnothing\). For each four-vertex set \(Q\subseteq V(T)\) such that \(T[Q]\) is disconnected, include its eleven-vertex complement \(V(T)\setminus Q\) as a facet of \(\Delta_4(T)\), together with every subset of that facet. This is the **ordinary** cut complex, not the total cut complex (whose defining four-sets are independent). Simplicial chains have the usual increasing-vertex orientation. The empty face is included for reduced chain homology. There are exactly \(390\) such facets, each of size \(11\), making a pure ten-dimensional complex. The full face vector, in dimensions zero through ten, is
\[
(15,105,455,1365,3003,5005,6435,6375,4570,1935,390).
\]
These are finite, explicitly defined objects. No assertion is made for other triangular graphs or cutoffs.

## Proof
**Exhaustive construction.** Index the fifteen two-subsets of \([6]\) lexicographically. For each of the \(\binom{15}{4}=1365\) four-subsets, test the connectivity of its induced intersection graph by breadth-first expansion from the least selected vertex. Exactly \(390\) sets are disconnected. A subset \(\sigma\subseteq V(T)\) is a face exactly when its complement contains one of these \(390\) disconnected four-sets. This direct predicate was checked for all \(2^{15}=32768\) subsets against the independently generated facet closure; both give \(29654\) augmented faces, including the empty face.

**Complete acyclic matching.** On the *augmented* face poset, process the fifteen coordinates in increasing order. At step \(j\), pair each still-unmatched face \(\sigma\) lacking coordinate \(j\) with \(\sigma\cup\{j\}\) whenever both are still unmatched; remove each paired pair from later stages. The resulting matching has \(14781\) pairs and leaves precisely five critical seven-simplices, seventy-two critical eight-simplices and fifteen critical ten-simplices. Orient each unmatched cover relation downward and each matched cover relation upward. An exhaustive topological sort of all \(212910\) directed Hasse incidences visits every one of the \(29654\) faces, proving that the matching is acyclic.

**Exact integral Morse differential.** Orient simplices by increasing vertex index and reduce each matched lower face using the signed incidence relation of its matched upper simplex; unmatched upper faces contribute zero as eliminated generators. This recursion terminates because of the just-verified acyclicity. It yields a reduced integral Morse chain complex supported in degrees \(7,8,10\), with ranks \(5,72,15\). The degree-ten differential is identically zero because there are no critical nine-cells. The degree-eight differential has size \(5\times72\); its columns of zero-based indices \(2,7,21,39,49\) are, respectively, the five standard basis vectors up to individual signs. Hence this matrix has a unimodular \(5\times5\) minor and is surjective over \(\mathbb Z\). Its kernel is a free abelian group of rank \(72-5=67\). The degree-seven homology vanishes; the fifteen ten-cells survive since there are no nine-cells or eleven-cells. All other reduced groups vanish. Algebraic discrete Morse cancellation preserves the reduced integral homology, proving the displayed formula.

**Non-shellability.** Every facet has dimension ten. A pure shellable complex is Cohen–Macaulay over every field and has reduced field homology concentrated in its top dimension. Since the integral degree-eight group is free of rank sixty-seven, its homology over every field is nonzero in degree eight. This contradicts Cohen–Macaulayness and shellability.

## Verification
Run \(\texttt{python3 verify.py}\) using Python 3.9 or later, without dependencies. It independently reconstructs all faces by two methods, checks all matched Hasse incidences and their acyclicity, constructs the signed integral Morse differential and its five explicit unit columns, and reduces every original simplicial boundary over \(\mathbb F_2\) without relying on the Morse matching. The latter gives reduced mod-two Betti numbers \((0,0,0,0,0,0,0,0,67,0,15)\), agreeing with the integral computation. Compare program output with \(\texttt{verification_output.txt}\). Both artifacts accompany this result.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced these cut complexes and determined topology for several graph families (2023 preprint). Their follow-up treats disjoint graph unions, squared paths and grid graphs (2024 preprint). Neither examined graph family is the triangular graph \(J(6,2)\) with cutoff four. Published work on \(\Delta_4(J(5,2))\) finds eleven three-spheres; this is the smaller six-point family member's five-point predecessor, not an implication about the fifteen-vertex graph's homology. Related total-cut complexes have a different face predicate, and neighborhood complexes of triangular graphs are likewise different. The comparison concerns specific objects and implications, not merely paper titles.

## Limitations
The integral **homology** groups are completely determined, but no homotopy decomposition into sphere wedges is asserted. In particular, higher-dimensional attaching maps may carry homotopy information not detected by the signed Morse differential; the computation does not rule them out. The field-homology calculation alone would not have excluded torsion, which is why the integral unit-minor check is essential. This finite graph does not imply a formula or threshold for all \(J(n,2)\). An unindexed earlier equivalent calculation remains possible despite the targeted search and primary-literature comparison.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, first public preprint 2023-04-26, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, first public preprint 2024-07-11, https://arxiv.org/abs/2407.08158.
3. H. Chandrakar et al., *Topology of total cut and cut complexes of grid graphs*, first public preprint 2024-08-14, https://arxiv.org/abs/2408.07646.
