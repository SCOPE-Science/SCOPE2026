# Exact Haar polygon-type law for central sections of the regular dodecahedron

## Finding

Write \(\varphi=(1+\sqrt5)/2\), and let \(D\) be the regular dodecahedron with the twenty vertices
\[
\{(\pm1,\pm1,\pm1)\}\ \cup\
\{(0,\pm\varphi^{-1},\pm\varphi),
(\pm\varphi^{-1},\pm\varphi,0),
(\pm\varphi,0,\pm\varphi^{-1})\},
\]
with independently chosen signs in each displayed group. Let \(U\) be uniform on the Euclidean unit sphere \(S^2\), and let \(N(U)\) count the vertices of the central planar polygon \(D\cap U^\perp\). Define
\[
\alpha=\arccos(1/3),\qquad \beta=\arccos(\sqrt5/3).
\]
Then \(N(U)\in\{6,8,10\}\) almost surely, and its **entire distribution** is
\[
\boxed{\begin{aligned}
\Pr\{N(U)=6\}&=10-\frac{15(\alpha+\beta)}\pi
=0.63840881155934\ldots,\\
\Pr\{N(U)=8\}&=\frac{15(2\alpha+\beta)}\pi-15
=0.23898946889977\ldots,\\
\Pr\{N(U)=10\}&=6-\frac{15\alpha}\pi
=0.12260171954089\ldots.
\end{aligned}}
\]
The ten vertex-orthogonality great circles partition \(S^2\) into exactly ninety-two generic sign chambers. Exactly twenty are spherical hexagons producing six-vertex planar sections; sixty are spherical triangles producing eight-vertex sections; and twelve are spherical pentagons producing ten-vertex sections. The spherical areas of **each individual chamber** in these three classes are, respectively,
\[
\boxed{2\pi-3\alpha-3\beta,\quad 2\alpha+\beta-\pi,
\quad 2\pi-5\alpha.}
\]
In particular \(\mathbb E N(U)=30\beta/\pi\). By Euclidean polarity, the same three probabilities describe the number of sides of the generic orthogonal planar **shadow of the regular icosahedron**, not the number of vertices in a central icosahedron section.

## Assumptions and scope

The section plane always contains the dodecahedron center. A direction is sampled by normalized surface area on \(S^2\), not by a random affine offset; antipodal directions induce the same section. Generic means that no original dodecahedral vertex lies on the plane. The nongeneric directions lie on finitely many great circles and have spherical probability zero. The metric scale of the dodecahedron has no effect on the results; the stated coordinates fix a convenient scale. The expression *polygon type* concerns only the number of sides, which determines a planar convex polygon's abstract combinatorial type.

## Proof

**Edge-crossing reduction.** The twenty displayed vertices all satisfy \(\|v\|_2^2=3\). The minimum nonzero squared distance among distinct vertices is \(6-2\sqrt5\); the thirty pairs at this distance are precisely the thirty dodecahedral edges. Each original vertex has degree three. For a generic \(u\), every section vertex arises uniquely from an original edge crossing \(u^\perp\) in its relative interior. Conversely, each such crossing is a section vertex. Consequently,
\[
N(u)=\#\bigl\{\{v,w\}\in E(D):
\langle u,v\rangle\langle u,w\rangle<0\bigr\}.
\tag{1}
\]
The ten pairs of antipodal dodecahedral vertices determine ten distinct unoriented great circles \(\langle u,v\rangle=0\). For \(u\) avoiding them, the ten signs of the vertex-axis inner products determine every factor in (1). Thus \(N(u)\) is constant in each open sign chamber.

**Exhaustive chamber construction over an exact number field.** Double all twenty vertex coordinates, so each coordinate is an integer linear combination of \(1\) and \(\sqrt5\). Choose one vector \(v_i\) from each antipodal pair, indexed \(0\le i<10\). All these vectors have squared length twelve. A direct exact dot-product evaluation verifies that no three axis vectors are coplanar: for each \(i<j\), \(v_i\times v_j\) is nonzero, and its dot product with every other axis is nonzero. Thus the ten great circles have forty-five transverse antipodal intersection pairs, with no triple concurrency.

Every open sign chamber touches at least one of those pairwise intersections; its closure is a spherical polygon cut out by closed hemispheres. At each oriented intersection \(w=\pm(v_i\times v_j)\), the two vanishing signs can be chosen independently in four ways, while all eight remaining signs are fixed by \(\operatorname{sgn}\langle w,v_k\rangle\). Therefore these \(90\times4\) exact local sign evaluations enumerate **every** attainable generic chamber sign mask, possibly with repetitions. Precisely ninety-two distinct masks occur. Independently, the number of regions for ten great circles in this transverse general-position arrangement is \(10(10-1)+2=92\), confirming completeness.

For each attainable sign mask \(s=(s_0,\ldots,s_9)\), its closed spherical polygon has precisely those oriented intersection vectors \(w\) for which
\[
s_k\langle w,v_k\rangle\ge0\quad\text{for every}\ k.
\tag{2}
\]
Because no three circles concur, each accepted \(w\) is one distinct polygon corner, and exactly two boundary great circles meet there. At the corner for indices \(i,j\), its spherical interior angle is
\[
\arccos\!\left(-\frac{s_i s_j\langle v_i,v_j\rangle}{12}\right).
\tag{3}
\]
This produces the complete exact classification below. Each count refers to the number of **distinct spherical chambers**, not to a sampling estimate.

| Section vertices | Chambers | Corners per chamber | Complete interior-angle multiset |
| --- | ---: | ---: | --- |
| \(6\) | \(20\) | \(6\) | Three \(\pi-\alpha\) and three \(\pi-\beta\) |
| \(8\) | \(60\) | \(3\) | Two \(\alpha\) and one \(\beta\) |
| \(10\) | \(12\) | \(5\) | Five \(\pi-\alpha\) |

These finite entries are independently reconstructible with the included pure-Python `check_dodeca_sections.py`, which explicitly generates all twenty coordinates and all thirty shortest-distance edges, uses exact integer-pair arithmetic in \(\mathbb Z[\sqrt5]\), verifies the no-triple-concurrence hypothesis, constructs all ninety-two masks, evaluates (1) and (2) for each, and compares the entire angle multiset (3). In particular, the computation is an **exhaustive exact finite certificate** for the above table, not a random experiment. The sign of \(a+b\sqrt5\) with integers \(a,b\) is decided without floating point by comparing \(a^2\) with \(5b^2\) when the two summands have opposing signs. The theorem about arbitrary directions follows by this complete finite chamber decomposition.

**Spherical excess and probabilities.** A convex spherical \(k\)-gon with interior angles \(\theta_1,\ldots,\theta_k\) has area \(\sum_i\theta_i-(k-2)\pi\). Applying it to the three rows proves, respectively,
\[
A_6=2\pi-3\alpha-3\beta,\qquad
A_8=2\alpha+\beta-\pi,\qquad
A_{10}=2\pi-5\alpha.
\tag{4}
\]
As a consistency check, \(20A_6+60A_8+12A_{10}=4\pi\). Since uniform spherical probability is area divided by \(4\pi\), multiplication of (4) by the corresponding chamber counts yields all three asserted exact probabilities. All areas in (4) are strictly positive.

**Independent mean identity.** For any two unit directions separated by spherical angle \(\theta\), a Haar-random normal separates their signs with probability \(\theta/\pi\). Projecting the normal onto their two-dimensional span proves this elementary fact. Every dodecahedral edge joins two vertices whose normalized scalar product is \(\sqrt5/3\), hence whose angle is \(\beta\). Linearity of expectation in (1) therefore gives \(\mathbb E N(U)=30\beta/\pi\), agreeing with the weighted sum of the three probabilities without assuming independent edge crossings.

**Polar interpretation.** For an origin-symmetric full-dimensional polytope, the polar within \(u^\perp\) of its central section equals the orthogonal projection of its polar body. In the plane, polarity preserves the number of polygon vertices/sides. The polar of this dodecahedron is an appropriately scaled regular icosahedron. This proves the stated silhouette interpretation but does **not** identify central sections of the icosahedron with central sections of the dodecahedron.

## Verification

The complete exact finite certificate is `check_dodeca_sections.py`, runnable using `python3 check_dodeca_sections.py` with Python 3.10 or later and no nonstandard dependencies. It verifies the coordinates, the full edge graph, all ten projective vertex axes, all forty-five transverse great-circle intersections, all ninety-two attainable sign masks, the three face-count/corner-count populations and every angle multiset. Its final line begins `CHECKS PASS`. An independent check multiplies each spherical area by its chamber count, verifies the total equals \(4\pi\), and compares the resulting expected side count against \(30\beta/\pi\). The numerical checks of inverse trigonometric identities are auxiliary; finite-case completeness and signs use exact arithmetic. No inference from Monte Carlo to an infinite probability statement is made.

## Relationship to prior work

Birkemeyer, Brose, Brandenburg and Prün (arXiv:2609.16195, initially public September 14, 2026) study the central-section vertex-count function of simple polytopes, its reconstruction properties and the governing arrangement of vertex-orthogonality hyperplanes. The complete accessible manuscript contains that general framework and section/projection polarity but does not calculate Haar measures or this dodecahedral three-point law. De Loera, Lopez-Campos and Torres (arXiv:2412.12419, initially public December 17, 2024) address achievable vertex counts of hyperplane sections; counts of possible values alone do not imply their Haar probabilities. Brandenburg, De Loera and Meroni (arXiv:2304.14239) treat parameter-cell decompositions and extremal sections, not these spherical chamber areas.

The published *Exact Haar polygon-type law for central icosahedron sections* gives a different two-point distribution for **central icosahedron sections**, with thirty-two spherical sign chambers. It is not the polar statement here: the polar counterpart here concerns **icosahedral shadows**, not icosahedral central sections. The published *Exact orientation-variance spectrum of Platonic shadow areas* computes moments of projected **area**, not silhouette polygon side counts. The exact formulas and ninety-two-chamber classification above are not implied by any of these inspected statements. Earlier unindexed stereological or spherical-tessellation calculations might nevertheless yield an equivalent law; the novelty assessment is limited to the compared accessible works, not a proof of historical priority.

## Limitations

The conclusion holds for exactly regular three-dimensional dodecahedra and uniformly random central planes. It does not classify sections through original vertices, noncentral sections, unequal metric deformations, or distributions of sectional area/perimeter. The chamber enumeration and resulting spherical areas are elementary exact computations in a fixed algebraic coordinate system; no general theorem for all simple polytopes is claimed. Historic spherical-geometric tables might already encode equivalent incidence information. The embedded checker verifies a mathematically justified exhaustive finite reduction; it is not an external independent scientific audit.

## References

1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public September 14, 2026), https://arxiv.org/abs/2609.16195.
2. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public December 17, 2024), https://arxiv.org/abs/2412.12419.
3. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first public April 27, 2023), https://arxiv.org/abs/2304.14239.
4. *Exact Haar polygon-type law for central icosahedron sections*, published geometric research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
5. *Exact orientation-variance spectrum of Platonic shadow areas*, published geometric research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
