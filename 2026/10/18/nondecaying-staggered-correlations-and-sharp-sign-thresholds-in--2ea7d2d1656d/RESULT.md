# Nondecaying staggered correlations and sharp sign thresholds in a globally reset voter chain

## Finding
Consider the nearest-neighbor voter process on the integer lattice: every site, at rate one, copies the spin of a uniformly chosen neighbor. Independently, a *single system-wide* Poisson clock of rate \(r>0\) simultaneously resets every spin to the fixed checkerboard configuration \(\eta_i=(-1)^i\). Spins take values \(\sigma_i\in\{-1,+1\}\). Write \(\operatorname{Cov}_r\) for covariance in the unique invariant probability measure and put
\[
q=\frac{2+r-\sqrt{r(r+4)}}{2}\in(0,1).
\]
For every integer \(i\) and every separation \(d\ge1\), the stationary one-point and connected two-point functions are exactly
\[
\mathbb E_r[\sigma_i]=(-1)^i\frac r{r+2},\qquad
\boxed{\operatorname{Cov}_r(\sigma_i,\sigma_{i+d})
=\frac4{r+4}\left[q^d+(-1)^d\frac r{(r+2)^2}\right].}
\]
In particular, the connected correlation **does not decay to zero** at large distance: along even or odd separations,
\[
\operatorname{Cov}_r(\sigma_i,\sigma_{i+d})
=(-1)^d\frac{4r}{(r+4)(r+2)^2}+O_r(q^d).
\]
All even-distance covariances and all nearest-neighbor covariances are strictly positive. For every odd separation \(d=2k+1\ge3\), there is exactly one critical reset rate \(r_k>0\): covariance is positive for \(0<r<r_k\), zero at \(r=r_k\), and negative for \(r>r_k\). The exact threshold is
\[
q_k^k(1+q_k^2)+q_k-1=0,\quad 0<q_k<1,\qquad
r_k=\frac{(1-q_k)^2}{q_k}.
\]
These critical rates strictly decrease with \(k\), and
\[
r_k\sim \frac{W(2k)^2}{k^2}\quad(k\to\infty),
\]
where \(W\) is the positive Lambert function satisfying \(W(z)e^{W(z)}=z\). For example, at separation three, \(r_1\approx0.658967081916968\).

The same model on the finite even cycle \(C_N\), for every even \(N\ge4\), has an exact finite-volume covariance at separation \(1\le d<N\):
\[
\boxed{\operatorname{Cov}_{r,N}(\sigma_i,\sigma_{i+d})
=\frac4{r+4}\left[\frac{q^d+q^{N-d}}{1+q^N}+(-1)^d\frac r{(r+2)^2}\right].}
\]
Its fixed-separation infinite-volume limit is the formula above. This finite-cycle identity is part of the theorem; the unique-threshold statement is asserted for the integer lattice.

## Assumptions and scope
The model uses continuous physical time. Each spin copies its left neighbor at rate \(1/2\) and its right neighbor at rate \(1/2\); the total copy-event rate is one per site, including events that leave a spin unchanged. Reset events are *global*, not independent site-by-site resets, and restore the same deterministic checkerboard state on every occasion. The reset clock is independent of all copy clocks. For the cycle, \(N\) must be even so this reference configuration is compatible with periodicity. All results hold for every real \(r>0\), without a small- or large-rate approximation.

The process exists on the countable product state space by the usual graphical construction between reset times and has the invariant renewal measure
\[
\mu_r=\int_0^\infty r e^{-rt}\,\delta_\eta P_t\,dt,
\]
where \(P_t\) is the voter semigroup without resetting. A common reset couples any two copies, so the stationary law is unique; its convergence for bounded cylinder observables is at least exponentially fast with rate \(r\). The finite-cycle version has the analogous renewal representation.

## Proof
**1. Uniqueness and one-point functions.** Construct all spin-copy arrows and the single independent reset clock on a common probability space. Two trajectories with arbitrary initial states are identical after their first common reset and hence remain identical. The renewal measure above is invariant and the coupling proves uniqueness. Symmetry under translation by two sites and under translation by one followed by a global spin reversal forces \(\mathbb E_r\sigma_i=(-1)^i m\). The stationary generator equation for \(\sigma_i\) is
\[
0=\tfrac12(\mathbb E_r\sigma_{i-1}+\mathbb E_r\sigma_{i+1})
-\mathbb E_r\sigma_i+r(\eta_i-\mathbb E_r\sigma_i).
\]
Substitution gives \(0=-(r+2)m+r\), hence \(m=r/(r+2)\). The same argument holds on every even cycle.

**2. Two-point recurrence.** Let \(C_d=\mathbb E_r[\sigma_i\sigma_{i+d}]\). The combined translation/spin-reversal symmetry makes \(C_d\) independent of \(i\), and \(C_0=1\). Acting with the two local copy generators on distinct spins and then accounting for a simultaneous reset gives, for every \(d\ge1\),
\[
0=C_{d-1}+C_{d+1}-(2+r)C_d+r(-1)^d.
\]
At \(d=1\), the value \(C_0=1\) is correctly included: replacing a spin by its neighbor makes the two-spin product exactly one. The recurrence is therefore valid without any independence assumption. Its bounded solution on the integer half-line is unique. Since \(q+q^{-1}=2+r\), the alternating particular solution is \(r(-1)^d/(r+4)\) and the decaying homogeneous solution is proportional to \(q^d\). The boundary condition \(C_0=1\) fixes the proportionality constant, proving
\[
C_d=\frac r{r+4}(-1)^d+\frac4{r+4}q^d.
\]
The other characteristic root \(q^{-1}>1\) is excluded by boundedness of correlations.

On an even cycle, impose \(C_0=C_N=1\) and \(C_d=C_{N-d}\). The identical recurrence for \(1\le d<N\) then has the unique solution
\[
C_{d,N}=\frac r{r+4}(-1)^d+\frac4{r+4}
\frac{q^d+q^{N-d}}{1+q^N}.
\]
Subtracting the product of the one-point means yields both boxed covariance formulas because the elementary identity
\[
\frac r{r+4}-\frac{r^2}{(r+2)^2}
=\frac{4r}{(r+4)(r+2)^2}
\]
holds at every positive \(r\).

**3. Exact signs and thresholds.** For even \(d\), both terms in the bracket of the integer-lattice covariance are positive. For \(d=1\), the bracket is \(q-r/(r+2)^2\). Using \(r=(1-q)^2/q\) and \(r+2=(1+q^2)/q\) gives
\[
q-\frac r{(r+2)^2}
=q\left[1-\frac{(1-q)^2}{(1+q^2)^2}\right]>0.
\]
For \(d=2k+1\ge3\), the covariance has the sign of
\[
q^{2k+1}-\frac{q(1-q)^2}{(1+q^2)^2},
\]
equivalently the sign of \(F_k(q)=q^k(1+q^2)+q-1\). The function \(F_k\) is strictly increasing on \((0,1)\), with \(F_k(0)=-1\) and \(F_k(1)=2\); therefore it has exactly one root \(q_k\). The map \(q\mapsto(1-q)^2/q\) is strictly decreasing, so the signs reverse once, with positive covariance below the reset-rate threshold and negative above it. Since \(F_{k+1}(q)<F_k(q)\) for \(0<q<1\), one has \(q_{k+1}>q_k\) and hence \(r_{k+1}<r_k\).

For asymptotics put \(\epsilon_k=1-q_k\). The threshold equation becomes
\[
\epsilon_k=(1-\epsilon_k)^k(2-2\epsilon_k+\epsilon_k^2).
\]
It follows that \(\epsilon_k\to0\), and \(\epsilon_k\le2e^{-k\epsilon_k}\), hence \(k\epsilon_k\le W(2k)=O(\log k)\). Consequently \(k\epsilon_k^2\to0\). Taking logarithms of the exact threshold equation gives
\[
\log\epsilon_k=-k\epsilon_k+\log2+o(1),\qquad
(k\epsilon_k)e^{k\epsilon_k}=2k(1+o(1)).
\]
Thus \(k\epsilon_k=W(2k)+o(1)\), and \(r_k=\epsilon_k^2/(1-\epsilon_k)\sim W(2k)^2/k^2\).

**4. Nondecaying staggered covariance.** Taking \(d\to\infty\) in the exact formula removes only \(q^d\), leaving the stated alternating constant. This term has a direct probabilistic interpretation: at stationarity the elapsed time since the most recent global reset is a *common* random variable \(A\sim\operatorname{Exp}(r)\). Conditional on \(A\), the single-spin mean is \((-1)^i e^{-2A}\). The covariance of these conditional means is \((-1)^d\operatorname{Var}(e^{-2A})\), where
\[
\operatorname{Var}(e^{-2A})=\frac r{r+4}-\left(\frac r{r+2}\right)^2
=\frac{4r}{(r+4)(r+2)^2}.
\]
This identifies the persistent long-distance signal with the shared reset age rather than with an ordinary finite-range pair interaction.

## Verification
The standalone script `verify_voter_reset.py` reconstructs the finite-state continuous-time Markov generator directly from its copy and reset transitions. It solves stationary balance equations on even rings of sizes \(4,6,8,10\) at five independent positive reset rates, checking all one- and two-point predictions. It separately checks \(1{,}500\) infinite recurrence identities, \(80\) signs on opposite sides of the threshold equations, and three large-distance Lambert-function comparisons. All checks passed. The generator test is independent of the closed-form recurrence derivation. Neither finite-state enumeration nor numerical root solving is used as a proof of the infinite theorem.

Run with Python 3, NumPy, and SciPy: `python verify_voter_reset.py`.

## Relationship to prior work
The classical voter model and coarsening behavior are analyzed by Ben-Naim, Frachebourg, and Krapivsky (1995 preprint). Evans and Majumdar (2011) established the modern stochastic-resetting paradigm for single-particle diffusion. Magoni, Majumdar, and Schehr (2020) applied **global** resetting to Glauber-Ising dynamics, deriving magnetization-distribution results and explicitly identifying two-point correlation structure as a further question. Grange (2022, revised 2023) studied voter correlations with **independent local** resets; its resetting mechanism and stationary two-point equations are different. The 2023 interacting-particle resetting review describes global and local mechanisms separately. The present theorem concerns a deterministic checkerboard reference configuration, gives exact connected correlations under a common global reset clock, and proves distance-dependent sign thresholds; these statements are not implied by the cited results in the passages and full texts examined.

## Limitations
The result is specific to one-dimensional unbiased nearest-neighbor voter copying, exponential global resets, and a checkerboard reset state; it does not establish analogous formulas for finite-temperature Ising dynamics, independent site resets, arbitrary reset patterns, or higher-dimensional systems. Only one- and two-point observables, not the full stationary distribution in closed finite-dimensional form, are characterized. The universal sign-threshold classification applies on the integer lattice; the finite-ring formula is exact, but no all-size uniqueness statement for finite-ring correlation zeros is asserted. The result is not a claim about thermodynamic equilibrium or a genuine temperature-driven phase transition. Distinct sublattice-distance and low-reset limits do not commute. Bibliographic coverage is limited to the identified sources and searches; a specialized unpublished or unindexed global-reset correlation calculation could overlap.

## References
1. E. Ben-Naim, L. Frachebourg, P. L. Krapivsky, *Coarsening and persistence in the voter model*, arXiv:cond-mat/9511040 (first posted 1995-11-08); Phys. Rev. E **53**, 3078 (1996). https://arxiv.org/abs/cond-mat/9511040
2. M. R. Evans, S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first posted 2011-02-14); Phys. Rev. Lett. **106**, 160601 (2011). https://arxiv.org/abs/1102.2704
3. M. Magoni, S. N. Majumdar, G. Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (first posted 2020-02-12); Phys. Rev. Research **2**, 033182 (2020). https://arxiv.org/html/2002.04867v1
4. P. Grange, *Voter model under stochastic resetting*, arXiv:2207.08590 (first posted 2022-07-18). https://arxiv.org/html/2207.08590v6
5. A. Nagar, S. Gupta, *Stochastic resetting in interacting particle systems: a review*, arXiv:2305.16955 (2023). https://arxiv.org/html/2305.16955v2
