# Face dimension determines all contraction orbits of finite-dimensional real polyhedral Banach spaces

## Finding

Let \(X\) be any real normed space of finite dimension \(n\ge 1\) whose closed unit ball \(B\) is a polytope, and let \(S=\partial B\). For each \(x\in S\), let \(F(x)\) be the unique minimal face of \(B\) containing \(x\), and set \(d(x)=\dim_{\mathrm{aff}}F(x)\). Define the invertible-contraction orbit
\[
\mathcal O(x)=\{Tx:T:X\to X\text{ invertible and real-linear},\ \|T\|\le 1\}\cap S.
\]
Then for all \(x,y\in S\),
\[
\boxed{y\in\mathcal O(x)\quad\Longleftrightarrow\quad d(x)\le d(y).}
\]
Consequently, mutual reachability has exactly \(n\) equivalence classes, corresponding to face dimensions \(0,1,\ldots,n-1\), ordered in a chain. Every orbit is relatively open and dense in \(S\), and for \(n\ge2\) the action is not semitransitive. The criterion applies to *every* centrally symmetric polytope, not merely cubes, cross-polytopes, or vertex-transitive unit balls.

## Assumptions and scope

A polyhedral norm means that \(B=\{z:\|z\|\le 1\}\) is a full-dimensional, centrally symmetric polytope with the origin in its interior. Faces are nonempty convex faces of \(B\), and their dimensions are affine dimensions. The minimal face \(F(x)\) exists uniquely and has \(x\) in its relative interior. Every proper face of a finite-dimensional polytope is exposed: there is a real-linear functional \(f\) with \(f(z)\le 1\) on \(B\) and \(F(x)=\{z\in B:f(z)=1\}\). These facts include all nonsimple polytopes. One-dimensional spaces are included.

Contractive means operator norm at most one, without imposing any bound on the norm of the inverse; requiring a contractive inverse would instead impose isometry. The orbit contains only images lying on the unit sphere. No complex-scalar or infinite-dimensional claim is made.

## Proof

**Necessity.** Suppose \(T\) is invertible, \(TB\subseteq B\), and \(Tx=y\in S\). Put \(G=F(y)\). The intersection \(B\cap T^{-1}(G)\) is a face of \(B\): whenever a proper convex combination of two elements of \(B\) belongs to it, both images belong to \(G\) because \(G\) is a face and both images are in \(B\). This face contains \(x\), hence contains the *minimal* face \(F(x)\). Therefore \(T(F(x))\subseteq F(y)\). Since \(T\) is injective, its restriction preserves affine dimension, giving \(d(x)\le d(y)\).

**Sufficiency.** Assume \(k=d(x)\le d(y)=l\). Choose norm-one exposing functionals \(f,g\) so that
\[
F(x)=\{z\in B:f(z)=1\},\qquad F(y)=\{z\in B:g(z)=1\}.
\]
In particular \(f(x)=g(y)=1\). Define \(L_x=\operatorname{span}(F(x)-x)\subseteq\ker f\) and \(L_y=\operatorname{span}(F(y)-y)\subseteq\ker g\); their respective dimensions are \(k,l\). Since \(k\le l\) and both kernels have dimension \(n-1\), basis extension gives a linear isomorphism
\[
U:\ker f\longrightarrow\ker g\qquad\text{with}\qquad U(L_x)\subseteq L_y.
\]
For any \(\varepsilon>0\), define the linear operator
\[
T_\varepsilon(z)=f(z)y+\varepsilon U\bigl(z-f(z)x\bigr).
\]
Here \(z-f(z)x\in\ker f\), so the expression is defined and \(T_\varepsilon(x)=y\). Moreover \(g(T_\varepsilon(z))=f(z)\). If \(T_\varepsilon(z)=0\), then \(f(z)=0\) and hence \(\varepsilon U(z)=0\); thus \(z=0\). Finite dimensionality makes \(T_\varepsilon\) invertible for every \(\varepsilon>0\).

It remains to show \(T_\varepsilon B\subseteq B\) for a sufficiently small common positive \(\varepsilon\). Let \(v\) be any vertex of \(B\). When \(f(v)=1\), the vertex \(v\) lies in \(F(x)\), so \(U(v-x)\in L_y\). As \(y\in\operatorname{relint}F(y)\), the point \(y+\varepsilon U(v-x)\) lies in \(F(y)\subseteq B\) for all sufficiently small \(\varepsilon>0\). When \(f(v)=-1\), central symmetry gives \(-v\in F(x)\), and linearity yields \(T_\varepsilon(v)=-T_\varepsilon(-v)\in-B=B\). Finally, if \(|f(v)|<1\), then \(T_\varepsilon(v)\to f(v)y\) as \(\varepsilon\downarrow0\), while \(\|f(v)y\|=|f(v)|<1\). Thus \(T_\varepsilon(v)\in B\) for all sufficiently small \(\varepsilon\). There are finitely many vertices, so one \(\varepsilon>0\) works for all. Convexity then gives \(T_\varepsilon B\subseteq B\), and therefore \(T_\varepsilon\) is the required invertible contraction.

**Orbit topology.** For every \(k\), the set of boundary points with minimal-face dimension less than \(k\) is the finite union of faces of dimensions at most \(k-1\), hence closed in \(S\). Its complement \(\{y:d(y)\ge k\}\) is therefore relatively open. It is dense because every boundary face lies in some facet, and the relative interiors of facets are dense in \(S\). A full-dimensional \(n\)-polytope has faces of every dimension \(0\) through \(n-1\), proving exactly \(n\) mutual-reachability classes. When \(n\ge2\), a facet-interior point cannot reach a vertex, so the semigroup is not transitive on \(S\).

## Verification

The necessity argument uses only the face-preimage property and injectivity; the sufficiency argument checks all three exhaustive vertex cases \(f(v)=1\), \(f(v)=-1\), and \(|f(v)|<1\), not merely a numerical sample. The one-dimensional boundary and nonsimple vertex cases require no generic-position assumption.

The optional exact-arithmetic program `check_faces.py` tests a non-cubical three-dimensional example with norm \(\|(u,v,w)\|=\max\{|u|,|v|,|u-v|,|w|\}\). It constructs invertible contractions for each of the six permitted ordered face-rank pairs on distinct faces and verifies the image and norm inequalities at all twelve vertices using rational arithmetic. This finite test is illustrative; the quantified result rests on the preceding proof.

## Relationship to prior work

Cabello Sánchez and Cabello Sánchez (2022), arXiv:2209.04652v1, define the contractive-automorphism semigroup, establish necessary smoothness/extremality conditions, describe the two planar \(\ell_1\) orbit types, and prove that a flat target is reachable from any unit vector. In a polyhedral norm, their flat-target result already implies that every unit vector has a dense orbit, because facet-relative-interior points are dense. Thus the dense-orbit consequence alone is *not* claimed as new. The additional result here is the **complete if-and-only-if reachability relation at every intermediate face dimension in every real polyhedral norm**, including nonsimple and noncoordinate polytopes.

A previously published classification of the face-rank reachability preorder for real and complex finite \(\ell_1\) and \(\ell_\infty\) coordinates (published-finding corpus record below) is a special case; its statement expressly does not extend to arbitrary polyhedral norms. The present argument uses the finite exposed-face structure directly and does not assume those coordinate representations.

## Limitations

The result does not apply verbatim to nonpolyhedral balls, arbitrary complex polyhedral analogues, or infinite-dimensional Banach spaces. It gives existence of an invertible contraction but no uniform lower bound for its smallest singular value or norm of its inverse. The exact classification is subject to the possibility of an equivalent description in older, unindexed work on contractive automorphism semigroups.

## References

1. F. Cabello Sánchez and J. Cabello Sánchez, *Dynamics of the semigroup of contractive automorphisms of Banach spaces*, arXiv:2209.04652v1 (first posted 2022-09-10), https://arxiv.org/abs/2209.04652.
2. F. Cabello Sánchez, *Wheeling around Mazur rotations problem*, arXiv:2109.01906v1 (first posted 2021-09-04), https://arxiv.org/abs/2109.01906.
3. *Face-rank orbit stratification for cube and cross-polytope norms*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-face-rank-orbit-stratification-for-cube-and-cross-polytope-norms--5e1433cfc121.
4. J. Becerra Guerrero and Á. Rodríguez Palacios, *Banach spaces with a large semigroup of contractive automorphisms*, J. Math. Anal. Appl. 475 (2019), 642–667, https://doi.org/10.1016/j.jmaa.2019.02.061.
