# The regular 24-cell has exactly 24 least-bright and 192 most-bright projection directions

## Finding

Let the standard regular four-dimensional 24-cell be
\[
C_{24}=\operatorname{conv}\left(\{\pm e_i:1\le i\le4\}\cup
\left\{\tfrac12(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4):\varepsilon_i\in\{-1,1\}\right\}\right)\subset\mathbb R^4.
\]
For every unit vector \(u\in S^3\), its **brightness** is the three-dimensional Euclidean volume of its orthogonal hyperplane shadow,
\[
b(u)=\operatorname{vol}_3(C_{24}\mid u^\perp).
\]
If the absolute coordinate values of \(u\), arranged in nonincreasing order, are \(a_1\ge a_2\ge a_3\ge a_4\ge0\), then
\[
\boxed{b(u)=\frac13\sum_{i<j}\bigl(|u_i+u_j|+|u_i-u_j|\bigr)=\frac23(3a_1+2a_2+a_3).}
\]
Its sharp complete directional range is
\[
\boxed{2\le b(u)\le\frac{2\sqrt{14}}3.}
\]
The minimum \(2\) holds at exactly **24 unit directions**, which are precisely the vertices of \(C_{24}\):
\[
\boxed{\{\pm e_i:1\le i\le4\}\cup\left\{\tfrac12(\varepsilon_1,\ldots,\varepsilon_4):\varepsilon_i\in\{-1,1\}\right\}.}
\]
The maximum \(2\sqrt{14}/3\) holds at exactly **192 unit directions**, the distinct signed coordinate permutations of
\[
\boxed{\frac{(3,2,1,0)}{\sqrt{14}}.}
\]
Thus the sharp brightness anisotropy ratio is
\[
\boxed{\frac{\max b}{\min b}=\frac{\sqrt{14}}3.}
\]

## Assumptions and scope

The 24-cell has the explicitly stated vertex normalization: every vertex is on \(S^3\), its four-dimensional volume is \(2\), and its 24 three-dimensional facets have volume \(\sqrt2/3\). Projection means **orthogonal** projection onto the hyperplane \(u^\perp\), with ordinary three-dimensional Euclidean volume; no central section is involved. Both \(u\) and \(-u\) are counted separately as unit directions, although they define the same unoriented hyperplane. Accordingly, there are 12 least-bright and 96 most-bright unoriented hyperplanes.

The conclusions are exact for the standard regular 24-cell and hence rescale with the third power under similarities. They are not asserted for general affine images or arbitrary four-dimensional parallelohedra.

## Proof

The convex body has the halfspace description
\[
C_{24}=\{x\in\mathbb R^4:|x_i|+|x_j|\le1\text{ for }1\le i<j\le4\}.
\]
Indeed, this is the \(D_4\) lattice Voronoi realization recorded in the primary geometric source. For each pair \(i<j\), its four facets have outward unit normals
\[
\frac{\varepsilon e_i+\eta e_j}{\sqrt2},\qquad\varepsilon,\eta\in\{-1,1\},
\]
and each facet is a regular octahedron of three-volume \(\sqrt2/3\).

By the Cauchy projection formula for four-dimensional polytopes, the three-volume of the orthogonal projection onto \(u^\perp\) is
\[
b(u)=\frac12\sum_{F\text{ facet}}\operatorname{vol}_3(F)|\langle u,\nu_F\rangle|.
\]
Substitution of the 24 normals and the common facet volume gives
\[
\begin{aligned}
b(u)&=\frac16\sum_{i<j}\sum_{\varepsilon,\eta\in\{-1,1\}}|\varepsilon u_i+\eta u_j|\\
&=\frac13\sum_{i<j}\bigl(|u_i+u_j|+|u_i-u_j|\bigr).
\end{aligned}
\]
Since
\[
|x+y|+|x-y|=2\max(|x|,|y|),
\]
we obtain
\[
b(u)=\frac23\sum_{i<j}\max(|u_i|,|u_j|)=\frac23(3a_1+2a_2+a_3).
\]

For the **maximum**, Cauchy–Schwarz gives
\[
3a_1+2a_2+a_3\le\sqrt{3^2+2^2+1^2}\sqrt{a_1^2+a_2^2+a_3^2+a_4^2}=\sqrt{14}.
\]
Equality holds exactly when
\[
(a_1,a_2,a_3,a_4)=\frac1{\sqrt{14}}(3,2,1,0).
\]
This is consistent with the coordinate order. The zero-coordinate location has four choices, the distinct positive magnitudes have six permutations, and their nonzero entries have eight sign choices, giving exactly \(4\cdot6\cdot8=192\) distinct oriented maximizers.

For the **minimum**, write each ordered nonnegative quadruple in the fundamental cone as
\[
a=t_1g_1+t_2g_2+t_3g_3+t_4g_4,\qquad t_j\ge0,
\]
where
\[
\begin{array}{ll}
g_1=(1,0,0,0),&g_2=(1,1,0,0),\\
g_3=(1,1,1,0),&g_4=(1,1,1,1).
\end{array}
\]
Here \(t_1=a_1-a_2\), \(t_2=a_2-a_3\), \(t_3=a_3-a_4\), and \(t_4=a_4\). For the linear functional \(L(a)=3a_1+2a_2+a_3\), direct calculation yields
\[
\left(\frac{L(g_j)}{\|g_j\|}\right)_{j=1}^4=\left(3,\frac5{\sqrt2},2\sqrt3,3\right).
\]
The two middle entries are strictly larger than \(3\). The triangle inequality now implies
\[
L(a)=\sum_{j=1}^4t_jL(g_j)\ge3\sum_{j=1}^4t_j\|g_j\|\ge3\left\|\sum_{j=1}^4t_jg_j\right\|=3\|a\|=3.
\]
Equality forces \(t_2=t_3=0\) in the first inequality; equality in the triangle inequality for the two remaining, nonparallel generators \(g_1,g_4\) requires \(t_1t_4=0\). Consequently, \(a\) must be proportional to \(g_1\) or \(g_4\). Unit normalization gives exactly
\[
a=(1,0,0,0)\quad\text{or}\quad a=(1/2,1/2,1/2,1/2).
\]
Their signed permutations consist of eight coordinate-axis unit vectors and sixteen half-sign unit vectors. Both families are exactly the 24 vertices of the original 24-cell.

The brightness function is continuous on the connected sphere \(S^3\), so its image is the entire interval between its attained extrema. Dividing the extreme values gives the claimed ratio.

## Verification

The accompanying standalone script `verify.py` performs exact rational arithmetic on the 24 vertex coordinates. It checks all 24 root-facet inequalities, identifies exactly six vertices per facet, recovers the regular-octahedral facet geometry, rederives the Cauchy coefficients, verifies all cone-generator inequalities, and counts the distinct extremizer directions. Its output is `VERIFY_OK`.

As a separate numerical cross-check, orthogonal projection of the explicit vertices followed by an independent three-dimensional convex-hull volume computation agreed to floating-point accuracy with the claimed brightness formula at a coordinate-axis direction, a half-sign direction, the claimed maximum, and a nonsymmetric generic direction. This finite check corroborates the normalization but does not substitute for the analytic proof of the range or equality cases.

## Relationship to prior work

The recent 24-cell isoperimetric theorem of Novaga and Song shows that the regular 24-cell uniquely minimizes surface area among four-dimensional parallelohedra at fixed volume. Its Lemma 2.3 specifies the standard realization and the 24 octahedral facet volumes, and its Lemma 8.1 records the twelve root-normal lines. It addresses the isoperimetric quotient and second variations rather than directional hyperplane-shadow volumes.

An's recent work on the dual geometry of spherical designs identifies exactly this 24-cell as an exceptional self-polar spherical five-design and explicitly describes the two 24-point dual realizations in Section 9.2. It does not compute or optimize the three-dimensional shadow-volume function.

Cauchy's formula and the regular 24-cell's facet data are standard ingredients and are not themselves presented as new. The contribution is the **complete exact brightness profile**, both sharp endpoints, and the classifications and counts of every extremizing direction; notably, precisely the original 24 vertex directions minimize brightness. Searches in shadow-volume, projection-body, \(D_4\) root-zonotope, and 24-cell extremal-projection terminology did not locate a published theorem with these endpoint classes.

## Limitations

This is an exact structural theorem for the single standard regular 24-cell; it is not a general theorem about all convex bodies, other lattice Voronoi polytopes, or affine deformations. It does not classify the combinatorial types of the resulting three-dimensional shadows or give stability estimates for almost-extremizing directions.

A classical root-zonotope formulation might encode the same extremal directions even if not indexed under the language of projections; that remains the principal originality risk. The full four-dimensional isoperimetric inequality is a previously established result and is not reproved or strengthened here.

## References

1. Congpei An, *Dual Geometry of Spherical Designs: Polarity, Self-Polar Rigidity, and Quadrature Structure*, arXiv:2609.02439v1, first submitted September 2, 2026; especially Section 9.2.
2. Matteo Novaga and Lark Song, *The Isoperimetric Problem for Four-Dimensional Parallelohedra*, arXiv:2610.01653v1, first submitted October 1, 2026; especially Lemmas 2.3 and 8.1.
3. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014; Cauchy's projection formula.
