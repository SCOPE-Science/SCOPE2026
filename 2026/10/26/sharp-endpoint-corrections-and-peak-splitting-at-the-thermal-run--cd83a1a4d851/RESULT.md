# Endpoint corrections to the thermal mode boundary of a trapped run-and-tumble particle

## Finding

Let \(a=\gamma/k\) be the ratio of the sign-flip rate to the harmonic relaxation rate and \(t=Dk/v^2\) the dimensionless thermal variance. For \(0<a<1\), write \(t_c(a)\) for the critical variance at which the central curvature of the stationary density vanishes. The quantitative claims concern the two subleading endpoint terms:
\[
t_c(a)=1-c_0a+O(a^2),\qquad
c_0=e^{1/2}\sqrt{2\pi}\operatorname{erf}(1/\sqrt2),\qquad a\downarrow0.
\]
As \(\delta=1-a\downarrow0\), put \(L=\log(1/\delta)\) and \(\lambda_c=1/[2t_c(1-\delta)]\). Then
\[
\lambda_c=L+\tfrac32\log L+\log(2/\sqrt\pi)+o(1).
\]
For context, there are exactly two modes at \(\pm m_a(t)\) for \(0<t<t_c(a)\), a unique mode at zero for \(t\ge t_c(a)\), and a unique mode at zero for all \(t>0\) when \(a\ge1\). At fixed \(0<a<1\), the Gaussian heat equation and the nondegenerate critical quartic give
\[
m_a(t)^2=3(t_c(a)-t)+O_a((t_c(a)-t)^2),\qquad t\uparrow t_c(a).
\]
The coefficient three is the local heat-flow law at such a symmetric quartic transition, not a special coefficient of the run-and-tumble law.

## Model and known inputs

In physical time \(s\), \(dX_s=(-kX_s+v\sigma_s)ds+\sqrt{2D}\,dW_s\), with \(k,v,\gamma,D>0\), independent Brownian motion \(W\), and a symmetric two-state telegraph process \(\sigma\) flipping at Poisson rate \(\gamma\). In stationarity \(Z=kX/v\) has the same distribution as \(U+\sqrt t G\), with independent standard Gaussian \(G\) and density
\[
f_a(u)=\frac{\Gamma(a+1/2)}{\sqrt\pi\Gamma(a)}(1-u^2)^{a-1}\boldsymbol1_{|u|<1}
\]
for \(U\). Write \(p_{a,t}=f_a*\varphi_t\), where \(\varphi_t\) is the Gaussian of variance \(t\). The beta law, its Gaussian convolution, and the curvature equation defining the boundary are known. In original length units the positive mode is \((v/k)m_a(t)\).

## Proof

### Curvature and its unique crossing

For \(Y=U^2\sim\operatorname{Beta}(1/2,a)\) and \(\lambda=1/(2t)\) put
\[
F_a(\lambda)=\int_0^1 y^{-1/2}(1-y)^{a-1}e^{-\lambda y}dy,\qquad H_a(\lambda)=-2\lambda F'_a(\lambda)-F_a(\lambda).
\]
The sign of \(p''_{a,t}(0)\) is the sign of \(H_a(\lambda)\), by differentiation under the convolution. Integrating the derivative of \(y^{1/2}(1-y)^ae^{-\lambda y}\) gives \(\lambda F_a''+(a+1/2+\lambda)F_a'+F_a/2=0\). Consequently, at any positive zero of \(H_a\), \(H'_a=2(a-1)F_a'>0\) for \(0<a<1\). Also \(H_a(0)<0\). At large \(\lambda\), use the integral for \(H_a\) with factor \(2\lambda y-1\), expand \((1-y)^{a-1}=1+(1-a)y+O_a(y^2)\) on \([0,1/2]\), and bound the remaining integrable tail by \(O_a(\lambda e^{-\lambda/2})\). Extending the polynomial terms to the half-line gives a zero constant-term integral and a linear-term integral \(\sqrt\pi(1-a)\lambda^{-3/2}\). The net error is \(O_a(\lambda^{-5/2})\). Thus there is at least one zero and, since every zero crosses upward, exactly one. Central curvature crosses downward as \(t\) increases through \(t_c\). The heat identity \(\partial_t p_{a,t}=\tfrac12\partial_x^2p_{a,t}\) gives \(p^{(4)}_{a,t_c}(0)<0\).

### Real critical points and mode opening

For \(0<a<1\), the derivative \(p'_{a,t}\) has at most three real zeros counted with multiplicity. To see this directly even at the integrably singular endpoints of \(f_a\), define the compactly supported distribution \(T=f'_a\). After multiplying \(p'_{a,t}(x)\) by a positive constant and by \(e^{x^2/(2t)}\), it equals \(\langle T,e^{-u^2/(2t)}e^{xu/t}\rangle\). Four real zeros counted with multiplicity would therefore give four tests annihilated by \(T\): the Gaussian factor in \(u\) times functions \(u^j e^{xu/t}\), using consecutive powers \(j=0,1,\dots\) up to each selected multiplicity minus one.

Every nonzero linear combination of these four exponential monomials has at most three real zeros counted with multiplicity. In general, for \(r\) such monomials with initial consecutive powers at each real exponent, the bound is \(r-1\): factor out the lowest exponential and differentiate, reducing that group's polynomial degree by one and leaving the permitted degrees of the other groups unchanged; use induction and Rolle's theorem counting multiplicities. A nonzero constant after factoring needs no derivative argument. The functions are linearly independent, for example by dominance of the largest real exponent and then its highest nonzero power at \(+\infty\).

There is thus a nonzero combination vanishing at \(-1,0,1\) (three homogeneous linear conditions), with these three zeros all simple. Multiply it by the Gaussian factor to obtain a test \(\psi\) whose sign agrees, after one overall sign choice, with the sign of the classical derivative of \(f_a\) on both \((-1,0)\) and \((0,1)\). Integrating by parts on intervals truncated at \(\pm(1-\varepsilon)\) and then taking \(\varepsilon\downarrow0\) gives
\[
\langle T,\psi\rangle=\int_{-1}^1 f_a'(u)\psi(u)du>0.
\]
The boundary terms are \(O(\varepsilon^a)\) and the integral is absolutely convergent because \(\psi\) vanishes at both endpoints. This contradicts annihilation. It proves the zero bound without a limit argument about real zeros.

The derivative is odd and strictly negative for \(x>1\). Positive central curvature forces an additional zero on each half-line, and the zero bound makes these simple and the only modes. For negative central curvature an additional positive zero would either have even multiplicity or force another zero on the same half-line, since the derivative is negative both near zero and beyond one. Both possibilities violate the bound by symmetry. At the critical value the zero at the origin is already triple and the quartic coefficient is negative. If \(a\ge1\), the beta density is symmetric and nonincreasing for positive \(u\). Express it by layers of centered intervals. Convolving each interval \([-s,s]\) of positive length with the Gaussian gives derivative \(\varphi_t(x+s)-\varphi_t(x-s)<0\) for \(x>0\). This gives strict unimodality also at \(a=1\).

For the displacement, \(p'_{a,t}(x)/x\) extends near \((t_c,0)\) as an analytic function of \((t,w)\) with \(w=x^2\). At \((t_c,0)\), its \(w\)-derivative is \(p^{(4)}_{a,t_c}(0)/6\), and its \(t\)-derivative is \(p^{(4)}_{a,t_c}(0)/2\). The implicit analytic solution has \(w'(t_c)=-3\), and is positive just below \(t_c\), where it must equal \(m_a(t)^2\). This proves the stated fixed-\(a\) remainder.

### Perfect persistence

For smooth \(g\) the beta integral, after subtracting \(g(1)\), gives
\[
\mathbb E_a[g(Y)]=g(1)+a\int_0^1\frac{y^{-1/2}(g(y)-g(1))}{1-y}\,dy+O(a^2).
\]
Indeed \(1/B(1/2,a)=a+O(a^2)\) and the subtracted integral is analytic near \(a=0\), since \(g(y)-g(1)=O(1-y)\). For \(g_t(y)=(y-t)e^{-y/(2t)}\) the analytic extension is joint near \((0,1)\). Write \(Q(a,t)=\mathbb E_a[g_t(Y)]\); it has the same zeros as central curvature. At \((0,1)\), \(Q=0\), \(\partial_tQ=-e^{-1/2}\), and \(\partial_a Q=-\int_0^1 y^{-1/2}e^{-y/2}dy=-\sqrt{2\pi}\operatorname{erf}(1/\sqrt2)\). The implicit function theorem gives the correction, and uniqueness identifies its branch with \(t_c\).

### Nearly uniform beta law

For \(a=1\), integrating the derivative of \(\sqrt y e^{-\lambda y}\) gives \(H_1(\lambda)=-2e^{-\lambda}\). For \(0<\delta\le1/2\) set \(D_\delta(y)=(1-y)^{-\delta}-1\). Uniformly on \([0,1/2]\), \(D_\delta(y)=\delta y+O(\delta y^2)\) by Taylor's theorem; on \([1/2,1]\) use \(0\le D_\delta(y)\le\delta(1-y)^{-1/2}[-\log(1-y)]\). Subtraction of the uniform-law integral and extension of the linear term to \([0,\infty)\) yield
\[
H_{1-\delta}(\lambda)=-2e^{-\lambda}+\delta\sqrt\pi\lambda^{-3/2}+O(\delta\lambda^{-5/2})\qquad(\lambda\ge1).
\]
Here the upper-half tail is \(O(\delta\lambda e^{-\lambda/2})\); the leading integral is \(\delta[2\Gamma(5/2)-\Gamma(3/2)]\lambda^{-3/2}\), and the Taylor remainder is bounded by its absolute integral. At \(L\) the negative term dominates, and at \(L+3\log L\) the positive term dominates for large \(L\). Thus the unique zero has \(\lambda_c=L+O(\log L)\), and its equation gives
\[
\lambda_c=L+\tfrac32\log\lambda_c+\log(2/\sqrt\pi)+O(1/\lambda_c).
\]
Since \(\log\lambda_c-\log L=o(1)\), this is the claimed correction.

## Reproducibility and scope

The accompanying `checks/verify.py` is a finite numerical check using NumPy and SciPy. It compares two evaluations of the curvature equation and probes the mode opening and endpoint scalings at finite parameters. It does not certify the zero count, asymptotic remainders, or priority. The proof above is analytic. The small-mode error is for fixed switching ratio; no joint uniformity with a persistence endpoint is asserted.

## Relationship to prior work

Sabhapandit and Majumdar (2024), §4.1, Eqs. (92)–(96), already give the beta/Gaussian convolution and the hypergeometric curvature condition for the equivalent trap-center model, with their \(\nu=a\) and \(\upsilon^2=1/t\). Guéneau, Majumdar and Schehr (2026), §V.A.1, Eqs. (89)–(97), give the same boundary and leading endpoint behavior (their \(\alpha=2a\), \(\theta=2t\)). Sevilla and Meléndez Mora (2026), §III, give the stationary convolution as well. The subleading endpoint terms are the distinct quantitative claims assessed here; the mode count and the generic heat-flow opening law are included to place them in context. These comparisons do not establish exhaustive priority.

- S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480v1 (2024).
- M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (2026).
- F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1 (2026).
