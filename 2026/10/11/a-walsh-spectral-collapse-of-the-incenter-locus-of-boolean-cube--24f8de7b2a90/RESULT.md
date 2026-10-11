# A Walsh-spectral collapse of the incenter locus of Boolean-cube graphical zonotopes

## Finding
For an integer \(d\ge1\), put \(N=2^d\), let \(Q_d\) be the graph with vertex set \(V=\{0,1\}^d\) and edges differing in precisely one coordinate, and define its **centered graphical zonotope**
\[
Z_d=\sum_{\{v,w\}\in E(Q_d)}\left[-\frac{e_v-e_w}{2},\frac{e_v-e_w}{2}\right]
\subset H=\left\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\right\}.
\]
The affine dimension of \(Z_d\) is \(N-1\); every distance and ball below is intrinsic to \(H\), with its standard Euclidean norm. The exact maximum-inscribed-ball radius is
\[
\rho_d=\begin{cases}
2^{d/2-1},&1\le d\le4,\\[3pt]
\dfrac{d}{2\sqrt{1-2^{-d}}},&d\ge5.
\end{cases}
\]
There is a sharp transition in both the **tangent facets of the ball centered at the origin** and the **complete locus of all maximum-ball centers**:

* For \(1\le d\le4\), exactly the \(2d\) facets given by the two opposite coordinate halfcubes in each coordinate direction touch the origin-centered radius-\(\rho_d\) ball. The incenter locus has affine dimension \(N-d-1\), and its affine hull is the span of the Walsh characters \(\chi_A(v)=(-1)^{\sum_{i\in A}v_i}\) with \(|A|\ge2\). Thus, for example, the locus is \(11\)-dimensional when \(d=4\).
* For \(d\ge5\), exactly the \(2N\) facets corresponding to singleton cuts and their complements touch the origin-centered maximal ball. Every radius-\(\rho_d\) inscribed ball has center \(0\); in particular, the incenter locus is zero-dimensional from \(d=5\) onward.

In both ranges the *entire*, not just affine, incenter locus has the explicit finite halfspace description
\[
\mathcal I_d=\left\{c\in H:\left|\sum_{v\in S}c_v\right|
+\rho_d\sqrt{\frac{|S|(N-|S|)}N}
\le\frac{|\partial S|}{2}
\quad\text{for every }\varnothing\ne S\subsetneq V\right\},
\]
where \(\partial S\) is the edge cut of \(Q_d\). In particular, the low-dimensional locus is a nondegenerate centrally symmetric polytope **relative to its stated affine span**, rather than just a formally described lower-dimensional set.

## Assumptions and scope
The edge segments are all unweighted and normalized to Euclidean half-length \(\|e_v-e_w\|/2=1/\sqrt2\). The zonotope is centered at the origin, rather than given by the translated usual sum of \([e_v,e_w]\); translation does not affect inradii or incenter dimensions. No assertion is made for edge-weighted cubes, powers of hypercubes, deformed graphical zonotopes, or other norms. A *tangent facet* means a genuine codimension-one face whose supporting hyperplane touches the maximal ball centered at the origin. Other choices of a center in \(\mathcal I_d\) may have additional supporting contacts.

## Proof
**1. Reduction to cuts, and a complete center description.** For \(u\in H\), the support function of the centered zonotope is
\[
h_{Z_d}(u)=\frac12\sum_{\{v,w\}\in E(Q_d)}|u_v-u_w|.
\]
The symmetry of \(Z_d\) shows that the origin is a maximum-ball center: averaging the two radius-\(r\) balls with centers \(c\) and \(-c\) inside the convex set yields the centered radius-\(r\) ball. For nonempty proper \(S\subset V\), set
\[
w_S=\mathbf1_S-\frac{|S|}{N}\mathbf1,
\quad
\|w_S\|^2=\frac{|S|(N-|S|)}N,
\quad
h_{Z_d}(w_S)=\frac{|\partial S|}{2}.
\]
Every nonzero \(u\in H\) is a positive combination \(u=\sum_j a_jw_{S_j}\) of such vectors indexed by nested upper level sets, with \(a_j>0\), by sorting the finitely many coordinates of \(u\). Along that decomposition the graph total variation is linear:
\(h_{Z_d}(u)=\sum_j a_jh_{Z_d}(w_{S_j})\), whereas
\(\|u\|\le\sum_j a_j\|w_{S_j}\|\).
Consequently
\[
\rho_d=\min_{\varnothing\ne S\subsetneq V}
\frac{|\partial S|}{2}\sqrt{\frac{N}{|S|(N-|S|)}}.
\tag{1}
\]
The same decomposition proves, in both directions, that \(c+\rho_d B_H\subseteq Z_d\) if and only if
\(\langle c,w_S\rangle+\rho_d\|w_S\|\le h_{Z_d}(w_S)\)
for every nontrivial \(S\). Applying the complementary cut as well produces exactly the asserted full halfspace description of \(\mathcal I_d\). There is no unexamined assumption that the incenter is unique.

**2. Sharp discrete edge isoperimetry and its equality case.** Let \(e(S)\) count edges induced by \(S\), put \(s=|S|\), and adopt \(0\log_2 0=0\). The elementary bound
\[
e(S)\le\frac{s\log_2s}{2},
\quad\text{hence}\quad
|\partial S|=ds-2e(S)\ge s(d-\log_2s)
\tag{2}
\]
follows by induction in \(d\). Split the cube at one coordinate into subsets of sizes \(a\le b\), \(a+b=s\). The cross-matching contains at most \(a\) edges, so by induction \(e(S)\le(a\log_2a+b\log_2b)/2+a\). This is bounded by \(s\log_2s/2\) since the binary entropy \(H_2(t)=-t\log_2t-(1-t)\log_2(1-t)\) satisfies \(H_2(t)\ge2t\) on \(0\le t\le1/2\). Strict concavity makes equality possible only at \(t=0\) or \(1/2\). Moreover, if \(s\) is a power of two, the full equality case forces at every successive split either an entirely occupied side or two identical equal-size optimal slices. Induction therefore identifies precisely the subcubes as equality cases for \(s\) a power of two. In particular, sets of size \(N/2\) attaining (2) are exactly the \(2d\) coordinate halfcubes. Sets of size one automatically attain (2).

**3. No intermediate cut sizes can minimize.** Replacing \(S\) by its complement permits \(1\le s\le N/2\). Combining (1) and (2) gives
\[
\frac{|\partial S|}{2\|w_S\|}
\ge\frac{\sqrt N}{2\ln2}\,f(t),
\qquad t=\ln\frac Ns\in[\ln2,d\ln2],
\qquad f(t)=\frac{t}{\sqrt{e^t-1}}.
\]
The derivative of \(f\) has the sign of \(2(1-e^{-t})-t\), which is positive for small positive \(t\), then negative after its unique positive zero. Thus \(f\) increases and then decreases, so its strict minimum on a nondegenerate closed interval occurs at one of the endpoints; every interior cut size has a *strictly larger* normalized boundary than the better endpoint. At \(s=N/2\) and \(s=1\), the sharp normalized boundaries are, respectively,
\[
\frac{\sqrt N}{2}\quad\text{and}\quad
\frac{d}{2\sqrt{1-1/N}}.
\tag{3}
\]
The halfcube branch is smaller exactly when \(d^2>N-1\), namely for \(2\le d\le4\); the singleton branch is smaller exactly when \(d^2<N-1\), namely for all \(d\ge5\). At \(d=1\) the two types coincide. Equality in (2) and strictness of the interior analysis therefore classify **all** radius-minimizing cuts. They also give the stated radius formula, with no asymptotic qualification.

**4. Tangent facets and center-locus rank.** A cut vector \(w_S\) defines a facet of a connected graphical zonotope exactly when both induced sides are connected; equivalently it is a ray of its essential graphical fan. Each coordinate halfcube and its complement are connected, as are each singleton and its complement in \(Q_d\). Thus all the maximizing cuts found above are genuine facets, and there are no additional tangent facets at the origin.

When \(d\le4\), the positive and negative active inequalities in \(\mathcal I_d\) force
\(\sum_{v:v_i=1}c_v=0\) for all \(1\le i\le d\), in addition to \(\sum_vc_v=0\). The \(d+1\) corresponding normals are independent, since the constant Walsh character and \(d\) degree-one Walsh characters are pairwise orthogonal. Their common orthogonal complement is exactly the span of all \(\chi_A\) with \(|A|\ge2\), of dimension \(N-d-1\). All other cut inequalities are **strict** at \(c=0\). Because there are finitely many of them, a sufficiently small ball in this complement remains feasible, proving this is precisely the affine hull and actual dimension of the incenter locus.

When \(d\ge5\), the active singleton-cut inequality and its complementary inequality force \(c_v=0\) for every \(v\in V\), since \(c\in H\). Thus the incenter locus is exactly \(\{0\}\). This proves both the contact-facet transition and the Walsh-spectral collapse.

## Verification
The standalone Python 3 verifier in `scripts/verify.py` uses exact rational arithmetic to enumerate every nontrivial cut for \(d=1,2,3,4\) (respectively \(2\), \(14\), \(254\), and \(65{,}534\) subsets). It independently checks the squared radius and the complete equality list against the claimed contact families; it also verifies exact Walsh orthogonality and the annihilation of high-degree characters by the low-dimensional active cuts. Deterministically sampled cuts in \(d=5,6\) supply additional boundary checks. The verifier is finite corroboration, not a proof of the all-dimensional statements: those follow from Steps 1–4.

## Relationship to prior work
Padrol, Pilaud, and Poullot study graphical zonotopes, their normal fans, biconnected cuts, and deformation cones; their facet-normal geometry makes it natural to ask which supporting hyperplanes are nearest to an intrinsic Euclidean center. Rashtchian and Raynaud recall the sharp classical Harper–Bernstein–Lindsey–Hart edge-isoperimetric theorem and its induced-edge bound, which controls the cut half of the proof. Pešović and Stojadinović study interpolations between graphical zonotopes and graph associahedra using combinatorial enumerators. These sources do not present the complete Boolean-cube incenter locus, its Walsh-degree affine span, or the sharp transition to a unique incenter at \(d=5\). The general reduction of a graphical-zonotope inradius to a normalized graph-cut minimum is a foundational reduction, **not** the distinct structural conclusion claimed here. The new work is the exact identification and geometric effect of *every* optimal cut for all Boolean-cube dimensions.

## Limitations
The classification applies only to the stated unweighted centered zonotopes with intrinsic Euclidean geometry. It makes no claims about uniqueness under weighted perturbations. The low-dimensional center polytope is given by a complete finite system of cut inequalities and its affine hull and dimension; its full vertex enumeration or volume is not determined. Finite checks do not replace the inductive isoperimetric argument or prove untested dimensions. Literature comparison is based on the specifically inspected sources and searches, not an assertion that every older mathematical work is accessible or that search failure proves novelty.

## References
1. A. Padrol, V. Pilaud, and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first public version 2021-11-24); *Discrete & Computational Geometry* 73 (2025), 447–465. Sections on graphical fans and deformation cones.
2. C. Rashtchian and W. Raynaud, *Edge Isoperimetric Inequalities for Powers of the Hypercube*, arXiv:1909.10435 (first public version 2019-09-23); *Electronic Journal of Combinatorics* 29(1) (2022), P1.47. Introduction and Theorem 1 (classical hypercube edge isoperimetry).
3. M. Pešović and T. Stojadinović, *Between Graphical Zonotope and Graph-Associahedron*, arXiv:2209.12053 (first public version 2022-09-24); *Turkish Journal of Mathematics* 47 (2023), 1362–1373.
