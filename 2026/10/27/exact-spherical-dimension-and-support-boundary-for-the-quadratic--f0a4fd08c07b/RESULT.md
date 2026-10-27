# Exact spherical dimension and support boundary for the quadratic geodesic Askey kernel

## Finding
For every real \(c>0\) and integer \(d\ge1\), put \(\psi_c(\theta)=(1-\theta/c)_+^2\) on \([0,\pi]\). Then \(\psi_c\) is zonally positive definite on \(S^d\) **if and only if** \(d\le3\) or \(c\ge\pi\). In fact, positive-definite cases are strictly positive definite. For every \(0<c<\pi\), infinitely many spherical degree coefficients in dimension four are strictly negative. More precisely, setting \(N=n+3/2\),
\[
I_n(c):=\int_0^c(1-\theta/c)^2 C_n^{3/2}(\cos\theta)\sin^3\theta\,d\theta
=\frac{2\sqrt{2/\pi}\,(\sin c)^{3/2}}{c^2N^{5/2}}\cos(Nc-\pi/4)+O_c(N^{-3}).
\]
The integral is an unnormalized Schoenberg coefficient; all normalizing constants are strictly positive.

## Assumptions and scope
\(S^d\) is the unit sphere in \(\mathbb R^{d+1}\), with geodesic distance \(\theta=\arccos(x\cdot y)\). Positive definiteness means that \([\psi_c(\arccos(x_i\cdot x_j))]_{i,j}\) is positive semidefinite for all finite point sets; strict definiteness requires positivity for distinct points and nonzero weights. Here \(C_n^{3/2}\) are Gegenbauer polynomials with their usual positive normalization at \(1\). The constants in \(O_c\) may depend on fixed \(c\in(0,\pi)\).

## Proof
**1. The known low-dimensional half.** The spherical Pólya theorem for geodesic truncated powers establishes that \((1-\theta/c)_+^2\) is strictly positive definite on \(S^3\) for every \(c>0\) [1, Theorem 5 and accompanying truncated-power corollary]. Restriction to an equatorial subsphere proves the assertion for \(1\le d\le3\).

**2. The all-dimensional large-support half.** On \([0,\pi]\), write \(u(\theta)=1-\theta/\pi=\tfrac12+\pi^{-1}\arcsin(\cos\theta)\). The Taylor series of \(\arcsin z\) has strictly positive coefficients at every odd power. Hence \(u(\arccos(x\cdot y))\) is positive definite in every sphere dimension, because each Gram matrix of \((x\cdot y)^k\) is positive semidefinite. For \(c\ge\pi\), \(1-\theta/c=(1-\pi/c)+(\pi/c)u(\theta)\); its square is positive definite by the Schur product theorem. The series for its square has strictly positive coefficients for every nonnegative degree (odd degrees arise from the positive constant times odd powers; even degrees from products of odd powers). On any fixed sphere these tensor-power kernels separate distinct points, giving strict positive definiteness.

**3. The sharp obstruction in dimension four.** It suffices to prove the displayed asymptotic and that its cosine is negative with fixed margin infinitely often. The Gegenbauer--Legendre identity \(C_n^{3/2}(x)=P'_{n+1}(x)\), followed by the standard Legendre derivative recurrence, yields
\[
I_n(c)=\frac{(n+1)(n+2)}{2n+3}\bigl(J_n(c)-J_{n+2}(c)\bigr),\quad J_m(c)=\int_0^c(1-\theta/c)^2\sin\theta\,P_m(\cos\theta)\,d\theta.
\]
The Mehler--Dirichlet integral for Legendre polynomials, followed by Tonelli/Fubini (all endpoint singularities are integrable), gives
\[
J_m(c)=\frac{\sqrt2}{\pi}\int_0^cH_c(t)\cos((m+\tfrac12)t)\,dt,
\quad H_c(t)=\int_t^c\frac{(1-\theta/c)^2\sin\theta}{\sqrt{\cos t-\cos\theta}}\,d\theta.
\]
The following endpoint expansions are obtained directly by substituting \(\theta=t+s\) and Taylor-expanding the analytic factors, uniformly for fixed \(0<c<\pi\):
\[
H_c(c-s)=\frac{16\sqrt{\sin c}}{15c^2}s^{5/2}+O_c(s^{7/2}),\qquad s\downarrow0,
\]
and
\[
H_c(t)=A_c+B_ct^2\log t+D_ct^2+O_c(t^4|\log t|),\qquad t\downarrow0.
\]
For the second expansion, substitute \(v=\sqrt{\cos t-\cos\theta}\) in the defining Abel integral: terms even in \(\theta\) give analytic powers of \(t^2\), while odd powers give successive \(t^{2j}\log t\); the first possible nonanalytic term is \(t^2\log t\). Differentiating the expansions with a smooth partition of unity gives the same expansions with the requisite symbol derivative bounds for Fourier integration by parts. In particular, the origin contributes \(K_c k^{-3}+O_c(k^{-4}\log k)\) to the cosine transform at frequency \(k\); taking the difference at frequencies \(k\) and \(k+2\) makes this \(O_c(k^{-4}\log k)\). The interior portion has arbitrarily fast decay by repeated integration by parts. At \(t=c\), the Fourier endpoint formula \(\int_0^\infty s^{5/2}\exp(-iks)\,ds=\Gamma(7/2)e^{-7\pi i/4}k^{-7/2}\), interpreted using exponential damping, gives
\[
J_m(c)=\frac{2\sqrt{2/\pi}\sqrt{\sin c}}{c^2(m+1/2)^{7/2}}\cos((m+1/2)c-7\pi/4)+K_c(m+1/2)^{-3}+O_c(m^{-4}\log m).
\]
Consequently, with \(N=n+3/2\), the elementary identity \(\cos a-\cos(a+2c)=2\sin c\sin(a+c)\), and \(\sin(Nc-7\pi/4)=\cos(Nc-\pi/4)\), we obtain the claimed \(I_n(c)\) asymptotic with remainder \(O_c(n^{-3}\log n)\). The logarithm can be removed using the full even-power--logarithm endpoint expansion: its next term after \(t^2\log t\) is \(t^4\log t\), whose cosine transform is \(O(n^{-5})\). Hence the difference of the origin terms is \(O(n^{-4})\) before multiplying by \(n\), and the final remainder is \(O_c(n^{-3})\).

For every fixed \(0<c<\pi\), the sequence \(\cos((n+3/2)c-\pi/4)\) has zero Cesàro mean and Cesàro square mean \(1/2\): these follow by summing the geometric progressions of \(e^{inc}\) and \(e^{2inc}\), except that \(c\notin\{0,\pi\}\) is essential. Thus it is less than a fixed negative constant for infinitely many positive integers \(n\). On this subsequence the main term dominates \(O_c(n^{-3})\), so infinitely many \(I_n(c)<0\). By Schoenberg's coefficient criterion [1,2], \(\psi_c\) is not positive definite on \(S^4\); embedding an equatorial \(S^4\) into \(S^d\) excludes every \(d\ge4\). This finishes all parameter cases.

## Verification
The Legendre recurrence, the Mehler--Dirichlet formula, and the two Abel-endpoint expansions are analytic identities, not numerical observations. The leading coefficient is checked by \(\mathrm B(1/2,3)=16/15\) and \(\Gamma(7/2)=15\sqrt\pi/8\). No numerical truncation of Gegenbauer coefficients is used to infer an infinite-sign claim. The positive side is obtained directly from positive power-series coefficients and a published spherical Pólya theorem.

## Relationship to prior work
Beatson--zu Castell--Xu [2, Conjecture 1.4] proposed positivity at the Gegenbauer threshold \(\delta\ge\lambda+1\); here \(\lambda=3/2\) and \(\delta=2<5/2\). That conjecture is not a proof of the present all-support failure statement. Gneiting [1] establishes the positive-dimensional side through \(d=3\), but does not supply the stated infinite-sign asymptotic for the next dimension. Later positivity results at or above \(\delta=\lambda+1\) concern a different exponent. The result is limited to the natural quadratic truncated-power family, not arbitrary compactly supported kernels.

## Limitations
The displayed Fourier asymptotic is pointwise for fixed \(c\in(0,\pi)\), not uniform as \(c\) approaches \(0\) or \(\pi\). No bound is claimed for the first negative degree. The result is an analytic self-reviewed mathematical claim; no independent review is asserted. Related unpublished or incompletely indexed classifications might affect priority.

## References
[1] T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (first posted 2011-11-30), especially Theorem 5 and truncated-power results. https://arxiv.org/abs/1111.7077
[2] R. K. Beatson, W. zu Castell and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437v1 (first posted 2011-10-11), especially Conjecture 1.4 and Gegenbauer integral criteria. https://arxiv.org/abs/1110.2437
[3] G. Szegő, *Orthogonal Polynomials*, standard Legendre recurrence, Mehler--Dirichlet representation, and Jacobi asymptotics.
