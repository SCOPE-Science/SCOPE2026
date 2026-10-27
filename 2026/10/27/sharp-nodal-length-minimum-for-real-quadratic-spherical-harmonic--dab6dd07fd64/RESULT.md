# Sharp nodal-length minimum for real quadratic spherical harmonics

## Finding
For every nonzero real spherical harmonic of degree two on the unit sphere \(S^2\), the total nodal arclength \(L\) satisfies
\[
4\pi\sqrt{\frac23}\ \leq\ L\ \leq\ 4\pi.
\]
The **sharp lower bound** is attained precisely by zonal (uniaxial) quadratics, whose symmetric trace-free coefficient matrix has two equal eigenvalues. The upper bound, previously established in greater generality by Gichev, is attained precisely when that matrix has a zero eigenvalue. In the latter case the nodal set is a union of two great circles. Both equality statements are understood up to orthogonal rotations, nonzero real scaling, and the equality of nodal sets as unparameterized subsets.

An explicit one-variable integral computes the length for every eigenvalue ratio, and a paired-integrand inequality proves the minimum without assuming monotonicity of that integral.

## Assumptions and scope
Let \(A\in\operatorname{Sym}_3(\mathbb R)\setminus\{0\}\) satisfy \(\operatorname{tr}A=0\). Set \(Y_A(x)=x^{\mathsf T}Ax\) for \(x\in S^2\), and let \(L(A)=\mathcal H^1\{x\in S^2:Y_A(x)=0\}\), with the usual spherical metric. Every real degree-two spherical harmonic is uniquely of this form. The statements concern real, single-degree harmonics, not complex nodal sets, other degrees, or surfaces other than the unit two-sphere.

Up to rotation, replacing \(A\) by \(-A\), and positive scaling, each \(A\) has the form \(\operatorname{diag}(1,-a,-(1-a))\) with \(0\leq a\leq1/2\). The signs are harmless because the spectrum of a nonzero traceless symmetric matrix has both signs.

## Proof
**1. Great-circle intersection count.** Write \(Q_a(x,y,z)=x^2-a y^2-(1-a)z^2\). For a unit normal \(n\), restriction of \(Q_a\) to the plane \(n^\perp\) has determinant equal to \(n^{\mathsf T}\operatorname{cof}(A)n\), which is
\[
a(1-a)n_x^2-(1-a)n_y^2-a n_z^2.
\]
A generic great circle meets the zero set in four transverse points precisely when this determinant is negative, and otherwise meets it in no points. Tangent and identically zero restrictions form a measure-zero collection of normals; this remains true at \(a=0\). The spherical Crofton formula, with the unit sphere and normalized uniform normals, is \(L=\pi\,\mathbb E N\), where \(N\) is the number of intersection points counted without multiplicity for generic great circles. Hence
\[
L(a)=4\pi\Pr\{n^{\mathsf T}\operatorname{cof}(A)n<0\}.
\]

**2. Exact nodal-length profile.** Write \(n=(t,\sqrt{1-t^2}\cos\phi,\sqrt{1-t^2}\sin\phi)\). Here \(t\) is uniform on \([-1,1]\) and \(\phi\) uniform on \([0,2\pi)\), independently. Put \(s=a(1-a)\) and \(U=(1-a)\cos^2\phi+a\sin^2\phi\). The indefinite-plane condition is \(s t^2<U(1-t^2)\). Integrating over \(t\) gives the exact formula
\[
\frac{L(a)}{4\pi}=\frac1{2\pi}\int_0^{2\pi}\sqrt{\frac{U}{U+s}}\,d\phi.
\]
At \(a=0\), the integrand is \(1\) almost everywhere, yielding \(L(0)=4\pi\). At \(a=1/2\), it is identically \(\sqrt{2/3}\), yielding \(L(1/2)=4\pi\sqrt{2/3}\).

**3. Pointwise paired estimate.** Assume \(0<a\leq1/2\). Pair the integrand at \(\phi\) with its value at \(\phi+\pi/2\). Define \(d=1-2a\in[0,1)\), \(v=\cos 2\phi\), \(U_+=(1+dv)/2\), \(U_-=(1-dv)/2\), \(k=U_+U_-=(1-d^2v^2)/4\), and \(s=(1-d^2)/4\). Let \(p=\sqrt{U_+/(U_++s)}\), \(q=\sqrt{U_-/(U_-+s)}\). Set \(D=(U_++s)(U_-+s)=k+s+s^2\). Direct algebra gives
\[
p^2+q^2=\frac{2k+s}{D},\qquad pq=\sqrt{\frac{k}{D}}.
\]
The exact polynomial deficit identities are
\[
2k-s-4s^2=\frac{d^2(3-2v^2-d^2)}4\geq0,
\qquad
5k-4s(1+s)=\frac{d^2(6-5v^2-d^2)}4\geq0.
\]
Since \(0\leq d<1\) and \(|v|\leq1\), both right-hand sides are nonnegative, and are strictly positive whenever \(d>0\). Consequently \(p^2+q^2\geq4/3\) and \(pq\geq2/3\), whence
\[
\frac{p+q}{2}\geq\sqrt{\frac23}.
\]
Averaging in \(\phi\) establishes the sharp lower bound, with strict inequality for every \(0\leq a<1/2\) (the case \(a=0\) having been handled separately). Thus equality in the lower bound occurs exactly when \(a=1/2\), namely for matrices with a repeated eigenvalue.

**4. Upper equality.** Pointwise \(\sqrt{U/(U+s)}\leq1\), and it is strictly less than \(1\) for \(s>0\). Therefore \(L\leq4\pi\), with equality exactly when \(a=0\), or equivalently when the determinant of \(A\) vanishes. Then \(Q_0=x^2-z^2=(x-z)(x+z)\), and the two nodal great circles each contribute length \(2\pi\). The general upper inequality is prior work; the elementary derivation here also identifies its degree-two equality case.

## Verification
The accompanying `verify.py` uses exact symbolic simplification to check both polynomial identities in Step 3. It independently computes the one-dimensional Crofton integral and direct spherical-curve arclength at eight parameter values, including both endpoints, and compares the results. Run `python verify.py` with Python, SymPy and SciPy installed; its recorded stdout is included in `verification_output.txt`. Numerical quadrature is only a consistency test; the infinite family and equality classification follow from the preceding inequalities and the Crofton formula.

## Relationship to prior work
Gichev, *Some remarks on spherical harmonics* (arXiv:0705.2547), proves the general sharp upper bound \(L\leq2\pi\ell\) for nodal lengths of real degree-\(\ell\) harmonics on \(S^2\), and explicitly points to the zonal length as a possible sharp lower bound; the source's stated lower bound is weaker. The present claim is the exact sharp **degree-two lower bound and complete real equality classification**, not a new general upper estimate. Todino's study of nodal lengths of random spherical harmonics in shrinking domains (arXiv:1807.11787; first posted 2018-07-31) provides the middle-period literature context but does not assert a deterministic degree-two sharp minimum. Gichev's earlier publication is relevant historical context outside the chosen middle-period lead source.

## Limitations
The argument does not establish the zonal-minimization conjecture in degrees above two, nor monotonicity of \(L(a)\) in the eigenvalue parameter. The real matrix and the round two-sphere are essential to the proof. Novelty is a best-knowledge literature assessment, not an independent priority certification; unindexed equivalent formulas for spherical quadratic zero curves remain possible.

## References
- V. M. Gichev, *Some remarks on spherical harmonics*, arXiv:0705.2547 (first posted 2007-05-17), especially the nodal-length Crofton formula, general upper bound, and lower-bound discussion.
- A. P. Todino, *Nodal Lengths in Shrinking Domains for Random Eigenfunctions on the Sphere*, arXiv:1807.11787 (first posted 2018-07-31).
- D. Marinucci, M. Rossi, I. Wigman, *The Asymptotic Equivalence of the Sample Trispectrum and the Nodal Length for Random Spherical Harmonics*, arXiv:1705.05747 (first posted 2017-05-16), for further literature context rather than an implication of the present deterministic theorem.
