# Integral torsion and the full symmetric character of the bidirected five-leaf biclique multipath complex

## Finding
Let \(D=\overleftrightarrow{K}_{2,5}\) have hubs \(u_0,u_1\) and leaves \(v_1,\ldots,v_5\), with both directions of each hub-to-leaf edge. Its multipath complex \(X(D)\) has
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,& i=2,\\
\mathbb Z^{31},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
The natural leaf-permutation action \(S_5\) commutes with hub interchange \(C_2\). As a rational \(S_5\)-representation, the \(+1\) hub-eigenspace of \(\widetilde H_3\) is
\[
S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}\oplus S^{(1,1,1,1,1)},
\]
of dimension \(16\); the \(-1\) eigenspace is
\[
S^{(3,2)}\oplus S^{(3,1,1)}\oplus S^{(2,1,1,1)},
\]
of dimension \(15\). Here \(S^\lambda\) denotes the rational Specht module indexed by partition \(\lambda\) of five. In particular the 31-dimensional homology has no \(S_5\)-fixed vector, and hub interchange has trace \(1\).

## Assumptions and scope
A simplex of \(X(D)\) is a set of distinct directed arcs spanning a disjoint union of directed paths, including isolated vertices. Every vertex has at most one incoming and one outgoing selected arc, and all directed cycles, including length-two cycles, are forbidden. The 20 oriented arcs are ordered by increasing leaf and, for each leaf, in the order \(u_0\to v_j\), \(v_j\to u_0\), \(u_1\to v_j\), \(v_j\to u_1\). Chains use the induced order of arc indices with the usual alternating simplicial boundary. The group \(S_5\times C_2\) permutes graph vertices (without reversing every arrow), inducing oriented simplicial chain maps. Coefficients are integral for the Betti/torsion classification and rational for the Specht decomposition.

## Proof
An exhaustive hereditary enumeration of eligible arc subsets yields \((f_0,f_1,f_2,f_3)=(20,130,320,240)\) and no faces above dimension three: at most two arcs can leave hubs and at most two can enter them. Boundary matrices have formats \(20\times130\), \(130\times320\), and \(320\times240\). Direct signed matrix multiplication gives \(\partial_1\partial_2=\partial_2\partial_3=0\).

Integer elementary row and column operations with unit pivots reduce \(\partial_1\) to 19 unit factors and a zero remainder, and \(\partial_2\) to 111 unit factors and a zero remainder. The same operations reduce \(\partial_3\) to 208 unit factors and a sparse nonzero remainder of rank one whose entries have greatest common divisor two. The remainder has rank one because each of its two-by-two minors vanishes, verified exhaustively; thus its sole nonzero Smith invariant is two. Accordingly the three boundary ranks are \(19,111,209\), and the nonzero Smith factors are respectively \(1^{19}\), \(1^{111}\), and \(1^{208},2\). The chain condition implies the torsion in the cokernel of \(\partial_3\) lies in the kernel of \(\partial_2\), since the image of \(\partial_2\) is free. Hence \(\widetilde H_2\cong\mathbb Z/2\mathbb Z\), while \(\widetilde H_3\) has rank \(240-209=31\). The first boundary has rank \(19\), proving connectivity, and \(\widetilde H_1=0\) follows from \(130-19-111=0\).

For every leaf permutation \(\sigma\) and hub-swap bit \(h\), the trace of its action on the \(k\)-chains equals the sum over setwise fixed \(k\)-simplices of the sign of the induced permutation of their ordered arcs. Let this trace be \(t_k(\sigma,h)\). Rational reduced homology is concentrated in degree three, so the reduced Lefschetz identity gives
\[
\operatorname{tr}(\sigma,h\mid\widetilde H_3(X(D);\mathbb Q))=1-\sum_{k=0}^{3}(-1)^k t_k(\sigma,h).
\]
The following complete list gives characters for each conjugacy partition of \(S_5\), with columns \(h=0\) and \(h=1\):

| Cycle type | No hub swap | Hub swap |
|---|---:|---:|
| \((1,1,1,1,1)\) | 31 | 1 |
| \((2,1,1,1)\) | -5 | -3 |
| \((2,2,1)\) | -1 | 1 |
| \((3,1,1)\) | 1 | 1 |
| \((3,2)\) | 1 | -3 |
| \((4,1)\) | -1 | 1 |
| \((5)\) | 1 | 1 |

Decomposing the half-sum and half-difference of these characters by the ordinary \(S_5\) character table gives precisely the Specht summands in the finding. The attached character checker calculates the table from all simplices, evaluates irreducible characters independently by rim-hook removal, and reconstructs all fourteen table entries from the stated multiplicities. Character orthogonality and the dimension check complete the rational representation classification.

## Verification
Run `python3 check_integral.py` and then `python3 check_character.py` from the directory containing both attached source files, using Python 3 and its standard library. The first reconstructs the entire complex, checks the chain property, performs exact integer unit-pivot reductions, checks the remaining rank-one minors and gcd, and confirms the stated homology. The second independently enumerates signed fixed simplices for representatives of all fourteen classes and confirms the irreducible decomposition. The integer algorithm is not based on floating-point ranks or mod-two dimensions. The same two scripts were executed successfully for this result.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith introduce multipath complexes, dynamic decompositions and the stable-module conjecture. Their complete bipartite examples use coherently oriented bipartite digraphs, not both directions of every edge as here. The bidirected polygonal study of Caputi, Collari and Smith concerns path and cycle graphs, not this biclique. Earlier calculations of the four-leaf bidirected biclique already detect two-torsion and an unstable-module counterexample; the present result does **not** claim novelty for that counterexample. The new object is the five-leaf complex and especially its full \(S_5\times C_2\) rational character, which does not follow from its integral homology ranks or the four-leaf calculation.

## Limitations
No simple-homotopy or wedge decomposition is deduced. The integral \(S_5\)-lattice structure and torsion-module extension beyond the abstract abelian groups are not determined. No formula for other numbers of leaves is asserted. Equivalent results outside the inspected literature remain possible. The character calculation is rational, not a complete integral equivariant classification.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first publicly posted 2022-08-09), https://arxiv.org/abs/2208.04656 .
2. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (2026), https://arxiv.org/abs/2601.05670 .
3. Study of multipath complexes of oriented bipartite graphs, arXiv:2401.01248 (2024), https://arxiv.org/abs/2401.01248 .
