# Arithmetic lattice phases of the projection functional for a pole–ring spherical design

## Finding
For every integer \(n\ge5\), form the \(n+1\) unit vectors in \(\mathbb R^3\)
\[
u_0=(0,0,1),\qquad
u_{j+1}=\frac{1}{\sqrt5}\left(2\cos\frac{2\pi j}{n},2\sin\frac{2\pi j}{n},1\right),\quad 0\le j<n.
\]
With weights \(w_0=1/6\) and \(w_{j+1}=5/(6n)\), they are a weighted spherical projective \((2,2)\)-design; specifically,
\[\sum_{i=0}^{n}w_i\langle u_i,x\rangle^4=\|x\|_2^4/5\quad(x\in\mathbb R^3).\]
Set \(v_i=\sqrt{3w_i}\,u_i\), and let \(G_n=(\langle v_i,v_j\rangle)_{0\le i,j\le n}\). Then \(G_n\) is an orthogonal projection of rank three. The **specified frame projection functional**, not a global optimization over arbitrary frames or sign matrices, is
\[
L_n:=\max_{t_i\ge0,\ \sum_{i=0}^n t_i^2=1}\sum_{i,j=0}^n t_i t_j |(G_n)_{ij}|=\rho(|G_n|).
\]
Write
\[
\theta=\arccos(-1/4),\qquad \alpha=\theta/(2\pi),\qquad
r_n=\lfloor n\alpha\rfloor,
\]
\[
a_n=-1+\frac{4r_n+2}{n}+
\frac8n\frac{\sin((2r_n+1)\pi/n)}{\sin(\pi/n)},\qquad
\Phi(a)=\frac{1+a+\sqrt{(a-1)^2+4}}4.
\]
**Exact all-size formula:** \(L_n=\Phi(a_n)\) for every integer \(n\ge5\). In particular, \(L_5=(1+\sqrt5)/2\) and \(L_6=(11+\sqrt{61})/12\).

Put
\[
a_*=\frac{2\theta+2\sqrt{15}}\pi-1,\quad
L_*=\Phi(a_*),\quad
C=4\pi\sqrt{15}\,\Phi'(a_*),\quad
\Phi'(a)=\frac14\left(1+\frac{a-1}{\sqrt{(a-1)^2+4}}\right).
\]
Then \(L_*=1.551088238794851\ldots\) and \(C=19.844172572692855\ldots>0\). If \(B_2(s)=s^2-s+1/6\) for \(0\le s<1\), the precise asymptotic law is
\[
\boxed{L_n=L_*-\frac{C}{n^2}B_2(\{n\alpha\})+O(n^{-3})}\qquad(n\to\infty).
\]
The constant implicit in \(O(n^{-3})\) is independent of \(n\). Since \(\alpha\) is irrational,
\[
\boxed{\limsup_{n\to\infty}n^2(L_n-L_*)=C/12,\qquad
\liminf_{n\to\infty}n^2(L_n-L_*)=-C/6.}
\]
Thus the convergence of this natural projection-functional sequence has a sharp sign-changing second-order arithmetic phase, not a constant second-order coefficient.

## Assumptions and scope
All vectors and inner products are real and Euclidean. The number of equispaced latitude points is an arbitrary integer \(n\ge5\). Matrix absolute value \(|G_n|\) is **entrywise**, and \(\rho\) is spectral radius. The functional \(L_n\) is evaluated at the displayed frame and optimized only over nonnegative unit weights \(t\); it is not the maximal relative projection constant obtained by optimizing over alternative matrices with the same signs. No assertion of global extremality of this design is made.

## Proof
**1. Design and tight-frame normalization.** Write \(x=(X,Y,Z)\), \(R^2=X^2+Y^2\). Because \(n\ge5\), discrete averaging of a trigonometric polynomial of degree at most four over the regular \(n\)-gon agrees with integration over the circle. Consequently
\[
\frac1n\sum_{j=0}^{n-1}(2X\cos(2\pi j/n)+2Y\sin(2\pi j/n)+Z)^4
=6R^4+12R^2Z^2+Z^4.
\]
Multiplying by the ring's total weight \(5/6\) and by \(5^{-2}\), then adding the pole's \(Z^4/6\), gives \((R^2+Z^2)^2/5\). Polarizing, or directly averaging second moments, yields \(\sum_iw_i u_i u_i^{\mathsf T}=I_3/3\). Therefore \(\sum_i v_i v_i^{\mathsf T}=I_3\); the matrix with columns \(v_i\) has orthonormal rows, so \(G_n\) is a rank-three orthogonal projection. The same fixed pole–ring geometry is uniquely determined among positive one-pole/one-latitude rotationally invariant fourth-moment designs by \(w+(1-w)z=1/3\) and \(w+(1-w)z^2=1/5\), whose nondegenerate solution is \(z=1/5\), \(w=1/6\).

**2. Spectral reduction.** The normalized columns are
\[
v_0=(0,0,1/\sqrt2),\qquad
v_{j+1}=(2\cos(2\pi j/n),2\sin(2\pi j/n),1)/\sqrt{2n}.
\]
Hence \(|\langle v_0,v_{j+1}\rangle|=1/(2\sqrt n)\) and
\[
|\langle v_{j+1},v_{k+1}\rangle|=
\frac{|1+4\cos(2\pi(j-k)/n)|}{2n}.
\]
The entrywise absolute Gram matrix is strictly positive, so Perron–Frobenius gives a unique positive leading eigenvector. Rotations of the ring commute with this matrix, forcing that vector to be constant on the ring coordinates. Compression to the pole and normalized all-ones ring vector yields exactly
\[
\frac12\begin{pmatrix}1&1\\1&a_n\end{pmatrix},\qquad
 a_n=\frac1n\sum_{k=0}^{n-1}|1+4\cos(2\pi k/n)|.
\]
Its largest eigenvalue is \(\Phi(a_n)\), and positivity shows it is \(\rho(|G_n|)\). For any symmetric entrywise nonnegative matrix, the maximum Rayleigh quotient is attained on a nonnegative vector; this proves the formula for the stated functional.

**3. Exact trigonometric sum.** The sign of \(1+4\cos t\) changes at \(t=\theta\) and \(2\pi-\theta\). These zeros never land on the \(n\)-grid: otherwise \(2\cos\theta=-1/2\) would be both a rational number and an algebraic integer because \(e^{i\theta}\) would be a root of unity; a rational algebraic integer is an integer. The positive samples are exactly the indices \(0,\pm1,\ldots,\pm r_n\) modulo \(n\). Because the full signed sample average is one, doubling the sum over positive indices and subtracting the full sum gives
\[
a_n=-1+\frac{2(2r_n+1)}{n}+
\frac8n\sum_{k=-r_n}^{r_n}\cos\frac{2\pi k}{n}.
\]
The finite cosine sum is \(\sin((2r_n+1)\pi/n)/\sin(\pi/n)\), as asserted. Substitution for \(n=5,6\) gives the two stated exact special values.

**4. Limit and lattice correction.** Define the continuous periodic function \(f(s)=|1+4\cos(2\pi s)|\). Its integral is
\[
\int_0^1 f(s)\,ds=\frac{2\theta+2\sqrt{15}}\pi-1=a_*.
\]
It is smooth except at \(s=\alpha\) and \(s=1-\alpha\), where its first derivative has the same upward jump \(4\pi\sqrt{15}\). Integrating its Fourier coefficients by parts twice separately on smooth intervals gives, for each nonzero integer \(m\),
\[
\widehat f(m)=-\frac{4\pi\sqrt{15}}{4\pi^2m^2}
\bigl(e^{-2\pi i m\alpha}+e^{2\pi i m\alpha}\bigr)
+O(|m|^{-3}).
\]
The error is summable uniformly after evaluating at nonzero multiples of \(n\). Discrete Fourier averaging, the absolutely convergent Bernoulli identity
\[
\sum_{\ell\in\mathbb Z\setminus\{0\}}\frac{e^{2\pi i\ell s}}{\ell^2}=2\pi^2B_2(\{s\}),
\]
and \(B_2(1-s)=B_2(s)\) now yield
\[
a_n-a_*=-\frac{4\pi\sqrt{15}}{n^2}B_2(\{n\alpha\})+O(n^{-3}).
\]
Since \(\Phi\) is analytic near \(a_*\), Taylor expansion proves the asserted asymptotic for \(L_n\). Irrationality of \(\alpha\), proved in step 3, makes \(\{n\alpha\}\) dense in \([0,1]\). Because the Bernoulli polynomial has minimum \(-1/12\) and maximum \(1/6\), the claimed limsup and liminf follow, with both bounds attained along subsequences.

## Verification
A standalone standard-library Python checker `verify_frame.py` replays the displayed finite cosine identity, Parseval property, positive spectral eigenvector, sample fourth moments, two small-size exact values, and Gaussian-free second-order phase diagnostics for fifteen indices from \(n=5\) through \(n=1000\). The checker passes. Its finite tests are diagnostics; the proof of the all-index statements is analytic and contained above.

## Relationship to prior work
Deręgowska and Lewandowska (arXiv:2608.08695v1, publicly posted August 9, 2026) study maximal projection constants, tight frames, and weighted spherical \((2,2)\)-designs. Hu and Tang's 2026 seven-vector counterexample uses the same one-pole/regular-six-point latitude geometry and establishes results for a different, globally optimized sign-matrix functional. Those constructions motivate examining a full regular-ring family; their cited conclusions do not give the exact all-\(n\) positive Gram spectral radius above or the Bernoulli-phase correction. General Fourier/Euler–Maclaurin quadrature identities supply a classical method for the correction and are not claimed as new. The new assertion is the complete concrete frame-family evaluation together with its sharp arithmetic convergence law.

## Limitations
The sequence \(L_n\) is a frame-dependent projection functional; it is not asserted to equal the maximal absolute projection constant in dimension three, nor any sign-matrix-optimized invariant. The pole+ring family is highly symmetric, and no theorem is given for perturbed or multiple-latitude configurations. Existing general quadrature results may provide alternate deductions of the asymptotic; novelty beyond the specifically evaluated family has not been claimed. Independent priority assessment remains necessary.

## References
1. B. Deręgowska and B. Lewandowska, *Maximal Projection Constants and Extremal Vector Configurations: Some Conjectures and Examples*, arXiv:2608.08695v1 (August 9, 2026), https://arxiv.org/abs/2608.08695.
2. T. Hu and Q. Tang, *A Seven-Vector Counterexample to a Conjecture on Maximal Projection Constants* (2026), publicly accessible author-uploaded manuscript.
3. Classical discrete Fourier summation and the Bernoulli-polynomial Fourier series, used solely as standard analytic tools.
