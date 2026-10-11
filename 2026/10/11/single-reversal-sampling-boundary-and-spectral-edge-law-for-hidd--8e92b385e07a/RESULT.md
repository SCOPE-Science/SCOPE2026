# Single-reversal sampling boundary and spectral-edge law for hidden critical autocorrelation

## Finding

For a slowly relaxing Ornstein--Uhlenbeck mode observed together with independent stationary nuisance fluctuations having a positive mixture-of-exponentials covariance, the **sign** of the population autocorrelation's response to the critical relaxation rate has a complete, sharp two-parameter phase diagram. A reversal is possible at some observation lag if and only if the target relaxation is faster than the **slowest** nuisance relaxation rate. Every such target rate has exactly one reversal lag. The full phase boundary is strictly monotone; its short-lag behavior is governed by the nuisance's *mean* relaxation rate, whereas its large-lag logarithmic correction detects the distribution's *slowest-rate spectral edge*.

## Assumptions and scope

Fix \(A,B>0\) and let \(r=A/B\). Let \(\nu\) be a Borel probability measure on \([b,\infty)\), with \(b=\inf\operatorname{supp}\nu>0\) and finite mean \(\bar\beta=\int\beta\,\nu(d\beta)<\infty\). For each \(a>0\), let \(X^{(a)}\) be the stationary, centered Ornstein--Uhlenbeck process
\[
 dX^{(a)}_s=-aX^{(a)}_s\,ds+\sqrt A\,dW_s.
\]
Let \(Y\) be any independent, centered, second-order stationary process with the parameter-independent covariance
\[
 \operatorname{Cov}(Y_0,Y_t)=\frac B2 q(|t|),\qquad q(t)=\int_{[b,\infty)}e^{-\beta t}\,\nu(d\beta).
\]
This class includes independent finite collections of stationary OU modes, their general Gaussian spectral mixtures, and non-Gaussian processes with these second-order statistics. Put \(Z^{(a)}=X^{(a)}+Y\) and define the **population** autocorrelation \(C_a(t)=\operatorname{Cov}(Z^{(a)}_0,Z^{(a)}_t)/\operatorname{Var}(Z^{(a)}_0)\) for \(t>0\). Only \(a\) varies: \(A,B,\nu\) remain fixed. The statements concern population autocorrelation, not finite-sample estimated trends or the full nonlinear saddle-node dynamics.

**Exact phase diagram.** If \(0<a\le b\), then \(\partial_a C_a(t)<0\) for every \(t>0\). If \(a>b\), exactly one \(t_*(a)>0\) satisfies \(\partial_a C_a(t_*(a))=0\), with negative derivative below and positive derivative above this lag. The function \(t_*:(b,\infty)\to(0,\infty)\) is a strictly decreasing continuous bijection. Its inverse \(a_*(t)>b\) is likewise strictly decreasing and obeys
\[
 \lim_{t\downarrow0}a_*(t)=\infty,\quad \lim_{t\to\infty}a_*(t)=b,\quad
 a_*(t)\sim\sqrt{\frac{2(r+\bar\beta)}t}\quad(t\downarrow0).
\]

**Spectral-edge refinement.** Assume additionally that, for some \(K>0\) and \(\kappa\ge0\),
\[
 \nu([b,b+h])\sim K h^\kappa\qquad(h\downarrow0).
\]
Then
\[
 a_*(t)=b+\frac{(\kappa+1)\log t+\log\!\left(\frac{b+r}{K\Gamma(\kappa+1)}\right)+o(1)}t\qquad(t\to\infty).
\]
For \(\kappa=0\), the condition means that \(\nu\) has mass \(K\) at \(b\). For \(\kappa>0\), it allows a continuous accumulation of nuisance relaxation rates near \(b\). No assumption of a finite number of nuisance modes is used.

## Proof

**1. A one-dimensional sign equation.** Independence and the OU covariance identity yield exactly
\[
 C_a(t)=\frac{r e^{-at}+a q(t)}{r+a}.
\]
Differentiating at fixed positive lag gives
\[
 \partial_a C_a(t)=\frac{r e^{-at}}{(r+a)^2}F_a(t),
 \quad F_a(t):=\int e^{(a-\beta)t}\nu(d\beta)-1-(a+r)t.
\]
The prefactor is strictly positive, so all signs reduce to \(F_a(t)\). If \(a\le b\), the integral does not exceed \(1\), whence \(F_a(t)\le-(a+r)t<0\).

**2. Existence and uniqueness of the reversal.** Suppose \(a>b\). Since \(\bar\beta<\infty\), the one-sided derivative exists at the origin and is
\[
 F_a(0)=0,\qquad F_a'(0)=-(r+\bar\beta)<0.
\]
For every \(t>0\), differentiation under the integral is valid (exponential damping controls arbitrarily large \(\beta\)) and
\[
 F_a''(t)=\int (a-\beta)^2 e^{(a-\beta)t}\nu(d\beta)>0.
\]
The inequality is strict because \(a>b\) entails positive measure in \([b,a)\). Also, this same positive mass supplies an exponentially growing lower bound as \(t\to\infty\), so \(F_a(t)\to\infty\). Thus the strictly convex function leaves zero with negative slope and crosses zero **exactly once** at \(t_*(a)>0\); it crosses with strictly positive derivative. This proves the sign statements, without assuming Gaussianity of \(Y\).

**3. Global monotonicity of the phase boundary.** At each crossing,
\[
 \partial_a F_a(t)=t\left(\int e^{(a-\beta)t}\nu(d\beta)-1\right)=t^2(a+r)>0.
\]
Since \(\partial_t F_a(t)>0\) at the unique positive crossing, the implicit-function theorem gives
\[
 t_*'(a)=-\frac{\partial_a F_a(t_*(a))}{\partial_t F_a(t_*(a))}<0.
\]
For any fixed \(t>0\), the function \(a\mapsto F_a(t)\) is strictly convex, negative at \(a=b\), and tends to infinity with \(a\). Therefore it has exactly one zero for \(a>b\), defining \(a_*(t)\). For fixed \(t\), \(F_a(t)<0\) near \(a=b\); for fixed \(a>b\), \(F_a(t)>0\) at all sufficiently large \(t\). These facts and the strict monotonicity prove that \(t_*(a)\to\infty\) as \(a\downarrow b\), that \(t_*(a)\to0\) as \(a\to\infty\), and both equivalent limits for \(a_*(t)\).

**4. Short-lag boundary.** At the threshold put \(u=t a_*(t)\). The exact root equation is
\[
 q(t)e^u=1+u+rt.
\]
As \(t\downarrow0\), this equation and \(q(t)\to1\) force \(u\to0\): a positive or divergent limit would contradict \(e^u>1+u\). Since the finite first moment implies \(q(t)=1-\bar\beta t+o(t)\), rearrangement yields
\[
 e^u-1-u=(1-q(t))e^u+rt=(\bar\beta+r)t+o(t).
\]
The left side is \(u^2/2+o(u^2)\), hence \(u\sim\sqrt{2(\bar\beta+r)t}\) and the stated short-lag law follows.

**5. Spectral-edge boundary layer.** Write \(\widetilde\nu\) for the image of \(\nu\) under \(\beta\mapsto\beta-b\), with distribution function \(G(h)=\widetilde\nu([0,h])\). Integration by parts gives the Laplace identity
\[
 e^{bt}q(t)=\int_0^\infty e^{-th}\widetilde\nu(dh)=\int_0^\infty e^{-v}G(v/t)\,dv.
\]
If \(G(h)\sim K h^\kappa\) with \(\kappa\ge0\), the integral, split at \(v=t\delta\) and dominated by the exponential tail, gives
\[
 q(t)\sim K\Gamma(\kappa+1)\,t^{-\kappa}e^{-bt}.
\]
Substitute this in the exact boundary equation and use \(a_*(t)\to b\) from step 3:
\[
 e^{(a_*(t)-b)t}\,K\Gamma(\kappa+1)t^{-\kappa}(1+o(1))
 =1+(a_*(t)+r)t\sim(b+r)t.
\]
Taking logarithms yields the claimed logarithmic spectral-edge expansion, including its constant term. All limits keep \(A,B,\nu\) fixed.

## Verification

The derivative factorization was checked independently by exact symbolic simplification of the covariance quotient. For the three-rate example \(r=0.4\), \(\nu=0.2\delta_{0.7}+0.3\delta_{1.5}+0.5\delta_5\), numerical root finding gives \(t_*(1)\approx15.84229750\), \(t_*(2)\approx2.64403111\), and \(t_*(4)\approx0.71381265\), with sign changes on the predicted sides. This finite check supports reproducibility but is **not** used to prove the all-rate statements. The proof is analytic and contains all needed estimates; no datasets or external programs are needed.

## Relationship to prior work

Ditlevsen and Ditlevsen (2026), Section 2, derive the variance-weighted autocorrelation for a critical mode observed with an independent OU nuisance and establish eventual slowing-down signals near the bifurcation. That identity motivates this question but does not provide the necessary-and-sufficient **global reversal criterion**, the unique monotone two-parameter sampling-lag boundary for arbitrary completely monotone nuisance covariances, or its sharp logarithmic spectral-edge law. Morr, Boers, and Ashwin (2023/2024) study misleading early warnings caused by shared driving noise in coupled systems; the present observation uses **independent** components and classifies the rate derivative versus the sampling lag. Bukoski and collaborators (2018) discuss slow-mode masking in neuronal models, not the exact phase boundary or edge asymptotics. The theorem is about population covariance; no broad claim about optimal statistical estimation or nonlinear stochastic tipping is made.

## Limitations

The OU target amplitude and all nuisance second-order statistics must remain fixed as \(a\) varies. Strict positivity of the slowest nuisance relaxation rate and finite mean are essential for the stated boundary and short-lag law. The logarithmic asymptotic requires the explicitly stated regular spectral-edge mass profile; arbitrary singular edges need not obey it. Correlated target and nuisance forcing, oscillatory or sign-changing nuisance covariances, sampling uncertainty, nonlinear drift, and nonstationary parameter sweeps lie outside the theorem. The positive derivative is a *population* reversal as the damping rate increases; it does not itself establish any finite-sample hypothesis test.

## References

1. S. Ditlevsen and P. Ditlevsen, *Early Warning Signals Can Vanish or Amplify: Dimensionality in Complex Systems*, arXiv:2609.01164v1 (2026), especially Section 2, equation (4). https://arxiv.org/abs/2609.01164
2. A. Morr, N. Boers, and P. Ashwin, *Internal noise interference to warnings of tipping points in generic multi-dimensional dynamical systems*, arXiv:2311.18597v2, Section 4 and Appendix A. https://arxiv.org/abs/2311.18597
3. A. Bukoski, D. A. Steyn-Ross, A. Pickett, and M. L. Steyn-Ross, *Anesthesia modifies subthreshold critical slowing in a stochastic Hodgkin-Huxley neuron exposed to inhibitory synaptic noise*, BMC Neuroscience 19 (Supplement 2), P159 (2018). https://doi.org/10.1186/s12868-018-0452-x
