# Translated Takagi ellipses determine every planar antilinear constrained numerical annulus

## Finding

Let \(A\) be **any** conjugate-linear map on a two-dimensional complex Hilbert space. Given \(|q|\le1\), its constrained numerical range is the annulus obtained by radially rotating a single explicitly determined translated ellipse. In particular the complete inner radius, outer radius, and criterion for an omitted central disk follow from two-dimensional Euclidean geometry, including degenerate cases.

Write \(Ax=M\overline{x}\) in an orthonormal basis, let \(B=M^*\), and decompose \(B=S+K\), where \(S=(B+B^T)/2\) and \(K=(B-B^T)/2\). Choose a unitary \(V\) with
\[
 V^T S V=\operatorname{diag}(a,b),\qquad a\ge b\ge0,
 \qquad V^T K V=\begin{pmatrix}0&\kappa\\-\kappa&0\end{pmatrix}.
\]
Such a \(V\) exists by Takagi factorization. Put \(r=|q|\), \(\alpha=(1+r)/2\), \(\beta=(1-r)/2\), \(\tau=\sqrt{1-r^2}\),
\[
 h=\alpha a-\beta b,\quad v=\alpha a+\beta b,\quad c=\tau\kappa,
 \quad E_{h,v}=\{h\cos\theta+i v\sin\theta:\ 0\le\theta<2\pi\}_{\mathrm{filled}}.
\]
Here \(E_{h,v}\) is the closed filled ellipse with horizontal semiaxis \(h\) and vertical semiaxis \(v\); when \(h=0\) it is the corresponding vertical segment, and when \(v=0\) it is the singleton \(\{0\}\). Then
\[
\boxed{W_q(A)=\{z\in\mathbb C:\ L\le |z|\le U\},\quad L=\min_{w\in E_{h,v}}|w-c|,\quad U=\max_{w\in E_{h,v}}|w-c|.}
\]
The values do not depend on the choice of Takagi basis or on the argument of \(q\). Both extrema are attained; the boundary circles occur in \(W_q(A)\).

When \(h,v>0\), the annulus has a **nonempty central hole** precisely when
\[
\boxed{(\operatorname{Re}c/h)^2+(\operatorname{Im}c/v)^2>1.}
\]
For \(h=0<v\), the hole is absent exactly when \(\operatorname{Re}c=0\) and \(|\operatorname{Im}c|\le v\). For \(v=0\), it is absent exactly when \(c=0\). Thus these formulas include arbitrary nonsymmetric, nonisometric and singular conjugate-linear maps.

There is also an explicit sharp **outer-extremizer transition** when the skew coordinate \(\kappa\) is real. Set \(d=|c|\) and \(\Delta=v^2-h^2=(1-r^2)ab\). If \(\Delta>0\), then
\[
 L=(d-h)_+\!,\qquad
 U=\begin{cases}
 v\sqrt{1+d^2/\Delta},&dh\le\Delta,\\
 d+h,&dh\ge\Delta.
 \end{cases}
\]
Below the strict transition \(dh<\Delta\) with \(d>0\), two conjugate boundary points maximize the distance; above it \(dh>\Delta\), the unique maximizing point of the ellipse is the endpoint opposite \(c\). At equality the two maximizers coalesce. If \(\Delta=0\), then \(U=d+h\). If \(h=0\), the inner-radius identity above remains valid. If \(q=1\), then \(c=0\), \(E_{h,v}\) is a disk and \(W_q(A)\) is the disk of radius \(a\).

## Assumptions and scope

The Hilbert space has complex dimension exactly two, the inner product is linear in the first entry, and
\[
 W_q(A)=\{\langle Ax,y\rangle:\ \|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
No invertibility, normality, isometricity, or distinctness of Takagi values is assumed. In the displayed translated-ellipse formula, \(\min\) and \(\max\) concern ordinary Euclidean distance in the plane, **not** numerical-range optimizations. For nondegenerate ellipses the extremal distances require only a one-angle continuous calculation; zero-distance membership has the closed-form tests above.

## Proof

**Reduction to the real parameter.** Multiplying \(y\) by a unit complex scalar changes the phase of \(\langle x,y\rangle\) but not the modulus of \(\langle Ax,y\rangle\). Multiplying both \(x\) and \(y\) by the same scalar rotates the latter numerical value through twice the opposite phase while preserving the constraint. Consequently \(W_q(A)\) is radial and its radial bounds depend only on \(r=|q|\); it suffices to work with the real constraint \(r\).

**Bilinear reduction.** With \(B=M^*\), complex conjugation of \(\langle Ax,y\rangle\) yields \(x^TBy\). In a Takagi basis the matrices are \(S=\operatorname{diag}(a,b)\), \(K=\kappa\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). For any constrained unit vectors one has uniquely ordered orthonormal vectors \(u,w\) such that \(x=\sqrt\alpha\,u+\sqrt\beta\,w\) and \(y=\sqrt\alpha\,u-\sqrt\beta\,w\), up to harmless degeneracies at \(r=1\). Every unitary matrix with columns \(u,w\) has the form
\[
 [u\ \ w]=e^{i\gamma}\begin{pmatrix}z&-\overline\zeta\\\zeta&\overline z\end{pmatrix},\qquad |z|^2+|\zeta|^2=1.
\]
Since \(u^TKw=\kappa e^{2i\gamma}\), an exact expansion gives
\[
 x^TBy=e^{2i\gamma}\bigl(\alpha a z^2+\alpha b\zeta^2-\beta a\overline\zeta^2-\beta b\overline z^2-\tau\kappa\bigr).
\]
Writing \(z=\sqrt t e^{i\phi}\), \(\zeta=\sqrt{1-t}e^{i\psi}\), \(0\le t\le1\), the expression in parentheses is precisely
\[
 t\bigl(h\cos2\phi+i v\sin2\phi\bigr)
 +(1-t)\bigl(h_2\cos2\psi+i v_2\sin2\psi\bigr)-c,
\]
where \(h_2=\alpha b-\beta a\) and \(v_2=\alpha b+\beta a\).

**Filled-ellipse lemma.** Because \(|h_2|\le h\) and \(v_2\le v\), the second centered ellipse \(E_2\) lies inside \(E_{h,v}\). Its boundary and that of \(E_{h,v}\) are swept independently by \(\psi\) and \(\phi\). The set of all segments joining an arbitrary point of \(\partial E_2\) to an arbitrary point of \(\partial E_{h,v}\) is exactly the filled ellipse \(E_{h,v}\). To see the reverse inclusion, choose any \(p\) in the filled ellipse and any \(e\in\partial E_2\) different from \(p\); extend the ray from \(e\) through \(p\) until it hits \(\partial E_{h,v}\). The point \(p\) is on that segment. This argument also works for a degenerate segment, by choosing an endpoint of \(E_2\); if both ellipses are points, it is trivial. Hence the parenthesized bilinear values, as \(u,w\) vary, fill \(E_{h,v}-c\) **exactly**. The determinant phase \(e^{2i\gamma}\) independently rotates this set through every angle. Its modulus image is a closed interval because the filled ellipse is connected. Taking both extrema proves the annulus assertion.

**Hole criterion and extremizer bifurcation.** The inner radius vanishes if and only if \(c\in E_{h,v}\), giving the displayed inequalities and degenerate versions. If \(c\) is real and \(d=|c|\), the squared distance from the ellipse boundary is
\[
 v^2+d^2-\Delta\cos^2\theta-2dh\cos\theta
\]
(after reversing the horizontal coordinate if needed). For \(\Delta>0\), maximizing this concave quadratic for \(\cos\theta\in[-1,1]\) yields \(\cos\theta=-dh/\Delta\) while \(dh\le\Delta\), and \(\cos\theta=-1\) after the threshold. It gives the stated two formulas, their matching at equality, and the two-to-one maximizing-point transition. Convexity and axial symmetry make the minimum distance equal \((d-h)_+\). The \(\Delta=0\) and \(r=1\) cases follow directly.

## Verification

Run `python3 checker.py` using Python 3.9 or later (no third-party packages). The checker reconstructs constrained orthonormal vectors and the bilinear expression for many deterministic complex parameter cases, checks ellipse nesting and the exact parametrization, verifies explicit axial formulas against independently sampled boundary distances, tests zero-operator/skew-only and other degeneracies, and checks the quaternionic-root and antiunitary limits. Finite diagnostics verify algebra and examples; the proof above establishes the universal statement.

## Relationship to prior work

Majumdar and Müller (2026), in their treatment of real-linear constrained numerical ranges, establish the planar antilinear **annular shape** but do not give the full arbitrary-matrix Takagi-ellipse radius prescription or the axial bifurcation formula. Li and Tam (2000), including the congruence theory reviewed in their introduction and the two-dimensional skew-congruence discussion, treat related unitary-congruence orbits and convexity phenomena; their theorems do not explicitly give the overlap-constrained arbitrary-planar antilinear radii. The classical symmetric-\(C\) and skew-\(C\) congruence cases eliminate one of the two competing terms and cannot alone supply their coupled translation. The present result directly solves that coupled planar range. Previous specialized annuli for antiunitaries and conjugate-linear quaternionic roots are included as proper restricted families, not claimed anew.

## Limitations

The result concerns two complex dimensions and uses finite-dimensional Takagi factorization. It gives an exact two-dimensional geometric radius prescription, not generally a radicals-only formula for a complex off-axis translation. It does not imply formulas for arbitrary higher-dimensional real-linear operators. Although relevant current and historical sources were compared, a complete independent priority check against every historical congruence-matrix result has not been performed; some older texts remain inaccessible. No external independent mathematical audit has been performed.

## References

1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823 (first posted 12 October 2026), especially the discussion of antilinear \(q\)-numerical ranges.
2. C.-K. Li and T.-Y. Tam, *Numerical Ranges Arising from Simple Lie Algebras*, Canadian Journal of Mathematics **52** (2000), 141–171, doi:10.4153/CJM-2000-007-2.
3. R. C. Thompson, *The congruence numerical range*, Linear and Multilinear Algebra **8** (1980), 197–206, doi:10.1080/03081088008817318.
