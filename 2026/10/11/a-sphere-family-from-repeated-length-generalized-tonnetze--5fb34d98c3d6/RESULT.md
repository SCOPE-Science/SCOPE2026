# A sphere family from repeated-length generalized Tonnetze
## Finding
For every integer \(k\ge 4\), let
\[
L_k=(\underbrace{1,\ldots,1}_{k-1\text{ entries}},2),\qquad n=k+1.
\]
Then the Jevtić--Živaljević generalized Tonnetz is exactly the boundary complex of the \(k\)-simplex:
\[
\operatorname{Tonn}^{k+1,k}(L_k)=\partial\Delta^k.
\]
Consequently its geometric realization is homeomorphic to \(S^{k-1}\).

## Assumptions and scope
The generalized Tonnetz \(\operatorname{Tonn}^{n,k}(L)\) is used in the sense of Jevtić and Živaljević: for a positive length vector \(L=(l_1,\ldots,l_k)\) with \(\sum_i l_i=n\), its generating \((k-1)\)-simplices are
\[
\Delta(x;\sigma)=\{x,\ x+l_{\sigma(1)},\ x+l_{\sigma(1)}+l_{\sigma(2)},\ldots,\ x+l_{\sigma(1)}+\cdots+l_{\sigma(k-1)}\}
\]
inside \(\mathbb Z_n\), where \(x\in\mathbb Z_n\) and \(\sigma\in\Sigma_k\).

For \(k\ge4\), the vector \(L_k\) is reduced but nongeneric because distinct singleton index sets carrying two of the repeated unit lengths have equal subset sums. The claim is an equality of abstract simplicial complexes, not merely a homology or homotopy calculation.

## Proof
Fix \(k\ge4\) and write \(n=k+1\). Any permutation of \(L_k\) is an ordering of one increment \(2\) and \(k-1\) increments \(1\). Lift the cyclic partial sums starting from \(x\) to ordinary integer partial sums before reducing modulo \(n\). Before the omitted last increment is added, those partial sums are strictly increasing and lie in an interval of length less than \(n\). Hence the \(k\) displayed vertices of every \(\Delta(x;\sigma)\) are distinct.

There are \(n=k+1\) vertices in total, so every generating simplex is a \(k\)-element subset of \(\mathbb Z_n\), hence the complement of one vertex. Therefore every generating simplex is a facet of \(\partial\Delta^k\), and
\[
\operatorname{Tonn}^{k+1,k}(L_k)\subseteq\partial\Delta^k.
\]

Conversely, place the increment \(2\) last in the ordering. Then
\[
\Delta(x;\sigma)=\{x,x+1,\ldots,x+k-1\}\subset\mathbb Z_{k+1},
\]
which is the complement of \(x-1\). As \(x\) ranges over \(\mathbb Z_{k+1}\), these are all \(k+1\) facets of \(\partial\Delta^k\). Thus the reverse inclusion holds and the two simplicial complexes are equal. Since the boundary of a \(k\)-simplex is a triangulation of \(S^{k-1}\), the topological conclusion follows.

## Verification
The bundled `verify.py` reconstructs the complexes directly from the defining partial-sum formula, using every distinct ordering of one \(2\) and \(k-1\) unit increments. For every \(4\le k\le10\) it verifies exact equality with the set of all codimension-one faces of a \(k\)-simplex and checks the face vector
\[
\bigl(\binom{k+1}{1},\binom{k+1}{2},\ldots,\binom{k+1}{k}\bigr).
\]
It also checks the proof's explicit coverage identity through \(k=64\): when the \(2\) is last, the facet starting at \(x\) misses exactly \(x-1\). These finite checks support the implementation and indexing; the all-\(k\) statement is proved symbolically above and does not rest on finite enumeration.

## Relationship to prior work
Jevtić and Živaljević define \(\operatorname{Tonn}^{n,k}(L)\) for arbitrary \(k\) and prove that a generic reduced length vector gives a \((k-1)\)-torus. Their proof explicitly uses genericity, and the inspected paper does not classify the repeated-length family \(L_k\).

Catanzaro studies a different, triad-focused generalized Tonnetz and proves that the special triadic case \(C(1,1,2)\) is the boundary of a tetrahedron. Thus the \(k=3\) predecessor of the pattern is known. The present claim starts at \(k=4\) and identifies the higher-dimensional Jevtić--Živaljević complexes themselves with simplex boundaries in every dimension. Searches under the exact parameter family, the boundary-simplex formulation, repeated-length aliases, and nongeneric-sphere wording found no statement covering the all-\(k\) result.

## Limitations
The result concerns only the family with \(k-1\) unit lengths and one length \(2\). It does not classify arbitrary nongeneric Tonnetze, repeated-length vectors with other multiplicities, or the all-distinct nongeneric regime. The literature comparison leaves the ordinary residual risk of an unindexed equivalent observation, but the directly relevant arbitrary-\(k\) source and the earlier complete triadic classification were both inspected at statement and proof level.

## References
1. Filip D. Jevtić and Rade T. Živaljević, “Generalized Tonnetz and discrete Abel--Jacobi map,” arXiv:2002.09184v1 (first posted 2020-02-21); *Topological Methods in Nonlinear Analysis* 57 (2021), 547--567, DOI 10.12775/TMNA.2020.049.
2. Michael J. Catanzaro, “Generalized Tonnetze,” arXiv:1612.03519v1 (posted 2016-12-12). In the triadic classification, Theorem 24 identifies \(C(1,1,2)\) with a tetrahedron boundary.
