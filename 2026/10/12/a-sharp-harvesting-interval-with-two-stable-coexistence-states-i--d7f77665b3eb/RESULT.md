# A sharp harvesting interval with two stable coexistence states in a weak-Allee predator–prey model

## Finding

Consider the diffusion-free weak-Allee predator–prey model of Liu, Liang, Li, Ye, and Ma, restricted to the mortality subfamily \(e=1\), \(\gamma=\eta\). For fixed \(\alpha,\beta,\eta>0\) and \(0<A<1\), the set of positive prey-harvesting rates \(E>0\) for which the model has **exactly three distinct strictly positive coexistence equilibria** is either empty or one sharp open interval specified below.

Define, for \(u\ge0\),
\[
h(u)=(1-u)(u+A)-\frac{\beta u}{\eta(1+\beta u)},\qquad
u_\mathrm{i}=\frac{(\beta^2/\eta)^{1/3}-1}{\beta}.
\]
There are exactly three distinct positive coexistence equilibria if and only if all the following hold:
\[
\beta^2>\eta,\qquad h'(0)<0,\qquad h'(u_\mathrm{i})>0,
\]
and, writing \(u_-<u_\mathrm{i}<u_+\) for the two positive roots of \(h'(u)=0\),
\[
\boxed{\quad
\alpha\max\{0,h(u_-)\}<E<\alpha\min\{A,h(u_+)\}
\quad}
\]
If the interval has no positive length, there is no harvesting rate with three distinct positive coexistence equilibria. For any three such equilibria \((u_j,\beta u_j/\eta)\), with \(0<u_1<u_2<u_3\), the middle equilibrium is a hyperbolic saddle and the outer equilibria have positive Jacobian determinants. Negative Jacobian traces suffice for local asymptotic stability of the outer equilibria; positive traces imply instability, and zero traces require a separate nonlinear analysis.

The interval is nonempty in an all-positive, explicitly certified example:
\[
\alpha=1,\quad A=\frac15,\quad \beta=8,\quad
\eta=\gamma=6,\quad e=1,\quad E=\frac{39}{200}.
\]
Here there are exactly three positive coexistence equilibria, the first and third are **locally asymptotically stable**, and the second is a hyperbolic saddle. In particular, this instance admits two distinct attracting prey–predator coexistence states at the same positive harvesting rate. The prey per-capita growth at zero predator and vanishing prey is still positive, \(\alpha A-E=1/200>0\); hence the pair of attractors does not result from imposing a negative low-density prey growth rate. Their hyperbolicity ensures this phenomenon persists throughout a neighborhood in the full positive parameter space, without imposing \(e=1\) or \(\gamma=\eta\) after perturbation.

## Assumptions and scope

The state is \((u,v)\in(0,\infty)^2\) and the equations, including proportional prey harvesting, are
\[
\dot u=\alpha u(1-u)(u+A)-\frac{\alpha uv}{1+\beta u}-Eu,
\qquad
\dot v=\frac{\beta uv}{1+\beta u}-\frac{\gamma v^2}{e+\eta v}.
\]
All rate parameters are strictly positive, and \(0<A<1\). For the sharp three-equilibrium classification only, impose the source's simplifying subfamily \(e=1\), \(\gamma=\eta\); its off-subfamily persistence conclusion applies only locally around the explicit hyperbolic example. A coexistence equilibrium means \(u>0\), \(v>0\) and both derivatives zero. The classification counts distinct positive equilibria, not multiplicities or boundary equilibria.

## Proof

**Reduction to a harvest-height intersection.** With \(e=1\) and \(\gamma=\eta\), division of the predator equation by \(v>0\) gives
\[
\frac{\beta u}{1+\beta u}=\frac{\eta v}{1+\eta v},
\quad\Longleftrightarrow\quad v=\frac{\beta u}{\eta}.
\]
Substitution into the prey equation, divided by \(\alpha u\), yields \(h(u)=E/\alpha\). Conversely, every positive solution of this scalar equation yields one positive equilibrium, so this is an exact equivalence. Multiplication by the positive denominator \(1+\beta u\) gives a cubic, with negative leading coefficient; therefore there are at most three positive solutions.

**Exact criterion.** Direct differentiation gives
\[
h'(u)=1-A-2u-\frac{\beta}{\eta(1+\beta u)^2},\qquad
h''(u)=-2+\frac{2\beta^2}{\eta(1+\beta u)^3}.
\]
The second derivative strictly decreases on the nonnegative half-line. If \(\beta^2\le\eta\), then \(h'\) strictly decreases for all \(u>0\) and cannot have the two positive zeros necessary for three crossings. If \(\beta^2>\eta\), the function \(h'\) first increases up to the unique point \(u_\mathrm i>0\) where \(h''=0\), and then strictly decreases to \(-\infty\). It has exactly two distinct positive roots precisely when \(h'(0)<0<h'(u_\mathrm i)\). Denote these roots by \(u_-<u_+\). Then \(h\) strictly decreases on \((0,u_-)\), increases on \((u_-,u_+)\), and decreases on \((u_+,\infty)\); its starting height is \(h(0)=A\), and its limit is \(-\infty\). Thus the positive level \(E/\alpha\) has exactly one intersection in each of those three ranges precisely when
\[
\max\{0,h(u_-)\}<E/\alpha<\min\{A,h(u_+)\}.
\]
This proves both directions, all strict boundaries, and the claimed single interval.

**Stability signs.** At any positive equilibrium in this subfamily, let \(J\) be the full two-dimensional reaction Jacobian. Differentiating the original equations and then imposing the two equilibrium relations gives the exact identity
\[
\boxed{\det J=-\frac{\alpha\beta u^2}{(1+\beta u)^2}h'(u).}
\]
At the three simple intersections \(h'(u_1)<0\), \(h'(u_2)>0\), \(h'(u_3)<0\). The first and third determinants are positive and the middle determinant negative. Hence the middle is a saddle, whereas the outer states are locally asymptotically stable when their traces are negative and are unstable when the traces are positive; a zero trace is not decided by this test.

**Exact two-attractor witness.** At the displayed rational parameters, the coexistence equation is equivalent to \(P(u)=0\), where
\[
P(u)=-4800u^3+3240u^2-296u+3,
\quad h(u)-\frac{39}{200}=\frac{P(u)}{600(1+8u)}.
\]
The endpoint signs are
\[
\begin{array}{c|rrrrrr}u&11/1000&12/1000&94/1000&96/1000&568/1000&569/1000\\\hline
\operatorname{sgn}P(u)&+&-&-&+&+&-
\end{array}
\]
so there is a simple positive root in each of the three disjoint intervals
\[
(11/1000,12/1000),\qquad(94/1000,96/1000),\qquad(568/1000,569/1000).
\]
The cubic has degree three, so these are all its roots. Each associated predator coordinate is \(v=4u/3>0\). On all positive coexistence states of this parameter slice, the Jacobian trace is
\[
\operatorname{tr}J=-\frac{2u\,Q(u)}{15(1+8u)^2},
\qquad Q(u)=960u^3-144u^2-161u+54.
\]
Here \(Q'(u)=(24u-7)(120u+23)\), so \(Q\) attains its minimum on \([0,\infty)\) at \(u=7/24\), with \(Q(7/24)=335/18>0\). Therefore the trace is strictly negative at all three positive equilibria. The determinant identity gives positive determinant at the first and third equilibria and negative determinant at the middle; the former are hyperbolic asymptotically stable, the latter a hyperbolic saddle. Finally, all three roots are simple and all three equilibria hyperbolic; parameter-continuity and the implicit-function theorem preserve this configuration under sufficiently small parameter perturbations, including \(e\) and \(\gamma-\eta\).

## Verification

A standalone SymPy script `verify.py` checks the equilibrium reduction, exact determinant identity, derivatives, witness cubic, all six rational endpoint signs, exact trace factorization, and global positivity of the trace polynomial. It exits with `VERIFY_OK` when all assertions hold. The analytical monotonicity argument above proves the global three-root iff statement; no numerical sampling is used as a substitute for it.

## Relationship to prior work

Liu et al. (2026), especially Eq. (4), Theorem 1, Theorem 4, and the discussion preceding their global-stability theorem, provide the model, its cubic coexistence equation, sufficient one-root conditions, and a general local stability test. They do not state the exact positive-harvest interval with three roots or establish a two-attractor parameter witness in this model. The present classification makes explicit the alternative coexistence branch geometry outside their sufficient uniqueness conditions; it does not dispute their conditional unique-equilibrium results.

Arancibia-Ibarra, Flores, and van Heijster (2022) already exhibited three positive coexistence equilibria and two stable states in a **different** weak-Allee Leslie–Gower predator–prey system, with predator nullcline \(v=u\) and prey nullcline \(v=(u+A)(1-u)(u-M)/Q\). Thus neither cubic bistability nor the general ecological phenomenon is claimed to be new. Their model lacks the particular proportional prey-harvest parameter and hyperbolic predator mortality of the Liu system, and their parameter criterion does not imply the sharp \(E\)-interval here. Devi and Fatma (2024) treat a strong-Allee, Holling-I, predator-harvesting model, likewise not this exact system. The novelty claimed is only the model-specific sharp classification together with a certified two-stable-state example.

## Limitations

The exact iff interval applies only when \(e=1\), \(\gamma=\eta\). Robustness outside this subfamily is local near the specific hyperbolic example, not a global classification of all parameters. The statement is about local attraction and equilibrium multiplicity; it neither classifies global basins nor guarantees ecological feasibility beyond positive state coordinates and rates, nor proves diffusion-driven stability or spatial pattern claims. No independent review or empirical validation is claimed. Prior-work coverage is necessarily bounded by the specifically inspected publications and searches.

## References

1. H. Liu, Y. Liang, Y. Li, J. Ye, and F. Ma, “Turing instability and pattern induced by weak Allee effect and prey harvesting in a predator-prey model,” *Advances in Continuous and Discrete Models* **2026**, 11 (2026), first public 5 January 2026. https://doi.org/10.1186/s13662-025-04046-z
2. C. Arancibia-Ibarra, J. D. Flores, and P. van Heijster, “Stability Analysis of a Modified Leslie–Gower Predation Model With Weak Allee Effect in the Prey,” *Frontiers in Applied Mathematics and Statistics* **7**, 731038 (published 26 January 2022). https://doi.org/10.3389/fams.2021.731038
3. S. Devi and R. Fatma, “Diffusion-Driven Instability and Bifurcation in the Predator–Prey System with Allee Effect in Prey and Predator Harvesting,” *International Journal of Applied and Computational Mathematics* **10**, 39 (2024). https://doi.org/10.1007/s40819-023-01673-6
