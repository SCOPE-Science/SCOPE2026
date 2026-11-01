# Minimal facets and circuit rays of planar prescribed-normal vertex cones

## Finding
For an integer \(n\ge3\), let \(a_i=(\cos\theta_i,\sin\theta_i)\) be distinct prescribed unit support directions with cyclic order \(\theta_0<\cdots<\theta_{n-1}<\theta_n=\theta_0+2\pi\), and with every gap \(\delta_i=\theta_{i+1}-\theta_i\in(0,\pi)\). All indices are cyclic.

Consider the cone of labeled point configurations
\[
C_a=\{(x_i)_{i=0}^{n-1}\in(\mathbb R^2)^n:\langle a_i,x_i-x_j\rangle\ge0\quad(0\le i,j<n)\}.
\]
The complete system of \(n(n-1)\) comparisons is equivalent to just the \(2n\) adjacent comparisons
\[
\langle a_i,x_i-x_{i+1}\rangle\ge0,\qquad
\langle a_{i+1},x_{i+1}-x_i\rangle\ge0\quad(0\le i<n).
\]
These \(2n\) inequalities are all facets of the full-dimensional cone, hence an irredundant complete description.

Write \(J\) for counterclockwise rotation by \(\pi/2\), put \(t_i=Ja_i\), and identify configurations differing by a common translation. Then \(C_a/\mathbb R^2\) is linearly isomorphic to the pointed cone
\[
Q_a=\left\{(\alpha_i,\beta_i)_{i=0}^{n-1}\in\mathbb R_{\ge0}^{2n}:\ \sum_{i=0}^{n-1}(\alpha_i+\beta_{i-1})t_i=0\right\}.
\]
Every extreme ray is a positive circuit using either two antipodal directions or three directions whose convex hull has the origin in its strict interior. Each participating direction independently admits one of two copies, so each antipodal pair supplies four rays and each strict-origin triple supplies eight.

In the regular case \(\theta_i=\theta_0+2\pi i/n\), the exact ray count is
\[
\#\operatorname{rays}(C_a/\mathbb R^2)=
\begin{cases}
\dfrac{n(n^2-1)}3,&n\text{ odd},\\[3pt]
\dfrac{n(n-2)(n-4)}3+2n,&n\text{ even}.
\end{cases}
\]
For example, the counts in orders \(3,4,5,6,7,8\) are respectively \(8,8,40,28,112,80\). These counts concern the **parameter cone**, not necessarily different convex hulls after forgetting labels.

## Assumptions and scope
The normal list must be pairwise distinct, cyclically ordered, with all successive angular gaps strictly less than \(\pi\). The cone includes degenerate point configurations, and its two-dimensional lineality consists of translating all points by the same vector. The ray claim always means rays of the pointed translation quotient. For the closed-form counts only, directions are equally spaced on the circle; no assumption of distinct positions \(x_i\) is imposed.

## Proof
**1. Adjacent comparisons imply every support inequality.** Put \(d_i=x_{i+1}-x_i\). The two adjacent comparisons state \(\langle a_i,d_i\rangle\le0\) and \(\langle a_{i+1},d_i\rangle\ge0\). Since \(0<\delta_i<\pi\), elementary planar sector geometry gives the *unique* decomposition
\[
d_i=\alpha_i t_i+\beta_i t_{i+1},\qquad
\alpha_i=\frac{\langle a_{i+1},d_i\rangle}{\sin\delta_i}\ge0,\quad
\beta_i=-\frac{\langle a_i,d_i\rangle}{\sin\delta_i}\ge0.
\]
Fix \(i,j\) and lift their angles so the counterclockwise difference \(\Delta\) belongs to \((0,2\pi)\). If \(\Delta\le\pi\), the intervening tangent vectors \(t_k,t_{k+1}\) on the forward arc all have nonpositive scalar product with \(a_i\). Consequently
\(\langle a_i,x_j-x_i\rangle=\sum_{k=i}^{j-1}\langle a_i,d_k\rangle\le0\).
If \(\Delta\ge\pi\), every tangent vector on the complementary forward arc from \(j\) to \(i\) has nonnegative scalar product with \(a_i\), so the same conclusion follows from \(x_j-x_i=-\sum_{k=j}^{i-1}d_k\). Thus all pairwise comparisons hold, including the boundary case \(\Delta=\pi\).

**2. Linear parametrization and its dimension.** By telescoping, the closure condition \(\sum_i d_i=0\) becomes
\[
\sum_i(\alpha_i+\beta_{i-1})t_i=0.
\]
Conversely, any nonnegative \((\alpha,\beta)\) satisfying this condition determines all \(d_i\), and their cumulative sums determine \((x_i)\) uniquely modulo translation. The maps are linear in both directions because adjacent tangent vectors are linearly independent. The closure matrix has rank two, hence the quotient dimension is \(2n-2\). Since no cyclic gap reaches \(\pi\), the origin is strictly inside the convex hull of the \(t_i\); it follows that positive numbers \(c_i\) satisfying \(\sum_i c_it_i=0\) exist. Splitting each \(c_i\) into two positive parts gives an interior point of \(Q_a\).

**3. Facet minimality.** Every coordinate inequality \(\alpha_i\ge0\) and \(\beta_i\ge0\) cuts a facet. For example, set \(\alpha_i=0\), \(\beta_{i-1}=c_i\), and for every \(k\ne i\) set \(\alpha_k=\beta_{k-1}=c_k/2\). This satisfies closure, has exactly the selected coordinate zero, and all other coordinates strictly positive. The same construction works with the copies exchanged. Hence every nonnegativity hyperplane supports a codimension-one face of \(Q_a\), corresponding to one of the \(2n\) original adjacent inequalities. The cone is full-dimensional before quotienting, and no further facets occur in this halfspace presentation.

**4. Extreme-ray classification.** For a nonnegative kernel \(\{z\ge0:Az=0\}\) of a rank-two matrix whose columns are nonzero, an extreme ray has inclusion-minimal positive dependent support. Indeed, if the kernel restricted to its strictly positive support has dimension at least two, a nonproportional kernel perturbation preserves nonnegativity for sufficiently small positive and negative scalars, contradicting extremality. Conversely, a one-dimensional positive kernel on its support gives a ray. A minimal positive dependence of planar nonzero vectors is either one antipodal pair or a triple having the origin in its strict interior. Both copies associated with one \(t_i\) cannot occur in minimal support: transferring weight between identical columns gives a perturbation. Each pair therefore has \(2^2=4\) independent copy choices and each triangle has \(2^3=8\). The isomorphism in Step 2 preserves extreme rays.

**5. Closed counts for regular directions.** For odd \(n=2m+1\), the central triangles are exactly triples whose three cyclic index gaps are at most \(m\). The number of ordered positive gap triples with sum \(n\) and this bound is \(m(m+1)/2\); since each triangle has three starting vertices, its total count is \(n m(m+1)/6=n(n^2-1)/24\). There are no antipodal pairs. For even \(n=2m\), the strict gap bound is \(m-1\), yielding \((m-1)(m-2)/2\) ordered gap triples, so there are \(n(n-2)(n-4)/24\) central triangles, as well as exactly \(n/2\) antipodal pairs. Multiplying the two types by eight and four, respectively, gives the displayed formulas. The gap-composition counts follow directly by inclusion-exclusion: subtract the three disjoint cases in which one gap exceeds the permitted maximum from the total \(\binom{n-1}{2}\) positive compositions.

## Verification
The standalone standard-library script `verify.py` checks all strict-origin triples and the closed count for every \(3\le n\le18\). For \(3\le n\le12\) it constructs 1,480 pair/triple circuit rays with all independent copy choices, verifies closure and checks every defining support comparison numerically. The successful local run reported `PASS`. These checks are finite corroboration only. Steps 1–5 establish the universal conclusions analytically; no numerical test is used to infer a statement about arbitrary \(n\).

## Relationship to prior work
Rieger (2026) defines exactly the prescribed-normal vertex cone and proves its general polyhedral nature and useful sufficient redundancy criteria (in particular, Lemmas 22–23). The finite adjacent reduction is consistent with, and can also be reached by iterating, those redundancy mechanisms. It is **not** presented as an independently new principle. The contribution established here is the complete, irredundant planar facet presentation *together with* the positive-circuit identification of every translation-quotient extreme ray and the explicit parity-dependent enumeration for every regular direction list. The cited source's relevant Sections 3–5 do not give that generator description or count.

Padrol, Pilaud and Poullot (2023) study facet descriptions and rays of deformation/type cones of graphical zonotopes, which fix a normal fan or edge-direction constraints for a different family. Their results do not directly identify the doubled-incidence positive-kernel cone above. The ambient positive-circuit criterion itself is standard linear algebra, not a claimed new theorem.

## Limitations
The finding describes the labeled configuration cone, not the nonconvex image of that cone under taking convex hulls, and says nothing about higher-dimensional normal configurations. The classification of rays uses the strict gap hypothesis; at gaps equal to \(\pi\) the unique tangent-sector decomposition breaks down. Similar complete formulas may exist in unindexed older literature; publication priority and independent review remain open.

## References
1. J. Rieger, *Galerkin approximations to the space of convex bodies by polytopes in nondegenerate V-representation*, arXiv:2608.26615v1, first submitted 2026-08-27, https://arxiv.org/abs/2608.26615. Relevant material: Sections 2.2, 3, 4, 5, especially Lemmas 22–23.
2. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry, online 2023-10-13, https://doi.org/10.1007/s00454-023-00586-x. Relevant material: Introduction and Section 2 on deformation cones.
