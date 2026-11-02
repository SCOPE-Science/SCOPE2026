# Universal near-diameter boundary-chord tails of convex polytopes

## Finding

Let \(d\ge3\), and let \(P\subset\mathbb R^d\) be any compact full-dimensional convex polytope with diameter \(L>0\) and total facet area \(S=\mathcal H^{d-1}(\partial P)>0\). Independently sample \(X,Y\) from normalized \((d-1)\)-dimensional Hausdorff measure on \(\partial P\), and set \(D=\|X-Y\|\).

There is an explicit strictly positive constant \(C(P)\) such that
\[
\Pr\{D>L-\varepsilon\}=C(P)\varepsilon^{2d-2}+O_P(\varepsilon^{2d-1})\qquad(\varepsilon\downarrow0).
\]
The exponent \(2d-2\) is universal over all such polytopes. The coefficient is a finite sum of geometrically computable facet-cone volumes at the **ordered diametral vertex pairs**, as described below. In particular, this is not a statement about motion-invariant random lines, sample maxima, interior-uniform points, or intrinsic surface geodesics.

For a regular \(d\)-simplex of side length \(\ell\),
\[
\Pr\{D>\ell-\varepsilon\}=
\frac{d(d+1)4^{d-2}((d-1)!)^2}{(2d-2)!}
\left(\frac{\varepsilon}{\ell}\right)^{2d-2}
+O_d\!\left((\varepsilon/\ell)^{2d-1}\right).
\]
For a Euclidean \(d\)-cube of side length \(a\),
\[
\Pr\{D>a\sqrt d-\varepsilon\}=
\frac{2^{d-2}d^{d-1}}{(2d-2)!}
\left(\frac{\varepsilon}{a}\right)^{2d-2}
+O_d\!\left((\varepsilon/a)^{2d-1}\right).
\]
Thus the leading coefficients in three dimensions are \(8/\ell^4\) for a regular tetrahedron and \(3/(4a^4)\) for a cube.

## Assumptions and scope

All statements concern a **fixed** \(d\ge3\) and a **fixed** full-dimensional convex polytope \(P\); any implied constant in \(O_P\) may depend on the polytope, and the expansion is not claimed uniform as dimension or aspect ratio varies. Write \(k=d-1\). Let \(\mathscr E(P)\) be the finite set of *ordered* pairs \((v,w)\) of vertices of \(P\) with \(\|w-v\|=L\). For such a pair let \(e_{vw}=(w-v)/L\), and for each facet \(F\) incident at \(v\) define the relative cone \(C_{v,F}=\{t(z-v):t\ge0,\ z\in F\}\), a pointed \(k\)-dimensional cone in the affine span of \(F-v\). Set
\[
B(v,w)=\frac1S\sum_{F\ni v}
\mathcal H^k\bigl(\{h\in C_{v,F}:\langle e_{vw},h\rangle\le1\}\bigr).
\]
The truncations are finite and have positive \(k\)-measure. The explicit coefficient is
\[
\boxed{C(P)=\frac{(k!)^2}{(2k)!}
\sum_{(v,w)\in\mathscr E(P)}B(v,w)B(w,v).}
\]
This coefficient is strictly positive, has units of inverse length to the power \(2k\), and includes both orientations of each diametral pair.

For computing individual summands, triangulate each \(C_{v,F}\) into full-dimensional simplicial cones of generating rays \(r_1,\ldots,r_k\). A simplicial contribution to the (unnormalized) truncated measure equals
\[
\frac{\sqrt{\det(\langle r_i,r_j\rangle)_{i,j=1}^k}}
{k!\,\prod_{i=1}^k\langle e_{vw},r_i\rangle}.
\]
This is invariant under positive rescaling of the rays. Faces of lower dimension do not contribute to \(\mathcal H^k\).

## Proof

**1. Diametral points are vertices; endpoint directions are positive.** For any fixed \(w\in P\), strict convexity of squared Euclidean norm implies that a nonvertex \(v\) cannot maximize \(\|w-v\|\) over \(P\). Repeating in the other variable proves that all diametral pairs belong to \(\mathscr E(P)\). Fix one such ordered pair \((v,w)\) and write \(e=(w-v)/L\). For every \(z\in P\), the diameter inequality \(\|w-z\|^2\le L^2\) gives
\[
2L\langle e,z-v\rangle\ge\|z-v\|^2.
\]
For each nonzero ray of the tangent cone at \(v\), apply this inequality to a sufficiently short nonzero point on the ray. It follows that \(\langle e,h\rangle>0\) for every nonzero tangent direction \(h\). Compactness of the tangent cone's intersection with the unit sphere gives a \(c_{vw}>0\) satisfying \(\langle e,h\rangle\ge c_{vw}\|h\|\) for all such \(h\). At \(w\), similarly \(\langle-e,h\rangle\ge c_{wv}\|h\|\). This proves that each truncated facet cone in the definition of \(B\) is compact and has finite measure.

**2. Exact local one-point cap law.** A sufficiently small neighborhood of a vertex is, facet by facet, exactly equal to a neighborhood of the apex of its facet cones. For every sufficiently small \(t>0\), positivity above ensures that the entire truncation \(\{h\in C_{v,F}:\langle e,h\rangle\le t\}\) lies inside this neighborhood. Consequently, with \(X\) drawn uniformly on \(\partial P\),
\[
\Pr\{X\text{ near }v,\ \langle e,X-v\rangle\le t\}=B(v,w)t^k.
\]
This equality is **exact** for sufficiently small \(t\): surface measure is homogeneous of degree \(k\) on every facet cone. Distinct facets overlap only on sets of zero \(\mathcal H^k\)-measure.

**3. Convolution for the linear diameter deficit.** Restrict \(X=v+h\) and \(Y=w+j\) to disjoint fixed small endpoint neighborhoods. Put \(a=\langle e,h\rangle\ge0\) and \(b=\langle-e,j\rangle\ge0\). Independence and the local cap laws imply
\[
\Pr\{X\text{ near }v,\ Y\text{ near }w,\ a+b\le t\}
=B(v,w)B(w,v)\frac{(k!)^2}{(2k)!}t^{2k}
\]
for all sufficiently small \(t>0\). Indeed, integrate the derivative \(kB(v,w)a^{k-1}\) against \(B(w,v)(t-a)^k\), using the beta integral \(k\operatorname B(k,k+1)=(k!)^2/(2k)!\).

**4. The exact Euclidean deficit has the same leading law.** In the same neighborhoods, Taylor expansion of Euclidean length around \(Le\) gives
\[
L-\|w+j-v-h\|=a+b+O_P((\|h\|+\|j\|)^2).
\]
By Step 1, \(a+b\ge c(\|h\|+\|j\|)\) for some strictly positive \(c\). Shrink the neighborhoods so the quadratic Taylor remainder is at most half the linear term; then the event \(D>L-\varepsilon\) inside them forces \(\|h\|+\|j\|=O_P(\varepsilon)\). Accordingly the near-diameter event is sandwiched between the linear events \(a+b<\varepsilon-K\varepsilon^2\) and \(a+b<\varepsilon+K\varepsilon^2\), with constants independent of \(\varepsilon\). Expanding \((\varepsilon\pm K\varepsilon^2)^{2k}\) gives the claimed \(O_P(\varepsilon^{2k+1})\) remainder.

**5. Sum over all and only diametral pairs.** Compactness, the strict-convexity argument of Step 1, and finiteness of \(\mathscr E(P)\) imply that all point pairs with distance sufficiently close to \(L\) lie in disjoint neighborhoods of members of \(\mathscr E(P)\). Summing Step 4 over ordered pairs yields the formula for \(C(P)\). Each \(B\) is positive, so the coefficient is positive and the tail exponent cannot be improved.

**6. Simplices and cubes.** In the regular simplex, equal facets have surface probability \(1/(d+1)\). Fix a diametral edge \(v\to w\). In barycentric coordinates on an incident facet, the linear axial loss has coefficient \(1\) on the barycentric direction toward \(w\) and \(1/2\) on each direction toward the other vertices, after scaling by \(\ell\). Of the \(d\) facets incident at \(v\), one omits \(w\) and contributes \(2^{d-1}\ell^{-k}/(d+1)\) to \(B\); the remaining \(d-1\) contribute \(2^{d-2}\ell^{-k}/(d+1)\) apiece. Thus \(B(v,w)=2^{d-2}\ell^{-k}\). There are \(d(d+1)\) ordered diametral vertex pairs, giving the simplex formula.

In the \(d\)-cube, only opposite vertices are diametral, giving \(2^d\) ordered pairs. Each of the \(d\) facets meeting an endpoint contributes a \(k\)-orthant truncated by a linear form whose \(k\) coefficients are \(1/\sqrt d\); division by the total boundary area \(2da^k\) gives \(B(v,w)=d^{k/2}/(2k!a^k)\). Substitution in the general coefficient gives the cube formula. The displayed tetrahedron and three-cube coefficients follow by setting \(d=3\).

## Verification

Run `python verify.py` with Python 3 and NumPy. The standalone script independently evaluates the local linearized facet cones using exact rational arithmetic for regular simplices of dimensions \(2\) through \(21\), verifies the closed forms and three-dimensional constants, checks the regular octahedron as a separate sanity check, and performs importance-sampled independent geometric diagnostics in dimensions \(3\) and \(4\). It reports `VERIFY_OK` on successful execution. The finite computations and Monte Carlo experiments are checks, not substitutes for the all-polytope proof above. The exact \(O_P\) remainder in Steps 4–5 is analytic, not inferred from simulation.

## Relationship to prior work

Mayer and Molchanov (2006) study limiting maximal interpoint distances in Euclidean balls. Their framework takes near-diameter **two-point tail behavior as an input** and computes cases with spherical symmetry; the explicit arbitrary-polytope **surface-area-pair** coefficient proved here is not a consequence of their stated ball formulas. Lao's 2010 thesis investigates distances on edges of planar polygons and sample-maximum laws in its Chapter 5. That work supports the local endpoint expansion approach but concerns planar polygonal boundary geometry, rather than dimension \(d\ge3\) polytope facets and the general \(2d-2\) coefficient. Brunel's 2015 preprint considers boundary-sampled random polytopes and diameter estimation under Hausdorff error, not this exact two-point upper-tail coefficient.

The statement also differs from results about random-line chords, point-pair short-distance tails, and interior-uniform point sampling: those measures and endpoint regimes have different local scaling. Existing general extreme-value machinery may use the coefficient as an input, but does not itself evaluate the necessary facet cones.

## Limitations

Historical priority is provisional: an equivalent cone-based regular-variation formula might appear under extreme-value or convex-geometric terminology not indexed by the inspected sources. No claim is made about arbitrary smooth bodies, nonconvex polyhedra, intrinsic geodesic distance, random-line sampling, growing dimension, or the limiting law of a maximum over many dependent pairs. Simulations involve finite \(\varepsilon\) and therefore have nonzero deterministic bias.

## References

- Michael Mayer and Ilya Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, first arXiv posting 2006-05-11, arXiv:math/0605289, https://arxiv.org/abs/math/0605289 ; https://arxiv.org/pdf/math/0605289 .
- Wei Lao, *Some weak limit laws for the diameter of random point sets in bounded regions*, KIT Scientific Publishing, 2010, Chapter 5 and its appendix, https://publikationen.bibliothek.kit.edu/1000019800/105664897 .
- Victor-Emmanuel Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, first arXiv posting 2015-03-05, arXiv:1503.01504, https://arxiv.org/abs/1503.01504 ; https://arxiv.org/pdf/1503.01504 .
