# Parity-sensitive optimal ellipsoid distortion of every diagonal cube slice

## Finding
For each integer \(n\ge3\) and each real \(0<s<n\), let
\[
K_{n,s}=\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i=s\},\qquad c_s=\tfrac{s}{n}\mathbf 1.
\]
Work in the affine hyperplane of \(K_{n,s}\), with its inherited Euclidean metric. Let \(J_{n,s}\) be its unique maximum-volume inscribed ellipsoid and \(L_{n,s}\) its unique minimum-volume enclosing ellipsoid. **Both are concentric Euclidean balls**, with center \(c_s\) and respective radii
\[
\boxed{r_{n,s}=\frac{\min(s,n-s)}{\sqrt{n(n-1)}}},\qquad
\boxed{R_{n,s}^{2}=\lfloor s\rfloor+(s-\lfloor s\rfloor)^2-\frac{s^2}{n}}.
\]
Thus the exact ellipsoidal volume ratio is
\[
\frac{\operatorname{vol}_{n-1}(L_{n,s})}{\operatorname{vol}_{n-1}(J_{n,s})}
=\left(\frac{R_{n,s}}{r_{n,s}}\right)^{n-1}.
\]
The distortion \(D_n(s)=R_{n,s}/r_{n,s}\) is symmetric under \(s\mapsto n-s\), constant with value \(n-1\) on \(0<s\le1\) and on \(n-1\le s<n\), strictly decreasing on \(1<s<n/2\), and strictly increasing on \(n/2<s<n-1\). Accordingly the **unique** global minimizing slice is \(s=n/2\), where
\[
\boxed{D_n(n/2)^2=\begin{cases}n-1,&n\text{ even},\\(n-1)^2/n,&n\text{ odd}.\end{cases}}
\]
The local stability of this optimum undergoes a parity transition: with \(h=|s-n/2|\downarrow0\),
\[
\boxed{D_n(s)^2-D_n(n/2)^2=
\begin{cases}
\dfrac{4(n-1)(n-2)}{n^2}h^2+O_n(h^3),&n\text{ even},\\[5pt]
\dfrac{4(n-1)^2}{n^2}h+O_n(h^2),&n\text{ odd}.
\end{cases}}
\]
Both leading coefficients are strictly positive. Hence the optimal ellipsoid ratio is quadratically stable for even \(n\) but has a linear cusp for odd \(n\). These claims hold for the *unrestricted* extremal ellipsoids, not just ellipsoids chosen to respect the coordinate symmetries.

## Assumptions and scope
The ambient cube is exactly \([0,1]^n\) with the standard Euclidean metric, and \(0<s<n\) ensures a full-dimensional compact convex body in the \((n-1)\)-dimensional affine space \(H_s\) given by the coordinate sum. Ellipsoid volumes are intrinsic \((n-1)\)-dimensional volumes. The distinction between \(s\in\mathbb Z\) and noninteger \(s\) is important at changes of vertex orbit type. At integer \(s\), the formula using \(\lfloor s\rfloor\) is interpreted literally. The endpoints \(s=0,n\) are excluded because the section is a point.

## Proof
**1. Symmetry forces both unrestricted extremal ellipsoids to be balls.** The polytopes are invariant under every permutation of the \(n\) coordinates. Both the John ellipsoid and the Löwner ellipsoid exist and are unique for any full-dimensional compact convex body in its affine hull. Their centers must therefore be fixed by all permutations, giving \(c_s\). On the translation space \(H_0=\{z:\sum z_i=0\}\), any permutation-invariant symmetric positive-definite operator is a scalar: its matrix in \(\mathbb R^n\) may be averaged over permutations, producing equal diagonal entries and equal off-diagonal entries, and such a matrix acts by one scalar on \(H_0\). Uniqueness of the extremizers makes their covariance matrices invariant, hence spherical. This rules out all translated or rotated competitors.

**2. Exact John radius and positive contact certificate.** The projection of \(e_i\) onto \(H_0\) equals \(p_i=e_i-\mathbf1/n\), with \(\|p_i\|^2=(n-1)/n\). Therefore the distance from \(c_s\) to the coordinate hyperplane \(x_i=0\) within \(H_s\) is \(s/\sqrt{n(n-1)}\), and to \(x_i=1\) is \((n-s)/\sqrt{n(n-1)}\). The ball of the stated radius is inside every defining coordinate halfspace, hence inside \(K_{n,s}\). At least one of these two families of hyperplanes is a true facet: if \(s\le n/2\), then \(s<n-1\) for \(n\ge3\), so all lower coordinate faces are facets; if \(s\ge n/2\), all upper coordinate faces are facets. Consequently no larger concentric ball can fit.

In fact, the stated ball is certified as **the unrestricted John ellipsoid** without invoking symmetry alone. For \(s\le n/2\), the point with one zero coordinate and each remaining coordinate equal to \(s/(n-1)\) belongs to \(K_{n,s}\) and contacts the ball. The \(n\) normalized contact directions are the negatives of \(u_i=\sqrt{n/(n-1)}\,p_i\). They satisfy
\[
\sum_i u_i=0,\qquad \sum_i\frac{n-1}{n}\,u_i\otimes u_i=I_{H_0},
\]
which are John's positive contact conditions. For \(s\ge n/2\), use the \(n\) analogous points with one coordinate one and all others \((s-1)/(n-1)\), with the positive \(u_i\) directions. At equality \(s=n/2\), both families contact. John's theorem establishes maximal ellipsoid volume globally and uniqueness.

**3. Vertices, circumsphere, and Löwner contact certificate.** At a vertex of \(K_{n,s}\), all but at most one coordinates are in \(\{0,1\}\): otherwise two fractional coordinates can be perturbed in opposite directions. Conversely every feasible such vector is a vertex. Write \(k=\lfloor s\rfloor\) and \(u=s-k\in[0,1)\). When \(u>0\), all vertices are the distinct coordinate permutations of \((1,\ldots,1,u,0,\ldots,0)\) with exactly \(k\) ones; when \(u=0\), they are the permutations of \(k\) ones and \(n-k\) zeros. Their squared distance from \(c_s\) is identically
\[
\sum_i(x_i-s/n)^2=\sum_i x_i^2-s^2/n=k+u^2-s^2/n=R_{n,s}^2.
\]
Convexity of the squared Euclidean norm implies the sphere of this radius contains the entire polytope. Let \(V\) be the uniform probability measure on its finite vertex orbit. Coordinate symmetry gives \(\mathbb E V=c_s\); its covariance is scalar on \(H_0\), and its trace is \(R_{n,s}^2\), hence
\[
\mathbb E[(V-c_s)\otimes(V-c_s)]=\frac{R_{n,s}^2}{n-1}I_{H_0}.
\]
Dividing contact vectors by \(R_{n,s}\) and weighting each vertex equally by \((n-1)/|\operatorname{vert}K_{n,s}|\) gives a zero-mean identity-covariance positive contact certificate. The dual (Löwner) ellipsoid characterization proves this containing sphere is the unique unrestricted minimum-volume ellipsoid. All vertices contact it, while no nonvertex does (strict convexity of the squared norm).

**4. Exact global minimization.** Cube complementation \(x\mapsto\mathbf1-x\) is an isometry from \(K_{n,s}\) to \(K_{n,n-s}\), so it suffices to study \(0<s\le n/2\). There the inradius squared is \(s^2/[n(n-1)]\). For \(k=\lfloor s\rfloor\), expand the exact squared distortion as
\[
D_n(s)^2=(n-1)\left[n-1-\frac{2nk}{s}+\frac{nk(k+1)}{s^2}\right].
\]
For noninteger \(s\in(k,k+1)\), its derivative is
\[
\frac{d}{ds}D_n(s)^2=\frac{2n(n-1)k(s-k-1)}{s^3}.
\]
It vanishes for \(k=0\) and is strictly negative for \(k\ge1\). The radius formula is continuous at all integer boundaries, so the profile is constant on \((0,1]\) and strictly decreasing on \((1,n/2)\). Reflecting proves the other half and uniqueness of its minimum. At \(s=n/2\), direct substitution gives \(D_n^2=n-1\) if \(n\) is even (integer central level), and \(D_n^2=(n-1)^2/n\) if odd (half-integer central level).

**5. Parity-sensitive stability.** Put \(s=n/2-h\), where \(h>0\) is small. If \(n\) is even, \(\lfloor s\rfloor=n/2-1\) and
\[
R_{n,s}^2=n/4-h+(1-1/n)h^2.
\]
If \(n\) is odd, \(\lfloor s\rfloor=(n-1)/2\) and
\[
R_{n,s}^2=(n-1)/4+(1-1/n)h^2.
\]
In both cases \(r_{n,s}^2=(n/2-h)^2/[n(n-1)]\). Substitute and expand the resulting rational functions at \(h=0\): for even \(n\), the linear terms cancel and the quadratic coefficient is \(4(n-1)(n-2)/n^2\); for odd \(n\), the linear coefficient is \(4(n-1)^2/n^2\). Reflection makes the asymptotics two-sided with \(h=|s-n/2|\). Their strictly positive coefficients establish the claimed sharp orders of local stability.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to enumerate all active-coordinate vertices in dimensions three through ten; verifies their Euclidean radii, centroids and contact covariances; independently solves random support-function linear programs using SciPy; checks the positive John contacts; and checks the sharp parity formula, simplex plateaus, and global inequalities. Run `python3 verify.py` with Python 3, NumPy and SciPy installed. The run recorded `VERIFY_OK 9960 exact and independent numerical checks`. The proof above, not finite enumeration, covers all integers \(n\ge3\) and all real \(0<s<n\).

## Relationship to prior work
The existence and contact characterizations of the unique John and Löwner ellipsoids are classical; Lin, Ge and Leng explicitly describe the John ellipsoid of a regular simplex. In the small-\(s\) region here the sections are regular simplices, and their radii are already consequences of that classical theorem.

Katz describes integral-rank hypersimplices as the base polytopes of uniform matroids. Ferroni and McGinnis study the broader family of thin box slices from the viewpoint of Ehrhart theory and enumeration. A more directly related earlier computation, *Thin slices of rectangular prisms have a three-barrier Euclidean inradius*, already determines the inradius and all incenters, including integer-rank hypersimplices. **The inradius formula is not claimed as new.** The precise claim retained here concerns both unrestricted ellipsoids throughout a *continuous* real-level family, the sharp globally optimized John-to-Löwner volume distortion, and the parity-dependent local stability at the unique optimal section.

Ivanov proves general bounds for John ellipsoid volumes of linear sections of the cube and the dual Löwner problem for projections of a cross-polytope. Those results control different quantities and do not imply this exact affine-level distortion profile or its parity stability law. A separately published three-phase John theorem for a **full-dimensional capped cube** concerns \(\sum x_i\le\tau\) rather than equality; taking its intersection with a hyperplane does not preserve its John ellipsoid, so that theorem likewise does not imply the present result.

## Limitations
The volume comparison is made **between the two ellipsoids**, not between an ellipsoid and the volume of the section. This is a Euclidean, coordinate-realization-sensitive theorem for diagonal parallel slices of a cube, not for arbitrary hyperplane orientations, arbitrary parallelotopes, or noisy slices. The two radii individually arise from accessible classical geometric computations; only the combined sharp full-family optimization, unrestricted certification and parity stability are retained as the contribution. An earlier unindexed paper might contain an equivalent ratio calculation; the literature comparison is substantial but not an independent historical-priority certification. No claim of independent mathematical validation is made.

## References
1. Si Lin, Xiong Ge, Gangsong Leng, *The John Theorem for Simplex*, arXiv:1001.4223, initial posting 2010-01-24, https://arxiv.org/abs/1001.4223.
2. Grigory Ivanov, *On the Volume of the John–Löwner Ellipsoid*, arXiv:1707.04442, initial posting 2017-07-14, https://arxiv.org/abs/1707.04442.
3. Eric Katz, *Matroid theory for algebraic geometers*, arXiv:1409.3503, initial posting 2014-09-11, https://arxiv.org/abs/1409.3503.
4. Luis Ferroni and Daniel McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808, initial posting 2022-02-23, https://arxiv.org/abs/2202.11808.
5. *Thin slices of rectangular prisms have a three-barrier Euclidean inradius*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-thin-slices-of-rectangular-prisms-have-a-three-barrier-euclidean--05cee6e258e6.
6. *Three-phase John ellipsoid of a capped hypercube*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127.
