# Complete integral homology of three-row rook neighborhood complexes

## Finding
For every integer \(n\ge5\), let \(R_{3,n}=K_3\square K_n\) be the rook graph on the \(3\)-by-\(n\) array, equivalently the line graph \(L(K_{3,n})\). Its **open Lovász neighborhood complex** has complete reduced integral homology
\[
\boxed{\widetilde H_d(\mathcal N(R_{3,n});\mathbb Z)\cong
\begin{cases}
\mathbb Z,&d=1,\\
\mathbb Z^{3n^2-9n+3},&d=2,\\
\mathbb Z^3,&d=n-2,\\
0,&\text{otherwise}.
\end{cases}}
\]
All homology is torsion-free; the listed degrees are distinct because \(n\ge5\). Thus there are two nonzero degrees below the three row-boundary spheres: one integral circle class and a quadratic family of integral two-classes. For \(n=5,6,7,8\), the rank triples in degrees \((1,2,n-2)\) are respectively \((1,33,3)\), \((1,57,3)\), \((1,87,3)\), and \((1,123,3)\).

## Assumptions and scope
All graphs are finite, simple, loopless and undirected. The rook graph has vertices \(v_{i,j}\) for \(i\in\{0,1,2\}\) and \(j\in\{0,\ldots,n-1\}\), with distinct vertices adjacent exactly when they share a row or a column. An **open** neighborhood omits its center, and a subset of vertices is a simplex of \(\mathcal N(G)\) precisely when its elements have a common adjacent vertex. The empty simplex is included by convention. No assertion is made at \(n<5\), and no homotopy-type or fundamental-group classification is claimed.

## Proof
**1. Three row-centered subcomplexes.** For each row \(i\), define
\[
F_{i,j}=\{v_{i,t}:t\ne j\}\cup\{v_{k,j}:k\ne i\},
\qquad
Y_i=\bigcup_{j=0}^{n-1}\Delta(F_{i,j}).
\]
Every graph open neighborhood is one of the displayed sets, so
\(\mathcal N(R_{3,n})=Y_0\cup Y_1\cup Y_2\).
For fixed \(i\), the intersection of any proper nonempty collection of the \(n\) maximal simplices \(\Delta(F_{i,j})\) contains at least one vertex in row \(i\), hence is a contractible simplex; the intersection of all \(n\) is empty. The simplicial nerve theorem applies, with nerve the boundary of the simplex on \(n\) vertices. Therefore
\[
Y_i\simeq S^{n-2}.
\]
In particular, for \(n\ge5\), each \(Y_i\) is connected and has no homology in degrees one or two.

**2. Intersections of different rows.** For different rows \(i\) and \(k\), write \(\ell\) for the remaining row. The intersection of the generating facets \(F_{i,a}\) and \(F_{k,b}\) consists of exactly \(\{v_{i,b},v_{k,a}\}\) when \(a\ne b\), and exactly \(\{v_{\ell,a}\}\) when \(a=b\). Consequently
\[
Y_i\cap Y_k\;=\;(K_{n,n}\setminus M)\;\sqcup\;\bigsqcup_{j=0}^{n-1}\{v_{\ell,j}\},
\]
where the crown graph uses rows \(i,k\) and its edges join unequal column indices. The crown graph is connected because \(n\ge3\), with \(2n\) vertices and \(n(n-1)\) edges. It has first Betti number
\[
c_n=n(n-1)-2n+1=n^2-3n+1.
\]
Thus every pair intersection has exactly \(n+1\) components, its \(H_1\) is \(\mathbb Z^{c_n}\), and all its homology above degree one vanishes. Intersecting all three row subcomplexes leaves exactly the \(3n\) isolated vertices, with no edge or higher simplex.

**3. Integral Mayer–Vietoris double complex.** Use the standard integral Mayer–Vietoris spectral sequence of a three-subcomplex simplicial cover,
\[
E^1_{p,q}=\bigoplus_{0\le i_0<\cdots<i_p\le2}
H_q(Y_{i_0}\cap\cdots\cap Y_{i_p};\mathbb Z)
\Longrightarrow H_{p+q}(\mathcal N(R_{3,n});\mathbb Z).
\]
For \(q=n-2\), only the three individual \(Y_i\) contribute, giving \(E^2_{0,n-2}=\mathbb Z^3\). For \(q=1\), only the three pair intersections contribute. As \(H_1(Y_i)=0\), their \(3c_n\) independent crown-graph cycles survive: \(E^2_{1,1}=\mathbb Z^{3c_n}\).

It remains to compute the \(q=0\) row integrally rather than by rank alone. In Čech degrees \(p=2,1,0\) it reads
\[
\mathbb Z^{3n}\xrightarrow{\,\partial_2\,}
\mathbb Z^{3(n+1)}\xrightarrow{\,\partial_1\,}\mathbb Z^3.
\]
Every pair-intersection component maps by \(\partial_1\) to the difference of its two row-component generators. Therefore \(\partial_1\) has rank two, and its kernel is free of rank \(3n+1\). Each triple-intersection vertex \(v_{r,j}\) maps under \(\partial_2\) to three pair-intersection components. In the pair formed by the **other two rows**, its image is the isolated component \(\{v_{r,j}\}\), with coefficient \(+1\) or \(-1\); in the other two pair intersections, its image lies in the connected crown component. Projecting the codomain to its \(3n\) isolated-component coordinates therefore gives a signed permutation matrix. In particular \(\partial_2\) is a **split injection over \(\mathbb Z\)**, with torsion-free cokernel and image of rank \(3n\). Hence
\[
E^2_{2,0}=0,\qquad E^2_{1,0}=\mathbb Z,
\qquad E^2_{0,0}=\mathbb Z.
\]

There are no other nonzero terms. In a three-set cover, the only potentially nontrivial higher differential is the \(d_2\) differential from column two to column zero; its source is zero in every homological row here. The spectral sequence collapses at \(E^2\). Each associated graded group is free, so additive extensions split over \(\mathbb Z\). The indicated \(H_1\), \(H_2\), and \(H_{n-2}\), together with connectedness and zero homology elsewhere, give the claimed complete reduced integral classification.

## Verification
The accompanying standard-library program `verify_rook3n.py` constructs the open neighborhoods, enumerates every face for \(5\le n\le8\), checks the facet-intersection nerves, checks each pair and triple row intersection, reconstructs the integral signed-isolated-component minor, and computes all reduced mod-two homology ranks by exact bitset Gaussian elimination. Running `python verify_rook3n.py` returns `ROOK3N_MV_FINITE_CHECKS_OK`; its actual output is supplied in `verification_output.txt`. The finite checks do not prove the integral theorem: its infinite extent and torsion-freeness follow from Steps 1–3 and the signed permutation minor.

## Relationship to prior work
Shukla [1] develops the **open** neighborhood complex and gives homotopy classifications for graphs of maximum degree at most three and for four-regular circulants. Our rook graph has degree \(n+1\ge6\), so those classification hypotheses do not apply. The directly related result [2] determines a natural quotient of rook neighborhood complexes and **all homology in degrees at least three**, but leaves degrees one and two undetermined; its statements do not supply the exact low-degree boundary maps needed here. The two-row rook-graph sphere-wedge theorem [3] treats \(K_2\square K_n\), not the three-row graph. The closed-neighborhood theory concerns a different simplicial complex; closed and open neighborhoods must not be interchanged. Finally, the sixteen-point Kummer biplane calculation [4] concerns \(K_4\square K_4\), a different row number and a complex with integral two-torsion. In contrast to these results, the theorem determines the entire integral homology of \(K_3\square K_n\) for the infinite range \(n\ge5\). No claim of novelty is made for special cases already separately tabulated.

## Limitations
The statement determines **homology**, not homotopy type, the integral fundamental group or integral symmetry representations in degrees one and two. There may exist homologically indistinguishable spaces with different attaching maps. The special case \(n=4\) is excluded and is not needed for the infinite-family proof. Computational agreement through \(n=8\) is a check, not an infinite-domain proof. Bibliographic comparison is finite; unindexed equivalent work remains possible.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first submitted 2018-02-13, https://arxiv.org/abs/1802.04526.

[2] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45.

[3] *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620.

[4] *The Kummer biplane block complex has an integral projective-plane summand*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-kummer-biplane-block-complex-has-an-integral-projective-plan--6184c6679525.
