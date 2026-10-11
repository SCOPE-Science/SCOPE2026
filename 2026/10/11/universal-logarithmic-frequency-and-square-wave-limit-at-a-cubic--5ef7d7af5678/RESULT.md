# Universal logarithmic frequency and square-wave limit at a cubic global center

## Finding

**Theorem (one high-energy law).** For arbitrary \(a\in\mathbb R\) and \(\kappa>0\) consider the cubic differential system
\[
\dot x=y,\qquad \dot y=-x+(a-\kappa x)y^2.
\]
Define \(g(x)=e^{\kappa x^2/2-ax}\), \(q(x)=\int_0^x g(u)\,du\), and \(V(x)=\int_0^x u g(u)^2\,du\). Every energy \(E>0\) determines a periodic orbit of
\[
H(x,y)=\tfrac12 g(x)^2y^2+V(x)=E,
\]
with positive and negative turning coordinates \(x_+(E)>0>x_-(E)\). Let \(T(E)\) be its **minimal period in the time appearing in the displayed vector field**. Then
\[
\lim_{E\to\infty}\sqrt{\log E}\,T(E)=2\pi,
\qquad
x_\pm(E)=\frac a\kappa\pm\sqrt{\frac{\log E}\kappa}+o(1).
\]
For the trajectory starting at \((x_+(E),0)\), put \(Q_E=\sqrt{2E/\log E}\), \(R_E=\sqrt{\log E/\kappa}\). At normalized phase \(s=t/T(E)\in[0,1]\), the canonically transformed position and momentum satisfy
\[
\sup_{0\le s\le1}\left|\frac{q(x_E(sT(E)))}{Q_E}-\cos(2\pi s)\right|\to0,
\quad
\sup_{0\le s\le1}\left|\frac{g(x_E(sT(E)))y_E(sT(E))}{\sqrt{2E}}+\sin(2\pi s)\right|\to0.
\]
The original coordinate instead develops a **square-wave time profile**:
\[
\frac{x_E(sT(E))}{R_E}\to\operatorname{sgn}(\cos(2\pi s))
\quad\text{in }L^p([0,1])\text{ for every finite }1\le p<\infty.
\]
In particular, for every bounded continuous \(f:\mathbb R\to\mathbb R\),
\[
\lim_{E\to\infty}\frac1{T(E)}\int_0^{T(E)}
 f\left(\frac{x_E(t)}{R_E}\right)\,dt
=\frac{f(-1)+f(1)}2.
\]

## Assumptions and scope

The constants \(a\) and \(\kappa\) are fixed as \(E\to\infty\); \(a\) may have either sign, whereas \(\kappa>0\). The energy \(E\) is measured relative to the minimum \(H(0,0)=0\). The logarithmic expressions and normalizers are used only for \(E>1\). The convergence in the original position is not uniform across the two jump phases \(s=1/4\) and \(s=3/4\). Every displayed time is **original physical time**, without reparametrizing the vector field.

## Proof

**1. Exact global conjugacy.** Since \(g'(x)=(\kappa x-a)g(x)\), differentiation along solutions gives
\[
\dot H=g(x)^2y\bigl(\dot y+(\kappa x-a)y^2+x\bigr)=0.
\]
The function \(g\) is positive and grows at both infinities, so \(q:\mathbb R\to\mathbb R\) is an increasing analytic diffeomorphism. Put \(p=g(x)y\) and \(W(q)=V(x(q))\). Then the unchanged-time equations are exactly
\[
\dot q=p,\qquad \dot p=-W'(q),\qquad W'(q)=x(q)g(x(q)).
\]
Here \(W(0)=0\), \(W'(q)\) has the sign of \(q\), and \(W(q)\to\infty\) as \(q\to\pm\infty\). Therefore every energy \(E>0\) is a simple closed oval enclosing the origin, with exactly two turning points. Its minimal time period is the well-defined quadrature
\[
T(E)=\sqrt2\int_{x_-(E)}^{x_+(E)}\frac{g(x)}{\sqrt{E-V(x)}}\,dx
=\sqrt2\int_{q_-(E)}^{q_+(E)}\frac{dq}{\sqrt{E-W(q)}}.
\]
This independently proves periodicity; it does not rely on the cited qualitative classification.

**2. Gaussian-tail asymptotics.** Put \(b(x)=\kappa x-a\). Applying l'Hôpital's rule separately at the two ends to \(q(x)\) and \(V(x)\) yields
\[
q(x)\sim\frac{g(x)}{b(x)},\qquad
V(x)\sim\frac{xg(x)^2}{2b(x)}\sim\frac{g(x)^2}{2\kappa},
\qquad x\to\pm\infty.
\]
The asymptotic expression for \(q\) is negative at the negative end, as required. It follows that
\[
\log|q(x)|=\tfrac12\kappa x^2-ax-\log|\kappa x-a|+o(1)
\]
and, writing \(x=x(q)\),
\[
\frac{W(q)}{q^2\log|q|}\to1,
\qquad
\frac{W'(q)}{2q\log|q|}\to1\quad(q\to\pm\infty).
\]
In addition, exact differentiation gives
\[
W''(q)=1+x(q)(\kappa x(q)-a).
\]
Thus for some parameter-dependent constant \(C>0\),
\[
|W''(q)|\le C\bigl(1+\log(2+|q|)\bigr)\quad(q\in\mathbb R).
\]
At \(V(x_\pm(E))=E\), the tail formula gives
\[
\kappa\bigl(x_\pm(E)-a/\kappa\bigr)^2
=\log E+\log(2\kappa)+a^2/\kappa+o(1).
\]
Taking the appropriate square-root signs proves the asserted turning-point expansions and \(x_+(E)+x_-(E)\to 2a/\kappa\).

**3. A uniform harmonic limit in unchanged physical time.** Define
\[
Q_E=\sqrt{2E/\log E},\qquad
\tau=\sqrt{\log E}\,t,
\qquad z_E(\tau)=\frac{q(x_E(t))}{Q_E}.
\]
Writing a prime for differentiation in \(\tau\), the exact second-order equation becomes
\[
z_E''=-F_E(z_E),\qquad
F_E(z)=\frac{W'(Q_Ez)}{Q_E\log E}.
\]
For every fixed \(M<\infty\), \(F_E(z)\to z\) uniformly for \(|z|\le M\). Indeed, on \(\eta\le|z|\le M\), this follows from \(W'(q)\sim2q\log|q|\) and \(2\log Q_E/\log E\to1\); on \(|z|\le\eta\), the preceding global \(W''\)-bound and \(W'(0)=0\) yield \(|F_E(z)|\le C_M\eta\) for all sufficiently large \(E\). Moreover, \(F_E'\) is uniformly bounded on every compact set by the same bound for \(W''\). The turning-point normalization follows explicitly from \(E=W(q_+(E))\), \(W(q)\sim q^2\log|q|\), and \(\log q_+(E)/\log E\to1/2\): hence \(z_E(0)=q(x_+(E))/Q_E\to1\), while \(z_E'(0)=0\). Standard Grönwall continuous dependence applied to this **explicit** family of equations therefore gives
\[
(z_E(\tau),z_E'(\tau))\to(\cos\tau,-\sin\tau)
\]
uniformly on every fixed compact \(\tau\)-interval. The conserved scaled energy is \((z_E')^2+W(Q_Ez_E)/E=1\), so both turning values tend to \(\pm1\). Because \(W\) has exactly one minimum and is strictly monotone on either side, each cycle traverses its turning points in order; the first right-turn return occurs near \(\tau=2\pi\) (alternatively, follow the two transverse crossings \(z_E=0\), near \(\pi/2\) and \(3\pi/2\), then the unique next turning point). Hence \(\sqrt{\log E}T(E)\to2\pi\), and on \(s=t/T(E)\in[0,1]\),
\[
\frac{q(x_E(sT(E)))}{Q_E}\to\cos(2\pi s),\qquad
\frac{p_E(sT(E))}{\sqrt{2E}}=z_E'(\sqrt{\log E}T(E)s)\to-\sin(2\pi s)
\]
uniformly. The second equation uses the identity \(Q_E\sqrt{\log E}=\sqrt{2E}\).

**4. Singular inverse transformation and occupation.** The Gaussian-tail estimate for \(q(x)\) implies that whenever \(z_E\to z\ne0\) with \(z_E\) bounded, then
\[
\frac{x(Q_Ez_E)}{R_E}\to\operatorname{sgn}z,
\qquad R_E=\sqrt{\log E/\kappa}.
\]
The turning-point estimates give the uniform bound \(\sup_t |x_E(t)|/R_E\le1+o(1)\). For every \(s\in[0,1]\) except \(1/4,3/4\), the uniform harmonic limit has nonzero cosine; hence the normalized original position converges pointwise to its indicated sign. Dominated convergence proves every finite \(L^p\) limit and, applied to any bounded continuous test function, proves the two-atom occupation law. No behavior at the two jump phases is asserted. This completes the proof.

## Verification

The checker `checker.py` tests the derived derivative and energy-balance cancellations using exact integer arithmetic on sampled inputs and uses a high-accuracy composite Simpson quadrature for \(a=0\), \(\kappa=1\), when \(V(x)=(e^{x^2}-1)/2\). The numerical sequence supports the limit \(T(E)\sqrt{\log E}\to2\pi\) but is not used as an infinite proof. All estimates for arbitrary parameters and for the waveform follow analytically from Steps 1–4.

## Relationship to prior work

Appis and Llibre, *Global centers of a family of cubic systems* (2024), Theorem 4(a), include the present family through \(a_1=a_2=a_4=a_5=a_7=0\), \(a_3=a\), \(a_6=-\kappa<0\), and prove existence of the global center. Their full open-access article concerns center classification and compactified phase portraits, not the quantitative high-energy physical period, canonical harmonic limit, or singular time-occupation law. General published period-function work for separable Hamiltonians studies critical periods, monotonicity and boundary behavior; it does not, on the material inspected, supply this family-specific package or the original-coordinate square-wave conclusion. The new finding is not an additional global-center classification.

## Limitations

This concerns only \(\kappa>0\) with fixed finite \(a\); no simultaneous singular parameter limits, finite-energy monotonicity theorem, rate of convergence, uniform original-coordinate waveform, or fluctuation law at the jump phases is claimed. The proof reconstructs a known canonical transformation; publication priority for all conceivable equivalent formulations is not conclusively established. Independent audit has not been performed.

## References

1. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, Aequationes Mathematicae 98 (2024), 1373–1389, DOI: `10.1007/s00010-024-01051-7`; openly available at `https://link.springer.com/article/10.1007/s00010-024-01051-7` (first online 2024-04-05).
2. J. Villadelprat and X. Zhang, *The Period Function of Hamiltonian Systems with Separable Variables*, Journal of Dynamics and Differential Equations 32 (2020), 741–767, DOI: `10.1007/s10884-019-09759-w`.
3. C. A. Buzzi, Y. R. Carvalho and A. Gasull, *The local period function for Hamiltonian systems with applications*, Journal of Differential Equations 280 (2021), 590–617, arXiv:`2008.02316`, DOI: `10.1016/j.jde.2021.01.033`.
