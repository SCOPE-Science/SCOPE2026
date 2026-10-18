# Spherical extremal ellipsoids and bipartite outer-contact topology of regular graphical discotopes

## Finding

Let \(G=([n],E)\) be any **connected finite simple \(d\)-regular graph**, with \(n\ge3\) and therefore \(d\ge2\). For each edge \(\{i,j\}\), let
\[
D_{ij}=\{s e_i+t e_j:s^2+t^2\le1\}\subset\mathbb R^n,
\qquad K_G=\sum_{\{i,j\}\in E}D_{ij}.
\]
All metric assertions use the standard Euclidean structure of \(\mathbb R^n\). The following hold simultaneously.

1. The unique largest inscribed Euclidean ball is \(d B_2^n\), and its full boundary contact set with \(K_G\) is \(\{\pm d e_i:1\le i\le n\}\). More generally, without regularity, a simple graph without isolated vertices has centered inradius equal to its minimum vertex degree.
2. The unique smallest enclosing Euclidean ball is \(R B_2^n\), where \(R=d\sqrt{n/2}\). In fact the **John ellipsoid** is exactly \(d B_2^n\), and the **Löwner ellipsoid** is exactly \(R B_2^n\), without any vertex-transitivity hypothesis.
3. The complete outer-sphere contact set \(\mathcal C_G=K_G\cap R S^{n-1}\) detects bipartiteness. If \(G\) is nonbipartite,
\[
\mathcal C_G=\{(d/\sqrt2)(\varepsilon_1,\ldots,\varepsilon_n):\varepsilon_i\in\{-1,1\}\},
\]
consisting of exactly \(2^n\) isolated points. If \(G\) is bipartite, its two color classes \(L,T\) both have size \(p=n/2\), and
\[
\mathcal C_G=\bigcup_{\varepsilon\in\{-1,1\}^L}\ \bigcup_{\eta\in\{-1,1\}^T}
\left\{x(\theta):0\le\theta\le\frac\pi2\right\},
\qquad
x_i(\theta)=\begin{cases}
d\varepsilon_i\cos\theta,&i\in L,\\
d\eta_i\sin\theta,&i\in T.
\end{cases}
\]
The arcs have disjoint interiors and meet only at their prescribed endpoints. Thus \(\mathcal C_G\), as an embedded topological graph, is the complete bipartite graph \(K_{2^p,2^p}\); it has \(2^{2p}\) quarter-great-circle arcs, \(2^{p+1}\) endpoints, and first Betti number \((2^p-1)^2\).

## Assumptions and scope

The graph is **simple** (one disk per unordered edge), **connected**, and **regular**; \(n\ge3\) excludes the exceptional one-edge graph whose discotope is a Euclidean disk. Each summand is a radius-one **filled** Euclidean disk in its coordinate two-plane, not a line segment and not the convex hull of several disks. The sum is a full-dimensional centrally symmetric convex body because the incident coordinate planes span \(\mathbb R^n\). Here \(B_2^n\) is the unit Euclidean ball and \(S^{n-1}\) its boundary. John and Löwner ellipsoids mean, respectively, the maximum-volume inscribed and minimum-volume containing ellipsoids, allowing arbitrary centers and positive-definite shapes.

## Proof

**Support and the centered inball.** The support of a summand in direction \(u\) is \(\sqrt{u_i^2+u_j^2}\); hence
\[
h_{K_G}(u)=\sum_{\{i,j\}\in E}\sqrt{u_i^2+u_j^2}.
\tag{1}
\]
For \(\|u\|_2=1\), write \(z_i=u_i^2\). Then \(z_i\ge0\), \(\sum_i z_i=1\), and every \(z_i+z_j\in[0,1]\). Since \(\sqrt s\ge s\) on this interval,
\[
h_{K_G}(u)\ge\sum_{\{i,j\}\in E}(z_i+z_j)
=\sum_i\deg(i)z_i\ge\delta(G).
\tag{2}
\]
For any coordinate vector \(e_k\) corresponding to a minimum-degree vertex, equality holds. Thus the origin-centered maximal ball has radius \(\delta(G)\); central symmetry shows no translated ball can have a greater radius, by averaging an inscribed ball and its negative. In the regular case, \(\delta(G)=d\), and all coordinate support planes \(x_i=\pm d\) are supporting planes of \(K_G\). A ball \(B(c,d)\subset K_G\) must satisfy \(\pm c_i+d\le d\) for every \(i\), so \(c=0\).

For completeness, equality in (2) for a regular connected graph on at least three vertices forces the support of \((z_i)\) to be a singleton. Indeed equality in every square-root comparison requires every edge sum \(z_i+z_j\) to equal either \(0\) or \(1\). If two coordinates are positive, choose one such coordinate \(i\). Any incident edge must have sum \(1\), forcing the full support into its two endpoints. But \(d\ge2\), so \(i\) has another neighbor, whose edge sum lies strictly between \(0\) and \(1\), a contradiction. Therefore \(h(u)=d\) only when \(u=\pm e_i\). The inner ball touches \(K_G\) exactly at \(\pm d e_i\), which also belong to \(K_G\) by taking \(e_i\) from each incident disk and zero from the others.

**Outradius and its equality locus.** Put \(m=|E|=nd/2\). Cauchy–Schwarz yields
\[
h_{K_G}(u)^2\le m\sum_{\{i,j\}\in E}(z_i+z_j)=md=\frac{nd^2}{2}.
\tag{3}
\]
Every signed flat vector \(u=\varepsilon/\sqrt n\) attains equality; hence \(R=\sqrt{md}=d\sqrt{n/2}\). For any compact convex body, \(\max_{x\in K}\|x\|_2=\max_{\|u\|=1}h_K(u)\), so this gives the smallest origin-centered enclosing sphere. Because \(K_G\) is centrally symmetric and has points of norm \(R\), a translated ball of the same or smaller radius cannot improve the enclosing radius: averaging squared distances to opposite farthest points forces its center to vanish.

Equality in (3) holds exactly when \(z_i+z_j=2/n\) for **every** graph edge. Along an edge, \(z_j=2/n-z_i\), so along any path the values alternate. Connectedness and an odd cycle force \(z_i=1/n\) at every vertex when the graph is nonbipartite. In the bipartite case, all vertices in one color class have one squared modulus \(a\), all in the other one have squared modulus \(b\), with \(a+b=2/n=1/p\). Allowing both signs independently gives precisely the two asserted descriptions.

To identify these maximizing directions with **actual boundary contacts**, let \(u\) be any unit direction with \(h_{K_G}(u)=R\), and choose a support point \(x\in K_G\) with \(u\cdot x=R\). Inequality (3) gives \(\|x\|\le R\), while Cauchy–Schwarz gives \(R=u\cdot x\le\|x\|\). Equality forces \(x=Ru\). Conversely every outer contact \(x\) yields such a direction \(u=x/R\). For signed flat directions this point is explicitly \((d/\sqrt2)\varepsilon\), obtained by summing \((\varepsilon_i e_i+\varepsilon_j e_j)/\sqrt2\) over all edges. For bipartite directions the edgewise maximizers sum to \(d\varepsilon_i\cos\theta\) on \(L\) and \(d\eta_j\sin\theta\) on \(T\).

At \(\theta=0\) the \(T\)-signs disappear, leaving \(2^p\) distinct vertices supported on \(L\); at \(\theta=\pi/2\) the \(L\)-signs disappear, leaving \(2^p\) distinct vertices supported on \(T\). For \(0<\theta<\pi/2\), no coordinates vanish; thus sign patterns and \(\theta\) are uniquely recoverable. The arcs are quarter-great-circles between orthogonal endpoint vectors, so their incidence structure is exactly \(K_{2^p,2^p}\). As a connected finite graph it has first Betti number
\[
2^{2p}-2^{p+1}+1=(2^p-1)^2.
\tag{4}
\]

**John ellipsoid.** Write an arbitrary inscribed ellipsoid as \(c+A B_2^n\), where \(A\) is invertible. Since \(h_{K_G}(\pm e_i)=d\), the two coordinate support constraints imply
\[
|c_i|+\|A^{\mathsf T}e_i\|_2\le d.
\]
Hadamard's determinant inequality gives \(|\det A|\le\prod_i\|A^{\mathsf T}e_i\|_2\le d^n\). The ball \(dB_2^n\) is already inside \(K_G\), so it reaches the maximum possible ellipsoid volume. Equality forces \(c=0\) and the rows of \(A\) to be mutually orthogonal with norm \(d\), hence the only maximizing ellipsoid is \(dB_2^n\).

**Löwner ellipsoid.** Every signed vertex \(x_\varepsilon=(d/\sqrt2)\varepsilon\) lies in \(K_G\). Consider any enclosing ellipsoid
\[
E=\{x:(x-c)^{\mathsf T}Q^{-1}(x-c)\le1\},\qquad Q\succ0.
\]
Averaging the containment inequality over all independently signed \(\varepsilon_i\in\{-1,1\}\) gives the exact covariance certificate
\[
\frac{d^2}{2}\operatorname{tr}(Q^{-1})+c^{\mathsf T}Q^{-1}c\le1.
\]
Consequently \(\operatorname{tr}(Q^{-1})\le2/d^2\). AM–GM on the positive eigenvalues of \(Q^{-1}\) gives
\[
\det Q\ge\left(\frac{nd^2}{2}\right)^n=R^{2n}.
\]
The containing ball \(RB_2^n\) reaches equality. Equality in both steps forces \(c=0\) and \(Q=R^2 I_n\); therefore it is the unique Löwner ellipsoid.

## Verification

The self-contained standard-library script `verify.py` tests the exact signed covariance identities and the support and outer-contact formulas on connected regular cycles, complete graphs, balanced complete bipartite graphs, a triangular prism, a cube, and the Petersen graph. It also tests independent randomly sampled unit directions and the entire bipartite outer-contact parametrization at several angles. Running `python verify.py` produced:

`PASS: 16 connected regular graphs; 16093 support checks; 4054 outer contacts; 601 exact signed covariance identities.`

These tests are **finite corroboration**, not a substitute for the general argument. The all-dimensional assertions are proved above using support-function inequalities, equality classification on connected graphs, and determinant bounds.

For the three-coordinate-disc case \(G=K_3\), the radii are \(2\) and \(\sqrt6\), and there are eight isolated outer contacts. For the four-cycle \(G=C_4\), the radii are \(2\) and \(2\sqrt2\), and the outer-contact set is an embedded \(K_{4,4}\) with first Betti number \(9\).

## Relationship to prior work

Gesmundo and Meroni introduced and analyzed discotopes as Minkowski sums of generalized disks, emphasizing their facial and algebraic boundaries; see *The Geometry of Discotopes* (arXiv:2111.01241, first posted November 1, 2021), especially Sections 2–3, 6–8 and the three-disk example. The present graph-indexed coordinate-plane specialization uses the same Minkowski-sum construction but computes its Euclidean extremal ellipsoids and **entire outer-contact topology**, which are not furnished by the cited boundary-variety results.

Mathis and Meroni's *Fiber Convex Bodies* (arXiv:2105.12406; DOI:10.1007/s00454-022-00451-3), especially Section 5.2, studies fiber bodies of discotopes, a different operation from the direct inball, circumball, and contact-locus questions here. Classical Hadamard and AM–GM inequalities are used openly; their general validity is not claimed as new.

A published mathematical-record result on the **convex hull** of three orthogonal disks concerns a different body (convex hull versus Minkowski sum). Similarly, graphical zonotopes have **line segments** for edge summands rather than filled two-dimensional disks, so their already-known ellipsoid formulas do not imply this statement.

## Limitations

The exact John–Löwner and contact-topology classification requires connected regular graphs; the auxiliary minimum-degree inradius formula applies more generally to graphs without isolated vertices. The formula does not claim the John or Löwner ellipsoid of an arbitrary nonregular graphical discotope, nor does it determine volumes, algebraic boundary degrees, or numerical algorithms for generic discotopes. The literature comparison cannot exclude an unindexed equivalent formulation under another name. Independent mathematical audit and validation have not been performed.

## References

1. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241 (first posted 2021-11-01), published in *Le Matematiche* 77 (2022), 143–171. https://arxiv.org/abs/2111.01241
2. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406; *Discrete & Computational Geometry* 70 (2023), 1451–1475. https://doi.org/10.1007/s00454-022-00451-3
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded ed., Cambridge University Press, 2014, background on support functions and extremal ellipsoids.
