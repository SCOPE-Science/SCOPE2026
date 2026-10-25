# A universal logarithmic high-dose law and an initial-load reversal of cumulative response

## Finding
For the incoherent feedforward differential system
\[
\dot x_u=-x_u+u,\qquad \dot y_u=u-x_uy_u,
\]
with fixed nonnegative initial state \(x_u(0)=x_0\geq0\), \(y_u(0)=y_0\geq0\), define \(C(u,T)=\int_0^T y_u(t)\,dt\) for any fixed \(T>0\). Then:

1. **Universal high-dose law.** Independently of \(x_0,y_0\),
\[
\lim_{u\to\infty}\frac{C(u,T)}{\log u}=\frac12.
\]
2. **Exact onset slope and threshold.** Put \(b(t)=1-e^{-t}\), \(B(t)=t-1+e^{-t}\), and \(A_0(t)=x_0b(t)\). Define the strictly positive quantities
\[
P(T,x_0)=\int_0^T e^{-A_0(t)}\left(\int_0^t e^{A_0(s)}\,ds\right)dt,
\quad Q(T,x_0)=\int_0^T e^{-A_0(t)}B(t)\,dt.
\]
The exact right derivative at zero input is
\[
\partial_u C(0^+,T)=P(T,x_0)-y_0Q(T,x_0).
\]
Consequently, for every \(y_0>P(T,x_0)/Q(T,x_0)\), the cumulative response initially *decreases* with dose but eventually diverges to positive infinity; it has at least one global minimum at a strictly positive input. This is nonmonotonicity for an entire open interval of biologically admissible initial output loads, not an isolated numerical parameter example.

In particular, at \(x_0=0\),
\[
\frac{P(T,0)}{Q(T,0)}=\frac{T^2}{T^2-2T+2(1-e^{-T})}.
\]
The explicit choice \(T=3\), \(x_0=0\), \(y_0=2\) satisfies \(\partial_u C(0^+,3)=-\tfrac12+2e^{-3}<0\) and the same universal high-dose law.

## Assumptions and scope
The input \(u\in[0,\infty)\) is constant over the measurement interval and varied between experiments. Initial conditions \(x_0,y_0\) are nonnegative and *independent of input*. The observation time \(T>0\) is finite and fixed while \(u\to\infty\). The state-space equations are the normalized scalar IFFM1/IFFL1 model, not the full multi-intermediate-node family. Solutions exist globally, are nonnegative, and depend smoothly on \(u\) over finite times by linear-ODE variation of constants.

## Proof
**Step 1: exact solution.** Solving the first equation gives
\[
x_u(t)=x_0e^{-t}+u b(t).
\]
Because \(\int_0^t x_u(r)dr=x_0b(t)+uB(t)\), variation of constants in the second equation gives
\[
y_u(t)=y_0e^{-x_0b(t)-uB(t)}+u\int_0^t
 e^{-x_0(e^{-s}-e^{-t})-u(B(t)-B(s))}\,ds.\tag{1}
\]
Both terms are nonnegative. This formula also proves continuous and differentiable parameter dependence at \(u=0\).

**Step 2: exact zero-dose derivative.** At \(u=0\), \(y_0(t)=y_0 e^{-A_0(t)}\) (the subscript on the left denotes dose zero; \(y_0\) without argument denotes the initial output). Differentiating the ODE with respect to input at zero dose, \(q(t)=\partial_u y_u(t)|_{u=0}\) solves
\[
q'(t)+x_0e^{-t}q(t)=1-b(t)y_0e^{-A_0(t)},\qquad q(0)=0.
\]
The integrating factor \(e^{A_0(t)}\) yields
\[
q(t)=e^{-A_0(t)}\left[\int_0^t e^{A_0(s)}ds-y_0B(t)\right].
\]
Integrating over \([0,T]\) yields the claimed \(P-y_0Q\). Both \(P>0\) and \(Q>0\), since \(B(t)>0\) for every \(t>0\). For \(x_0=0\), direct integration yields \(P=T^2/2\) and \(Q=T^2/2-T+1-e^{-T}\); this gives the displayed explicit threshold and witness.

**Step 3: a Gaussian integral lemma.** For each \(a>0\) and \(\delta>0\), define
\[
G_a(u,t)=u\int_0^t\exp[-au(t^2-s^2)/2]ds.
\]
Then
\[
\lim_{u\to\infty}\frac{1}{\log u}\int_0^\delta G_a(u,t)dt=\frac{1}{2a},
\qquad \sup_{u\ge1}G_a(u,\delta)<\infty.\tag{2}
\]
Indeed, with \(z=\sqrt{au}\,t\) and
\(H(z)=e^{-z^2/2}\int_0^z e^{v^2/2}dv\), one has \(G_a(u,t)=\sqrt{u/a}\,H(\sqrt{au}\,t)\) and
\(\int_0^\delta G_a(u,t)dt=a^{-1}\int_0^{\delta\sqrt{au}}H(z)dz\).
For \(z>0\), substitute \(w=z(z-v)\) to find
\[
zH(z)=\int_0^{z^2}\exp[-w+w^2/(2z^2)]\,dw.
\]
The integrand is bounded by \(e^{-w/2}\) on its integration domain, and tends to \(e^{-w}\) for every fixed \(w\). Dominated convergence gives \(zH(z)\to1\). Therefore \(\int_0^R H(z)dz\sim\log R\) as \(R\to\infty\). This proves both assertions in (2).

**Step 4: squeeze the dose boundary layer.** Fix \(0<\delta<T\) and set \(c_\delta=(1-e^{-\delta})/\delta\), so \(0<c_\delta<1\) and \(c_\delta\to1\) as \(\delta\downarrow0\). Concavity of \(b\) gives \(c_\delta r\le b(r)\le r\) for \(0\le r\le\delta\). Thus, for \(0\le s\le t\le\delta\),
\[
\frac{c_\delta}{2}(t^2-s^2)\le B(t)-B(s)\le\frac12(t^2-s^2),
\quad 0\le x_0(e^{-s}-e^{-t})\le x_0\delta.
\]
Equation (1) consequently yields
\[
e^{-x_0\delta}G_1(u,t)\le y_u(t)\le
 y_0\exp[-c_\delta ut^2/2]+G_{c_\delta}(u,t).\tag{3}
\]
The integral of the middle transient term is at most \(y_0\sqrt{\pi/(2c_\delta u)}\). By (2), the inequalities imply
\[
\frac{e^{-x_0\delta}}2\le\liminf_{u\to\infty}\frac{\int_0^\delta y_u(t)dt}{\log u}
\le\limsup_{u\to\infty}\frac{\int_0^\delta y_u(t)dt}{\log u}\le\frac{1}{2c_\delta}.\tag{4}
\]
For \(t\in[\delta,T]\), \(x_u(t)\ge u b(\delta)\) and comparison with \(z'=u-ub(\delta)z\) gives
\[
0\le y_u(t)\le y_u(\delta)e^{-ub(\delta)(t-\delta)}+rac1{b(\delta)}.
\]
By (2) and (3), \(y_u(\delta)\) is bounded uniformly for all \(u\ge1\), hence \(\int_\delta^T y_u(t)dt=O_{\delta,T,x_0,y_0}(1)\). This interval contributes nothing after division by \(\log u\). Letting \(\delta\downarrow0\) in (4) proves the universal coefficient \(1/2\).

**Step 5: nonmonotonicity and an interior global minimum.** When \(y_0>P/Q\), Step 2 gives a strictly negative right derivative at zero, hence there exists \(v>0\) with \(C(v,T)<C(0,T)\). Step 4 shows \(C(u,T)\to+\infty\). Continuity therefore supplies a global minimizer \(u_*\in(0,\infty)\). The response decreases initially and eventually exceeds its starting value, so it cannot be monotone. No claim of uniqueness of this minimizer is made. ∎

## Verification
All algebraic formulae can be differentiated or integrated directly. The accompanying standalone numerical-check file evaluates the special-case threshold and checks the derivative using independent finite-dose ODE integration. It also checks increasing cumulative responses at large doses and reports where finite numerical tests stop. The universal limit and existence statements are established by Steps 1–5, not by finite numerical sampling.

## Relationship to prior work
The scalar model is exactly row 5 of Table 2, denoted IFFM1, in Wafi–de Oliveira–Sontag (arXiv:2604.01573, first posted 2026-04-02). Section 4.1 and Appendix B, Proposition B.5, prove monotone cumulative response when the initial output is pre-adapted, \(y_0=1\), and cover arbitrary nonnegative initial intermediate state in the scalar case. Their numerical experiments also keep \(y_0=y_{\mathrm{ss}}\) for this model. Gupta–Sontag (2025), section 2, studies the same IFFL1 model with \(y_0\) fixed at its steady-state value; its monotonicity theorem does not quantify arbitrary preloads. The result here keeps the same differential equations but changes the initial-output hypothesis, gives the exact dose-zero derivative threshold and a universal high-dose logarithmic asymptotic, and proves a nonmonotone region. These new conclusions do not contradict the pre-adapted case.

## Limitations
This is a finite-horizon, input-independent-initial-condition theorem for the normalized scalar model. The strict inequality \(y_0>P/Q\) is an exact criterion for negative *initial slope* and a sufficient criterion for nonmonotonicity, not a necessary-and-sufficient criterion for global nonmonotonicity. No uniqueness of the minimum, estimated biological parameter ranges, statistical dose-estimation accuracy, or generalization to the full matrix IFFM network is proved. The logarithmic asymptotic is a ratio limit; no finite-input error bound or constant second asymptotic term is claimed. The normal form assumes dose enters both equations without saturation.

## References
1. M. K. Wafi, A. C. B. de Oliveira and E. D. Sontag, *When is cumulative dose response monotonic? Analysis of incoherent feedforward motifs*, arXiv:2604.01573, first posted 2026-04-02; https://arxiv.org/abs/2604.01573 . In particular Table 2 model 5, §4.1, Appendix B Proposition B.5 and §5.
2. V. Gupta and E. D. Sontag, *Cumulative dose responses for adapting biological systems*, Journal of the Royal Society Interface 22 (2025), article 20240877, https://doi.org/10.1098/rsif.2024.0877 ; accessible full-text author reprint: https://www.sontaglab.org/FTPDIR/2025_gupta_sontag_cdr_rsi_reprint.pdf . In particular §1.8 and §2.
