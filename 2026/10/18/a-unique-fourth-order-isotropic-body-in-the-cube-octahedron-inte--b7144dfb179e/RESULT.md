# A unique fourth-order isotropic body in the cube–octahedron intersection family

## Finding
For each real \(c>0\), let
\[
K_c=\{x\in[-1,1]^3:|x_1|+|x_2|+|x_3|\le c\},
\qquad J_{a b d}(c)=\int_{K_c}x_1^a x_2^b x_3^d\,dx.
\]
There is **exactly one** parameter \(c>0\) for which the uniform solid-volume fourth-moment tensor is rotationally isotropic, meaning
\[
\int_{K_c}\langle x,u\rangle^4\,dx
=\frac{\|u\|_2^4}{5}\int_{K_c}\|x\|_2^4\,dx
\quad\text{for every }u\in\mathbb R^3.
\tag{1}
\]
It is the unique root in \((1,2)\) of the degree-seven equation
\[
\boxed{2c^7-21c^6+63c^5-35c^4-105c^3+147c^2-49c-3=0,}
\tag{2}
\]
with
\[
\boxed{c_*=1.699067658322615498760211\ldots.}
\]
The polytope \(K_{c_*}\) is **not** a Euclidean ball, nor the regular truncated octahedron; it has 24 vertices (the signed coordinate permutations of \((1,c_*-1,0)\)), six square and eight hexagonal facets, and full cubic symmetry. Its second moments are isotropic by symmetry, and its fourth moments are isotropic only at this parameter. Its sixth moments are **not** isotropic at this parameter: specifically,
\[
\boxed{J_{600}(c_*)-5J_{420}(c_*)<0.}
\tag{3}
\]
Thus rotationally isotropic fourth-order moments arise accidentally inside a one-parameter family of nonspherical, cubic-symmetry convex polyhedra, without extending to sixth order.

## Assumptions and scope
The measure is ordinary three-dimensional Lebesgue volume on the **filled** convex body; it is not a surface-area or vertex measure. The origin is the symmetry center, and all parameters are positive. Equality (1) is a property of the *tensor of fourth volume moments*, not rotational invariance of the set itself. Changing \(c\) changes the body, except that \(K_c=[-1,1]^3\) for \(c\ge3\). For \(0<c\le1\), the body is a scaled regular octahedron. The only parameter with (1) lies strictly between these regimes. The one-dimensional family is not claimed to exhaust all fourth-isotropic convex bodies.

## Proof
**1. Reduction to a single scalar.** Permutations and independent sign flips of coordinates preserve \(K_c\), so odd monomial moments vanish and
\[
\int_{K_c}\langle x,u\rangle^4\,dx
=A(c)\sum_{i=1}^3u_i^4+6B(c)\sum_{i<j}u_i^2u_j^2,
\]
where \(A(c)=J_{400}(c)\), \(B(c)=J_{220}(c)\). Because \(\|u\|_2^4=\sum_i u_i^4+2\sum_{i<j}u_i^2u_j^2\), equality (1) is equivalent to the one scalar equation \(A(c)=3B(c)\). Indeed when this holds, the quartic polynomial equals \(A(c)\|u\|_2^4\), while the spherical average of \(\langle x,u\rangle^4\) over unit \(u\) is \(\|x\|^4/5\). The same cubic symmetry makes the covariance matrix scalar for every \(c\). For \(1<c<2\), intersecting the six planes \(x_i=\pm1\) with the \(\ell_1\)-constraint gives six planar diamonds (squares), each with vertices along two coordinate directions at distance \(c-1\). Each of the eight signed planes \(\pm x_1\pm x_2\pm x_3=c\) gives a hexagonal facet whose six vertices are the corresponding signed permutations of \((1,c-1,0)\). These are all bounding facets, and their 24 distinct vertices give the asserted nonregular combinatorics at \(c_*\).

**2. Exact moments by simplex inclusion–exclusion.** It suffices to integrate over the nonnegative octant and multiply by eight. For any **even nonnegative** integer exponents \((a,b,d)\), inclusion–exclusion on the coordinate upper bounds \(x_i\le1\) gives, on each interval with fixed \(k=\lfloor c\rfloor\), a sum over subsets \(S\subseteq\{1,2,3\}\) with \(|S|\le k\):
\[
J_{a b d}(c)=8\sum_{\substack{S\subseteq\{1,2,3\}\\|S|\le k}}(-1)^{|S|}\sum_{0\le j_i\le a_i\;(i\in S)}
\left(\prod_{i\in S}\binom{a_i}{j_i}\right)
\frac{\prod_{i=1}^3 b_i!}{(b_1+b_2+b_3+3)!}
(c-|S|)^{b_1+b_2+b_3+3}.
\tag{4}
\]
Here \((a_1,a_2,a_3)=(a,b,d)\), \(b_i=j_i\) for \(i\in S\), and \(b_i=a_i\) otherwise. For \(c\) at an integer endpoint, the zero-volume limiting terms are harmless. Formula (4) follows by shifting \(x_i=y_i+1\) for the chosen forbidden coordinates and integrating each resulting monomial over the simplex \(y_i\ge0\), \(\sum_i y_i\le c-|S|\):
\[
\int y_1^{b_1}y_2^{b_2}y_3^{b_3}\,dy
=\frac{\prod_i b_i!}{(\sum_i b_i+3)!}(c-|S|)^{\sum_i b_i+3}.
\]
The equality is an elementary Dirichlet-beta integral, so no numerical approximation enters (4).

Write \(H(c)=A(c)-3B(c)\). On the first nontrivial interval \(1\le c\le2\), applying (4) yields
\[
\boxed{H(c)=-\frac2{105}\left(2c^7-21c^6+63c^5-35c^4-105c^3+147c^2-49c-3\right).}
\tag{5}
\]
On \(2\le c\le3\), the same calculation gives
\[
H(c)=\frac2{105}\left(c^7-21c^6+147c^5-455c^4+595c^3-63c^2-567c+403\right).
\tag{6}
\]
On \(0<c\le1\), direct octahedral scaling gives \(H(c)=2c^7/105>0\); on \(c\ge3\), independent uniform cube coordinates give \(H(c)=-16/15<0\).

**3. Existence and uniqueness on all positive parameters.** Substitution in (5) gives \(H(1)=2/105>0\) and \(H(2)=-2/7<0\), establishing a root in \((1,2)\). For \(z>0\), set \(c=(1+2z)/(1+z)\), which bijectively parametrizes \((1,2)\). Exact expansion gives
\[
(1+z)^7H\!\left(\frac{1+2z}{1+z}\right)
=\frac2{105}+\frac4{15}z+\frac85z^2+4z^3+4z^4
+\frac45z^5-\frac45z^6-\frac27z^7.
\tag{7}
\]
The displayed coefficient sequence has exactly one sign change. Descartes' sign rule therefore gives *at most one* positive root, while the endpoint sign change gives at least one. For \(2<c<3\), use instead \(c=(2+3z)/(1+z)\). The resulting numerator \((1+z)^7H(c)\) has coefficients in ascending powers of \(z\) equal to
\[
-\frac27,\ -\frac{16}5,\ -\frac{68}5,\ -\frac{88}3,
\ -\frac{104}3,\ -\frac{112}5,\ -\frac{112}{15},\ -\frac{16}{15},
\]
all strictly negative. Together with the outer regimes, this proves exactly one positive parameter. Repeated exact-sign rational bisection of (5) yields the stated decimal value.

**4. Nonisotropy at sixth order.** If a sixth moment tensor were rotationally isotropic, coefficient comparison in \(\int\langle x,u\rangle^6\,dx\) would force \(J_{600}=5J_{420}\). Inclusion–exclusion instead gives, on \([1,2]\),
\[
J_{600}(c)-5J_{420}(c)
=-\frac1{189}\left(4c^9-45c^8+180c^7-336c^6+252c^5+252c^4-840c^3+792c^2-270c+9\right).
\tag{8}
\]
Exact evaluation of (5) puts \(c_*\) in \((1699/1000,17/10)\). Substituting \(c=(a+bz)/(1+z)\) into (8), where \(a=1699/1000\), \(b=17/10\), and multiplying by \((1+z)^9\), produces a degree-nine polynomial whose **ten coefficients are all strictly negative** (verified exactly and reproducibly in `verify.py`). Since every \(z>0\) corresponds to a point in that bracket and the multiplier is positive, (8) is strictly negative at \(c_*\). This proves (3) without using a floating-point sign test.

## Verification
The standalone `verify.py` rebuilds the monomial moment polynomials from equation (4) with exact rational arithmetic, verifies equations (5), (7), the sign-definite transform on \((2,3)\), the root bracket, and the ten negative coefficients for the sixth-moment defect. It checks both boundary regimes and isolates the root by rational bisection. Running `python3 verify.py` requires only the Python standard library and prints `VERIFY_OK exact_moment_polynomials root_uniqueness fourth_isotropy sixth_anisotropy`. Independent two-dimensional numerical quadrature of the positive-octant section integral was also compared at parameters \(1.2\), \(c_*\), \(1.9\), and \(2.5\), with absolute differences below \(2\times10^{-8}\) for each fourth-moment monomial. These numerical checks are diagnostics, not the proof of the all-parameter claim.

## Relationship to prior work
The 2011 preprint of Gravin, Lasserre, Pasechnik and Robins establishes general direct and inverse polynomial moment formulas for arbitrary convex polytopes, not the existence or uniqueness of a fourth-isotropic member of this particular family. Gravin, Pasechnik and the Shapiros (2012) develop the generating-function theory of polytope moments but do not classify isotropic fourth moments along the cube–octahedron intersection path. Módis and Kovács (2024) examine the rotational invariance of moments of the **five regular Platonic solids**; their result that fourth moments of regular cubes and octahedra are anisotropic agrees with the endpoint signs here but does not forbid an intermediate, nonregular polytope from having an isotropic fourth tensor.

The published *Complete normalized quartic tensors of the five Platonic solids* likewise computes the regular-solid tensors but not the 24-vertex interpolation or its unique algebraic zero. The published *Sharp tetrahedral-volume profile in the cube–octahedron intersection family* studies the **same bodies**, but optimizes inscribed tetrahedron volume, a quantity that neither supplies nor bounds fourth-moment tensor components. Neither result implies (2) or (3). No theorem or exact table covering the present isotropic-transition claim was identified in the consulted sources; this absence does not constitute a definitive historical-priority guarantee.

## Limitations
Only uniform **volume** moments of the exact three-dimensional family defined here are analyzed. No claim is made for surface tensors, higher-dimensional cube–cross-polytope interpolations, nearby asymmetric deformations, or general fourth-isotropic polyhedra. The sixth-order obstruction is established only at the unique fourth-isotropic parameter. The computations are exact but have not been independently audited; unindexed historical inertia-moment tables may contain comparable special cases.

## References
1. N. Gravin, J. Lasserre, D. Pasechnik and S. Robins, *The inverse moment problem for convex polytopes*, arXiv:1106.5723, initial public submission June 28, 2011; later *Discrete & Computational Geometry* 48 (2012), 596–621; https://arxiv.org/abs/1106.5723 .
2. N. Gravin, D. V. Pasechnik, B. Shapiro and M. Shapiro, *On moments of a polytope*, arXiv:1210.3193, initial submission October 11, 2012; https://arxiv.org/abs/1210.3193 .
3. M. Módis and F. Kovács, *On rotational invariance of higher-order moments of regular polyhedra*, *Facta Universitatis: Architecture and Civil Engineering* 22 (2024), 15–22; DOI 10.2298/FUACE230630022M; https://doiserbia.nb.rs/ft.aspx?id=0354-46052300022M .
4. *Complete normalized quartic tensors of the five Platonic solids*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-normalized-quartic-tensors-of-the-five-platonic-solids--57af44c43405 .
5. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf .
