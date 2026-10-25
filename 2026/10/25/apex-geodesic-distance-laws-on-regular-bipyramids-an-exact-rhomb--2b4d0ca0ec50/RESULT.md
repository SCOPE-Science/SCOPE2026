# Apex geodesic-distance laws on regular bipyramids: an exact rhombus reduction and a cusp transition

## Finding
Let \(n\ge3\), \(R>0\), \(h>0\). Let \(P_{n,R,h}\) be the boundary of the convex hull of the vertices of a regular planar \(n\)-gon of circumradius \(R\) in the plane \(z=0\), together with the two apexes \((0,0,\pm h)\). Equip its surface with intrinsic Euclidean length distance. Fix the north apex \(N\) and sample \(X\) uniformly with respect to surface area. Write
\[
a=\sqrt{R^2+h^2},\quad \alpha=2\arcsin\!\left(\frac{R\sin(\pi/n)}{a}\right),\quad b=\sin\alpha,\quad L=2\cos(\alpha/2).
\]
Then \(0<\alpha<2\pi/n\le2\pi/3\). Let \(D=d_{P_{n,R,h}}(N,X)\) and \(T=D/a\). For independent \(U,V\sim\operatorname{Uniform}(0,1)\),
\[
T^2\ \stackrel{d}{=}\ U^2+V^2+2\cos(\alpha)UV.\tag{1}
\]
In particular, the entire law depends on the number of equatorial vertices only through the face-apex angle \(\alpha\); it equals the Euclidean distance from a vertex to a uniform point in a planar rhombus with side length one and vertex angle \(\alpha\).

Here is its complete elementary cumulative distribution \(F_\alpha(t)=\Pr(T\le t)\). Set \(u(t)=\arcsin(b/t)\) whenever \(t\ge b\), and define
\[
C_\alpha(t)=\frac{\alpha t^2}{2b},\qquad
M_\alpha(t)=\frac{t^2(\alpha/2-\pi+2u(t))+2b^2\cot u(t)}{b},
\]
\[
O_\alpha(t)=b\bigl(\cot u(t)-\cot\alpha\bigr)+\frac{t^2}{b}\bigl(u(t)-\alpha/2\bigr).
\]
For \(\alpha\le\pi/2\),
\[
F_\alpha(t)=\begin{cases}0&t<0,\\C_\alpha(t)&0\le t\le1,\\O_\alpha(t)&1<t<L,\\1&t\ge L.\end{cases}\tag{2}
\]
For \(\pi/2<\alpha<2\pi/3\),
\[
F_\alpha(t)=\begin{cases}0&t<0,\\C_\alpha(t)&0\le t\le b,\\M_\alpha(t)&b<t\le1,\\O_\alpha(t)&1<t<L,\\1&t\ge L.\end{cases}\tag{3}
\]
The maximum possible apex distance is \(aL\), and
\[
\frac{\mathbb E D^2}{a^2}=\frac23+\frac12\cos\alpha,\qquad
\frac{\mathbb E D^4}{a^4}=\frac{28}{45}+\cos\alpha+\frac49\cos^2\alpha.\tag{4}
\]
For fixed \(a\), the distances are strictly stochastically decreasing as \(\alpha\) increases (at nontrivial comparison thresholds). Their distribution determines \(a\) and \(\alpha\) from its support endpoint and second moment, but in general does not determine \(n\).

A geometric change of onset exponent occurs when the planar face triangle passes through a right apex angle. Set \(B_\alpha(t)=C_\alpha(t)\), the unrestricted small-radius cone-area expression, and \(\Delta_\alpha(t)=B_\alpha(t)-F_\alpha(t)\). With \(t_0=1\) for \(\alpha\le\pi/2\), and \(t_0=\sin\alpha\) for \(\alpha>\pi/2\), the first nonzero discrepancy has the sharp one-sided asymptotic law
\[
\Delta_\alpha(t_0+\varepsilon)\sim
\begin{cases}
\varepsilon^2/\cos\alpha,&0<\alpha<\pi/2,\\
(4\sqrt2/3)\varepsilon^{3/2},&\alpha=\pi/2,\\
(8/3)\sqrt{2/\sin\alpha}\,\varepsilon^{3/2},&\pi/2<\alpha<2\pi/3.
\end{cases}\tag{5}
\]
An obtuse face-apex angle is possible only for \(n=3\); for a triangular bipyramid, \(\alpha=\pi/2\) exactly when \(h/R=1/\sqrt2\). Thus this tangency onset is a genuine, sharply located geometry-dependent transition absent for \(n\ge4\).

## Assumptions and scope
A regular bipyramid here means the symmetric convex union of two *congruent right pyramids* on a regular \(n\)-gon, with positive common apex height \(h\) and circumradius \(R\). Surface measure is the induced two-dimensional Hausdorff measure, normalized to total mass one. The source point is precisely one apex. Edge/vertex tie sets are null for the sampling law. All formulas require finite \(n\ge3\) and strictly positive \(R,h\); the degenerate limit \(h=0\) is not asserted. The planar rhombus is an auxiliary intrinsically developed object, not an isometric embedding of the whole polyhedral surface into one rhombus.

## Proof
**Exact intrinsic-distance reduction.** Each upper triangle has two equal lateral sides of length \(a\), equatorial base \(2R\sin(\pi/n)\), and apex angle \(\alpha\). The corresponding lower triangle glued across that equatorial base is congruent and reflects to a rhombus \(Q_j\) with four sides of length \(a\) and apex angle \(\alpha\). Develop each of the \(n\) pairs of triangles this way, always marking the developed image \(N_j\) of the north apex. Define \(f(x)\) as the planar Euclidean distance from \(N_j\) to the image of \(x\) in its associated rhombus. The two definitions agree on an equatorial edge because it was the unfolding hinge. They agree on an upper radial edge since both developments measure the same arclength from \(N\). They agree on a lower radial edge because the two developed source images are reflections across that radial edge (equivalently, both determine the same congruent three-vertex triangle with the two edge endpoints). Hence \(f\) is a well-defined continuous function on the surface.

Inside every triangular face, \(f\) is Euclidean distance from a fixed planar point and has Lipschitz constant one. Subdividing a rectifiable surface path at face crossings, and then approximating general paths, shows that \(|f(x)-f(y)|\le d_P(x,y)\) globally. As \(f(N)=0\), \(d_P(N,x)\ge f(x)\). Conversely, the straight segment from the developed \(N_j\) to the developed \(x\) stays inside the convex rhombus \(Q_j\), and its inverse development is a surface path of length \(f(x)\). Consequently \(d_P(N,x)=f(x)\) for all surface points, including the seams by continuity. The lower radial edges form the source cut-locus branches, while interior points of a rhombus have a unique radial minimizing path.

**Distribution.** Every \(Q_j\) has the same area and represents a pair of surface faces without changing area. Thus uniform surface sampling reduces to uniform area sampling in one rhombus. If its two unit edge directions from \(N_j\) are \(e_1,e_2\) with \(e_1\cdot e_2=\cos\alpha\), a uniform point is \(a(Ue_1+Ve_2)\) for independent uniform \(U,V\in[0,1]\). Squared length gives (1) and direct monomial integration gives (4).

**Complete CDF.** Polar angle \(\theta\in[0,\alpha]\) from the first rhombus side measures a radial boundary
\[
\rho(\theta)=\frac{a\sin\alpha}{\max\{\sin\theta,\sin(\alpha-\theta)\}}.
\]
Its symmetry gives exactly
\[
F_\alpha(t)=\frac{1}{\sin\alpha}\int_0^{\alpha/2}
\min\!\left\{t^2,\frac{\sin^2\alpha}{\sin^2(\alpha-\theta)}\right\}\,d\theta.\tag{6}
\]
If \(\alpha\le\pi/2\), the radial boundary is monotone on the half-angle and first meets the growing disk at \(t=1\). If \(\alpha>\pi/2\), it has an interior minimum \(b=\sin\alpha\) at \(\theta=\alpha-\pi/2\); then two angular roots occur until \(t=1\), when the left root reaches zero. Above \(t=1\), there is only one root. Solving \(\sin(\alpha-\theta)=b/t\), integrating \(\csc^2\) by the cotangent antiderivative, and inserting the corresponding angular intervals gives (2) and (3), including continuous matching at branch points. The farthest rhombus vertex is opposite the source, at length \(aL\), because \(\alpha<2\pi/3\) implies \(L>1\).

**Sharp onset.** The untruncated cone area is \(B_\alpha(t)=\alpha t^2/(2\sin\alpha)\). When \(\alpha<\pi/2\), the radial boundary near the first contacting angle satisfies \(\rho(\theta)/a=1+\cot\alpha\,\theta+O(\theta^2)\), yielding \(\Delta\sim\varepsilon^2/\cos\alpha\) after integrating the linear wedge deficit. At \(\alpha=\pi/2\), the contact is at an endpoint, with \(\rho(\theta)/a=1+\theta^2/2+O(\theta^4)\); its half-Gaussian-width integral yields \(4\sqrt2\varepsilon^{3/2}/3\). For \(\alpha>\pi/2\), the contact is at an interior angle and \(\rho(\theta)/a=b\sec(\theta-\theta_0)\). Both sides contribute, giving \((8/3)\sqrt{2/b}\,\varepsilon^{3/2}\). This proves (5).

**Ordering and reconstruction.** Under the same uniforms in (1), \(T_\alpha^2\) is strictly decreasing in \(\alpha\) whenever \(UV>0\), proving stochastic order. Given an unnormalized law, let \(d_{\max}\) be its support endpoint and \(m_2=\mathbb ED^2\). Put \(q=m_2/d_{\max}^2\). Since \(d_{\max}^2=2a^2(1+\cos\alpha)\),
\[
\cos\alpha=\frac{4-12q}{12q-3},\qquad a=\frac{d_{\max}}{2\cos(\alpha/2)}.
\]
The ratio \(q=(4+3\cos\alpha)/(12(1+\cos\alpha))\) is strictly decreasing in \(\cos\alpha\) on the admissible range, so reconstruction is unique. Given \(n\), subsequently \(R=a\sin(\alpha/2)/\sin(\pi/n)\) and \(h=\sqrt{a^2-R^2}\). Different permissible \(n\) may yield the same \(a,\alpha\) and therefore the same law.

## Verification
The companion `CHECK.py` independently evaluates the polar integral (6) by numerical quadrature with all relevant integration breakpoints and compares it to the closed forms (2)–(3) for acute, right and obtuse face-apex angles. It also independently samples the planar rhombus, checks both low even moments and the first-contact asymptotics, and tests branch matching and probability bounds. These checks corroborate finite numerical instances; the proof above establishes the quantifiers for all \(n,R,h\). The reproducibility program is not an infinite proof certificate.

## Relationship to prior work
Itoh, O'Rourke and Vîlcu (arXiv:0812.2257, first public 2008-12-12) treat star/source unfolding principles for arbitrary convex polyhedral surfaces; their scope is geometric unfolding, not this apex-specific distance distribution, stochastic identification or onset transition. Li and Qiu (2016, DOI 10.1155/2016/8371750) give general distance-to-vertex distributions within planar triangles and polygonal decompositions, which are powerful prerequisites for evaluating the rhombus law once the nonplanar intrinsic-distance reduction has been proved. They do not derive the regular-bipyramid source distance reduction or the phase transition in (5). O'Rourke and Vîlcu (arXiv:2312.01534) study skeletal cut loci in general; its accessible abstract is relevant but insufficient to exclude an equivalent special-case cut-locus characterization. The mathematical contribution claimed here is the uniform exact surface-geodesic law for the complete regular-bipyramid family, its special triangular-bipyramid contact transition, and the distributional inverse and shape-invariance statements, not general point-to-polygon distance integration or general polyhedral unfolding.

## Limitations
The law refers to uniform **surface area**, not volume or edge sampling, and to distances from an apex, not between two random surface points. It assumes a symmetric double right regular pyramid with congruent upper and lower faces and does not cover unequal apex heights. The derivation uses no numerical claim of exhaustive literature coverage. An overlooked explicit special case in classical source-unfolding or planar rhombus statistics remains possible. The general shortest-path and point-to-polygon methods are established prior results, acknowledged above. 

## References
1. Jin-ichi Itoh, Joseph O'Rourke, Costin Vîlcu, *Unfolding Convex Polyhedra via Quasigeodesic Star Unfoldings*, arXiv:0812.2257, first version 2008-12-12. https://arxiv.org/abs/0812.2257
2. Hongjun Li and Xing Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, Mathematical Problems in Engineering 2016, article 8371750; published 2016-12-08. https://doi.org/10.1155/2016/8371750
3. Joseph O'Rourke and Costin Vîlcu, *Skeletal Cut Loci on Convex Polyhedra*, arXiv:2312.01534, first version 2023-12-03. https://arxiv.org/abs/2312.01534
