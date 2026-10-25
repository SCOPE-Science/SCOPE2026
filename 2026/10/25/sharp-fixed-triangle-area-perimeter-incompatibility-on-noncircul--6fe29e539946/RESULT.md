# Sharp fixed-triangle area–perimeter incompatibility on noncircular ellipses

## Finding

For \(a\ge b>0\), consider the ellipse \(E_{a,b}=\{(x,y):x^2/a^2+y^2/b^2\le1\}\). Write \(P_\star(a,b)\) for the maximum perimeter of a triangle with vertices on the boundary, and \(P_A(a,b)\) for the maximum perimeter among the *maximum-area* inscribed triangles. Define the loss incurred by first insisting on maximum area to be \(G(a,b)=P_\star(a,b)-P_A(a,b)\). Then \(G(a,a)=0\), while for every \(a>b>0\),

\[
G(a,b)\ge \frac{81b^7(a^2-b^2)^2}{2048a^{10}}>0.
\]

The nonasymptotic constant is explicit but not asserted sharp. The exact sharp near-circular law is

\[
G(1+\varepsilon,1)=\frac{9\sqrt3}{16}\varepsilon^2+O(\varepsilon^3)
\qquad(\varepsilon\downarrow0).
\]

Equivalently, for \(a/b\downarrow1\), the leading discrepancy is \(\frac{9\sqrt3}{16}(a-b)^2/b\). This is a fixed-three-vertex, two-intrinsic-volume rigidity statement, not a limit with the vertex count tending to infinity.

## Assumptions and scope

Triangles are nondegenerate, have three distinct boundary vertices, and have ordinary Euclidean area and Euclidean perimeter; the ellipse is centered with positive semiaxes. Its area-maximizing triangles form the complete one-parameter family obtained by applying \(A=\operatorname{diag}(a,b)\) to equilateral triples on the unit circle:

\[
X_i(\theta)=A(\cos(\theta+2\pi i/3),\sin(\theta+2\pi i/3)),\quad i=0,1,2.
\]

This follows because the inverse affine map scales all triangle areas by the same factor and the equilateral triangles are the unique maximum-area inscribed triangles of a circle. Their area is \(\Delta=3\sqrt3\,ab/4\). The extrema \(P_\star,P_A\) exist by compactness. If a perimeter-maximizing triple were degenerate, separating its vertices slightly produces positive area without reducing perimeter to first order, and in any case the bound below constructs a strictly better nondegenerate triangle than every area-maximizer.

## Proof

**1. Exact first variation of an area-maximizer.** Put \(u_i=(\cos(\theta+2\pi i/3),\sin(\theta+2\pi i/3))\), and let \(s_i\) be the Euclidean length of the side opposite \(X_i\). Since \(u_{i+1}-u_{i-1}\) is parallel to the quarter-turn of \(u_i\), the ellipse tangent at \(X_i\) is parallel to that opposite side, and

\[
s_i=\sqrt3\,\lVert A Ju_i\rVert,
\quad 3b^2\le s_i^2\le3a^2,
\quad J(x,y)=(-y,x).
\]

Fix an index \(i\), put \(u=s_{i+1}\), \(v=s_{i-1}\), \(w=s_i\), and vary only \(X_i\) along the ellipse with its two neighbors fixed. If the varied vertex moves with unit speed along its tangent, an elementary projection onto the opposite chord gives the magnitude of the perimeter derivative

\[
D_i=\frac{|u-v|\bigl((u+v)^2-w^2\bigr)}{2wuv}.
\]

This is the difference of the two tangent projections of the unit edge vectors. The denominator is nonzero, and the second factor is positive for each nondegenerate triangle.

**2. A uniform nonstationarity bound.** The three numbers \(\sin^2(\theta+2\pi i/3)\) have range at least \(3/4\): their pairwise differences are \(\frac{\sqrt3}{2}\) times three sine values separated by \(2\pi/3\), one of whose absolute values is at least \(\sqrt3/2\). As \(s_i^2=3(b^2+(a^2-b^2)\sin^2(\theta+2\pi i/3))\), some pair has

\[
|u^2-v^2|\ge\frac94(a^2-b^2).
\]

Thus \(|u-v|\ge9(a^2-b^2)/(8\sqrt3\,a)\). Heron's identity and \(\Delta=3\sqrt3\,ab/4\) give

\[
\bigl((u+v)^2-w^2\bigr)\bigl(w^2-(u-v)^2\bigr)
=16\Delta^2=27a^2b^2.
\]

Since \(w^2-(u-v)^2\le w^2\le3a^2\), the first factor is at least \(9b^2\). Also \(2wuv\le6\sqrt3\,a^3\). Consequently, for some vertex of *every* area-maximizing triangle,

\[
D_i\ge\frac9{16}\frac{b^2(a^2-b^2)}{a^4}.
\]

**3. An actual perimeter gain.** Write \(X(t)=(a\cos t,b\sin t)\). As \(|X'(t)|\ge b\), the absolute angle-derivative of the perimeter at the selected vertex is at least \(bD_i\). The other two vertices are fixed. For a signed angular displacement \(|h|\le b/(2a)\), the moving vertex moves by at most \(b/2\); each of its two incident chords originally has length at least \(\sqrt3 b\) and remains longer than \(b\). Since \(|X'|,|X''|\le a\), twice differentiating the two distance functions bounds the second derivative of perimeter in absolute value by

\[
M:=2a+\frac{2a^2}{b}\le\frac{4a^2}{b}.
\]

Also \(|P'(t)|\le2a\). Take \(h=P'(t)/M\), which has \(|h|\le b/(2a)\). Taylor's theorem yields a gain at least \(P'(t)^2/(2M)\), hence

\[
P_\star-\operatorname{per}(X_0X_1X_2)
\ge\frac{b^3 D_i^2}{8a^2}
\ge\frac{81b^7(a^2-b^2)^2}{2048a^{10}}.
\]

This holds for every maximum-area orientation; taking their largest perimeter proves the global inequality and strict incompatibility for \(a>b\). For \(a=b\), equilateral triangles maximize both quantities by Jensen's inequality for the three circular arc gaps.

**4. Sharp near-circle coefficient.** Set \(a=1+\varepsilon\), \(b=1\), and parameterize an ordered boundary triple by

\[
\alpha_i=\theta+2\pi i/3+\delta_i,\quad\sum_i\delta_i=0.
\]

Here \(\theta\) is the mean phase; the two independent \(\delta_i\) measure departures from equally spaced vertices. At \(\varepsilon=0\), perimeter is \(2\sum_i\sin((\alpha_{i+1}-\alpha_i)/2)\), with a strict transverse maximum at \(\delta=0\). The exact length of the side joining angles \(\alpha_i\) and \(\alpha_{i+1}\) is

\[
2\sin\!\left(\frac{\alpha_{i+1}-\alpha_i}{2}\right)
\sqrt{(1+\varepsilon)^2\sin^2\!\left(\frac{\alpha_{i+1}+\alpha_i}{2}\right)
+\cos^2\!\left(\frac{\alpha_{i+1}+\alpha_i}{2}\right)}.
\]

Taylor expansion, uniformly in \(\theta\), gives with \(S_i=\sin(2\theta+4\pi i/3)\)

\[
\begin{aligned}
P(\theta,\delta,\varepsilon)=P_A^{(2)}(\varepsilon)
&-\frac{3\sqrt3}{8}\sum_i\delta_i^2
-\frac{3\sqrt3}{4}\varepsilon\sum_i S_i\delta_i\\
&+O(\varepsilon^3+\varepsilon^2\lVert\delta\rVert
+\varepsilon\lVert\delta\rVert^2+\lVert\delta\rVert^3),
\end{aligned}
\]

where \(P_A^{(2)}(\varepsilon)=3\sqrt3+(3\sqrt3/2)\varepsilon+(3\sqrt3/16)\varepsilon^2\). The constant term is independent of \(\theta\) to second order because the three squared sine values sum to \(3/2\) and their fourth powers sum to \(9/8\). The linear perturbation in \(\delta\) is obtained by differentiating the preceding exact side-length expression; the \(i\)th coefficient is \(-3\sqrt3\,\varepsilon S_i/4\). Completing the square yields a unique transverse optimizer

\[
\delta_i=-\varepsilon S_i+O(\varepsilon^2),
\quad\sum_i S_i=0,
\quad\sum_i S_i^2=3/2,
\]

with gain \((9\sqrt3/16)\varepsilon^2+O(\varepsilon^3)\), uniformly in \(\theta\). By compactness and the strict Jensen maximum at \(\varepsilon=0\), every global perimeter maximizer converges transversely to an equally spaced triple as \(\varepsilon\to0\); the nondegenerate transverse Hessian and first-order stationarity then imply \(\delta=O(\varepsilon)\). Thus this uniform local expansion captures the global maximum. For every area-maximizer \(\delta=0\), its perimeter is \(P_A^{(2)}(\varepsilon)+O(\varepsilon^3)\) uniformly in \(\theta\). Subtracting proves the coefficient in the finding.

## Verification

The standalone `verify_gap.py` checks 800 parameter-orientation instances of the constructive Taylor improvement and four near-circular optimizations against the analytic coefficient. Run `python3 verify_gap.py` with Python 3, NumPy and SciPy available. The observed normalized gaps at \(\varepsilon=0.02,0.01,0.005,0.002\) are approximately \(0.9627865,0.9685631,0.9714288,0.9731406\), tending towards \(9\sqrt3/16\approx0.9742786\). These computations are finite corroboration; the claims for every positive semiaxis ratio and the exact coefficient follow from the proof above.

## Relationship to prior work

Hoehner [1] establishes asymptotic rigidity for simultaneous approximation of intrinsic volumes by many-vertex polytopes (both versions were examined). The fixed-three-vertex loss and its sharp small-eccentricity coefficient do not follow from an asymptotic statement as the vertex count tends to infinity. In the planar setting, area and perimeter are the two nonconstant intrinsic volumes of a triangle.

The public work *Exact perimeter selection among maximum-area polygons inscribed in ellipses* [2] classifies **which orientation of an already area-maximizing inscribed polygon has greatest perimeter**. Its full text explicitly excludes comparison with the unrestricted perimeter maximum among *all* inscribed polygons. This is the distinction measured by \(G\). Nandakumar's question [3] and Israel's answer identify the billiard/reflection stationarity condition for unrestricted maximum perimeter but give neither a uniform gap from the area-maximizing family nor a sharp quadratic near-circular gap coefficient. Classical circle maximum-area and affine invariance establish the area-maximizer family, not the new quantitative comparison.

## Limitations

The lower bound is intentionally nonoptimal outside the near-circular regime. No closed formula for \(P_\star(a,b)\), no exact characterization of all perimeter maximizers for a general ellipse, and no higher-dimensional or higher-vertex analogue are claimed. The literature comparison does not rule out an earlier equivalent local asymptotic in billiard or elliptic-integral research; independent verification has not been performed.

## References

[1] S. Hoehner, *One polytope fits all: Characterization of the Euclidean ball via simultaneous intrinsic volume approximation*, arXiv:2602.18547v1, first public 2026-02-20; revised as *Simultaneous random polytope approximation characterizes the Euclidean ball*, arXiv:2602.18547v2, 2026-10-13. https://arxiv.org/abs/2602.18547

[2] *Exact perimeter selection among maximum-area polygons inscribed in ellipses*, public research record dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-perimeter-selection-among-maximum-area-polygons-inscribed--9338777854e9

[3] R. Nandakumar, *Inscribed n-gons of maximum perimeter for an ellipse*, MathOverflow, 2021-10-27; answer by R. Israel, 2021-10-27. https://mathoverflow.net/questions/407192/inscribed-n-gons-of-maximum-perimeter-for-an-ellipse
