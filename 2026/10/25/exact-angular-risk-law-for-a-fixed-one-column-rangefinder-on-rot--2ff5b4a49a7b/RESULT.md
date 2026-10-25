# Exact angular risk law for a fixed one-column rangefinder on rotating positive-definite matrices

## Finding

Let \(a>b>0\), \(0<L\le\pi\), and \(q\) be any nonnegative integer. Write \(m=2q+1\), let \(R(t)\) denote planar counterclockwise rotation by \(t\), and set
\[
A(t)=R(t)\begin{pmatrix}a&0\\0&b\end{pmatrix}R(t)^{\mathsf T},\qquad 0\le t\le L.
\]
For a **single nonzero parameter-independent sketch vector** \(\omega\in\mathbb R^2\), form the standard \(q\)-step power-rangefinder sample \(y_q(t)=A(t)^m\omega\), its orthogonal range projector \(P_q(t)=y_q(t)y_q(t)^{\mathsf T}/\|y_q(t)\|_2^2\), and the one-column approximation \(\widehat A_q(t)=P_q(t)A(t)\). Set \(W_q(\omega)=\max_{0\le t\le L}\|A(t)-\widehat A_q(t)\|_F\). For this planar rank-one residual, the Frobenius norm equals the operator norm.

**Sharp deterministic minimax law.** For every finite \(q\),
\[
\min_{\omega\ne0} W_q(\omega)^2
=
M_q(L)^2
:=\frac{b^2a^{2m}\cos^2(L/2)+a^2b^{2m}\sin^2(L/2)}
{a^{2m}\cos^2(L/2)+b^{2m}\sin^2(L/2)}.
\]
For \(0<L<\pi\), the optimal input rays are exactly those with angle \(L/2\) modulo \(\pi\). For \(L=\pi\), every nonzero input is optimal and \(W_q(\omega)=a\), independent of \(q\). Yet the best rank-one approximation to \(A(t)\) has error \(b\) at every parameter.

**Exact random uniform-error law.** If \(\omega\) is isotropic Gaussian, its input ray is uniform on the projective circle of length \(\pi\), and
\[
\mathbb P\{W_q(\omega)=a\}=\frac L\pi.
\]
For \(0<L<\pi\), this is an atom in the distribution of \(W_q\). More explicitly, for \(M_q(L)^2\le z<a^2\), define
\[
\delta_m(z)=\arcsin\sqrt{\frac{b^{2m}(a^2-z)}
{a^{2m}(z-b^2)+b^{2m}(a^2-z)}}.
\]
Then
\[
\mathbb P\{W_q^2\le z\}
=\frac{\pi-L-2\delta_m(z)}{\pi}.
\]
The distribution function is zero below \(M_q(L)^2\) and one at or above \(a^2\). For \(L=\pi\), \(W_q=a\) surely.

**Path-integrated identity without power iteration.** For \(q=0\) and \(L=\pi\), every nonzero \(\omega\) obeys
\[
\frac1\pi\int_0^\pi\|A(t)-\widehat A_0(t)\|_F^2\,dt=ab.
\]
Consequently the half-turn worst-parameter error-to-best-rank-one ratio is exactly \(a/b\), and the root-mean-square error ratio is \(\sqrt{a/b}\). Both can be arbitrarily large despite smoothness and a parameter-independent positive spectral gap.

## Assumptions and scope

All matrices and vectors are real; exact arithmetic is used. The parameter interval is continuous, not a finite grid. The spectral values \(a\) and \(b\) are positive and constant, while the eigenvectors vary smoothly. The same \(\omega\) is used for all parameters. A finite power-iteration depth \(q\ge0\) means \((AA^{\mathsf T})^qA\omega=A^{2q+1}\omega\) because each \(A(t)\) is symmetric positive definite. For random statements, \(\omega\sim N(0,I_2)\); the zero-vector event has probability zero. The residual is of rank one, so its Frobenius and spectral norms agree.

## Proof

**1. Exact residual formula.** Fix nonzero \(\omega\) of input-ray angle \(\phi\), defined modulo \(\pi\). Rotate coordinates by \(R(t)^{\mathsf T}\), and put \(\theta=\phi-t\). The sample vector is proportional to \((a^m\cos\theta,b^m\sin\theta)^{\mathsf T}\). Let \(D=\operatorname{diag}(a,b)\). For the projector onto this sampled direction,
\[
\begin{aligned}
e_q(\theta)^2
&=\|(I-P)D\|_F^2\\
&=a^2+b^2-\frac{a^{2m+2}\cos^2\theta+b^{2m+2}\sin^2\theta}
{a^{2m}\cos^2\theta+b^{2m}\sin^2\theta}\\
&=\frac{b^2a^{2m}\cos^2\theta+a^2b^{2m}\sin^2\theta}
{a^{2m}\cos^2\theta+b^{2m}\sin^2\theta}.
\end{aligned}
\]
It is \(\pi\)-periodic and even. As a function of \(u=\sin^2\theta\in[0,1]\), its derivative is
\[
\frac{a^{2m}b^{2m}(a^2-b^2)}
{\bigl(a^{2m}(1-u)+b^{2m}u\bigr)^2}>0.
\]
Thus its minimum over directions is \(b^2\), at the leading eigenvector, and its maximum is \(a^2\), at the weaker eigenvector.

**2. Deterministic angular minimax.** The angles \(\theta=\phi-t\) traversed as \(0\le t\le L\) form a closed arc of projective-circle length \(L\). The set of rays at angular distance at most \(r\in[0,\pi/2]\) from the leading eigenvector is a projective arc of length \(2r\). Any such arc containing the entire parameter arc must have \(2r\ge L\), and equality is attained by centering the parameter arc at the leading eigenvector. By the strict monotonicity above, the smallest possible maximum squared residual equals \(e_q(L/2)^2=M_q(L)^2\). When \(0<L<\pi\), the centering ray is unique modulo \(\pi\); when \(L=\pi\), the entire projective circle is traversed for any input ray and the maximum is \(a^2\).

**3. The full worst-error distribution.** A nonzero isotropic Gaussian vector has uniform projective angle \(\phi\in[0,\pi)\). The parameter arc contains the weak-eigenvector ray, where the squared residual is \(a^2\), precisely for a set of angles of length \(L\); hence its probability is \(L/\pi\).

On the complementary event the weak-eigenvector ray lies in the missing arc of length \(\pi-L\). Let \(d\) be its shortest projective distance to the parameter arc. Then \(0<d\le(\pi-L)/2\) and, for \(u\in[0,(\pi-L)/2]\), the unconditional probability \(\mathbb P\{d\ge u\}\) equals \((\pi-L-2u)/\pi\). At this distance, the maximal squared error is
\[
z(d)=\frac{b^2a^{2m}\sin^2d+a^2b^{2m}\cos^2d}
{a^{2m}\sin^2d+b^{2m}\cos^2d},
\]
which decreases strictly as \(d\) increases. Solving \(z=z(d)\) yields \(d=\delta_m(z)\), as stated. Therefore \(\mathbb P\{W_q^2\le z\}=\mathbb P\{d\ge\delta_m(z)\}=(\pi-L-2\delta_m(z))/\pi\) for the indicated interior range. The endpoints give the claimed atom and complete distribution.

**4. Exact half-turn integral for \(q=0\).** With \(m=1\), the numerator in the residual formula simplifies to \(a^2b^2\). Thus
\[
\begin{aligned}
\int_0^\pi e_0(\phi-t)^2\,dt
&=a^2b^2\int_0^\pi\frac{dt}{a^2\cos^2t+b^2\sin^2t}\\
&=2a^2b^2\int_0^\infty\frac{du}{a^2+b^2u^2}\\
&=\pi ab.
\end{aligned}
\]
Periodicity eliminates \(\phi\). The positive-definite spectrum \(a>b\) makes the best rank-one error at each parameter exactly \(b\), proving both ratios.

**5. Finite power iteration cannot remove the half-turn barrier.** At the parameter for which the fixed input ray coincides with the weaker eigenvector, every finite odd power \(A(t)^{2q+1}\omega\) remains on that eigenvector. Its range projection misses the leading eigenvector, so the residual is \(a\), completing the all-depth claim.

## Verification

The standalone `verify.py` uses exact rational matrices and `fractions.Fraction` to check the residual identity at power depths \(q=0,1,2\) for multiple input vectors. It also checks the analytical minimax formula against finite angular searches, the half-turn integral by midpoint quadrature for several spectra and phases, and the Gaussian-angle atom and distribution formula against deterministic angular grids. Its recorded terminal output is:

`VERIFY_OK: exact matrix identities, sharp-angle checks, half-turn quadrature, atom geometry`

These finite checks are consistency tests, not proofs of the continuum, probability distribution, or all-depth quantifiers; those follow from the calculations above.

## Relationship to prior work

Kressner and Lam, *Randomized low-rank approximation of parameter-dependent matrices* (arXiv:2302.12761, first submitted 2023-02-24), introduce fixed random test matrices for parameter-dependent HMT and Nyström approximations. Their article proves an integrated expectation bound (Theorem 4) and a uniform-error probability estimate (Theorem 7), with at least two or four oversampling columns and target rank at least two under their stated hypotheses. Their Remark 1 also explicitly notes that a parameter-dependent projection error may be discontinuous at a rank drop. The result here analyzes a distinct unoversampled target-rank-one boundary: it gives an exact continuum minimax error, complete random maximum-error distribution, and a pathwise integral for a continuously rotating, everywhere nonsingular and uniformly gapped positive-definite family. It neither invalidates nor extends their oversampled theorem by implication.

Diouane, Gürol, Di Perrotolo, and Vasseur, *A general error analysis for randomized low-rank approximation methods* (arXiv:2206.08793, 2022), establish projection-error bounds for a single fixed matrix, including deterministic canonical-angle estimates and Gaussian covariance-dependent expectations. Those pointwise bounds do not supply the rotating-parameter minimax and exact shared-probe distribution here. Classical randomized rangefinding and power iteration are described by Halko, Martinsson, and Tropp (arXiv:0909.4061) and Tropp and Webber (arXiv:2306.12418), respectively.

## Limitations

This is an exact two-dimensional construction for a shared single-column sketch, not a lower bound for all low-rank approximation algorithms. It says nothing adverse about the source's oversampled high-probability guarantees. The parametric failure is a continuum worst case and is not necessarily visible in a finite parameter grid. A two-column Gaussian sketch of these invertible \(2\times2\) matrices spans the full space almost surely; a subsequent rank-one SVD truncation then achieves the optimal error \(b\). No claim is made for independently redrawn sketches at each parameter, non-Gaussian angle distributions (except deterministic conclusions), noisy arithmetic, or finite-time discretizations of the parameter. Unidentified equivalent prior observations remain possible.

## References

1. D. Kressner and H. Y. Lam, *Randomized low-rank approximation of parameter-dependent matrices*, arXiv:2302.12761, first posted 2023-02-24; *Numerical Linear Algebra with Applications* 31 (2024), e2576. https://arxiv.org/abs/2302.12761 ; https://onlinelibrary.wiley.com/doi/10.1002/nla.2576
2. Y. Diouane, S. Gürol, A. Scotto Di Perrotolo, and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, 2022. https://arxiv.org/abs/2206.08793
3. N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, 2009; *SIAM Review* 53 (2011). https://arxiv.org/abs/0909.4061
4. J. A. Tropp and R. J. Webber, *Randomized algorithms for low-rank matrix approximation: Design, analysis, and applications*, arXiv:2306.12418, 2023. https://arxiv.org/abs/2306.12418
