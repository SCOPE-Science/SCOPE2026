# Euclidean inball contact tensorization for finite metric transportation norms

## Finding

Let \((X_i,d_i)\), for \(1\le i\le s\), be finite metric spaces, each with at least two points, and let \(s\ge2\). Equip \(X=\prod_i X_i\) with the metric \(d(x,y)=\sum_i d_i(x_i,y_i)\). Write \(N_i=|X_i|\) and \(N=\prod_iN_i\). On the zero-sum Euclidean space \(H_X=\{z\in\mathbb R^X:\sum_xz_x=0\}\), consider the real transportation-norm unit ball
\[
 B_X=\operatorname{conv}\left\{\frac{e_x-e_y}{d(x,y)}:x\ne y\right\}.
\]
For each factor, let \(K_i\) be the centered unit Lipschitz ball: the functions \(h:X_i\to\mathbb R\) with \(\sum h=0\) and \(|h(u)-h(v)|\le d_i(u,v)\). Define the exact variance maximum \(\alpha_i=\max_{h\in K_i}N_i^{-1}\sum_u h(u)^2\), its complete maximizer set \(S_i=\{h\in K_i:N_i^{-1}\sum_u h(u)^2=\alpha_i\}\), and \(q_i=\dim\operatorname{span}(S_i)\).

**Contact-and-center tensorization theorem.** The largest Euclidean ball contained in \(B_X\) has radius
\[
 r_X=\left(N\sum_{i=1}^s\alpha_i\right)^{-1/2}.
\]
Precisely \(\prod_i|S_i|\) facets touch the origin-centered ball. Their outward normal vectors, normalized to support value one, are exactly the centered functions
\[
 h(x)=\sum_{i=1}^s h_i(x_i),\qquad h_i\in S_i.
\]
The affine hull of the set of **all centers of radius-\(r_X\) balls** in \(B_X\) is the vector subspace
\[
 L=\left\{z\in H_X:\sum_{x\in X}z_xh_i(x_i)=0\ \text{for every }i\text{ and }h_i\in S_i\right\},
\]
and has dimension \(N-1-\sum_iq_i\). In particular, the radius-attaining center set contains a relative neighborhood of the origin in \(L\).

For Cartesian products of paths, \(X_i=\{0,1,\ldots,n_i-1\}\), \(d_i(u,v)=|u-v|\), \(n_i\ge2\), the theorem gives the fully explicit infinite family
\[
 r_X=\sqrt{\frac{12}{N\sum_i(n_i^2-1)}},\quad
 \#\{\text{tangent facets}\}=2^s,\quad
 \dim\operatorname{aff}(\text{maximum-ball centers})=N-s-1.
\]
Here the only touching-facet normals are the \(2^s\) centered signed coordinate ramps \(h_\varepsilon(x)=\sum_i\varepsilon_i(x_i-(n_i-1)/2)\), \(\varepsilon_i\in\{-1,1\}\). When at least one \(n_i\ge3\), these grids lie beyond both individual paths and Boolean hypercubes.

## Assumptions and scope

All scalars, spaces and supporting normals are real. Euclidean distance means the standard inner product on the zero-sum coordinate subspace of \(\mathbb R^X\), not a rescaled Hilbert metric. The tensor theorem allows arbitrary finite factor metrics, without assuming graph realizability or integral distances. The product metric is the **sum** of factor metrics, not their Euclidean product. Only facets touching the largest ball centered at the origin are counted; the affine-center assertion addresses **all** largest balls, including translated ones. Sets \(S_i\) are finite and nonempty: Euclidean squared norm is strictly convex and maximizers on a compact polytope are vertices. Every \(S_i\) is closed under negation.

## Proof

**1. Polarity and facet distance.** The polar of \(B_X\) in \(H_X\) is the polytope \(K_X\) of centered real \(1\)-Lipschitz functions. Since \(B_X\) is full-dimensional, vertices of \(K_X\) correspond bijectively to facets \(\langle z,h\rangle\le1\) of \(B_X\). The origin-to-facet distance is \(1/\|h\|_2\). Hence the centered Euclidean inradius equals \(1/\max_{h\in K_X}\|h\|_2\); the contacting facets are exactly its squared-norm maximizers. Central symmetry of \(B_X\) implies that no translated ball can have larger radius: if balls centered at \(z\) and \(-z\) of radius \(r\) lie inside, their midpoint ball centered at the origin also lies inside.

**2. Sharp product inequality and equality.** Put the uniform probability measure on each factor and write \(U=(U_1,\ldots,U_s)\) for independent uniform coordinates. For a centered \(1\)-Lipschitz \(h\in K_X\), each one-coordinate section is \(1\)-Lipschitz in its factor metric. The Efron–Stein/orthogonal conditional-variance inequality gives
\[
 \mathbb E[h(U)^2]\le\sum_i \mathbb E\big[\operatorname{Var}(h(U)\mid U_j,\ j\ne i)\big]\le\sum_i\alpha_i.
\]
For clarity, in the finite Hoeffding decomposition \(h=\sum_{\varnothing\ne A\subseteq[s]}h_A\), where the \(h_A\) are mutually orthogonal zero-marginal coordinate-interaction terms, the left side is \(\sum_A\|h_A\|_{L^2}^2\), whereas the first right side is \(\sum_A|A|\|h_A\|_{L^2}^2\). Equality in the first inequality holds **if and only if** all terms involving at least two coordinates vanish: \(h(U)=\sum_i h_i(U_i)\) with each \(h_i\) centered. For such an additive function, its \(1\)-Lipschitz property on the sum metric is equivalent to \(h_i\in K_i\) for every \(i\). Equality in the second inequality therefore holds precisely when \(h_i\in S_i\) for all \(i\). Every such sum is feasible, so the sharp product variance is \(\sum_i\alpha_i\). Multiplying by \(N\) yields the stated maximal squared Euclidean norm. All maximizing \(h\) are vertices of \(K_X\) by strict convexity; the decomposition is unique under zero-mean normalization. This proves the inradius, the complete contacting-normal set, and the product cardinality.

**3. All optimal inball centers.** Any radius-\(r_X\) center \(z\) must obey \(\langle z,h\rangle+r_X\|h\|_2\le1\) for each vertex \(h\) of \(K_X\). For a maximal-norm vertex \(h\), the second term equals one; both \(h\) and \(-h\) occur. Thus \(\langle z,h\rangle=0\) for every contacting normal. Conversely, at the origin every noncontacting vertex has a **strict** inequality; there are finitely many, so sufficiently small vectors orthogonal to every contacting normal still satisfy all their inequalities. Therefore the affine span of the set of optimal centers is the orthogonal complement of the span of all contacting normals inside \(H_X\). Their span is exactly the direct sum of the lifted \(\operatorname{span}(S_i)\). Indeed, \(S_i=-S_i\); subtracting two sums that differ only by the sign of one factor isolates twice that factor. Different lifted centered factor spaces are pairwise orthogonal under the uniform product inner product. The normal rank is \(\sum_iq_i\), proving the affine-dimension and relative-neighborhood assertions.

**4. Grid evaluation.** For any \(1\)-Lipschitz \(g:\{0,\dots,n-1\}\to\mathbb R\), the variance identity and Lipschitz inequality give
\[
 \frac1n\sum_j(g(j)-\overline g)^2
 =\frac1{2n^2}\sum_{u,v}(g(u)-g(v))^2
 \le\frac1{2n^2}\sum_{u,v}(u-v)^2=\frac{n^2-1}{12}.
\]
At equality every pairwise difference has maximal absolute value; in particular the endpoints differ by \(n-1\). The successive increments are bounded by one, so each has the same sign and magnitude one. Thus the only centered maximizers are \(\pm(j-(n-1)/2)\), giving \(\alpha_i=(n_i^2-1)/12\), \(|S_i|=2\), \(q_i=1\). Substitution proves all grid formulas and the complete equality classification.

## Verification

The accompanying `verify_grids.py` uses only exact integer/Fraction arithmetic. For each stated small grid it enumerates assignments of signs along a spanning tree, retains exactly the assignments tight on every edge, checks the global metric constraints and the connected tight-edge criterion, and computes the variance numerator, maximizing normals and their rational rank. Checks cover \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), \((2,3,3)\) and \((2,2,2,2)\); the last case examines \(2^{15}\) sign assignments. The same exact calculations verify predicted maximal squared norms, contact counts and rank in all seven cases. The finite checks corroborate but do not replace the proof valid for all finite factor metrics.

## Relationship to prior work

Bobkov and Houdré (1996, Theorem 1 and Lemma 5) prove the **maximal variance tensorization principle** for independent product variables. That scalar principle is prior work, not a novelty claim. Higashitani, Jochemko and Michałek (first public version 2018-07-20) give general facet descriptions of symmetric edge polytopes. D'Alì, Delucchi and Michałek (first public version 2019-10-11) develop these polytopes and their finite-metric interpretation. Çelik, Jamneshan, Montúfar, Sturmfels and Venturello (first public version 2020-03-15) explicitly treat Cartesian products of paths as finite Wasserstein metrics and tabulate the full face vectors in small grid examples (including the \((3,3)\) and \((3,2)\) cases). Those known face-vector counts are not claimed as new. None of these inspected papers states this **contact-facet product classification plus complete affine-incenter rank law**. The geometric statement unifies the previously considered individual path and Boolean-cube inball calculations while additionally treating arbitrary finite product factors and rectangular grids. Its derivation explicitly requires both the variance equality cases and the polar facet-center conditions; no assertion of a new variance bound is made.

## Limitations

This theorem concerns standard Euclidean inballs of the real symmetric transportation unit ball, not a general Banach-space inradius, Banach–Mazur distance, or all face numbers. The center locus is determined up to its affine span and a relative interior neighborhood; its complete boundary inequalities are not enumerated. Although relevant full-text general polytope papers and the Bobkov–Houdré variance paper were inspected, possible unindexed geometric corollaries or treatments not retrieved remain a bibliographic risk. An independent scientific audit has not been performed.

## References

1. S. G. Bobkov and C. Houdré, *Variance of Lipschitz Functions and an Isoperimetric Problem for a Class of Product Measures*, Bernoulli **2** (1996), 249–255, doi:10.3150/bj/1178291721. Author-hosted full text: https://www-users.cse.umn.edu/~bobko001/papers/1996_Bernoulli_BH.pdf.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public 2018-07-20, https://arxiv.org/abs/1807.07678.
3. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public 2019-10-11, https://arxiv.org/abs/1910.05193.
4. T. Ö. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels and L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725, first public 2020-03-15, https://arxiv.org/abs/2003.06725 (Section 4 and Table 1).
