# Exact minimum enclosing ball and contact classes of simplex-sum stellohedra

## Finding

For any integer \(k\ge1\), let \([k]=\{1,\ldots,k\}\), let \(e_0,e_1,\ldots,e_k\) be the standard basis of \(\mathbb R^{k+1}\), and define the simplex-sum stellohedron
\[
P_k=\sum_{\varnothing\ne A\subseteq[k]}\Delta_{\{0\}\cup A},\qquad
\Delta_J=\operatorname{conv}\{e_j:j\in J\}.
\]
This \(k\)-polytope lies in the hyperplane with coordinate sum \(N=2^k-1\). Use the Euclidean metric induced by the ambient coordinate space, not an arbitrary affine-equivalent realization.

The **unique smallest enclosing Euclidean ball** has center
\[
\boxed{c_k=(h,t,\ldots,t),\qquad t=\frac{2N+1}{3(k+1)},\quad h=N-kt}
\]
and squared radius
\[
\boxed{R_k^2=\frac{k(2N+1)^2}{9(k+1)}.}
\]
There are exactly \(1+k!\) contact vertices: the hub vertex \((N,0,\ldots,0)\) and all permutations of \((0,2^{k-1},2^{k-2},\ldots,1)\). All other vertices, and all nonvertex points of the polytope, are strictly inside the ball.

More quantitatively, for each rank \(r\in\{0,\ldots,k\}\), every vertex of rank \(r\) has squared-radius clearance
\[
\boxed{R_k^2-\|v-c_k\|^2
=\frac23(2^k-2^{k-r})(2^{k-r}-1).}
\]
It vanishes exactly for \(r=0\) and \(r=k\).

## Assumptions and scope

The star graph has hub \(0\) and leaves \([k]\); connected vertex subsets of cardinality at least two are exactly the \(\{0\}\cup A\) with nonempty \(A\subseteq[k]\). The usual graph-associahedron realization as the Minkowski sum over **all** nonempty connected subsets includes the singleton summands \(\{e_i\}\) for \(0\le i\le k\). Hence that usual realization equals \(P_k+(1,\ldots,1)\); translations preserve enclosing radii and contact classes and translate the center by the same vector. All statements here are made for the explicitly defined \(P_k\), avoiding any ambiguity from affine-equivalent realizations.

For \(k=1\) the polytope is a line segment and the formula gives its midpoint and intrinsic radius \(1/\sqrt2\). For every \(k\ge2\), the polytope is full-dimensional in the coordinate-sum hyperplane because the summands with \(A=\{i\}\) provide the spanning directions \(e_i-e_0\).

## Proof

**1. Enumerate the vertices from support functionals.** Fix a linear functional \(u\) whose \(k+1\) coordinate coefficients are distinct. Exactly \(r\) leaf coefficients lie above \(u_0\); name these leaves \(i_1,\ldots,i_r\) in decreasing coefficient order. The exposed vertex of \(\Delta_{\{0\}\cup A}\) is whichever of \(e_0\) and \(\{e_i:i\in A\}\) has largest coefficient. Leaf \(i_j\) is selected by exactly \(2^{k-j}\) of the summands: a subset \(A\) must contain \(i_j\), exclude the \(j-1\) larger leaves, and may choose any of the \(k-j\) remaining leaves. The hub is selected exactly when \(A\) avoids all \(r\) higher leaves and is nonempty, giving \(2^{k-r}-1\) selections. Other leaves are never selected. Therefore the exposed vertex has coordinates
\[
(v_0,v_{i_1},\ldots,v_{i_r})=(2^{k-r}-1,2^{k-1},\ldots,2^{k-r}),
\]
with zero in the other leaf coordinates. Conversely, every ordered choice of \(r\) distinct leaves can be realized by strict coefficients, and every polytope vertex has a generic exposing functional. The hub coordinate determines \(r\), while the distinct powers determine the ordered leaves, so the listed vertices are pairwise distinct. Their number is \(\sum_{r=0}^k k!/(k-r)!\).

**2. Exact containment and boundary contacts.** Write \(B=2^k\), and for a rank-\(r\) vertex set \(a=2^{k-r}\), \(M=B-a\). The total positive leaf-coordinate sum is \(M\), and their squared-coordinate sum, by a finite geometric series, is
\[
\sum_{j=1}^r 4^{k-j}=\frac{B^2-a^2}{3}=\frac{M(B+a)}3.
\]
Put \(F_r=\|v-c_k\|^2\). At the rank-zero hub vertex,
\[
F_0=(N-h)^2+kt^2=k(k+1)t^2=R_k^2.
\]
For an arbitrary rank, expand the squares and use \(a-1=N-M\):
\[
\begin{aligned}
F_r-F_0
&=M^2-2Mkt+\frac{M(B+a)}3-2Mt\\
&=M\left[B-a+\frac{B+a}{3}-2(k+1)t\right]\\
&=-\frac23M(a-1).
\end{aligned}
\]
The last equality substitutes \(2(k+1)t=2(2B-1)/3\). Since \(M,a-1\ge0\), the displayed ball contains every vertex and hence the whole polytope. Equality occurs only at \(r=0\) and \(r=k\). For \(0<r<k\), both factors are positive, giving strict clearance. Every nonvertex point is a nontrivial convex combination of distinct vertices; strict convexity of squared Euclidean distance, together with the vertex bound, places it strictly inside the sphere.

**3. A positive global optimality certificate.** Denote the rank-zero hub vertex by \(z=(N,0,\ldots,0)\). The average of the \(k!\) rank-\(k\) contact vertices is
\[
w=(0,N/k,\ldots,N/k),
\]
because their positive leaf coordinates are permutations of \(2^{k-1},\ldots,1\), summing to \(N\). Put \(\alpha=h/N\). The parameters obey \(0<\alpha<1\): \(h=N-kt<N\) because \(t>0\), and \(h=((k+3)N-k)/(3(k+1))>0\) because \(N\ge k\). Furthermore,
\[
\alpha z+(1-\alpha)w=(h,t,\ldots,t)=c_k.
\]
Therefore the strictly positive probability distribution that assigns mass \(\alpha\) to \(z\) and distributes mass \(1-\alpha\) uniformly over rank-\(k\) contacts has barycenter \(c_k\). For **any** candidate ball center \(y\in\mathbb R^{k+1}\), including nonsymmetric and off-hyperplane choices, the variance identity gives
\[
\sum_{v\text{ contact}}\omega_v\|v-y\|^2
=\sum_v\omega_v\|v-c_k\|^2+\|y-c_k\|^2
=R_k^2+\|y-c_k\|^2.
\]
At least one contact is therefore at distance at least \(R_k\) from \(y\), with strictly larger distance whenever \(y\ne c_k\). The constructed containing ball is globally minimum and its center is unique.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only the Python 3 standard library and rational arithmetic. Run \(\texttt{python3 verify.py}\). It checks every rank-distance identity for \(1\le k\le80\), independently constructs every ordered-leaf vertex for \(1\le k\le8\), checks exact contact classes and barycentric identities, and reconstructs simplex-sum exposed vertices using 600 independently generated generic coefficient vectors. Its recorded successful run checked 3,320 rank identities, 125,672 explicitly enumerated vertices, and 46,241 contacts. The finite checks do **not** certify the universal quantifier; that follows from the exact formulas and the proof above.

## Relationship to prior work

Devadoss and Smith describe graph associahedra from tubings of connected subgraphs, assigning primary classification 52B11 to their work. Pešović and Stojadinović give the Minkowski-sum realization by simplices over connected subsets and study enumerative and Hopf-algebraic invariants. Applying that realization to a star identifies \(P_k\), up to the singleton translation. The present theorem instead determines an explicitly normalized **Euclidean** minimum enclosing ball and its complete contact set; neither of the two inspected primary texts establishes this radius or the contact-clearance formula.

The distinction from general facts that minimum enclosing balls are determined by contacting points is the explicit verification that only two combinatorial ranks are contacts and that the displayed positive contact distribution is optimal in every dimension. An earlier equivalent computation under circumsphere, Euclidean Chebyshev center, minimal bounding sphere, or optimal experimental-design terminology remains a possible bibliographic risk.

## Limitations

This result concerns the standard unweighted simplex-sum realization with its inherited Euclidean metric. General affine changes of coordinates preserve neither these distances nor the stated numerical radius. It makes no assertion about arbitrary graph associahedra, weighted Minkowski sums, their inradii, or uniqueness of a prior appearance in unindexed literature. No independent audit or external priority certification has been performed.

## References

1. S. L. Devadoss and M. Smith, *Colorful Graph Associahedra*, arXiv:2011.08169 (initial public submission 2020-11-16). Introduction and graph-associahedron background, §2.
2. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (initial public submission 2022-09-24). §2, Definition 2.1, and its specialization to graph associahedra.
