# Exact intrinsic vertex-distance distribution on the regular octahedron

## Finding

Give the surface of the unit-edge regular Euclidean octahedron its intrinsic shortest-path metric, fix any vertex \(v\), and sample \(X\) uniformly from the entire surface by area. Write \(R=d(v,X)\). Then \(0\le R\le\sqrt3\) and its **exact** cumulative distribution is

\[
F_R(r)=\Pr(R\le r)=
\begin{cases}
0,&r<0,\\[3pt]
\dfrac{\pi r^2}{3\sqrt3},&0\le r\le1,\\[8pt]
1-t(r)+\dfrac{2r^2}{\sqrt3}\arccos\!\left(\dfrac{s(r)}r\right),&1<r<\sqrt3,\\[8pt]
1,&r\ge\sqrt3,
\end{cases}
\]
where
\[
t(r)=\frac{3-\sqrt{4r^2-3}}2,\qquad
s(r)=\sqrt3\left(1-\frac{t(r)}2\right).
\]

The distribution is continuously differentiable at \(r=1\), but its second derivative has a **downward jump of exactly \(4\)**:
\[
F_R''(1^-)=\frac{2\pi}{3\sqrt3},\qquad
F_R''(1^+)=\frac{2\pi}{3\sqrt3}-4.
\]
The squared-distance moment and extreme tail are
\[
\mathbb E[R^2]=\frac{11}{12},\qquad
\Pr(R>\sqrt3-\varepsilon)=\frac23\varepsilon^2+O(\varepsilon^3)
\quad(\varepsilon\downarrow0).
\]
For an octahedron of edge length \(a>0\), replace \(R\) by \(d(v,X)/a\); in particular \(\mathbb E[d(v,X)^2]=11a^2/12\). This is a fixed-vertex **intrinsic** distance law, not a Euclidean chord law and not the distance distribution of two independently sampled surface points.

## Assumptions and scope

The object is the whole boundary of a convex regular octahedron, with eight Euclidean equilateral faces of edge length one. The metric is the infimum of lengths of surface curves. The probability measure is normalized two-dimensional Hausdorff area; the total area is \(8(\sqrt3/4)=2\sqrt3\). The choice of vertex is immaterial by symmetry. All formulas apply to every real threshold \(r\), including junctions and endpoints. No distribution of distances from generic source points or between two random points is asserted.

## Proof

**1. Exact facewise distance.** Denote the chosen vertex by \(N\), its opposite vertex by \(S\), and the four cyclic equatorial vertices by \(E_i\) (indices modulo four). The eight equilateral faces are \(T_i=NE_iE_{i+1}\) and \(B_i=SE_iE_{i+1}\). Develop each joined pair \(T_i\cup B_i\) across its equatorial edge into the Euclidean rhombus with opposite corners \(N_i'\) and \(S\). Choose planar coordinates on \(B_i\) so that
\[
S=(0,0),\quad E_i=(\sqrt3/2,1/2),\quad
E_{i+1}=(\sqrt3/2,-1/2),\quad N_i'=(\sqrt3,0).
\]
Set \(f(p)=|p-N|\) in the planar copy of each top face, and \(f(p)=|p-N_i'|\) in the planar copy of each bottom face. Across a top--bottom equatorial edge the two points used for the norm are reflected across that edge; across two adjacent bottom faces the reflected source images are reflected across their shared \(SE_i\) edge. Thus the formulas agree along every shared edge; they plainly agree across top--top edges too. Hence \(f\) is continuous on the whole surface. On each flat face it is Euclidean \(1\)-Lipschitz. Subdividing rectifiable paths at face transitions (or using local Lipschitz charts) shows that \(|f(p)-f(q)|\le d(p,q)\) globally. Because \(f(N)=0\), \(f(p)\le d(N,p)\).

Conversely, if \(p\in T_i\), its straight planar segment to \(N\) lies on that face and has length \(f(p)\). If \(p\in B_i\), the straight segment joining \(N_i'\) to \(p\) lies in the convex rhombus \(T_i\cup B_i\), so it folds to a surface path of length \(f(p)\). Consequently **\(d(N,p)=f(p)\) on every face**, including all edges and vertices. In particular \(d(N,S)=\sqrt3\), and \(S\) is the unique most distant point.

**2. Circular sectors up to unit distance.** Each developed rhombus has an angle \(\pi/3\) at \(N_i'\). Its remote boundary consists of \(SE_i\) and \(SE_{i+1}\), both at minimum distance \(1\) from \(N_i'\), attained at the equatorial endpoints. Thus for \(0\le r\le1\), the radius-\(r\) disk about \(N_i'\) intersects this rhombus in a complete sector of angle \(\pi/3\) and area \(\pi r^2/6\). The four rhombi partition the surface (up to measure-zero edges), so the total intrinsic-ball area is \(4\pi r^2/6=2\pi r^2/3\). Dividing by \(2\sqrt3\) proves the quadratic first branch. In particular, the wavefront crosses the equatorial edges already at distance \(\sqrt3/2\), yet the ball-area law has no transition there.

**3. The last branch.** For \(1<r<\sqrt3\), each whole top face lies inside the intrinsic ball, and the complement is four congruent curvilinear regions near \(S\), one in each bottom face. In the displayed bottom-face coordinates, \(d(N,p)=|p-(\sqrt3,0)|\). The circle centered at \((\sqrt3,0)\) of radius \(r\) meets each side \(SE_i\) at distance \(t\) from \(S\). The quadratic \(t^2-3t+3-r^2=0\) gives its relevant root \(t=(3-\sqrt{4r^2-3})/2\), with \(0<t<1\). The two contact points form a chord of length \(t\) a perpendicular distance \(s=\sqrt3(1-t/2)\) from the circle center. The area outside the disk but inside the bottom triangle is the area of the equilateral triangle of side \(t\) less the disk segment cut off toward \(S\):
\[
A_{\mathrm{out}}(r)=\frac{\sqrt3}{4}t^2-
\left[r^2\arccos(s/r)-\frac{st}{2}\right]
=\frac{\sqrt3}{2}t-r^2\arccos(s/r).
\]
The whole-surface area outside the ball is \(4A_{\mathrm{out}}\); division by \(2\sqrt3\) gives the asserted upper branch and its continuous endpoint value \(F_R(\sqrt3)=1\).

**4. Second moment and regularity.** Uniform barycentric coordinates \((u,v,1-u-v)\) in an equilateral triangle satisfy \(\mathbb E[u]=\mathbb E[v]=1/3\), \(\mathbb E[u^2]=\mathbb E[v^2]=1/6\), and \(\mathbb E[uv]=1/12\). Applied to the facewise squared Euclidean norm from \(N\), a top face contributes mean \(5/12\). On a bottom face the unfolded source is \((\sqrt3,0)\), giving mean \(17/12\). Four faces of each kind, all equal in area, yield \(\mathbb E[R^2]=(5/12+17/12)/2=11/12\). Direct differentiation of the two elementary CDF branches at \(r=1\) gives the stated one-sided derivatives; the first derivatives agree and the second differ by exactly \(4\).

**5. Sharp upper tail.** Near \(S\), write a point in each bottom face in polar coordinates \((\rho,\theta)\), with \(|\theta|\le\pi/6\) and \(\rho\downarrow0\). Here \(d(N,p)^2=3+\rho^2-2\sqrt3\rho\cos\theta\). For \(r=\sqrt3-\varepsilon\), the region with distance exceeding \(r\) has \(0\le\rho<\varepsilon/\cos\theta+O(\varepsilon^2)\), uniformly in \(\theta\). Its area per bottom face is therefore
\[
\frac12\varepsilon^2\int_{-\pi/6}^{\pi/6}\sec^2\theta\,d\theta
+O(\varepsilon^3)
=\frac{\varepsilon^2}{\sqrt3}+O(\varepsilon^3).
\]
There are four bottom faces; normalizing by \(2\sqrt3\) yields \((2/3)\varepsilon^2+O(\varepsilon^3)\).

## Verification

Run `python3 verify_octahedron.py` with standard Python 3. The source is a complete standalone artifact. Its exact rational arithmetic develops every simple adjacent-face sequence from a specified bottom face back to a top source face: 65 sequences give 13 distinct source images in the triangular lattice. For each of those images, the squared-distance difference from the direct rhombus image is affine in the target point and is checked **exactly** at all three target-triangle vertices. This independently supports the facewise nearest-image lemma without using floating point.

The same script performs deterministic triangle-grid checks of the squared moment, 300,000 seeded uniform-face Monte Carlo trials comparing ten CDF thresholds and the moment, and three terminal-tail checks. All assertions passed in the recorded run. This is reproducibility evidence, not an exhaustive numerical proof of a continuum claim; the proof above establishes the continuum assertions analytically.

## Relationship to prior work

Ciccariello (arXiv:1401.7950, first posted January 30, 2014) derives the **ambient Euclidean random-chord** distribution of the regular octahedron by integrating across face pairs. Its distance is a straight-line chord through or on the solid, and it is not a fixed-vertex shortest-surface-path law. Examination of its accessible complete preprint text confirms this difference in its definitions, domain of integration, and conclusions.

Schwartz (arXiv:2004.11852, first posted April 24, 2020) concerns the **farthest-point map** for the intrinsic octahedral metric. The map identifies extremizers of pointwise distance, whereas the finding here computes the area of **all distance sublevel sets from a vertex**. Its abstract and publication description were checked; the full text was unavailable during this review, so no whole-document noncoverage claim is made. Earlier works on polyhedral shortest paths also provide general development techniques but do not by themselves evaluate this particular exact area distribution. No assertion is made that a database search proves historical uniqueness.

## Limitations

This is not a general-source or two-random-points distribution. The polyhedron is exactly regular; the formulas do not extend without additional work to arbitrary octahedra. The sharp numerical claims follow from elementary development and area calculations; the supporting checks are finite. Historical-priority uncertainty remains, particularly because the full Schwartz text was not accessible and unindexed classical treatments of spherical polyhedral wavefronts may exist. No independent scientific audit or external verification has been performed.

## References

1. S. Ciccariello, *The chord-length probability density of the regular octahedron*, arXiv:1401.7950 (initial public preprint January 30, 2014); *Journal of Applied Crystallography* **47** (2014), 1216–1227, DOI:10.1107/S1600576714011121. This paper concerns ambient chords, not intrinsic geodesics.
2. R. E. Schwartz, *The Farthest Point Map on the Regular Octahedron*, arXiv:2004.11852 (initial public preprint April 24, 2020); *Experimental Mathematics* **31** (2022), 1086–1097, DOI:10.1080/10586458.2021.1894269. The accessible abstract concerns farthest-point dynamics, not a complete fixed-vertex distance law.
