# Complete central-section side-count law across the cube–octahedron interpolation

## Finding

Let
\[
K_t=[-1,1]^3\cap\{(x_1,x_2,x_3):|x_1|+|x_2|+|x_3|\le t\},\qquad 1\le t\le3.
\]
Choose an unoriented plane through the origin using the rotation-invariant probability distribution on the Grassmannian of planes in \(\mathbb R^3\), and denote by \(N_t\) the number of sides of its section of \(K_t\). Then the *entire law*, for every \(t\) in this closed interval, is given by the formulas below. Apart from the exceptional set of plane normals passing through polytope vertices, the section is a nondegenerate convex polygon and its sides and vertices have the same number.

For any nonzero vectors \(u,v,w\in\mathbb R^3\) in an open half-space, set
\[
\Omega(u,v,w)=2\arctan\left(
\frac{|\det(u,v,w)|}{
\|u\|\|v\|\|w\|+(u\cdot v)\|w\|+(u\cdot w)\|v\|+(v\cdot w)\|u\|}
\right).
\]
For the nondegenerate positive cones below, \(\Omega\) is their spherical solid angle in steradians. This provides elementary closed forms using arithmetic, square roots and inverse trigonometric functions.

**Octahedral side, \(1<t<2\).** Put \(s=t-1\), and define
\[
\begin{aligned}
M_-(s)&=\frac{24}{\pi}\arccos\!\frac1{1+s^2}
+\frac{12}{\pi}\arccos\!\frac{2s}{1+s^2},\\
q_-(s)&=\frac{12}{\pi}\Omega\big((1,0,0),(1,s,s^2),(1,s,s)\big).
\end{aligned}
\]
The only possible side counts are \(6,8,10\), and
\[
\boxed{\begin{aligned}
\Pr(N_t=6)&=4-M_-(s)/2+q_-(s),\\
\Pr(N_t=8)&=(M_-(s)-6)/2-2q_-(s),\\
\Pr(N_t=10)&=q_-(s).
\end{aligned}}
\]

**Cubic side, \(2<t<3\).** Put \(s=t-2\), and define
\[
\begin{aligned}
M_+(s)&=\frac{24}{\pi}\arccos\!\frac{1+2s}{2+s^2}
+\frac{12}{\pi}\arccos\!\frac{2-s^2}{2+s^2},\\
p_+(s)&=\frac6\pi\Omega\big((1,0,0),(1,s,0),(1,0,s)\big),\\
q_+(s)&=\frac{12}{\pi}\Omega\big((1,1,0),(1,1,1-s),
(1+s,1+s^2,1-s)\big).
\end{aligned}
\]
The only possible side counts are \(4,6,8,10\), and
\[
\boxed{\begin{aligned}
\Pr(N_t=4)&=p_+(s),\\
\Pr(N_t=6)&=4-M_+(s)/2-2p_+(s)+q_+(s),\\
\Pr(N_t=8)&=M_+(s)/2-3+p_+(s)-2q_+(s),\\
\Pr(N_t=10)&=q_+(s).
\end{aligned}}
\]
All the displayed possible counts have strictly positive probabilities for their respective open parameter intervals.

**Special parameters.** At \(t=1\), the regular octahedron has \(N_t=6\) almost surely. At \(t=2\), the cuboctahedron has \(N_t=8\) almost surely. At \(t=3\), the cube has
\[
\Pr(N_t=4)=\frac6\pi\arcsin\frac13,\qquad
\Pr(N_t=6)=1-\frac6\pi\arcsin\frac13.
\]
These endpoint laws are the continuous limits of the appropriate interior formulas.

**Rigidity and the sharp mean peak.** In the two open ranges, \(\mathbb E N_t=M_-(t-1)\) or \(M_+(t-2)\), respectively. The mean increases strictly from \(6\) to \(8\) on \([1,2]\), then decreases strictly from \(8\) to \(12\arccos(1/3)/\pi\) on \([2,3]\). Thus the cuboctahedron is the **unique maximum of mean section complexity** in the family and the **unique parameter with deterministic octagonal generic central sections**. Every other interior parameter admits a decagonal section on a nonempty open set of plane directions, despite the absence of decagons at the cuboctahedral parameter itself.

## Assumptions and scope

The positive parameter \(t\) is fixed before sampling. The normal is uniform on the unit sphere, modulo antipodal identification; there is no random plane offset. Normals for which some vertex of \(K_t\) lies on the plane form a finite union of great circles and have measure zero. All probability statements are consequently unaffected by conventions on these nongeneric normals. The dimension is three, the cube and octahedron are coaxial, and their relative scale is exactly the one in the displayed definition. Symmetry permits ordering the absolute normal coordinates as \(a>b>c>0\) during the proof; this is a reduction, not a restriction on the sampling measure.

## Proof

**1. Combinatorial descriptions.** For \(1<t<2\) write \(s=t-1\). The vertices of \(K_t\) are the \(24\) distinct signed permutations of \((1,s,0)\). There are \(24\) edges lying in coordinate cube facets, joining pairs such as \((1,s,0)\) and \((1,0,s)\), and \(12\) edges shared by two octahedral facets, joining pairs such as \((1,s,0)\) and \((s,1,0)\). For \(2<t<3\) write \(s=t-2\). The vertices are the \(24\) signed permutations of \((1,1,s)\). There are \(24\) edges each shared by a cube facet and an octahedral facet, such as the segment between \((1,1,s)\) and \((1,s,1)\), and \(12\) shortened original cube edges, such as the segment between \((1,1,s)\) and \((1,1,-s)\). These lists follow directly by intersecting the active inequalities in the defining half-space system. At \(t=2\) the repeated vertex coordinates merge into the \(12\) vertices \((\pm1,\pm1,0)\) and their permutations, joined by \(24\) cuboctahedral edges. For \(t=1,3\) the bodies are the standard octahedron and cube.

For any convex polyhedron containing the origin strictly in its interior, a generic central plane crosses one edge at each section-polygon vertex. Each polyhedral edge \([u,v]\) contributes precisely when \((n\cdot u)(n\cdot v)<0\). Its Haar crossing probability is \(\arccos((u\cdot v)/(\|u\|\|v\|))/\pi\): the signs disagree on two spherical lunes whose combined area fraction is the angle divided by \(\pi\). This proves the mean identities \(M_-(s)\) and \(M_+(s)\) by the two edge-orbit counts from the preceding paragraph, *without* assuming independence of edge events.

**2. Exact ordered-normal count on the octahedral side.** Take \(a>b>c>0\) to be the sorted absolute coordinates of the plane normal, and \(0<s<1\). Each of the two cube facets orthogonal to the largest coordinate has no intersection with the plane. The facets orthogonal to the middle and smallest coordinates contribute four edge crossings per opposite pair precisely if \(b<sa\) and \(c<sa\), respectively. The twelve edges shared by two octahedral facets contribute two crossings for each of the three inequalities \(b>sa\), \(c>sa\), \(c>sb\). Adding the disjoint edge-orbit contributions gives
\[
N_t=6+2\mathbf1_{\{b<sa\}}+2\mathbf1_{\{c<sa\}}
-2\mathbf1_{\{c<sb\}}.
\]
The ordering implications \(b<sa\Rightarrow c<sa\) and \(c<sb\Rightarrow c<sa\) show that only \(6,8,10\) occur. In particular, \(N_t=10\) if and only if
\[
b<sa,\qquad sb<c<b,
\]
with the other ordering conditions automatic. This is a three-ray cone in the positive ordered chamber, with rays proportional to \((1,0,0)\), \((1,s,s^2)\), and \((1,s,s)\). Its spherical area is \(\Omega\) of these rays. There are \(3!2^3=48\) congruent ordered signed chambers, so its total spherical probability is \(48\Omega/(4\pi)=12\Omega/\pi=q_-(s)\). With support \(\{6,8,10\}\), probability normalization and the already computed mean \(M_-(s)\) uniquely determine the other two probabilities as displayed.

**3. Exact ordered-normal count on the cubic side.** Write again \(a>b>c>0\) and \(0<s<1\). Each cube facet of \(K_t\) is an octagon. The normal plane intersects each of the opposite facets orthogonal to the two smaller normal coordinates, and it also intersects the opposite pair orthogonal to the largest one exactly when \(a<b+sc\). Counting two boundary edge intersections per intersected cube facet produces \(8+4I\), where \(I=\mathbf1_{\{a-b<sc\}}\); this counts an edge shared by two cube facets twice. Among the twelve such cube–cube edges, the exact number crossed is \(2(I+J+L+K)\), with
\[
J=\mathbf1_{\{a-c<sb\}},\qquad
L=\mathbf1_{\{b-c<sa\}},\qquad
K=\mathbf1_{\{b+c<sa\}}.
\]
Indeed, on an original cube edge parallel to a coordinate axis the normal dot product varies over an interval of radius \(s\) times that axis's normal-coordinate magnitude; crossing depends on whether the absolute signed sum of the other two coordinates is smaller than that radius. We subtract these double counts and obtain
\[
N_t=8+2I-2J-2L-2K.
\]
The ordering gives \(J\Rightarrow I\), \(J\Rightarrow L\), \(K\Rightarrow L\) and \(K\Rightarrow \neg I\). Thus precisely \(4,6,8,10\) are possible. The event \(N_t=4\) is exactly \(b+c<sa\); after combining the two orders of the smaller coordinates, its positive-octant cone has rays \((1,0,0),(1,s,0),(1,0,s)\). There are three choices of largest axis and eight sign choices, hence probability \(24\Omega/(4\pi)=6\Omega/\pi=p_+(s)\).

The decagon event \(N_t=10\) is exactly
\[
a-b<sc,\qquad b-c>sa,
\]
with \(a>b>c>0\). To see why, the second inequality forces \(J=K=0\); the first yields \(I=1\), and \(L=0\). Conversely, these are the only indicator values producing ten. On the slice \(a=1\) the domain is the triangle bounded by \(b=1\), \(b=1-sc\), and \(b=s+c\), with vertices
\[
(b,c)=(1,0),\quad (1,1-s),\quad
\left(\frac{1+s^2}{1+s},\frac{1-s}{1+s}\right).
\]
The corresponding three cone rays are precisely those used in \(q_+(s)\). The \(48\) symmetry chambers give probability \(12\Omega/\pi=q_+(s)\). The known \(p_+(s)\), \(q_+(s)\), total mass one, and mean \(M_+(s)\) determine the two remaining probabilities in the statement.

**4. Positive support and endpoints.** All the solid-angle cones above have positive area for \(0<s<1\); hence the decagon cells occur on both sides and the four-sided cell on the cubic side is nonempty. Six- and eight-sided cells on both sides are likewise open: for the six-sided cell one can choose the three sorted coordinates sufficiently close to one another (octahedral side), and on the cubic side the same choice makes \(I=J=L=1\). For an octagonal cell, the octahedral side permits \(a=1,b=s/2,c=s^2/4\); on the cubic side choose \(a=1,b=(1+s)/2,c=(1-s)/4\), which makes all \(I,J,L,K\) vanish. (Small strict perturbations avoid accidental equalities.) Direct limiting evaluation of the cone angles gives the stated endpoint laws. At \(t=2\), a square face perpendicular to a coordinate axis is intersected exactly when that coordinate is not the largest in absolute normal magnitude. Thus exactly four square faces, each in two opposite pairs, contribute two crossing edges each, yielding \(N_2=8\) for every generic normal. For the octahedron \(N_1=6\) generically; for the cube, the criterion \(a<b+c\) gives the familiar four-/six-sided split. The last cubic solid angle at \(s=1\) is \(6\arcsin(1/3)/\pi\).

**5. Sharp unique maximum.** Direct differentiation yields
\[
M_-'(s)=\frac{24}{\pi(1+s^2)}
\left(\frac{2}{\sqrt{2+s^2}}-1\right)>0
\qquad (0<s<1),
\]
while
\[
M_+'(s)=\frac{24}{\pi(2+s^2)}
\left(\sqrt2-\frac{2(s+2)}{\sqrt{s^2+2s+3}}\right)<0
\qquad (0<s<1).
\]
The second inequality follows from \(2(s+2)^2>s^2+2s+3\). The first follows from \(2+s^2<4\). Both one-sided functions take value \(8\) at the cuboctahedron, so \(t=2\) uniquely maximizes \(\mathbb E N_t\). Since only that parameter makes its section law deterministic at eight, its octagonal rigidity is likewise unique.

## Verification

The standalone `verify_sections.py` enumerates the exact half-space vertices and edges using rational arithmetic, compares direct edge-crossing counts with the derived ordered-chamber formulas at six rational parameters, and independently tests the Haar distribution formulas by Gaussian-normal sampling on both sides of the transition. It also checks mean normalization, endpoint limits and strict mean trends on finite grids. Run `python verify_sections.py` with Python 3. The proof above, not a finite computation or sample, establishes the continuum parameter statement. The calculations are not an independent audit.

## Relationship to prior work

Kabluchko and Seidel (2020) establish a general face-count framework for random central sections of regular polytopes. Its edge-count observation supplies one component of the first-moment method, but it neither gives this one-parameter family nor its joint phase-dependent polygon distributions. Berlow, Brandenburg, Meroni and Shankar (2021) give general chamber descriptions of polytope intersection bodies. Brandenburg, De Loera and Meroni (2023) provide combinatorial slicing chambers and optimization methods; their computed examples concern other polytopes and deterministic optimization, not the present exact Haar probabilities.

A previously available exact law for the regular truncated octahedron agrees with the special parameter \(t=3/2\); an earlier sharp cuboctahedral cusp analysis describes only the first-order behavior as \(t\to2\). Both results are credited as prior. The present result extends those isolated and local cases to an exact closed-form distribution at **every** parameter \(1\le t\le3\), including four-sided and decagonal probabilities, with no numerical integration. This is not a novelty claim for the general chamber concept, the regular truncated-octahedron special case, or the leading cusp coefficients. The possibility of an older unlocated equivalent global law remains a priority limitation.

## Limitations

The distribution is for strictly central Haar planes and the specified coaxial cube–octahedron family, not affine-offset sections or arbitrarily oriented/weighted bodies. The formulas are almost-sure statements because boundary directions have Haar probability zero. They give the polygon's number of sides, not its perimeter, area, or full combinatorial embedding. The mean formula uses a standard edge-crossing principle, so it is not asserted as a new general theorem. Historical priority is conditional on the inspected literature and available public records; independent audit has not been performed.

## References

1. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492, first publicly submitted 2020-06-16, https://arxiv.org/abs/2006.09492 (especially Section 4 and Proposition 4.1).
2. K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, first publicly submitted 2021-10-12, https://arxiv.org/abs/2110.05996 (especially Section 2 and the cube example).
3. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first publicly submitted 2023-04-27, https://arxiv.org/abs/2304.14239 (especially Theorem 1.1 and Sections 2, 5).
4. Earlier mathematical reports: *The exact Haar section-type law of the truncated octahedron* (the parameter \(t=3/2\)) and *Sharp asymmetric octagon-law cusp at the cuboctahedral transition* (the local limit \(t\to2\)). Their individual claims are not counted as new here.
