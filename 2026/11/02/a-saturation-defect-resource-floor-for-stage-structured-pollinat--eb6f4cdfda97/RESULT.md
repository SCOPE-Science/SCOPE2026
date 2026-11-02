# A saturation-defect resource floor for stage-structured pollinator persistence

## Finding

In the dimensionless plant--larva--adult (PLA) model of Revilla and Encinas-Viso [1], a precisely weighted combined insect biomass has an exact negative saturation defect. This determines a quantitative resource condition for every positive periodic population or compact positive stationary state, and a global sufficient condition for insect extinction independent of initial insect density.

Write \(x\), \(y\), and \(z\) for plant, larval, and adult biomasses, respectively. Define

\[
q=\gamma\beta,\quad c=\frac{\varepsilon\alpha}{\eta},\quad
\mathcal R(X)=\frac{qX(cX+\phi)}{\nu(\mu+qX)}.
\]

Let \(x_*>0\) be the unique root of \(\mathcal R(x_*)=1\), equivalently

\[
x_*=\frac{\nu-\phi+\sqrt{(\nu-\phi)^2+4c\nu\mu/q}}{2c},\qquad
K_*=1+\frac{\mu}{qx_*}.
\]

**One resource-budget theorem.** The insect-weight \(W=y+K_*z\) satisfies the pointwise identity

\[
\boxed{\frac{dW}{dt}=(x-x_*)A-J,\quad
A=\frac{\mu}{x_*}y+cz,\quad J=\frac{cxz^2}{\eta+z}.}
\]

Thus every strictly positive periodic trajectory of period \(T>0\) satisfies the exact strict weighted-mean law

\[
\boxed{\frac{\int_0^T x(t)A(t)\,dt}{\int_0^T A(t)\,dt}
=x_*+\frac{\int_0^T J(t)\,dt}{\int_0^T A(t)\,dt}>x_*.}
\]

The same identity, with integration against an invariant probability measure, holds for every probability measure invariant under the PLA flow whose support is compact and contained entirely in the strictly positive orthant. In particular, every strictly positive periodic solution has \(\max_t x(t)>x_*\), irrespective of whether its plant biomass lies above or below the carrying capacity \(1\) at other times.

Finally, if \(1+\sigma\alpha<x_*\), then **every** solution initialized with \(x(0)>0\), \(y(0),z(0)\ge0\) obeys \(y(t)+z(t)=O(e^{-\delta t})\) for some \(\delta>0\) depending on the parameters, and \(x(t)\to1\). This provides an explicit global exclusion criterion, including possible large-insect initial conditions, rather than only a local invasion test.

## Assumptions and scope

The autonomous dimensionless ODE, with time in plant-renewal units, is exactly

\[
\begin{aligned}
\dot x&=x(1-x)+\sigma\alpha\frac{xz}{\eta+z}-\beta xy,\\
\dot y&=\varepsilon\alpha\frac{xz}{\eta+z}+\phi z-(\mu+\gamma\beta x)y,\\
\dot z&=\gamma\beta xy-\nu z.
\end{aligned}
\]

Assume \(\alpha,\eta,\beta,\mu,\nu,\sigma>0\), \(0<\varepsilon,\gamma<1\), and \(\phi\ge0\). The positive orthant is forward invariant. Initial plant biomass is strictly positive and insect biomasses are nonnegative. No assumption about the existence of a positive periodic orbit is made: the periodic and invariant-state statements are conditional on their existence. The invariant probability measure is for the deterministic flow, not for a stochastic perturbation. The numerical value \(x_*\) is an insect replacement level as a function of plant biomass; it need not be below plant carrying capacity.

## Proof

**1. Unique replacement biomass.** Because \(q,c,\mu,\nu>0\) and \(\phi\ge0\), the function \(\mathcal R(X)\) is strictly increasing from \(0\) to \(+\infty\) for \(X>0\). Its positive unit root is therefore unique and solves

\[
cx_*^2+(\phi-\nu)x_*-\frac{\nu\mu}{q}=0.
\]

In particular, the root equation is equivalent to both

\[
q x_*(K_*-1)=\mu,\qquad \nu K_*=cx_*+\phi.
\]

**2. Exact balance and saturation.** Substitute the larval and adult equations into \(\dot W=\dot y+K_*\dot z\). The coefficient of \(y\) becomes

\[
-\mu+qx(K_*-1)=\frac{\mu}{x_*}(x-x_*).
\]

The adult contribution becomes \(\varepsilon\alpha xz/(\eta+z)+(\phi-\nu K_*)z\). Since \(\varepsilon\alpha=c\eta\), it equals

\[
cz(x-x_*)-\frac{cxz^2}{\eta+z}.
\]

This yields the displayed identity exactly, with no quasi-linear approximation beyond the flower quasi-steady-state assumption already present in the model.

**3. All positive recurrent states.** Integrate the derivative of \(W\) over one period, obtaining \(0=\int_0^T(x-x_*)A-\int_0^T J\). Strict positivity of \(x,y,z\) throughout the period gives \(\int A>0\) and \(\int J>0\). Division yields the strict weighted-average law. For a compactly supported invariant probability measure in \((0,\infty)^3\), invariance and differentiability give \(\int\dot W\,d\pi=0\) (all quantities are bounded on the compact support), and strict positivity of the integrands gives the identical argument. A weighted mean cannot exceed the maximum plant biomass, hence \(\max_t x(t)>x_*\) for any positive periodic trajectory.

**4. Global exclusion under the plant ceiling.** Put \(M=1+\sigma\alpha\). For every nonnegative state,

\[
\dot x\le x(M-x)
\]

because \(z/(\eta+z)\le1\) and the herbivory term is nonpositive. Standard scalar logistic comparison gives \(\limsup_{t\to\infty}x(t)\le M\). If \(M<x_*\), choose \(d>0\) with \(M+d<x_*\); then for all sufficiently large \(t\), \(x(t)\le M+d\), so

\[
\dot W\le-(x_*-M-d)A
\le-(x_*-M-d)\min\left\{\frac{\mu}{x_*},\frac{c}{K_*}\right\}W.
\]

Thus \(W\), and hence \(y,z\), decay exponentially. The logistic upper and lower comparisons for the plant, using \(\beta y\to0\) and \(\sigma\alpha z/(\eta+z)\to0\), then show \(\limsup x\le1\le\liminf x\). Positivity and boundedness establish global existence and justify these comparisons. This completes the proof.

**5. Sharpness of the recurrent resource floor.** The strict threshold \(x_*\) is not a numerical artifact. Fix positive insect parameters with \(x_*>1\) and take any \(\xi>x_*\) sufficiently close. Define

\[
F(\xi)=\frac{\nu(\mu+q\xi)}{q\xi}-\phi,\qquad
z_\xi=\frac{\varepsilon\alpha\xi}{F(\xi)}-\eta,\qquad
y_\xi=\frac{\nu z_\xi}{q\xi},
\]

and choose the positive plant-benefit coefficient

\[
\sigma_\xi=\frac{(\xi-1+\beta y_\xi)(\eta+z_\xi)}{\alpha z_\xi}.
\]

Since \(F(x_*)=cx_*>0\), and \(F\) strictly decreases, \(z_\xi>0\) for \(\xi>x_*\). Direct substitution makes \((\xi,y_\xi,z_\xi)\) an exact positive equilibrium. As \(\xi\downarrow x_*\), its plant coordinate approaches the floor from above. This varying-\(\sigma\) construction demonstrates sharpness for the resource-floor parameter, not an optimality claim for the extinction test at a fixed \(\sigma\).

## Verification

A standalone exact checker `check.py` verifies the symbolic cancellation in the weighted derivative using the positive-root relation, an explicit nonzero equilibrium, and 1,000 exact rational assertions across 500 positive parameter configurations. The infinite-parameter theorem is proved by the identities and comparison in the preceding section, not by finite computational sampling.

For one exact example take \(\alpha=3/2\), \(\eta=1\), \(\varepsilon=\gamma=1/2\), \(\beta=2\), \(\mu=\nu=1\), \(\phi=0\). Then \(q=1\), \(c=3/4\), \(x_*=2\), \(K_*=3/2\). With \(\sigma=1/2\), \(M=7/4<2\), giving global insect extinction. With \(\sigma=177/44\), the positive state \((x,y,z)=(3,11/48,11/16)\) is an exact equilibrium; its resource surplus and saturation penalty are both \(121/192\).

To replay, use Python 3 with SymPy and execute `python check.py` in the directory containing the extracted public files.

## Relationship to prior work

Revilla and Encinas-Viso [1] introduce the PLA ODE, its invasion reproductive ratio at the plant-only state, the positive larval-isocline threshold (equivalent to \(x_*\) at equilibrium), and numerical coexistence and oscillatory regimes. Those baseline model facts are **not** proposed as new. The assertion assessed here is the exact **positive saturation-defect law on all compact positive stationary states**, yielding a quantitative weighted plant-resource floor on cycles, together with a global Lyapunov exclusion test from the logistic plant ceiling. Their published discussion expressly raises time-averaging as an unresolved way of classifying oscillatory plant--insect regimes; the inspected main paper does not provide this identity.

Related mathematical-ecology studies [2,3] analyze distinct plant--pollinator--herbivore systems with a separate herbivore species, or plant--nectar--pollinator mutualisms with a different obligatory species. Such results do not, based on their inspected model descriptions, imply the specific three-compartment resource law. Published results for other predator--prey systems may also use weighted biomass balances, but do not directly supply this PLA identity. The primary article's supplemental technical appendix could not be obtained for full inspection, and historical priority therefore remains subject to independent evaluation.

## Limitations

The theorem is deterministic and autonomous and assumes homogeneous interacting biomasses, fast-flower reduction, saturating adult benefits, positive larval and adult loss, and the displayed stage transition. It is not an observed ecological effect. A strict weighted mean above \(x_*\) does **not** assert an unweighted mean plant biomass above the threshold, nor existence or stability of periodic orbits. The condition \(1+\sigma\alpha<x_*\) is sufficient, not proved necessary, for global extinction. The equality case is excluded from the extinction conclusion. The invariant-measure extension requires compact support entirely in the positive orthant; it does not apply unchanged to boundary-supported measures or stochastic systems.

## References

[1] T. A. Revilla and F. Encinas-Viso, *Dynamical transitions in a pollination--herbivory interaction: a conflict between mutualism and antagonism*, arXiv:1404.4804 (public April 18, 2014); *PLOS ONE* 10(2), e0117964 (2015), https://doi.org/10.1371/journal.pone.0117964.

[2] M. Chen, H. Wu, and Y. Wang, *Persistence and Oscillations of Plant-Pollinator-Herbivore Systems*, *Bulletin of Mathematical Biology* 82, 57 (2020), https://doi.org/10.1007/s11538-020-00735-w.

[3] H. Yuan, Y. Wang, H. Wu, and S. Wu, *Persistence of pollination-mutualisms under the effect of intermediary resource*, *Natural Resource Modeling* 33 (2020), https://doi.org/10.1111/nrm.12259.
