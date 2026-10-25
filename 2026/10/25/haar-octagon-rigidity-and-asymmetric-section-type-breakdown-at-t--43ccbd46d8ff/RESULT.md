# Haar octagon rigidity and asymmetric section-type breakdown at the cuboctahedron

## Finding
Let
\[
K_c=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le c\},\qquad 1<c<3,
\]
and let \(N_c\) be the number of sides of \(K_c\cap U^\perp\), where \(U\) is uniformly distributed on the unit sphere. Write \(p_j(c)=\Pr(N_c=j)\). The standard regular cuboctahedron is \(K_2\).

**Theorem (rigid point and one-sided phase laws).** Every generic central section of \(K_2\) is an octagon. Moreover \(p_8(c)=1\) within the stated parameter interval **if and only if** \(c=2\). For \(\varepsilon\downarrow0\),
\[
\begin{aligned}
p_6(2-\varepsilon)&=\frac{2\sqrt3}{\pi}\varepsilon+O(\varepsilon^2),\\
p_{10}(2-\varepsilon)&=\frac6\pi\left(1-\frac1{\sqrt3}\right)\varepsilon+O(\varepsilon^2),\\
p_8(2-\varepsilon)&=1-\frac6\pi\varepsilon+O(\varepsilon^2),\\
p_4(2-\varepsilon)&=0;
\end{aligned}
\]
whereas
\[
\begin{aligned}
p_4(2+\varepsilon)&=\frac3\pi\varepsilon^2+O(\varepsilon^4),\\
p_6(2+\varepsilon)&=\frac{4\sqrt3}{\pi}\varepsilon+O(\varepsilon^2),\\
p_{10}(2+\varepsilon)&=\frac{12}{\pi}\left(\frac1{\sqrt2}-\frac1{\sqrt3}\right)\varepsilon+O(\varepsilon^2),\\
p_8(2+\varepsilon)&=1-\frac{6\sqrt2}{\pi}\varepsilon+O(\varepsilon^2).
\end{aligned}
\]
In particular, the one-sided linear rates at which octagonal sections cease to be certain have the exact ratio \(\sqrt2\).

There is also an **all-parameter exact law** for quadrilaterals on the cube side of the transition: for every \(2<c<3\), putting \(\delta=c-2\),
\[
\boxed{p_4(c)=\frac{12}{\pi}\arctan\!\frac{\sqrt{1+\delta^2}-1}{\sqrt{1+\delta^2}+1}.}
\]
The formula extends continuously to \(c=2\) and to the untruncated cube at \(c=3\), where it becomes the known cube quadrilateral probability \(6\arcsin(1/3)/\pi\).

## Assumptions and scope
Planes pass through the origin and have rotation-invariant (Haar) distribution: sampling the unit normal uniformly on the sphere produces the same distribution on unoriented planes. The side count is that of the convex section polygon. Exceptional normal directions giving planes through polytope vertices, or through an edge, form a zero-area subset and are excluded from the word *generic*. Parameters lie in the open interval stated; endpoint cube and octahedron values are not new assertions. Only the polytope family \(K_c\), not arbitrary affine deformations, is covered. The probabilities depend on the Euclidean orientation measure, not an affine-pushforward measure.

## Proof
**1. Face-incidence classification.** The polytope has six coordinate faces \(x_i=\pm1\) when their relative interiors are nonempty, and eight diagonal faces \(\pm x_1\pm x_2\pm x_3=c\). For a generic central plane, each intersected face contributes precisely one edge of the section polygon. Opposite faces are simultaneously intersected. By signed-permutation symmetry we may sort the absolute normal coordinates as \(a>b>d>0\).

For \(1<c<2\), write \(s=c-1\). The vertices of a diagonal face, after fixing its octant signs, are the coordinate permutations of \((1,s,0)\); the coordinate face is an \(\ell_1\) diamond of radius \(s\). The pair of coordinate faces associated to \(b\) is crossed exactly when \(b<sa\), and the pair associated to \(d\) exactly when \(d<sa\); the \(a\)-coordinate pair is never crossed. Four diagonal faces are always crossed. Of the other four, a pair is crossed exactly when \(d>sb\), and the last pair never is. Therefore **for every generic normal**
\[
\boxed{N_c=4+2\mathbf1_{\{d>sb\}}+2\mathbf1_{\{b<sa\}}+2\mathbf1_{\{d<sa\}},\qquad 1<c<2.}\tag{1}
\]
For example, the extra diagonal pair corresponds to the sign patterns \((+,+,-)\) and \((-,-,+)\): the smallest face-vertex dot product has the sign of \(sb-d\). The always-crossed pairs have patterns \((+,-,+)\), \((-,+,-)\) and \((+,-,-)\), \((-,+,+)\). The coordinate and diagonal tests together show that the generic counts on this side belong to \(\{6,8,10\}\).

For \(2<c<3\), write \(\delta=c-2\). A diagonal face has vertices at the sign-modified permutations of \((1,1,\delta)\). Its face-vertex dot products give the two possibly crossed pairs \((+,-,+)\) and \((+,-,-)\) (along with their negatives), with crossing criteria respectively \(b>d+\delta a\) and the conjunction \(b+d>\delta a\), \(a>d+\delta b\). The other four diagonal faces are not crossed. The lower two coordinate-face pairs are always crossed, while the \(a\)-coordinate pair is crossed exactly when \(a<b+\delta d\). Hence
\[
\boxed{\begin{aligned}
N_c=4&+2\mathbf1_{\{a<b+\delta d\}}+2\mathbf1_{\{b>d+\delta a\}}\\
&+2\mathbf1_{\{b+d>\delta a\}}\mathbf1_{\{a>d+\delta b\}},\qquad 2<c<3.
\end{aligned}}\tag{2}
\]
Here the generic side counts belong to \(\{4,6,8,10\}\). At \(c=2\), the face vertices are permutations of \((1,1,0)\); for strict \(a>b>d>0\), precisely four square and four triangle faces are crossed, so \(N_2=8\). The other parameters have positive-area regions with a different count: for \(c<2\), take \(a\) and \(b\) nearly equal and \(d\) sufficiently small in (1), obtaining six sides; for \(c>2\), take \(b+d<\delta a\) in (2), obtaining four sides.

**2. Exact quadrilateral law.** For \(0<\delta<1\), equation (2) yields \(N_c=4\) **exactly when** \(b+d<\delta a\). The forward direction can be proved by contradiction: if the last indicator vanishes because \(a\le d+\delta b\) while \(b+d>\delta a\), then \(a<b+\delta d\), so the first indicator is nonzero. Conversely, the inequality \(b+d<\delta a\) forces every added term in (2) to vanish. The event consists of six disjoint spherical cones around the signed coordinate axes: for the cone around \(e_1\), it is \(|u_2|+|u_3|<\delta u_1\). One quadrant of this cone is the spherical triangle generated by \((1,0,0)\), \((1,\delta,0)\), \((1,0,\delta)\). The standard determinant solid-angle formula gives that triangle area as
\[
2\arctan\frac{\delta^2}{\bigl(1+\sqrt{1+\delta^2}\bigr)^2}
=2\arctan\frac{\sqrt{1+\delta^2}-1}{\sqrt{1+\delta^2}+1}.
\]
Each cone has four such triangles, and there are six cones. Division by spherical area \(4\pi\) yields the exact formula. Expanding its arctangent gives \(p_4(2+\varepsilon)=3\varepsilon^2/\pi+O(\varepsilon^4)\).

**3. One-sided asymptotics.** The 48 signed-coordinate-order chambers partition the sphere up to area zero, so the probability measure in the chamber \(a>b>d>0\) is \((12/\pi)\,d\omega\), where \(d\omega\) is spherical area. At \(c=2\), the only first-order changes occur in thin strips beside the two chamber great-circle sides \(a=b\) and \(b=d\). Their intersection at the body diagonal, and the axial corner, contribute area \(O(\varepsilon^2)\). The strict inequalities in (1) and (2) show that first-order changes at \(a=b\) have count 6 on the left and count 10 on the right; at \(b=d\) the roles reverse.

Parameterize the first interface by the rays \((1,1,t)\) and the second by \((1,t,t)\), for \(0\le t\le1\). The inward first-order spherical strip areas are obtained by differentiating the threshold conditions in (1) and (2), giving respectively
\[
\begin{array}{c|c|c}
&c=2-\varepsilon&c=2+\varepsilon\\\hline
a=b &\displaystyle \varepsilon\int_0^1\frac{dt}{(2+t^2)^{3/2}}=\frac{\varepsilon}{2\sqrt3}&\displaystyle \varepsilon\int_0^1\frac{t\,dt}{(2+t^2)^{3/2}}=\varepsilon\left(\frac1{\sqrt2}-\frac1{\sqrt3}\right)\\
b=d &\displaystyle\varepsilon\int_0^1\frac{t\,dt}{(1+2t^2)^{3/2}}=\frac\varepsilon2\left(1-\frac1{\sqrt3}\right)&\displaystyle\varepsilon\int_0^1\frac{dt}{(1+2t^2)^{3/2}}=\frac\varepsilon{\sqrt3}.
\end{array}
\]
Smooth coarea in these open great-circle arcs, together with direct bounded analysis of the finitely many meeting points, yields remainders \(O(\varepsilon^2)\). Multiplying by \(12/\pi\) and assigning the changed side counts gives the displayed four individual linear coefficients. Summing gives \(p_8(2-\varepsilon)=1-6\varepsilon/\pi+O(\varepsilon^2)\) and \(p_8(2+\varepsilon)=1-6\sqrt2\varepsilon/\pi+O(\varepsilon^2)\). This completes the proof.

## Verification
The accompanying `verify.py` is runnable under Python 3 using only the standard library. It independently enumerates the vertices and 24 or 36 true polytope edges from active facets, counts intersected edges for 13,500 generic Gaussian normal samples across nine shape parameters, compares those counts to the two facet formulas, evaluates all four spherical strip integrals by numerical quadrature, checks the exact cone law against the classical cube endpoint, and compares Haar simulations at two small offsets with the leading coefficients, and checks the exact cone probability at three additional cube-side parameters. Run `python3 verify.py` from a directory containing that file. A successful run ends with `ALL_CUBOCTAHEDRAL_PHASE_TRANSITION_CHECKS_OK`. Finite checks corroborate the analytic incidence and integration arguments; they are not proofs of an infinite-parameter theorem.

## Relationship to prior work
Lonke's 1998 paper determines expected face counts of Haar-uniform central sections of cubes, not the four-type phase behavior of \(K_c\). The equal cube quadrilateral probability appearing as the \(c\to3\) endpoint is **known**, and is included solely as a consistency check. Pak's geometry lecture notes describe the same truncated-cube family and identify its cuboctahedral member, but the inspected discussion treats scissor-congruence rather than random central-section probabilities. Berlow, Brandenburg, Meroni and Shankar develop the general hyperplane-chamber method for polytope intersection bodies and treat cubes, but do not evaluate these probabilities for \(K_c\).

Related published calculations of the illumination number and the maximal inscribed tetrahedron throughout this **same** cube–octahedron family give values for other invariants; neither invariant determines the polygon-side probabilities or the asymmetric one-sided derivatives. An available separate exact section-count comparison for the single truncated octahedron \(K_{3/2}\) likewise does not cover the cuboctahedral transition or either side of it. The new statement is therefore distinguished from those exact-source implications. A differently formulated or unindexed stereological formula may exist; a comprehensive historical-priority certification is not claimed.

## Limitations
The theorem concerns generic **central**, not translated, planes and the specific symmetric cube–octahedron intersection family. The one-sided formulas are local near \(c=2\), and apart from the quadrilateral branch do not give complete finite-parameter probability laws. Exceptional orientations have zero Haar probability but may have a different polygon count. The proof is analytical and subject to independent expert review; finite simulations cannot establish its novelty or replace its continuous calculations.

## References
1. Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123, first publicly posted 1998-12-21, https://arxiv.org/abs/math/9812123 .
2. I. Pak, *Lectures on Discrete and Polyhedral Geometry*, chapter 16, Exercise 16.1 and Figure 16.4, 2010 lecture notes, https://www.math.ucla.edu/~pak/geompol8.pdf .
3. K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, first posted 2021-10-12; *Beiträge zur Algebra und Geometrie* 63 (2022), 419–439, https://arxiv.org/abs/2110.05996 .
4. A. van Oosterom and J. Strackee, *The Solid Angle of a Plane Triangle*, *IEEE Transactions on Biomedical Engineering* BME-30 (1983), 125–126, DOI 10.1109/TBME.1983.325207 (standard solid-angle formula).
