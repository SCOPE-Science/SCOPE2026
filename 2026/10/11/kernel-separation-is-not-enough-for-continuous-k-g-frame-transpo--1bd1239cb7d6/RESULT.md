# Kernel separation is not enough for continuous \(K\)-\(g\)-frame transport

## Finding
Theorem 2.1 of Alizadeh--Rahmani asserts that a continuous \(K\)-\(g\)-frame \(\{\Lambda_\omega}\) remains a continuous \(K\)-\(g\)-frame after right composition by \(U^*\) whenever \(U\) has closed range, \(UK=KU\), and
\[
R(K^*)\cap N(U^*)=\{0\}.
\]
That condition is insufficient. The theorem can fail even when \(U\) is a norm-one partial isometry and the original continuous \(K\)-\(g\)-frame is Parseval.

More precisely, for \(K\ne0\) and \(UK=KU\), define
\[
\delta(U,K)=\inf\{\|U^*x\|:x\in R(K^*),\ \|x\|=1\}.
\]
Right composition \(\{\Lambda_\omega}\mapsto\{\Lambda_\omega U^*}\) preserves every continuous \(K\)-\(g\)-frame exactly when \(\delta(U,K)>0\). If \(\{\Lambda_\omega}\) has bounds \(A,B\), then
\[
A\delta(U,K)^2\|K^*f\|^2
\le
\int_\Omega\|\Lambda_\omega U^*f\|^2\,d\mu(\omega)
\le
B\|U\|^2\|f\|^2.
\]

## Assumptions and scope
Let
\[
H=\ell^2(\mathbb N;\mathbb C^2).
\]
In the \(n\)-th copy of \(\mathbb C^2\), let \(e_n\) and \(h_n\) denote the first and second coordinate unit vectors. Set
\[
\lambda_n=\frac1{n+1},\qquad
 a_n=\sqrt{1-\lambda_n^2},
\]
and define \(U\) blockwise by
\[
Ue_n=\lambda_ne_n,
\qquad
Uh_n=a_ne_n.
\]
Equivalently,
\[
U_n=
\begin{pmatrix}
\lambda_n&a_n\\
0&0
\end{pmatrix}.
\]
Put \(K=U\). Take \(\Omega\) to be a one-point measure space of mass one, take the coefficient Hilbert space to be \(H\), and let the sole analysis operator be
\[
\Lambda=K^*=U^*.
\]
This is a legitimate continuous \(K\)-\(g\)-frame model: measurability is automatic on a one-point space.

## Proof
For every \(n\), the row \((\lambda_n,a_n)\) has Euclidean norm one. Hence each block \(U_n\) has norm one and
\[
U_nU_n^*=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Therefore \(U\) is a norm-one partial isometry whose range is the closed first-coordinate subspace
\[
R(U)=\overline{\operatorname{span}}\{e_n:n\ge1\}.
\]
Its adjoint satisfies
\[
U^*e_n=\lambda_ne_n+a_nh_n,
\qquad
U^*h_n=0.
\]
The vectors
\[
v_n=\lambda_ne_n+a_nh_n
\]
form an orthonormal sequence, so
\[
R(U^*)=\overline{\operatorname{span}}\{v_n:n\ge1\}
\]
is closed. Also
\[
N(U^*)=\overline{\operatorname{span}}\{h_n:n\ge1\}.
\]
Because every \(\lambda_n\) is nonzero, a vector \(\sum_nc_nv_n\) can lie in \(N(U^*)\) only if every \(c_n=0\). Thus
\[
R(K^*)\cap N(U^*)=R(U^*)\cap N(U^*)=\{0\}.
\]
The commutation hypothesis is automatic because \(K=U\).

The one-point family \(\Lambda=K^*\) is Parseval relative to \(K\): for every \(f\in H\),
\[
\|\Lambda f\|^2=\|K^*f\|^2\le\|f\|^2.
\]
Thus it has lower and upper bounds \(A=B=1\).

However,
\[
(U^*)^2e_n
=U^*v_n
=\lambda_nv_n.
\]
Consequently
\[
\|K^*e_n\|=\|v_n\|=1,
\qquad
\|\Lambda U^*e_n\|=\|(U^*)^2e_n\|=\lambda_n\longrightarrow0.
\]
No positive constant \(C\) can satisfy
\[
C\|K^*f\|^2\le\|\Lambda U^*f\|^2
\]
for all \(f\in H\). Hence the transformed family is not a continuous \(K\)-\(g\)-frame.

The exact universal repair is immediate from the commutation relation. If \(\delta(U,K)>0\) and \(\{\Lambda_\omega}\) has lower bound \(A\), then
\[
\begin{aligned}
\int_\Omega\|\Lambda_\omega U^*f\|^2\,d\mu(\omega)
&\ge A\|K^*U^*f\|^2\\
&=A\|U^*K^*f\|^2\\
&\ge A\delta(U,K)^2\|K^*f\|^2.
\end{aligned}
\]
The upper bound is
\[
\int_\Omega\|\Lambda_\omega U^*f\|^2\,d\mu(\omega)
\le B\|U\|^2\|f\|^2.
\]
Conversely, if right composition by \(U^*\) preserves every continuous \(K\)-\(g\)-frame, apply it to the one-point family \(\Lambda=K^*\). The resulting lower frame inequality is exactly
\[
\|U^*K^*f\|\ge c\|K^*f\|
\]
for some \(c>0\), which says \(\delta(U,K)>0\).

Finally, if \(U\) has closed range and
\[
R(K^*)\subseteq R(U),
\]
then for \(x\in R(K^*)\),
\[
x=UU^\dagger x,
\]
so
\[
\|x\|
=\|(U^\dagger)^*U^*x\|
\le\|U^\dagger\|\,\|U^*x\|.
\]
Hence \(\delta(U,K)\ge\|U^\dagger\|^-1\), recovering the numerical lower bound claimed in the source under a genuinely sufficient range hypothesis.

## Verification
The target theorem was read in the journal PDF. It explicitly assumes closed range of \(U\), commutation \(UK=KU\), and the intersection condition \(R(K^*)\cap N(U^*)=\{0\}\), and it claims lower bound \(A\|U^\dagger\|^-2\). Its proof begins the critical estimate with
\[
\|K^*f\|^2=\|UU^\dagger K^*f\|^2.
\]
But \(UU^\dagger\) is the orthogonal projection onto \(R(U)\), so this identity requires \(K^*f\in R(U)\) for every \(f\), equivalently \(R(K^*)\subseteq R(U)\). The stated intersection condition does not provide that inclusion.

For the displayed block construction, each \(U_n\) has singular values \(1\) and \(0\), so the direct sum has norm one and closed range. The adjoint-range vectors \(v_n\) are unit vectors and satisfy
\[
U^*v_n=\lambda_nv_n,
\]
with \(\lambda_n\to0\). This gives an exact symbolic obstruction; no finite computation is used to infer failure of the infinite lower frame bound.

The universal criterion is proved in both directions. The forward direction is the continuous \(K\)-\(g\)-frame lower inequality plus commutation, and necessity is obtained by the canonical one-point test family \(\Lambda=K^*\).

## Relationship to prior work
The 2019 paper *Continuous \(K\)-\(g\)-Frames in Hilbert Spaces* supplies the standard definition and operator characterization used by the target article. The 2021 preprint *Some points on c-K-g-frames and their duals* by the same authors develops range-factorization, duality, and atomic-system characterizations; its Theorem 2.1 is a different factorization theorem and does not state the transport result corrected here.

The closest indexed research records found in the overlap search concern closed-range reconstruction for \(K\)-frames, unbounded diagonal scaling, compact perturbations, and other range phenomena. They do not state the target theorem's block partial-isometry counterexample or the exact universal criterion \(\delta(U,K)>0\).

## Limitations
The accepted claim concerns the specific transport operation \(\{\Lambda_\omega}\mapsto\{\Lambda_\omega U^*}\) under the commutation hypothesis \(UK=KU\). It does not classify transformations when commutation is absent. The sufficient range replacement \(R(K^*)\subseteq R(U)\) is not asserted to be necessary; the exact universal condition is bounded-below behavior of \(U^*\) on \(R(K^*)\).

A residual literature risk remains that an unindexed erratum, thesis remark, or informal note may have observed the same source-specific defect.

## References
1. E. Alizadeh and M. Rahmani, *Construction Methods and Sum of c-K-g-Frames in Hilbert Spaces*, Journal of Mathematical Extension 17 (2023), article 3, DOI 10.30495/JME.2023.2199. First public journal posting verified as 5 July 2022.
2. M. Rahmani and E. Alizadeh, *Some points on c-K-g-frames and their duals*, arXiv:2106.07230v1, 14 June 2021.
3. E. Alizadeh, A. Rahimi, E. Osgooei, and M. Rahmani, *Continuous K-g-Frames in Hilbert Spaces*, Bulletin of the Iranian Mathematical Society 45 (2019), 1091--1104, DOI 10.1007/s41980-018-0186-7.
