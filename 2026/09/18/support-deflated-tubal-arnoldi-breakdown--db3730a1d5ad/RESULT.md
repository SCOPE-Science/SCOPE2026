# Fourier-partial breakdown and support-deflated tubal Arnoldi

## Statement

Let \(\mathcal A\in\mathbb C^{n\times n\times p}\) and \(\mathcal B\in\mathbb C^{n\times 1\times p}\), and use the standard t-product based on the length-\(p\) discrete Fourier transform. Write the Fourier frontal slices as
\[
(\widehat A_k,\widehat b_k),\qquad k=1,\ldots,p,
\]
and assume first that every \(\widehat b_k\neq0\). Let
\[
\nu_k=\dim \operatorname{span}\{\widehat b_k,\widehat A_k\widehat b_k,
\widehat A_k^2\widehat b_k,\ldots\}
\]
be the classical Krylov grade of the \(k\)-th Fourier pair. Set
\[
\nu_{\min}=\min_k\nu_k,\qquad \nu_{\max}=\max_k\nu_k.
\]

The tensor tubal Krylov module decomposes exactly by Fourier frequency:
\[
\widehat{\mathcal K_j^t(\mathcal A,\mathcal B)}_k
=
\mathcal K_j(\widehat A_k,\widehat b_k),
\]
and, over the complex tubal-scalar algebra \(R\cong\mathbb C^p\),
\[
\mathcal K_j^t(\mathcal A,\mathcal B)
\cong
\prod_{k=1}^p \mathcal K_j(\widehat A_k,\widehat b_k).
\]
Consequently its component dimensions are
\[
d_k(j)=\min\{j,\nu_k\}.
\]
A module over \(R\cong\mathbb C^p\) is free of rank \(r\) exactly when every frequency component has complex dimension \(r\). Hence
\[
\boxed{\mathcal K_j^t\text{ is free of rank }j\quad\Longleftrightarrow\quad j\le\nu_{\min}.}
\]
More generally, \(\mathcal K_j^t\) is free if and only if all \(d_k(j)\) are equal.

This identifies the first exact breakdown of the usual unit-tubal-normalized Arnoldi process. In exact arithmetic it occurs when the process tries to create basis vector \(\nu_{\min}+1\): at least one Fourier Arnoldi residual is zero, so the subdiagonal tubal scalar has a zero Fourier coefficient and is noninvertible. The breakdown is globally happy if and only if
\[
\boxed{\nu_{\min}=\nu_{\max}.}
\]
If the grades differ, the first zero Fourier residual is only a **partial** or **non-happy** breakdown: at least one Fourier slice has reached its invariant cyclic space while another has not.

There is an exact continuation that does not require an invertible tubal normalizer. If \(\mathcal W\) is an orthogonalized residual, define the tubal scalar \(h\) through
\[
\widehat h_k=\|\widehat w_k\|_2,
\]
and its componentwise Moore--Penrose inverse through
\[
\widehat h_k^\dagger=
\begin{cases}
1/\widehat h_k,&\widehat h_k\ne0,\\
0,&\widehat h_k=0.
\end{cases}
\]
Set
\[
\mathcal q=\mathcal W*h^\dagger.
\]
Then
\[
\mathcal W=\mathcal q*h,
\qquad
\mathcal q^**\mathcal q=p,
\]
where \(p=hh^\dagger\) is the idempotent tubal scalar whose Fourier entries are one exactly on the active frequencies. Iterating this rule yields a support-orthogonal frame \(\{\mathcal q_j\}\) with
\[
\mathcal q_i^**\mathcal q_j=0\quad(i\ne j),
\qquad
\mathcal q_j^**\mathcal q_j=p_j,
\]
where
\[
\widehat p_j(k)=\mathbf 1_{\{j\le\nu_k\}}.
\]
The supports decrease monotonically. Frequency \(k\) follows ordinary matrix Arnoldi through step \(\nu_k\) and is then frozen. The process therefore terminates only at \(\nu_{\max}\), rather than at \(\nu_{\min}\).

Equivalently, the limiting cyclic module has the projective decomposition
\[
\boxed{
\mathcal K_\infty^t
\cong
\bigoplus_{j=1}^{\nu_{\max}} Rp_j.
}
\]
This reduces to a free module exactly when all grades coincide.

## Proof

Under the t-product, Fourier transformation diagonalizes tube convolution, so multiplication by a tubal scalar acts independently at every frequency. A general t-linear combination
\[
\sum_{r=0}^{j-1}\mathcal A^r*\mathcal B*c_r
\]
has Fourier component
\[
\sum_{r=0}^{j-1}\widehat A_k^r\widehat b_k\,\widehat c_r(k).
\]
Because the scalar coefficients \(\widehat c_r(k)\) can be chosen independently for each \(k\), the image is exactly the Cartesian product of the ordinary Fourier-slice Krylov spaces. This proves the decomposition and the dimensions \(d_k(j)\).

Let \(e_k\in R\) be the primitive idempotent supported only at frequency \(k\). If \(M\cong R^r\), then \(e_kM\cong\mathbb C^r\) for every \(k\). Conversely, if \(M=\prod_kV_k\) and every \(\dim_\mathbb C V_k=r\), choosing a basis independently in every \(V_k\) gives \(M\cong R^r\). This proves the free-module criterion.

Before a classical Arnoldi process reaches its grade, its orthogonalized residual is nonzero; at the grade it is zero and the cyclic Krylov space is invariant. Since tensor t-Arnoldi is simultaneous ordinary Arnoldi on all Fourier slices, every subdiagonal Fourier coefficient is nonzero through steps \(j<\nu_{\min}\), while at step \(j=\nu_{\min}\) at least one becomes zero. Thus the first noninvertible tubal subdiagonal is exactly the one that would create \(\mathcal q_{\nu_{\min}+1}\). At that point the full tensor Krylov module is invariant exactly when every slice has already reached its grade, i.e. exactly when \(\nu_{\min}=\nu_{\max}\).

For the continuation, if \(\widehat h_k>0\), then \(\widehat q_k=\widehat w_k/\widehat h_k\), while if \(\widehat h_k=0\), then \(\widehat w_k=\widehat q_k=0\). Hence \(\widehat q_k\widehat h_k=\widehat w_k\) at every frequency and \(\widehat q_k^*\widehat q_k\) is one on the active set and zero off it. Orthogonality between different support vectors follows frequencywise from ordinary Arnoldi. At frequency \(k\), exactly \(\nu_k\) nonzero vectors are generated. Thus the frame spans the full product module, with the \(j\)-th vector generating the ideal \(Rp_j\), proving the direct-sum decomposition.

## Tensor-function consequence

Let \(f\) be a primary matrix function defined on every \(\operatorname{spec}(\widehat A_k)\). At iteration \(j\), set
\[
m_k(j)=\min\{j,\nu_k\},
\]
and let \(V_{k,m_k}\) and \(H_{k,m_k}\) be the ordinary Arnoldi basis and reduced Hessenberg matrix for frequency \(k\). Define
\[
\widehat y_{k,j}
=
\|\widehat b_k\|_2
V_{k,m_k}f(H_{k,m_k})e_1.
\]
If \(j\ge\nu_k\), the cyclic Krylov subspace is invariant, so this Fourier component is exact. Therefore, with the usual unnormalized FFT convention,
\[
\boxed{
\|f(\mathcal A)*\mathcal B-\mathcal Y_j\|_F^2
=
\frac1p\sum_{k:\nu_k>j}
\|f(\widehat A_k)\widehat b_k-\widehat y_{k,j}\|_2^2.
}
\]
In particular,
\[
\boxed{\mathcal Y_{\nu_{\max}}=f(\mathcal A)*\mathcal B.}
\]
A frequency-locking implementation performs exactly \(\sum_k\nu_k\) active frontal matrix-vector products before exact termination, versus \(p\nu_{\max}\) if every frequency is padded to the longest grade.

## Explicit real family with arbitrarily large partial-breakdown gap

Take \(p=2\) and let \(J_m\) be the lower shift, \(J_me_i=e_{i+1}\) for \(i<m\). In the Fourier domain set
\[
\widehat A_1=0,\qquad \widehat A_2=J_m,
\qquad
\widehat b_1=\widehat b_2=e_1.
\]
The inverse two-point DFT gives the real tensors
\[
\mathcal A(:,:,1)=\frac12J_m,\qquad
\mathcal A(:,:,2)=-\frac12J_m,
\]
\[
\mathcal B(:,:,1)=e_1,\qquad
\mathcal B(:,:,2)=0.
\]
The Fourier grades are
\[
(\nu_1,\nu_2)=(1,m).
\]
After the first Arnoldi multiplication the two Fourier residual norms are \((0,1)\). Thus ordinary unit-tubal normalization encounters a noninvertible subdiagonal immediately, although the second frequency is not converged. For \(f(z)=e^z\),
\[
e^{J_m}e_1=\sum_{r=0}^{m-1}\frac{e_{r+1}}{r!},
\]
which is not in \(\operatorname{span}\{e_1\}\) for \(m\ge2\). The gap
\[
\nu_{\max}/\nu_{\min}=m
\]
is unbounded.

For \(m=8\), the verification artifact gives a one-step tensor exponential relative error
\[
0.624633332252756\ldots
\]
when the process stops at this partial breakdown. The support-deflated process uses \(9=1+8\) active Fourier frontal matvecs instead of \(16\) padded matvecs and recovers the exponential action exactly in exact arithmetic.

## Positive-tolerance premature-stop family

The 2026 normalization algorithm stops if **any** Fourier slice norm is below its tolerance. This introduces a robust finite-tolerance failure even when no exact Fourier grade is small. For arbitrary \(\tau>0\), choose \(0<\epsilon<\tau\) and
\[
\widehat A_1=\epsilon J_m,\qquad
\widehat A_2=J_m,
\qquad
\widehat b_1=\widehat b_2=e_1.
\]
Both exact grades are \(m\), but the first orthogonalized residual norms are
\[
(\epsilon,1).
\]
Hence the stated normalization rule stops after the first basis vector whenever \(\epsilon<\tau<1\), despite the second frequency being far from convergence. The strict inequalities persist under sufficiently small perturbations, so this is not a measure-zero exact-breakdown phenomenon.

For \(m=8\), \(\tau=10^{-3}\), and \(\epsilon=10^{-4}\), the verification artifact gives relative tensor exponential error
\[
0.624633333741215\ldots
\]
if the calculation is terminated at that point. A tolerance-aware implementation should therefore lock only the small-residual Fourier components and continue the others; deriving a backward-stable locking policy is separate from the exact-arithmetic theorem above.

## Relation to prior work

Bouyghf, El Ghomari, and El Ichi (2026) introduce the tubal Arnoldi method for tensor-function approximation. Their normalization computes the Euclidean norm of every Fourier frontal vector and stops if one norm is below tolerance; Algorithm 2 invokes this normalization at every Arnoldi step. This record studies the breakdown geometry implicit in that rule.

Reichel and Ugwu (2021/2022) explicitly define t-Arnoldi breakdown as noninvertibility of a subdiagonal tubal scalar, state that their analysis assumes the iteration count is small enough to avoid it, and note that noninvertibility corresponds to a zero Fourier coefficient. They also observe that t-Arnoldi is simultaneous standard Arnoldi on the Fourier frontal slices. These facts are prior art; the contribution here is the exact grade characterization and the support-deflated continuation after only some frequencies have broken down.

El Ichi, Jbilou, and Sadaka (2021/2022) develop related tubal-Krylov methods. Classical block Arnoldi and block rational Arnoldi literature contains deflation strategies for rank loss, but those methods work over a field and do not by themselves state the product-ring/free-module obstruction or the idempotent-support continuation above. Kilmer, Braman, Hao, and Hoover (2013) provide the t-product algebra and normalization framework on which these tensor Krylov methods build.

To the best of our knowledge, the inspected tensor-Krylov literature does not state: (i) that the first tubal-Arnoldi breakdown is exactly the minimum Fourier Krylov grade, (ii) that unequal Fourier grades make the cyclic t-Krylov module non-free, (iii) the support-idempotent normalization that continues independently to the maximum grade, or (iv) the resulting exact tensor-function error decomposition and positive-tolerance premature-stop family.

## Limitations

The structural theorem is an exact-arithmetic statement. The positive-tolerance example proves that a global `Stop` rule can terminate prematurely, but it does not provide a certified floating-point threshold or backward-error analysis for frequency locking. Near-breakdown classification in floating point may require reorthogonalization and scale-aware tests.

The module proof is stated over the complexified tubal-scalar algebra \(\mathbb C^p\). For real tensors, Fourier slices and support masks must respect conjugate symmetry; the explicit \(p=2\) family is real. Frequencies with \(\widehat b_k=0\) can be treated as already inactive, but were excluded from the main statement to keep the normalization notation simple.

The support-deflated frame satisfies \(\mathcal q_j^**\mathcal q_j=p_j\), not the ordinary unit-tubal identity. Algorithms that require a single rectangular tensor \(V\) with \(V^**V=I\) must therefore be adapted to a frequency-ragged or projective representation. The result concerns the lateral-vector t-tubal Arnoldi process; block and tubal-global variants are not analyzed here.

The tensor-function exactness statement assumes the relevant primary matrix function is defined on every Fourier-slice spectrum. No claim is made about optimal finite-precision performance, restart strategies, or total computational time.

## Reproducibility

`artifacts/verify.py` checks the real two-frequency family, the grades, the first Fourier residual norms, the support masks and support orthogonality, the active frontal-matvec count, exact recovery at the maximum grade, and the positive-tolerance family. It uses only Python and NumPy. `artifacts/verification_output.txt` records the resulting values.

## References

1. F. Bouyghf, M. El Ghomari, and A. El Ichi, *The tubal Arnoldi method for tensor function approximation*, arXiv:2609.11369v1 (2026). https://arxiv.org/abs/2609.11369
2. L. Reichel and U. O. Ugwu, *Tensor Arnoldi-Tikhonov and GMRES-type methods for ill-posed problems with a t-product structure*, arXiv:2110.04796; later published version (2022). https://arxiv.org/abs/2110.04796
3. A. El Ichi, K. Jbilou, and R. Sadaka, *On tensor tubal-Krylov subspace methods*, Linear and Multilinear Algebra 70 (2022), 7575--7598. https://doi.org/10.1080/03081087.2021.1999381
4. M. E. Kilmer, K. Braman, N. Hao, and R. C. Hoover, *Third-Order Tensors as Operators on Matrices: A Theoretical and Computational Framework with Applications in Imaging*, SIAM J. Matrix Anal. Appl. 34 (2013), 148--172. https://doi.org/10.1137/110837711
5. S. Elsworth and S. Guettel, *The Block Rational Arnoldi Method*, SIAM J. Matrix Anal. Appl. 41 (2020), 365--388. https://doi.org/10.1137/19M1245505
