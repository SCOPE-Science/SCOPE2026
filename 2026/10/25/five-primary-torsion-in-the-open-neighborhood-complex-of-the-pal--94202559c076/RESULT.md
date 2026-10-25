# Five-primary torsion in the open neighborhood complex of the Paley graph of order twenty-five

## Finding
Let \(P_{25}\) be the ordinary Paley graph on the field \(\mathbb F_{25}\), and let \(K=\mathcal N(P_{25})\) be its *open* Lovász neighborhood simplicial complex. Its complete reduced integral homology is
\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{205}\oplus\mathbb Z/5\mathbb Z,&j=3,\\
\mathbb Z^4,&j=4,\\
0,&j\notin\{3,4\}.
\end{cases}
\]
In particular, this natural twenty-five-vertex conference graph has genuine order-five torsion in degree three, alongside four independent integral degree-four classes. No homotopy-wedge decomposition is claimed.

## Assumptions and scope
Identify \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-2)\), with elements \(a+bu\) indexed in ascending order by \(5a+b\) for \(0\le a,b\le4\). The polynomial is irreducible because \(2\) is not a quadratic residue modulo five. Write \(Q=\{z^2:z\in\mathbb F_{25}^{\times}\}\), a set of twelve nonzero elements. Distinct vertices \(x,y\) are adjacent exactly when \(y-x\in Q\). Since \(-1\in Q\), this defines an undirected loopless graph. The *open* neighborhood \(N(x)\) does not contain \(x\). A nonempty set \(\sigma\) is a face of \(K\) exactly when \(\sigma\subseteq N(x)\) for some \(x\). This is neither the clique complex nor the closed-neighborhood complex. All chains and homology groups below have integral coefficients unless specified.

## Proof
**Complete finite complex.** Enumerate the twelve-element neighborhoods by finite-field arithmetic and take the union of their full simplex faces. There are exactly \(93{,}350\) nonempty faces. The complete face vector, in dimensions zero through eleven, is
\[
(25,300,2200,9475,18750,22950,19800,12375,5500,1650,300,25).
\]
The same adjacency calculation verifies that each neighboring pair has five common neighbors and each nonneighboring distinct pair has six, giving parameters \((25,12,5,6)\). Every face is represented by its twenty-five-bit vertex mask; an oriented simplex lists its vertices in increasing mask-bit order.

**Exact collapses.** For every nonempty face \(\sigma\), maintain the number of its immediate codimension-minus-one cofaces. Visit faces of count one, prioritizing increasing cardinality and then integer mask. If \(\tau\) is the unique immediate coface, delete the pair \((\sigma,\tau)\), updating incidence counts. A face with precisely one immediate coface has a unique maximal coface, equal to that immediate coface; hence each deletion is a legal elementary simplicial collapse. Exactly \(43{,}546\) such collapses leave \(6{,}258\) nonempty faces, with face vector
\[
(25,300,1605,2929,1399).
\]
This reduced complex has dimension four and is homotopy equivalent to \(K\).

**Acyclic Morse matching.** Process the remaining faces in vertex order
\[
(24,10,13,6,11,1,17,5,23,14,22,16,20,19,8,21,0,18,2,4,15,12,3,9,7).
\]
At each vertex, scan currently unmatched faces by increasing integer mask, pairing \(\sigma\) with \(\sigma\cup\{v\}\) whenever both exist and are unmatched. This produces \(2{,}967\) disjoint covering pairs. Orient matched Hasse incidences upward and all other codimension-one incidences downward. The oriented Hasse graph has \(6{,}258\) nodes and \(24{,}126\) incidences; an exhaustive topological sort visits every node, proving acyclicity. Exactly one vertex, \(262\) three-simplices and \(61\) four-simplices are critical, with no critical cells in any other dimension.

**Signed integral Morse differential.** Let \([b:f]\in\{\pm1\}\) denote the standard simplicial boundary coefficient of the facet \(f\) in \(b\). To project an oriented three-simplex \(f\) onto critical three-simplices, use the following terminating recurrence: \(F(f)=f\) when critical; \(F(f)=0\) when matched downward to a two-simplex; and when \(f\) is paired upward with a four-simplex \(b\), set
\[
F(f)=-[b:f]^{-1}\sum_{\substack{g\subset b,\ \dim g=3\\g\neq f}}[b:g]F(g).
\]
The acyclic gradient orientation makes this well-defined. Applying \(F\) to the oriented boundaries of the \(61\) critical four-simplices gives the integral Morse differential \(B:\mathbb Z^{61}\to\mathbb Z^{262}\). With rows and columns indexed by increasing critical-face masks, \(B\) has \(923\) nonzero entries. Its complete sparse signed matrix is in `morse_matrix.json`; the SHA-256 of that file is `d02a1d00c8834f54985df10eb737677bd9cffcac76708533d1c0ccc88ab9ce79`.

Exact Smith normal form over the integers yields precisely \(56\) nonzero invariant factors equal to \(1\) and one equal to \(5\); the rank is \(57\). Therefore \(\ker B\cong\mathbb Z^4\) and \(\operatorname{coker}B\cong\mathbb Z^{205}\oplus\mathbb Z/5\mathbb Z\). The Morse chain groups occur only in dimensions zero, three and four, so no other reduced homology survives. This proves the finding.

## Verification
Run `python3 verify.py` with SymPy version \(1.14\) or another compatible release and `morse_matrix.json` in the same directory. The deterministic verifier reconstructs the finite field, all neighborhoods and faces, every free collapse, all Morse pairs, the complete oriented Hasse graph and the signed matrix. It checks exact Smith invariant factors and byte-for-byte agreement with the supplied matrix. The captured successful run is `verification_output.txt`. As a separate check not using Morse cancellations, sparse simplicial boundary elimination on the remaining \(6{,}258\)-face complex gives ranks \((24,276,1329,1395)\) modulo two and \((24,276,1329,1394)\) modulo five in dimensions one through four, consistent with exactly one five-primary jump. Finite-field ranks alone do not establish the integral invariant-factor structure: that uses the full exact integer Smith calculation.

## Relationship to prior work
Lovász introduced the graph neighborhood complex as a topological approach to graph coloring. Kahle's *The neighborhood complex of a random graph* (first public on 2005-12-04) studies asymptotic connectivity and dimensional bounds for random graphs, rather than these specific Paley homology groups. Matsushita's *Fundamental groups of neighborhood complexes* (first public on 2012-10-10) identifies fundamental groups of neighborhood complexes via graph walks, not their degree-three torsion or degree-four free homology.

Previously published exact calculations for \(\mathcal N(P_{13})\) and \(\mathcal N(P_{17})\) concern different field sizes: the former is a wedge of twenty-five two-spheres, whereas the latter has order-three torsion in degree two and free third homology. Neither statement entails the integral homology of \(\mathcal N(P_{25})\). The field of order twenty-five is a non-prime square field, not the cyclic prime-field case of those papers. No inspected source or targeted indexed record supplied the particular order-five torsion and mixed-degree ranks proved here.

## Limitations
The claim is an exact finite topological calculation only for the open-neighborhood complex of this graph. It does not classify the entire homotopy type, the action of the automorphism group, or other Paley or conference graphs. It does not assert a universal relationship between field size and homology torsion. The computation is exhaustive and reproducible but has not undergone independent mathematical audit. A mathematically equivalent unindexed or otherwise inaccessible result cannot be excluded solely from bibliographic searches.

## References
1. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory Series A 25 (1978), 319–324.
2. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077v1, 2005-12-04; Journal of Combinatorial Theory Series A 114 (2007), 380–387. https://arxiv.org/abs/math/0512077
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, 2012-10-10; Journal of Mathematical Sciences, University of Tokyo 24 (2017), 321–353. https://arxiv.org/abs/1210.2803
4. *The neighborhood complex of the order-13 Paley graph is a wedge of 25 two-spheres*, public mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-neighborhood-complex-of-the-order-13-paley-graph-is-a-wedge--3f8cbbf12bfc
5. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, public mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
