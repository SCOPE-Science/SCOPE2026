# Reset-induced long-range correlation reversal in finite coalescing rings

## Finding
For every integer \(N\ge4\), consider coalescing continuous-time walkers on a cycle of \(N\) labeled sites. Every occupied site attempts a jump to each adjacent site at rate one, with immediate coalescence when the destination is occupied. An independent Poisson clock of rate \(r>0\) resets all sites to occupied. Let \(X_i\) be the indicator that site \(i\) is occupied in the unique stationary law. For any two **nonadjacent** distinct sites \(i,j\),
\[
\lim_{r\downarrow0}\operatorname{Cov}(X_i,X_j)=-\frac1{N^2},\qquad
\operatorname{Cov}(X_i,X_j)=\frac4{r^2}+O_N(r^{-3})\quad(r\to\infty).
\]
Therefore each nonadjacent pair changes covariance sign at least once as the common reset rate increases.

For the smallest eligible cycle, \(N=4\), write \(D(r)=r^2+8r+8\). The **nearest-neighbor** and **opposite-site** stationary covariances have the exact formulas
\[
C_{\mathrm{near}}(r)=-\frac{64}{(r+4)^2D(r)^2}<0,
\]
\[
C_{\mathrm{opp}}(r)=\frac{4\left(r^5+16r^4+88r^3+192r^2+112r-128\right)}{(r+4)^2(r+8)D(r)^2}.
\]
The opposite-site covariance changes sign exactly once, at the unique positive root \(r_\star\approx0.530754559718673\) of its numerator polynomial. Consequently, **for \(r>r_\star\), opposite sites are positively correlated while neighboring sites are negatively correlated**.

## Assumptions and scope
The cycle \(C_N\) has \(N\ge4\) vertices and unoriented nearest-neighbor edges. Every **oriented** edge with an occupied departure site has its own rate-one jump clock; a jump onto an occupied vertex removes the departing particle and leaves precisely one at the arrival vertex. There is no spontaneous death, birth between resets, or particle exclusion without coalescence. A single global rate-\(r\) Poisson process resets the **entire** configuration to full occupancy. We study the nonempty finite state space and all real \(r>0\). Rates are normalized to one per oriented jump, rather than one per undirected bond.

## Proof
**1. Stationary age mixture.** Let \(P_t\) be the semigroup without resets and let \(\eta_*\) denote full occupancy. Because a rate-\(r\) reset clock erases history, the stationary distribution is the resolvent mixture
\[
\pi_{N,r}=r\int_0^\infty e^{-rt}\,P_t(\eta_*,\cdot)\,dt.
\]
This is the unique stationary law: the full configuration is reached from every state at the first reset; all reachable states then lie in the unique recurrent class. Expectations of bounded observables are analytic in \(r>0\) by the finite-state resolvent formula.

**2. Rare resets.** Without resets the number of particles never increases and, on the finite connected cycle, eventually reaches one almost surely. In the one-particle sector the walker moves symmetrically and its distribution tends to uniform on the \(N\) sites. Therefore \(P_t(\eta_*,\cdot)\) converges to the uniform singleton law. Taking the Abel limit of the age integral gives \(\pi_{N,r}\to\pi_{N,0}\) as \(r\downarrow0\), where \(\pi_{N,0}\) is uniform on singleton configurations. For \(i\ne j\), \(\mathbb E X_i=1/N\) and \(\mathbb E(X_iX_j)=0\), giving \(-1/N^2\).

**3. Frequent resets.** Let \(V_i=1-X_i\) be the vacancy indicator. In the no-reset dynamics started from full occupancy, a vacancy at a particular site \(i\) can be created by either of its two outgoing arrows in one jump. Thus \(\mathbb P(V_i(t)=1)=2t+O_N(t^2)\). For nonadjacent \(i,j\), reaching vacancies at both sites requires at least two jumps. There are precisely eight ordered two-jump sequences which vacate both, namely two choices of arrow at \(i\), two at \(j\), and either temporal order. None of these jumps refills the other site because \(i,j\) are not neighbors; the corresponding Taylor coefficient is \(8t^2/2=4t^2\). Hence \(\mathbb P(V_i(t)=V_j(t)=1)=4t^2+O_N(t^3)\). Averaging over an exponential age of mean \(1/r\) yields
\[
\mathbb EV_i=\frac2r+O_N(r^{-2}),\qquad
\mathbb E(V_iV_j)=\frac8{r^2}+O_N(r^{-3}).
\]
Because \(\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(V_i,V_j)\), subtraction proves \(4r^{-2}+O_N(r^{-3})\), strictly positive for sufficiently large \(r\). Continuity together with step 2 proves at least one zero for every nonadjacent pair.

**4. Exact four-cycle stationary law.** The \(15\) nonempty configurations on the four-cycle split under dihedral symmetry into the full state \(F\), four states with three particles \(T\), four adjacent-pair states \(A\), two opposite-pair states \(O\), and four singleton states \(S\). Let \(f,t,a,o,s\) be the **total** probability masses of these five orbits. Elementary jump counting gives
\[
(r+8)f=r,\quad (r+4)t=8f,\quad (r+4)a=2t+4o,\quad
(r+4)o=2t+2a,\quad rs=2a.
\]
These balances sum to normalization; transitions within an orbit do not affect its total mass. The unique solution is
\[
f=\frac r{r+8},\quad t=\frac{8r}{(r+4)(r+8)},\quad
 a=\frac{16r}{(r+4)D(r)},\quad
 o=\frac{16r(r+6)}{(r+4)(r+8)D(r)},\quad
 s=\frac{32}{(r+4)D(r)}.
\]
The single-site mean is
\[
m=f+\frac34t+\frac12(a+o)+\frac14s
=\frac{r^3+10r^2+24r+8}{(r+4)D(r)}.
\]
For an adjacent pair, the joint occupied probability equals \(f+t/2+a/4\); for an opposite pair it equals \(f+t/2+o/2\). Subtracting \(m^2\) and reducing gives the two rational formulas in the finding. The polynomial \(p(r)=r^5+16r^4+88r^3+192r^2+112r-128\) satisfies \(p(0)=-128\), tends to infinity and has \(p'(r)>0\) for every \(r>0\). Consequently it has exactly one positive root, with the stated sign transition.

## Verification
A standalone `check.py` independently constructs the 15-state continuous-time generator, checks **every individual stationary balance equation** symbolically against the orbit formula, reproduces the covariance expressions, verifies their limits and the unique-root criterion, and solves additional finite-size stationary generators numerically for cycles of 4–7 vertices and four positive reset rates. Execution requires Python 3, SymPy, NumPy, and SciPy. The exact proof above, rather than the finite experiments, establishes the assertions for all finite \(N\).

## Relationship to prior work
Durang, Henkel, and Park (2013) introduced coagulation–diffusion with stochastic resetting and obtained exact density, empty-interval, and interparticle-distance results, principally on an infinite chain. The present statement concerns the **spatial covariance of two separated occupied sites on finite cycles**, the sign change for every nonadjacent pair, and the exact four-cycle mixed-sign threshold; single contiguous empty-interval probabilities do not immediately specify two separated-site occupancy covariances. Durang, Fortin, and Henkel (2010) studied two-time correlations for coagulation–diffusion **without** global resetting. General resetting-induced correlations in different, non-coalescing quantum models also do not imply the classical cycle formulas here. The elementary resolvent identity and coalescence dynamics are precedents, not themselves claimed as new.

## Limitations
For cycles larger than four, existence but not uniqueness of the sign crossover is proved. The all-size high-reset law is asymptotic, not an exact finite-rate covariance formula. Exact nearest-neighbor negativity is asserted only for the four-cycle; no general theorem of negative association is claimed. Site-dependent jump rates, non-global resets, infinite volume and time-dependent reset hazards are outside scope. Bibliographic overlap with additional finite-ring multi-interval correlation literature cannot be fully excluded without an independent survey; no independent audit has been performed.

## References
1. X. Durang, M. Henkel, H. Park, Statistical mechanics of the coagulation-diffusion process with a stochastic reset, arXiv:1309.2107v1 (2013-09-09), https://arxiv.org/abs/1309.2107.
2. X. Durang, J.-Y. Fortin, M. Henkel, Exact two-time correlation and response functions in the one-dimensional coagulation-diffusion process by the empty-interval-particle method, arXiv:1012.4724 (2010), https://arxiv.org/abs/1012.4724.
3. M. Magoni, F. Carollo, G. Perfetto, I. Lesanovsky, Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting, arXiv:2202.12655 (2022), https://arxiv.org/abs/2202.12655.
