# Exact beta law for positivity loss in two-sided Gaussian Nyström rank-one truncation

## Finding

For the two-sided Gaussian generalized Nyström approximation followed by its best rank-one singular-value truncation, an identity-matrix input can produce a negative symmetric eigenvalue. On the smallest nontrivial codimension-one family, the negativity has an **exact beta distribution**, explicit tails, and a sharp moment threshold.

Let integers \(p,\ell\ge4\), \(k=p+1\), \(n=k+1\), and \(t=k+\ell\) be fixed. Draw independent Gaussian matrices \(\Omega\in\mathbb R^{n\times k}\) and \(\Psi\in\mathbb R^{n\times t}\), each with mutually independent standard normal entries. Let \(Z=I_n\), and form the exact-arithmetic rank-one approximation
\[
 P=\Omega(\Psi^{\mathsf T}\Omega)^\dagger\Psi^{\mathsf T},\qquad
 Y=[\![P]\!]_1,
 \qquad D=-\lambda_{\min}\!\left(\frac{Y+Y^{\mathsf T}}2\right).
\]
Here \(\dagger\) denotes the Moore–Penrose pseudoinverse and \([\![P]\!]_1\) denotes its best rank-one truncated singular-value decomposition. Its leading singular value is simple almost surely, so \(Y\) is unambiguously defined almost surely.

**Theorem.** Independently distributed variables \(U\sim\chi^2_k\) and \(V\sim\chi^2_{\ell+1}\) give the exact identities in distribution
\[
 D\;\overset{\mathrm d}=\;\frac{\sqrt{1+U/V}-1}{2},
 \qquad (1+2D)^{-2}\sim\operatorname{Beta}\left(\frac{\ell+1}{2},\frac{k}{2}\right).
\]
In particular \(D>0\) almost surely, and for every \(x\ge0\),
\[
 \Pr(D>x)=I_{(1+2x)^{-2}}\!\left(\frac{\ell+1}{2},\frac{k}{2}\right),
\]
where \(I_z(a,b)=B_z(a,b)/B(a,b)\) is the regularized lower incomplete beta function. Let \(a=(\ell+1)/2\) and \(b=k/2\). The exact tail law is
\[
 \Pr(D>x)\sim\frac{2^{-2a}}{aB(a,b)}x^{-2a}\quad(x\longrightarrow\infty).
\]
It follows that for every real \(q>0\), \(\mathbb E D^q<\infty\) **if and only if** \(q<\ell+1\), and
\[
 \mathbb E D=\frac12\left[\frac{B(\ell/2,k/2)}{B((\ell+1)/2,k/2)}-1\right].
\]
For \(p=5\), \(\ell=4\), the expectation equals \(41/128\). Thus the negative eigenvalue has unbounded magnitude with a polynomial tail of sharp exponent \(\ell+1\), even though the input \(Z=I_n\) is positive definite and has unit operator norm.

## Assumptions and scope

Everything is real, finite-dimensional, and in exact arithmetic. Both sketch matrices are independent and standard Gaussian. The target rank is one and the right sketch has \(k=p+1\) columns, while the left sketch has \(k+\ell\) columns, matching the parameterization of Lam, Ceruti, and Kressner, Section 2.3 [1]. The identity input has dimension \(k+1\), so the projected subspace has codimension one. Although \(p,\ell\ge4\) reproduces the source's recommended setting, the proof itself works for all \(k\ge1\) and \(\ell\ge0\) for which \(t\ge k\); the theorem is stated in the primary source's setting.

The quantity \(D\) measures the negative eigenvalue of the **symmetric part after rank-one truncation**. It is neither the Frobenius approximation error nor a claim about an entire time-integration trajectory. The input identity is a canonical high-rank, isotropic stress test, not a nearly rank-one data matrix.

## Proof

**1. Exact oblique block form.** Almost surely \(\Omega\) has full column rank. Choose an orthonormal basis \(Q\in\mathbb R^{n\times k}\) for its columns, and choose a unit normal \(v\perp\operatorname{ran}Q\). Independence and rotational invariance of \(\Psi\) imply that
\[
 X=\Psi^{\mathsf T}Q\in\mathbb R^{t\times k},\quad
 y=\Psi^{\mathsf T}v\in\mathbb R^{t}
\]
are independent standard Gaussian arrays. Since \(X\) has full column rank almost surely, the change from \(\Omega\) to \(Q\) leaves its oblique projector unchanged:
\[
 P=QX^\dagger\Psi^{\mathsf T}.
\]
Relative to the orthonormal coordinates \([Q,v]\), write \(b=X^\dagger y\in\mathbb R^k\). Then
\[
 [Q,v]^{\mathsf T}P[Q,v]
 =\begin{pmatrix}I_k&b\\0&0\end{pmatrix}.
\]

**2. Truncation and the negative eigenvalue.** The nonzero squared singular values of this block matrix are the eigenvalues of \(I_k+bb^{\mathsf T}\): \(1+\|b\|_2^2\) once and \(1\) with multiplicity \(k-1\). Its top left singular vector is \(b/\|b\|_2\) for \(b\ne0\), a full-probability event. Set \(r=\|b\|_2\). The best rank-one truncation, restricted to the span of \(b/\|b\|_2\) and \(v\), is exactly
\[
 Y\big|_{\operatorname{span}\{b,v\}}=\begin{pmatrix}1&r\\0&0\end{pmatrix},
 \qquad \frac{Y+Y^{\mathsf T}}2\bigg|_{\operatorname{span}\{b,v\}}
 =\begin{pmatrix}1&r/2\\r/2&0\end{pmatrix}.
\]
The symmetric part is zero on the remaining coordinates and has the two eigenvalues \((1\pm\sqrt{1+r^2})/2\) in the displayed block. Hence \(D=(\sqrt{1+r^2}-1)/2>0\) almost surely.

**3. Exact Gaussian regression distribution.** Given \(X\), the independent standard normal vector \(y\) yields
\[
 b\mid X\sim N_k\left(0,(X^{\mathsf T}X)^{-1}\right).
\]
The Gram matrix \(X^{\mathsf T}X\) has the \(k\)-variate Wishart law with \(t=k+\ell\) degrees of freedom and identity scale. Integrating its density against the displayed conditional normal density gives
\[
 f_b(z)=\frac{\Gamma((t+1)/2)}{\pi^{k/2}\Gamma((\ell+1)/2)}
 (1+\|z\|_2^2)^{-(t+1)/2},\qquad z\in\mathbb R^k.
\]
This is the multivariate Student distribution \(b\overset{\mathrm d}=g/\sqrt V\), where \(g\sim N_k(0,I_k)\), \(V\sim\chi^2_{\ell+1}\), independently. One may equivalently verify this density directly by integrating the scalar gamma density of \(V\) in the Gaussian mixture \(g/\sqrt V\). Therefore \(r^2\overset{\mathrm d}=U/V\) with \(U=\|g\|_2^2\sim\chi^2_k\).

**4. Beta transform and tail.** The chi-square ratio identity gives \(V/(U+V)\sim\operatorname{Beta}(a,b)\), with \(a=(\ell+1)/2\) and \(b=k/2\). By Step 2,
\[
 \frac{V}{U+V}=(1+r^2)^{-1}\overset{\mathrm d}=(1+2D)^{-2}.
\]
The event \(D>x\) is exactly the event that this beta variable is below \((1+2x)^{-2}\), yielding the stated CDF. Since \(I_z(a,b)\sim z^a/[aB(a,b)]\) as \(z\downarrow0\), the sharp tail follows using \((1+2x)^{-2}\sim(2x)^{-2}\). The tail integral criterion proves the moment threshold. For the mean, \(1+2D=T^{-1/2}\) with \(T\sim\operatorname{Beta}(a,b)\), whence \(\mathbb ET^{-1/2}=B(a-1/2,b)/B(a,b)\). All beta arguments are positive in the stated range. Substituting \(k=6,\ell=4\) reduces the beta quotient to \(105/64\), so \(\mathbb ED=41/128\). This proves every assertion.

## Verification

The standalone `verifier.py` reproduces the two-sketch pseudoinverse, computes its rank-one SVD and symmetrized eigenvalues, checks the canonical exact block example, and compares direct Gaussian least-squares sampling with the beta prediction. Executed under Python with NumPy and SciPy, it prints `PASS 812 checks; tested deterministic algebra, full Gaussian sketches and beta-law sampling`. Monte Carlo frequencies only corroborate the distribution law; Steps 1–4 constitute its proof. For a deterministic illustration, choose \(X\) to contain \(I_k\) in its first \(k\) rows, and choose \(y=2e_1\). Then \(b=2e_1\), and the symmetrized rank-one output has negative eigenvalue exactly \((1-\sqrt5)/2\).

## Relationship to prior work

Lam, Ceruti and Kressner [1, Section 2.3, equation (8)] give the precise two-sided generalized Nyström approximation and rank truncation used here; their theorem gives bounds on Frobenius approximation-error moments with oversampling. Nakatsukasa [2, Sections 1–3] studies the generalized Nyström oblique projector and its numerical stability and accuracy. Tropp and collaborators [3, Sections 5–6] study structure-aware positive-semidefinite approximations, highlighting why PSD-preserving alternatives have additional design requirements. The published dimension-dependent oblique-projection error formula [4, Section 3.1] provides a complementary expected-error estimate; its ordinary second moment does not imply a distribution of negative eigenvalues.

The oblique-projector block decomposition, Gaussian/Wishart regression law, and beta-ratio identity are established ingredients, **not** claimed as new. The precise structural claim assessed here is their application to the top-SVD-truncated two-sided estimator: the identity-input negativity distribution, all-oversampling tail exponent, explicit mean, and sharp moment cutoff. A result implying this whole statement may exist under different terminology in literature on canonical angles, randomized oblique projections, or matrix-valued Student distributions; publication priority is not certified by a finite literature search.

## Limitations

The exact law is for rank-one SVD truncation of identity inputs with one-dimensional sketch-range complement. It is not an optimality theorem for low-rank data, does not imply that a specific low-rank differential-equation trajectory reaches the identity input, and does not address finite-precision pseudoinverses, other sketch distributions, or general rank targets. For the full identity matrix, the best rank-one approximation already has substantial error; nonnegativity is an additional structural property rather than a surrogate for approximation accuracy. The same-sketch symmetric positive-semidefinite Nyström approximation is a different method and remains PSD on this input.

## References

[1] H. Y. Lam, G. Ceruti, D. Kressner, *Randomized low-rank Runge-Kutta methods*, arXiv:2409.06384v1, first publicly posted 2024-09-10. https://arxiv.org/html/2409.06384v1 ; https://arxiv.org/abs/2409.06384v1.

[2] Y. Nakatsukasa, *Fast and stable randomized low-rank matrix approximation*, arXiv:2009.11392, 2020. https://arxiv.org/abs/2009.11392.

[3] J. A. Tropp, A. Yurtsever, M. Udell, V. Cevher, *Practical sketching algorithms for low-rank matrix approximation*, arXiv:1609.00048 / SIAM Journal on Matrix Analysis and Applications 38 (2017). https://arxiv.org/abs/1609.00048.

[4] *Randomized low-rank approximation of parameter-dependent matrices*, Numerical Linear Algebra with Applications, DOI:10.1002/nla.2576, discussion of oblique-projector and expected-error identities. https://doi.org/10.1002/nla.2576.
