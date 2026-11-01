# Sharp quadrupole conditioning on paired spherical latitude rings

## Finding
Stable recovery of quadrupolar spherical modes from two cyclic sensor rings depends on the smallest and largest singular values of the exactly degree-two evaluation map. The ring height is the natural scalar design variable, while the relative rotation and ring population could in principle change the optimum.

Let \(m\ge5\) be an integer, \(0<h<1\), and \(\delta\in\mathbb R\). Consider the \(2m\) equally weighted samples
\[
X_{m,h,\delta}=\left\{\left(r\cos\frac{2\pi j}{m},r\sin\frac{2\pi j}{m},h\right),\ \left(r\cos\left(\frac{2\pi j}{m}+\delta\right),r\sin\left(\frac{2\pi j}{m}+\delta\right),-h\right):0\le j<m\right\},\qquad r=\sqrt{1-h^2}.
\]
Let \(E:\mathcal H_2(S^2)\to\mathbb C^{2m}\) evaluate every complex spherical harmonic of **exactly** degree \(2\), with orthonormal domain basis for the standard area measure on \(S^2\) and the usual unweighted Euclidean norm on sample values. Set \(u=h^2\). The full spectrum of \(E^*E\) is
\[
\frac{5m}{8\pi}\{A(u)\ [1],\ B(u)\ [2],\ C(u)\ [2]\},\qquad A(u)=(3u-1)^2,\quad B(u)=6u(1-u),\quad C(u)=\frac32(1-u)^2,
\]
where bracketed numbers are multiplicities. In particular the spectrum is **independent of the relative ring rotation** \(\delta\), and the evaluation map has rank \(5\) unless \(u=1/3\), when its rank is \(4\).

Its least possible squared spectral condition number, over all such heights and rotations, is
\[
\boxed{\min_{0<h<1,\ \delta\in\mathbb R}\kappa_2(E)^2=\frac{5+\sqrt{21}}4},\qquad
\boxed{h^2=\frac{6-\sqrt{21}}{15}}.
\]
The optimal **height is unique**; every ring rotation is optimal. At this height the smaller Gram eigenvalue has multiplicity three and the larger has multiplicity two. At the singular latitude \(u=1/3\), the condition number is infinite. The result applies in particular to the usual half-step antiprismatic offset \(\delta=\pi/m\), but does not require equilateral antiprism edges.

## Assumptions and scope
The sampling points lie on the unit sphere and are distinct for \(0<h<1\). Harmonic degree is exactly two, rather than the band-limited sum of degrees zero through two. The five basis functions use the standard unit \(L^2(S^2,d\omega)\) normalization, with total area \(4\pi\). There is no reweighting of individual samples; a common positive weight does not change the condition number. The integer restriction \(m\ge5\) prevents aliasing among the five azimuthal orders \(-2,-1,0,1,2\). No claim about arbitrary unequal ring weights, nonuniform longitudes, or higher degrees is made.

## Proof
Write \(w=x+iy\) on the sphere. One orthonormal complex basis, ordered by azimuthal indices \(-2,-1,0,1,2\), is
\[
\sqrt{\frac{15}{32\pi}}\bar w^2,\quad
\sqrt{\frac{15}{8\pi}}z\bar w,\quad
\sqrt{\frac5{16\pi}}(3z^2-1),\quad
-\sqrt{\frac{15}{8\pi}}zw,\quad
\sqrt{\frac{15}{32\pi}}w^2.
\]
(Only immaterial signs distinguish this from other standard conventions.) For each ring and every integer \(d\) with \(0<|d|\le4\),
\[
\sum_{j=0}^{m-1} e^{2\pi i jd/m}=0.
\]
Thus columns indexed by different azimuthal orders are orthogonal, separately on each ring. The additional longitude phase \(\delta\) does not affect that conclusion or any column norm. The two rings have identical squared column norms because changing \(z=h\) to \(z=-h\) changes only signs of odd powers. Summing norms over all \(2m\) samples yields exactly the five eigenvalues stated in the Finding, including their multiplicities. On \(0<u<1\), \(B(u)\) and \(C(u)\) are strictly positive while \(A(u)=0\) precisely at \(u=1/3\), proving the rank assertion.

For a full-rank map, its squared condition number is
\[
R(u)=\frac{\max\{A(u),B(u),C(u)\}}{\min\{A(u),B(u),C(u)\}}.
\]
Put \(u_*=(6-\sqrt{21})/15\), the smaller root of \(15u^2-12u+1=0\), and \(R_*=(5+\sqrt{21})/4\). At \(u_*\) one has \(A=B>0\), \(C>A\), and
\[
R(u_*)=\frac{C(u_*)}{B(u_*)}=\frac{1-u_*}{4u_*}=R_*.
\]
We prove strict optimality everywhere else. For \(0<u<u_*\),
\[
R(u)\ge\frac{C(u)}{B(u)}=\frac{1-u}{4u}>R_*.
\]
For \(u_*<u<1/3\),
\[
R(u)\ge\frac{C(u)}{A(u)}=\frac{3(1-u)^2}{2(1-3u)^2}>\frac{C(u_*)}{A(u_*)}=R_*;
\]
the middle quotient increases strictly on \((0,1/3)\). At \(u=1/3\) the map is singular. For \(1/3<u\le2/5\), \(A(u)\le1/25\) and \(B(u)\ge4/3\), so \(R(u)\ge B/A\ge100/3>R_*\). Finally, for \(2/5\le u<1\),
\[
R(u)\ge\frac{B(u)}{C(u)}=\frac{4u}{1-u}\ge\frac83>R_*.
\]
These cases cover every admissible height and prove global sharpness and uniqueness of \(u_*\). Rotation-independence has already been established at the Gram-matrix level.

## Verification
The standalone `verify_quadrupole.py` uses only the Python 3 standard library and independently constructs all five normalized degree-two complex spherical harmonics in Cartesian coordinates. It sums the complete numerical Gram matrix for six ring sizes, three relative phases, and ten heights, including the extremal and singular heights. All \(180\) tests of the five diagonal values and twenty off-diagonal zeros passed at absolute tolerance \(2\cdot10^{-11}\). A separate \(9{,}999\)-height scan corroborated the sharp bound. Run with `python verify_quadrupole.py` in the extracted package directory. These finite floating-point checks are corroborative; the preceding exact orthogonality and inequality proof establishes the theorem for all admissible parameters.

## Relationship to prior work
Khalid, Kennedy, and McEwen's spherical sampling study (first public 19 March 2014) develops stable numerical transforms using latitude rings and analyzes the conditioning of band-limited transform submatrices. Khalid and Kennedy's subsequent latitude-placement study investigates optimized ring locations numerically for full band-limited transforms. Both supply motivation for optimizing latitude, but their inspected results address differing sampling patterns and objectives. They do not give the present five-eigenvalue formula, its independence of ring twist, or the unique radical minimizer for the exact degree-two frame. The basic spherical-harmonic orthogonality is classical; the contribution claimed here is the closed sharp restricted-design solution, not those standard identities.

## Limitations
The statement concerns exactly one harmonic degree on two equally populated mirror-symmetric rings. It is not an optimal-dimensionality sampling theorem for arbitrary band limits, nor an assertion about global optimality among unrestricted point sets. The originality comparison is bounded rather than exhaustive, and equivalent formulas in specialized acoustics or spherical array-design publications remain a possible prior-art risk. Independent mathematical review has not been performed.

## References
1. Z. Khalid, R. A. Kennedy, and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (first submitted 2014-03-19), https://arxiv.org/html/1403.4661v2 ; https://arxiv.org/abs/1403.4661 .
2. Z. Khalid and R. A. Kennedy, *On the Placement of Latitudes in Iso-Latitude Optimal-Dimensionality Sampling Schemes on the Sphere* (2014 conference text), https://www.zubairkhalid.org/papers/C17.pdf .
3. Standard normalized degree-two spherical harmonic formulas; the normalization and complete algebraic computation are reproduced in the proof and standalone checker, so no external table is needed.
