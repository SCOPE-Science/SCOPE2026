# Sharp endpoint-area laws for random central sections of the three-cube

## Finding
Let \(Q=[-1,1]^3\), let \(U\) be uniformly distributed on the unit sphere \(S^2\), and let \(A(U)=\mathcal H^2(Q\cap U^\perp)\) be ordinary Euclidean area. Then \(4\le A(U)\le4\sqrt2\). There is \(\varepsilon_0>0\) such that, for every \(0<\varepsilon<\varepsilon_0\), the **exact** lower-end distribution is
\[
\Pr\{A(U)\le4+\varepsilon\}=3\left(1-\frac4{4+\varepsilon}\right).
\]
At the upper endpoint,
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{A(U)\ge4\sqrt2-\varepsilon\}}{\varepsilon^2}
=\frac{3(4+\pi)}{16\pi\sqrt2}.
\]
Consequently the lower probability has leading coefficient \(3/4\) and exponent one, while the upper probability has an explicit coefficient and exponent two. These statements are for central sections with a Haar-uniform *normal*, not for randomly offset planes or for planar projections.

## Assumptions and scope
The cube has side length two; the surface measure of \(S^2\) is normalized by \(4\pi\). The endpoints are the classical extrema: the six oriented coordinate-axis normals give area \(4\), and the twelve oriented signed coordinate-face-diagonal normals give area \(4\sqrt2\). The probability statements are insensitive to the choice between oriented and unoriented normals because \(A(U)=A(-U)\). The lower identity holds in a sufficiently small, unspecified but positive, endpoint neighborhood; the upper statement is a sharp first asymptotic and does not assert an exact interior CDF.

## Proof
**1. Directional formula.** For an arbitrary unit normal put \(a\ge b\ge c\ge0\) equal to the descending order of its absolute coordinates. By signed permutations assume \(U=(a,b,c)\). When \(c>0\), solve the plane equation for the first coordinate: \(x_1=-(b x_2+c x_3)/a\). Orthogonal area on this graph has Jacobian \(1/a\), since \(\|U\|_2=1\). Its domain in the \((x_2,x_3)\)-square \([-1,1]^2\) obeys \(|b x_2+c x_3|\le a\). If \(a\ge b+c\), this restriction removes nothing and area is \(4/a\). Otherwise the two forbidden corner triangles have combined square-area \((b+c-a)^2/(bc)\). Thus
\[
A(U)=\frac4a-\frac{(b+c-a)_+^2}{abc},\qquad c>0,
\]
with continuous extension \(A(U)=4/a\) when \(c=0\). In particular, this formula alone provides an all-direction evaluator, without calculating the random-area CDF.

**2. Endpoint normal sets.** The classical cube-section extrema and their equality cases give \(A=4\) only at the six coordinate axes and \(A=4\sqrt2\) only at the twelve signed coordinate face diagonals, as in the cited cube-section literature. Alternatively the first conclusion follows from the directional formula and elementary chamber optimization; for the upper endpoint one may use the known sharp cube slicing theorem and its equality cases. Their finiteness and continuity ensure that every sufficiently small endpoint event lies in disjoint prescribed neighborhoods of the relevant normals.

**3. Exact lower-end germ.** Near a coordinate normal \(U=(\sqrt{1-t^2-s^2},t,s)\), one has \(a\ge b+c\), so \(A(U)=4/a\). For sufficiently small \(\varepsilon\), \(A\le4+\varepsilon\) is therefore precisely the spherical cap \(a\ge4/(4+\varepsilon)\), repeated at six disjoint axes. A cap with cosine threshold \(z\) has normalized area \((1-z)/2\); six caps yield exactly \(3(1-4/(4+\varepsilon))\). This establishes both the germ and \(\Pr(A\le4+\varepsilon)=\tfrac34\varepsilon+O(\varepsilon^2)\).

**4. Upper-end tangent deficit.** At \(U_0=(1,1,0)/\sqrt2\), take the orthogonal tangent basis \(e_t=(1,-1,0)/\sqrt2\) and \(e_s=(0,0,1)\), and write
\[
U(t,s)=\sqrt{1-t^2-s^2}\,U_0+t e_t+s e_s.
\]
For \(p=|t|\), \(q=|s|\), the exact formula from step 1 gives, uniformly in angular directions as \((t,s)\to(0,0)\),
\[
4\sqrt2-A(U(t,s))=D(p,q)+o(\sqrt{t^2+s^2}),\quad
D(p,q)=4\sqrt2\,p+\frac{2(q-\sqrt2p)_+^2}{q}.
\]
The quotient is defined to be zero at \(q=0\). This is a continuous strictly positive degree-one homogeneous function off the origin. Indeed \(D=4\sqrt2p\) when \(q\le\sqrt2p\), while \(D=2q+4p^2/q\) when \(q\ge\sqrt2p\).

**5. Spherical sublevel area.** For \(p,q\ge0\), the inequality \(D(p,q)\le1\) is equivalent to
\[
0\le p\le\frac1{4\sqrt2},\qquad
0\le q\le\frac{1+\sqrt{1-32p^2}}4.
\]
Hence the area of this first-quadrant region is exactly
\[
J=\int_0^{1/(4\sqrt2)}\frac{1+\sqrt{1-32p^2}}4\,dp
=\frac{4+\pi}{64\sqrt2}.
\]
The tangent chart has spherical Jacobian \((1-t^2-s^2)^{-1/2}=1+O(t^2+s^2)\). Positivity and homogeneity of \(D\) imply that the rescaled upper-end event converges in area to \(\{D(|t|,|s|)\le1\}\). Its area near each maximizing normal is \(4J\varepsilon^2+o(\varepsilon^2)\). There are twelve such normals, giving
\[
\Pr(A\ge4\sqrt2-\varepsilon)
=\frac{12\cdot4J}{4\pi}\varepsilon^2+o(\varepsilon^2)
=\frac{3(4+\pi)}{16\pi\sqrt2}\varepsilon^2+o(\varepsilon^2).
\]
This calculation counts all orientation sectors and includes the absolute-value cusp along the face-diagonal normal.

## Verification
Run `python3 checker.py` with only the Python standard library. The checker reconstructs the plane–cube intersection independently from the twelve cube edges, projects the intersection vertices to an orthonormal plane basis, computes their planar convex-hull area, and compares 400 random normals against the explicit formula (maximum observed discrepancy below \(5\times10^{-12}\)). It also checks endpoint configurations, first-order tangent expansions at multiple directions, and a numerical quadrature of the exact tangent-sublevel area. These are finite reproducibility checks, not substitutes for the analytic proof or for the literature comparison.

## Relationship to prior work
Fodor and González Merino (first public version 2025-11-03) study central *diagonal* Gaussian-weighted cube sections, not a Haar-random Euclidean-volume distribution. Ambrus and classical cube-slicing work establish section-volume extrema and critical normals; these extrema alone do not determine probabilities in shrinking spherical neighborhoods. Marichal and Mossinghoff provide exact section volume for a *fixed* normal, but do not integrate its endpoint events over Haar normals. Lonke determines expected face numbers of random central cube sections, not area-tail coefficients. Van der Jagt, Jongbloed, and Vittorietti consider the distinct model of isotropically and uniformly random *offset* hyperplanes, and prove density-existence/approximation statements rather than the central fixed-offset endpoint coefficients here. A direct prior derivation of the same coefficients remains a bibliographic possibility.

## Limitations
Only the three-dimensional, centered, axis-aligned side-two cube and Haar-uniform central-plane normals are treated. The upper result is asymptotic and does not yield the middle part of the full distribution. The proof uses previously established global extrema and their equality configurations; independent validation has not been performed. The references are comparison evidence, not proof of absolute novelty.

## References
- F. Fodor and B. González Merino, *Central diagonal sections of Gaussian cubes*, arXiv:2511.01504v1 (2025-11-03), https://arxiv.org/abs/2511.01504.
- G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778, https://arxiv.org/abs/2107.14778.
- Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, https://arxiv.org/abs/math/9812123.
- J.-L. Marichal and M. J. Mossinghoff, *Slices, slabs, and sections of the unit hypercube*, arXiv:math/0607715, https://arxiv.org/abs/math/0607715.
- T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, Image Analysis & Stereology 42 (2023), 171–184, https://doi.org/10.5566/ias.2923.
