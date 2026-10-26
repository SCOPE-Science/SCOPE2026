# Complete two-dimensional equality rigidity for the \(L^2\)-Cartesian numerical radius

## Finding
For every complex \(2\times2\) matrix \(T\), write \(T=H+iK\) with \(H=H^*\), \(K=K^*\), and define
\[
\Omega_2(T)^2=\frac1{2\pi}\int_0^{2\pi}\|H\cos\theta+K\sin\theta\|^2\,d\theta,
\qquad
w(T)=\max_{\|x\|=1}|\langle Tx,x\rangle|.
\]
Both sharp inequalities in the cited source have complete equality classifications in dimension two:
\[
\boxed{\ \Omega_2(T)^2=\tfrac14\|T^*T+TT^*\|
\quad\Longleftrightarrow\quad
\operatorname{tr}T=0\ \text{or}\ T=e^{i\phi}S\ (S=S^*)\ },
\]
where \(\phi\in\mathbb R\), and
\[
\boxed{\ \Omega_2(T)=w(T)\quad\Longleftrightarrow\quad T^2=0\ }.
\]
In particular, every traceless \(2\times2\) matrix satisfies the exact norm identity
\[
\Omega_2(T)=\tfrac12\|T\|_{\mathrm{HS}}.
\]
The zero matrix is included in both characterizations. Neither characterization is claimed in larger matrix sizes.

## Assumptions and scope
All vector norms are standard Euclidean norms on \(\mathbb C^2\), matrix operator norms are induced Hilbert norms, and \(\|\cdot\|_{\mathrm{HS}}\) denotes the Hilbert–Schmidt norm. No invertibility, normality, rank, or positivity is assumed. The source's lower bound concerns the operator sum \(T^*T+TT^*\), not the different estimate \(\Omega_2(T)^2\ge w(T)^2/2\).

## Proof
Let \(\sigma_1,\sigma_2,\sigma_3\) be the Hermitian Pauli matrices. Every \(T\in M_2(\mathbb C)\) has a unique representation
\[
T=(a+ib)I+(u+iv)\cdot\sigma,
\qquad a,b\in\mathbb R,\quad u,v\in\mathbb R^3.
\]
The identity \((q\cdot\sigma)^2=\|q\|^2I\) for real \(q\) gives, for \(s_\theta=a\cos\theta+b\sin\theta\) and \(q_\theta=u\cos\theta+v\sin\theta\),
\[
\|H\cos\theta+K\sin\theta\|=|s_\theta|+\|q_\theta\|.
\]
Its square integrates to
\[
\Omega_2(T)^2
=\frac{a^2+b^2+\|u\|^2+\|v\|^2}{2}
+2\Big\langle |s_\theta|\,\|q_\theta\|\Big\rangle,
\]
where brackets denote normalized angular average. The same Pauli identity gives
\[
H^2+K^2=(a^2+b^2+\|u\|^2+\|v\|^2)I+2(au+bv)\cdot\sigma,
\]
so
\[
\frac14\|T^*T+TT^*\|
=\frac{a^2+b^2+\|u\|^2+\|v\|^2}{2}+\|au+bv\|.
\]
Since \(2\langle s_\theta q_\theta\rangle=au+bv\), the triangle inequality for the average of vectors yields
\[
\|au+bv\|\le2\big\langle |s_\theta|\,\|q_\theta\|\big\rangle.
\]
If \(a=b=0\), then equality is immediate and \(\operatorname{tr}T=0\). Otherwise multiplication of \(T\) by a unimodular scalar rotates \((a,b)\), so assume \(a>0,b=0\). Equality in the vector-integral triangle inequality forces the vectors \(s_\theta q_\theta\) to lie on one fixed nonnegative ray for almost every \(\theta\), unless they all vanish. Dividing by \(a\cos^2\theta\), where \(\cos\theta\ne0\), forces the affine line
\[
u+v\tan\theta,\qquad \tan\theta\in\mathbb R,
\]
to lie on one fixed nonnegative ray. This is possible only if \(v=0\); indeed for \(v\ne0\), the affine line is unbounded in opposite directions. Thus the imaginary part of the rotated \(T\) is zero and \(T\) is a phase multiple of a Hermitian matrix. Conversely if \(v=0=b\), the integrand \(s_\theta q_\theta=a u\cos^2\theta\) lies on one nonnegative ray, giving equality. This proves the lower-bound classification.

If \(a=b=0\), the preceding averaged formula becomes
\(\Omega_2(T)^2=(\|u\|^2+\|v\|^2)/2=\|T\|_{\mathrm{HS}}^2/4\), proving the additional identity.

For the upper bound, the function
\[
f(\theta)=\|H\cos\theta+K\sin\theta\|=|s_\theta|+\|q_\theta\|
\]
is continuous and \(w(T)=\max_\theta f(\theta)\), so equality of its squared mean with its squared maximum holds exactly when \(f\) is constant. If \((a,b)\ne(0,0)\), take an angle \(\theta_0\) with \(s_{\theta_0}=0\). At that angle \(|s_\theta|\) has a strictly positive derivative jump. The summand \(\|q_\theta\|\) is differentiable there if \(q_{\theta_0}\ne0\); if \(q_{\theta_0}=0\), it also has a nonnegative upward derivative jump. Therefore \(f\) cannot be constant. Hence constant \(f\) requires \(a=b=0\). In that case
\[
f(\theta)^2=\|u\|^2\cos^2\theta+\|v\|^2\sin^2\theta+2(u\cdot v)\sin\theta\cos\theta
\]
is constant exactly when \(\|u\|=\|v\|\) and \(u\cdot v=0\). These two identities are equivalent to
\[
T^2=((\|u\|^2-\|v\|^2)+2i\,u\cdot v)I=0
\]
by the Pauli product identity. Conversely, if \(T^2=0\), these identities hold and \(f\) is constant. This establishes the upper-bound classification.

## Verification
The analytic proof applies to every complex \(2\times2\) matrix. Its integral-equality step uses finite-dimensional equality in the Euclidean triangle inequality, while the upper classification uses only continuity and a one-sided cusp argument. The independent checker `check_cartesian_M2.py` evaluates the original angular norm by \(4096\)-point quadrature on four families of \(300\) matrices each: traceless, phase-self-adjoint, unrestricted, and rank-one nilpotent. It verifies the relevant equality identities and inequalities to numerical tolerances. This finite sampling is not a substitute for the proof. It does not certify historical priority.

## Relationship to prior work
Audeh, Moradi, and Sahoo introduce \(\Omega_2\), prove both global inequalities, and show sharpness with sufficient examples; their Theorems 4, 5, and 17 do not provide the necessary two-dimensional equality criteria. An existing rank-one calculation derives \(\Omega_2\) as a function of normalized trace overlap for rank-one operators, including its two endpoint examples. That result does not determine the lower equality class at rank two, particularly the traceless invertible matrices, nor the complete upper equality criterion among all matrices. A separate stability result characterizes equality in the *other* comparison \(\Omega_2(T)^2\ge w(T)^2/2\), not equality in the operator-sum lower bound considered here. The older Cartesian-decomposition paper concerns the supremal numerical-radius representation, not the new integral functional. Thus the two classifications here are not direct implications of the inspected cited statements.

## Limitations
This is a two-dimensional equality classification, not a dimension-free theorem. The two-dimensional Pauli identity is essential; there may be other equality mechanisms in larger dimensions. The proofs use exact complex matrix algebra and no stochastic or symbolic computation. A search cannot exclude all unknown or differently named prior results, especially ones stated in terms of convex-support functions.

## References
1. W. Audeh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1, first posted 2026-10-04, Theorems 4, 5, 17.
2. *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius*, published mathematical research record dated 2026-10-11, identifier `2026/10/11/SCOPE-exact-rank-one-overlap-profile-for-the-l-2-cartesian-numerical-r--846b702b24b7`, RESULT.md.
3. *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, published mathematical research record dated 2026-10-11, identifier `2026/10/11/SCOPE-cubic-operator-norm-stability-for-the-l-2-cartesian-numerical-ra--ffd07fee0727`, RESULT.md.
4. F. Kittaneh, M. S. Moslehian, T. Yamazaki, *Cartesian decomposition and numerical radius inequalities*, Linear Algebra Appl. 471 (2015), 46–53, DOI:10.1016/j.laa.2014.12.016.
