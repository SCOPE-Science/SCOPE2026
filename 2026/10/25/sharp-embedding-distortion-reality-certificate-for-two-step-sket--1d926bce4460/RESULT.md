# Sharp embedding-distortion reality certificate for two-step sketched symmetric Lanczos

## Finding
For a real symmetric matrix, the sketched two-step Lanczos reduced matrix can acquire conjugate nonreal eigenvalues even when the sketch preserves squared norms on the entire three-dimensional space needed for the computation. A sharp deterministic certificate uses only the two consecutive Lanczos off-diagonal coefficients. For an embedding of distortion \(0\le\varepsilon<1\), the imaginary part of every sketched Ritz value is bounded by
\[
|\operatorname{Im}\lambda|\le \sqrt{\left[a\left(\frac{b\varepsilon}{\sqrt{1-\varepsilon^2}}-a\right)\right]_+},
\qquad [x]_+=\max\{x,0\}.
\]
When \(b>0\), all such reduced eigenvalues are real for \(\varepsilon\le a/\sqrt{a^2+b^2}\). The numerical bound and the uniform threshold are attained by three-dimensional positive-definite systems. At the threshold the extremal reduced matrix has a defective repeated eigenvalue; above it the maximal imaginary part is strictly positive.

## Assumptions and scope
Let \(n\ge2\), \(A\in\mathbb R^{n\times n}\) be real symmetric and \(v_1\) a Euclidean unit vector. Put
\[
\alpha=v_1^{\mathsf T}Av_1,\quad a=\|Av_1-\alpha v_1\|_2>0,\quad v_2=(Av_1-\alpha v_1)/a,
\]
\[
\beta=v_2^{\mathsf T}Av_2,\quad r=Av_2-av_1-\beta v_2,\quad b=\|r\|_2\ge0.
\]
Here \(r\) is orthogonal to both Lanczos vectors. Write \(V=[v_1,v_2]\) and \(\mathcal U=\operatorname{span}\{v_1,v_2,r\}\). Suppose a *real* sketch matrix \(S\in\mathbb R^{s\times n}\) obeys
\[
(1-\varepsilon)\|z\|_2^2\le\|Sz\|_2^2\le(1+\varepsilon)\|z\|_2^2\quad(z\in\mathcal U),\qquad 0\le\varepsilon<1.
\]
The two-by-two sketched Rayleigh--Ritz matrix is
\[
H=((SV)^{\mathsf T}(SV))^{-1}(SV)^{\mathsf T}(SAV).
\]
The embedding ensures that the inverse exists. This formula is basis-independent up to similarity within the fixed two-dimensional trial space and applies to a two-step sketched Arnoldi/Lanczos projection in exact arithmetic. The condition is an embedding on \(\operatorname{span}\{V,AV\}\), not merely on the trial space \(\operatorname{span}\{V\}\).

## Proof
When \(b=0\), \(AV\) lies in the range of \(V\), so the sketch cancels from the reduced matrix: \(H=V^{\mathsf T}AV\), which is symmetric. Assume henceforth that \(b>0\) and put \(v_3=r/b\). In the orthonormal frame \(W=[v_1,v_2,v_3]\), the relevant columns of \(A\) are
\[
W^{\mathsf T}AV=\begin{pmatrix}\alpha&a\\a&\beta\\0&b\end{pmatrix}.
\]
Let \(G=W^{\mathsf T}S^{\mathsf T}SW=\begin{pmatrix}E&g\\g^{\mathsf T}&\gamma\end{pmatrix}\), where \(E\) is two-by-two. The embedding gives \((1-\varepsilon)I_3\preceq G\preceq(1+\varepsilon)I_3\). Write \(t=E^{-1}g=(t_1,t_2)^{\mathsf T}\). Direct multiplication yields
\[
H=\begin{pmatrix}\alpha&a+b t_1\\a&\beta+b t_2\end{pmatrix},\qquad
D=(\alpha-\beta-bt_2)^2+4a(a+bt_1),
\]
where \(D\) is the characteristic discriminant.

We prove the sharp metric cross-block bound
\[
\|E^{-1}g\|_2\le R_\varepsilon:=\frac{\varepsilon}{\sqrt{1-\varepsilon^2}}.
\]
If \(t=0\), this is immediate. Otherwise take \(u=t/\|t\|_2\). The compression of \(G\) to the orthonormal pair \((u,0)\) and the third coordinate is \(\begin{psmallmatrix}p&q\\q&r_0\end{psmallmatrix}\), with \(p=u^{\mathsf T}Eu>0\) and \(q=u^{\mathsf T}g=\|t\|_2p\). Its eigenvalues are also in \([1-\varepsilon,1+\varepsilon]\). Write \(p=1+s_0\), so \(|s_0|\le\varepsilon\). Positivity of the compression minus \((1-\varepsilon)I\), and of \((1+\varepsilon)I\) minus the compression, gives
\[
q^2\le(\varepsilon+s_0)(r_0-1+\varepsilon),\quad
q^2\le(\varepsilon-s_0)(1+\varepsilon-r_0).
\]
Multiplying the first bound by \((\varepsilon-s_0)/(2\varepsilon)\), the second by \((\varepsilon+s_0)/(2\varepsilon)\), and adding proves \(q^2\le\varepsilon^2-s_0^2\) for \(\varepsilon>0\). Therefore
\[
\|t\|_2^2=\frac{q^2}{(1+s_0)^2}\le\frac{\varepsilon^2-s_0^2}{(1+s_0)^2}\le\frac{\varepsilon^2}{1-\varepsilon^2}.
\]
The last inequality is a one-variable maximum attained at \(s_0=-\varepsilon^2\). For \(\varepsilon=0\), \(G=I\) and \(t=0\).

Since \(t_1\ge-R_\varepsilon\) and a square is nonnegative,
\[
D\ge4a(a-bR_\varepsilon).
\]
If \(D\ge0\), both eigenvalues are real; if \(D<0\), their imaginary parts have magnitude \(\sqrt{-D}/2\). Both cases yield the stated imaginary-part bound. If \(\varepsilon<a/\sqrt{a^2+b^2}\), then \(D>0\), so the two Ritz values are real and distinct; equality guarantees \(D\ge0\).

To prove sharpness, fix arbitrary \(a,b>0\) and \(0<\varepsilon<1\). In three dimensions take
\[
A=dI_3+\begin{pmatrix}0&a&0\\a&0&b\\0&b&0\end{pmatrix},\qquad v_1=e_1,\qquad d>\sqrt{a^2+b^2}.
\]
This \(A\) is positive definite and its two Lanczos coefficients equal the prescribed \(a,b\). Realize the sketch by the positive-definite Gram matrix \(S^{\mathsf T}S=G_\varepsilon\), where
\[
G_\varepsilon=\begin{pmatrix}
1-\varepsilon^2&0&-\varepsilon\sqrt{1-\varepsilon^2}\\
0&1&0\\
-\varepsilon\sqrt{1-\varepsilon^2}&0&1+\varepsilon^2
\end{pmatrix}.
\]
Its eigenvalues are exactly \(1-\varepsilon,1,1+\varepsilon\), so it satisfies the specified squared-norm embedding with equality in the extremal directions. In this case \(t_1=-R_\varepsilon\), \(t_2=0\), and
\[
H=\begin{pmatrix}d&a-bR_\varepsilon\\a&d\end{pmatrix},\qquad
(\lambda-d)^2=a(a-bR_\varepsilon).
\]
For \(\varepsilon=a/\sqrt{a^2+b^2}\), the upper-right entry vanishes but the lower-left entry \(a\) does not, giving one non-diagonalizable Jordan block. Above this threshold the eigenvalues are precisely \(d\pm i\sqrt{a(bR_\varepsilon-a)}\). Thus the stated imaginary-part bound is globally sharp; varying \(a/b\) also makes the threshold arbitrarily close to zero.

## Verification
The standalone `verify.py` checks the Gram matrix characteristic polynomial, reduced-matrix identity, and sharp-threshold substitution symbolically with SymPy. It also generates one thousand randomized real symmetric positive-definite matrices and compatible bounded-distortion Gram matrices, reconstructs the Lanczos data from the matrices, and compares the actual reduced spectra against the theoretical bound. Three additional nonreal examples achieve the predicted imaginary part numerically. The exact proof above, not these finite checks, establishes the universal assertions.

## Relationship to prior work
Nakatsukasa and Tropp introduced the sketched Rayleigh--Ritz framework and explicitly observed in Section 6.8 of the 2021 open preprint that real symmetric input need not produce real sketched eigenvalue estimates. De Damas and Grigori's 2024 randomized implicitly restarted Arnoldi paper defines the sketched Petrov--Galerkin/Ritz procedure in Section 3.2. Subsequent work by Liu and Liu (2026) treats the qualitative nonreal-spectrum issue with real Schur arithmetic. These sources do not supply the present exact two-coefficient, sharp deterministic distortion threshold and universal imaginary-part envelope. A separate previously recorded result (identifier `7cd7cbdb-20aa-4dae-820a-6537f0baf613`) computes the occurrence probability under an unconditioned Gaussian sketch on a particular tridiagonal family; it does not assert the conditional worst-case envelope over all norm-preserving sketches. This distinction is one of quantifiers and implications, not a change of vocabulary.

## Limitations
The theorem controls only two-step projections of real symmetric matrices in exact arithmetic; the sketch must embed the full space spanned by the two Lanczos vectors and the next residual. For a fixed matrix with unequal leading Lanczos diagonal coefficients, the uniform threshold need not be necessary for its particular spectrum. The sharpness sketch is a deterministic admissible matrix; no claim is made that a given random sketch distribution attains equality with positive probability. The same witness can be embedded in any larger dimension by appending a positive scalar block to the input matrix and zero columns to the sketch, giving \(s=3<n\) while preserving the required three-dimensional embedding. The result does not give convergence rates for a restarted eigensolver. The numerical verifier is supporting finite evidence, not a substitute for the analytical proof.

## References
1. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113, first posted 2021-10-29, Sections 2, 6, and 6.8; later SIAM J. Matrix Anal. Appl. 45 (2024), 1183–1214, DOI 10.1137/23M1565413. https://arxiv.org/abs/2111.00113
2. J.-G. de Damas and L. Grigori, *Randomized Implicitly Restarted Arnoldi method for the non-symmetric eigenvalue problem*, arXiv:2407.03208v1, first posted 2024-07-03, Section 3.2. https://arxiv.org/html/2407.03208v1
3. J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1, posted 2026-10-15, Sections 2.2 and 3.1. https://arxiv.org/html/2610.22261v1
