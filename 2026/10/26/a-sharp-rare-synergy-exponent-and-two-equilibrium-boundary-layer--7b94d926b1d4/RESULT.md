# A sharp rare-synergy exponent and two equilibrium boundary layers in nonlinear public-goods dynamics

## Finding

Consider the well-mixed stochastic synergy/discounting public-goods evolutionary model of Zhu et al. [1], with group size \(G=n+1\), nonlinear coefficient \(0<\delta<1\), positive selection strength \(s>0\), and benefit multiplier \(r=\kappa G\), where \(\kappa>1\) is fixed. Suppose a group is synergistic with probability \(p_n=cL^{-n}\), where \(c>0\) and \(L>1\) are fixed, and otherwise has discounted benefits. The probability is understood for all sufficiently large integers \(n\) for which \(0<p_n<1\). Define

\[
F_n(x)=\kappa\left[c\left(\frac{1+\delta x}{L}\right)^n+\left(1-cL^{-n}\right)(1-\delta x)^n\right]-1,
\quad
\dot x=x(1-x)\tanh\!\left(\frac{sF_n(x)}2\right),\quad 0\le x\le1.
\]

There is, for every sufficiently large \(n\), a unique attracting interior equilibrium \(a_n\), and

\[
n a_n\longrightarrow\frac{\log\kappa}{\delta}.
\]

There is a sharp **rarity-exponent transition** at \(L=1+\delta\):

1. If \(1<L<1+\delta\), exactly one further interior equilibrium \(b_n\) exists. It is repelling, full cooperation \(x=1\) is attracting, and the two basins are \((0,b_n)\to a_n\) and \((b_n,1]\to1\). With \(x_L=(L-1)/\delta\in(0,1)\),
\[
 b_n=x_L-\frac{L\log(\kappa c)}{\delta n}+o(n^{-1}).
\]
In particular, \(p_n\to0\) exponentially yet the all-cooperation basin has limiting width \(1-x_L>0\).

2. If \(L>1+\delta\), there is no further interior equilibrium; \(x=1\) is repelling and every initial \(0<x<1\) tends to \(a_n\).

3. If \(L=1+\delta\), the boundary is resolved by the amplitude \(c\). When \(c<\kappa^{-1}\), only \(a_n\) exists and full cooperation is repelling. When \(c>\kappa^{-1}\), the second equilibrium exists, full cooperation is attracting, and
\[
 n(1-b_n)\longrightarrow\frac{1+\delta}{\delta}\log(\kappa c).
\]
At the **exact critical amplitude** \(c=\kappa^{-1}\), there are still two interior equilibria for every sufficiently large \(n\), and their upper separatrix has a much thinner layer:
\[
 \boxed{\displaystyle\lim_{n\to\infty}\frac{n(1-b_n)}{(1-\delta)^n}
 =\frac{\kappa(1+\delta)}{\delta}.}
\]

All stated interior equilibria are simple. In cases with two interior equilibria, \(a_n\) and full cooperation are attracting while \(b_n\) separates their basins. The all-defection equilibrium \(x=0\) is always repelling. These are statements about deterministic well-mixed population-frequency dynamics, not finite-population fixation.

For illustration, choose \(\delta=2/5\), \(\kappa=3/2\), \(L=6/5\), \(c=1\), and \(n=96\) (groups of \(97\) people). Even though the synergy probability is \((5/6)^{96}\approx2.5038043\times10^{-8}\), exact rational sign evaluations place the two interior roots at
\[
 0.01053<a_{96}<0.01055,\qquad0.48735<b_{96}<0.48736.
\]
Thus more than half the initial-frequency interval remains in the basin of full cooperation despite extraordinarily rare synergistic groups.

## Assumptions and scope

* The population is infinite and well mixed, with two strategies and homogeneous payoff parameters. Each sampled group is synergistic with probability \(p_n\), independently of the focal strategy, with nonlinear contribution factors \(1+\delta\) and \(1-\delta\). Selection strength \(s>0\) is fixed (the stationary points do not depend on its magnitude).
* \(\kappa>1\), \(0<\delta<1\), \(c>0\), and \(L>1\) are constants independent of \(n\). The group-size-dependent benefit multiplier is exactly \(r=(n+1)\kappa\). There is no claim for fixed \(r\) as \(n\to\infty\).
* All conclusions are eventual in integer \(n\), and no universal finite cutoff is asserted. A basin statement assumes an initial fraction strictly between neighboring equilibria. At an equilibrium the trajectory remains there.
* All logarithms are natural; \(o(n^{-1})\) holds for fixed parameters of the specified regime. At critical amplitude the upper-equilibrium distance is exponentially smaller than \(n^{-1}\).

## Proof

**Model reduction.** The expected payoff difference of the stochastic nonlinear public-goods model is [1, Eq. (6) and Supplementary Eq. (S2)]
\[
 \Pi_C-\Pi_D=\frac rG\{p(1+\delta x)^{G-1}+(1-p)(1-\delta x)^{G-1}\}-1.
\]
Substituting \(G=n+1\), \(r/G=\kappa\), and \(p=p_n=cL^{-n}\) gives exactly \(F_n\). The dynamics is forward invariant on \([0,1]\). Since \(\tanh\) is strictly increasing and vanishes only at zero, nonboundary equilibria are exactly the zeros of \(F_n\), with the same directional signs. In particular \(F_n(0)=\kappa-1>0\), so \(0\) is repelling.

**At most two interior zeros, and one low-frequency zero.** For integer \(n\ge2\),
\[
 F_n''(x)=\kappa n(n-1)\delta^2\left[p_n(1+\delta x)^{n-2}+(1-p_n)(1-\delta x)^{n-2}\right]>0
\]
for every \(x\in[0,1]\). The function has at most two zeros, and its derivative is strictly increasing. Set \(x_*=\min\{(L-1)/\delta,1\}\) and choose any fixed \(y\in(0,x_*)\). Then \((1+\delta y)/L<1\) and \(0<1-\delta y<1\), so \(F_n(y)\to-1\). Hence \(F_n\) has exactly one low zero \(a_n\in(0,y)\) for large \(n\), at which its derivative is negative. It can have exactly one second, larger interior zero if and only if \(F_n(1)>0\). Indeed, when \(F_n(1)<0\), the strict convexity and endpoint signs rule out a second root; when \(F_n(1)>0\), the intermediate value theorem gives one between \(y\) and \(1\), where the derivative is positive. Equality \(F_n(1)=0\) is excluded in the eventual parameter regimes below.

**Full-cooperation threshold.** The endpoint is
\[
 F_n(1)=\kappa\left[c\left(\frac{1+\delta}{L}\right)^n+(1-cL^{-n})(1-\delta)^n\right]-1.
\]
For \(L<1+\delta\) this tends to \(+\infty\); for \(L>1+\delta\) it tends to \(-1\). At \(L=1+\delta\) its limit is \(\kappa c-1\). At equality \(c=\kappa^{-1}\) the exact expression simplifies to \(F_n(1)=\kappa(1-p_n)(1-\delta)^n>0\). Thus the asserted exact counts and stability types follow. In general the exact finite-size endpoint threshold, whenever its numerator is positive, is the already algebraically available
\[
 p_n^{\rm crit}=\frac{\kappa^{-1}-(1-\delta)^n}{(1+\delta)^n-(1-\delta)^n};
\]
this formula is included for comparison, not claimed as a new finite-size criterion.

**Low boundary layer.** Fix \(u\ge0\). Uniformly on compact \(u\)-intervals,
\[
 F_n(u/n)\longrightarrow\kappa e^{-\delta u}-1,
\]
because the synergistic contribution is bounded by \(cL^{-n}e^{\delta u}\) and vanishes, while the discounted contribution converges to \(e^{-\delta u}\). The limiting function is strictly decreasing with its unique zero at \(u=\log(\kappa)/\delta>0\). Bracketing this zero and using the uniqueness of \(a_n\) gives \(na_n\to\log(\kappa)/\delta\).

**Macroscopic upper separatrix when \(1<L<1+\delta\).** Write \(x_L=(L-1)/\delta\in(0,1)\). For each fixed \(z\in\mathbb R\),
\[
 F_n(x_L+z/n)\longrightarrow\kappa c e^{\delta z/L}-1,
\]
because \((1+\delta(x_L+z/n))/L=1+\delta z/(Ln)\), while \((1-\delta(x_L+z/n))^n\to0\) since \(1-\delta x_L=2-L\in(0,1)\). The limiting function has a unique strict sign crossing at \(z_0=-(L/\delta)\log(\kappa c)\). Bracketing by \(z_0\pm\varepsilon\) identifies the upper root and proves \(n(b_n-x_L)\to z_0\). In particular the all-cooperation basin width \(1-b_n\to1-x_L>0\).

**Critical upper layers.** Let \(L=1+\delta\). For fixed \(z\ge0\),
\[
 F_n(1-z/n)\longrightarrow\kappa c\exp\left(-\frac{\delta z}{1+\delta}\right)-1.
\]
For \(c>\kappa^{-1}\), this crosses zero at a positive \(z_0=(1+\delta)\log(\kappa c)/\delta\); bracketing yields \(n(1-b_n)\to z_0\).

At exact amplitude \(c=\kappa^{-1}\), put \(y_n(C)=C(1-\delta)^n/n\) for a fixed \(C>0\). Expanding the two terms using \( (1+\delta(1-y))/(1+\delta)=1-\delta y/(1+\delta)\) gives
\[
 \frac{F_n(1-y_n(C))}{(1-\delta)^n}
 =\kappa-\frac{\delta C}{1+\delta}+o(1).
\]
Indeed the first term is \((1-\delta y/(1+\delta))^n=1-\delta n y/(1+\delta)+O((ny)^2)\) and the second is \(\kappa(1-p_n)(1-\delta+\delta y)^n\sim\kappa(1-\delta)^n\). For \(C\) below, respectively above, \(C_*=\kappa(1+\delta)/\delta\), the displayed normalized value is positive, respectively negative. For large \(n\), both test points lie beyond the low root, so they bracket the unique upper root. Letting the constants approach \(C_*\) proves \(n(1-b_n)/(1-\delta)^n\to C_*\).

**Stability and basins.** At an interior simple zero \(z\), the ODE derivative is \(z(1-z)sF_n'(z)/2\), hence \(a_n\) is attracting and \(b_n\), when present, repelling. At \(x=1\) the linearized derivative equals \(-\tanh(sF_n(1)/2)\), giving the indicated attracting or repelling behavior. The strict sign pattern of \(F_n\) in each interval proves all basin statements by one-dimensional uniqueness and monotone convergence. The exceptional equilibrium points themselves remain fixed. This completes the proof.

## Verification

The standalone standard-library script `verify.py` evaluates \(F_n\) and the endpoint threshold in exact rational arithmetic, checks strict-convexity witnesses, and uses high-precision decimal bisection only to illustrate the asymptotic locations. It tests subcritical, critical-above, critical-below, critical-equality, and supercritical rarity bases for several group sizes. Its numerical root findings are not used to prove the general theorem.

For the illustrated \(n=96\) parameters, the four endpoint inequalities establishing the two rational root brackets are evaluated **exactly**. The source equations, convexity inequality, and asymptotic bracketing arguments above constitute the proof for all sufficiently large \(n\).

## Relationship to prior work

Zhu et al. [1] supply the stochastic synergy/discounting game, the finite-group payoff difference, and a finite-parameter classification of possible stable states. In particular, their endpoint threshold and the existence of bistability at fixed parameters are not new. The finding here treats the linked limit of growing group size and **exponentially vanishing synergy probability** and derives an exact rarity-rate transition, macroscopic and microscopic separatrix laws, and an exponentially thinner critical-amplitude crossover. Those claims require additional uniform limiting and boundary-layer arguments; they are not stated in [1] or its accessible supplement.

Peña [2] studies how **randomly distributed group sizes** change cooperation for nonlinear public goods, not a group-size-indexed stochastic mixture whose synergy probability decays exponentially. Li, Wu, and Wang [3] study regular-network weak-selection fixation with purely synergistic or discounted interactions rather than the current well-mixed convex mixture and its singular rarity regime. Peña and Nöldeke [4] analyze changes in stable and unstable cooperative frequencies with group size; importantly, their Section 4 also extends the discussion to size-dependent payoffs, particularly benefit-sharing gains of the form \(d_k^{(n)}=\Delta u_k/n-c\). Their results neither specialize to a randomly sampled synergy-versus-discount mixture with exponentially size-dependent synergy probability nor supply the present critical rarity exponent and the two distinct upper-boundary scales. Llabrés et al. [5] examine deterministic nonlinear games of mixed interaction order on hypergraphs, not this probability-mixture scaling. These are comparisons of objects and hypotheses, not claims of exhaustive publication priority.

## Limitations

The conclusion is for the deterministic infinite-population mean-field approximation with homogeneous, well-mixed groups, independent fixed synergistic/discounted group type, one nonlinear coefficient \(\delta\), and a benefit multiplier growing linearly with group size. It does not assert that finite stochastic populations fixate according to these basins, that heterogeneous networks follow the same law, or that a fixed benefit multiplier has these asymptotics. All parameters are kept fixed apart from \(G=n+1\), \(r=\kappa G\), and \(p_n=cL^{-n}\). No generalization to arbitrary synergy-probability sequences, dependence across groups, or finite-\(n\) quantitative error bound is proved. Publication priority beyond the sources inspected remains unverified.

## References

[1] Wenqiang Zhu, Xin Wang, Chaoqian Wang, Longzhao Liu, Jiaxin Hu, Zhiming Zheng, Shaoting Tang, Hongwei Zheng, and Jin Dong, *Evolutionary dynamics in stochastic nonlinear public goods games*, arXiv:2408.02042, first submitted 2024-08-04; *Communications Physics* 7 (2024), DOI: 10.1038/s42005-024-01865-6. Original manuscript and supplementary mathematical analysis: https://arxiv.org/abs/2408.02042.

[2] Jorge Peña, *Group-size diversity in public goods games*, *Evolution* 66 (2012), 623–636; published online 2011-11-04; DOI: 10.1111/j.1558-5646.2011.01504.x.

[3] Aming Li, Bin Wu, and Long Wang, *Cooperation with both synergistic and local interactions can be worse than each alone*, *Scientific Reports* 4 (2014), 5536; DOI: 10.1038/srep05536.

[4] Jorge Peña and Georg Nöldeke, *Group size effects in social evolution*, *Journal of Theoretical Biology* 457 (2018), 211–220; DOI: 10.1016/j.jtbi.2018.08.004. Full author-hosted open-access primary PDF inspected, including Sections 3–4 and Propositions 1–6; https://jorgeapenas.github.io/assets/pdf/Pena2018.pdf.

[5] Jaume Llabrés, Onkar Sadekar, Federico Malizia, and Federico Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228, first submitted 2026-04-08. https://arxiv.org/abs/2604.07228.
