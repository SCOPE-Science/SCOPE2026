# Sharp weak-resetting threshold with an independently switching Brownian gate

## Finding

A one-dimensional diffusing searcher is reflected at the right end of an interval. The left end is an independently switching reactive gate, open (absorbing) or closed (reflecting). Poisson resetting relocates only the searcher; the gate continues its own Markov trajectory. This distinction matters because resetting does **not** regenerate the whole initial state.

Let the interval be \([0,L]\), let the diffusion generator be \(D\partial_{xx}\) with \(D>0\), and set \(x=aL\), \(0<a<1\). The gate opens from closed state \(0\) to open state \(1\) at rate \(\alpha>0\), and closes at rate \(\beta>0\). Start it in the stationary law \(\pi_0=\beta/(\alpha+\beta)\), \(\pi_1=\alpha/(\alpha+\beta)\). The particle starts at \(x\), and independently jumps back to \(x\) at rate \(r\), without resetting the gate. Write \(T_r\) for first absorption time and \(M(r)=\mathbb E[T_r]\).

Define the dimensionless quantities
\[
 k=L\sqrt{\frac{\alpha+\beta}{D}},\qquad c=\frac\beta\alpha,\qquad
 f(a)=\frac{a(a-2)(5a^2-10a+4)}{24},
\]
\[
 F_k(a)=k^2\cosh k\left(a-\frac{a^2}{2}-\frac13\right)
 +\cosh(k(1-a))-\frac12\cosh k-\frac{k}{2\sinh k}.
\]
Then the exact weak-resetting response is
\[
 \boxed{M'(0+)=\frac{L^4}{D^2}\left(f(a)+\frac{cF_k(a)}{k^3\sinh k}\right).}
\]
For every strictly positive choice of parameters there is a **unique** threshold \(a_*=a_*(k,c)\) with
\[
 \boxed{1-\frac1{\sqrt3}<a_*<1-\frac1{\sqrt5}}.
\]
The derivative is negative on \(0<a<a_*\), positive on \(a_*<a<1\), and zero precisely at the threshold. Thus arbitrarily weak resetting is strictly beneficial below the threshold and strictly detrimental above it. These are local-at-zero statements, not assertions about all positive reset rates. In particular, \(a<1-1/\sqrt3\) is a universal sufficient condition for improvement; \(a>1-1/\sqrt5\) precludes improvement for sufficiently weak resetting for every positive gate-rate pair. The bounds are sharp over gate parameters. For each fixed \(k\), \(a_*(k,c)\) is strictly decreasing in \(c\).

## Assumptions and scope

The particle has Brownian generator \(D\partial_{xx}\), instantaneous position-only Poisson resets, no drift, reflection at \(L\), and at \(0\) Neumann reflection while closed and Dirichlet absorption while open. Gate switching is independent of particle motion and resets. At an absorption event the process terminates. We assume \(L,D,\alpha,\beta>0\), \(0<a<1\), stationary initial gate law, and investigate the right derivative with respect to the reset rate at \(r=0\). Smooth parameter dependence follows from invertibility of the killed Markov generator on the bounded interval; the coupled backward elliptic problem has a unique bounded solution with finite moments.

## Proof

**1. Scaling and backward equations.** Rescale space by \(L\) and time by \(L^2/D\); in the proof put \(L=D=1\). The physical reset rate becomes \(\rho=rL^2/D\), while \(k^2=(\alpha+\beta)L^2/D\); hence the dimensional derivative acquires \(L^4/D^2\). Denote the state-conditioned means by \(m_j(y;\rho)\), \(j=0\) (closed), \(j=1\) (open), with position reset to \(a\). They solve
\[
 m_0''+\alpha(m_1-m_0)+\rho[m_0(a)-m_0(y)]=-1,
\]
\[
 m_1''+\beta(m_0-m_1)+\rho[m_1(a)-m_1(y)]=-1,
\]
with \(m_1(0)=0\), \(m_0'(0)=0\), and \(m_0'(1)=m_1'(1)=0\). The gate is **not** reset in the nonlocal term. These boundary-value equations also establish analyticity near \(\rho=0\) by standard bounded-operator perturbation of the killed resolvent.

**2. Zero-rate mean.** Put \(\pi_0=\beta/(\alpha+\beta)\), \(\pi_1=\alpha/(\alpha+\beta)\), \(\bar m=\pi_0m_0+\pi_1m_1\), and \(\delta=m_0-m_1\). At \(\rho=0\), letting \(B(y)=y-y^2/2\) and \(A=(\pi_1k\sinh k)^{-1}\), the equations and four boundary conditions give
\[
 \bar m(y;0)=B(y)+\frac{\beta}{\alpha}\frac{\coth k}{k},\qquad
 \delta(y;0)=A\cosh(k(1-y)).
\]
In particular the mean without resetting is \(M(0)=\frac{L^2}{D}[B(a)+c\coth(k)/k]\).

**3. Exact response.** Differentiate the backward equations at \(\rho=0\) and write \(n_j=\partial_\rho m_j|_0\), \(\bar n=\pi_0n_0+\pi_1n_1\), and \(\eta=n_0-n_1\). They obey
\[
 \bar n''(y)=B(y)-B(a),\qquad
 \eta''(y)-k^2\eta(y)=A[\cosh(k(1-y))-\cosh(k(1-a))],
\]
with \(\bar n'(1)=\eta'(1)=0\), \(\bar n(0)=\pi_0\eta(0)\), and \(\bar n'(0)+\pi_1\eta'(0)=0\). Thus \(\bar n'(0)=B(a)-1/3\). A Neumann-at-one particular solution of the second equation is
\[
 \eta(y)=C\cosh(k(1-y)) +\frac{A(1-y)\sinh(k(1-y))}{2k}
 +\frac{A\cosh(k(1-a))}{k^2},
\]
where \(C\) is fixed by the condition at zero. Integrating the first equation twice and imposing the conditions at zero produces
\[
 \bar n(a)=\frac{a(a-2)(5a^2-10a+4)}{24}
 +\frac{\beta}{\alpha}\frac{F_k(a)}{k^3\sinh k}.
\]
Since the initial gate is stationary, \(\bar n(a)\) is the desired nondimensional derivative. This proves the displayed exact formula, including the normalization.

**4. Universal endpoint signs.** Put \(b=1-a\). The following absolutely convergent power series identity is useful:
\[
 2\sinh k\,F_k(a)=\frac{k^2(1-3b^2)}6\sinh(2k)
 +2\sinh k\cosh(kb)-\frac12\sinh(2k)-k.
\]
For every integer \(j\ge1\), the coefficient of \(k^{2j+1}/(2j+1)!\) on the right is
\[
 P_j(b)=(1+b)^{2j+1}+(1-b)^{2j+1}-2^{2j}
 +\frac{1-3b^2}{6}2^{2j-1}(2j)(2j+1).
\]
Here \(P_1(b)=0\) for all \(b\). At \(b=1\) the coefficients for \(j\ge2\) equal \(2^{2j-1}[2-(2j)(2j+1)/3]<0\); hence \(F_k(0)<0\) for every \(k>0\). At \(b=1/\sqrt3\), the last term in \(P_j\) vanishes. For \(S_j=(1+b)^{2j+1}+(1-b)^{2j+1}\), one has \(S_2=88/9<16\) and \(S_{j+1}<(4)S_j\), so \(P_j<0\) for all \(j\ge2\), proving \(F_k(1-1/\sqrt3)<0\). At \(b=1/\sqrt5\), \(P_2=16/15>0\); for \(j\ge3\), \(P_j=S_j+2^{2j}[j(2j+1)/15-1]>0\). Thus \(F_k(1-1/\sqrt5)>0\). Since \(f(a)<0\) for \(0<a<1-1/\sqrt5\), and \(f(1-1/\sqrt5)=0\), the total response is negative at the lower bound and positive at the upper bound.

**5. Exactly one crossing.** Write \(H(a)=f(a)+cF_k(a)/(k^3\sinh k)\). Direct differentiation gives
\[
 H^{(3)}(a)=5(a-1)-c\frac{\sinh(k(1-a))}{\sinh k}<0
 \qquad(0<a<1),
\]
\[
 H'(1)=0,\qquad H''(1)=-\frac12+c\frac{1-\cosh k}{k\sinh k}<0.
\]
Therefore \(H'\) is strictly concave, is positive immediately to the left of \(1\), and has at most one sign switch on \((0,1)\), from negative to positive; consequently \(H\) is either increasing or first decreasing and then increasing. As \(H(0)<0\), the strict opposite signs at the bracket endpoints force exactly one root \(a_*\), with the stated signs throughout the interval. At the root \(f(a_*)<0\), so \(F_k(a_*)>0\). Implicit differentiation then yields
\[
 \frac{\partial a_*}{\partial c}=-\frac{F_k(a_*)/(k^3\sinh k)}{H'(a_*)}<0.
\]
(The root lies on the strictly increasing part of \(H\), so \(H'(a_*)>0\).)

**6. Sharpness.** Holding \(k>0\) fixed and letting \(c\downarrow0\) sends the unique root to the non-gated zero \(1-1/\sqrt5\). On the other hand, taking \(k\to\infty\) and \(c/k\to\infty\) makes \(H(a)/[c/k]\to a-a^2/2-1/3\) for each fixed \(a>0\), uniformly on closed subintervals of \((0,1)\). The root therefore approaches \(1-1/\sqrt3\). Both limits can be realized with strictly positive gate rates, and both endpoint bounds are sharp but not attained for positive finite parameters.

## Verification

The self-contained file `verify.py` independently differentiates the finite-state reflecting lattice generator at zero reset rate, solves two sparse resolvent systems, extrapolates the lattice spacing to zero, and compares with the closed formula. It also checks root localization, strict monotonicity with respect to the closing/opening rate ratio, and the endpoint-series coefficient signs. On the provided program run all 193 tests passed. The analytic power-series and concavity arguments, not lattice sampling, establish the theorem for all positive parameters. Run from the extracted artifact directory using `python verify.py` (requires NumPy and SciPy).

## Relationship to prior work

Bressloff (2020, arXiv:2009.02739) studies stochastic resetting with a gated target on a reflecting interval, but its renewal formulation explicitly **resets the gate state** along with the particle (Section 3). Its possible enhancement of resetting at initially unfavorable distal positions consequently does not imply this particle-only result. Mercado-Vásquez and Boyer (2021, arXiv:2107.02148) explicitly keep the gate independent of particle resets, but study the **half-line** and derive mean and fluctuation formulas, not a bounded-interval location threshold. Bressloff (2026, arXiv:2601.01588) considers independent gate dynamics with Poisson resetting on the **half-line** (Section 3.1) and a finite interval with gated ends **without bulk Poisson resets** (Section 3.2), and thus does not state the combined sharp interval threshold here. Benkhadaj and Grebenkov (2022, arXiv:2209.00947) study position/local-time resetting and reactivity models in bounded domains, but not this independently Markov-gated boundary's reset-location crossover. These are comparisons of assumptions and implied statements, not proofs of absolute priority.

## Limitations

The result identifies the sign of the derivative at zero and hence the benefit or harm of **sufficiently small positive** resetting, not the global minimizing reset rate. It does not cover nonstationary initial gate laws, simultaneous gate resetting, time-dependent reset rates, biased diffusion, multiple gates, or general domains. The strongest remaining priority risk is an implicit reduction of this exact threshold from general Markov-modulated first-passage resolvent formulas; no claim of independent verification is made.

## References

1. P. C. Bressloff, "Diffusive search for a stochastically-gated target with resetting," arXiv:2009.02739v1 (first public 2020-09-06), https://arxiv.org/abs/2009.02739 .
2. G. Mercado-Vásquez and D. Boyer, "Search of stochastically gated targets with diffusive particles under resetting," arXiv:2107.02148v1 (first public 2021-07-05), https://arxiv.org/html/2107.02148v2 .
3. Z. Benkhadaj and D. S. Grebenkov, "Encounter-based approach to diffusion with resetting," arXiv:2209.00947v1 (first public 2022-09-02), https://arxiv.org/abs/2209.00947 .
4. P. C. Bressloff, "Renewal theory for Brownian motion with stochastically gated targets," arXiv:2601.01588v1 (first public 2026-01-04), https://arxiv.org/abs/2601.01588 .
