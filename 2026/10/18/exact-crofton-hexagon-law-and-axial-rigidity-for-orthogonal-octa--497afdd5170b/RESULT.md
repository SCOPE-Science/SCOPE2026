# Exact Crofton hexagon law and axial rigidity for orthogonal octahedra

## Finding
For every \(a,b,c>0\), consider the three-dimensional orthogonal cross-polytope
\[
K(a,b,c)=\operatorname{conv}\{\pm a e_1,\pm b e_2,\pm c e_3\}.
\]
Choose an **unoriented affine plane** from Euclidean-motion-invariant measure, conditioned on intersecting the interior of this body, and let \(N\) be the number of vertices of the intersection polygon. Put
\[
L_{ab}=\sqrt{a^2+b^2},\quad L_{bc}=\sqrt{b^2+c^2},\quad L_{ca}=\sqrt{c^2+a^2},\qquad S=L_{ab}+L_{bc}+L_{ca},
\]
\[
T=L_{ab}\arctan\frac{ab}{cL_{ab}}+L_{bc}\arctan\frac{bc}{aL_{bc}}+L_{ca}\arctan\frac{ca}{bL_{ca}}.
\]
Almost surely the section is either a quadrilateral or a hexagon, with the **complete exact law**
\[
\boxed{\Pr(N=6)=\frac{\pi S}{2T}-2,\qquad\Pr(N=4)=3-\frac{\pi S}{2T}.}
\]
All inverse tangents take their values in \((0,\pi/2)\). These formulas cover every strictly positive independent triple of perpendicular semiaxes.

For the axially stretched family \(a=b=1\), \(c=\lambda>0\), the hexagon probability increases strictly on \((0,1)\), decreases strictly on \((1,\infty)\), and attains its unique maximum at \(\lambda=1\):
\[
\boxed{\max_{\lambda>0}\Pr(N=6)=\frac{\pi}{\arccos(1/3)}-2\approx0.552149656059771.}
\]
Its two sharp degeneration laws are
\[
\lim_{\lambda\downarrow0}\Pr(N=6)=\sqrt2-1,\qquad
\Pr(N=6)\sim\frac{\sqrt2}{\lambda}\quad(\lambda\to\infty).
\]
The equal-axis probability is supplied as a benchmark, not claimed to be new by itself.

## Assumptions and scope
The ambient Euclidean metric is fixed. The vectors \(e_1,e_2,e_3\) are perpendicular unit coordinate vectors, and \(a,b,c>0\). A generic unoriented plane is \(H(n,t)=\{x\in\mathbb R^3:n\cdot x=t\}\), where \(n\in S^2\) and \(t\in\mathbb R\), modulo \((n,t)\sim(-n,-t)\). The unconditioned invariant measure is proportional to spherical area measure \(d\sigma(n)\) times Lebesgue measure \(dt\). We condition on \(H(n,t)\) meeting the interior of \(K\). Crucially, **the normal is not uniform after conditioning**: its density is proportional to the width of the body in that direction. Ties in vertex heights or offsets through vertices have probability zero.

The result is for affine cuts, not uniformly oriented *central* sections or orthogonal *projections*. Linear transformations that are not Euclidean similarities change this probability distribution. The explicit optimizer statement is restricted to the one-parameter axial family; it is not an all-triaxial extremality claim.

## Proof
**1. Section-vertex classification and Crofton conditioning.** Fix a generic unit vector \(n\) and let \(A>B>C>0\) be the decreasing rearrangement of \(a|n_1|,b|n_2|,c|n_3|\). The vertex heights of \(K\) are \(\pm A,\pm B,\pm C\). Every octahedron vertex has four neighbors: its edge graph is the complete tripartite graph on the three antipodal pairs. For a plane with \(B<|t|<A\), exactly one vertex lies on the smaller side, so the section meets precisely its four incident edges and is a quadrilateral. For \(0<|t|<B\), the smaller side has either two vertices from different antipodal pairs, joined by an edge, or three vertices from distinct pairs forming a triangular face. The cut intersects respectively \(4+4-2=6\) or \(3\cdot4-2\cdot3=6\) edges, so the section is a hexagon. The same holds for negative \(t\) by symmetry. Therefore \(N=6\) exactly when \(|t|<B\), outside null sets.

For each \(n\), conditioning on intersection permits \(-A<t<A\). Integrating the invariant plane measure first in \(t\), the overall numerator for six-sided sections is \(\int 2B\,d\sigma\), and the total intersection mass is \(\int2A\,d\sigma\). Hence
\[
\Pr(N=6)=\frac{\mathbb E B}{\mathbb E A},
\]
where the expectations on the right now use an **unweighted uniform** spherical normal.

**2. Pairwise maximum reduction.** For any three nonnegative reals \(x,y,z\), their middle order statistic obeys the pointwise identity
\[
\operatorname{med}(x,y,z)=\max(x,y)+\max(y,z)+\max(z,x)-2\max(x,y,z).
\]
For \(n\) uniform on \(S^2\), polar coordinates in any coordinate two-plane give
\[
\mathbb E\max(a|n_1|,b|n_2|)
=\mathbb E\sqrt{n_1^2+n_2^2}\cdot\frac{2}{\pi}\sqrt{a^2+b^2}
=\frac\pi4\cdot\frac2\pi L_{ab}=\frac{L_{ab}}2.
\]
The angular integral is exact: over a quadrant the dividing angle satisfies \(\tan\theta=a/b\), and the integral of the larger of \(a\cos\theta\) and \(b\sin\theta\) is \(\sqrt{a^2+b^2}\). The radial average is \(\pi/4\). Summing the three pairs yields
\[
\mathbb E B=\frac S2-2\mathbb E A.
\]

**3. Exact mean support by the polyhedral mean-width formula.** The support function of \(K\) is \(h_K(n)=A\). For any three-dimensional convex polytope \(Q\), the mean Euclidean width is
\[
\overline w(Q)=\frac1{4\pi}\sum_{e\in E(Q)}\ell(e)\gamma(e),
\]
where \(\ell(e)\) is edge length and \(\gamma(e)\) is the exterior dihedral angle. One standard derivation applies the Euclidean Steiner formula to \(Q+rB_2^3\): its quadratic coefficient is \(\frac12\sum_e\ell(e)\gamma(e)=2\pi\overline w(Q)\). Here central symmetry gives \(\overline w(K)=2\mathbb E h_K=2\mathbb E A\).

There are four edges joining the \(a\)- and \(b\)-axis vertex pairs, each of length \(L_{ab}\). Their two adjoining face outward normals are proportional to \((\pm1/a,\pm1/b,1/c)\) and \((\pm1/a,\pm1/b,-1/c)\), so their exterior dihedral angle is
\[
\gamma_{ab}=2\arctan\frac{ab}{cL_{ab}}.
\]
The other eight edges break into four each of types \(bc\) and \(ca\), with corresponding cyclic formulas. Consequently
\[
\sum_e\ell(e)\gamma(e)=8T,
\quad\overline w(K)=\frac{2T}{\pi},
\quad\mathbb E A=\frac T\pi.
\]
Inserting these identities into \(\mathbb EB/\mathbb EA\) proves the two exact probability formulas.

**4. Strict axial optimizer.** Set \(a=b=1,c=\lambda\), \(R=\sqrt{1+\lambda^2}\), and write
\[
S(\lambda)=\sqrt2+2R,\quad
\psi(\lambda)=\arctan\frac1{\sqrt2\lambda},\quad
\phi(\lambda)=\arctan\frac\lambda R,\quad
T(\lambda)=\sqrt2\psi+2R\phi.
\]
Direct differentiation gives \(S'=2\lambda/R\), \(\psi'=-\sqrt2/(1+2\lambda^2)\) and \(\phi'=1/[R(1+2\lambda^2)]\). The last two contributions cancel exactly, giving \(T'=S'\phi\). Therefore
\[
\left(\frac TS\right)'=\frac{S'}{S^2}\bigl(S\phi-T\bigr)
=\frac{\sqrt2 S'}{S^2}\bigl(\phi-\psi\bigr).
\]
Both angles lie in \((0,\pi/2)\), and comparison of their arguments gives \(\phi<\psi\) for \(0<\lambda<1\), equality at \(\lambda=1\), and \(\phi>\psi\) for \(\lambda>1\) (equivalently the positive root of \(2\lambda^4-\lambda^2-1=0\) is \(\lambda=1\)). Thus \(T/S\) has its unique strict minimum at \(1\). Because \(\Pr(N=6)=\pi/(2(T/S))-2\), the hexagon probability has the asserted unique strict maximum. At \(\lambda=1\), \(2\arctan(1/\sqrt2)=\arccos(1/3)\), producing the benchmark formula.

For \(\lambda\downarrow0\), \(S\to\sqrt2+2\) and \(T\to\pi\sqrt2/2\), proving the first degeneration limit. For \(\lambda\to\infty\), \(S=2\lambda+\sqrt2+O(\lambda^{-1})\) and \(T=\pi\lambda/2+O(\lambda^{-1})\), giving \(\Pr(N=6)=\sqrt2/\lambda+O(\lambda^{-2})\). The proof is valid for every positive parameter, without numerical extrapolation.

## Verification
Run `python3 octahedron_crofton_check.py` with Python 3 and NumPy. Its independent check explicitly lists all twelve octahedron edges and counts signed crossings of each plane rather than reusing the median formula. It compares a width-weighted estimate from 200,000 Gaussian unit normals and independent offsets for each of six strongly different aspect ratios against the analytical expression. All 1,200,000 sampled planes had four or six crossing edges; absolute differences were below \(0.0017\). The checker also verifies the regular-case trigonometric simplification; its successful output terminates with `OCTAHEDRON_CROFTON_CHECK_OK`.

The finite random tests are only diagnostics. The proof for all parameters is the exact edge-cut classification, deterministic order-statistic identity, polyhedral mean-width evaluation, and derivative-sign factorization above.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg, and Prün [1] investigate combinatorial information encoded by affine and central polytope sections and prove slice-equivalence and reconstruction statements. Their full available text supplies the motivating section-type framework but does not calculate this Euclidean Crofton distribution for orthogonally stretched octahedra.

Known regular-cross-polytope affine-section face-vector formulas cover the equal-axis octahedron; the regular-case value here is consequently a benchmark rather than a novel isolated invariant. The existing full-axis and axial **octahedron shadow** analyses [2,3] give exact probabilities for random **orthogonal projections**, which are not probabilities for random **noncentral affine intersections**. Even after identifying face combinatorics in individual directions, the random-plane offset and width reweighting change the measure. The full triaxial Crofton law and its strict axial height-ratio classification do not follow by simply replacing parameters in the published shadow formulas. The standard mean-width and solid-angle identities used as tools are not claimed as inventions.

## Limitations
This establishes the complete four-versus-six Crofton law for all positive perpendicular axis lengths and a strict optimizer only in the two-equal-axes subfamily. It does not establish an optimizer for arbitrary independent axis triples or for nonorthogonal affine images. It does not cover central Haar sampling, arbitrary non-invariant plane distributions, or dimensions higher than three. The formula for regular octahedra alone is previously covered. An older or unindexed equivalent Crofton calculation may exist; independent historical-priority review remains outstanding. No independent mathematical audit has been performed.

## References
[1] A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1, first posted September 14, 2026. https://arxiv.org/abs/2609.16195

[2] *Sharp triaxial octahedron shadow bound and quadratic shape stability*, publicly available 2026 study of orthogonal shadow-face probabilities. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-triaxial-octahedron-shadow-bound-and-quadratic-shape-stabi--c544249c351b

[3] *Axial rigidity of six-vertex shadows of octahedra*, publicly available 2026 study of orthogonal shadow-face probabilities. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-axial-rigidity-of-six-vertex-shadows-of-octahedra--ddf3a826ab64
