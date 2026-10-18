# Sharp brightness extrema and exact moments of the regular truncated octahedron

## Finding

Let \(P\subset\mathbb R^3\) be the regular truncated octahedron with unit edge length and let \(U\) be uniformly distributed on the unit sphere. Denote by \(B(u)\) the area of the orthogonal projection of \(P\) onto the plane \(u^\perp\). Then the exact range and all equality directions are

\[
4\sqrt2\le B(u)\le\sqrt{51}.
\]

Equality on the left holds **exactly** at the twelve signed permutations of \((1,1,0)/\sqrt2\), and equality on the right **exactly** at the twenty-four signed permutations of \((7,1,1)/\sqrt{51}\). The exact first two moments are

\[
\mathbb E B(U)=\frac32+3\sqrt3,
\]

\[
\mathbb E B(U)^2=10+\frac{4+60\sqrt2+18\arcsin(1/3)+24\arcsin(1/\sqrt3)}{\pi}.
\]

Consequently,

\[
\operatorname{Var}(B(U))=10+\frac{4+60\sqrt2+18\arcsin(1/3)+24\arcsin(1/\sqrt3)}{\pi} - \left(\frac32+3\sqrt3\right)^2
=0.0933124491448\ldots.
\]

There is also a complete **two-chamber directional area law**. Sort the absolute coordinates of any unit normal into \(a\ge b\ge c\ge0\). Then

\[
B(u)=\begin{cases}
4(a+b+c),&a\le b+c,\\
7a+b+c,&a\ge b+c.
\end{cases}
\]

At the common boundary the two expressions agree. This simple piecewise-linear law explains both the asymmetric maximizing directions and the exact area moments.

## Assumptions and scope

Use the explicit unit-edge realization

\[
P=\frac1{\sqrt2}\operatorname{conv}\{\text{all coordinate permutations of }(0,\pm1,\pm2)\}.
\]

Its twenty-four vertices have thirty-six edges of length one, six square faces of area one, and eight regular hexagonal faces of area \(3\sqrt3/2\). The conclusions quantify over **every** unit normal \(u\in S^2\); orientations differing by a sign describe the same unoriented projection plane. Expectations use normalized spherical area measure \(d\omega/(4\pi)\), with no size or orientation selection bias.

## Proof

**1. Cauchy's projection-area identity and the two chambers.** For a convex polyhedron with facet areas \(A_F\) and outward unit normals \(n_F\), Cauchy's projection formula says

\[
B(u)=\frac12\sum_F A_F\,|n_F\cdot u|.
\]

The opposite square-face normals are the three coordinate axes. The opposite regular-hexagon-face normals are the four unoriented body diagonals, represented by \((1,1,1)/\sqrt3\), \((1,1,-1)/\sqrt3\), \((1,-1,1)/\sqrt3\), and \((-1,1,1)/\sqrt3\). Opposite facets give one absolute-value term per axis. Writing the four unnormalized diagonals as \(d_j\), the area is therefore

\[
B(u)=|u_1|+|u_2|+|u_3|+\frac32\sum_{j=1}^4|d_j\cdot u|.
\]

Signed permutation symmetry permits \((u_1,u_2,u_3)=(a,b,c)\) with \(a\ge b\ge c\ge0\). Of the four forms, only \(-a+b+c\) can be negative. Their absolute-value sum is \(2(a+b+c)\) when \(a\le b+c\), and \(4a\) when \(a\ge b+c\). This proves the asserted two-chamber law, including continuity at the boundary.

**2. Exact minimum, maximum, and equality.** Within the first chamber, every ordered triple decomposes as

\[
(a,b,c)=(b-c)(1,1,0)+(b+c-a)(1,1,1)+(a-b)(2,1,1),
\]

with all three coefficients nonnegative. The respective values of \(4(a+b+c)/\sqrt{a^2+b^2+c^2}\) on these three rays are \(4\sqrt2\), \(4\sqrt3\), and \(16/\sqrt6\). Since the numerator is linear and Euclidean norm is subadditive, the ratio on a positive cone is at least the smallest ray ratio. Equality requires precisely the first ray. In the second chamber, similarly,

\[
(a,b,c)=(a-b-c)(1,0,0)+(b-c)(1,1,0)+c(2,1,1).
\]

The ratios for \(7a+b+c\) on these rays are \(7\), \(4\sqrt2\), and \(16/\sqrt6\). The common sharp minimum is therefore \(4\sqrt2\), with only the sorted direction \((1,1,0)/\sqrt2\) attaining it.

For the maximum, Cauchy–Schwarz gives \(B(u)\le4\sqrt3\) in the first chamber and \(B(u)\le\sqrt{7^2+1^2+1^2}=\sqrt{51}\) in the second. The larger bound is attained precisely at \((7,1,1)/\sqrt{51}\), which belongs strictly to the second chamber. Restoring signed permutations yields exactly the claimed equality directions.

**3. An exact spherical absolute-product kernel.** For any unit vectors \(v,w\) with \(r=|v\cdot w|\), and Haar-uniform \(U\in S^2\),

\[
K(r):=\mathbb E\{|v\cdot U|\,|w\cdot U|\}=
\frac{2}{3\pi}\bigl(\sqrt{1-r^2}+r\arcsin r\bigr).
\]

To derive this, let \(G\) be a standard three-dimensional Gaussian. Its direction \(U=G/\|G\|\) is uniform and independent of its radius, and \(\mathbb E\|G\|^2=3\). An orthogonal change of basis makes the first two scalar products \(X\) and \(rX+\sqrt{1-r^2}Y\), with independent standard Gaussians \(X,Y\). Two-dimensional polar integration gives

\[
\mathbb E|X|\,|rX+\sqrt{1-r^2}Y|=\frac{2}{\pi}\bigl(\sqrt{1-r^2}+r\arcsin r\bigr).
\]

Dividing by three proves the kernel. Also, \(\mathbb E|v\cdot U|=1/2\) for every unit \(v\).

**4. Expansion of the moments.** The brightness formula is a sum of seven unoriented unit-normal absolute projections. Three coordinate axes have weight one, and four body diagonals have weight \(h=3\sqrt3/2\). There are exactly three coordinate-axis pairs with \(r=0\), six body-diagonal pairs with \(r=1/3\), and twelve mixed pairs with \(r=1/\sqrt3\). Therefore

\[
\mathbb E B(U)=\frac12(3+4h)=\frac32+3\sqrt3
\]

and

\[
\begin{aligned}
\mathbb E B(U)^2
&=\frac{3+4h^2}{3}+6K(0)+12h^2K(1/3)+24hK(1/\sqrt3)\\
&=10+\frac{4+60\sqrt2+18\arcsin(1/3)+24\arcsin(1/\sqrt3)}{\pi}.
\end{aligned}
\]

Subtracting the square of the mean yields the stated variance. Every use of a probabilistic expectation is an exact spherical integral; no finite-sample approximation enters the proof.

## Verification

The accompanying standalone file `check_brightness.py` constructs all twenty-four vertices directly; counts the thirty-six unit edges and the six square/eight hexagonal faces; compares the full facet-normal and two-chamber formulas at 1,500 independent deterministic pseudorandom directions; checks six projected convex-hull areas from the vertices; independently reconstructs all three angle-pair multiplicities and the kernel expansion; checks the six extremal cone rays; and performs a separate equal-area spherical midpoint quadrature with 259,200 nodes. Run with `python3 check_brightness.py` (Python standard library only). Its success marker is `TRUNCATED_OCTAHEDRON_BRIGHTNESS_OK`. The general inequalities and moment formulas are proved above; numerical quadrature is corroborating evidence only.

## Relationship to prior work

Finch's 2012 work on planar projections develops area and perimeter moments for regular simplices and cubes, and motivates further exact shadow statistics. Lángi's 2021 work identifies the regular truncated octahedron as a mean-width extremizer among equal-volume three-dimensional parallelohedra, but concerns mean width rather than this orientation-specific projected-area range and second moment. The established Cauchy projection formula and spherical absolute-product kernel provide general machinery; their explicit application alone does not supply the two-chamber extremizer classification without analyzing the sign geometry of this solid.

The 2026 preprint *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* is particularly relevant: its accessible abstract mentions the **directional width** law of the regular truncated octahedron and a **tetrahedral** brightness law. Its complete text was not available for comparison here, so any possible overlap in the projected-area statistic remains a priority risk, and priority is not claimed definitively.

## Limitations

The theorem is for the exactly regular, unit-edge truncated octahedron and Haar-uniform orientations. Scaling the solid by \(s>0\) multiplies projected areas by \(s^2\), means by \(s^2\), and variances by \(s^4\). The theorem does not provide the full cumulative distribution, finite-sample inference bounds, or an extremum over *all* parallelohedra. Its originality assessment is provisional in light of the inaccessible full 2026 preprint and older general projected-area literature. No independent mathematical validation has been performed.

## References

1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public 2011-10-04.
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464, first public 2012-03-12; particularly Sections 1–3 and 5.
3. Z. Lángi, *An isoperimetric problem for three-dimensional parallelohedra*, arXiv:2102.11621, first public 2021-02-23, especially Sections 1–2.
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (accessible abstract only; full-text comparison outstanding).
5. E. W. Weisstein, *Truncated Octahedron*, MathWorld (standard face structure and dimensions; not an originality authority).
