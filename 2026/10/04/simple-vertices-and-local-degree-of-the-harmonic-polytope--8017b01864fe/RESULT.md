# Simple vertices and local degree of the harmonic polytope
## Finding
For every integer \(n\ge 2\), vertices of the harmonic polytope \(H_{n,n}\) admit an exact local-degree formula. A vertex is indexed by a fine harmonic triple \((k;\pi_1,\pi_2)\). For a label \(x\), let \(p_a(x)\) be its position in the permutation \(\pi_a\). Let \(M=(m_1,\ldots,m_s)\) be the labels maximal for the product order on \((p_1(x),p_2(x))\), ordered so that \(p_1(m_1)<\cdots<p_1(m_s)\); then \(p_2(m_1)>\cdots>p_2(m_s)\), and harmonicity of the fine triple is equivalent to \(k\in M\). If \(k=m_j\), define \(\varepsilon_-=1\) when \(j>1\) and \(p_1(k)=p_1(m_{j-1})+1\), and define \(\varepsilon_+=1\) when \(j<s\) and \(p_2(k)=p_2(m_{j+1})+1\); otherwise the corresponding indicator is zero. Then
\[
\deg(k;\pi_1,\pi_2)=2n+s-3-\varepsilon_- -\varepsilon_+.
\]
Since \(\dim H_{n,n}=2n-2\), the vertex is simple exactly when \(s-1=\varepsilon_-+\varepsilon_+\). Thus a simple vertex has one of only three forms: \(s=1\); \(s=2\) with the unique neighboring product maximum adjacent to the marked maximum in the relevant permutation; or \(s=3\) with the marked maximum in the middle and both required adjacencies. No vertex with \(s\ge4\) is simple.

The exact number of simple vertices is
\[
 n!\left(3(n-1)!+(n-2)!H_{n-2}\right),
\]
where \(H_0=0\). Since Ardila--Escobar proved that the total number of vertices is \((n!)^2H_n\), the simple-vertex proportion is
\[
\frac{3(n-1)+H_{n-2}}{n(n-1)H_n},
\]
which tends to zero. For example, \(H_{3,3}\) has \(66\) vertices, of which exactly \(42\) are simple; its vertex degrees are \(4\) on those \(42\) vertices and \(5\) on the remaining \(24\).

## Assumptions and scope
The statement concerns the harmonic polytope of Ardila and Escobar for integers \(n\ge2\), with vertices indexed by their fine harmonic triples. Graph degree means degree in the one-skeleton of the polytope. The product order uses the positions in the two permutation components of the fine harmonic triple. The harmonic number is \(H_r=\sum_{i=1}^r 1/i\) for \(r\ge1\), with \(H_0=0\).

## Proof
Ardila and Escobar identify every face of the normal fan with a harmonic triple and give its dimension. A fine triple has \(K=\{k\}\), both ordered partitions are permutations, and its normal cone has dimension \(2n-2\). An edge incident to the corresponding polytope vertex is dual to a codimension-one face of that normal cone, so it is enough to classify the harmonic triples that cover the fine triple with fan dimension \(2n-3\).

Write a coarsening as \((K';\pi'_1,\pi'_2)\). Let \(a_1\) and \(a_2\) be the numbers of adjacent merges made in the two permutations, and let \(r=\ell(\pi'_1|K')-1\). The dimension formula gives a codimension drop of exactly \(a_1+a_2+r\). Hence a codimension-one coarsening is of exactly one of two kinds: one adjacent merge with \(K'=\{k\}\), or no merge with \(K'=\{k,\ell\}\).

There are initially \(2(n-1)\) possible single adjacent merges. A merge not involving \(k\) preserves harmonicity. A merge of \(k\) with its successor in either permutation is also forced to be harmonic by maximality of \(k\). The only possible failures are the merge with the immediate predecessor of \(k\) in \(\pi_1\) and the merge with the immediate predecessor of \(k\) in \(\pi_2\). The first fails precisely when that predecessor is the preceding product maximum \(m_{j-1}\), counted by \(\varepsilon_-\); the second fails precisely when the next product maximum \(m_{j+1}\) is immediately before \(k\) in \(\pi_2\), counted by \(\varepsilon_+\). Thus the merge type contributes \(2(n-1)-\varepsilon_- -\varepsilon_+\) edges.

With the permutations unchanged, \(K'=\{k,\ell\}\) is harmonic exactly when both \(k\) and \(\ell\) are product maxima. Indeed, the opposite-order condition for \(K'\) makes the two elements incomparable, while the harmonic condition for every outside label is exactly product maximality for each member of \(K'\). Hence there are \(s-1\) coarsenings of the second type. Adding the two contributions yields
\[
2(n-1)-\varepsilon_- -\varepsilon_+ +(s-1)=2n+s-3-\varepsilon_- -\varepsilon_+.
\]
The simplicity classification follows by setting this equal to \(2n-2\).

For the enumeration, fix \(\pi_1\) and relabel so that it is the identity. If \(q_i=p_2(i)\), the product maxima are exactly the right-to-left maxima of the permutation \(q\), and a vertex corresponds to a permutation with one marked right-to-left maximum. Simple marked permutations split into three disjoint classes. With one right-to-left maximum there are \((n-1)!\) choices. With two right-to-left maxima, marking the first is simple exactly when their values are consecutive, and marking the second is simple exactly when their positions are consecutive; each class has \((n-1)!\) members. With three right-to-left maxima, only the middle one can be simple. The two adjacency conditions give a bijection with a permutation of \(n-2\) having a marked right-to-left maximum: delete the global maximum and the final lower neighbor; conversely, raise values above the marked value, insert the new global maximum immediately before the marked maximum, and append the marked value's missing lower neighbor. The number of such marked permutations is \((n-2)!H_{n-2}\). Therefore the number for each fixed \(\pi_1\) is \(3(n-1)!+(n-2)!H_{n-2}\), and multiplying by the \(n!\) choices of \(\pi_1\) proves the count.

## Verification
The accompanying standard-library program `artifacts/verify.py` independently enumerates all relative permutations through \(n=8\). For every marked right-to-left maximum it counts codimension-one coarsenings directly from the harmonicity conditions, compares that count with the degree formula, and checks the closed simple-vertex count. It reports `VERIFY_OK harmonic-polytope simple-vertex classification n=2..8`. The computation is a finite consistency check only; the proof above establishes the theorem for all \(n\).

## Relationship to prior work
Ardila and Escobar introduced \(H_{n,n}\), described its full face poset by harmonic triples, proved \(\dim H_{n,n}=2n-2\), counted its vertices and facets, and observed that the harmonic fan is already non-simplicial for \(n=3\). Their face-poset theorem is the essential input here, but the source does not state a vertex-degree formula, classify the simplicial maximal cones, count simple vertices, or derive their vanishing asymptotic proportion. Ardila's later bipermutahedron paper studies the related simple refinement and the Minkowski quotient; it does not give the local-degree statistic for the harmonic polytope. Sage's documented harmonic-polytope entry records the known dimension, facet count, vertex count, and the \(n=3\) global \(f\)-vector, but not the simple-vertex count or degree distribution.

## Limitations
The theorem concerns only local one-skeleton degree and simplicity; it does not give the full degree distribution in closed form, the adjacency graph, or a resolution of the singularities of the associated toric variety. The originality comparison is strongest against the two directly related primary papers and the documented Sage entry; a terminologically different derivation in uncatalogued literature remains a residual risk. The finite verifier reaches \(n=8\) and is not used as a substitute for the infinite proof.

## References
Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, first public version 2020-06-04; Selecta Mathematica 27 (2021), DOI:10.1007/s00029-021-00687-6.

Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, first public version 2020-08-05; Combinatorial Theory 2 (2022), no. 3.

SageMath Reference Manual, `harmonic_polytope(n)`, Combinatorial and Discrete Geometry polytope library.
