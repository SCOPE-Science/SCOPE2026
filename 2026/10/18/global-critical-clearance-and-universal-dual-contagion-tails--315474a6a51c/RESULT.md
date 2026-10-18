# Global critical clearance and universal dual-contagion tails

## Finding

Consider the deterministic, well-mixed, disease-exchange-symmetric two-SIS-contagion model with transmission rate \(\tau\), singly infected recovery rate \(\gamma>0\), recovery rate \(\gamma_2>0\) per infection in doubly infected individuals, and transmission multiplier \(\alpha>0\) for doubly infected individuals. Let \(u(t)\) denote the fraction in **each** singly infected class and \(v(t)\) the doubly infected fraction. At the exact degeneracy separating the two local transition types,
\[
\tau=\gamma,\qquad \alpha=\frac{2\gamma_2}{\gamma},
\]
**every** physically admissible initial state converges to the disease-free state. Moreover, for **every nonzero** admissible initial state,
\[
\boxed{\lim_{t\to\infty}\sqrt t\,u(t)=\sqrt{\frac{\gamma_2}{2\gamma^2}}},\qquad
\boxed{\lim_{t\to\infty}t\,v(t)=\frac1{2\gamma}}.
\]
Consequently, for either disease, \(i(t)=u(t)+v(t)\) obeys \(i(t)\sim\sqrt{\gamma_2/(2\gamma^2t)}\), and \(v(t)/u(t)^2\to\gamma/\gamma_2\). In particular, **the asymptotic amplitude of the doubly infected class is independent of its recovery rate** after tuning the interaction to the degeneracy boundary.

## Assumptions and scope

The four mutually exclusive joint states are \(SS\), \(IS\), \(SI\), and \(II\). Disease-exchange symmetry is imposed on the initial state so that \([IS]=[SI]=u\), \([II]=v\), and \([SS]=1-2u-v\). The feasible triangle is
\[
\mathcal T=\{(u,v):u\ge0,\ v\ge0,\ 2u+v\le1\}.
\]
In physical time, set \(\Phi=\tau(u+\alpha v)\). The governing equations, taken from the source's interacting-contagions model, are
\[
\dot u=(1-3u-v)\Phi+\gamma_2v-\gamma u,\qquad
\dot v=2u\Phi-2\gamma_2v.
\]
All parameters and initial conditions are deterministic and fixed; no fast-variable or quasistatic approximation is used. The theorem assumes \(\gamma,\gamma_2>0\) and the specified equalities for \(\tau,\alpha\), and asserts no rate for the identically disease-free initial state.

## Proof

**1. Exact critical vector field and physical invariance.** Set \(h=\gamma_2/\gamma>0\) and dimensionless time \(s=\gamma t\). At \(\tau=\gamma\), \(\alpha=2h\), direct expansion gives
\[
\begin{aligned}
\frac{du}{ds}&=3hv-3u^2-(1+6h)uv-2hv^2=:F(u,v),\\
\frac{dv}{ds}&=2u^2+4huv-2hv=:G(u,v).
\end{aligned}
\]
On the face \(v=0\), \(G=2u^2\ge0\). On the face \(u=0\), \(F=hv(3-2v)\ge0\) for \(0\le v\le1\). Finally, writing \(w=1-2u-v\), the original transition equations yield \(dw/ds=-2w(u+2hv)+2u\), hence \(dw/ds=2u\ge0\) on \(w=0\). The compact triangle \(\mathcal T\) is positively invariant. The vector field is polynomial, so every solution from \(\mathcal T\) exists for all positive time. Every nonzero solution has \(u,v>0\) for all sufficiently small positive time and thereafter by inward-pointing boundaries.

**2. Global convergence, not merely a local stability statement.** The weighted infected mass
\[
Z(u,v)=u+\frac32v
\]
has the exact identity
\[
\frac{dZ}{ds}=F+\frac32G=-v(u+2hv)\le0.
\]
The zero-derivative set is exactly \(v=0\). If \(v=0\) and \(u>0\), then \(dv/ds=2u^2>0\); thus the largest invariant subset of the zero-derivative set is the origin. LaSalle's invariance principle on the compact positively invariant triangle yields
\[
(u(s),v(s))\longrightarrow(0,0)
\]
for every state in \(\mathcal T\). In particular, the disease-free state is the unique equilibrium in \(\mathcal T\).

**3. The fast doubly infected class becomes quadratic in the slow total.** Fix a nonzero initial state. Since \(Z>0\) at positive finite times, introduce \(q=v/Z\) and \(r=v/Z^2\). The physical bounds imply
\[
0\le u/Z\le1,\quad 0\le v/Z\le2/3,\quad 0<Z\le3/2.
\]
The equations for \(v\) and \(Z\) give the **exact** scalar identities
\[
\begin{aligned}
q'&=\frac{2u^2}{Z}
  +q\left[-2h+4hu+\frac{v(u+2hv)}{Z}\right],\\
r'&=2\left(\frac{u}{Z}\right)^2
  +r\left[-2h+4hu+\frac{2v(u+2hv)}{Z}\right],
\end{aligned}
\]
where prime denotes differentiation with respect to \(s\). Since \(u,v,Z\to0\) and \(v(u+2hv)/Z\le(2/3)(1+4h/3)Z\to0\), the coefficient multiplying \(q\) is eventually at most \(-h\). Also \(2u^2/Z\le2Z\to0\). Scalar differential comparison gives \(q(s)\to0\). Therefore \(u/Z=1-3q/2\to1\). In the equation for \(r\), the inhomogeneity tends to \(2\) and the coefficient multiplying \(r\) tends to \(-2h\); elementary variation of constants (eventual uniform exponential stability of this scalar inhomogeneous equation) gives
\[
\lim_{s\to\infty}r(s)=\frac1h.
\]
This last step requires no center-manifold theorem and applies to every nonzero physical initial state.

**4. Exact algebraic amplitudes.** By the identity for \(Z\),
\[
\frac{d}{ds}Z^{-2}
 =\frac{2v(u+2hv)}{Z^3}
 =2r\left(\frac uZ+2h\frac vZ\right)
 \longrightarrow\frac2h.
\]
Integrating the derivative limit and dividing by \(s\) proves \(sZ(s)^2\to h/2\). Since \(u/Z\to1\) and \(v/Z^2\to1/h\), it follows that
\[
\lim_{s\to\infty}\sqrt s\,u(s)=\sqrt{h/2},\qquad
\lim_{s\to\infty}s\,v(s)=1/2.
\]
Substituting \(s=\gamma t\) and \(h=\gamma_2/\gamma\) yields the claimed physical-time limits. The same limits give \(v/u^2\to1/h=\gamma/\gamma_2\), completing the proof.

## Verification

`verify.py` checks the exact vector field against the original joint-state equations using symbolic algebra, confirms the three boundary-invariance identities, checks the weighted Lyapunov derivative and both exact ratio equations, and integrates the system for five distinct values of \(h\) and three distinct initial conditions per value. The finite-time checks compare the scaled quantities to their limiting constants at dimensionless time \(s=100000\). Execute `python verify.py` after installing dependencies listed in `requirements.txt`. Symbolic identities corroborate the algebra; the infinite-time statements follow from the proof above, **not** from the finite integrations.

## Relationship to prior work

Hébert-Dufresne, Simon and Kiss, *Fast-variable reduction to complex contagion unifies epidemic models* (arXiv:2610.05467v1, first posted October 4, 2026), Appendix 6.2.4, equations (93)–(113), supplies the exact symmetric co-infection equations and locates \(\tau_c=\gamma\) and the continuous/discontinuous transition boundary \(\alpha^*=2\gamma_2/\gamma\). Its quasi-static force-of-infection calculation determines the **sign** of the first local bifurcation coefficient on either side of the boundary. It does not state or prove global attraction at equality or the two physical-time decay amplitudes for the original two-dimensional dynamics. Those are the contribution proved here.

Hébert-Dufresne, Scarpino and Young, *Interacting contagions are indistinguishable from social reinforcement* (arXiv:1906.01147), establishes a correspondence with complex contagion and studies qualitative transitions; this physical mapping and the existence of transition boundaries are not claimed as new. Generic cubic critical slowdowns are also known in other epidemic normal forms. The current result concerns the **specific full cooperative two-SIS equations**, their global physical state triangle, an exact weighted Lyapunov identity, and a doubly infected tail with an amplitude universal in \(\gamma_2\). It is not a generic claim that algebraic critical exponents are novel.

## Limitations

The model is a deterministic well-mixed mean-field system, with exactly equal disease transmission parameters and disease-exchange-symmetric initial data. It does not cover the full four-state nonsymmetric dynamics, non-mean-field networks, finite-population stochastic extinction times, deviations away from both critical parameter equalities, or finite-time error bounds uniform as \(\gamma_2/\gamma\to0\) or \(\infty\). The strict nonzero-initial-state condition is necessary for the positive asymptotic amplitudes. Historical priority has not received an independent expert audit.

## References

1. L. Hébert-Dufresne, P. L. Simon and I. Z. Kiss, *Fast-variable reduction to complex contagion unifies epidemic models*, arXiv:2610.05467v1 (posted October 4, 2026), Appendix 6.2.4, equations (93)–(113). https://arxiv.org/html/2610.05467v1
2. L. Hébert-Dufresne, S. V. Scarpino and J.-G. Young, *Interacting contagions are indistinguishable from social reinforcement*, arXiv:1906.01147 (2019). https://arxiv.org/abs/1906.01147
