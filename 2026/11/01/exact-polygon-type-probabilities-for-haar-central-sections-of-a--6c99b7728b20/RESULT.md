# Exact polygon-type probabilities for Haar-central sections of a regular truncated tetrahedron

## Finding

Let \(K\) be a regular truncated tetrahedron, and cut it by the plane through its centroid with a Haar-uniform unoriented normal. Write \(N\) for the number of sides of the resulting planar convex polygon. All generic section polygons have four, five, or six sides; all three types occur with positive probability. Define

\[
\begin{aligned}
S_1&=10\sqrt6+4\sqrt{30}+17\sqrt2+7\sqrt{10},\\
S_2&=6\sqrt{11}+4\sqrt{22}+8\sqrt6+11\sqrt3,\\
q&=\frac{24}{\pi}\left(\arctan\frac2{S_1}+\arctan\frac1{S_2}\right),\\
\mu&=\frac{18}{\pi}\arccos\frac7{11}.
\end{aligned}
\]

Then the **entire Haar polygon-type law** is

\[
\boxed{\mathbb P(N=4)=5-\mu+q,\qquad
\mathbb P(N=5)=\mu-4-2q,\qquad
\mathbb P(N=6)=q.}
\]

Their values, in order, are approximately \(0.2159360853126404727\), \(0.5202474652389363762\), and \(0.2638164494484231511\). Consequently a pentagon is the most common section, with probability greater than one-half, while the exact expected side count is \(\mu\approx5.0478803641357826784\).

## Assumptions and scope

Start with the tetrahedron whose vertices are \((1,1,1)\), \((1,-1,-1)\), \((-1,1,-1)\), and \((-1,-1,1)\). Truncate each corner one-third along every incident edge and rescale the resulting polytope by three. The rescaled truncated tetrahedron has the twelve vertices

\[
V=\{2A+B:A,B\in T,\ A\ne B\},
\]

where \(T\) is the four-point set above. This rescaling does not change section types. The plane has equation \(u\cdot x=0\), with \(u\) sampled uniformly on \(S^2\), identified with its antipode. Normals through a vertex comprise a null set and are excluded from the generic classification.

## Proof

**1. Sections as edge crossings.** Directly from the twelve vertices, exactly eighteen unordered vertex pairs have squared distance \(8\); these are precisely the edges of the truncated tetrahedron. Every vertex has squared norm \(11\); adjacent vertices have inner product \(7\). For a generic normal \(u\), the number of vertices of the polygon \(K\cap u^\perp\) is exactly

\[
N(u)=\sum_{\{v,w\}\in E}{\bf1}\{(u\cdot v)(u\cdot w)<0\}.
\]

The formula also proves that the side count depends only on the signs of twelve homogeneous linear forms.

**2. Exhaustive angular subdivision.** The tetrahedral symmetry group and invariance under \(u\mapsto-u\) reduce spherical directions to a chamber with \(u\) proportional to \((1,y,z)\), where \(0\le z\le y\le1\). The forty-eight equivalent chambers each have solid angle \(\pi/12\). Besides the chamber boundary, the vertex-sign changes occur only on four line segments of the form

\[
z=(1+y)/3,\quad z=3y-1,\quad z=1-3y,\quad z=(1-y)/3.
\]

These four segments partition the triangular parameter chamber into precisely six positive-area cells, listed below by their ordered planar vertices \((y,z)\). Their side counts follow by substituting an interior rational barycenter into the edge-crossing expression; no sign changes can occur inside a cell.

| Side count | Planar vertices of the cell |
| --- | --- |
| \(5\) | \((1,2/3),(1,0),(2/5,1/5),(1/2,1/2)\) |
| \(6\) | \((1,0),(1/3,0),(2/5,1/5)\) |
| \(4\) | \((1/3,0),(0,0),(1/4,1/4)\) |
| \(4\) | \((1/4,1/4),(1/2,1/2),(2/5,1/5)\) |
| \(5\) | \((2/5,1/5),(1/3,0),(1/4,1/4)\) |
| \(6\) | \((1/2,1/2),(1,1),(1,2/3)\) |

The six cells partition the whole chamber, so no other generic section side counts exist.

**3. The hexagonal probability.** The two six-sided cells are spherical triangles with vertex rays, respectively,

\[
\begin{aligned}
A&:\ (1,1,0),\ (3,1,0),\ (5,2,1),\\
B&:\ (2,1,1),\ (1,1,1),\ (3,3,2).
\end{aligned}
\]

For rays \(a,b,c\) making a spherical triangle of solid angle less than a hemisphere, the standard exact formula is

\[
\Omega(a,b,c)=2\arctan\frac{|\det(a,b,c)|}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(b\cdot c)\|a\|+(c\cdot a)\|b\|}.
\]

The two determinants have absolute values \(2\) and \(1\); their denominators are exactly \(S_1\) and \(S_2\). Because the chamber has solid angle \(\pi/12\), its two six-sided triangles contribute

\[
\mathbb P(N=6)=\frac{12}{\pi}\left(2\arctan\frac2{S_1}+2\arctan\frac1{S_2}\right)=q.
\]

**4. The other two probabilities.** Two nonzero vectors making angle \(\theta\in[0,\pi]\) have opposite signs under a Haar-uniform normal with probability \(\theta/\pi\): rotational invariance reduces the event to the angular wedge between the two great-circle sign boundaries. Here every one of the eighteen edges has \(\cos\theta=7/11\). Linearity of expectation therefore gives

\[
\mathbb E N=\frac{18}{\pi}\arccos(7/11)=\mu.
\]

Writing \(p_j=\mathbb P(N=j)\), we have \(p_4+p_5+p_6=1\), \(4p_4+5p_5+6p_6=\mu\), and \(p_6=q\). Solving these equations gives the stated formula. Positivity follows also from the nonempty angular cells of each type. The strict pentagonal majority also has a purely rational certificate. Use the classical bounds \(333/106<\pi<355/113\), the elementary radical bounds \(S_1>9257/100\), \(S_2>773/10\), and \(\sqrt2>1414/1000\). The alternating arctangent series gives \(\arctan t>t-t^3/3+t^5/5-t^7/7\) for \(0<t<1\), whereas \(\arctan t\le t\). Substitution into \(\mu-4-2q\) proves the explicit strict bound \(p_5>0.518\); the standalone checker evaluates that final inequality with exact rational fractions. This completes the proof.

## Verification

Run `python verify_truncated_tetra.py` with Python, NumPy, and mpmath available. The standalone checker reconstructs the twelve vertices and eighteen edges, tests the four exact sign-change lines, uses exact rational arithmetic to verify six polygonal cell boundaries and rational interior sign certificates, computes all six spherical solid angles independently, and checks agreement between the direct cell-area law and the edge-angle expectation. A separate \(240000\)-normal Monte Carlo experiment gives \(51993\), \(124711\), and \(63296\) sections with four, five, and six sides, respectively, within expected sampling error. An exact rational interval certificate additionally proves that pentagons occur with probability above \(0.518\). The universal theorem follows from the exact chamber decomposition and solid-angle identities, not from Monte Carlo.

## Relationship to prior work

The truncated tetrahedron is classical; its four triangular faces, four regular hexagonal faces, twelve vertices, and eighteen edges are standard (Weisstein, *Truncated Tetrahedron*). König and Koldobsky (2018) study maximal perimeters of central hyperplane sections of cubes, and König (2020) analyzes extremal sections of the regular simplex, cross-polytope, and cube. Those works establish general geometric motivation but do not furnish this truncated-tetrahedral probability law. Lavau (2019) investigates a different property of the same truncated tetrahedron, namely passage of a congruent solid through a tunnel. The finite chamber computation and full three-atom probability distribution are the contribution here. A broader, previously overlooked stereological or integral-geometric classification could still affect historical priority.

## Limitations

The theorem applies to planes through the centroid with rotation-invariant orientation, to one fixed regular truncated tetrahedron up to similarity, and to the generic polygonal section. It does not classify off-center sections, other truncation depths, other solids, or weighted orientations. It has undergone self-review only; no independent audit or historical-priority certification is claimed.

## References

1. H. König and A. Koldobsky, *On the maximal perimeter of sections of the cube*, arXiv:1806.08659 (first publicly posted 2018-06-22); *Advances in Mathematics* 346 (2019), 773–804, doi:10.1016/j.aim.2019.02.017.
2. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743 (first publicly posted 2020-02-25).
3. E. W. Weisstein, *Truncated Tetrahedron*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedron.html.
4. G. Lavau, *The Truncated Tetrahedron Is Rupert*, *American Mathematical Monthly* 126 (2019), 929–932, doi:10.1080/00029890.2019.1656958.
