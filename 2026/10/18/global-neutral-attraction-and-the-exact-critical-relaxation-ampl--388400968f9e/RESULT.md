# Global neutral attraction and the exact critical relaxation amplitude in a two-group cultural polarization model

## Finding
For the two-group nonlinear opinion dynamics with sender reformulation, structural homophily, receiver-tailored amplification and optional content filtering described below, the **sharp global neutral-attraction threshold** is
\[
\kappa+\beta[\tau+(1-\tau)(1-\rho+\rho\alpha)]\le 1.
\]
At and below this boundary, every trajectory in the physical opinion square converges to neutral consensus and no other equilibrium exists; strictly below it the convergence is uniformly exponential. Above it, neutral consensus is linearly unstable and nonzero consensual equilibria exist. At equality, write \(m(t)=(x_+(t)+x_-(t))/2\). For every initial condition with \(m(0)\ne0\),
\[
\lim_{t\to\infty}\sqrt t\,m(t)
=\operatorname{sgn}(m(0))\sqrt{\frac{3}{2\ell[1+\beta(1-\tau)\rho\alpha^3]}}.
\]
The opinion difference \(p(t)=(x_+(t)-x_-(t))/2\) decays exponentially. On the invariant antisymmetric axis \(m(0)=0\), both opinions decay exponentially, rather than following the universal algebraic common-mode law. Thus at criticality the cubic coefficient detects nonlinear cultural reformulation, while the asymptotic common-mode amplitude is independent of structural mixing contrast.

## Assumptions and scope
Two group opinions satisfy \((x_+,x_-)\in[-1,1]^2\). The map for cultural sender reformulation, the structural interaction matrix, and the received field are
\[
\begin{aligned}
\Phi(s)&=(1-\rho)s+\rho\tanh(\alpha s),\\
A_\eta&=\frac12\begin{pmatrix}1+\eta&1-\eta\\1-\eta&1+\eta\end{pmatrix},\\
h(x)&=(1-\tau)A_\eta\bigl(\Phi(x_+),\Phi(x_-)\bigr)^\top+\tau x,\\
r_i(x)&=\tanh(\beta h_i(x)).
\end{aligned}
\]
The parameters obey \(0\le\rho\le1\), \(\alpha\ge0\), \(\beta>0\), \(0\le\tau<1\), \(0\le\eta<1\), and \(a=1-\rho+\rho\alpha>0\). The direct-response law is
\[
\dot x_i=\lambda(r_i-x_i),\qquad\lambda>0.
\]
The content-filtered law is
\[
\dot x_i=\frac\gamma2\{r_i+u_i-x_i(1+r_i u_i)\},\qquad
u_i=\tanh(\kappa x_i),\quad\gamma>0,\quad\kappa=k_A/2\ge0.
\]
This formulation also covers the direct law by setting \(\kappa=0\) and using \(\ell=\lambda\) rather than \(\ell=\gamma/2\). In the filtered law, set \(\ell=\gamma/2\). For either law define
\[
H=\tau+(1-\tau)a,\quad
c=\kappa+\beta H,\quad
Q=1+\beta(1-\tau)\rho\alpha^3,\quad
\delta=\ell\beta(1-\tau)(1-\eta)a.
\]
All parameters, vector fields, uniqueness and limits refer to continuous physical time. The statements quantify over **every** initial opinion pair in the entire square; there is no equilibrium-selection assumption. The square is forward invariant because each component field is strictly inward at the corresponding boundary face.

## Proof
**1. Envelope and global neutral-attraction threshold.** Since \(\Phi\) is odd and monotone with \(|\Phi(s)|\le a|s|\) for \(|s|\le1\), and \(A_\eta\) has nonnegative rows summing to one,
\[
M:=\max\{|x_+|,|x_-|\}\quad\Longrightarrow\quad
|h_i|\le HM,\qquad |r_i|\le R:=\tanh(\beta HM).
\]
At any nonzero state, choose an index where \(|x_i|=M\) and orient the component by its sign. For the direct law,
\[
\operatorname{sgn}(x_i)\dot x_i\le\ell[R-M]
\le\ell[\tanh(cM)-M].
\]
For the filtered law put \(U=\tanh(\kappa M)\). At the positive active face the component velocity is increasing in the received response \(r\), since its derivative with respect to \(r\) is \(\ell(1-MU)>0\). Maximizing at \(r=R\) gives, by the addition formula for hyperbolic tangents,
\[
\begin{aligned}
\operatorname{sgn}(x_i)\dot x_i
&\le\ell\{R+U-M(1+RU)\}\\
&=\ell(1+RU)\{\tanh(cM)-M\}.
\end{aligned}
\]
The negative active face follows from global reversal symmetry. Taking the maximum over all active coordinates yields the upper Dini derivative of \(M\). Thus for \(c\le1\), since \(RU\ge0\) and \(\tanh(cM)\le\tanh M<M\) for \(M>0\), **both** response laws satisfy
\[
D^+M\le-\ell(M-\tanh M)<0\qquad(M>0).
\]
It follows that the origin is the only equilibrium and globally attracting. If \(c<1\), use \(\tanh(cM)\le cM\), obtaining the explicit uniform bound
\[
M(t)\le M(0)e^{-\ell(1-c)t}.
\]
At \(c=1\), let \(b_*:=\min_{0\le v\le1}(v-\tanh v)/v^3>0\), defining the quotient at zero by \(1/3\). Comparison of \(D^+M\le-\ell b_*M^3\) proves the global critical estimate
\[
M(t)\le\bigl(M(0)^{-2}+2\ell b_*t\bigr)^{-1/2}
\]
when \(M(0)>0\); the zero trajectory is stationary.

If \(c>1\), the invariant consensus diagonal \(x_+=x_-=z\) has scalar linearization \(\dot z=\ell(c-1)z+O(z^3)\), so the neutral equilibrium has an unstable common mode. The scalar field at \(z=1\) is strictly negative: \(r<1\) for finite parameters, and in the filtered case the inward expression equals \(-\ell(1-r)(1-u)<0\). Continuity implies a positive interior fixed point; oddness supplies a negative one. This establishes sharpness.

**2. Critical fast and slow variables.** On the surface \(c=1\), define \(m=(x_++x_-)/2\) and \(p=(x_+-x_-)/2\). Exchange of groups sends \(p\mapsto-p\); simultaneous reversal sends \((m,p)\mapsto(-m,-p)\). Consequently the exact analytic vector field has invariant axes \(m=0\) and \(p=0\), and near the origin it has the forms
\[
\dot m=m\left[-\frac{\ell Q}{3}m^2+O(m^4+p^2)\right],
\qquad
\dot p=p\left[-\delta+O(m^2+p^2)\right].
\]
Indeed, writing \(B=\beta H\) and \(C=\beta(1-\tau)\rho\alpha^3\), the consensus expansion is
\[
\begin{aligned}
\Phi(m)&=am-\rho\alpha^3m^3/3+O(m^5),\\
r&=Bm-(B^3+C)m^3/3+O(m^5),\\
u&=\kappa m-\kappa^3m^3/3+O(m^5).
\end{aligned}
\]
For the filtered response \(r+u-m(1+ru)\), the cubic coefficient simplifies, using \(B+\kappa=1\), to
\[
-\frac{B^3+\kappa^3+C+3B\kappa}{3}=-\frac{1+C}{3}=-\frac Q3.
\]
The same expression results for the direct response by \(\kappa=0\). The transverse linear coefficient is
\[
\ell\{\kappa+\beta[\tau+(1-\tau)\eta a]-1\}=-\delta<0.
\]

**3. Exact asymptotic amplitude.** The global estimate from step 1 ensures \((m(t),p(t))\to(0,0)\). Therefore, for large enough time, the transverse equation yields \(|p(t)|=O(e^{-\delta t/2})\). If \(m(0)=0\), invariant-axis uniqueness gives \(m(t)=0\) for all time; the transverse exponential statement proves the exceptional behavior. Otherwise \(m(t)\) never changes sign by invariance and ODE uniqueness. From the displayed nonlinear equation, \(d\log|m|/dt\to0\), so for every \(\epsilon>0\) there is a constant \(C_\epsilon>0\) such that \(|m(t)|\ge C_\epsilon e^{-\epsilon t}\) for sufficiently large \(t\). Therefore \(p(t)^2/m(t)^2\to0\). The slow equation gives
\[
\frac{d}{dt}\frac1{m(t)^2}
=\frac{2\ell Q}{3}+O(m(t)^2)+O\left(\frac{p(t)^2}{m(t)^2}\right)
\longrightarrow\frac{2\ell Q}{3}.
\]
Averaging this derivative in physical time proves
\[
\lim_{t\to\infty}t\,m(t)^2=\frac{3}{2\ell Q},
\]
with the initial sign determining the signed limit in the Finding. No finite simulation is used to establish the infinite-time claim.

## Verification
The standalone `verify.py` checks exact rational identities at one nontrivial critical parameter point, symbolically reconstructs the cubic coefficient, tests 2,400 randomly selected inward-envelope inequalities and numerically integrates the critical system for both update laws and multiple initial conditions. Run `python -m pip install -r requirements.txt` and then `python verify.py`. Its successful output is a reproducibility check, not a substitute for steps 1–3. For the filtered instance \(\rho=1/2,\alpha=2,\tau=1/4,\eta=1/3,\kappa=1/5,\beta=32/55,\gamma=2\), the exact values are \(H=11/8\), \(c=1\), \(Q=151/55\), \(\delta=24/55\), and the asymptotic magnitude coefficient is \(\sqrt{165/302}\).

## Relationship to prior work
Michaud and Jansson (arXiv:2609.37521v1, 2026) introduced the nonlinear two-group cultural, structural and mediated polarization model and studied its fixed points and **local** neutral-state stability. Their local common-mode threshold provides the motivation for identifying the actual global basin and sharp nonhyperbolic rate. The present result is not a claim that cubic critical slowing or hyperbolic-tangent stability estimates are new in themselves. It combines a global max-norm comparison, an explicit local cubic identity under optional filtering, and the full two-group critical asymptotic across all initial states. Existing general mean-field Ising and nonlinear-network Lyapunov theories are relevant conceptual antecedents; implication-equivalent broader general theorems cannot be excluded categorically.

## Limitations
The global attraction theorem requires nonnegative mixing weights, finite nonnegative response parameters, positive cross-group mixing \(\eta<1\), and no exogenous opinion bias. Without strictly positive cross-group mixing the antisymmetric eigenvalue can vanish and the one-dimensional critical asymptotic need not hold. The theorem does not address more than two communities, signed edges, time delays, stochastic forcing, heterogeneous group parameters or a global classification of polarized equilibria above threshold. Its originality is reviewed provisionally; independent historical-priority verification has not been performed.

## References
1. Michaud and Jansson, *Cultural, Structural, and Mediated Routes to Polarization in a Nonlinear Mean-Field Model*, arXiv:2609.37521v1, first public September 29, 2026, https://arxiv.org/abs/2609.37521 .
2. Baron, *Consensus, polarisation and coexistence in a continuous opinion dynamics model with quenched disorder*, 2021, https://arxiv.org/abs/2105.06123 .
