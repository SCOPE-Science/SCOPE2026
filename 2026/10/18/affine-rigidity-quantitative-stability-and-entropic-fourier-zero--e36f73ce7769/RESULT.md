# Affine rigidity, quantitative stability, and entropic Fourier-zero loss for products of Euclidean balls

## Finding

Let \(m\ge 2\) and let \(d_1,\ldots,d_m\) be positive integers with \(d=\sum_i d_i\). Put \(C=\prod_{i=1}^m B^{d_i}_2\), where \(B^q_2\) is the closed Euclidean unit ball in \(\mathbb R^q\). For an invertible real \(d\)-by-\(d\) matrix \(A\), consider the full-dimensional convex body \(K=AC\). Write \(A_i\) for its \(d\)-by-\(d_i\) column blocks, \(\omega_q=\pi^{q/2}/\Gamma(1+q/2)\), and \(j_i=j_{d_i/2,1}\) for the first positive zero of the Bessel function \(J_{d_i/2}\). Define the first **real** Fourier-zero radius by

\[
\rho(K)=\min\{\|\xi\|_2:\xi\in\mathbb R^d,\ \widehat{\mathbf1_K}(\xi)=0\},\qquad
\widehat{\mathbf1_K}(\xi)=\int_K e^{-\mathrm i\langle \xi,x\rangle}\,dx.
\]

**Exact spectral and sharp volume statements.** Every such body satisfies

\[
\boxed{\rho(K)=\min_{1\le i\le m}\frac{j_i}{\|A_i\|_{\mathrm{op}}}},
\qquad
\boxed{\rho(K)^d\operatorname{vol}_d(K)\le\prod_{i=1}^m\omega_{d_i}j_i^{d_i}}.
\]

Equality in the second inequality holds **if and only if** there are \(s>0\) and an orthogonal matrix \(U\) such that

\[
A=sU\operatorname{diag}(j_1I_{d_1},\ldots,j_mI_{d_m}).
\]

Thus the optimizer among all affine images of this product, at any prescribed volume, is unique up to Euclidean isometry and common dilation (with the given factor dimensions). In particular arbitrary skewing, anisotropic deformation of individual factors, and inter-factor mixing cannot improve the first-zero radius after volume normalization.

**Dimension-free quantitative rigidity.** Set \(D=\operatorname{diag}(j_iI_{d_i})\), \(T=\rho(K)AD^{-1}\), and

\[
\delta(K)=\log\left(\frac{\prod_i\omega_{d_i}j_i^{d_i}}{\rho(K)^d\operatorname{vol}_d(K)}\right)\ge0.
\]

There exists an orthogonal matrix \(U\) for which

\[
\boxed{\|T-U\|_F^2\le2\delta(K).}
\]

The exponent \(1/2\) implicit in the resulting square-root stability is optimal: in every nontrivial factor partition, there are affine perturbations with \(\delta\to0\) and \(\min_U\|T-U\|_F\asymp\sqrt\delta\). The numerical constant \(2\) in the displayed estimate is **not claimed optimal**.

**High-dimensional entropy law.** Let the number of factors \(m\) be fixed, and let \(d_i=d_i(d)\to\infty\) with \(p_i=d_i/d\to\alpha_i>0\), \(\sum_i\alpha_i=1\). The best attainable ratio to the first-zero radius of the same-volume \(d\)-ball has the limit

\[
\boxed{
\lim_{d\to\infty}\sup_{A\in GL(d,\mathbb R)}\frac{\rho\bigl(A\prod_i B^{d_i}_2\bigr)}{\rho(B^d_{\operatorname{vol}(A C)})}
=\prod_{i=1}^m\alpha_i^{\alpha_i/2}
=\exp\!\left(-\tfrac12H(\alpha)\right),
\quad H(\alpha)=-\sum_i\alpha_i\log\alpha_i.
}
\]

The ratio is independent of the common chosen volume. For two equally sized growing factors it tends to \(1/\sqrt2\), and for three equally sized growing factors it tends to \(1/\sqrt3\). More quantitatively, if all \(p_i\ge c>0\), its ratio to \(\exp(-H(p)/2)\) is \(1+O_{m,c}(d^{-2/3})\).

## Assumptions and scope

The dimension \(d\), all factor dimensions, and the invertible matrix \(A\) are arbitrary with \(m\ge2\). The matrix may mix all coordinate blocks, with no block-diagonal or orthogonality assumption. The Fourier zero is taken over **real frequency vectors**, not the complex null variety. The centroid of \(C\) is the origin; translating \(K\) changes its Fourier transform by a nonvanishing phase and leaves \(\rho\) unchanged. The ratio to the equal-volume Euclidean ball uses the same Fourier convention for both bodies and is independent of a common Fourier normalization constant.

The asymptotic assertion assumes a **fixed** number of blocks and strictly positive limiting proportions. No uniform claim is made for shrinking proportions or an increasing number of blocks.

## Proof

**Step 1: Factorization and exact first zero.** The elementary radial Fourier integral for a Euclidean unit ball states

\[
\widehat{\mathbf1_{B_2^q}}(\eta)=(2\pi)^{q/2}\|\eta\|_2^{-q/2}J_{q/2}(\|\eta\|_2),
\]

with the positive continuous value \(\omega_q\) at \(\eta=0\). Under the change of variables \(x=Ay\), this implies

\[
\widehat{\mathbf1_K}(\xi)=|\det A|\prod_{i=1}^m
\widehat{\mathbf1_{B_2^{d_i}}}(A_i^T\xi).
\]

The product cannot vanish while every \(\|A_i^T\xi\|<j_i\). Since \(\|A_i^T\xi\|\le\|A_i\|_{\mathrm{op}}\|\xi\|\), every Fourier zero has length at least the minimum of \(j_i/\|A_i\|_{\mathrm{op}}\). Conversely, choose an index attaining that minimum, and choose a unit left singular vector \(u\) of \(A_i\) for its largest singular value. Then \(\xi=(j_i/\|A_i\|_{\mathrm{op}})u\) makes the \(i\)-th factor vanish. This proves the first boxed identity, including attainment.

**Step 2: Sharp global inequality and equality.** Put \(\rho=\rho(K)\) and define \(T=\rho AD^{-1}\). Step 1 yields \(\|T_i\|_{\mathrm{op}}\le1\) for every column block. Every column therefore has norm at most one. Hadamard's determinant inequality gives

\[
|\det T|\le\prod_{j=1}^d\|\operatorname{col}_j(T)\|_2\le1.
\]

Since \(\operatorname{vol}(K)=|\det A|\prod_i\omega_{d_i}\), the determinant bound is precisely the second boxed inequality. Equality requires all columns of \(T\) to be unit vectors and mutually orthogonal; equivalently \(T\in O(d)\). This says \(A=\rho^{-1}UD\), as asserted. Conversely, such \(A\) satisfies the equality because all block norms are \(\rho^{-1}j_i\). This establishes both necessity and sufficiency, without making any assumption about distinct or repeated factor dimensions.

**Step 3: Dimension-free stability.** Let \(G=T^TT\), which is positive definite. Each block has all singular values at most one, so

\[
\operatorname{tr}G=\sum_{i=1}^m\|T_i\|_F^2\le\sum_{i=1}^m d_i=d.
\]

Let \(\lambda_1,\ldots,\lambda_d>0\) be the eigenvalues of \(G\). The elementary scalar inequality \(z-1\ge\log z\), with \(z=\sqrt\lambda\), gives

\[
\lambda-1-\log\lambda-(\sqrt\lambda-1)^2
=2(\sqrt\lambda-1-\log\sqrt\lambda)\ge0.
\]

The polar decomposition \(T=U\sqrt G\) supplies an orthogonal matrix \(U\), and the Procrustes identity yields

\[
\begin{aligned}
\|T-U\|_F^2
&=\sum_j(\sqrt{\lambda_j}-1)^2\\
&\le\operatorname{tr}G-d-\log\det G\\
&\le-\log\det G
=-2\log|\det T|=2\delta(K).
\end{aligned}
\]

To prove optimality of the **exponent**, choose one coordinate from each of two different blocks and modify the corresponding identity matrix columns by the planar matrix

\[
C_\varepsilon=\begin{pmatrix}1&\varepsilon\\0&\sqrt{1-\varepsilon^2}\end{pmatrix},\qquad0<\varepsilon<1,
\]

leaving all other coordinates unchanged. Every original column block continues to have orthonormal columns, so its operator norm is exactly one. Set \(A_\varepsilon=T_\varepsilon D\), where \(T_\varepsilon\) is this block-modified identity; the exact radius formula gives \(\rho=1\). Its deficit equals \(\delta=-\tfrac12\log(1-\varepsilon^2)=\varepsilon^2/2+O(\varepsilon^4)\). The nontrivial singular values are \(\sqrt{1+\varepsilon}\) and \(\sqrt{1-\varepsilon}\), so

\[
\inf_{U\in O(d)}\|T_\varepsilon-U\|_F^2
=(\sqrt{1+\varepsilon}-1)^2+(\sqrt{1-\varepsilon}-1)^2
=\varepsilon^2/2+O(\varepsilon^4).
\]

Thus no estimate with exponent strictly larger than \(1/2\) can hold uniformly near equality.

**Step 4: Sharp entropy limit.** Let \(F(q)=j_{q/2,1}\omega_q^{1/q}\). By Step 2, at prescribed volume \(V>0\), the optimal first-zero radius is \((\prod_i\omega_{d_i}j_i^{d_i}/V)^{1/d}\). The equal-volume Euclidean ball has radius \((V/\omega_d)^{1/d}\) and Fourier first-zero radius \(j_{d/2,1}(\omega_d/V)^{1/d}\). Hence the **exact finite-dimensional comparison** is

\[
\frac{\rho_{\max}}{\rho(B^d_{\mathrm{same\ volume}})}
=\frac{\prod_i F(d_i)^{d_i/d}}{F(d)}.
\]

Stirling's formula implies \(\omega_q^{1/q}=\sqrt{2\pi e/q}\,(1+O(\log q/q))\), while the classical first-zero asymptotic \(j_{q/2,1}=(q/2)(1+O(q^{-2/3}))\) gives

\[
F(q)=\sqrt{\pi e q/2}\,(1+O(q^{-2/3})).
\]

Writing \(p_i=d_i/d\) in the exact comparison and using \(p_i\ge c>0\), we obtain

\[
\log\frac{\rho_{\max}}{\rho(B^d_{\mathrm{same\ volume}})}
=\tfrac12\sum_i p_i\log p_i+O_{m,c}(d^{-2/3}).
\]

Taking \(d\to\infty\) gives the entropy formula and both balanced examples. The Bessel-zero asymptotic is **established special-function literature**, not claimed new here.

## Verification

The accompanying standalone `check_fourier_product.py` uses NumPy and SciPy. It computes first Bessel zeros independently, samples 409 invertible block-affine configurations across five dimension partitions, and checks the determinant bound, equality examples, and the polar-distance inequality. It also tests a two-block shear family for the sharp square-root exponent, and displays finite-dimensional balanced-product ratios in dimensions 10, 20, 40, and 80 approaching \(1/\sqrt2\). All these finite checks passed. The analytical proof above, not floating-point testing, establishes the universal statements and the limit.

Reproduction: `python check_fourier_product.py` with Python 3, NumPy, and SciPy. Root finding is by sign bracketing and Brent's method; its finite numerical tolerances are not an infinite-dimensional certificate.

## Relationship to prior work

Benguria, Levitin, and Parnovski [1, Example 3.5 and Example 3.6] established the Fourier transform and first zero of the ball and analyzed cuboids, including their comparison to the equal-volume ball. Thus the special partition with every factor one-dimensional is **previously covered**; the basic Bessel and tensor-product formulas are standard. Their full text does not state the arbitrary affine mixed-ball product equality classification, the dimension-free orthogonality stability estimate, or the factor-proportion entropy law.

Gómez-Serrano, Levitin, Platt, and Polterovich [2, Sections 1–2] disprove the ball-maximizer conjecture and prove that in dimensions at least three the global first-zero functional has no fixed-volume maximizer. Their construction uses elongated **bipyramids**, geometrically distinct from affine products of round factors. The present bound is a sharp **restricted-class** result, entirely compatible with their global counterexample. Their full HTML preprint was examined including the principal theorems and proof structure.

Dunster [3] supplies established uniform large-order Bessel-zero asymptotics. They imply the special-function estimate used in Step 4; no new asymptotic formula for individual Bessel zeros is asserted.

## Limitations

The result applies only to invertible affine images of fixed Cartesian products of Euclidean balls, not all centrally symmetric convex bodies. The first Fourier-zero radius is a real-frequency quantity; complex zeros and other spectral descriptors are outside the claim. The coefficient \(2\) in the stability inequality is sufficient and not asserted optimal, while the square-root exponent is sharp. The entropy limit requires fixed \(m\) and positive limiting block proportions. It does not say that the exact finite-dimensional ratio is less than one for every partition, nor provide a uniform result for increasing numbers of factors. Historical priority of the combined restricted-class rigidity/stability/entropy theorem has not been independently certified.

## References

[1] R. Benguria, M. Levitin, and L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, Journal of Functional Analysis 257 (2009), 2088–2123, arXiv:0801.1617. Full preprint: https://arxiv.org/pdf/0801.1617 .

[2] J. Gómez-Serrano, M. Levitin, D. Platt, and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517 (first public release 2026-09-09). Full text: https://arxiv.org/html/2609.10517v1 .

[3] T. M. Dunster, *Error bounds for a uniform asymptotic approximation of the zeros of the Bessel function \(J_\nu\)*, arXiv:2405.08208 (first public release 2024-05-13); full text https://arxiv.org/pdf/2405.08208 .
