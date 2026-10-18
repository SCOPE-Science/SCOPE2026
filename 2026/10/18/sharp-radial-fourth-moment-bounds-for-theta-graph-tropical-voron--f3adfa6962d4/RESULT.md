# Sharp radial fourth-moment bounds for theta-graph tropical Voronoi hexagons

## Finding

Let \(G\) be a three-path theta graph with three internally vertex-disjoint paths of positive integral lengths \(a,b,c\ge2\), each edge of unit length. Let \(B\) be an oriented vertex–edge incidence matrix of \(G\), \(K=\ker B\subset\mathbb R^{a+b+c}\), and \(\Pi_K\) the ordinary Euclidean orthogonal projection. On the centered cographic zonotope (equivalently, the tropical Jacobian's Voronoi cell)
\[
 Z_{a,b,c}=\Pi_K([-1/2,1/2]^{a+b+c}),
\]
let \(X\) be uniform with respect to two-dimensional Euclidean area measure. Put \(T=a+b+c\), \(S=ab+bc+ca\), and \(P=abc\). Then its radial fourth moment is
\[
\boxed{J=\mathbb E\|X\|^4=\frac{9S^2T^2+18PST-3P^2-8S^3}{720S^2}.}
\]
Its radial second moment, previously determined in the tropical Jacobian literature, is \(I=\mathbb E\|X\|^2=(ST+P)/(12S)\). The **new sharp universal fourth-to-second ratio inequality** is
\[
\boxed{\frac{168}{125}\le \frac{J}{I^2}<\frac95.}
\]
Equality in the lower bound holds exactly when \(a=b=c\). The upper constant is the supremum, not attained for finite lengths: for example \(a=b=2\) and \(c\to\infty\) gives \(J/I^2\to9/5\). The formula and bounds extend verbatim to arbitrary positive real path lengths through the equivalent metric three-edge banana-graph realization.

## Assumptions and scope

All paths are given a consistent orientation between the two branch vertices; reversing chosen edge orientations merely applies an orthogonal sign change and does not affect radial moments. Each of the three paths has at least two edges so that the theta graph is simple; positive real path-length data may instead be regarded as a metric banana graph with three parallel edges. The metric is **the Euclidean metric inherited from the edge-coordinate cycle subspace**, not the unweighted Euclidean metric on an arbitrary lattice basis. The distribution is uniform area measure on the actual hexagon, not the pushforward of uniform measure on the ambient cube (which is generally nonuniform).

## Proof

Write \(f_a,f_b,f_c\) for the three disjoint path-indicator vectors in the ambient edge space. Cycle vectors are constant on each path with values \(u,v,w\) satisfying \(u+v+w=0\), with intrinsic squared norm \(au^2+bv^2+cw^2\). Let
\[
 g=\frac{f_a}{a}+\frac{f_b}{b}+\frac{f_c}{c},\quad h=\|g\|^{-2}=\frac{P}{S},\quad p_i=\Pi_K f_i=f_i-hg.
\]
The equality for \(p_i\) follows because \(K\) is orthogonal in the three-dimensional path-constant space to \(g\). Therefore
\[
\|p_i\|^2=i-h,\qquad \langle p_i,p_j\rangle=-h\ (i\ne j),\qquad
Z_{a,b,c}=\sum_{i\in\{a,b,c\}}[-p_i/2,p_i/2].
\]
Here the index \(i\) denotes a path length, with copies retained even if two lengths are equal. The positive linear dependence \(p_a/a+p_b/b+p_c/c=0\) makes \(Z\) a centrally symmetric hexagon: its six vertices arise from the sign triples with two signs of one kind and one of the other. Since the sum of their three signs is \(\pm1\), projection of the corresponding half-signed path-indicator vector gives the same squared radius for each vertex,
\[
R^2=\frac{T-h}{4}.
\]
An edge parallel to \(p_i\) joins two consecutive vertices; its squared length is \(i-h\), and their inner product divided by \(R^2\) is
\[
 c_i=1-\frac{i-h}{2R^2}=\frac{T+h-2i}{T-h}.
\]
The Euclidean area of the hexagon is \(\sqrt S\). Indeed, for distinct paths \(i,j\), the Gram determinant of \(p_i,p_j\) is \(ij-h(i+j)=i^2j^2/S\), so the parallelogram area spanned by those generators is \(ij/\sqrt S\). The sum of these three areas is \(S/\sqrt S=\sqrt S\). The area fraction of the **two** central triangles bordering the edge pair parallel to \(p_i\) is
\[
 w_i=\frac{i(T-i)}{2S},\qquad \sum_i w_i=1.
\]
For each triangle with vertices \(0,U,V\), \(\|U\|=\|V\|=R\), and \(\langle U,V\rangle=cR^2\), write a uniform point as \(sU+tV\), with \(s,t\ge0\) and \(s+t\le1\). Its Dirichlet moments give
\[
\mathbb E_\triangle\|sU+tV\|^2=\frac{R^2}{6}(2+c),\qquad
\mathbb E_\triangle\|sU+tV\|^4=\frac{R^4}{45}(7+6c+2c^2).
\]
Specifically, \(\mathbb E(s^4)=1/15\), \(\mathbb E(s^3t)=1/60\), and \(\mathbb E(s^2t^2)=1/90\). Averaging over the six origin-based triangles yields
\[
I=\frac{R^2}{6}\sum_i w_i(2+c_i),\qquad
J=\frac{R^4}{45}\sum_i w_i(7+6c_i+2c_i^2).
\]
Use \(\sum_i i(T-i)=2S\), \(\sum_i i^2(T-i)=TS-3P\), and \(\sum_i i^3(T-i)=T^2S-2S^2-TP\). Simplification gives exactly the claimed second and fourth moments.

For sharpness of the ratio put \(Q=J/I^2\). Its strict upper deficit factors as
\[
\frac95-Q=\frac{4(3P^2+2S^3)}{5(ST+P)^2}>0.
\]
For the lower bound it suffices by symmetry to take \(a=x\), \(b=x+y\), \(c=x+y+z\), with \(x>0\) and \(y,z\ge0\). An exact polynomial identity gives
\[
Q-\frac{168}{125}=\frac{N}{125(ST+P)^2},\quad
N=57S^2T^2+114PST-243P^2-200S^3,
\]
where
\[
\begin{aligned}
N={}&480x^4(y^2+yz+z^2)\\
&+20x^3(2y+z)(31y^2+31yz+34z^2)\\
&+12x^2(89y^4+178y^3z+212y^2z^2+123yz^3+19z^4)\\
&+12xy(y+z)(2y+z)(14y^2+14yz+19z^2)\\
&+y^2(y+z)^2(28y^2+28yz+57z^2).
\end{aligned}
\]
All terms are nonnegative; because \(x>0\), the first term is strictly positive whenever \(y+z>0\). Consequently equality holds precisely at \(a=b=c\). Finally \(a=b=2\), \(c\to\infty\) yields \(Q\to9/5\), proving optimality of both constants.

## Verification

The accompanying standalone `verify.py` checks the exact Dirichlet triangle integration, all rational moment identities, the strict upper deficit, the explicit polynomial positivity certificate (by expanding both sides), the equality condition, and the limiting value. It also verifies the bounds with exact rational arithmetic on \(11^3=1331\) integer triples. Run `python verify.py` with SymPy installed; expected output begins `MOMENT_PROOF_CHECK_OK`. The symbolic identities, together with elementary positivity and the integration argument above, establish the all-parameter theorem; the finite rational sample is ancillary.

## Relationship to prior work

De Jong and Shokrieh, *Tropical moments of tropical Jacobians* (first posted October 5, 2018), Proposition 7.3, identify the orthogonally projected edge cube as the graph Jacobian Voronoi cell; Example 8.3 already computes the **second radial moment** for three parallel edges, namely \((T+P/S)/12\). That formula is used here as a baseline and **not claimed as new**. Bach, Beck, and Rehberg, *Acyclotopes and Tocyclotopes* (first posted September 23, 2024), construct the cographic/Gale zonotope and investigate its combinatorics and Ehrhart data; its analyzed sections do not give fourth radial moments or the sharp normalized bounds. The precise new contributions here are the fourth-moment formula and sharp ratio classification, not the cographic definition, Voronoi property, second moment, or elementary planar hexagon geometry.

## Limitations

The theorem concerns genus-two theta networks and their metric banana equivalents with positive path lengths. It does not determine all higher moments or provide a universal inequality for arbitrary planar lattices. The mathematical overlap assessment is limited to the inspected primary texts and searchable records: a differently titled or unindexed covering result cannot be excluded. No independent mathematical audit has been performed.

## References

1. R. de Jong and F. Shokrieh, *Tropical moments of tropical Jacobians*, arXiv:1810.02639 (initial posting 2018-10-05), especially Proposition 7.3 and Example 8.3. https://arxiv.org/abs/1810.02639
2. E. Bach, M. Beck, and S. Rehberg, *Acyclotopes and Tocyclotopes*, arXiv:2409.15227 (initial posting 2024-09-23), especially the cographic/Gale zonotope construction. https://arxiv.org/abs/2409.15227
