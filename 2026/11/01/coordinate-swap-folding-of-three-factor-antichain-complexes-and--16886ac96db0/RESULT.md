# Coordinate-swap folding of three-factor antichain complexes and the first fixed two-cycle

## Finding

Write \(\mathcal A(P)\) for the abstract simplicial complex of nonempty antichains of a finite poset \(P\), with the empty face included by convention. For every nonempty finite poset \(Q\), transposing the first two factors of \([2]\times[2]\times Q\) induces an involution \(\tau\). There is an explicit, canonical piecewise-linear homeomorphism
\[
 |\mathcal A([2]\times[2]\times Q)|^{\langle\tau\rangle}
 \cong_{\mathrm{PL}} |\mathcal A([3]\times Q)|.
\]

For \(Q=[n]\), set \(F_n=|\mathcal A([2]\times[2]\times[n])|^{\langle\tau\rangle}\). The canonical simplicial triangulation has face vector \(\bigl(3n,3\binom n2,\binom n3\bigr)\). Its **complete integral homology** is
\[
 H_j(F_n;\mathbb Z)\cong
 \begin{cases}
 \mathbb Z^3,&j=0,\;n\ge1,\\
 \mathbb Z^{3n-7},&j=1,\;n\ge3,\\
 \mathbb Z^{\binom{n-3}{3}},&j=2,\;n\ge3,\\
 0,&\text{otherwise}.
 \end{cases}
\]
In particular, the number of connected components is always three, and the first nonzero second homology occurs precisely at \(n=6\), when it is \(\mathbb Z\).

## Assumptions and scope

The factors \([2]\) and \([3]\) are linearly ordered sets of the indicated cardinalities; product orders are coordinatewise. All spaces are ordinary geometric realizations, and \(\tau\) acts simplicially by exchanging the two binary coordinates, not by exchanging simplicial vertices in an abstract chain complex. No grading, lattice, or connectivity hypothesis is required of \(Q\), apart from finiteness and nonemptiness. Homology has integral coefficients throughout. The displayed binomial coefficient is interpreted as zero when the upper entry is below the lower entry.

## Proof

**1. The fixed-point orbit triangulation.** The involution on vertices has, for each \(q\in Q\), exactly three orbits:
\[
 A_q=\{(0,0,q)\},\qquad
 B_q=\{(0,1,q),(1,0,q)\},\qquad
 D_q=\{(1,1,q)\}.
\]
Each orbit is an antichain (the two elements in \(B_q\) are incomparable). For a simplicial action of an involution, a geometric point is fixed precisely when its unique barycentric coefficients agree on the elements in each orbit in its support. Consequently, its entire invariant support is an antichain and it has a unique expression as a convex combination of the orbit barycenters. The fixed set thus has a simplex for exactly those collections of orbits whose unions are antichains; its realization is PL-homeomorphic to the original geometric fixed set. This is a statement about actual fixed points, not a claim that the fixed points are a full subcomplex on fixed original vertices.

**2. Exact poset reduction for arbitrary \(Q\).** Identify \(A_q,B_q,D_q\), respectively, with \((0,q),(1,q),(2,q)\) in \([3]\times Q\). Within a common orbit type, two distinct orbits are compatible exactly when their parameters in \(Q\) are incomparable. Between earlier and later types \(u<v\), an orbit at \(q\) is compatible with one at \(r\) if and only if \(q\not\le r\). In particular, the cross pairs between the two elements in \(B_q\) and \(B_r\) cannot introduce any additional comparabilities: each has one binary coordinate larger and the other smaller. The same compatibility criterion is exactly incomparability of \((u,q)\) and \((v,r)\) in \([3]\times Q\). Every subset is a face if and only if every pair is compatible, so this identifies the fixed-point orbit complex **simplicially** with \(\mathcal A([3]\times Q)\). Composing with the barycentric realization gives the claimed PL homeomorphism.

**3. Specialized chain model.** For \(Q=[n]\), write \(A_i,B_i,D_i\) with \(i=0,\dots,n-1\). The only edges are \(A_iB_j\), \(A_iD_j\), and \(B_iD_j\) with the first subscript strictly greater than the second. The only triangles are \(A_iB_jD_\ell\) with \(i>j>\ell\). This proves the face-vector formula and shows that the homology is concentrated in degrees at most two.

**4. A graph-and-cones decomposition.** Let \(G\) be the induced bipartite graph on the \(A\) and \(D\) vertices, with edges \(A_iD_\ell\) exactly when \(i>\ell\). For \(n\ge2\), its three connected components consist of the isolated vertices \(A_0\), \(D_{n-1}\), and one connected main graph. The full complex is \(G\) with cones at the vertices \(B_j\) attached along their links \(L_j\subseteq G\). Here \(L_0\) is the discrete set \(\{A_1,\dots,A_{n-1}\}\), \(L_{n-1}\) is the discrete set \(\{D_0,\dots,D_{n-2}\}\), and for \(1\le j\le n-2\) the link is the complete bipartite graph
\[
 L_j=K_{n-1-j,j}
\]
on \(A_i\) with \(i>j\) and \(D_\ell\) with \(\ell<j\). The cones meet one another only along \(G\).

**5. Relative homology.** The relative chain complex of \((F_n,G)\) splits as a sum of suspensions of augmented chain complexes of the links. Consequently
\[
 H_2(F_n,G;\mathbb Z)\cong\bigoplus_{j=1}^{n-2}\widetilde H_1(L_j;\mathbb Z)
 \cong\mathbb Z^{\binom{n-2}{3}},\qquad
 H_1(F_n,G;\mathbb Z)\cong\mathbb Z^{2(n-2)}.
\]
The second equality uses the two discrete endpoint links; the internal complete bipartite links are connected. All inclusions \(L_j\hookrightarrow G\) land in the main connected component, so the relative boundary map from \(H_1(F_n,G)\) to \(H_0(G)\) vanishes.

**6. The integral image is a primitive coordinate sublattice.** For \(n\ge3\), a spanning tree of the main component of \(G\) consists of all \(A_iD_0\) with \(1\le i\le n-1\) and all \(A_{n-1}D_\ell\) with \(1\le\ell\le n-2\). The remaining edges give a free integral cycle basis \(z_{i,\ell}\), indexed by \(2\le i\le n-2\) and \(1\le\ell<i\). Thus \(H_1(G;\mathbb Z)\cong\mathbb Z^{\binom{n-2}{2}}\). Each internal link \(L_j\) contains only chords indexed by \(i>j>\ell\), so the image of its first homology involves only \(z_{i,\ell}\) with \(i-\ell\ge2\). Conversely, for any such \((i,\ell)\), the four-cycle using \(A_i,A_{n-1},D_\ell,D_0\) belongs to \(L_{\ell+1}\) and represents the basis vector \(z_{i,\ell}\) up to sign. Therefore the image of the connecting map
\[
 H_2(F_n,G;\mathbb Z)\longrightarrow H_1(G;\mathbb Z)
\]
is **exactly** the direct summand spanned by those \(z_{i,\ell}\) with \(i-\ell\ge2\). Its rank is \(\binom{n-3}{2}\). In particular the quotient is torsion-free, with basis the consecutive-gap cycles \(z_{i,i-1}\), of rank \(n-3\). This direct-summand argument is essential: a mod-two rank computation alone would not establish integral torsion-freeness.

**7. Resolve the exact sequence.** The long exact sequence of the pair, together with the primitive image, gives
\[
 H_2(F_n;\mathbb Z)\cong \mathbb Z^{\binom{n-2}{3}-\binom{n-3}{2}}=
 \mathbb Z^{\binom{n-3}{3}},
\]
and a short exact sequence of free abelian groups
\[
 0\to\mathbb Z^{n-3}\to H_1(F_n;\mathbb Z)\to\mathbb Z^{2(n-2)}\to0.
\]
Since the right-hand group is free, the sequence splits, giving \(H_1(F_n;\mathbb Z)\cong\mathbb Z^{3n-7}\). The cone attachments do not change the three components of \(G\). For \(n=1\), the complex is three isolated points; for \(n=2\), it consists of a path and two isolated points. The formulas and vanishing assertions follow, and the binomial expression is positive first at \(n=6\).

## Verification

The included standalone Python file `verify.py` reconstructs orbit-union antichains **directly from the original product partial order** and compares them with the predicted three-layer complex, not merely its face counts. It tests every simplex through dimension two for chain lengths \(1\le n\le16\), a total of 83,572 admissibility decisions, and independently computes all mod-two boundary ranks. It also tests all 19 labeled partial orders on three points, comparing all 512 orbit subsets per poset, for 9,728 additional decisions. These finite computations check formulas and small cases; the full finite-poset PL theorem and integral all-length homology theorem are proved by the preceding combinatorial arguments, not extrapolated from experiments.

Run `python3 verify.py` using Python 3.9 or later; no third-party packages are required.

## Relationship to prior work

Chen, Dong and Tang (2026) study antichain polynomials of products of chains, including three-factor products, and supply the literature motivation for the original three-factor posets. Barik, Mondal and Mukherjee (2026) study nonequivariant independence complexes of comparability graphs arising from chain products and related constructions. Their nonequivariant results concern different spaces or the nonequivariant two-factor target; **those results are not asserted to make the target's Betti numbers new by themselves**. The present structural assertion is instead an identification of the actual geometric fixed-point space of an involution on a three-factor antichain complex for **arbitrary finite \(Q\)**. Homology of the target is included to extract a concrete consequence not inferable merely from the homology of the original three-factor complex or a Lefschetz character. No claim is made that searching establishes uniqueness against all unpublished or unindexed results.

## Limitations

The arbitrary-poset theorem establishes a PL model, not a homotopy decomposition of that model for every \(Q\). The integral homology formula requires a chain third factor. The proof does not determine the full action on the homology of the ambient three-factor complex, or higher-group fixed loci. The numerical homology of the nonequivariant two-factor target may be implicit in earlier literature. The source-comparison process cannot exclude equivalent unindexed work; independent mathematical validation has not been performed.

## References

1. X. Chen, Y. Dong, S. Tang, *Antichain polynomials of products of chains and minuscule posets*, arXiv:2609.28983v1 (first public version 2026-09-24), https://arxiv.org/abs/2609.28983 . Full open text: https://arxiv.org/html/2609.28983 .
2. S. Barik, A. Mondal, S. Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606v1 (2026-04-14), https://arxiv.org/abs/2604.12606 .
