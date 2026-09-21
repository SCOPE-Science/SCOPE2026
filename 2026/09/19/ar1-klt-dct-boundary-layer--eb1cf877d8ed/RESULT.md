# A 1/N boundary layer in the DCT endpoint of the AR(1) KLT

## Result

Let
\[
R_N(\rho)=\bigl[\rho^{|i-j|}\bigr]_{i,j=0}^{N-1},\qquad 0\le \rho<1,
\]
and let \(v_N\) be the unit Perron eigenvector of \(R_N(\rho_N)\), chosen entrywise positive. Let
\[
d_N=N^{-1/2}(1,\ldots,1)^\top
\]
be the DC row of the orthonormal DCT-II, and define the joint size/correlation parameter
\[
\kappa_N=N(1-\rho_N).
\]

The fixed-size statement \(\rho\to1\Rightarrow\mathrm{KLT}\to\mathrm{DCT\!\!\!-II}\) has a sharp non-uniform boundary layer when \(N\) also grows.

### Theorem 1: exact top-mode transition

If \(\kappa_N\to\kappa\in[0,\infty)\), then
\[
\langle v_N,d_N\rangle\longrightarrow A(\kappa),
\]
where \(x=x(\kappa)\in[0,\pi)\) is the unique solution of
\[
\boxed{x\tan(x/2)=\kappa}
\]
and
\[
\boxed{
A(\kappa)=
\frac{2\sin(x/2)/x}
{\sqrt{\tfrac12+\tfrac{\sin x}{2x}}}
}
\]
with the continuous convention \(A(0)=1\).

If instead \(\kappa_N\to\infty\), then
\[
\boxed{
\langle v_N,d_N\rangle\longrightarrow \frac{2\sqrt2}{\pi}
=0.900316316157\ldots
}
\]
and hence the limiting principal angle is
\[
\boxed{
\arccos(2\sqrt2/\pi)=25.8003232176\ldots^\circ .
}
\]

Consequently,
\[
\boxed{
\|v_N-d_N\|_2\to0
\quad\Longleftrightarrow\quad
N(1-\rho_N)\to0.
}
\]
Thus \(1-\rho=o(N^{-1})\) is the exact scale for convergence of the leading AR(1) KLT vector to the DCT-II DC vector. Merely assuming \(\rho_N\to1\) is insufficient.

For small \(\kappa\),
\[
\arccos A(\kappa)
=
\frac{\kappa}{6\sqrt5}+O(\kappa^2).
\]

### Proof

The AR(1) precision matrix is tridiagonal and its normalized eigenvectors may be written in sinusoidal form. For the first, symmetric mode, the exact secular equation is
\[
\cos\frac{(N+1)\omega_N}{2}
=
\rho_N\cos\frac{(N-1)\omega_N}{2}.
\]
Putting \(x_N=N\omega_N\) and rearranging gives the exact identity
\[
\tan(x_N/2)\tan(x_N/(2N))
=
\frac{1-\rho_N}{1+\rho_N},
\]
or
\[
\tan(x_N/2)\,[2N\tan(x_N/(2N))]
=
\frac{2\kappa_N}{1+\rho_N}.
\]
The first frequency satisfies \(0<x_N<\pi\). If \(\kappa_N\to\kappa<\infty\), then \(\rho_N\to1\), every subsequential limit satisfies \(x\tan(x/2)=\kappa\), and strict monotonicity on \([0,\pi)\) gives uniqueness. If \(\kappa_N\to\infty\), the right side diverges while \(2N\tan(x_N/(2N))\) stays bounded, forcing \(x_N\to\pi\).

The same symmetric mode has the centered-cosine form
\[
(v_N)_j\propto
\cos\!\left(\omega_N\left(j-\frac{N-1}{2}\right)\right).
\]
Finite trigonometric sums therefore give the exact cosine similarity
\[
\langle v_N,d_N\rangle
=
\frac{\sin(N\omega_N/2)/\sin(\omega_N/2)}
{\sqrt{N\left[N/2+\sin(N\omega_N)/(2\sin\omega_N)\right]}}.
\]
Substituting \(x_N=N\omega_N\) and taking limits yields \(A(\kappa)\), while \(x_N\to\pi\) yields \(2\sqrt2/\pi\).

If \(\kappa_N\to0\), the displayed formula gives convergence to one. Conversely, if \(\kappa_N\not\to0\), an extended-real subsequence has \(\kappa_N\to\kappa\in(0,\infty]\); its limiting cosine is strictly less than one because the limiting cosine profile is nonconstant. This proves the iff statement. Finally,
\[
x^2=2\kappa-\frac13\kappa^2+O(\kappa^3),
\qquad
A=1-\frac{x^4}{1440}+O(x^6),
\]
which gives the small-\(\kappa\) angle expansion.

## Consequence for the exact fast KLT factorization

Reznik (2026) factors the even-order AR(1) KLT as
\[
W_N
=P_N\,\operatorname{blockdiag}(Q_s C_{N/2}^{II},Q_a C_{N/2}^{IV})B_N,
\]
whereas the classical Chen DCT-II factorization is obtained by replacing \(Q_s,Q_a\) by identities. After the standard row ordering and sign alignment,
\[
\|W_N-C_N^{II}\|_2
=
\max\{\|Q_s-I\|_2,\|Q_a-I\|_2\}.
\]
Since operator norm dominates the distance between corresponding unit rows, Theorem 1 implies that for any even sequence with \(\kappa_N\to\kappa>0\),
\[
\boxed{
\liminf_{N\to\infty}
\max\{\|Q_s-I\|_2,\|Q_a-I\|_2\}
\ge
\sqrt{2-2A(\kappa)}>0.
}
\]
For \(\kappa=\infty\), the lower bound is
\[
\boxed{
\sqrt{2-4\sqrt2/\pi}
=0.446505730854\ldots .
}
\]
Hence the fixed-\(N\) statement \(Q_s,Q_a\to I\) as \(\rho\to1\) is not uniform in transform size. A necessary condition for the correction factors to vanish in operator norm along growing sizes is
\[
1-\rho=o(N^{-1}).
\]
This is a necessary condition only; no uniform sufficiency claim for the full transform is made here.

## Fixed-mode Robin limit

The same scale governs every fixed spectral mode. Let \(\omega_{m,N}\) be the \(m\)-th KLT frequency and suppose \(\kappa_N\to\kappa\in(0,\infty)\). Then
\[
x_{m,N}:=N\omega_{m,N}\longrightarrow x_m(\kappa),
\]
where \(x_m\in((m-1)\pi,m\pi)\) is the unique solution of
\[
\boxed{
x_m+2\arctan(x_m/\kappa)=m\pi.
}
\]
Under piecewise-constant interpolation of the normalized discrete eigenvector, the mode converges in \(L^2(0,1)\) to the normalized function
\[
\phi_{m,\kappa}(s)
\propto
\sin\!\left(x_m s+\frac{m\pi-x_m}{2}\right),
\]
which satisfies
\[
\boxed{
\phi'(0)=\kappa\phi(0),\qquad
\phi'(1)=-\kappa\phi(1).
}
\]
Moreover,
\[
\boxed{
\frac{\lambda_{m,N}}{N}
\longrightarrow
\frac{2\kappa}{\kappa^2+x_m(\kappa)^2}.
}
\]
At \(\kappa\downarrow0\), the frequencies tend to the DCT grid \((m-1)\pi\); at \(\kappa\to\infty\), they tend to the sine-grid values \(m\pi\). The continuum Robin eigenproblem itself is classical; the point here is that the exact discrete AR(1) secular equation identifies \(N(1-\rho)\) as its joint KLT/DCT transition parameter.

## Why classical transform-coding performance can still look DCT-like

Basis nonconvergence need not imply poor energy compaction. For the DCT DC vector \(d_N\), define its captured variance
\[
r_N=d_N^\top R_N(\rho_N)d_N.
\]
When \(\kappa_N\to\kappa\in(0,\infty)\), a Riemann-sum limit gives
\[
\frac{r_N}{N}
\longrightarrow
J(\kappa)
=
\frac{2(\kappa-1+e^{-\kappa})}{\kappa^2},
\]
whereas the optimal first KLT eigenvalue obeys
\[
\frac{\lambda_{1,N}}{N}
\longrightarrow
\Lambda_1(\kappa)
=
\frac{2\kappa}{\kappa^2+x(\kappa)^2}.
\]
Thus the leading-mode Rayleigh efficiency has the explicit limit
\[
\boxed{
\frac{r_N}{\lambda_{1,N}}
\longrightarrow
E(\kappa)
=
\frac{(\kappa-1+e^{-\kappa})(\kappa^2+x(\kappa)^2)}{\kappa^3}.
}
\]
It tends to one as \(\kappa\downarrow0\) and also as \(\kappa\to\infty\), even though the top eigenvector angle tends to \(25.8^\circ\) in the latter limit. This gives a concrete mechanism by which classical asymptotic performance equivalence of DCT and KLT can coexist with a nonvanishing basis/operator discrepancy.

## Verification

`artifacts/verify_boundary_layer.py` evaluates the exact finite-\(N\) secular formula and independently diagonalizes moderate AR(1) covariance matrices. For example, at \(N=256\), the direct top-mode overlaps for \(\kappa=0.1,1,5,20\) are respectively
\[
0.999972867535,\quad
0.997800519946,\quad
0.975898414208,\quad
0.934014776093,
\]
converging toward the predicted limits
\[
0.999972875930,\quad
0.997807929634,\quad
0.976154287172,\quad
0.935044953425.
\]
The artifact also checks the limiting leading-mode energy-efficiency formula.

## Relation to prior literature and originality scope

The following ingredients are established prior work and are not claimed as new: the exact AR(1) eigenstructure and sinusoidal secular equations; the fixed-\(N\), \(\rho\to1\) convergence to DCT-II; DCT/KLT transform-coding performance comparisons and asymptotic performance equivalence; the continuum exponential-kernel/Robin eigenproblem; and Reznik's DCT-core plus orthogonal-correction factorization.

The contribution claimed here, to the best of our knowledge, is the **joint local-to-unity classification** \(N(1-\rho)\), including the exact top-mode limiting angle and iff threshold, its quantitative non-uniformity consequence for Reznik's correction factors, the fixed-mode discrete-to-Robin transition derived from the exact AR(1) secular equation, and the explicit reconciliation between nonvanishing basis angle and near-optimal leading-mode Rayleigh performance.

No matching SCOPE record was found by searches for the AR(1) KLT/DCT object, Kac--Murdock--Szegő terminology, the source preprint, and synonymous KLT/cosine-transform formulations. External searches likewise found classical endpoint and performance-equivalence literature but no statement of the joint \(N(1-\rho)\) transition above. Because older transform literature is broad and some relevant full texts were not inspected, this is not a claim of exhaustive literature coverage.

## Limitations

- The sharp iff theorem concerns the **leading KLT mode versus the DCT DC mode**. It does not prove a full-basis operator-norm iff theorem.
- The lower bound on \(Q_s,Q_a\) proves non-uniformity and a necessary scale for their operator convergence; it does not prove that \(N(1-\rho)\to0\) is sufficient for the entire correction matrices.
- The fixed-mode statements hold mode-by-mode and do not by themselves control modes whose indices grow with \(N\).
- The Rayleigh-efficiency formula concerns only the leading DCT component, not total coding gain or rate-distortion performance.
- Full texts of Jain (1979), Unser (1984), Clarke (1981), and Sherman (2023) were not all inspected. Their accessible abstracts, secondary expositions, and cited descriptions concern sinusoidal families, performance equivalence, fixed-size endpoint behavior, or exact finite-\(N\) eigenstructure; they remain the most plausible sources of unobserved overlap.
- Reznik's motivating preprint is recent, so contemporaneous or not-yet-indexed follow-up work remains possible.

## References

1. Y. A. Reznik, “Exact fast factorizations of the AR(1) Karhunen–Loève transform,” arXiv:2609.20221, 2026. https://arxiv.org/abs/2609.20221
2. R. J. Clarke, “Relation between the Karhunen–Loève and cosine transforms,” *IEE Proceedings F*, 128(6), 359–360, 1981. https://doi.org/10.1049/ip-f-1.1981.0061
3. A. K. Jain, “A sinusoidal family of unitary transforms,” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, PAMI-1(4), 356–365, 1979. https://doi.org/10.1109/TPAMI.1979.4766944
4. M. Unser, “On the approximation of the discrete Karhunen–Loève transform for stationary processes,” *Signal Processing*, 7(3), 231–249, 1984. https://doi.org/10.1016/0165-1684(84)90002-1
5. M. U. Torun and A. N. Akansu, “An efficient method to derive explicit KLT kernel for first-order autoregressive discrete process,” *IEEE Transactions on Signal Processing*, 61(15), 3944–3953, 2013. https://doi.org/10.1109/TSP.2013.2265225
6. P. J. Sherman, “On the eigenstructure of the AR(1) covariance,” *IEEE Statistical Signal Processing Workshop*, 2023. https://doi.org/10.1109/SSP53291.2023.10208005
