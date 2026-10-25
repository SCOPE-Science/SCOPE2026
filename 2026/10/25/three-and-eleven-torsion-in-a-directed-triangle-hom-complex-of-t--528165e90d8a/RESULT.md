# Three- and eleven-torsion in a directed-triangle Hom complex of the Paley tournament

## Finding
Let \(P_{11}\) be the tournament on \(\mathbb Z/11\mathbb Z\) in which \(i\to j\) exactly when \(j-i\) is a nonzero square modulo \(11\). Let \(X=\operatorname{Hom}(\overrightarrow C_3,P_{11})\) be the directed multihomomorphism complex, with its standard products-of-simplices CW structure. Its integral homology is
\[
H_k(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z\oplus\mathbb Z/33\mathbb Z,&k=1,\\
0,&k\geq2.
\end{cases}
\]
In particular, both three-primary and eleven-primary torsion occur in first integral homology. This complex is not homotopy equivalent to any wedge of spheres.

## Assumptions and scope
The directed source is the three-cycle \(0\to1\to2\to0\), not an undirected triangle. For three nonempty subsets \(A,B,C\subset\mathbb Z/11\mathbb Z\), a cell of \(X\) is present precisely when every edge from \(A\) to \(B\), from \(B\) to \(C\), and from \(C\) to \(A\) exists in \(P_{11}\). It is the product \(\Delta(A)\times\Delta(B)\times\Delta(C)\), with dimension \(|A|+|B|+|C|-3\). Vertices of each factor are oriented in the order \(0,1,\ldots,10\). No simplicial replacement or neighborhood complex is substituted for this CW complex. The result concerns the specific canonical tournament of order eleven and the ordinary integral, rather than equivariant, homology.

## Proof
Put \(Q=\{1,3,4,5,9\}\subset\mathbb Z/11\mathbb Z\), and write \(N^+(u)=u+Q\) and \(N^-(u)=u-Q\). Exhaustively and without duplicate cells, choose each nonempty \(A\), then each nonempty \(B\subset\bigcap_{a\in A}N^+(a)\), then each nonempty
\[
C\subset\left(\bigcap_{b\in B}N^+(b)\right)\cap\left(\bigcap_{a\in A}N^-(a)\right).
\]
These inclusion conditions are necessary and sufficient for a directed multihomomorphism. The attached checker also independently regenerates the complete collection by extending directed-triangle vertex assignments. Both constructions agree. They produce precisely \(165\) zero-cells, \(495\) one-cells and \(330\) two-cells, with no cells in larger degrees. Among the two-cells, \(165\) are triangular products \(\Delta^2\times\Delta^0\times\Delta^0\) (up to permuting factors) and \(165\) are squares \(\Delta^1\times\Delta^1\times\Delta^0\).

With the product orientations just specified, the cellular boundary in column notation is
\[
\begin{split}
\partial(\Delta A\times\Delta B\times\Delta C)
={}&(\partial\Delta A)\times\Delta B\times\Delta C\\
&+(-1)^{|A|-1}\Delta A\times(\partial\Delta B)\times\Delta C\\
&+(-1)^{|A|+|B|-2}\Delta A\times\Delta B\times(\partial\Delta C),
\end{split}
\]
where each simplicial boundary is the alternating deletion sum. The exact computation constructs all columns of \(d_1:\mathbb Z^{495}\to\mathbb Z^{165}\) and \(d_2:\mathbb Z^{330}\to\mathbb Z^{495}\), verifies \(d_1d_2=0\), and establishes connectedness of the one-skeleton, so \(\operatorname{rank}d_1=164\).

To determine the *integral* rather than merely rational homology, the checker performs \(329\) integral unit-pivot eliminations on \(d_2\). Each pivot \(\pm1\) is separated using integer row and column operations, which are unimodular and therefore preserve the remaining Smith invariants. After those eliminations, exactly one nonzero column remains. It has \(33\) nonzero entries, all equal in absolute value to \(33\); their gcd is \(33\). Reducing that column by the Euclidean algorithm gives the last Smith invariant \(33\). Thus the nonzero Smith diagonal of \(d_2\) is
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{329\text{ times}},33),
\qquad \operatorname{rank}d_2=330.
\]
Consequently, \(H_2=\ker d_2=0\). The rank of \(H_1\) is \(495-164-330=1\). Since \(\operatorname{im}d_1\) is a free abelian group, the exact sequence \(0\to H_1\to\operatorname{coker}d_2\to\operatorname{im}d_1\to0\) shows that the torsion subgroup of \(H_1\) equals that of \(\operatorname{coker}d_2\), namely \(\mathbb Z/33\mathbb Z\). Connectedness gives \(H_0\cong\mathbb Z\); absence of higher-dimensional cells gives \(H_k=0\) for \(k>2\). A wedge of spheres has torsion-free integral homology, completing the last assertion.

## Verification
Execute `python3 check_hom_p11.py` with Python 3.8 or later. The checker is standalone and uses only Python's standard library. It constructs all cells and both boundary matrices from the tournament adjacency rule; checks an independent cell enumeration, orientations and \(d_1d_2=0\); counts connected components; and carries out the exact unimodular eliminations. Independent modular rank checks give rank \(330\) modulo \(2,5,13\) and rank \(329\) modulo \(3,11\), consistent with the full integral result. Every check terminates with assertions and reports PASS on success. The checker calculates a finite CW chain complex completely; it is not a numerical approximation or a finite test of an asserted infinite family.

## Relationship to prior work
Dochtermann and Singh introduced the directed Hom-complex framework, treated complexes of directed cycles and tournaments, and studied several low-order tournament examples [1]. A published calculation for the directed three-cycle and the nine-vertex *regular cyclic* tournament gives the homotopy type of a circle [2]; it concerns a different target than \(P_{11}\), and is not claimed here. The directed flag complex, directed path homology, and out-neighborhood complex of a tournament are different constructions and do not, solely by their invariants, imply the present integral Hom calculation. Literature and mathematical-record searches described in the accompanying scientific review found no covering calculation of this specific Hom complex. A search cannot rule out equivalent unindexed results.

## Limitations
This computes all integral **homology groups** of the specified directed Hom complex, not its fundamental group, complete homotopy type, integral action of tournament automorphisms, or the first occurrence of torsion among all target tournaments. The exact Smith calculation is algorithmic and depends on the supplied complete deterministic checker, whose source reconstructs the complex; no independent external audit has been performed. The originality assessment is necessarily limited to the sources materially inspected.

## References
[1] A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, initial public version 24 August 2021, https://arxiv.org/abs/2108.10948.

[2] *The directed Hom complex \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) has the homotopy type of a circle*, mathematical research record, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-directed-hom-complex-operatorname-hom-overrightarrow-c-3-r-9--879b51cbdd1a.
