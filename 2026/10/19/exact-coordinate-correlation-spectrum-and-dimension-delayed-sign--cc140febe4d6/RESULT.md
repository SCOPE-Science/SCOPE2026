# Sharp dimensional slowdown of first-coordinate covariance in the twisted baker map

## Finding

For each integer \(M\ge2\), let \(F\) be the twisted baker map on \(X=[-1,1]\times[0,1]^{M-1}\), and let \(m\) be normalized Lebesgue measure. For the first-coordinate stationary autocovariance
\[
C_M(n)=\int_X x_1(F^n x)_1\,dm(x),\qquad \rho_M=\limsup_{n\to\infty}|C_M(n)|^{1/n},
\]
the exact exponential rate has the sharp large-dimension expansion
\[
\boxed{\displaystyle \rho_M=1-\frac{\log3}{2M}+O(M^{-2}).}
\]
In particular, the physical coordinate has no dimension-uniform exponential rate bounded strictly below one. A pair of nonreal transfer roots approaches one as
\[
\lambda_{M,\pm}=1+\frac{-\log3\pm i\pi}{2M}+O(M^{-2}).
\]
It is not necessary to identify which roots maximize the modulus in each dimension: the pair gives the sharp lower bound, and the characteristic equation gives a matching upper bound for the maximal modulus.

## Assumptions and scope

The map is
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
The observable \(x_1\) has zero mean. The limit superior is in lag with dimension held fixed; the dimension is then taken large in the resulting rate. This is not a claim about all observables, a simultaneous lag-and-dimension asymptotic, or the full transfer spectrum.

## Proof

**Transfer input.** The two full inverse branches \(G_L(y)=((y_1-1)/2,y_2,\ldots,y_M)\) and \(G_R(y)=(y_2,\ldots,y_M,(1-y_1)/2)\) each have Jacobian magnitude \(1/2\). Their average is the stationary transfer operator. On centered coordinates \(u_1=x_1\), \(u_j=x_j-1/2\) for \(j\ge2\), its row-coefficient matrix \(B_M\) has first row corresponding to \(Pu_1=u_1/4+u_2/2\), rows \(Pu_j=(u_j+u_{j+1})/2\) for \(2\le j<M\), and last row corresponding to \(Pu_M=-u_1/4+u_M/2\). This finite action and the first-coordinate resolvent are available in [2]. For completeness, independence and transfer duality give \(C_M(n)=(B_M^n)_{11}/3\). The determinant of \(I-zB_M\) has a diagonal term and a single cyclic term, and the first principal cofactor is \((1-z/2)^{M-1}\), giving
\[
\sum_{n\ge0} C_M(n)z^n
=\frac{(1-z/2)^{M-1}}{3[(1-z/4)(1-z/2)^{M-1}+z^M/2^{M+1}]}.
\]
The numerator cannot cancel any finite poles, as the denominator inside brackets at \(z=2\) is \(1/2\). Each nonzero eigenvalue gives a pole at its reciprocal. The equation for eigenvalues is
\[
(4\lambda-1)(2\lambda-1)^{M-1}=-1.
\]
No such root can have modulus \(\ge1\), because the two factors then have moduli at least \(3\) and \(1\), respectively. There is a nonzero root since the trace is positive. The radius formula for a power series therefore gives \(\rho_M=\max|\lambda|\), with \(0<\rho_M<1\).

**Near-unit roots.** Put \(h=1/M\) and \(2\lambda-1=e^{hw}\). The equation becomes
\[
(2e^{hw}+1)e^{(1-h)w}+1=0.
\]
At \(h=0\), the root \(w=-\log3+i\pi\) is simple, since the derivative in \(w\) is \(-1\). Analytic implicit continuation gives a root \(w(h)=-\log3+i\pi+O(h)\) and its conjugate for real \(h\). Expanding \(\lambda=(1+e^{hw(h)})/2\) gives the pair in the Finding. In particular \(\rho_M\ge 1-(\log3)/(2M)-K/M^2\) for some fixed \(K\) and all sufficiently large \(M\).

**Matching upper bound.** For an eigenvalue \(\lambda\) of maximal modulus, the lower bound just proved gives \(|4\lambda-1|\ge4\rho_M-1\ge3-O(M^{-1})\). The exact characteristic equation then yields
\[
\rho_M=\left|\frac{1+(2\lambda-1)}2\right|
\le\frac{1+|2\lambda-1|}2
=\frac{1+|4\lambda-1|^{-1/(M-1)}}2
\le 1-\frac{\log3}{2M}+O(M^{-2}).
\]
For the last step, use the lower bound \(3-L/M\) on \(|4\lambda-1|\) for a constant \(L\); the logarithm of that lower bound is \(\log3+O(M^{-1})\). Together the two bounds give the sharp rate.

## Verification

The accompanying `verify_twisted_baker_affine.py` checks the finite transfer calculation, including the characteristic determinant and rational resolvent, and compares inverse-branch words with matrix powers in small dimensions. These are checks on the transfer input; the analytic continuation and modulus bounds, not the code, prove the dimensional asymptotic.

## Relationship to prior work

Saiki, Takahasi and Yorke [1] introduced the map, proved invariance and established Bernoulli mixing; their periodic-orbit Jacobians are different spectral objects. The centered-coordinate transfer matrix and the complete first-coordinate resolvent are credited to the equivalent available calculation in [2], which further studies sign oscillations and long-run variance. The exact first sign reversal at lag \(M\) follows by expanding that resolvent and is not claimed as a separate finding here. The present result is the sharp dimension dependence of the geometric covariance rate, not the fixed-dimension transfer polynomial or an oscillation theorem.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, [arXiv:2202.04304](https://arxiv.org/abs/2202.04304), Theorem D and §3.
2. *Oscillatory coordinate memory and dimension-free variance in the twisted baker map*, [Resultary record 765a4f4ba4c8](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-oscillatory-coordinate-memory-and-dimension-free-variance-in-the--765a4f4ba4c8), Finding and proof steps 1–2.
