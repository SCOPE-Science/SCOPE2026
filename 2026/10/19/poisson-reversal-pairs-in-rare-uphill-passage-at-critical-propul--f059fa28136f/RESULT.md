# Poisson reversal pairs in rare uphill passage at critical propulsion balance

## Finding

Consider a thermal one-dimensional run-and-tumble particle on the real line, with a constant adverse load whose magnitude approaches the propulsion speed in a square-root thermal window. Conditional on its eventually reaching an uphill point, its number of propulsion reversals converges to twice a Poisson variable, while its first-passage time, multiplied by the square root of thermal diffusivity, converges to a deterministic constant.

Precisely, for fixed \(a,b,r>0\) and \(\xi\in\mathbb R\), put
\[
\varepsilon=\sqrt{rD},\qquad
k_\xi=\frac{\sqrt{\xi^2+4}-\xi}{2},\qquad
h_\xi=\sqrt{\xi^2+4},\qquad
\mu_\xi=\frac{ar}{2bk_\xi h_\xi}.
\]
As \(D\downarrow0\), the joint conditional transform of the first-passage time \(\tau_a\) and the number \(N_a\) of direction reversals before passage satisfies, for every \(u\ge0\) and \(0\le z\le1\),
\[
\lim_{D\downarrow0}
\mathbb E\!\left[z^{N_a}e^{-u\sqrt{rD}\,\tau_a}\mid\tau_a<\infty\right]
=\exp\!\left(-\frac{au}{h_\xi}+\mu_\xi(z^2-1)\right).
\]
Thus
\[
(\sqrt{rD}\,\tau_a,N_a)\mid\{\tau_a<\infty\}
\Longrightarrow\left(\frac{a}{h_\xi},2P_\xi\right),
\qquad P_\xi\sim\operatorname{Poisson}(\mu_\xi).
\]
At exact force–propulsion balance \(\xi=0\), the limiting mean of \(P_0\) is \(ar/(4b)\), and the scaled passage time is \(a/2\). In particular, asymptotically no odd number of reversals contributes to successful uphill passage, despite an order-one nonzero chance of two or more reversals under this conditioning.

## Assumptions and scope

Let \(W_t\) be standard Brownian motion and \(S_t\in\{+1,-1\}\) an independent continuous-time Markov chain reversing sign at rate \(r\). For each sufficiently small \(D>0\), define the process
\[
Y_0=0,\quad S_0=+1,\qquad
\mathrm dY_t=(bS_t-b+\xi\sqrt{rD})\,\mathrm dt+\sqrt{2D}\,\mathrm dW_t.
\]
The target is the single uphill level \(a>0\); set \(\tau_a=\inf\{t\ge0:Y_t=a\}\), and \(N_a=\#\{t\in(0,\tau_a]:S_t\ne S_{t-}\}\) on \(\{\tau_a<\infty\}\). The drift in the plus orientation is \(\delta=\xi\sqrt{rD}\), and in the minus orientation it is \(\delta-2b\). Assume \(D\) small enough that \(\delta<b\), ensuring strictly negative long-term drift and a nontrivial eventual-hit event. The target is on the entire real line: there is **no second boundary, no reset, and no full double-well dynamics**. The potential's constant-slope segment motivates this local model but is not asserted to be equivalent to a complete bistable escape problem.

## Proof

**1. Boundary-value transform.** For \(y<a\), let
\[
F_\pm(y;z,s)=\mathbb E_{y,\pm}\left[z^{N_a}e^{-s\tau_a};\,\tau_a<\infty\right]
\qquad(0\le z\le1,\ s\ge0).
\]
The backward generator, weighting each sign reversal by \(z\), gives
\[
D F_+''+\delta F_+'-(r+s)F_++rzF_-=0,
\quad
D F_-''+(\delta-2b)F_-'-(r+s)F_-+rzF_+=0.
\]
Since \(\tau_a=0\) at the target, \(F_+(a)=F_-(a)=1\). Both transforms vanish as \(y\to-\infty\). For \(s=0,z=1\), this follows from the negative mean drift: \(Y_t/t\to\delta-b<0\) almost surely; standard exponential supermartingale barriers for the two-state generator give exponential decay of upward-hitting probability from large negative starting points. For smaller \(z\) and larger \(s\), the bounds \(0\le F_\pm(y;z,s)\le F_\pm(y;1,0)\) suffice. Bounded Dirichlet uniqueness follows by optional stopping at \(-R\) and \(a\), followed by \(R\to\infty\).

**2. Two decaying spatial modes.** An exponential mode \(e^{\kappa(y-a)}(v_+,v_-)\) exists if
\[
Q_{D,z,s}(\kappa)=
\big(D\kappa^2+\delta\kappa-r-s\big)
\big(D\kappa^2+(\delta-2b)\kappa-r-s\big)-r^2z^2=0.
\]
When \(z>0\), each diagonal quadratic has one positive zero, denoted \(\rho_+<\rho_-\) for all small \(D\); their leading orders are \(\rho_+=\Theta(D^{-1/2})\) and \(\rho_-=\Theta(D^{-1})\). The quartic is strictly negative at both \(\rho_+\) and \(\rho_-\) and positive at large positive \(\kappa\). Also \(Q(0)=(r+s)^2-r^2z^2\ge0\); in the boundary case \(z=1,s=0\), \(Q'(0)=2r(b-\delta)>0\). Hence two roots lie strictly in \((0,\rho_+)\) and \((\rho_-,\infty)\). There are exactly two strictly positive roots, since the quartic has two real negative roots when \(Q(0)>0\) by the corresponding negative-root sign argument; at \(z=1,s=0\) it has one negative and one zero root. Call the positive roots \(\kappa_s<\kappa_f\). The modes with negative or zero spatial exponent cannot satisfy decay at negative infinity.

**3. Singular-root expansions.** Set \(\varepsilon=\sqrt{rD}\) and \(s=u\varepsilon\), with \(u\ge0\) fixed. Substitute \(\kappa=(rk/\varepsilon)+c\) into the characteristic equation. The coefficient of \(\varepsilon^{-1}\) requires \(k^2+\xi k-1=0\). Its positive solution is \(k=k_\xi>0\). The next coefficient gives
\[
\kappa_s=
\frac{rk_\xi}{\varepsilon}
+\frac{u}{h_\xi}
-\frac{rz^2}{2bk_\xi h_\xi}
+O(\varepsilon)
\qquad(z\in(0,1],\ u\text{ fixed}).
\]
The coefficient \(h_\xi=2k_\xi+\xi=\sqrt{\xi^2+4}>0\) makes the implicit-root expansion nondegenerate. The fast positive root obeys \(\kappa_f=2b/D+O(D^{-1/2})\). Normalize the slow eigenvector to have plus component \(1\): its minus component is \(O(\varepsilon)\) because the first diagonal factor is \(O(\varepsilon)\). Normalize the fast eigenvector to have minus component \(1\): its plus component is \(O(D)\) because the first diagonal factor at \(\kappa_f\) is \(\Theta(D^{-1})\). All estimates are pointwise in \(u,z\), and uniform on compact positive \(z\)-intervals.

**4. Boundary matching and conditioning.** The general decaying solution is a linear combination of the two positive modes. Matching \(F_+(a)=F_-(a)=1\), the coefficient of the slow plus-normalized mode is \(1+o(1)\), and that of the fast minus-normalized mode is \(1+o(1)\). Since \(\kappa_f a\gg \kappa_s a\), the fast term is exponentially negligible at \(y=0\). Thus
\[
F_+(0;z,u\varepsilon)
=(1+o(1))\exp\left(-a\frac{rk_\xi}{\varepsilon}
-\frac{au}{h_\xi}+\frac{arz^2}{2bk_\xi h_\xi}\right).
\]
At \(z=1,u=0\), this yields the positive but vanishing hit probability
\[
\Pr_{0,+}(\tau_a<\infty)
=(1+o(1))\exp\left(-\frac{ark_\xi}{\varepsilon}+\mu_\xi\right).
\]
Dividing the former transform by the latter gives the joint transform in the finding. The case \(z=0\) follows directly from the uncoupled plus-state scalar equation: there can be no reversals, and the corresponding positive spatial root has the same slow-root expansion with its \(z^2\)-term zero. Finally, convergence of joint Laplace–probability-generating transforms and their continuity at the origin identifies the joint limit. In particular the second coordinate must be supported on even nonnegative integers, with half-count Poisson of mean \(\mu_\xi\).

## Verification

The standalone script `verify.py` forms the exact characteristic quartic, finds its positive roots, constructs its two boundary-matched eigenmodes, and compares the finite-\(D\) conditional joint transform against the limiting closed form for three values of \(\xi\) and two independent \((z,u)\) tests. It also checks the no-reversal case \(z=0\). Numerical root calculations are finite-parameter diagnostics and are **not** the infinite-limit proof; the proof is the boundary-value and root-asymptotics argument above. Reproduce with Python 3 and NumPy: `python verify.py`.

## Relationship to prior work

Singh and Aghion (2026, arXiv:2610.08029v1) study a thermal run-and-tumble process in a bistable piecewise-linear potential and establish spatial densities, relaxation, first-passage means and coarse-graining. The constant adverse force and near-balance scale here arise naturally from the model's linear-force segments, but the current full-line first-passage setting is explicitly distinct from their complete bistable geometry. Grange and Yuan (2025/2026, arXiv:2509.11308) study first passage with imposed drift and finite tumble duration **without translational Brownian noise**. Neri (2025, arXiv:2504.03441) presents general first-passage martingales and a finite-interval lattice run-and-tumble calculation. These works supply related methodology, but the examined results do not state the present square-root-noise conditional joint time-and-reversal-count limit. General Markov-modulated Brownian first-passage matrix methods may subsume the finite-\(D\) transform; novelty is asserted only for the explicit singular critical-window limit and marked reversal law, not for the backward equations themselves.

## Limitations

The limit fixes \(a,b,r,\xi\) and conditions on an exponentially rare event, so it does not characterize typical trajectories. It assumes independent Gaussian translational noise, exponential direction reversals, initial positive orientation, and the entire real line. It is not a result for arbitrary wall configurations, arbitrary initial orientation, the full bistable potential, or finite \(D\) away from the critical window. The count law is a distributional limit, not an exact finite-\(D\) Poisson identity. No independent external validation has been performed; broad Markov-additive first-passage theory remains a possible source of implicit prior coverage.

## References

1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential* (2026), arXiv:2610.08029v1, https://arxiv.org/abs/2610.08029.
2. P. Grange and L. Yuan, *First passage of a run-and-tumble particle with exponentially-distributed tumble duration in the presence of a drift* (2025/2026), arXiv:2509.11308, https://arxiv.org/abs/2509.11308.
3. I. Neri, *Martingale approach for first-passage problems of time-additive observables in Markov processes* (2025), arXiv:2504.03441, https://arxiv.org/abs/2504.03441.
4. M. Mukherjee, P. Le Doussal and N. R. Smith, *Large deviations in statistics of the local time and occupation time for a run and tumble particle* (2024), arXiv:2405.07032, https://arxiv.org/abs/2405.07032.
