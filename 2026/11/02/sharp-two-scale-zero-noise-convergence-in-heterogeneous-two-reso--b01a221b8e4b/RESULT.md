# Sharp two-scale zero-noise convergence in heterogeneous two-resource congestion games

## Finding

A continuum congestion game with nonuniform resource impacts admits a sharp separation between the rate at which its **logit choice probabilities** approach a pure equilibrium and the rate at which its **induced deterministic partition** approaches that equilibrium.

Let characteristics \(x\in[0,1]\) have probability density \(\rho\in C^3([0,1])\), with \(\rho>0\) and \(\int_0^1\rho(x)\,dx=1\). Choose positive \(\alpha,\beta\) and strictly positive \(w_1,w_2\in C^3([0,1])\). The two resource costs at profile \(p:[0,1]\to[0,1]\), where \(p(x)\) is the share of type \(x\) using resource 1, are
\[
c_1(x;p)=x+\alpha\int_0^1w_1(y)p(y)\rho(y)\,dy,
\qquad
c_2(x;p)=\beta\int_0^1w_2(y)(1-p(y))\rho(y)\,dy.
\]
Put \(g=\alpha w_1+\beta w_2\), \(f=\rho g\), and \(W_2=\int_0^1w_2\rho\). Let \(t_0\) be the unique real solution of
\[
t_0+\int_0^{\min(1,\max(0,t_0))}f(x)\,dx=\beta W_2,
\]
and assume \(0<t_0<1\). The unique pure Nash allocation is \(p_0(x)=\mathbf1_{\{x<t_0\}}\) almost everywhere.

For any \(\sigma>0\), the unique continuum logit equilibrium \(p_\sigma\) has the form
\[
p_\sigma(x)=\frac{1}{1+\exp((x-t_\sigma)/\sigma)},\qquad
t_\sigma+\int_0^1f(x)p_\sigma(x)\,dx=\beta W_2.
\]
As \(\sigma\downarrow0\), its cutoff, the \(L^1\) and \(L^2\) choice-profile errors, and the symmetric-difference mass of the induced deterministic allocation \(A_\sigma=\{x:x<t_\sigma\}\cap[0,1]\) satisfy
\[
t_\sigma-t_0=-\frac{\pi^2 f'(t_0)}{6(1+f(t_0))}\,\sigma^2+o(\sigma^2),
\]
\[
\|p_\sigma-p_0\|_{L^1(\rho)}=2\rho(t_0)\log2\,\sigma+o(\sigma),
\]
\[
\|p_\sigma-p_0\|_{L^2(\rho)}^2=(2\log2-1)\rho(t_0)\,\sigma+o(\sigma),
\]
\[
\int_{A_\sigma\triangle A_0}\rho(x)\,dx
=\frac{\pi^2\rho(t_0)|f'(t_0)|}{6(1+f(t_0))}\,\sigma^2+o(\sigma^2).
\]
The last coefficient may vanish, whereas the two norm coefficients are strictly positive. Consequently the order-two deterministic-partition error and the order-one probabilistic-profile error represent distinct observables, not contradictory rates.

For the explicit *non-potential* game with \(\rho\equiv1\), \(\alpha=\beta=1\), \(w_1(x)=1+x\), and \(w_2(x)=1\), the nonzero cutoff coefficient is exact:
\[
t_0=\sqrt{11}-3,\qquad
 t_\sigma=t_0-\frac{\pi^2}{6\sqrt{11}}\sigma^2+o(\sigma^2).
\]
In addition, the cutoff \(t_\sigma\) is strictly decreasing for **all** \(\sigma>0\), with limits \(\sqrt{11}-3\) at zero noise and \(-1/4\) at infinite noise.

## Assumptions and scope

The population is nonatomic with characteristics distributed according to \(\rho(x)\,dx\). Individual agents cannot affect congestion by themselves. Each agent minimizes their own resource cost. Gumbel-distributed independent utility shocks with common scale \(\sigma\) induce the stated logit probabilities. Both congestion terms use their respective resource-specific nonnegative weighted masses. No idiosyncratic-cost ties have positive mass because the intrinsic cost difference is \(x\).

These claims apply to two resources, positive smooth density and impact kernels, and an interior zero-noise cutoff. For the general theorem, \(f'(t_0)\) is allowed to vanish. The explicit globally monotone example is not asserted to represent arbitrary kernels or more resources. Classification: MSC2020 \(91A14\) (potential and congestion games).

## Proof

**Equilibrium reduction and uniqueness.** Write the resource-2 contribution \(\beta\int w_2(1-p)\rho\) as \(\beta W_2-\beta\int w_2p\rho\). Hence the difference between the two costs equals \(x-t\), where
\[
t=\beta W_2-\int_0^1g(x)p(x)\rho(x)\,dx.
\]
Minimizing the two costs under independent Gumbel shocks gives \(p(x)=(1+\exp((x-t)/\sigma))^{-1}\). The scalar residual
\[
H_\sigma(t)=t+\int_0^1 f(x)\bigl(1+\exp((x-t)/\sigma)\bigr)^{-1}\,dx-\beta W_2
\]
is continuous and strictly increasing from negative to positive infinity, since \(f>0\) and the logistic factor increases in \(t\). Thus it has exactly one real zero. At \(\sigma=0\), the same statement holds with the logistic factor replaced by \(\mathbf1_{\{x<t\}}\). The resulting cutoff is the unique pure equilibrium; dominated convergence and boundedness of the cutoffs give \(t_\sigma\to t_0\).

**Boundary-layer expansion.** Put \(L(z)=1/(1+e^{-z})\) and \(K(z)=L(-z)-\mathbf1_{\{z<0\}}\). The function \(K\) is odd, decays exponentially, and has moments
\[
\int_{\mathbb R}K(z)\,dz=0,\qquad
\int_{\mathbb R}zK(z)\,dz
=2\int_0^\infty\frac{z}{1+e^z}\,dz=\frac{\pi^2}{6}.
\]
Uniformly for \(t\) in a compact neighborhood of the interior point \(t_0\), change variables \(x=t+\sigma z\) and Taylor-expand \(f\) to obtain
\[
\int_0^1f(x)L((t-x)/\sigma)\,dx
=\int_0^t f(x)\,dx+\frac{\pi^2}{6}\sigma^2 f'(t)+o(\sigma^2).
\]
The truncation tails are exponentially small. Since the derivative of \(t+\int_0^t f-\beta W_2\) at \(t_0\) equals \(1+f(t_0)>0\), the implicit scalar equation first yields \(t_\sigma-t_0=O(\sigma^2)\), then the displayed exact coefficient.

**Sharp profile and deterministic-partition rates.** The integral of the absolute logistic-step difference across the real line is \(2\log2\); its squared integral is \(2\log2-1\). Rescale \(x=t_0+\sigma z\), use \((t_\sigma-t_0)/\sigma\to0\), and apply dominated convergence with exponential tails. This yields the two weighted norm asymptotics. For small enough noise, \(A_\sigma\triangle A_0\) is the interval between the two cutoffs, so its measure is \(\rho(t_0)|t_\sigma-t_0|+o(|t_\sigma-t_0|)\). Substitution gives the formula even when the quadratic coefficient vanishes.

**Non-potential witness and global monotonicity.** In the explicit game, \(g(x)=2+x\) and \(\beta W_2=1\). The zero-noise equation is \(t+2t+t^2/2=1\), giving \(t_0=\sqrt{11}-3\). Thus \(f'(t_0)=1\) and \(1+f(t_0)=\sqrt{11}\).

A potential differentiable along all feasible variations would have derivative \(\int(x+\int gp-1)\,\eta(x)\,dx\). Its cross-directional derivatives would need to be symmetric. Taking \(u=\mathbf1_{[0,1/4]}\), \(v=\mathbf1_{[3/4,1]}\) gives the nonzero antisymmetric difference
\[
\left(\int u\right)\left(\int gv\right)-
\left(\int v\right)\left(\int gu\right)=\frac3{64}.
\]
The corresponding rectangular path integrals differ, ruling out a potential even in the weaker feasible-directional sense.

For every positive \(\sigma\), its cutoff satisfies \(-1/4<t_\sigma<t_0<1/2\): at \(t=-1/4\) all logistic probabilities are below \(1/2\), while at \(t=t_0\) the logistic integral exceeds its hard-threshold integral by pairing \(t_0-z\) with \(t_0+z\) and using the strict increase of \(g\). At any \(t\le t_0\), the derivative with respect to noise of the logistic integral is positive. For \(t\le0\), every \(x-t\) is positive; for \(0<t\le t_0\), pair the negative contribution from \(t-z\) with the larger positive contribution from \(t+z\), and include the positive unpaired interval \((2t,1]\). Implicit differentiation gives \(dt_\sigma/d\sigma<0\). Uniform convergence of the sigmoid to \(1/2\) as \(\sigma\to\infty\) yields the limit \(1-\frac12\int_0^1(2+x)\,dx=-1/4\).

## Verification

The accompanying `check_rates.py` solves the exact scalar equilibrium equation with bracketing, checks its self-consistency against both congestion terms, and numerically tests the cutoff, \(L^1\), and squared \(L^2\) coefficients at decreasing noise levels. It also checks global cutoff monotonicity over a multiscale test grid, verifies the exact \(3/64\) non-potential cross-derivative obstruction, and independently tests the general formula with a nonuniform density and nonconstant positive impact kernels. Running `python check_rates.py` with SciPy available prints `VERIFY_OK sigma_cases=9 asymptotic_orders=3 nonpotential_gap=3/64` and `VERIFY_GENERAL_OK density_and_heterogeneous_weights`. These finite tests are corroboration; the proof above establishes all quantified statements.

## Relationship to prior work

Dupont, Petit, and Séguret introduce the stochastic variational Nash / continuum logit framework and prove existence, uniqueness under monotonicity, and qualitative zero-noise convergence for non-potential heterogeneous congestion games. Their conclusion explicitly lists **quantitative convergence rates** as future work. Their Theorem 2.2 concerns the induced deterministic partition and does not give its quadratic coefficient; their fixed-point results do not imply the displayed sharp \(L^1\) and \(L^2\) constants. The Sommerfeld / Fermi-Dirac expansion is a classical analytic tool and is not claimed as new: the contribution here is its coupling to the congestion equilibrium self-consistency equation, together with the simultaneous sharp rates for two different equilibrium observables and a genuine non-potential witness.

Cominetti, Scarsini, Schröder, and Stier-Moses address limits from large finite-player games toward nonatomic games, a distinct limit from the present fixed-population small-noise logit regime. Cominetti, Dose, and Scarsini study equilibrium monotonicity under changes in demand, rather than these noise-induced sharp rates. Those comparisons are limited to the accessible material and do not prove global publication priority.

## Limitations

The expansion assumes an interior pure cutoff and smooth positive characteristic density; boundary or singular-density cutoffs can have different exponents. A vanishing derivative \(f'(t_0)\) eliminates the displayed order-two leading term and may require a higher-order analysis. The profile rates are for logit *choice probabilities*, not a random realization of individual choices. The theorem does not establish analogous rates for three or more resources, general interaction nonlinearities, or discontinuous type distributions. Novelty has not been independently audited; differently formulated equivalent prior results remain possible.

## References

1. A. Dupont, Q. Petit, A. Séguret, *Non-Potential Congestion Games with a Continuum of Players*, arXiv:2610.18035 (first submitted 2026-10-13), https://arxiv.org/abs/2610.18035.
2. R. Cominetti, M. Scarsini, M. Schröder, N. Stier-Moses, *Approximation and Convergence of Large Atomic Congestion Games*, Mathematics of Operations Research 48 (2023), https://doi.org/10.1287/moor.2022.1281.
3. R. Cominetti, V. Dose, M. Scarsini, *Monotonicity of Equilibria in Nonatomic Congestion Games*, European Journal of Operational Research 316 (2024), https://doi.org/10.1016/j.ejor.2024.01.050.
4. *Sommerfeld expansion*, standard Fermi-Dirac moment formula; see https://lampz.tugraz.at/~hadley/ss1/fermigas/sommerfeldtable/sommerfeld.php.
