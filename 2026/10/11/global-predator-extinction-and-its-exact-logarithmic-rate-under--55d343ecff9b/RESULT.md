# Global predator extinction and its exact logarithmic rate under a sharp handling-time barrier

## Finding

For the cooperative-hunting predator–prey maturation-delay model (15) of Enatsu, Roy and Banerjee [1], **every strictly positive initial history** converges to the predator-free equilibrium \((\kappa,0)\) if
\[
 h\ge q:=e^{-\beta\tau}.
\]
This includes equality, all finite delays, and arbitrarily strong cooperation. Predator extinction is exponential and has the **exact, initial-history-independent logarithmic rate**
\[
 \lim_{t\to\infty}\frac{\log p(t)}{t}=-\rho_*,\qquad
 \rho_*+\frac{q\kappa}{1+h\kappa}e^{\rho_*\tau}=1,
 \quad 0<\rho_*<1.
\]
The bound is sharp as a **parameter-uniform** guarantee: if \(h<q\), choices of \(\kappa>1/(q-h)\) admit a strictly positive coexistence equilibrium for every choice of positive \(\sigma\) and \(\alpha\). It is not claimed that every individual parameter tuple with \(h<q\) persists.

## Assumptions and scope

Fix \(\sigma,\kappa,\alpha,h,\beta>0\) and a finite delay \(\tau\ge0\). Set \(q=e^{-\beta\tau}\), and define the saturating capture kernel
\[
 H(n,p)=\frac{(1+\alpha p)n}{1+h(1+\alpha p)n}.
\]
For \(t\ge0\) consider
\[
 \begin{aligned}
 \dot n(t)&=\sigma n(t)\left(1-\frac{n(t)}{\kappa}\right)-H(n(t),p(t))p(t),\\
 \dot p(t)&=qH(n(t-\tau),p(t-\tau))p(t-\tau)-p(t).
 \end{aligned}
\]
Histories \((n_0,p_0)\in C([ -\tau,0],(0,\infty)^2)\) are arbitrary; at \(\tau=0\) they reduce to strictly positive initial values. The conclusions concern classical solutions of this retarded system; all logarithms are natural. Positivity is required to obtain the finite logarithmic decay exponent for predator density.

## Proof

**1. Global positive bounded solutions.** Strict positivity of prey follows from its multiplicative equation (the predation term equals \(n\) times a locally bounded nonnegative coefficient). The variation-of-constants formula
\[
 p(t)=p(0)e^{-t}+q\int_0^t e^{-(t-s)}H(n(s-\tau),p(s-\tau))p(s-\tau)\,\mathrm ds
\]
with the method of steps shows \(p(t)>0\). Let
\[
 K=\max\!\left\{\kappa,\max_{s\in[-\tau,0]}n(s)\right\},\qquad
 P=\max_{s\in[-\tau,0]}p(s).
\]
The logistic differential inequality \(\dot n\le\sigma n(1-n/\kappa)\) implies \(0<n(t)\le K\). The exact saturation inequality
\[
 0\le qH(n,p)=\frac{q(1+\alpha p)n}{1+h(1+\alpha p)n}<\frac{q}{h}\le1
\]
holds for every finite positive \(n,p\) under \(h\ge q\). Thus the constant \(P\) is a supersolution of the scalar predator delay equation and comparison gives \(0<p(t)\le P\). The finite bounds and local regularity exclude finite-time blow-up.

**2. A strict uniform subcritical margin, even at equality.** The monotonicity of \(H\) in each nonnegative argument and the bounds above give
\[
 qH(n(t),p(t))\le A:=\frac{qK(1+\alpha P)}{1+hK(1+\alpha P)}<1.
\]
The strict inequality holds even when \(h=q\), because \(K,P\) are finite. The function \(r\mapsto r+Ae^{r\tau}\) increases strictly from \(A<1\) at \(r=0\) to more than \(1\) at \(r=1\); hence there is a unique \(\rho_A\in(0,1)\) satisfying \(\rho_A+Ae^{\rho_A\tau}=1\). The function \(t\mapsto Pe^{-\rho_A t}\) solves the constant-coefficient linear delay equation \(\dot y=Ay(t-\tau)-y(t)\) and dominates the history \(p(s)\le P\) for \(s\in[-\tau,0]\). Quasimonotone scalar comparison yields
\[
 0<p(t)\le Pe^{-\rho_A t}\qquad(t\ge0).
\]

**3. Recovery of the prey carrying capacity.** Write
\[
 d(t)=\frac{(1+\alpha p(t))p(t)}{1+h(1+\alpha p(t))n(t)}.
\]
Then \(0\le d(t)\le(1+\alpha P)Pe^{-\rho_A t}\to0\). For \(u(t)=1/n(t)\), direct differentiation gives the *linear* nonautonomous equation
\[
 \dot u(t)=(-\sigma+d(t))u(t)+\frac{\sigma}{\kappa}.
\]
For every \(\delta\in(0,\sigma)\), eventually \(0\le d(t)\le\delta\). Scalar ODE comparison between coefficient bounds \(-\sigma\) and \(-\sigma+\delta\) implies
\[
 \frac1\kappa\le\liminf_{t\to\infty}u(t)
 \le\limsup_{t\to\infty}u(t)
 \le\frac{\sigma}{\kappa(\sigma-\delta)}.
\]
Sending \(\delta\downarrow0\) proves \(u(t)\to1/\kappa\), hence \(n(t)\to\kappa\).

**4. Exact logarithmic extinction exponent.** The predator gain coefficient
\[
 a(t)=qH(n(t-\tau),p(t-\tau))
\]
converges to \(a_*=q\kappa/(1+h\kappa)\), which lies strictly between \(0\) and \(1\). Fix any \(\eta>0\) small enough that \(0<a_-:=a_*-\eta<a_+:=a_*+\eta<1\). For all \(t\ge T\) sufficiently large,
\[
 a_-p(t-\tau)-p(t)\le\dot p(t)\le a_+p(t-\tau)-p(t).
\]
Let \(\rho_-\) and \(\rho_+\) be the unique roots in \((0,1)\) of \(\rho+a_-e^{\rho\tau}=1\) and \(\rho+a_+e^{\rho\tau}=1\), respectively (so \(\rho_+<\rho_-\)). Since \(p\) is continuous and strictly positive on \([T-\tau,T]\), one may choose finite constants \(m>0\) and \(M>0\) such that comparison with the two exponential solutions yields
\[
 me^{-\rho_-(t-T)}\le p(t)\le Me^{-\rho_+(t-T)}\quad(t\ge T).
\]
Consequently \(-\rho_-\le\liminf_{t\to\infty}\log p(t)/t\le\limsup_{t\to\infty}\log p(t)/t\le-\rho_+\). Continuity and uniqueness of the characteristic root as \(\eta\downarrow0\) give the claimed limit \(-\rho_*\).

**5. Sharpness as a uniform guarantee.** Suppose \(0<h<q\) and select \(\kappa>1/(q-h)\). For \(v\ge0\) define
\[
 N(v)=\frac{1}{(q-h)(1+\alpha v)},\qquad
 F(v)=q\sigma N(v)\left(1-\frac{N(v)}\kappa\right)-v.
\]
At \(v=0\), \(N(0)=1/(q-h)<\kappa\), so \(F(0)>0\), whereas \(F(v)\to-\infty\) as \(v\to\infty\). By continuity there is a root \(v_*>0\). Because \(qH(N(v_*),v_*)=1\) and \(F(v_*)=0\), the constant history \((N(v_*),v_*)\) is a strictly positive coexistence equilibrium. It does not undergo predator extinction, establishing sharpness in the stated parameter-uniform sense. This construction does not establish persistence for all subcritical handling times and capacities.

## Verification

The executable standard-library-only script `verify.py` checks exact rational identities underpinning the saturation barrier and coexistence construction, independently recomputes characteristic roots by bracketing, and tests illustrative admissible parameters on both sides and at the equality boundary. Run `python3 verify.py` in the directory containing this file; expected terminal output is `CHECK_OK`. The proof above, rather than these finite checks, establishes the universal statements.

## Relationship to prior work

Enatsu, Roy and Banerjee [1, equations (15a)–(15b), Theorem 3.1, subsequent stability analysis, and Discussion] establish the delayed model, count positive equilibria and analyze local predator-free stability and bifurcation scenarios. Their disappearance of positive equilibria and numerical approach to extinction does not imply every positive delay history converges or specify its exponential tail. The present result establishes the global all-history theorem, including the saturation equality, and an exact exponent without a small-cooperation assumption.

For the same handling-time barrier, exclusion of strictly positive periodic coexistence follows from the global theorem. A no-cycle statement alone would not exclude nonperiodic omega limits or establish the exact logarithmic extinction rate. Standard scalar delay comparison principles are used as proof techniques; no generic new comparison theorem is claimed. Neighboring cooperative-hunting delay articles [2,3] study related but not identical delayed vector fields and do not supply an inspected dominating statement for this exact model and parameter boundary.

## Limitations

The theorem only guarantees global extinction when \(h\ge e^{-\beta\tau}\). For smaller handling time, predator extinction can still occur for particular parameter choices or histories; this result does not classify those basins. The rate is a limit of \(t^{-1}\log p(t)\), not a claim that \(p(t)e^{\rho_*t}\) converges to a positive constant. No finite-time population extinction or stochastic version is claimed. Results for nonnegative histories with identically zero prey or predator are outside the logarithmic-rate statement. The related 2025 maturation/hunting paper [2] was available only at abstract/metadata level for comparison; additional full-text verification may reveal more relevant overlap.

## References

[1] Y. Enatsu, J. Roy, M. Banerjee, “Hunting cooperation in a prey–predator model with maturation delay,” *Journal of Biological Dynamics* 18 (2024), article 2332279, published online 2024-03-22, DOI: 10.1080/17513758.2024.2332279.

[2] K. Vishwakarma, “Dynamics of a Predator–Prey Model with Maturation Delay and Hunting Cooperation in Predator,” *International Journal of Applied and Computational Mathematics* 11 (2025), DOI: 10.1007/s40819-025-01879-w; abstract and indexed metadata consulted.

[3] “Dynamical Regimes in a Delayed Predator–Prey Model with Predator Hunting Cooperation: Bifurcations, Stability, and Complex Dynamics,” *Modelling* 6 (2025), article 84, DOI: 10.3390/modelling6030084; different prey-delay formulation.
