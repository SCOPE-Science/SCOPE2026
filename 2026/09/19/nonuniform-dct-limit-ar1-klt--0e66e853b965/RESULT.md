# The AR(1) KLT-to-DCT endpoint is nonuniform in block length

## Statement

Let
\[
R_N(\rho)=\big[\rho^{|i-j|}\big]_{i,j=0}^{N-1},\qquad 0<\rho<1,
\]
and let \(W_N(\rho)\) be the orthogonal Karhunen--Loève transform (KLT) whose rows are the eigenvectors of \(R_N(\rho)\), ordered by decreasing eigenvalue and with the first row chosen positive. For fixed \(N\), the classical limit \(\rho\to1\) is the DCT-II. Recent exact factorizations of the AR(1) KLT likewise have correction factors that tend to the identity at fixed block length.

That endpoint is not uniform in \(N\). The sharp low-mode boundary scale is
\[
c_N=N(1-\rho_N).
\]
For every fixed mode index \(m\ge1\), if \(\rho_N\to1\) and \(c_N\to c\in(0,\infty)\), then, writing \(\omega_{m,N}\) for the exact AR(1) eigenfrequency and \(x_{m,N}=N\omega_{m,N}\),
\[
\boxed{x_{m,N}\longrightarrow x_m(c)},
\]
where \(x_m(c)\in((m-1)\pi,m\pi)\) is the unique solution of
\[
\boxed{\tan\!\left(\frac{m\pi-x}{2}\right)=\frac{x}{c}.}
\]
With the usual piecewise-constant embedding of a unit Euclidean eigenvector into \(L^2[-1/2,1/2]\), the normalized mode converges to
\[
\boxed{
\phi_{m,c}(t)=
\frac{\sin\!\left(m\pi/2+x_m(c)t\right)}
{\left(\int_{-1/2}^{1/2}\sin^2\!\left(m\pi/2+x_m(c)t\right)\,dt\right)^{1/2}}
}.
\]
For \(c>0\), the corresponding eigenvalue satisfies
\[
\boxed{
\frac{\lambda_{m,N}}{N}\longrightarrow
\frac{2c}{c^2+x_m(c)^2}.
}
\]
The two endpoint mode profiles are obtained continuously:
\[
x_m(0)=(m-1)\pi \quad\text{(DCT/Neumann side)},
\qquad
x_m(\infty)=m\pi \quad\text{(Dirichlet side)}.
\]
Thus \(\rho_N\to1\) alone is insufficient to force even the lowest KLT modes toward DCT-II. The parameter that decides the low-mode shape is correlation length relative to block length, represented here by \(N(1-\rho_N)\).

## A sharp first-row obstruction

For \(m=1\), \(x=x_1(c)\) is equivalently characterized by
\[
\boxed{c=x\tan(x/2)},\qquad x\in[0,\pi].
\]
The limiting first KLT row is a normalized centered cosine \(\cos(xt)\), whereas the first DCT-II row is constant. Their limiting overlap is
\[
A(c)=
\frac{2\sin(x/2)/x}
{\sqrt{\tfrac12+\tfrac{\sin x}{2x}}},
\]
and the sign-aligned Euclidean row distance is
\[
\boxed{D(c)=\sqrt{2-2A(c)}}.
\]
For every \(c>0\), \(D(c)>0\). Consequently,
\[
\boxed{
\liminf_{N\to\infty}\|W_N(\rho_N)-C_N^{\mathrm{II}}\|_2\ge D(c)>0
}
\]
whenever \(N(1-\rho_N)\to c>0\), under the natural common frequency ordering and sign convention. In particular, for any sequence \(\rho_N\to1\), the first KLT row converges to the DCT DC row **if and only if**
\[
\boxed{N(1-\rho_N)\to0.}
\]
For small \(c\),
\[
D(c)=\frac{c}{\sqrt{180}}+O(c^2),
\]
so the deterioration begins linearly in the scaled boundary parameter.

A particularly stark example is
\[
\rho_N=1-N^{-1/2}.
\]
Then \(\rho_N\to1\) but \(N(1-\rho_N)\to\infty\), and the first KLT profile tends to the normalized Dirichlet mode \(\sqrt2\cos(\pi t)\). Hence
\[
A(\infty)=\frac{2\sqrt2}{\pi},
\qquad
\boxed{
D(\infty)=\sqrt{2-\frac{4\sqrt2}{\pi}}
=0.446505730854\ldots .
}
\]
Adjacent-sample correlation therefore can tend to one while the leading KLT vector remains a fixed, macroscopic distance from the DCT DC vector.

## Structural explanation

The exact inverse covariance admits the tridiagonal form
\[
T_N(\rho)=(1-\rho^2)R_N(\rho)^{-1}.
\]
Let \(L_N\) be the standard DCT-II second-difference generator,
\[
L_N=
\begin{pmatrix}
1&-1&&\\
-1&2&\ddots&\\
&\ddots&\ddots&-1\\
&&-1&1
\end{pmatrix},
\]
and let
\[
E_N=e_0e_0^T+e_{N-1}e_{N-1}^T,
\qquad \delta=1-\rho.
\]
A direct entrywise calculation gives the exact identity
\[
\boxed{
T_N(\rho)=\rho\big(L_N+\delta E_N\big)+\delta^2 I.
}
\]
Therefore the KLT eigenvectors are exactly those of a DCT-II discrete Laplacian with a boundary-mass perturbation \(\delta E_N\). Low DCT modes have endpoint amplitudes of order \(N^{-1/2}\), while their lowest spectral gaps are order \(N^{-2}\); a boundary perturbation of size \(\delta\) therefore becomes order one at \(N\delta\asymp1\). The limiting Robin equation above is the continuum manifestation of this boundary layer.

This identity also explains why the two limits do not commute. Taking \(\rho\to1\) first at fixed \(N\) eliminates the boundary perturbation and yields DCT-II. Taking \(N\to\infty\) first with fixed \(0<\rho<1\), or more generally with \(N(1-\rho_N)\to\infty\), yields the Dirichlet low-mode profile; sending \(\rho\to1\) afterward does not recover the constant first mode.

## Consequence for exact fast factorizations

The motivating exact factorization for even \(N\) writes the AR(1) KLT using the same butterfly and half-size DCT-II/DCT-IV cores as the Chen DCT-II factorization, followed by \(\rho\)-dependent orthogonal correction factors. It proves that these corrections tend to identity when \(\rho\to1\) for fixed \(N\).

The lower bound above shows that this identity limit cannot be uniform in block length. Along any critical sequence \(N(1-\rho_N)\to c>0\), the complete correction stage, expressed in the compatible ordering of the source factorization, must remain a nonzero operator-norm distance from identity; otherwise multiplication by the common orthogonal core would force \(W_N(\rho_N)-C_N^{\mathrm{II}}\to0\), contradicting the first-row bound. In the Dirichlet-side regime, that obstruction is at least \(0.446505730854\ldots\).

This does not contradict the fixed-\(N\) theorem. It supplies the missing quantifier: for large blocks, "\(\rho\) close to one" must be interpreted relative to \(N\), and the DCT endpoint is a uniform approximation to the leading mode only on the stricter scale \(1-\rho=o(N^{-1})\).

## Proof

The exact phase equation for the \(m\)-th AR(1) mode is
\[
(N+1)\omega_{m,N}+2\theta_N(\omega_{m,N})=m\pi,
\]
with
\[
\tan\theta_N(\omega)
=\frac{\rho_N\sin\omega}{1-\rho_N\cos\omega},
\qquad 0<\theta_N<\pi/2.
\]
Set \(x_{m,N}=N\omega_{m,N}\). The phase equation places \(x_{m,N}\) in a compact interval approaching \([(m-1)\pi,m\pi]\). Along any convergent subsequence \(x_{m,N}\to x\), if \(N(1-\rho_N)\to c\in(0,\infty)\), then
\[
N\rho_N\sin(x_{m,N}/N)\to x,
\]
while
\[
N\big(1-\rho_N\cos(x_{m,N}/N)\big)
=N(1-\rho_N)+N\rho_N\big(1-\cos(x_{m,N}/N)\big)
\to c.
\]
Therefore \(\tan\theta_N\to x/c\). The phase equation also gives
\[
\theta_N\to\frac{m\pi-x}{2},
\]
so every subsequential limit solves
\[
\tan\left(\frac{m\pi-x}{2}\right)=\frac{x}{c}.
\]
On \(((m-1)\pi,m\pi)\), the left side minus \(x/c\) is strictly decreasing from \(+\infty\) to a negative value, giving a unique root and hence convergence of the full sequence. The cases \(c=0\) and \(c=\infty\) follow from the same phase balance, forcing \(\theta\to\pi/2\) and \(\theta\to0\), respectively.

Using the phase equation inside the exact eigenvector formula gives the centered representation
\[
w_{m,N}(k)\propto
\sin\!\left(\frac{m\pi}{2}+\omega_{m,N}\left(k-\frac{N-1}{2}\right)\right).
\]
Riemann-sum normalization then yields \(\phi_{m,c}\). Finally,
\[
\lambda_{m,N}
=\frac{1-\rho_N^2}
{(1-\rho_N)^2+2\rho_N(1-\cos\omega_{m,N})},
\]
and multiplication of numerator and denominator by the appropriate powers of \(N\) gives the stated \(\lambda_{m,N}/N\) limit.

For \(m=1\), the finite and limiting profiles are positive centered cosines. Integrating the limiting profile against the unit constant function gives \(A(c)\), and unit-vector geometry gives \(D(c)\). The spectral norm of a matrix dominates the Euclidean norm of any row, establishing the operator lower bound. The iff criterion follows by compactifying \(c_N\) to \([0,\infty]\): every subsequential limit with \(c>0\), including \(c=\infty\), has positive row distance, whereas \(c_N\to0\) forces \(x_{1,N}\to0\).

## Verification

`artifacts/verify_ar1_dct_boundary.py` evaluates the exact phase equation, the critical roots, eigenvalue limits, and row-distance formulas. It also directly diagonalizes moderate-size covariance matrices with NumPy and compares their Perron eigenvectors against the closed-form first mode. `artifacts/verification_output.txt` records the output obtained with Python and NumPy 2.3.5.

For example, at \(c=1\) the limiting first frequency and row distance are
\[
x_1(1)=1.306542374188806\ldots,
\qquad
D(1)=0.066212844165043\ldots.
\]
At \(N=1024\) with \(\rho=e^{-1/N}\), the exact finite values are
\[
N\omega_1=1.306542254756973\ldots,
\qquad
\|w_1-d_{\rm DC}\|_2=0.066212678037569\ldots.
\]
For \(N=256\), direct dense diagonalization agrees with the closed-form first mode to \(9.9\times10^{-16}\) in Euclidean norm.

## Prior literature and novelty boundary

The finite-dimensional AR(1) KLT eigenproblem, its sinusoidal eigenvectors, the associated transcendental equations, and the fixed-block limit to DCT-II are classical. Clarke's 1981 result is the standard DCT endpoint reference. Torun and Akansu (2013) give explicit discrete AR(1) KLT kernels and also discuss the corresponding continuous exponential-covariance KLE; continuous Robin transcendental equations for the exponential kernel are therefore not claimed as new here. The recent Reznik factorization supplies the exact DCT-core-plus-correction structure motivating the uniformity question.

The contribution claimed here is restricted to the **joint large-block/high-correlation boundary law** for this transform: the critical variable \(N(1-\rho)\), the fixed-mode interpolation between DCT/Neumann and Dirichlet profiles, the explicit first-row distance \(D(c)\), the iff criterion for convergence of the leading KLT vector to the DCT DC row, the noncommuting limits, and the resulting nonuniformity of the identity correction-factor limit in the recent exact factorization.

## Limitations

The theorem concerns fixed low mode indices as \(N\to\infty\). It does not provide a uniform approximation for all \(N\) KLT modes, a coding-gain bound, or an end-to-end complexity comparison between the exact factorization and DCT-II. The operator-norm nonconvergence statement is a lower bound inherited from the first row; it does not characterize the full correction spectrum. The continuous exponential-kernel eigenproblem is prior art, and the present novelty claim is only the discrete-to-DCT nonuniformity and its factorization consequence.

## References

1. Y. A. Reznik, "Exact fast factorizations of the AR(1) Karhunen--Loève transform," arXiv:2609.20221v1, 2026. https://arxiv.org/abs/2609.20221
2. M. U. Torun and A. N. Akansu, "An Efficient Method to Derive Explicit KLT Kernel for First-Order Autoregressive Discrete Process," IEEE Transactions on Signal Processing 61(15), 3944--3953, 2013. https://doi.org/10.1109/TSP.2013.2265225
3. R. J. Clarke, "Relation between the Karhunen--Loève and cosine transforms," IEE Proceedings F 128(6), 359--360, 1981. https://doi.org/10.1049/ip-f-1.1981.0061
