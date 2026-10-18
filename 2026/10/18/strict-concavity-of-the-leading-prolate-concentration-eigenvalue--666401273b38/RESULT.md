# Strict concavity of the leading prolate concentration eigenvalue

## Finding
For every real \(c>0\), let \(K_c\) act on \(L^2([-1,1])\) by
\[
(K_cf)(x)=\int_{-1}^1\frac{\sin(c(x-y))}{\pi(x-y)}f(y)\,dy,
\]
with the continuous diagonal value \(c/\pi\). Write \(\Lambda(c)\) for its largest eigenvalue. Then \(\Lambda\) is twice continuously differentiable and strictly increasing and strictly concave:
\[
\boxed{\Lambda'(c)>0,\qquad\Lambda''(c)<0\quad(c>0).}
\]
More precisely, let \(\psi_c\) be the unique positive even eigenfunction of \(K_c\) of norm one in \(L^2([-1,1])\), and set \(b(c)=\psi_c(1)^2\). Then
\[
0<b(c)<\tfrac12,\qquad b'(c)<0,
\quad \Lambda'(c)=\frac{2\Lambda(c)b(c)}c,
\quad \Lambda''(c)=\frac{2\Lambda(c)}{c^2}\big(2b(c)^2-b(c)+cb'(c)\big)<0.
\]
In particular, additional bandwidth always produces a strictly smaller marginal increase in the optimally attainable energy concentration, even though \(\Lambda(c)\) itself increases.

## Assumptions and scope
The parameter \(c\) is the positive product of half-lengths of a symmetric time interval and its angular-frequency interval. The Hilbert norm is the unweighted Lebesgue \(L^2([-1,1])\) norm. Only the top eigenvalue of the classical order-zero sinc/prolate operator is considered. The Sturm–Liouville eigenfunction and the Fourier-operator eigenfunction share this normalization; no conclusion about second derivatives of higher eigenvalues is made.

## Proof
Put \(q=c^2\), \(p(x)=1-x^2\), and consider the self-adjoint prolate Sturm–Liouville operator
\[
H_q=-\frac{d}{dx}\left(p(x)\frac{d}{dx}\right)+qx^2
\]
on \((-1,1)\) with regular bounded behavior at the singular endpoints. Its lowest eigenvalue \(\chi(q)\) is simple and has a strictly positive even, real, normalized eigenfunction \(\psi_q\). By classical prolate commutation and eigenvalue ordering, this is the eigenfunction corresponding to the simple largest eigenvalue of \(K_c\) when \(q=c^2\). Smooth parameter dependence follows from standard perturbation theory for a simple eigenvalue.

The finite Fourier transform \((F_cf)(x)=\int_{-1}^1 e^{icxy}f(y)\,dy\) has \(F_c\psi_c=\mu_c\psi_c\) and \(F_c^*F_c=(2\pi/c)K_c\). Thus \(|\mu_c|^2=2\pi\Lambda(c)/c\). Direct kernel differentiation gives \(K_c'(x,y)=\cos(c(x-y))/\pi\), so Hellmann–Feynman and evenness yield
\[
\Lambda'(c)=\frac1\pi\left|\int_{-1}^1e^{icx}\psi_c(x)\,dx\right|^2
=\frac{|\mu_c\psi_c(1)|^2}{\pi}=\frac{2\Lambda(c)b(c)}c.
\]
The first expression is positive because the finite Fourier eigenvalue and \(\psi_c(1)\) are both nonzero.

For strict decrease of \(b\), write a dot for \(\partial_q\). Hellmann–Feynman for \(H_q\) gives
\[
\dot\chi(q)=m_q=\int_{-1}^1x^2\psi_q(x)^2\,dx\in(0,1).
\]
Differentiating \(H_q\psi_q=\chi(q)\psi_q\), subtracting the original equation multiplied by \(\dot\psi_q\), and integrating shows
\[
W_q(x):=p(x)\big(\psi_q(x)\dot\psi_q'(x)-\psi_q'(x)\dot\psi_q(x)\big)
=\int_0^x(t^2-m_q)\psi_q(t)^2\,dt.
\]
Evenness gives \(W_q(0)=0\). At \(x=1\), regularity and \(p(1)=0\) give \(W_q(1)=0\). The integrand is strictly negative before \(\sqrt{m_q}\) and strictly positive after it; hence \(W_q(x)<0\) for every \(0<x<1\). In particular,
\[
\partial_q\left(\frac{\psi_q'(x)}{\psi_q(x)}\right)
=\frac{W_q(x)}{p(x)\psi_q(x)^2}<0.
\]
Integrating this inequality between \(x\) and \(1\) shows that \(\psi_q(x)/\psi_q(1)\) strictly increases with \(q\), for each \(0\le x<1\). Since
\[
\frac1{b(\sqrt q)}=\int_{-1}^1\left(\frac{\psi_q(x)}{\psi_q(1)}\right)^2dx,
\]
it follows that \(b'(c)<0\) for all \(c>0\).

Finally, the Rayleigh quotient of the constant trial function gives \(0<\chi(q)\le q/3<q\). Using \((p\psi_q')'=(qx^2-\chi(q))\psi_q\), the quantity \(p\psi_q'\) first strictly decreases and then strictly increases on \((0,1)\), is zero at both endpoints, and is strictly negative in between. Hence \(\psi_q\) is strictly decreasing in \(x\in(0,1)\). Its normalization implies \(0<\psi_q(1)^2<1/2\), i.e. \(0<b(c)<1/2\). A final differentiation of \(\Lambda'(c)=2\Lambda(c)b(c)/c\) gives
\[
\Lambda''(c)=\frac{2\Lambda(c)}{c^2}(2b(c)^2-b(c)+cb'(c))<0,
\]
since \(2b(c)^2-b(c)<0\) and \(cb'(c)<0\), proving the claim.

## Verification
The operator factor \(F_c^*F_c=(2\pi/c)K_c\), the diagonal derivative \(\partial_cK_c(x,x)=1/\pi\), and the finite-Fourier normalization independently give the same eigenvalue derivative. The Wronskian identity, its boundary cancellation, and the single sign change of \(x^2-m_q\) establish the strict parameter comparison without numerical extrapolation. Independent Nyström sampling at representative \(c\)-values \(0.05,0.2,0.5,1,2,3,5,8\) returned strictly negative second differences; this is a consistency check only, not a proof. The proof uses the established top-eigenfunction/ground-state correspondence of prolate spectral theory.

## Relationship to prior work
Abreu and Speckbacher (2026) establish optimality of intervals among all observation sets of prescribed measure for Paley–Wiener concentration. Their geometric optimality statement does not determine curvature of the leading concentration eigenvalue as time-bandwidth varies. Classical Slepian–Pollak theory supplies the commuting prolate differential operator and the finite Fourier eigenstructure used here. Osipov and Rokhlin (2013) study the computational prolate spectral machinery. The additional strict Wronskian comparison of normalized endpoint amplitudes yields the global curvature sign. A targeted literature/database comparison did not reveal an equivalent statement, but historical-priority uncertainty remains, especially for older prolate inequalities.

## Limitations
The statement is restricted to the classical one-dimensional symmetric single-interval, order-zero prolate operator and its leading eigenvalue. It does not imply concavity for arbitrary sets, other eigenvalue indices, or higher dimensions. Standard prolate spectral theory is invoked for the commuting operator and the identity of the top integral eigenfunction with the differential ground state. No independent audit has been performed.

## References
1. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192, first public 2026-07-21.
2. D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—I*, Bell System Technical Journal **40** (1961), 43–63.
3. A. Osipov and V. Rokhlin, *On the evaluation of prolate spheroidal wave functions and associated quadrature rules*, arXiv:1301.1707 (2013).
