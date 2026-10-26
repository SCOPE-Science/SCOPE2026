# A Poisson resource-ancestry envelope for quantitative extinction in recycling branching Brownian motion

## Finding

In the spatial self-generated-resource branching Brownian motion of Głuchowski and Menz [1], put \(\theta=\beta m/c\), let \(n_0\) be the number of initially alive particles and \(r_0=\mu_0(\mathbb R^d)/m\) the initial resource in corpse-mass units, and let \(\tau_0\) be the first time the population becomes empty. Let \(Q\) denote the total number of particles ever alive, including the initial population. For every deterministic finite initial configuration, every dimension \(d\ge1\), and every bounded, nonnegative, symmetric Borel interaction kernel, the following assertions hold.

**Resource-ancestry domination.** There is a coupling with a forest of independent Poisson(\(\theta\))-offspring Galton–Watson trees having \(n_0+I\) roots, where \(I\) is independent Poisson with mean \(\theta r_0\), such that \(Q\le T\) and \(\tau_0\le S\) almost surely. Here \(T\) is the forest's total number of vertices and \(S\) is the sum of independent exponential lifetimes of rate \(\delta\) over its vertices, independent of the forest. The inequalities are understood with extended values when appropriate.

**Subcritical quantitative extinction.** If \(0<\theta<1\), set
\[
q_* = \delta\bigl(1-\theta e^{1-\theta}\bigr)>0.
\]
For every \(0<q<q_*\), put \(z_q=\delta/(\delta-q)\), and let \(F_\theta(z_q)\) be the solution in \((1,1/\theta)\) of
\[
F_\theta(z_q)=z_q\exp\{\theta(F_\theta(z_q)-1)\}.
\]
Then, for every \(t\ge0\),
\[
\boxed{\displaystyle
\mathbb P(\tau_0>t)\le
F_\theta(z_q)^{n_0}
\exp\{\theta r_0(F_\theta(z_q)-1)\}\,e^{-qt}.}
\]
In particular, \(\mathbb E\tau_0\le(n_0+\theta r_0)/(\delta(1-\theta))\). The permitted exponential rate is uniform over space, diffusion coefficient, kernel shape, and finite initial spatial geometry.

**Critical quantitative extinction.** If \(\theta=1\), then, for every \(t>0\),
\[
\boxed{\displaystyle
\mathbb P(\tau_0>t)\le
\min\left\{1,\ \frac{\sqrt2\,(n_0+r_0)}{(1-e^{-1})\sqrt{\delta t}}\right\}.}
\]
These are upper bounds, not matching lower bounds or assertions of optimal physical-process decay rates.

## Assumptions and scope

Particles perform independent Brownian motions in \(\mathbb R^d\), die at rate \(\delta>0\), and at death deposit resource mass \(m>0\) at their death position. At time \(t\), a live particle at \(x\) gives birth at intensity \(\beta(K*\mu_t)(x)\), with newborn at \(x\). Resource at \(y\) depletes at rate \(c(K*\eta_t)(y)\), with \(\beta,c>0\). The kernel \(K\) is bounded, nonnegative, symmetric, Borel measurable, and not identically zero. The initial particle counting measure \(\eta_0\) has finite integer mass \(n_0\), and the initial nonnegative Borel resource \(\mu_0\) has finite mass. Extinction is absorbing; no immigration or external resource replenishment is permitted. The model's usual well-posed nonexplosive process construction is assumed [1, Section 1]. The bounds remain valid for \(n_0=0\), when \(\tau_0=0\) and \(Q=0\).

The physical time variable and original death rate \(\delta\) are retained. No assumption is made that the resource is fully consumed, that deaths occur at spatially separated points, or that the potential forest accurately approximates the actual joint spatial law. The distributional assertions concern upper-envelope couplings, not equality in law for \(Q\) or \(\tau_0\).

## Proof

**1. Decompose resource by its origin.** Label each initially alive individual and each later newborn. For each particle \(v\), upon its death at \(d_v\) write \(\mu_{v,t}\) for the remaining resource descended from its deposited point mass \(m\delta_{X_v(d_v)}\); for \(t<d_v\) set this component to zero. Write \(\mu_{\star,t}\) for surviving initial resource, whose initial measure is \(\mu_0\). The resource-evolution equation implies the positive decomposition
\[
\mu_t=\mu_{\star,t}+\sum_{v:d_v\le t}\mu_{v,t},
\]
with each component depleted according to the same multiplicative consumption equation as in [1, equations (1), (4)–(5)]. Let \(C_j(t)\) be the cumulative consumed mass of component \(j\), measured from the time the component appeared. Then \(C_\star(\infty)\le\mu_0(\mathbb R^d)\) and \(C_v(\infty)\le m\). This inequality needs no spatial interaction lower bound.

**2. Mark births by the component paying for them.** By symmetry of \(K\), the instantaneous birth rate attributable to component \(j\) is
\[
\lambda_j(t)=\beta\int(K*\mu_{j,t})(x)\,\eta_t(dx)
=\frac\beta c\frac{dC_j(t)}{dt}
=\frac\theta m\frac{dC_j(t)}{dt}
\]
for almost every time between jumps. The full birth intensity is the sum of these nonnegative contributions. Given its component mark, a birth at location \(x\) is sampled from the corresponding kernel-weighted live-particle intensity, preserving the original spatial birth law. Assign an independent unit-rate Poisson point process in the **consumed-mass coordinate** to each component, so that births charged to component \(j\) are its Poisson points encountered before the random horizon \(\theta C_j(\infty)/m\). This is the standard random-time-change construction of component-marked jump intensities [5]; it is well-defined by successive event construction/localization. Because the coordinate horizons are bounded above, the number of actual births charged to the initial component is at most an independent \(\operatorname{Poisson}(\theta r_0)\) variable, and the number charged to a particular corpse is at most an independent \(\operatorname{Poisson}(\theta)\) variable. The **complete** Poisson point processes on these deterministic coordinate intervals are independent of one another and of independently sampled death clocks; adaptive consumption can only suppress available points, never produce more.

**3. Build the forest.** Let the \(n_0\) initially alive individuals and all potential Poisson points of the initial-resource component be roots. For every potential individual, independently sample a Poisson point process on \([0,\theta]\); its points are potential children paid for by the resource that would be released when this individual dies. Attach every actual newborn to the label of the resource component charged for its birth, rather than to its biological mother. A resource-parent must already be dead at its child's birth, so the resulting resource-ancestry graph is acyclic. A child of the initial component is an additional root. Sampling all unused potential points recursively completes an ordinary independent Poisson(\(\theta\)) Galton–Watson forest with \(n_0+I\) roots and \(I\sim\operatorname{Poisson}(\theta r_0)\). Every actual individual injects into a potential vertex, giving \(Q\le T\) pathwise. Give every potential vertex an independent rate-\(\delta\) exponential lifetime, using the already sampled lifetime for an actual individual. These lifetimes are independent of the complete potential offspring forest because particle death clocks and component Poisson point processes are sampled independently. If \(\tau_0<\infty\), the occupation identity gives
\[
\tau_0\le\int_0^{\tau_0}\eta_s(\mathbb R^d)\,ds
=\sum_{v\text{ actual}}(d_v-b_v)
\le\sum_{v\text{ potential}}E_v=S.
\]
If \(S<\infty\), the same occupation inequality up to every finite time forces \(\tau_0\le S\), so the bound is valid without first assuming extinction. This proves the domination assertion.

**4. Subcritical generating functions and exponential time tails.** For \(\theta\le1\), the Poisson-offspring forest is finite almost surely. If \(Y\) is the total number of potential vertices descended from one root, its probability generating function \(F_\theta(z)=\mathbb E z^Y\) obeys
\[
F_\theta(z)=z\exp\{\theta(F_\theta(z)-1)\}.
\]
For \(0<\theta<1\), the increasing solution has its first positive singularity at \(z_c=e^{\theta-1}/\theta>1\) and \(F_\theta(z_c)=1/\theta\). Thus, when \(1<z<z_c\),
\[
\mathbb E z^T=F_\theta(z)^{n_0}\exp\{\theta r_0(F_\theta(z)-1)\}.
\]
Conditionally on the forest, \(S\) is the sum of \(T\) independent rate-\(\delta\) exponential variables. Therefore, for \(0<q<q_*\), its moment generating function is obtained by substituting \(z=\delta/(\delta-q)<z_c\):
\[
\mathbb E e^{qS}=F_\theta(z)^{n_0}\exp\{\theta r_0(F_\theta(z)-1)\}.
\]
By \(\tau_0\le S\) and Markov's inequality, this proves the exponential bound. Moreover \(\mathbb E T=(n_0+\theta r_0)/(1-\theta)\), whence \(\mathbb E\tau_0\le\mathbb E S=\mathbb E T/\delta\).

**5. Critical \(t^{-1/2}\) tail.** Take \(\theta=1\). For \(t>0\) set \(z_t=\delta t/(1+\delta t)\), \(u_t=1-F_1(z_t)\), and \(h_t=\log(1+1/(\delta t))\). The fixed-point equation becomes
\[
-\log(1-u_t)-u_t=h_t.
\]
Since \(-\log(1-u)-u\ge u^2/2\) for \(u\in[0,1)\),
\[
0\le u_t\le\sqrt{2h_t}\le\sqrt{2/(\delta t)}.
\]
The Laplace transform of the exponential-lifetime forest is
\[
\mathbb E e^{-S/t}=(1-u_t)^{n_0}\exp(-r_0u_t).
\]
Consequently,
\[
(1-e^{-1})\mathbb P(S>t)
\le 1-\mathbb E e^{-S/t}
\le(n_0+r_0)u_t
\le(n_0+r_0)\sqrt{2/(\delta t)}.
\]
Apply \(\mathbb P(\tau_0>t)\le\mathbb P(S>t)\) and the trivial bound by one. This proves the critical assertion.

## Verification

The independent standard-library program `VERIFY.py` numerically checks the subcritical Borel generating-function equation against a separately evaluated large finite series; the admissible exponential-moment domain; and the critical logarithmic identity and square-root inequalities for multiple parameters. It reports **52 passed numerical algebra and series assertions**. This checks representative algebraic instances, not the spatial coupling or any infinite-population theorem. The coupling proof above, together with the cited source's exact generator and resource decomposition, supplies the analytical argument.

## Relationship to prior work

Głuchowski and Menz [1] define the identical spatial particle/resource process, prove almost-sure extinction at \(\theta\le1\), and give the resource decomposition [1, equation (5)] and the exact proportionality of birth to consumption rates [1, Section 1]. Their extinction proof uses a nonnegative supermartingale; it does not establish the explicit Poisson-forest domination or the exponential and critical polynomial extinction-time tail bounds above. Classical Poisson–Galton–Watson total-progeny generating functions and Borel laws [2, 3] supply the **known** probabilistic input, not the new model-specific resource-ancestry embedding. General marked or type-space Poisson–Galton–Watson integrability results [4] concern branching forests once constructed; the delicate question here is whether this interacting spatial resource process admits such a dominating forest. The theorem provides that explicit coupling and converts it into uniform finite-time bounds.

## Limitations

The exponential rate \(q_*\) describes the dominating potential forest, and may be much smaller than the actual process's optimal extinction rate. The critical \(t^{-1/2}\) bound is one-sided and is not claimed sharp; no positive matching lower bound or critical expected-extinction-time divergence is proved. The offspring coupling depends essentially on proportional birth and consumption of the same nonnegative symmetric interaction kernel, additive resource deposits at deaths, and independent constant-rate death clocks. These statements do not automatically extend to externally supplied or diffusing resources, resource-dependent death rates, nonsymmetric kernels with differing birth/consumption forms, or \(\theta>1\), where the dominating forest may survive. Independent verification and further literature-priority assessment have not been performed.

## References

[1] M. Głuchowski and G. Menz, *A sharp survival threshold for branching Brownian motion in a self-generated resource environment*, arXiv:2610.21476v1 (first posted 2026-10-15), https://arxiv.org/html/2610.21476v1.

[2] E. Borel, *Sur l'emploi du théorème de Bernoulli pour faciliter le calcul d'une infinité de coefficients*, C. R. Acad. Sci. 214 (1942), 452–456.

[3] M. Dwass, *The total progeny in a branching process and a related random walk*, Journal of Applied Probability 6 (1969), 682–686.

[4] B. Hu and W. Sun, *Dynamical Equations for Poisson Galton–Watson Trees and Component Densities of Sparse Inhomogeneous Random Graphs*, arXiv:2607.16833 (2026), https://arxiv.org/abs/2607.16833.

[5] N. L. Garcia, *Birth and death processes as projections of higher-dimensional Poisson processes*, Advances in Applied Probability (2016), https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/birth-and-death-processes-as-projections-of-higherdimensional-poisson-processes/A57F3E452F835EBE420C1F13832CC32D. (General Poisson projection/time-change background; the forest embedding in the present model is not asserted by this source.)
