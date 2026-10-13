# Gaussian-in-generation herbivore collapse in a strong-Allee Ricker system

## Finding

Consider the biomass-sharing discrete plant–herbivore dynamics
\[
 x_{n+1}=x_n f(x_n)e^{-a y_n},\qquad
 y_{n+1}=x_n f(x_n)(1-e^{-a y_n}),
\]
with \(a>0\), strictly positive initial populations, and a positive growth factor \(f\) that is continuously differentiable near zero with \(q=f(0)\in(0,1)\). Every positive orbit converging to extinction has *sharp, simultaneous* asymptotics
\[
 x_n=Cq^n(1+o(1)),\qquad
 y_n=D(aC)^nq^{n(n+1)/2}(1+o(1)),\tag{1}
\]
for finite strictly positive, orbit-dependent constants \(C,D\) given explicitly below. In particular, plant biomass falls geometrically while herbivore biomass falls at a quadratic logarithmic rate. The exponent \(n(n+1)/2\) is fixed by the shared-biomass attack-after-growth mechanism rather than by the precise higher-order growth law.

For the strong-Allee Ricker model (5) of Bešo–Kalabušić–Pilav [1],
\[
 f(x)=\exp\bigl(r(1-x)(x-b)\bigr),\qquad r>0,\quad 0<b<1,
\]
every positive orbit tending to \((0,0)\) obeys (1) with \(q=e^{-rb}\); in particular, all initial states with \(0<x_0<b\) and \(y_0>0\) are covered without a separate extinction assumption. Consequently
\[
 \lim_{n\to\infty}\frac{\log x_n}{n}=-rb,\qquad
 \lim_{n\to\infty}\frac{\log y_n}{n^2}=-\frac{rb}{2}.
\]
Let \(T_x(\eta)\) and \(T_y(\eta)\) denote the first generations at which the respective positive normalized biomasses fall to or below \(\eta\). For each fixed orbit as above,
\[
 T_x(\eta)=\frac{\log(1/\eta)}{rb}+O(1),\qquad
 T_y(\eta)=\sqrt{\frac{2\log(1/\eta)}{rb}}+O(1)
 \quad(\eta\downarrow0).
\]
The detection-time contrast is an asymptotic statement about the deterministic equations, not a claim about stochastic ecological extinction.

## Assumptions and scope

The general theorem assumes that \(f:(0,\infty)\to(0,\infty)\) has a positive continuously differentiable extension to some interval \([0,\varepsilon)\), with \(0<q=f(0)<1\). Choose \(x_0>0,y_0>0\), require the orbit be well-defined for every nonnegative integer \(n\), and assume \((x_n,y_n)\to(0,0)\). The Ricker specialization requires \(r,a>0\), \(0<b<1\); its map is well-defined and positive for every positive initial state. Neither assertion includes the coordinate-axis initial conditions \(x_0=0\) or \(y_0=0\), for which the positive prefactor in (1) generally cannot exist.

For any such orbit put
\[
 \delta_j=\log\frac{f(x_j)}q-a y_j,\qquad
 \phi_j=\log\frac{e^{a y_j}-1}{a y_j}.
\]
The asymptotic constants are the absolutely convergent expressions
\[
 \log C=\log x_0+\sum_{j=0}^{\infty}\delta_j,
 \qquad
 \log D=\log y_0-\sum_{j=1}^{\infty}j\delta_j+\sum_{j=0}^{\infty}\phi_j.
\tag{2}
\]
These definitions make the full prefactors, and not just logarithmic orders, reproducible from the initial state and parameters.

## Proof

**1. Uniform eventual contraction.** Since \(f(0)=q<1\) and \(f\) is continuous, choose \(q<\rho<1\) and a sufficiently small neighborhood of zero in which \(0<f(x)\le\rho\). A trajectory converging to zero eventually enters this neighborhood and thereafter
\[
 0<x_{n+1}\le\rho x_n.
\]
Thus \(x_n=O(\rho^n)\). Since \(0<1-e^{-a y_n}<1\), the second recurrence gives \(0<y_{n+1}\le x_n f(x_n)\le\rho x_n\) for all sufficiently large \(n\), hence \(y_n=O(\rho^n)\) as well.

**2. Summability and the plant prefactor.** Local differentiability and \(f(0)=q>0\) yield \(\log(f(x)/q)=O(x)\) as \(x\downarrow0\). Therefore \(\sum_{j=0}^{\infty}(j+1)|\delta_j|<\infty\). Taking logarithms of the plant recurrence gives the *exact identity*
\[
 \log x_n=\log x_0+n\log q+\sum_{j=0}^{n-1}\delta_j.
\]
This proves \(x_n/(Cq^n)\to1\), with the positive finite \(C\) in (2), and also
\[
 \log\frac{x_k}{Cq^k}=-\sum_{j=k}^{\infty}\delta_j.
\tag{3}
\]
The right-hand side is absolutely summable over \(k\ge1\) because the weighted series already converges.

**3. The herbivore prefactor.** The two recurrences satisfy the exact biomass-partition identity
\[
 y_{n+1}=x_{n+1}(e^{a y_n}-1).
\]
For \(y\downarrow0\), \(\log[(e^{ay}-1)/(ay)]=O(y)\); hence \(\sum_{j=0}^{\infty}|\phi_j|<\infty\). Iteration yields
\[
 \log y_n=\log y_0+n\log a+\sum_{k=1}^{n}\log x_k+\sum_{j=0}^{n-1}\phi_j.
\]
Substitute (3), then interchange the absolutely convergent triangular series:
\[
 \sum_{k=1}^{\infty}\log\frac{x_k}{Cq^k}
 =-\sum_{j=1}^{\infty}j\delta_j.
\]
The finite sum \(\sum_{k=1}^n k\log q=n(n+1)\log q/2\) gives
\[
 \log y_n=\frac{n(n+1)}2\log q+n\log(aC)+\log D+o(1).
\]
Exponentiation establishes (1). Every infinite manipulation above is justified by the exponential majorants in Step 1; no finite simulation is treated as a proof.

**4. Ricker extinction basin and threshold clocks.** If \(0<x_0<b\), then \(f(x)<1\) on \((0,b)\). Moreover \(r(1-x)(x-b)\) increases on \([0,b]\), since its derivative is \(r(1+b-2x)>0\). Thus \(x_{n+1}<x_n<b\) and \(x_{n+1}\le f(x_0)x_n\) for every \(n\), while \(y_{n+1}\le x_n\), proving extinction without invoking an unproved basin assertion. More generally, each positive extinction orbit eventually enters this region, so the general theorem applies. At zero density \(q=\exp[-rb]\) and the displayed Ricker rates follow. Lastly, the exact identity \(y_{n+1}/y_n=x_{n+1}(e^{a y_n}-1)/y_n\) shows that the herbivore ratio tends to zero, so both coordinates are eventually decreasing. Inverting the asymptotic logarithmic laws in (1), with integer rounding, gives the two stated first-threshold generation estimates. The \(O(1)\) constants may depend on the orbit.

## Verification

Run `python verify.py` using Python 3 and the standard library. It first compares two algebraically equivalent updates over finite positive trajectories, then uses numerically stable logarithmic recurrences to compare the asserted finite-prefactor formula at generations 100, 160 and 230 for three parameter sets, including cases with herbivore biomass below ordinary floating-point underflow. Expected terminal line: `VERIFY_OK`. This reproduces *finite arithmetic consistency only*; the uniform-contraction and weighted-series arguments above establish the infinite-time theorem.

## Relationship to prior work

Bešo, Kalabušić and Pilav [1, normalized model (5), §3.1, Lemmas 3.1–3.4] establish extinction basins and local stability, but do not give the explicit two-scale asymptotic with positive prefactors or the first-threshold clock distinction. Their model has two species sharing growth biomass after plant growth. Chow and Jang [2, model (2.2), §§2–3] analyze a closely related earlier strong-Allee *host–parasitoid* map, but the parasitoid there attacks before growth and follows a different update; their results classify extinction and stability, not the present rate-and-prefactor theorem. The non-Allee plant-herbivore map of Kang, Armbruster and Kuang [3] has \(f(0)>1\), so the low-density contraction hypothesis underpinning (1) is inapplicable to its extinction-origin regime.

The novelty claim is restricted to the precise joint asymptotic constants and quadratic-rate/detection-time law on the extinction basin, not to extinction itself, to the existence of strong Allee effects, or to the general facts of local stability.

## Limitations

The theorem is conditional on convergence to extinction outside the explicit \(0<x_0<b\) basin. It does not classify all global attractors, other basins, noisy finite populations, stochastic hitting times, or effects of spatial dispersal. Coordinate-axis solutions and the critical case \(f(0)=1\) require different asymptotics. The positive constants \(C,D\) depend on the complete orbit, and their defining series do not generally simplify to elementary parameter-only formulas. Existing analogous theorems for other ecological maps may remain unindexed; the exact same-map literature comparison is limited to the inspected sources and searches.

## References

[1] E. Bešo, S. Kalabušić and E. Pilav, *Dynamics of a plant-herbivore system with Ricker plant growth and the strong Allee effects on plant population*, Discrete and Continuous Dynamical Systems B 29 (2024), 627–665, DOI: 10.3934/dcdsb.2023108. First public online access June 9, 2023. Full author-uploaded article text: https://www.researchgate.net/publication/371538305_Dynamics_of_a_plant-herbivore_system_with_Ricker_plant_growth_and_the_strong_Allee_effects_on_plant_population; journal record: https://www.aimsciences.org/article/doi/10.3934/dcdsb.2023108.

[2] Y. Chow and S. R.-J. Jang, *Allee effects in a Ricker-type predator–prey system*, Journal of Difference Equations and Applications 20 (2014), 1350–1371, DOI: 10.1080/10236198.2014.918966; preprint arXiv:1404.5555.

[3] Y. Kang, D. Armbruster and Y. Kuang, *Dynamics of a plant-herbivore model*, Journal of Biological Dynamics 2 (2008), 89–101, DOI: 10.1080/17513750801956313.
