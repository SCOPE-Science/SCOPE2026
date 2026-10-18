# Phase-resolved excursion laws for a rational-degree grazing map

## Finding

Consider the continuous one-dimensional grazing map
\[
f_\mu(x)=\begin{cases}
\nu x+a(\mu-x)^\gamma,&x\le\mu,\\
\nu x,&x\ge\mu,
\end{cases}
\qquad 0<\nu<1,\quad a>0,\quad \gamma=\frac qp\in(0,1),
\]
where \(p>q\ge1\) are coprime integers. Let \(I_\mu=[\nu\mu,\mu]\), let \(Z\) be uniform on \([\nu,1]\), and start at \(x_0=\mu Z\). The **first return** is \(T_\mu=\min\{n\ge1:f_\mu^n(x_0)\in I_\mu\}\), and the normalized return location is \(R_\mu=f_\mu^{T_\mu}(x_0)/\mu\).

Put \(\alpha=1-\gamma\), \(\lambda=\log(1/\nu)\), and, for integers \(j\to\infty\) and any fixed phase \(\theta\in[0,1)\), choose
\[
\mu_j(\theta)=(a\nu^{j+\theta})^{1/\alpha}.
\]
Let \(U=1-Z\) be uniform on \((0,1-\nu)\), and define
\[
V=\frac\gamma\lambda\log\frac1U,\qquad
J_\theta=1-\lfloor V-\theta\rfloor,\qquad
Q_\theta=\nu^{\{V-\theta\}},
\]
where \(\{t\}=t-\lfloor t\rfloor\). Then, under the natural coupling using the same \(U\),
\[
\boxed{\quad (T_{\mu_j}-j,R_{\mu_j})\longrightarrow(J_\theta,Q_\theta)
\quad\text{almost surely}.\quad}
\]
In particular, the centered integer return time converges in **total variation**, and the pair converges in distribution.

For \(v_0=(\gamma/\lambda)\log(1/(1-\nu))\), \(\rho=\lambda/\gamma\), and every integer \(h\), the limiting return-time tail has the exact phase-dependent form
\[
\boxed{\quad
\Pr(J_\theta\ge h)
=\max\left\{0,1-\frac{\nu^{(\theta+2-h)/\gamma}}{1-\nu}\right\}.\quad}
\]
Set \(h_0=\lfloor\theta+1-v_0\rfloor\). On the entire long-excursion stratum \(J_\theta\le h_0\), the nonnegative deficit \(h_0-J_\theta\) and the return coordinate \(Q_\theta\) are **independent**: the deficit is geometric, with probabilities \((1-\nu^{1/\gamma})\nu^{k/\gamma}\) for \(k=0,1,2,\ldots\), while the return-coordinate density is
\[
\boxed{\quad g(r)=\frac{r^{1/\gamma-1}}{\gamma(1-\nu^{1/\gamma})},
\qquad \nu<r<1.\quad}
\]
Thus the long-excursion duration and reinjection location separate into an exact geometric law and a universal power-law kernel, despite the phase dependence of the full return-time distribution.

There is also a first finite-parameter correction. For any fixed integer \(h\) for which \(b_h:=\nu^{(\theta+2-h)/\gamma}\) lies strictly between \(0\) and \(1-\nu\),
\[
\Pr(T_{\mu_j}-j\ge h)
=1-\frac{b_h}{1-\nu}
+\frac{(1-b_h)b_h^{1-\gamma}}{\gamma(1-\nu)}\nu^{j+\theta+1}
+O(\nu^{2j}).
\]
All limits and error terms hold for each fixed admissible parameter choice, phase, and indicated threshold; the probability refers to the initial uniform distribution, not an invariant distribution of the map.

## Assumptions and scope

All phase limits take \(j\to\infty\) with \(\nu,a,p,q,\theta\) fixed. The coefficient \(a\) is the coefficient denoted \(e\) in equation (4) of the source. Both branches agree at \(x=\mu\). Initial points belong to the full closed natural section \(I_\mu\); its endpoints have probability zero under the specified uniform law. The almost-sure statements exclude the null set where \(U=0\) or \(V-\theta\) is an integer. Neither mixing nor existence of an absolutely continuous invariant probability is assumed.

For example, if \(\nu=\gamma=1/2\), \(a=1\), and \(\theta=0\), then \(\mu_j=4^{-j}\) and
\[
\Pr(J_0=1)=\frac12,\qquad
\Pr(J_0=-k)=\frac38\,4^{-k}\quad(k\ge0),\qquad
\mathbb E J_0=\frac13.
\]
In this example, conditioned on \(J_0\le0\), the reinjection density is \(g(r)=8r/3\) on \((1/2,1)\).

## Proof

**1. Exact first-return reduction.** Write \(z=1-u\in[\nu,1]\). The first image of \(\mu z\) is
\[
y=\mu\{\nu(1-u)+a\mu^{-\alpha}u^\gamma\}.
\]
For all sufficiently small positive \(\mu\), \(y\ge\nu\mu\) uniformly in \(u\in[0,1-\nu]\): for \(u>0\), it suffices that \(a\mu^{-\alpha}u^{\gamma-1}\ge\nu\), which follows from \(a\mu^{-\alpha}(1-\nu)^{\gamma-1}\ge\nu\). If \(y\le\mu\), the orbit returns immediately. Otherwise every iterate before its return is on the linear branch and equals a successive multiple of \(\nu y\). The first such multiple not exceeding \(\mu\) lies in \([\nu\mu,\mu]\), so return is always finite. With \(s=\log(y/\mu)/\lambda\), the exact identity is
\[
T_\mu=1+\max\{0,\lceil s\rceil\},\qquad
R_\mu=\nu^{T_\mu-1}\frac y\mu.
\]
The convention at exact equality is included in this formula.

**2. Almost-sure phase limit.** On the specified scale \(a\mu_j^{-\alpha}=\nu^{-(j+\theta)}\), so
\[
\frac y{\mu_j}=\nu^{-(j+\theta)}u^\gamma+\nu(1-u),\quad
s_j=j+\theta-V+\frac1\lambda\log\left(1+
\frac{\nu^{j+\theta+1}(1-u)}{u^\gamma}\right).
\]
For every fixed \(u>0\), the final term tends to zero. When \(V-\theta\notin\mathbb Z\), the ceiling therefore eventually stabilizes, and
\[
T_{\mu_j}-j=1+\lceil\theta-V\rceil
=1-\lfloor V-\theta\rfloor.
\]
Substitution into the exact return-coordinate formula gives \(R_{\mu_j}\to\nu^{\{V-\theta\}}\). The excluded set has zero uniform probability. Eventual almost-sure equality of the integer variables bounds their total-variation distance by their mismatch probability, which tends to zero.

**3. The complete limiting law.** The uniform distribution of \(U\) gives
\[
\Pr(V\ge v)=\min\left\{1,\frac{\nu^{v/\gamma}}{1-\nu}\right\},
\qquad
V\overset{d}=v_0+E,\quad \Pr(E>t)=e^{-\rho t}\quad(t\ge0).
\]
Since \(J_\theta\ge h\) precisely when \(V<\theta+2-h\) outside a null set, the displayed tail formula follows. For \(h\le h_0\), the full interval \([\theta+1-h,\theta+2-h)\) lies above \(v_0\), and hence
\[
\Pr(J_\theta=h)
=e^{-\rho(\theta+1-h-v_0)}(1-e^{-\rho}).
\]
Successive masses differ by the factor \(e^{-\rho}=\nu^{1/\gamma}\), proving the geometric law when conditioned on \(J_\theta\le h_0\).

On \(J_\theta=h\), set \(t=V-\theta-(1-h)\in(0,1)\). The limiting return coordinate is \(r=\nu^t\). Change of variables from the exponential density of \(V\) gives the **joint**, not merely marginal, density
\[
\Pr(J_\theta=h,\ Q_\theta\in dr)
=\frac{e^{-\rho(\theta+1-h-v_0)}}\gamma
r^{1/\gamma-1}\,dr,
\qquad \nu<r<1,\quad h\le h_0.
\]
Its integral is the mass above, and division by that mass yields the claimed density \(g\), independent of \(h\). This proves the conditional independence statement.

**4. Finite-scale correction.** Fix an integer \(h\) with \(0<b_h<1-\nu\). For sufficiently large \(j\), the exact return formula makes \(\{T_{\mu_j}-j\ge h\}\) equivalent, up to a null equality set, to
\[
U^\gamma+\varepsilon_j(1-U)>b_h^\gamma,
\qquad\varepsilon_j=\nu^{j+\theta+1}.
\]
The left side is strictly increasing for \(0\le U\le1-\nu\) once \(j\) is large. Its unique interior threshold \(u_j\) has the implicit-function expansion
\[
u_j=b_h-\frac{(1-b_h)b_h^{1-\gamma}}\gamma\varepsilon_j
+O(\varepsilon_j^2).
\]
Because \(U\) is uniform on \((0,1-\nu)\), the probability equals \(1-u_j/(1-\nu)\). This proves the correction including its sign and scope.

**5. Mean return time.** For fixed \(\theta\), the quantity \(T_{\mu_j}-j\) is uniformly bounded above; this follows from \(y/\mu_j\le\nu^{-(j+\theta)}(1-\nu)^\gamma+\nu\). If \(T_{\mu_j}\le j-k\), its return iterate gives \(y/\mu_j\le\nu^{-(j-k-1)}\), hence \(U^\gamma\le\nu^{k+\theta+1}\). Thus
\[
\Pr(j-T_{\mu_j}\ge k)
\le\min\left\{1,\frac{\nu^{(k+\theta+1)/\gamma}}{1-\nu}\right\}.
\]
The geometric bound proves uniform integrability and convergence of expectations. More explicitly, with \(m=\lceil v_0-\theta\rceil\) and \(t=m-v_0+\theta\in[0,1)\), the exponential law yields
\[
\mathbb E T_{\mu_j}
=j+2-m-\frac{e^{-\rho t}}{1-e^{-\rho}}+o(1).
\]
For the displayed square-root example this specializes to \(\mathbb E T_{\mu_j}=j+1/3+o(1)\).

## Verification

The standalone `verification.py` uses exact rational arithmetic for first returns of a square-root specialization with rational square initial offsets. It compares direct iterates with the centered limiting integers and numerically evaluated return coordinates at three shrinking parameters, checks exact normalization and expectation of the limiting geometric masses, and uses floating-point bisection on a finite-parameter tail threshold to test the first correction. Executing `python3 verification.py` produced `EXACT_GRAZING_RETURN_CHECK_OK`. The analytic argument above supplies all infinite-limit proofs; neither floating-point comparisons nor finite samples establish those limits.

## Relationship to prior work

Lima and Perdigão introduced the rational-degree piecewise map and its natural interval \(I_\mu\), established return to that interval, and studied bifurcation regimes; their Proposition 2, Lemma 4, and equations (11)–(13) provide pointwise return-length constraints. These are the starting observations, not claimed as new. The result here classifies the **joint phase-resolved distribution** of return duration and reinjection location under a specified natural Lebesgue ensemble, shows exact long-excursion independence and a geometric/power-law kernel, and obtains a controlled finite-parameter correction. Their pointwise return-length calculations are compatible with, but do not explicitly state, this full joint statistical conclusion.

Lima and Perdigão's companion 2024 preprint derives higher-order grazing discontinuity maps for hybrid flows, a different object. Earlier work by Halse, Homer, and di Bernardo investigates period-adding and period windows in other one-dimensional piecewise-smooth normal forms. General return-time results for mixing systems and shrinking targets (Haydn and Vaienti) concern invariant-measure recurrences rather than the specified parameter-dependent, Lebesgue-initialized first-excursion kernel. No claim is made that these general theories are disproved or superseded.

## Limitations

The probability law is for uniformly chosen **initial conditions** in the shrinking section, not the stationary law of an induced return map; the latter is not determined here. The all-phase result is asymptotic as \(\mu\to0^+\); the displayed first correction requires a fixed threshold strictly inside the nontrivial tail range. The theorem does not classify periodic or chaotic invariant sets or their physical measures. Search and source inspection cannot establish absolute publication priority; relevant older literature on grazing or overshoot statistics may contain equivalent formulations.

## References

1. Maurício Firmino Silva Lima and Tiago Rodrigo Perdigão, *One-dimensional Piecewise Smooth Rational Degree Maps*, arXiv:2407.02782v1 (first posted 2024-07-03), https://arxiv.org/abs/2407.02782.
2. Maurício Firmino Silva Lima and Tiago Rodrigo Perdigão, *Zero Time Discontinuity Mapping and Poincaré Discontinuity Mapping in a neighbourhood of a regular grazing point of order 4 in impacting hybrid systems*, arXiv:2407.02434v1 (2024), https://arxiv.org/abs/2407.02434.
3. C. K. Halse, M. E. Homer, and M. di Bernardo, *C-bifurcations and period-adding in one-dimensional piecewise smooth maps*, Chaos, Solitons & Fractals 18 (2003), 953–976, doi:10.1016/S0960-0779(03)00066-3.
4. N. Haydn and S. Vaienti, *The limiting distribution and error terms for return times of dynamical systems*, Discrete and Continuous Dynamical Systems 10 (2004), 589–616, doi:10.3934/dcds.2004.10.589.
