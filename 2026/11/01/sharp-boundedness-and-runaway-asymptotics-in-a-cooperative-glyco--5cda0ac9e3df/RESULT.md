# Sharp boundedness and runaway asymptotics in a cooperative glycolysis oscillator

## Finding
For the product-recycling glycolysis system below, the sign of the **net product-removal rate** \(\lambda=\kappa_s+d\) exactly separates bounded dynamics from universal product runaway, provided conversion capacity exceeds maximum substrate supply plus recycling capacity. Every strictly positive solution is bounded when \(\lambda>0\); every strictly positive solution is unbounded when \(\lambda\le0\), with the following *sharp physical-time asymptotics*.

Define
\[
\xi=\frac{\nu+\sigma_i}{\sigma-\nu-\sigma_i},\qquad M_0=x_0+\frac{y_0}{q}.
\]
At zero net removal, all strictly positive initial conditions satisfy
\[
\boxed{x(t)\to\xi,\qquad y(t)=q\nu t+q(M_0-\xi)+o(1).}
\]
At negative net removal, let \(\mu=-\lambda>0\). There exists a **strictly positive, initial-condition-dependent** constant \(C\) such that
\[
\boxed{x(t)\to\xi,\qquad y(t)=C e^{\mu t}-\frac{q\nu}{\mu}+o(1).}
\]
The substrate limit and both leading production rates are independent of the Hill exponent and allosteric equilibrium ratio. No positive equilibrium, periodic orbit, or other compact forward-invariant set exists at \(\lambda\le0\). The sign threshold is exact: the original glycolysis system has bounded positive solutions for every \(\lambda>0\), whereas all positive solutions escape to infinity for \(\lambda\le0\).

## Assumptions and scope
Let \(\nu,\sigma,\sigma_i,q,L,\kappa,\kappa_s\) be strictly positive; let \(n\ge1\) be real; let \(d\in\mathbb R\); and assume
\[
\sigma>\nu+\sigma_i.
\]
For arbitrary \(x(0)=x_0>0\) and \(y(0)=y_0>0\), consider
\[
\begin{aligned}
\dot x&=\nu-\sigma\Phi(x,y)+\sigma_i R_n(y),\\
\dot y&=q[\sigma\Phi(x,y)-\sigma_iR_n(y)]-\lambda y,\\
\Phi(x,y)&=\frac{x(x+1)(y+1)^2}{L+(x+1)^2(y+1)^2},\\
R_n(y)&=\frac{y^n}{\kappa^n+y^n},\qquad \lambda=\kappa_s+d.
\end{aligned}
\]
The stated asymptotics concern the forward physical-time dynamics of the original ODE, not a rescaled clock. The condition on conversion capacity is satisfied by the paper's baseline numerical parameters. The result does not assert global classification of attractors in the bounded half-space \(\lambda>0\).

## Proof
**(1) Positivity, a uniform substrate ceiling, and completeness.** For all \(x,y\ge0\), \(0\le R_n(y)\le1\) and
\[
0\le\Phi(x,y)=\frac{x}{x+1}\frac{(x+1)^2(y+1)^2}{L+(x+1)^2(y+1)^2}<1.
\]
At the substrate boundary \(x=0\), \(\dot x=\nu+\sigma_iR_n(y)>0\). At \(y=0\) and \(x>0\), \(\dot y=q\sigma\Phi(x,0)>0\). Thus the positive quadrant is forward invariant. Further, for each \(x\ge0\), \(\Phi(x,y)\ge\Phi(x,0)\), and \(\Phi(x,0)\to1\) as \(x\to\infty\). Since \(\sigma>\nu+\sigma_i\), choose \(X>0\) such that \(\sigma\Phi(x,0)>\nu+\sigma_i\) for all \(x\ge X\). Then \(\dot x<0\) whenever \(x\ge X\). Consequently
\[
0<x(t)\le B:=\max\{x_0,X\}\quad\text{for all }t\ge0.
\]
For \(\lambda>0\), \(\dot y\le q\sigma-\lambda y\), so \(y(t)\le\max\{y_0,q\sigma/\lambda\}\). If \(\lambda\le0\), write \(\mu=-\lambda\ge0\); then \(\dot y\le q\sigma+\mu y\). Both bounds exclude finite-time escape, proving forward completeness in every case.

**(2) The exact mass balance and universal divergence.** Set \(M=x+y/q\). Reaction and recycling fluxes cancel *identically*, leaving
\[
\boxed{\dot M=\nu-\lambda y/q.}
\]
When \(\lambda\le0\), \(\dot M\ge\nu\), hence \(M(t)\ge M_0+\nu t\). Since \(x(t)\le B\),
\[
y(t)\ge q(M_0+\nu t-B)\longrightarrow\infty.
\]
In particular, no nonempty compact forward-invariant subset of the positive quadrant can exist for \(\lambda\le0\). When \(\lambda>0\), the already established bounds prove the boundedness half of the dichotomy.

**(3) Exact limiting substrate concentration.** Since \(x(t)\) stays in \([0,B]\) and \(y(t)\to\infty\), the explicit fraction obeys
\[
\sup_{0\le x\le B}\left|\Phi(x,y(t))-\frac{x}{1+x}\right|\le\frac{L}{(1+y(t))^2}\to0,
\]
and \(R_n(y(t))\to1\). Thus the scalar substrate equation is asymptotic, uniformly on the bounded interval, to
\[
\dot x=f(x):=\nu+\sigma_i-\frac{\sigma x}{1+x}.
\]
The continuous function \(f\) is strictly decreasing, positive below and negative above its unique positive zero \(\xi=(\nu+\sigma_i)/(\sigma-\nu-\sigma_i)\). For every \(\varepsilon>0\), sufficiently late trajectories point strictly inward at \(x=\xi-\varepsilon\) and \(x=\xi+\varepsilon\), and move uniformly toward that interval whenever outside it. Therefore \(x(t)\to\xi\).

**(4) Refined linear law at critical removal.** If \(\lambda=0\), integrate the mass identity exactly: \(M(t)=M_0+\nu t\). Consequently
\[
y(t)=q\nu t+q[M_0-x(t)]=q\nu t+q(M_0-\xi)+o(1).
\]

**(5) Refined exponential law below critical removal.** Let \(\lambda=-\mu<0\). Put
\[
h(t)=q\{\sigma\Phi(x(t),y(t))-\sigma_iR_n(y(t))\}.
\]
This is bounded, and Step (3) gives \(h(t)\to q[\sigma\xi/(1+\xi)-\sigma_i]=q\nu\). The product equation is \(\dot y=\mu y+h(t)\), so variation of constants gives the finite limit
\[
C:=\lim_{t\to\infty}e^{-\mu t}y(t)=y_0+\int_0^\infty e^{-\mu s}h(s)\,ds.
\]
To prove **strict positivity**, use \(h(t)\ge-q\sigma_i\). Since \(y(t)\to\infty\), choose \(T\) with \(y(T)>q\sigma_i/\mu\). The comparison equation yields
\[
y(t)\ge\left(y(T)-\frac{q\sigma_i}{\mu}\right)e^{\mu(t-T)}+\frac{q\sigma_i}{\mu}\quad(t\ge T),
\]
so \(C\ge e^{-\mu T}[y(T)-q\sigma_i/\mu]>0\). Moreover,
\[
C e^{\mu t}-y(t)=\int_t^\infty e^{-\mu(s-t)}h(s)\,ds\longrightarrow\frac{q\nu}{\mu},
\]
by dominated convergence. This establishes the claimed additive constant and finishes the proof.

## Verification
The companion standalone script `verify.py` symbolically checks the nonlinear-flux cancellation, the exact saturation identity, the monotonicity identity for the minimal substrate flux, and the equation defining \(\xi\). It also integrates three illustrative positive initial-value problems for \(\lambda=0\), \(\lambda<0\), and \(\lambda>0\). These numerical examples are diagnostic only; the universal asymptotics are proved by the inequalities and limit arguments above. The sign of the finite exponential amplitude is derived analytically rather than inferred from fitted data.

## Relationship to prior work
Wang, Gelens, Xu and Rong (2026), Section II, introduce precisely this system, establish a positive-equilibrium criterion for positive net removal, and describe boundedness without specifying a required sign for \(\kappa_s+d\). Their later sections analyze Hopf bifurcations, birhythmicity, and isolas in parameter windows with positive net removal. The identity obtained by combining the two equations already appears in their equilibrium calculation; it is **not** claimed as new. The result here instead proves the sharp **global boundedness boundary** over the source's signed-\(d\) parameter domain and exact all-initial-state linear/exponential asymptotics on the unbounded side. The earlier Goldbeter–Moran product-recycling model (1988) also uses positive first-order product clearance and analyzes oscillatory domains, not negative-clearance runaway. Its positive-clearance boundedness statement does not cover \(\lambda\le0\). No claim of originality is made for the elementary cancellation itself or for general scalar comparison principles.

## Limitations
The biological interpretation of negative effective removal is limited: it corresponds mathematically to net linear product generation, and physically requires a compensating source or feedback. The result relies on \(\sigma>\nu+\sigma_i\), does not cover conversion capacity at or below supply plus maximal recycling, and does not classify equilibria or cycles when \(\lambda>0\). Its strict positivity assumption avoids boundary regularity questions for noninteger Hill exponents. Historical priority of the combined asymptotic statement has not been independently established.

## References
1. F. Wang, L. Gelens, Y. Xu and L. Rong, *Isolas of limit cycles and birhythmicity induced by cooperative feedback in a glycolysis model*, arXiv:2606.31545, publicly posted 2026-06-30. https://arxiv.org/abs/2606.31545
2. A. Goldbeter and F. Moran, *Dynamics of a biochemical system with multiple oscillatory domains as a clue for multiple modes of neuronal oscillations*, European Biophysics Journal 15 (1988), 277–287. https://utc.ulb.be/ARTICLES/1988_Goldbeter_Eur_Biophys_J.pdf
3. S. Kar and D. S. Ray, *Nonlinear dynamics of glycolysis*, Modern Physics Letters B 18 (2004), 653–678, DOI:10.1142/S0217984904007207 (review; abstract consulted, not treated as full-text exclusion).
