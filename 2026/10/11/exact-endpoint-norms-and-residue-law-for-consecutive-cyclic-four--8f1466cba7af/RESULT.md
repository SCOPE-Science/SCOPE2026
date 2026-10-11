# Exact endpoint norms and residue law for consecutive cyclic Fourier projections
## Finding
For integers \(N\ge m\ge2\), let \(P_{m,N}\) be the Fourier projection on \(\mathbb Z_N\), with normalized counting measure, onto the consecutive frequencies \(\{0,1,\ldots,m-1\}\). Its convolution kernel is
\[
D_m(j/N)=\sum_{\nu=0}^{m-1}e^{2\pi i\nu j/N},
\]
and therefore
\[
\|P_{m,N}\|_{\ell^\infty\to\ell^\infty}
=\|P_{m,N}\|_{\ell^1\to\ell^1}
=\frac1N\sum_{j=0}^{N-1}\left|D_m(j/N)\right|.
\]
Put \(b_k=\lfloor kN/m\rfloor\). Define \(A_{m,N}(M)\), for \(0\le M\le N\), by
\[
A_{m,N}(M)=
\begin{cases}
M-s+\displaystyle\sum_{r=1}^{s}\frac{\sin((2M+1)r\pi/N)}{\sin(r\pi/N)},&m=2s+1,\\[2mm]
-s+\displaystyle\sum_{r=1}^{s}\frac{\sin((2M+1)(2r-1)\pi/(2N))}{\sin((2r-1)\pi/(2N))},&m=2s.
\end{cases}
\]
Then
\[
\boxed{\displaystyle
\|P_{m,N}\|=
\frac1N\left((-1)^{m-1}A_{m,N}(N)+2\sum_{k=1}^{m-1}(-1)^{k-1}A_{m,N}(b_k)\right).}
\]
This is an exact all-\(m\), all-\(N\) formula with no absolute values and no sum whose length grows with \(N\) when \(m\) is fixed.

For the continuous comparison constant, define
\[
\Lambda_m=\int_0^1\left|\frac{\sin(m\pi x)}{\sin(\pi x)}\right|\,dx.
\]
If \(B_2(t)=t^2-t+1/6\), then for each fixed \(m\),
\[
\boxed{\displaystyle
\|P_{m,N}\|=\Lambda_m-
\frac{m\pi}{N^2}\sum_{k=1}^{m-1}\csc\!\left(\frac{\pi k}{m}\right)
B_2\!\left(\left\{\frac{Nk}{m}\right\}\right)+O_m(N^{-3}).}
\]
The coefficient is therefore a periodic function of \(N\bmod m\). It records, to second order, how the sampling grid meets or misses the \(m-1\) zeros of the length-\(m\) Dirichlet kernel.

## Assumptions and scope
The group is \(\mathbb Z_N\) with normalized counting measure \(N^{-1}\sum_{x\in\mathbb Z_N}\). The frequency set consists of \(m\) distinct consecutive characters, so \(2\le m\le N\). Translation of the frequency block only modulates the kernel and does not change the norm.

The asymptotic statement keeps \(m\) fixed while \(N\to\infty\). Its remainder \(O_m(N^{-3})\) is not asserted uniformly as \(m\) grows. The braces \(\{t\}\) denote fractional part in \([0,1)\).

For completeness, an elementary antiderivative of
\[
R_m(x)=\frac{\sin(m\pi x)}{\sin(\pi x)}
\]
is
\[
Q_m(x)=
\begin{cases}
x+\displaystyle\sum_{r=1}^{(m-1)/2}\frac{\sin(2\pi r x)}{\pi r},&m\text{ odd},\\[2mm]
\displaystyle\sum_{r=1}^{m/2}\frac{2\sin((2r-1)\pi x)}{(2r-1)\pi},&m\text{ even}.
\end{cases}
\]
Thus the continuous constant itself has the finite expression
\[
\Lambda_m=\sum_{k=0}^{m-1}(-1)^k\left(Q_m((k+1)/m)-Q_m(k/m)\right).
\]

## Proof
Fourier inversion gives
\[
(P_{m,N}f)(x)=\frac1N\sum_{y\in\mathbb Z_N}D_m(y/N)f(x-y).
\]
Young's inequality gives the upper bound by the normalized \(\ell^1\) norm of the kernel. Equality in \(\ell^\infty\) is obtained by choosing the values of \(f\) to align the phases of the kernel at one output point. Equality in \(\ell^1\) is obtained from a point mass, or equivalently by the standard convolution-operator norm calculation. Hence the displayed absolute kernel average is the exact endpoint norm.

For \(1\le j\le N-1\), the geometric-sum identity gives
\[
\left|D_m(j/N)\right|=
\left|\frac{\sin(\pi m j/N)}{\sin(\pi j/N)}\right|.
\]
Write
\[
R_{m,N}(j)=\frac{\sin(\pi m j/N)}{\sin(\pi j/N)}
\]
with its continuous limiting values at the endpoints. On the integer block
\[
b_k<j\le b_{k+1},\qquad 0\le k\le m-1,
\]
the numerator has sign \((-1)^k\); if the right endpoint is an exact zero, the sign assignment is immaterial. Replacing the \(j=0\) term by the limiting \(j=N\) term preserves its absolute value \(m\). Therefore, with
\[
A_{m,N}(M)=\sum_{j=1}^{M}R_{m,N}(j),
\]
we have
\[
N\|P_{m,N}\|=
\sum_{k=0}^{m-1}(-1)^k\bigl(A_{m,N}(b_{k+1})-A_{m,N}(b_k)\bigr),
\]
which telescopes to the exact formula in the Finding.

It remains to evaluate \(A_{m,N}\). The standard Chebyshev identities are
\[
\frac{\sin((2s+1)\theta)}{\sin\theta}=1+2\sum_{r=1}^{s}\cos(2r\theta)
\]
and
\[
\frac{\sin(2s\theta)}{\sin\theta}=2\sum_{r=1}^{s}\cos((2r-1)\theta).
\]
Summing the resulting cosine progressions for \(j=1,\ldots,M\) gives exactly the two displayed formulas for \(A_{m,N}(M)\).

For the second-order law, set
\[
F_m(x)=\left|\frac{\sin(m\pi x)}{\sin(\pi x)}\right|
\]
with its continuous periodic extension. It is continuous and piecewise analytic. At \(a_k=k/m\), \(1\le k\le m-1\), its first derivative has jump
\[
J_k=F'_{m,+}(a_k)-F'_{m,-}(a_k)=2m\pi\csc\!\left(\frac{\pi k}{m}\right).
\]
In the distributional second derivative,
\[
F_m''=g_m+\sum_{k=1}^{m-1}J_k\delta_{a_k},
\]
where \(g_m\) is piecewise continuously differentiable and of bounded variation. Hence, for nonzero Fourier index \(n\),
\[
\widehat F_m(n)=-\frac1{4\pi^2n^2}\sum_{k=1}^{m-1}J_ke^{-2\pi i n k/m}+O_m(|n|^{-3}).
\]
The Fourier series is absolutely convergent, so the exact trapezoidal identity gives
\[
\frac1N\sum_{j=0}^{N-1}F_m(j/N)=\sum_{\ell\in\mathbb Z}\widehat F_m(\ell N).
\]
Using
\[
\sum_{\ell\ne0}\frac{e^{2\pi i\ell t}}{\ell^2}=2\pi^2B_2(\{t\})
\]
and summing the \(O_m(|\ell N|^{-3})\) remainder proves the residue-class expansion.

## Verification
The accompanying `verify.py` evaluates the exact closed form against the direct sampled absolute Dirichlet-kernel sum in \(4205\) pairs \((m,N)\), with \(2\le N\le160\) and \(2\le m\le\min(N,30)\). The largest floating-point discrepancy is below \(1.2\times10^{-14}\).

The verifier also checks every residue class for \(2\le m\le10\) at large \(N\) against the second-order coefficient and checks that the \(m=4\) coefficients reduce to the four independently known residue-class constants. These numerical checks corroborate the algebra; the proof above establishes the theorem for all admissible \((m,N)\) and the asymptotic law for every fixed \(m\).

## Relationship to prior work
Bonami and Révész develop the idempotent-trigonometric-polynomial framework, explicitly use Dirichlet kernels, and study finite grids and finite cyclic groups in the concentration problem. Their papers provide the natural setting for the question, but the inspected full text does not state an exact endpoint norm for every consecutive block length \(m\), nor the Bernoulli-polynomial residue law above.

A published exact result for three consecutive frequencies gives a residue-class formula when \(m=3\). That result is a strict special case of the present theorem: it has fixed block length three and does not imply the arbitrary-\(m\) partial-sum formula or the general second-order coefficient. Targeted searches under the aliases “finite cyclic Lebesgue constant,” “sampled Dirichlet-kernel \(L^1\) norm,” “consecutive Fourier projection,” and “Bernoulli residue law” did not locate a statement implying the all-length theorem.

## Limitations
The theorem concerns consecutive frequency blocks and endpoint \(\ell^1\) and \(\ell^\infty\) operator norms. It does not determine interior \(\ell^p\) projection norms or arbitrary nonconsecutive spectra. The second-order remainder is controlled for each fixed \(m\), not uniformly in growing \(m\).

There remains a residual originality risk that the exact sign-block summation, or an equivalent fixed-\(m\) sampling expansion, appears in older approximation-theory or numerical-Fourier literature under different terminology. The searches and full-text comparisons performed here did not identify such coverage.

## References
1. A. Bonami and S. Gy. Révész, “Integral Concentration of idempotent trigonometric polynomials with gaps,” arXiv:0707.3023v1, first public 2007-07-20. Primary MSC 42A05.
2. A. Bonami and S. Gy. Révész, “Concentration of the integral norm of idempotents,” arXiv:0811.4576v1, first public 2008-11-27. MSC 42A05, 42A16.
3. “Exact three-frequency Fourier projection norm on every cyclic group,” published-finding corpus record b176a6018242.
