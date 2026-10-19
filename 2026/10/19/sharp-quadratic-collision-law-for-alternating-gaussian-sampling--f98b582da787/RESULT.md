# Sharp quadratic collision law for alternating Gaussian sampling and its Hermite limit

## Finding
Fix \(a>0\). In the Gaussian integer-translate space, observe a function at the two points
\[
\lambda_{k,-}=2k+\tfrac12-\varepsilon,\qquad
\lambda_{k,+}=2k+\tfrac12+\varepsilon,\qquad k\in\mathbb Z.
\]
Let \(B_a(\varepsilon)\) and \(U_a(\varepsilon)\) be the **optimal squared sampling bounds**, relative to the generating-coefficient \(\ell^2\)-norm. Let
\[
A_a(x)=\sum_{j\in\mathbb Z}\exp[-2a(2j+x)^2],\quad
A=A_a(1/2),\quad D=A_a'(1/2),\quad q=e^{-2a},
\]
with Jacobi functions \(\vartheta_3(t,q)=\sum_{n\in\mathbb Z}q^{n^2}e^{2int}\) and \(\vartheta_4(t,q)=\sum_{n\in\mathbb Z}(-1)^nq^{n^2}e^{2int}\). Then \(D<0\) and the following **sharp**, strictly positive constant controls the collision:
\[
\boxed{\quad B_a(\varepsilon)=C_a\varepsilon^2+O_a(\varepsilon^4),\qquad
C_a=\frac{D^2}{A}\frac{\vartheta_4(0,q)^2}{\vartheta_3(0,q)}>0.\quad}
\]
The leading lower singular-value profile over the full polyphase Brillouin zone is
\[
C_a(\omega)=\frac{D^2}{A}\frac{\vartheta_4(\omega/2,q)^2}{\vartheta_3(\omega/2,q)},\qquad 0\le\omega\le\pi,
\]
and is strictly increasing in \(\omega\). Thus the worst quasi-frequency is uniquely \(\omega=0\) (modulo \(2\pi\)) at leading order, rather than an unverified numerical grid minimum. At the same time,
\[
U_a(\varepsilon)=4A\vartheta_3(0,q)+O_a(\varepsilon^2),\qquad
\frac{U_a(\varepsilon)}{B_a(\varepsilon)}\sim
\frac{4A^2\vartheta_3(0,q)^2}{D^2\vartheta_4(0,q)^2}\varepsilon^{-2}.
\]
At exact coalescence, ordinary repeated values are rank deficient; their *confluent replacement* by the value and first derivative at each midpoint gives a bounded invertible sampling operator. The sharp coefficient has the contrasting width regimes
\[
\boxed{\ C_a\sim\frac{4\pi^3}{a}e^{-\pi^2/(2a)}\ (a\downarrow0),\qquad
C_a\sim4a^2e^{-a/2}\ (a\to\infty).\ }
\]

## Assumptions and scope
For each real \(a>0\), consider the Hilbert space
\[
V_a=\left\{f_c(x)=\sum_{j\in\mathbb Z}c_j e^{-a(x-j)^2}: c\in\ell^2(\mathbb Z)\right\},\qquad
\|f_c\|_{V_a}:=\|c\|_{\ell^2}.
\]
The integral translates of a Gaussian are a Riesz sequence; in particular the coefficient representation is unique. The sample operator for \(\varepsilon>0\) is \(T_{a,\varepsilon}c=(f_c(\lambda_{k,-}),f_c(\lambda_{k,+}))_{k\in\mathbb Z}\), with the product sequence space carrying the ordinary unweighted sum-of-squares norm. Precisely,
\[
B_a(\varepsilon)=\inf_{\|c\|_2=1}\|T_{a,\varepsilon}c\|_2^2,\qquad
U_a(\varepsilon)=\sup_{\|c\|_2=1}\|T_{a,\varepsilon}c\|_2^2.
\]
The asymptotics are for \(\varepsilon\downarrow0\) at **fixed** \(a>0\); the remainder constants need not be uniform in \(a\). The confluent operator is \(T_{a,H}c=(f_c(2k+1/2),f_c'(2k+1/2))_{k\in\mathbb Z}\). For sufficiently small \(\varepsilon>0\), both ordinary sample bounds are positive and finite. This result makes no assertion of full-range stability for all possible \(\varepsilon\).

## Proof
**1. Exact two-channel Fourier reduction.** Split the source coefficients into \((c_{2n})_{n\in\mathbb Z}\) and \((c_{2n+1})_{n\in\mathbb Z}\). Discrete Fourier transformation in the period-two variable is unitary from their direct sum onto \(L^2([ -\pi,\pi];\mathbb C^2)\) (with normalized measure). The two sampling cosets produce multiplication by the \(2\times2\) matrix
\[
H_{a,\varepsilon}(\omega)=\begin{pmatrix}h_a(\tfrac12-\varepsilon,\omega)\\h_a(\tfrac12+\varepsilon,\omega)\end{pmatrix},
\qquad
h_a(x,\omega)=\left(\sum_{n\in\mathbb Z}e^{-a(2n+x)^2}e^{-in\omega},\ 
\sum_{n\in\mathbb Z}e^{-a(2n+x-1)^2}e^{-in\omega}\right).
\]
The series and all their derivatives converge absolutely and uniformly on the compact \(x\)-interval used and in \(\omega\). Because this matrix is continuous and the Fourier transform is unitary,
\[
B_a(\varepsilon)=\min_{\omega\in[-\pi,\pi]}\sigma_{\min}(H_{a,\varepsilon}(\omega))^2,
\qquad
U_a(\varepsilon)=\max_{\omega\in[-\pi,\pi]}\sigma_{\max}(H_{a,\varepsilon}(\omega))^2.
\]
These are genuinely optimal bounds because a Fourier-band coefficient vector may be concentrated in an arbitrarily small neighborhood of an extremizing \(\omega\).

**2. Parity and the exact theta identities.** Abbreviate \(u(\omega)=\sum_ne^{-a(2n+1/2)^2}e^{-in\omega}\) and its spatial derivative \(u'(\omega)=\sum_n[-2a(2n+1/2)]e^{-a(2n+1/2)^2}e^{-in\omega}\). Symmetry \(n\mapsto-n\) in the second source channel gives
\[
h_a(1/2,\omega)=(u,\overline{u}),\qquad
\partial_xh_a(1/2,\omega)=(u',-\overline{u'}).
\]
Put \(h=h_a(1/2,\omega)\) and \(d=\partial_xh_a(1/2,\omega)\). Consequently
\[
\det\begin{pmatrix}h\\d\end{pmatrix}
=-2\operatorname{Re}(\overline u u')=-\partial_x|u_x(\omega)|^2\big|_{x=1/2},
\quad u_x(\omega)=\sum_ne^{-a(2n+x)^2}e^{-in\omega}.
\]
Expand \(\left|u_x\right|^2\) by setting \(r=n-m\) and \(s=n+m\). Since
\( (2n+x)^2+(2m+x)^2=2(s+x)^2+2r^2\), the parity of \(s\) matches that of \(r\). Thus
\[
|u_x(\omega)|^2
=A_a(x)\sum_{r\in 2\mathbb Z}e^{-2ar^2}e^{-ir\omega}
+A_a(x+1)\sum_{r\in 2\mathbb Z+1}e^{-2ar^2}e^{-ir\omega}.
\]
The even lattice symmetry gives \(A_a(3/2)=A_a(1/2)=A\) and \(A_a'(3/2)=-A_a'(1/2)=-D\). Evaluate and differentiate:
\[
\boxed{\ |u(\omega)|^2=A\vartheta_3(\omega/2,q),\qquad
\det\begin{pmatrix}h\\d\end{pmatrix}=-D\vartheta_4(\omega/2,q).\ }
\]
All denominators and determinants below are nonzero. Indeed, the Jacobi triple product implies \(\vartheta_3(t,q)>0\) and \(\vartheta_4(t,q)>0\) for real \(t\) and \(0<q<1\). Moreover \(D<0\): Poisson summation yields
\[
A_a(x)=\sqrt{\frac{\pi}{8a}}\vartheta_3\left(\frac{\pi x}{2},e^{-\pi^2/(8a)}\right),
\]
and the product formula makes \(\vartheta_3(t,Q)\) strictly decreasing for \(0<t<\pi/2\), so the derivative at \(x=1/2\) is negative.

**3. Uniform perturbation and sharp minimization.** Apply the unitary row transform \(2^{-1/2}\begin{psmallmatrix}1&1\\-1&1\end{psmallmatrix}\) to \(H_{a,\varepsilon}\). Uniform Taylor expansions on the compact frequency circle give its rows as
\(\sqrt2(h+O_a(\varepsilon^2))\) and \(\sqrt2(\varepsilon d+O_a(\varepsilon^3))\). Since \(\|h\|^2=2A\vartheta_3(\omega/2,q)\) has a positive uniform minimum, the large squared singular value equals \(2\|h\|^2+O_a(\varepsilon^2)\), and the small squared singular value equals
\[
2\varepsilon^2\left(\|d\|^2-\frac{|\langle d,h\rangle|^2}{\|h\|^2}\right)
+O_a(\varepsilon^4)
=\frac{2\varepsilon^2|\det(h,d)|^2}{\|h\|^2}+O_a(\varepsilon^4)
=\frac{D^2}{A}\frac{\vartheta_4(\omega/2,q)^2}{\vartheta_3(\omega/2,q)}\varepsilon^2+O_a(\varepsilon^4).
\]
One may derive the even-order remainder without eigenvector perturbation: the determinant of the row-transformed matrix is odd in \(\varepsilon\), hence its modulus squared has expansion \(4\varepsilon^2|\det(h,d)|^2+O_a(\varepsilon^4)\); divide by the large eigenvalue, which is uniformly separated from zero.

The Jacobi product representations
\[
\vartheta_3(t,q)=\prod_{n\ge1}(1-q^{2n})(1+2q^{2n-1}\cos2t+q^{4n-2}),
\]
\[
\vartheta_4(t,q)=\prod_{n\ge1}(1-q^{2n})(1-2q^{2n-1}\cos2t+q^{4n-2})
\]
show that \(\vartheta_3(t,q)\) strictly decreases and \(\vartheta_4(t,q)\) strictly increases as \(t\) increases from \(0\) to \(\pi/2\). Their squared ratio is therefore strictly increasing. The global lower-coefficient minimum is at \(\omega=0\), and the upper-limit maximum is also at \(\omega=0\). Taking minima and maxima of the **uniform** expansions proves the stated sharp squared sampling asymptotics and the condition-number formula.

**4. Confluent Hermite limit.** The two-channel symbol of \(T_{a,H}\) has rows \(h\) and \(d\). Its determinant is \(-D\vartheta_4(\omega/2,q)\), whose modulus has a positive minimum on the frequency circle. Its norm is bounded, hence its inverse matrix is uniformly bounded. The corresponding multiplier, and therefore \(T_{a,H}:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)\oplus\ell^2(\mathbb Z)\), is a bounded isomorphism. The ordinary duplicated-value operator at \(\varepsilon=0\) has identical polyphase rows, explaining the quadratic singular-value collapse.

**5. Extreme Gaussian widths.** For \(a\to\infty\), the unique nearest term in \(A_a(1/2)\) gives \(A\sim e^{-a/2}\), \(D\sim-2ae^{-a/2}\), and \(\vartheta_3(0,q),\vartheta_4(0,q)\to1\). Thus \(C_a\sim4a^2e^{-a/2}\). For \(a\downarrow0\), Poisson summation yields \(A\sim\sqrt{\pi/(8a)}\) and \(D\sim-2\pi\sqrt{\pi/(8a)}e^{-\pi^2/(8a)}\). Theta modular transformations give \(\vartheta_3(0,e^{-2a})\sim\sqrt{\pi/(2a)}\) and \(\vartheta_4(0,e^{-2a})\sim2\sqrt{\pi/(2a)}e^{-\pi^2/(8a)}\). Multiplication yields \(C_a\sim(4\pi^3/a)e^{-\pi^2/(2a)}\).

## Verification
Run the accompanying standalone script `gaussian_period2_check.py` with Python and NumPy. It implements the two-channel symbol from the proof by truncating Gaussian series symmetrically at 35 terms on each side and checks the theta/coefficient identities on 1001 frequencies for each of three generator widths. It also compares the computed optimal eigenvalue with the sharp asymptotics at four decreasing separations. The 3033 numerical checks passed. These **finite and floating-point checks are corroboration only**: strict positivity, uniqueness of the limiting extremizing quasi-frequency, infinite dimensional invertibility, and asymptotic error estimates are supplied analytically in the proof.

## Relationship to prior work
Baranov, Belov, and Gröchenig (arXiv:2112.01248, initial version 2021-12-02) classify complete interpolating sequences for Gaussian shift-invariant spaces at critical density, and give the coefficient \(\ell^2\) normalization. That existence characterization does not state the best constants or their exact near-collision rate, nor the present confluent fiber identity. Gröchenig, Romero, and Stöckler (arXiv:1712.07899) study sampling with derivatives and prove a general sufficient sampling theorem under the **strict** weighted density hypothesis \(D^->1\); the exactly critical, period-two Hermite design here is not its conclusion. Kiselev, Minin, Novikov, and Sitnik (arXiv:1308.2649) calculate theta-function Riesz constants for integer **generator translates** and cardinal interpolants; those constants concern a different operator than alternating near-coincident *evaluation* samples. More generally, standard Fourier/polyphase diagonalization and Jacobi product formulas are background tools and not claimed as novel. Exact claim/implication comparisons and remaining priority risks are documented in the accompanying review.

## Limitations
All statements are for the Gaussian with real \(a>0\), two samples in each period-two cell, and the unweighted coefficient-sequence norm. The \(O_a\)-estimates are not uniform under simultaneous variation of \(a\) and \(\varepsilon\). Exact optimal bounds for general finite positive separations are not determined. Only leading-order uniqueness of the worst quasi-frequency is proved; no uniqueness assertion for every nonzero separation is made. The Hermite limit uses value-plus-derivative observations with their stated, unnormalized data norm. No independent external audit or worldwide priority determination is asserted.

## References
1. A. Baranov, Y. Belov, K. Gröchenig, *Complete interpolating sequences for the Gaussian shift-invariant space*, arXiv:2112.01248 (v1, 2021-12-02), https://arxiv.org/abs/2112.01248.
2. K. Gröchenig, J. L. Romero, J. Stöckler, *Sharp results on sampling with derivatives in shift-invariant spaces and multi-window Gabor frames*, arXiv:1712.07899 (v1, 2017), https://arxiv.org/abs/1712.07899.
3. E. A. Kiselev, L. A. Minin, I. Ya. Novikov, S. M. Sitnik, *On Evaluation of Riesz Constants for Systems of Shifted Gaussians*, arXiv:1308.2649 (v1, 2013), https://arxiv.org/abs/1308.2649.
