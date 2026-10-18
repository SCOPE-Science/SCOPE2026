# Exact affine roundness of triangular log-cosh projection levels

## Finding

Let \(K\subset\mathbb R^2\) be any nondegenerate triangle with centroid at the origin and Euclidean area \(V>0\). For every \(\beta>0\), form the Orlicz boundary functional
\[
\Phi_K(y)=\int_{\partial K} (x\cdot\nu_K(x))\log\cosh\!\left(\frac{y\cdot\nu_K(x)}{2x\cdot\nu_K(x)}\right)\,dS(x)
\]
(the integral is the sum over open edges), and let \(C_{K,\beta}=\{y:\Phi_K(y)\le\beta\}\). Define \(c=3\beta/(2V)\), and let \(\tau(c)>0\) be the unique solution of
\[
\log\cosh\tau+2\log\cosh(\tau/2)=c.
\]
The precise affine Banach–Mazur distance to a Euclidean disk is
\[
\boxed{d_{\mathrm{BM}}(C_{K,\beta},B_2^2)
=\frac{2\operatorname{arcosh}(e^{c/2})}{\sqrt3\,\tau(c)}.}
\]
If \(K=T K_\triangle\), where \(T\) is invertible and \(K_\triangle\) is the equilateral triangle centered at its centroid with inradius \(1\), the **unique** John and Löwner ellipses of \(C_{K,\beta}\) are respectively
\[
T\bigl(2\tau(c) B_2^2\bigr),\qquad
T\left(\frac4{\sqrt3}\operatorname{arcosh}(e^{c/2}) B_2^2\right).
\]
In the equilateral reference frame, the six John contacts point along the inward/outward edge normals and the six Löwner contacts along their angular bisectors; no other contacts occur. The shape factor is strictly between \(1\) and \(2/\sqrt3\), with exact endpoint behavior
\[
d_{\mathrm{BM}}=1+\frac{2}{405}c^2+O(c^3)\quad(c\downarrow0),
\qquad d_{\mathrm{BM}}=\frac2{\sqrt3}\left(1-\frac{\log2}{c}+O(c^{-2})\right)\quad(c\to\infty).
\]
In particular, its first departure from Euclidean roundness is **quadratic in the level**, because the two angular extremal values agree through degree four and first differ in degree six.

## Assumptions and scope

A triangle is centered by translating its centroid to the origin before defining \(\Phi_K\). The origin then lies strictly inside \(K\), so the denominators in the facet functional are positive. The level \(\beta\) is any positive real number. The primary case of the 2026 log-cosh construction is \(\beta=1\); the all-level family is included because it gives a natural exact affine shape profile. The 2026 smooth-covariogram convergence theorem assumes a \(C^3\) boundary and therefore cannot directly be asserted for polygons. The present assertions concern the well-defined facet integral and also the Hausdorff limits of its bodies for smooth convex approximations, not an unproved direct covariogram limit for polygonal \(K\).

For a centered equilateral reference triangle with inradius \(r>0\), choose its three outward unit edge normals \(u_j=(\cos(2\pi j/3),\sin(2\pi j/3))\), for \(j=0,1,2\). Every centered triangle is a nonsingular linear image of such a reference triangle. Its John ellipse means the unique maximal-area ellipse it contains; its Löwner ellipse means the unique minimal-area containing ellipse. The Banach–Mazur distance is the infimum of \(\lambda\ge1\) over ellipses \(E\) such that \(E\subseteq C\subseteq\lambda E\), allowing general invertible affine coordinates.

## Proof

**1. Facet reduction and affine covariance.** An equilateral triangle of inradius \(r\) has area \(V=3\sqrt3\,r^2\); each edge has length \(2\sqrt3\,r\) and support distance \(r\). Thus each facet contributes \(2V/3\) times a single log-cosh term. Writing \(y=2rt(\cos\theta,\sin\theta)\),
\[
\Phi_K(y)=\frac{2V}{3}F_t(\theta),\qquad
F_t(\theta)=\sum_{j=0}^2\log\cosh\bigl(t\cos(\theta-2\pi j/3)\bigr).
\]
For any nonsingular linear map \(T\), the facet identity \((x\cdot\nu)dS\mapsto|\det T|(x\cdot\nu)dS\) and the transformed normal ratio give
\[
\Phi_{TK}(y)=|\det T|\,\Phi_K(T^{-1}y).
\]
Therefore \(C_{TK,\beta}=T C_{K,\beta/|\det T|}\), and the dimensionless level \(c=3\beta/(2\operatorname{area}K)\) is invariant under this transformation.

**2. Exact angular extrema at every positive radius.** Set \(x_j=\cos(\theta-2\pi j/3)\). Then \(\sum x_j=0\), \(\sum x_j^2=3/2\), and
\[
x_j^3=A x_j+B,\qquad A=3/4,\qquad B=\tfrac14\cos3\theta.
\]
Let \(P_m=\sum_j x_j^m\). Its initial data are \(P_0=3\), \(P_1=0\), \(P_2=2A\), with recurrence
\[
P_m=A P_{m-2}+B P_{m-3}\qquad(m\ge3).
\]
Induction shows that every coefficient of \(P_m\), when regarded as a polynomial in the formal nonnegative variable \(A\) and formal variable \(B\), is nonnegative. Its nonzero monomials have weighted degree \(2a+3b=m\); hence for every even \(m\) only even powers of \(B\) occur. Moreover \(P_6=2A^3+3B^2\). Consequently, for every \(t>0\),
\[
\sum_{j=0}^2\cosh(2t x_j)=\sum_{k\ge0}\frac{(2t)^{2k}}{(2k)!}P_{2k}
\]
is a **strictly increasing function of \(B^2\)** on \([0,1/16]\). Termwise use is legitimate because the series is absolutely convergent for fixed \(t\). Since \(\sum x_j=0\), the product-to-sum identity gives
\[
\prod_{j=0}^2\cosh(t x_j)=\frac{1+\sum_j\cosh(2t x_j)}4.
\]
Taking logarithms shows that \(F_t(\theta)\) has exactly its maxima when \(|\cos3\theta|=1\), and exactly its minima when \(\cos3\theta=0\). Their values are
\[
M(t)=\log\cosh t+2\log\cosh(t/2),\qquad
m(t)=2\log\cosh(\sqrt3\,t/2).
\]
In particular \(M(t)>m(t)\) for every \(t>0\), with no angular phase transition.

**3. Exact John and Löwner circles in the reference frame.** Both \(M\) and \(m\) are continuous, strictly increasing from zero to infinity. The farthest radial point in \(\{F_t(\theta)\le c\}\) therefore occurs exactly at an angular minimum of \(F_t\), and the largest centered inscribed radius occurs exactly at an angular maximum. Hence
\[
r_J=2r\,M^{-1}(c)=2r\tau(c),\qquad
r_L=2r\,m^{-1}(c)=\frac{4r}{\sqrt3}\operatorname{arcosh}(e^{c/2}).
\]
The body has dihedral sixfold symmetry, because its defining functional is even and invariant under rotations of \(2\pi/3\). Uniqueness of the maximal contained and minimal containing ellipses forces both to be centered disks: a positive-definite quadratic form commuting with a rotation by \(\pi/3\) is a scalar matrix. This proves the ellipse formulas and all asserted six-point contact sets; nonsingular linear covariance proves the statements for every centered triangle.

**4. Optimal affine (not merely concentric-circle) distortion.** Suppose a centrally symmetric convex body \(C\) is invariant under the sixfold rotation group and an ellipse \(E_A=\{x:x^TAx\le1\}\) satisfies \(E_A\subseteq C\subseteq\lambda E_A\). Rotate this pair by each of the six symmetries and average the six positive-definite matrices \(A_j\) to obtain \(\bar A\), which is scalar. The outer inclusions survive averaging because \(x^TAx\) is linear in \(A\). The inner inclusions also survive: \(h_{E_A}(u)^2=u^TA^{-1}u\), and \(A\mapsto u^TA^{-1}u=\sup_z\{2u\cdot z-z^TAz\}\) is convex. Therefore the disk \(E_{\bar A}\) remains inside \(C\), and \(C\subseteq\lambda E_{\bar A}\). A disk fitting between \(C\)'s sharp inner and outer disks requires \(\lambda\ge r_L/r_J\). This factor is attained by the John disk, so it equals the Banach–Mazur distance. Affine invariance transfers the conclusion to arbitrary centroid-centered triangles.

**5. Strict shape bounds and sharp asymptotics.** The strict angular extremum inequality gives \(r_L>r_J\), so the distance exceeds \(1\). To see that it is always smaller than \(2/\sqrt3\), let \(a=\operatorname{arcosh}(e^{c/2})\), whence \(\log\cosh a=c/2\). The identity \(\cosh a=2\cosh^2(a/2)-1>\cosh^2(a/2)\) gives \(M(a)=c/2+2\log\cosh(a/2)<c\); therefore \(\tau(c)>a\) and \(r_L/r_J<2/\sqrt3\). Taylor expansion gives
\[
M(t)=\tfrac34t^2-\tfrac3{32}t^4+\tfrac{11}{480}t^6+O(t^8),\qquad
m(t)=\tfrac34t^2-\tfrac3{32}t^4+\tfrac3{160}t^6+O(t^8).
\]
Thus \(M(t)-m(t)=t^6/240+O(t^8)\). At the common level \(c\), the two inverse arguments differ by \(t^5/360+O(t^7)\), and \(t^2=4c/3+O(c^2)\). Dividing the inverse radii yields \(r_L/r_J=1+2c^2/405+O(c^3)\). As \(t\to\infty\),
\[
M(t)=2t-3\log2+O(e^{-t}),\qquad
m(t)=\sqrt3\,t-2\log2+O(e^{-\sqrt3 t}),
\]
which yields the displayed large-level asymptotic and the sharp limiting factor \(2/\sqrt3\).

**6. Smooth approximation interpretation.** Let \(K_j\) be smooth strictly convex centered bodies converging to the centered triangle \(K\) in Hausdorff distance, retaining a common interior disk. Their support functions converge uniformly, and their surface-area measures converge weakly. Writing \(\Phi\) as an integral on the unit circle against those measures, the integrand \(h\log\cosh((y\cdot u)/(2h))\) is uniformly continuous for \(y\) bounded and \(h\) bounded away from zero. Hence \(\Phi_{K_j}\to\Phi_K\) locally uniformly, and strict radial increase plus coercivity imply Hausdorff convergence \(\{\Phi_{K_j}\le\beta\}\to C_{K,\beta}\). This statement concerns the iterated smooth-body transition construction and does not exchange the polygonal approximation limit with the smoothed-covariogram limit.

## Verification

The standalone `check.py` uses exact rational recurrences for the sixth power sum, verifies the radial formulas by inversion, and numerically evaluates 16,209 angular samples at nine radial scales. It recorded maximum angular-envelope excess \(7.11\times10^{-15}\), consistent with roundoff, and no failed assertions. Its finite tests are supplementary; the analytic nonnegative-coefficient argument is the proof for every angle and scale. The asymptotic coefficients follow from the expansions in step 5 and do not rely on numerical fitting.

For the equilateral triangle with inradius \(1\), the primary level \(\beta=1\) has \(c=1/(2\sqrt3)\), \(r_J\approx1.270359021574\), \(r_L\approx1.270859874980\), and affine distance \(\approx1.000394261306\).

## Relationship to prior work

Haddad, Jiménez and Resende (2026) introduce the smooth covariogram and prove the critical \(\log\cosh\) transition formula for \(C^3\) convex boundaries. The present theorem extracts the complete equilateral/affine-triangle shape profile from that functional, fixes the six contact directions without assumptions on the level, proves the sharp quadratic departure from roundness, and establishes optimality among **all affine ellipses**, not just concentric circles. The source's transition theorem is not invoked for a nonsmooth triangle.

The earlier general Orlicz projection-body framework of Lutwak, Yang and Zhang (2010) motivates the functional class but no specifically verified formula from that paper is used. Related exact projection-body computations on parallelotopes rely on orthogonal facet directions and do not imply the three-normal angular extremum theorem here. General uniqueness and symmetry facts for extremal ellipses are standard and are reproved or explicitly justified as needed.

## Limitations

The origin must be the triangle's centroid; using a different origin alters the support-distance weights. The results are specific to the \(\log\cosh\) Orlicz kernel. They do not assert a direct covariogram limit for a nonsmooth triangle, nor determine geometric quantities such as the area of a general level body. The numerical checker is finite and cannot establish the infinite angular claim independently. The earliest Orlicz projection-body primary literature was not fully accessible, leaving a historical-priority risk despite the distinct exact statement and comparisons.

## References

1. J. Haddad, C. H. Jiménez and M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (first public submission 2026-10-08), https://arxiv.org/html/2610.11700v1.
2. E. Lutwak, D. Yang and G. Zhang, *Orlicz projection bodies*, Advances in Mathematics **223** (2010), 220–242, https://doi.org/10.1016/j.aim.2009.08.002.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, expanded edition, Cambridge University Press, 2014 (standard support functions, area measures and ellipsoid results).
