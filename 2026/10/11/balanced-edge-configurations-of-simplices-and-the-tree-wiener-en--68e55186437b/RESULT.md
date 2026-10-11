# Balanced edge configurations of simplices and the tree–Wiener energy identity

## Finding

Let \(n\ge3\) and let \(\Delta=\operatorname{conv}\{v_1,\ldots,v_n\}\) be any nondegenerate Euclidean simplex of dimension \(n-1\), with vertex centroid
\[
G=\frac1n\sum_{i=1}^{n}v_i.
\]
Consider unordered sets \(X=\{x_1,\ldots,x_{n-1}\}\) of \(n-1\) points on its one-skeleton such that
\[
\frac1{n-1}\sum_{r=1}^{n-1}x_r=G.
\tag{1}
\]
There are **exactly \(n^{n-2}\) such sets**. They correspond bijectively to labeled spanning trees \(T\) on the vertex labels \(\{1,\ldots,n\}\). For each edge \(e=\{i,j\}\) of \(T\), delete \(e\) and let \(k\) be the number of vertices in the component containing \(i\). The corresponding point is uniquely
\[
\boxed{\displaystyle
x_e=\frac{n-k}{n}v_i+\frac{k}{n}v_j.
}
\tag{2}
\]
In particular, all balancing points lie strictly inside **distinct** simplex edges; no collisions or simplex vertices are possible.

When \(\Delta\) is regular with edge length \(s>0\), define the geometric dispersion of this configuration by
\[
\mathcal E(X)=\sum_{\{e,f\}\subseteq E(T)}\lVert x_e-x_f\rVert^2.
\]
If \(W(T)=\sum_{1\le i<j\le n}\operatorname{dist}_T(i,j)\) is the (unordered-pair) Wiener index of \(T\), then
\[
\boxed{\displaystyle
\mathcal E(X)
=s^2(n-1)\left(\frac{(n-1)^2}{2n}-\frac{W(T)}{n^2}\right).
}
\tag{3}
\]
Consequently,
\[
\boxed{\displaystyle
\frac{s^2(n-1)^2(n-2)}{3n}
\le\mathcal E(X)\le
\frac{s^2(n-1)^3(n-2)}{2n^2}.
}
\tag{4}
\]
For \(n\ge4\), the lower equality holds exactly for labeled **paths** and the upper exactly for labeled **stars**; there are \(n!/2\) minimizing and \(n\) maximizing configurations. For \(n=3\), all three trees are simultaneously paths and stars, and both bounds equal \(4s^2/9\).

This is one geometric classification, with (3)–(4) describing a natural metric invariant of every classified configuration.

## Assumptions and scope

The vertices \(v_i\) are affinely independent. The one-skeleton consists of their closed line-segment edges, including the vertices. The balancing points are **unordered** and carry equal weights; repetitions are allowed a priori but are ruled out by the theorem. Trees are simple undirected labeled graphs. All Euclidean distances in (3)–(4) use the ambient inner product, and regularity is required only for these metric statements. The count and the location formula (2) hold for every shape of simplex by affine invariance.

A point in an \((n-1)\)-simplex is represented uniquely by its barycentric coordinates relative to its \(n\) vertices. Each coordinate of \(G\) is \(1/n\). The contribution of the \(n-1\) edge points to each vertex coordinate must therefore be \((n-1)/n\), which lies strictly between zero and one.

## Proof

### 1. Every balanced configuration has a spanning-tree support

Let \(X\) satisfy (1). No \(x_r\) can be a simplex vertex: its barycentric coordinate at that vertex would contribute \(1\), exceeding the required coordinate sum \((n-1)/n\). Each \(x_r\) therefore lies in the relative interior of a unique simplex edge. Construct the **multigraph** \(H\) on the \(n\) vertices having one edge, with multiplicity, for each \(x_r\).

If \(A\) were a connected component of \(H\) of size \(1\le k<n\), and \(r_A\) of the chosen points lay on edges of that component, summing the barycentric coordinates over the vertices in \(A\) would give
\[
r_A=\frac{k(n-1)}n.
\]
Since \(r_A\) is an integer and \(\gcd(n,n-1)=1\), this is impossible for \(1\le k<n\). Thus \(H\) is connected. It has exactly \(n\) vertices and \(n-1\) edges counted with multiplicity, hence is a tree; in particular, all its edges are distinct.

### 2. The cut formula and converse

For an edge \(e=\{i,j\}\), let deleting \(e\) partition the tree into \(A\) and its complement, with \(i\in A\) and \(|A|=k\). Exactly \(k-1\) of the other edge points lie entirely on edges within \(A\). Their total barycentric contribution to the coordinates indexed by \(A\) is \(k-1\). The chosen point on \(e\) therefore contributes exactly
\[
\frac{k(n-1)}n-(k-1)=\frac{n-k}n
\]
to vertex \(i\), proving the unique formula (2). Both coefficients are strictly between zero and one.

Conversely, choose **any** labeled tree \(T\) and place point (2) on every edge. At any vertex \(i\), the coefficient contributed by edge \(\{i,j\}\) equals \(|C_{j}|/n\), where \(C_j\) is the component reached through \(j\) after deleting that edge. As \(j\) ranges over the neighbors of \(i\), these components partition the other \(n-1\) vertices. Therefore the total coefficient at \(v_i\) is
\[
\sum_{j\sim i}\frac{|C_j|}{n}=\frac{n-1}{n},
\]
so the points average to \(G\). They lie strictly inside the distinct tree edges. Distinct trees yield distinct point sets because distinct open edges of a simplex have disjoint relative interiors. By Cayley's labeled-tree formula, the number of configurations is \(n^{n-2}\).

### 3. Exact regular-simplex dispersion

Represent the centered regular simplex with edge length \(s\) in the hyperplane \(\sum z_i=0\) of \(\mathbb R^n\) using
\[
v_i-G=\frac{s}{\sqrt2}\left(e_i-\frac1n\mathbf1\right),
\]
where \(e_i\) are the standard coordinate unit vectors and \(\mathbf1\) is the all-ones vector. Formula (2) gives, for an edge whose deletion leaves components of sizes \(k\) and \(n-k\),
\[
\lVert x_e-G\rVert^2
=\frac{s^2}{2}\left(\frac{n-1}{n}-\frac{2k(n-k)}{n^2}\right).
\tag{5}
\]
Each unordered pair \(\{i,j\}\) of tree vertices contributes one unit to \(k_e(n-k_e)\) for each edge \(e\) on its unique tree path. Therefore
\[
\sum_{e\in E(T)}k_e(n-k_e)=W(T).
\tag{6}
\]
Summing (5) over its \(n-1\) edges yields
\[
\sum_e\lVert x_e-G\rVert^2
=s^2\left(\frac{(n-1)^2}{2n}-\frac{W(T)}{n^2}\right).
\]
Finally, since \(\sum_e(x_e-G)=0\), the standard polarization identity gives
\[
\sum_{e<f}\lVert x_e-x_f\rVert^2
=(n-1)\sum_e\lVert x_e-G\rVert^2,
\]
proving (3).

### 4. Sharp extremes, including equality

Every \(n\)-vertex tree has \(n-1\) pairs of adjacent vertices; each other pair has graph distance at least two. Thus
\[
W(T)\ge (n-1)+2\left(\binom n2-(n-1)\right)=(n-1)^2.
\]
For \(n\ge4\), equality forces every nonadjacent pair to have distance exactly two, or equivalently the tree to be a star. The star attains this bound.

For the upper bound, choose a leaf \(v\). List the distances from \(v\) to the other vertices in ascending order as \(d_1,\ldots,d_{n-1}\). Then \(d_k\le k\): if the eccentricity is at least \(k\), the initial \(k\) vertices on a longest path give \(k\) vertices within distance \(k\); otherwise every vertex is within distance less than \(k\). Hence
\[
\sum_{u\ne v}\operatorname{dist}_T(v,u)
\le\frac{n(n-1)}2.
\]
Removing the leaf preserves a tree. Induction gives
\[
W(T)\le \frac{n^3-n}{6},
\]
with equality exactly when \(T\) is a path: equality in the leaf-distance sum forces one vertex at each distance \(1,\ldots,n-1\), hence a leaf-rooted path. Direct calculation gives \(W(P_n)=(n^3-n)/6\). Inserting both sharp Wiener bounds into (3) proves (4), reversing the direction of the inequalities because the coefficient of \(W\) is negative. The equality counts are \(n\) labeled stars and \(n!/2\) labeled paths for \(n\ge4\). In the triangular case these families coincide.

## Verification

The standalone `verify.py` uses **exact rational arithmetic** and an independent construction: it enumerates Prüfer codes, rebuilds each labeled tree, computes each cut by graph traversal, forms the actual affine-coordinate edge points, and computes all pairwise squared distances directly. It independently calculates the Wiener index by all-pairs shortest paths, then checks (1)–(4), the individual cut weights, and equality classifications.

This verification was exhaustive for \(n=3,4,5,6\), respectively \(3,16,125,1296\) labeled trees, with another 150 reproducible pseudorandom trees checked at each of \(n=7,8,9,12,17,30\). The script returned `VERIFY_OK`. It requires only the Python standard library. The quantified all-dimensional result is proved analytically above; finite enumeration is corroboration, not an infinite proof.

For the regular tetrahedron (\(n=4\)), the 16 configurations divide into 12 path configurations of energy \(3s^2/2\) and four star configurations of energy \(27s^2/16\).

## Relationship to prior work

Dobbins's 2013 preprint (later *Inventiones Mathematicae*) proves that every point of any \(d\)-polytope is the equal-weight barycenter of \(d\) points on its edges. That theorem establishes **existence**, including the simplex centroid case, but does not give the finite labeled-tree classification, the unique component-size coefficients, or the energy/Wiener identity. The paper explicitly leaves computational determination of such points for further work; the present theorem supplies an exact procedure for this canonical centroidal instance.

Barba and coauthors' weight-balancing research gives independent geometric motivations and related existence constructions. Dobbins and Frick's 2018 continuation treats mixed skeleton dimensions and weight constraints using simplices, without the present tree enumeration or Euclidean dispersion correspondence.

On the combinatorial side, Cayley's tree count and the extrema of the classical Wiener index are known. Their use here is not presented as an independent advance in graph theory. The new link is the **geometric bijection** from balanced simplex-edge masses to *every* labeled tree, with the exact metric identity (3); the familiar graph invariants then transfer to sharp geometric statements.

We also compared the construction with the graphical-zonotope viewpoint: for each tree, balancing asks whether the uniform coordinate vector belongs to the Minkowski sum of its edge segments. General zonotope/permutohedron facts make this a natural reformulation, but the cited closest polytope-skeleton results do not state the full bijection or the energy identity.

## Limitations

The exact count holds for the **vertex centroid** of a simplex, equal weights, and exactly one fewer point than vertices. It does not classify all possible balancing configurations for an arbitrary target point or non-simplex polytope. Affine invariance of the bijection does not extend to the metric energy: formula (3) requires a regular Euclidean simplex.

The Wiener extremal inequalities and Cayley's formula are classical ingredients. The novelty claim does not extend to those results individually. The primary literature contains existential balancing theorems; a differently indexed treatment of the centroidal simplex case or a zonotope reformulation could already contain an equivalent tree classification, and this remains a historical originality risk.

## References

1. M. G. Dobbins, *A point in a \(nd\)-polytope is the barycenter of \(n\) points in its \(d\)-faces*, arXiv:1312.4411v1 (public 16 December 2013); *Inventiones Mathematicae* 199 (2015), 287–292, DOI: 10.1007/s00222-014-0523-2. The source lists primary MSC 51M04.
2. L. Barba, O. Cheong, J.-L. De Carufel, M. G. Dobbins et al., *Weight balancing on boundaries and skeletons*, SoCG 2014, DOI: 10.1145/2582112.2582142; later account arXiv:1511.04123.
3. M. G. Dobbins and F. Frick, *Barycenters of points in polytope skeleta*, arXiv:1809.01613 (2018).
4. H. Wang, *The extremal values of the Wiener index of a tree with given degree sequence*, arXiv:0709.1679 (2007), for a broader classical tree-index context.
