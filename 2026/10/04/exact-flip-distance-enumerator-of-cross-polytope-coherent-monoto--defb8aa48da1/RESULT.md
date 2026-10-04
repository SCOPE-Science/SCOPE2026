# Exact flip-distance enumerator of cross-polytope coherent monotone paths
## Finding
Let \(n\ge 3\), put \(m=n-1\), and let
\[
\diamond^n=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\subset\mathbb R^n.
\]
Fix a generic linear functional \(\varphi\) with
\[
0<\varphi(e_1)<\cdots<\varphi(e_n).
\]
Black and De Loera identify the coherent \(\varphi\)-monotone paths with the nonzero sign vectors
\[
V_m=\{-1,0,1\}^m\setminus\{0\},
\]
and show that a polygonal flip between two coherent paths occurs exactly when their sign vectors have \(\ell_1\)-distance one.

For \(s,t\in V_m\), the exact flip distance is
\[
d_{\mathrm{flip}}(s,t)=
\begin{cases}
4,&t=-s\text{ and }|\operatorname{supp}(s)|=1,\\
\|s-t\|_1,&\text{otherwise}.
\end{cases}
\]
Thus the only failure of the ambient ternary-grid \(\ell_1\) metric is at the \(m\) unordered antipodal unit-vector pairs.

The complete ordered distance enumerator is
\[
D_m(z)=\sum_{s,t\in V_m} z^{d_{\mathrm{flip}}(s,t)}
=(3+4z+2z^2)^m-2(1+2z)^m+1+2m(z^4-z^2).
\]
In particular, the graph Wiener index, namely the sum of distances over unordered distinct pairs, is
\[
W_m=4m\,9^{m-1}-2m\,3^{m-1}+2m.
\]
The mean distance over unordered distinct coherent-path pairs is therefore
\[
\frac{W_m}{\binom{3^m-1}{2}}.
\]

## Assumptions and scope
The statement concerns coherent monotone paths on the standard cross-polytope under a generic orientation ordered as above. It uses the sign-vector correspondence and adjacency theorem proved by Black and De Loera. It does not claim an exact all-pairs metric for the larger flip graph containing incoherent monotone paths.

The restriction \(n\ge3\) is essential for the displayed exceptional distance: when \(m=1\), removing the origin disconnects the two nonzero ternary vertices. For \(m\ge2\), the coherent-path graph is connected.

## Proof
By the cited adjacency theorem, the coherent-path flip graph is the graph on \(V_m\) whose edges join sign vectors differing in one coordinate by \(0\leftrightarrow 1\) or \(0\leftrightarrow -1\). Every edge changes \(\ell_1\)-distance by one, so every path from \(s\) to \(t\) has length at least \(\|s-t\|_1\).

It remains to decide when an ambient ternary-grid \(\ell_1\)-geodesic can avoid the deleted origin.

If \(\operatorname{supp}(s)\ne\operatorname{supp}(t)\), then, in the direction in which a target-only coordinate exists, turn on that coordinate before changing the remaining coordinates. It remains nonzero as an anchor while every required coordinate change is made. Reversing this path handles the opposite containment. The resulting path has exactly \(\|s-t\|_1\) edges and never meets the origin.

Suppose next that the supports are equal. If some common support coordinate has the same sign in \(s\) and \(t\), hold it fixed while changing all other coordinates along shortest coordinate paths. Again the origin is avoided with exactly \(\|s-t\|_1\) steps.

The remaining equal-support case has opposite signs in every supported coordinate. If the common support has size at least two, choose two supported coordinates. Change the first through zero while leaving the second nonzero, complete its sign reversal, and then keep the first as the nonzero anchor while reversing the other coordinates. This is still an \(\ell_1\)-geodesic.

Only opposite unit vectors remain. For \(s=e_i\) and \(t=-e_i\), every two-step ambient \(\ell_1\)-geodesic is \(e_i\to0\to-e_i\), so distance two is impossible in the punctured graph. The graph is bipartite by parity of \(\|s\|_1\), hence their distance is even. Since \(m\ge2\), choosing \(j\ne i\) gives the four-edge path
\[
e_i\to e_i+e_j\to e_j\to -e_i+e_j\to-e_i,
\]
with the obvious sign changes for general opposite unit vectors. Their distance is therefore exactly four. This proves the metric formula.

For the enumerator, first keep the origin. In one coordinate, among the nine ordered pairs of symbols in \(\{-1,0,1\}\), three have distance zero, four have distance one, and two have distance two. Hence the ordered \(\ell_1\)-distance enumerator of the full ternary cube is
\[
(3+4z+2z^2)^m.
\]
For ordered pairs with one endpoint equal to the origin, the one-coordinate polynomial is \(1+2z\). Removing all pairs having an origin endpoint therefore subtracts \(2(1+2z)^m\) and adds back the doubly subtracted origin pair, giving
\[
(3+4z+2z^2)^m-2(1+2z)^m+1.
\]
Exactly \(2m\) ordered pairs, namely \((e_i,-e_i)\) and \((-e_i,e_i)\), move from distance two to distance four. This adds \(2m(z^4-z^2)\), proving the formula for \(D_m\).

Finally, differentiating at \(z=1\) sums all ordered distances:
\[
D_m'(1)=8m\,9^{m-1}-4m\,3^{m-1}+4m.
\]
Each unordered pair is counted twice, so
\[
W_m=\frac12D_m'(1)=4m\,9^{m-1}-2m\,3^{m-1}+2m.
\]

## Verification
The standalone verifier enumerates the punctured ternary grid for \(m=2,3,4,5\), computes every graph distance by breadth-first search, and checks all three identities: the pointwise metric formula, every coefficient of the ordered distance enumerator, and the Wiener-index formula. Its successful output is

`VERIFY_OK exact signohedron flip-distance enumerator`

These finite checks corroborate the proof but are not used to extend a finite computation to arbitrary dimension.

## Relationship to prior work
Black and De Loera prove that the coherent monotone paths are indexed by nonzero ternary sign vectors and that adjacency is exactly Taxi-Cab distance one; they then compute the diameter \(2(n-1)\). Their proof of the diameter notes that the only extra issue is avoiding the deleted origin, but it does not state the exact distance between every pair, identify the unique exceptional pair type, or give a distance enumerator or Wiener index.

Athanasiadis, De Loera, and Zhang study general enumerative bounds and diameters for monotone-path graphs. Juhnke and Poullot later refine the enumeration of cross-polytope monotone paths by the length of each individual monotone path, including coherent ones. That path-length distribution is a different statistic from the pairwise number of flips between coherent paths. Their full text has no occurrence of “flip distance”, “Taxi”, or “Wiener”.

Targeted searches for the signohedron metric, cross-polytope coherent-path flip distance, punctured ternary-grid distance, and a Wiener index did not locate a statement implying the formula above. The remaining novelty risk is that the graph-theoretic calculation may exist under unrelated terminology for a punctured Cartesian product.

## Limitations
The result is conditional only on the published sign-vector model and adjacency characterization. It concerns pairwise distances within the coherent-path graph, not distances in the larger graph of all monotone paths. The latter graph can admit shortcuts through incoherent paths, so this theorem must not be transferred to it without a separate argument.

The literature search cannot prove global uniqueness of the result. In particular, an unindexed graph-theory treatment of the punctured ternary cube could contain an equivalent distance enumerator.

## References
1. A. E. Black and J. A. De Loera, “Monotone Paths on Cross-Polytopes”, arXiv:2102.01237, first submitted 2 February 2021; *Discrete & Computational Geometry* 70 (2023), 1245–1265, DOI 10.1007/s00454-023-00563-4.
2. C. A. Athanasiadis, J. A. De Loera, and Z. Zhang, “Enumerative problems for arborescences and monotone paths on polytope graphs”, arXiv:2002.00999; *Journal of Graph Theory* 99 (2022), 58–81, DOI 10.1002/jgt.22725.
3. M. Juhnke and G. Poullot, “Unimodality of the number of paths per length on polytopes: Examples, counterexamples, and a central limit theorem”, arXiv:2504.20739.
